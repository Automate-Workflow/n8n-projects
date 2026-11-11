#!/usr/bin/env python3
"""Check HTTP reachability of URLs listed in data/n8n_list.csv with retries and timeouts."""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import datetime
import json
import ssl
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_csv import configure_utf8_stdio, load_csv_rows  # noqa: E402

USER_AGENT = (
    "AutomateWorkflow-n8n-projects-link-checker/1.0 "
    "(+https://github.com/Automate-Workflow/n8n-projects)"
)

FALLBACK_STATUSES = {400, 403, 405, 429, 500, 501, 502, 503, 504}
TRANSIENT_STATUSES = {429, 500, 502, 503, 504}


@dataclass
class LinkCheckResult:
    """Result record for a single checked URL."""

    url: str
    project_ids: list[int]
    status_class: str
    http_code: int | None
    method_used: str
    final_url: str
    attempts: int
    elapsed_ms: int
    detail: str


def _perform_request(
    url: str,
    method: str,
    timeout: float,
    context: ssl.SSLContext,
) -> tuple[int, str]:
    """Execute one HTTP request and return (status_code, final_url)."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-2047"

    request = urllib.request.Request(url, method=method, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
        if method == "GET":
            response.read(2048)
        status = getattr(response, "status", None) or response.getcode()
        return int(status), response.geturl()


def check_single_url(
    url: str,
    project_ids: list[int],
    timeout: float,
    retries: int,
    base_delay: float,
) -> LinkCheckResult:
    """Check one URL using HEAD with GET fallback and exponential backoff retries."""
    context = ssl.create_default_context()
    start_time = time.monotonic()
    last_code: int | None = None
    last_method = "HEAD"
    last_detail = ""
    final_url = url

    for attempt in range(1, retries + 1):
        methods = ("HEAD", "GET") if attempt == 1 else ("GET",)
        should_retry = False

        for method in methods:
            last_method = method
            try:
                code, resolved = _perform_request(url, method, timeout, context)
                elapsed_ms = int((time.monotonic() - start_time) * 1000)
                status_class = "REDIRECTED" if resolved != url else "OK"
                return LinkCheckResult(
                    url=url,
                    project_ids=project_ids,
                    status_class=status_class,
                    http_code=code,
                    method_used=method,
                    final_url=resolved,
                    attempts=attempt,
                    elapsed_ms=elapsed_ms,
                    detail="Reachable",
                )
            except urllib.error.HTTPError as exc:
                last_code = int(exc.code)
                final_url = exc.geturl() or url
                last_detail = f"HTTP {exc.code}: {exc.reason}"
                if method == "HEAD" and exc.code in FALLBACK_STATUSES:
                    continue
                if exc.code in (404, 410):
                    elapsed_ms = int((time.monotonic() - start_time) * 1000)
                    return LinkCheckResult(
                        url=url,
                        project_ids=project_ids,
                        status_class="BROKEN",
                        http_code=last_code,
                        method_used=method,
                        final_url=final_url,
                        attempts=attempt,
                        elapsed_ms=elapsed_ms,
                        detail=last_detail,
                    )
                if exc.code in TRANSIENT_STATUSES:
                    should_retry = True
                    break
                # 403/401/other 4xx often indicate bot filtering; classify as WARN
                elapsed_ms = int((time.monotonic() - start_time) * 1000)
                return LinkCheckResult(
                    url=url,
                    project_ids=project_ids,
                    status_class="WARN",
                    http_code=last_code,
                    method_used=method,
                    final_url=final_url,
                    attempts=attempt,
                    elapsed_ms=elapsed_ms,
                    detail=last_detail,
                )
            except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError) as exc:
                last_code = None
                last_detail = f"{type(exc).__name__}: {exc}"
                if method == "HEAD":
                    continue
                should_retry = True

        if should_retry and attempt < retries:
            time.sleep(base_delay * (2 ** (attempt - 1)))
        elif not should_retry:
            break

    elapsed_ms = int((time.monotonic() - start_time) * 1000)
    return LinkCheckResult(
        url=url,
        project_ids=project_ids,
        status_class="WARN",
        http_code=last_code,
        method_used=last_method,
        final_url=final_url,
        attempts=retries,
        elapsed_ms=elapsed_ms,
        detail=last_detail or "Transient network or host error",
    )


def render_markdown_report(
    results: list[LinkCheckResult],
    total_rows: int,
    checked_at: str,
) -> str:
    """Format link check results into a Markdown report."""
    counts: dict[str, int] = {"OK": 0, "REDIRECTED": 0, "WARN": 0, "BROKEN": 0}
    for res in results:
        counts[res.status_class] = counts.get(res.status_class, 0) + 1

    lines = [
        "# Link Check Report",
        "",
        f"- **Checked (UTC)**: {checked_at}",
        f"- **Total CSV rows**: {total_rows}",
        f"- **Unique URLs checked**: {len(results)}",
        f"- **OK**: {counts['OK']}",
        f"- **Redirected**: {counts['REDIRECTED']}",
        f"- **Warnings (rate limit / bot filter / transient host error)**: {counts['WARN']}",
        f"- **Broken (404 / 410)**: {counts['BROKEN']}",
        "",
    ]

    attention = [r for r in results if r.status_class in {"BROKEN", "WARN", "REDIRECTED"}]
    if attention:
        lines.extend(
            [
                "## URLs Requiring Attention or Redirected",
                "",
                "| Status | HTTP | Project IDs | URL | Detail |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for res in attention:
            ids_text = ", ".join(str(pid) for pid in res.project_ids)
            code_text = str(res.http_code) if res.http_code is not None else "N/A"
            detail = res.detail.replace("|", "\\|")
            lines.append(
                f"| {res.status_class} | {code_text} | {ids_text} | {res.url} | {detail} |"
            )
        lines.append("")

    lines.extend(
        [
            "## All Checked URLs",
            "",
            "| Status | HTTP | Method | Latency (ms) | Project IDs | URL |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for res in results:
        ids_text = ", ".join(str(pid) for pid in res.project_ids)
        code_text = str(res.http_code) if res.http_code is not None else "N/A"
        lines.append(
            f"| {res.status_class} | {code_text} | {res.method_used} | {res.elapsed_ms} | {ids_text} | {res.url} |"
        )
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Verify HTTP reachability of URLs in data/n8n_list.csv."
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=repo_root / "data" / "n8n_list.csv",
        help="Path to the CSV file (default: data/n8n_list.csv).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root / "reports" / "link-check-report.md",
        help="Markdown report output path (default: reports/link-check-report.md).",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        default=None,
        help="Optional JSON report output path.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=15.0,
        help="Per-request timeout in seconds (default: 15.0).",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Max attempts per URL (default: 3).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Base delay in seconds for exponential backoff (default: 1.0).",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=6,
        help="Concurrent worker threads (default: 6).",
    )
    parser.add_argument(
        "--fail-on-broken",
        action="store_true",
        help="Exit with code 1 if any URL returns HTTP 404 or 410.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Entry point for CLI execution."""
    configure_utf8_stdio()
    args = parse_args(argv)

    if not args.csv.is_file():
        print(f"ERROR: CSV file not found: {args.csv}", file=sys.stderr)
        return 2

    try:
        _, rows, _ = load_csv_rows(args.csv)
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        print(f"ERROR: Failed to read {args.csv}: {exc}", file=sys.stderr)
        return 2

    url_map: dict[str, list[int]] = {}
    for row in rows:
        url = row.get("url", "").strip()
        pid = int(row.get("id", "0").strip() or 0)
        if url:
            url_map.setdefault(url, []).append(pid)

    results: list[LinkCheckResult] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        future_map = {
            pool.submit(
                check_single_url,
                url,
                sorted(ids),
                args.timeout,
                max(1, args.retries),
                args.delay,
            ): url
            for url, ids in url_map.items()
        }
        for future in concurrent.futures.as_completed(future_map):
            results.append(future.result())

    results.sort(key=lambda r: (r.project_ids[0] if r.project_ids else 0, r.url))
    checked_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    report_md = render_markdown_report(results, total_rows=len(rows), checked_at=checked_at)

    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(report_md)

        if args.json_output is not None:
            args.json_output.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "checked_at": checked_at,
                "total_rows": len(rows),
                "unique_urls": len(results),
                "results": [asdict(r) for r in results],
            }
            with args.json_output.open("w", encoding="utf-8", newline="\n") as handle:
                json.dump(payload, handle, indent=2)
                handle.write("\n")
    except OSError as exc:
        print(f"ERROR: Failed to write report: {exc}", file=sys.stderr)
        return 2

    ok_count = sum(1 for r in results if r.status_class == "OK")
    redirect_count = sum(1 for r in results if r.status_class == "REDIRECTED")
    warn_count = sum(1 for r in results if r.status_class == "WARN")
    broken_count = sum(1 for r in results if r.status_class == "BROKEN")

    print(
        f"Link check complete ({len(results)} unique URLs across {len(rows)} rows): "
        f"OK={ok_count}, REDIRECTED={redirect_count}, WARN={warn_count}, BROKEN={broken_count}."
    )
    print(f"Report written to {args.output}")

    if args.fail_on_broken and broken_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
