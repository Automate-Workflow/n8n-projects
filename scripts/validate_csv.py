#!/usr/bin/env python3
"""Validate data/n8n_list.csv against the repository schema and URL rules."""

from __future__ import annotations

import argparse
import csv
import datetime
import sys
import urllib.parse
from pathlib import Path

EXPECTED_COLUMNS: tuple[str, ...] = (
    "id",
    "title",
    "category",
    "difficulty",
    "learning_phase",
    "tools_and_skills",
    "description",
    "source_type",
    "url",
    "notes",
    "verified_date",
    "status",
)

REQUIRED_COLUMNS: tuple[str, ...] = (
    "id",
    "title",
    "category",
    "difficulty",
    "learning_phase",
    "tools_and_skills",
    "description",
    "source_type",
    "url",
    "verified_date",
    "status",
)

CATEGORY_SPECS: tuple[tuple[str, str], ...] = (
    ("WhatsApp", "whatsapp"),
    ("LinkedIn", "linkedin"),
    ("Resume/HR", "resume-hr"),
    ("Text/Classification", "text-classification"),
    ("Voice", "voice"),
    ("Image", "image"),
    ("Computer Vision", "computer-vision"),
    ("Video", "video"),
    ("Paper", "paper"),
)

CATEGORY_TO_SLUG: dict[str, str] = dict(CATEGORY_SPECS)

ALLOWED_DIFFICULTIES: tuple[str, ...] = (
    "Beginner",
    "Intermediate",
    "Advanced",
)

ALLOWED_PHASES: tuple[str, ...] = (
    "Phase 1 - Foundations",
    "Phase 2 - Chatbots and Voice",
    "Phase 3 - Documents, Vision and Data",
    "Phase 4 - Advanced Agents and Integrations",
)

ALLOWED_SOURCE_TYPES: tuple[str, ...] = (
    "GitHub file",
    "GitHub folder",
    "GitHub repo",
    "GitHub profile (pinned repo)",
    "n8n.io template",
)


def configure_utf8_stdio() -> None:
    """Ensure stdout and stderr handle UTF-8 cleanly on Windows consoles."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


def contains_emoji(text: str) -> bool:
    """Return True if text contains common Unicode emoji or pictograph codepoints."""
    for ch in text:
        cp = ord(ch)
        if (
            0x1F300 <= cp <= 0x1FAFF
            or 0x2600 <= cp <= 0x27BF
            or cp == 0xFE0F
            or cp == 0x200D
        ):
            return True
    return False


def is_valid_http_url(url: str) -> bool:
    """Return True when url is a well-formed HTTP/HTTPS URL with no whitespace."""
    if not url or any(ch.isspace() for ch in url):
        return False
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    if not parsed.netloc or "." not in parsed.netloc:
        return False
    return True


def load_csv_rows(csv_path: Path) -> tuple[list[str], list[dict[str, str]], bool]:
    """Read CSV rows using utf-8-sig and return (fieldnames, rows, has_bom)."""
    raw_head = csv_path.read_bytes()[:3]
    has_bom = raw_head == b"\xef\xbb\xbf"
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = [dict(row) for row in reader]
    return fieldnames, rows, has_bom


def validate_rows(
    fieldnames: list[str],
    rows: list[dict[str, str]],
    has_bom: bool = True,
    expected_count: int | None = None,
) -> tuple[list[str], list[str]]:
    """Validate CSV headers, rows, IDs, enums, dates, and URLs."""
    errors: list[str] = []
    warnings: list[str] = []

    if not has_bom:
        warnings.append("CSV file does not begin with a UTF-8 BOM (utf-8-sig recommended).")

    if tuple(fieldnames) != EXPECTED_COLUMNS:
        errors.append(
            f"Header mismatch. Expected {list(EXPECTED_COLUMNS)}, found {fieldnames}."
        )
        return errors, warnings

    if not rows:
        errors.append("CSV contains zero data rows.")
        return errors, warnings

    if expected_count is not None and len(rows) != expected_count:
        errors.append(
            f"Expected {expected_count} data rows, found {len(rows)}."
        )

    seen_ids: set[int] = set()
    parsed_ids: list[int] = []
    id_to_row: dict[int, dict[str, str]] = {}
    url_to_ids: dict[str, list[int]] = {}

    for index, row in enumerate(rows, start=1):
        if None in row:
            errors.append(f"Row {index}: extra unmapped columns found: {row[None]!r}.")
        if any(value is None for key, value in row.items() if key is not None):
            errors.append(f"Row {index}: missing columns detected (row shorter than header).")
            continue

        for col in REQUIRED_COLUMNS:
            if not row.get(col, "").strip():
                errors.append(f"Row {index}: required column '{col}' is empty.")

        raw_id = row.get("id", "").strip()
        row_id: int | None = None
        if raw_id:
            try:
                row_id = int(raw_id)
                if row_id <= 0:
                    errors.append(f"Row {index}: id must be positive, got {raw_id!r}.")
                elif row_id in seen_ids:
                    errors.append(f"Row {index}: duplicate id {row_id}.")
                else:
                    seen_ids.add(row_id)
                    parsed_ids.append(row_id)
                    id_to_row[row_id] = row
            except ValueError:
                errors.append(f"Row {index}: id must be an integer, got {raw_id!r}.")

        category = row.get("category", "").strip()
        if category and category not in CATEGORY_TO_SLUG:
            errors.append(
                f"Row {index} (id={raw_id}): invalid category {category!r}."
            )

        difficulty = row.get("difficulty", "").strip()
        if difficulty and difficulty not in ALLOWED_DIFFICULTIES:
            errors.append(
                f"Row {index} (id={raw_id}): invalid difficulty {difficulty!r}."
            )

        phase = row.get("learning_phase", "").strip()
        if phase and phase not in ALLOWED_PHASES:
            errors.append(
                f"Row {index} (id={raw_id}): invalid learning_phase {phase!r}."
            )

        source_type = row.get("source_type", "").strip()
        if source_type and source_type not in ALLOWED_SOURCE_TYPES:
            errors.append(
                f"Row {index} (id={raw_id}): invalid source_type {source_type!r}."
            )

        url = row.get("url", "").strip()
        if url and not is_valid_http_url(url):
            errors.append(f"Row {index} (id={raw_id}): invalid URL {url!r}.")
        elif url and row_id is not None:
            url_to_ids.setdefault(url, []).append(row_id)

        verified_date = row.get("verified_date", "").strip()
        if verified_date:
            try:
                datetime.date.fromisoformat(verified_date)
            except ValueError:
                errors.append(
                    f"Row {index} (id={raw_id}): verified_date must be YYYY-MM-DD, got {verified_date!r}."
                )

        for col, value in row.items():
            if col is None or col == "url":
                continue
            if contains_emoji(value):
                errors.append(
                    f"Row {index} (id={raw_id}): emoji character disallowed in '{col}'."
                )

    if parsed_ids and parsed_ids != list(range(1, len(parsed_ids) + 1)):
        warnings.append("IDs are not strictly sequential starting at 1.")

    for url, id_list in url_to_ids.items():
        if len(id_list) > 1:
            missing_hint = [
                pid
                for pid in id_list
                if "open the named workflow" not in id_to_row[pid].get("notes", "").lower()
                and "pinned repo" not in id_to_row[pid].get("notes", "").lower()
            ]
            if missing_hint:
                warnings.append(
                    f"Shared URL {url} used by IDs {id_list} without navigation hint in notes for IDs {missing_hint}."
                )

    return errors, warnings


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Validate data/n8n_list.csv schema, IDs, enums, dates, and URLs."
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=repo_root / "data" / "n8n_list.csv",
        help="Path to the CSV file (default: data/n8n_list.csv).",
    )
    parser.add_argument(
        "--expected-count",
        type=int,
        default=None,
        help="Optional exact number of rows expected.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as validation errors.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress summary output when validation succeeds.",
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
        fieldnames, rows, has_bom = load_csv_rows(args.csv)
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        print(f"ERROR: Failed to read {args.csv}: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate_rows(
        fieldnames=fieldnames,
        rows=rows,
        has_bom=has_bom,
        expected_count=args.expected_count,
    )

    for warning in warnings:
        prefix = "ERROR" if args.strict else "WARN"
        stream = sys.stderr if args.strict else sys.stdout
        print(f"{prefix}: {warning}", file=stream)

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors or (args.strict and warnings):
        print(
            f"Validation failed for {args.csv} ({len(errors)} error(s), {len(warnings)} warning(s)).",
            file=sys.stderr,
        )
        return 1

    if not args.quiet:
        categories = sorted({r["category"].strip() for r in rows})
        phases = sorted({r["learning_phase"].strip() for r in rows})
        print(
            f"OK: Validated {len(rows)} rows in {args.csv} across {len(categories)} categories and {len(phases)} phases."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
