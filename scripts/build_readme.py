#!/usr/bin/env python3
"""Generate CSV-driven sections in README.md, category pages, learning-path.md, and SVG badges."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_csv import (  # noqa: E402
    ALLOWED_DIFFICULTIES,
    ALLOWED_PHASES,
    CATEGORY_SPECS,
    CATEGORY_TO_SLUG,
    configure_utf8_stdio,
    load_csv_rows,
    validate_rows,
)

PHASE_DESCRIPTIONS: dict[str, str] = {
    "Phase 1 - Foundations": (
        "Start with single-trigger workflows connecting email, chat, spreadsheets, and "
        "storage with an LLM node to learn credentials, prompts, and structured routing."
    ),
    "Phase 2 - Chatbots and Voice": (
        "Progress to stateful conversational assistants over Telegram and WhatsApp, adding "
        "speech-to-text transcription, local models, and vector retrieval."
    ),
    "Phase 3 - Documents, Vision and Data": (
        "Build extraction pipelines for PDFs, resumes, forms, academic papers, and images "
        "using OCR, multimodal vision models, and structured output parsers."
    ),
    "Phase 4 - Advanced Agents and Integrations": (
        "Combine multi-agent tool calling, self-hosted APIs, MCP servers, and multi-step "
        "media orchestration for production-grade automation systems."
    ),
}

PHASE_ANCHORS: dict[str, str] = {
    "Phase 1 - Foundations": "phase-1---foundations",
    "Phase 2 - Chatbots and Voice": "phase-2---chatbots-and-voice",
    "Phase 3 - Documents, Vision and Data": "phase-3---documents-vision-and-data",
    "Phase 4 - Advanced Agents and Integrations": "phase-4---advanced-agents-and-integrations",
}

PHASE_BADGE_MAP: dict[str, str] = {
    "Phase 1 - Foundations": "phase-1.svg",
    "Phase 2 - Chatbots and Voice": "phase-2.svg",
    "Phase 3 - Documents, Vision and Data": "phase-3.svg",
    "Phase 4 - Advanced Agents and Integrations": "phase-4.svg",
}

DIFFICULTY_BADGE_MAP: dict[str, str] = {
    "Beginner": "difficulty-beginner.svg",
    "Intermediate": "difficulty-intermediate.svg",
    "Advanced": "difficulty-advanced.svg",
}

REPO_OWNER = "Automate-Workflow"
REPO_NAME = "n8n-projects"


def escape_md_cell(value: str) -> str:
    """Normalize whitespace and escape Markdown pipe characters for table cells."""
    cleaned = " ".join(value.split())
    return cleaned.replace("|", "\\|")


def format_tools(raw_tools: str) -> str:
    """Format semicolon-separated tools_and_skills cleanly for Markdown tables."""
    parts = [part.strip() for part in raw_tools.split(";") if part.strip()]
    return escape_md_cell(", ".join(parts))


def navigation_hint(row: dict[str, str]) -> str:
    """Return a visible navigation hint when a row points to a multi-workflow repo or profile."""
    notes_lower = row.get("notes", "").lower()
    desc = row.get("description", "")
    match = re.search(r"\(([^()]+\.json)\)", desc)
    filename_hint = f": `{match.group(1)}`" if match else ""

    if "open the named workflow" in notes_lower:
        return f" *(open the named workflow{filename_hint})*"
    if "pinned repo" in notes_lower or "profile page" in notes_lower:
        return " *(profile page: open the pinned repo)*"
    return ""


def sort_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Deterministically sort rows by canonical category order then numeric id."""
    cat_index = {name: idx for idx, (name, _) in enumerate(CATEGORY_SPECS)}

    def key_fn(row: dict[str, str]) -> tuple[int, str, int]:
        cat = row["category"].strip()
        return (
            cat_index.get(cat, len(CATEGORY_SPECS)),
            cat.lower(),
            int(row["id"].strip()),
        )

    return sorted(rows, key=key_fn)


def replace_marked_section(content: str, marker: str, body: str) -> str:
    """Replace content exclusively between <!-- MARKER:START --> and <!-- MARKER:END -->."""
    start_tag = f"<!-- {marker}:START -->"
    end_tag = f"<!-- {marker}:END -->"
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        raise ValueError(f"Missing or malformed marker pair {start_tag} / {end_tag}.")

    before = content[: start_idx + len(start_tag)]
    after = content[end_idx:]
    normalized_body = body.strip("\n")
    return f"{before}\n{normalized_body}\n{after}"


def build_shield_svg(
    title: str,
    desc: str,
    left_text: str,
    right_text: str,
    right_bg: str = "#B91C1C",
    right_fg: str = "#FFFFFF",
) -> str:
    """Build a crisp, theme-independent shields-style SVG badge."""
    left_w = max(54, len(left_text) * 7 + 16)
    right_w = max(36, len(right_text) * 7 + 16)
    total_w = left_w + right_w
    left_x = left_w / 2
    right_x = left_w + (right_w / 2)
    clip_id = re.sub(r"[^a-z0-9]+", "-", left_text.lower()).strip("-") or "badge"

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="20" '
        f'viewBox="0 0 {total_w} 20" role="img" aria-labelledby="badge-{clip_id}-title badge-{clip_id}-desc">\n'
        f'  <title id="badge-{clip_id}-title">{title}</title>\n'
        f'  <desc id="badge-{clip_id}-desc">{desc}</desc>\n'
        f'  <clipPath id="clip-{clip_id}">\n'
        f'    <rect width="{total_w}" height="20" rx="4" />\n'
        f'  </clipPath>\n'
        f'  <g clip-path="url(#clip-{clip_id})">\n'
        f'    <rect width="{left_w}" height="20" fill="#111827" />\n'
        f'    <rect x="{left_w}" width="{right_w}" height="20" fill="{right_bg}" />\n'
        f'  </g>\n'
        f'  <g font-family="Verdana, Geneva, DejaVu Sans, sans-serif" font-size="11" text-anchor="middle">\n'
        f'    <text x="{left_x:.1f}" y="14" fill="#FFFFFF">{left_text}</text>\n'
        f'    <text x="{right_x:.1f}" y="14" fill="{right_fg}" font-weight="700">{right_text}</text>\n'
        f'  </g>\n'
        f'</svg>\n'
    )


def render_readme_badges(rows: list[dict[str, str]]) -> str:
    """Render the centered badge strip for README.md."""
    project_count = len(rows)
    latest_date = max(r["verified_date"].strip() for r in rows)
    base_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}"

    return "\n".join(
        [
            '<p align="center">',
            '  <a href="LICENSE"><img src="assets/badges/license-mit.svg" alt="License: MIT" height="20" /></a>',
            f'  <a href="{base_url}/actions/workflows/validate.yml"><img src="{base_url}/actions/workflows/validate.yml/badge.svg" alt="Validate workflow status" height="20" /></a>',
            f'  <a href="{base_url}/actions/workflows/links.yml"><img src="{base_url}/actions/workflows/links.yml/badge.svg" alt="Link check workflow status" height="20" /></a>',
            f'  <a href="data/n8n_list.csv"><img src="assets/badges/projects-count.svg" alt="Projects: {project_count}" height="20" /></a>',
            f'  <a href="data/n8n_list.csv"><img src="assets/badges/last-updated.svg" alt="Last verified: {latest_date}" height="20" /></a>',
            "</p>",
        ]
    )


def render_categories_overview(rows: list[dict[str, str]]) -> str:
    """Render the category overview table for README.md."""
    by_cat: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_cat.setdefault(row["category"].strip(), []).append(row)

    lines = [
        "| Icon | Category | Projects | Difficulty Breakdown | Directory Section |",
        "| --- | --- | --- | --- | --- |",
    ]

    for category, slug in CATEGORY_SPECS:
        cat_rows = by_cat.get(category, [])
        if not cat_rows:
            continue
        diff_counts = Counter(r["difficulty"].strip() for r in cat_rows)
        diff_summary = ", ".join(
            f"{diff_counts[d]} {d}"
            for d in ALLOWED_DIFFICULTIES
            if diff_counts.get(d, 0) > 0
        )
        icon_html = (
            f'<img src="assets/icons/{slug}.svg" alt="{category} icon" width="28" height="28" />'
        )
        cat_link = f"[{category}](docs/categories/{slug}.md)"
        section_link = f"[Jump to {category}](#category-{slug})"
        lines.append(
            f"| {icon_html} | {cat_link} | {len(cat_rows)} | {diff_summary} | {section_link} |"
        )

    return "\n".join(lines)


def render_readme_learning_path(rows: list[dict[str, str]]) -> str:
    """Render the four-phase learning path summary for README.md."""
    by_phase: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_phase.setdefault(row["learning_phase"].strip(), []).append(row)

    blocks: list[str] = []
    for phase in ALLOWED_PHASES:
        phase_rows = sorted(
            by_phase.get(phase, []),
            key=lambda r: int(r["id"].strip()),
        )
        badge_file = PHASE_BADGE_MAP[phase]
        anchor = PHASE_ANCHORS[phase]
        id_links = ", ".join(
            f"[#{r['id'].strip()}]({r['url'].strip()})" for r in phase_rows
        )
        blocks.extend(
            [
                f'<p><img src="assets/badges/{badge_file}" alt="{phase}" height="20" /></p>',
                "",
                f"### [{phase}](docs/learning-path.md#{anchor})",
                "",
                PHASE_DESCRIPTIONS[phase],
                "",
                f"**Included projects ({len(phase_rows)}):** {id_links}",
                "",
            ]
        )

    return "\n".join(blocks).rstrip()


def render_readme_directory(rows: list[dict[str, str]]) -> str:
    """Render the full directory grouped by category for README.md."""
    by_cat: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_cat.setdefault(row["category"].strip(), []).append(row)

    sections: list[str] = []
    for category, slug in CATEGORY_SPECS:
        cat_rows = by_cat.get(category, [])
        if not cat_rows:
            continue

        sections.extend(
            [
                f'<h3><a id="category-{slug}"></a><img src="assets/icons/{slug}.svg" alt="{category} icon" width="28" height="28" align="absmiddle" /> {category} ({len(cat_rows)})</h3>',
                "",
                f"Category guide and risk notes: [docs/categories/{slug}.md](docs/categories/{slug}.md)",
                "",
                "| Title | Difficulty | Phase | Tools | Source type |",
                "| --- | --- | --- | --- | --- |",
            ]
        )

        for row in cat_rows:
            pid = row["id"].strip()
            title = escape_md_cell(row["title"].strip())
            url = row["url"].strip()
            hint = navigation_hint(row)
            title_cell = f"**#{pid}** [{title}]({url}){hint}"

            difficulty = row["difficulty"].strip()
            diff_badge = DIFFICULTY_BADGE_MAP[difficulty]
            diff_cell = (
                f'<img src="assets/badges/{diff_badge}" alt="{difficulty}" height="18" />'
            )

            phase = row["learning_phase"].strip()
            phase_short = phase.split(" - ", 1)[0]
            phase_anchor = PHASE_ANCHORS[phase]
            phase_cell = f"[{phase_short}](docs/learning-path.md#{phase_anchor})"

            tools_cell = format_tools(row["tools_and_skills"])
            source_cell = escape_md_cell(row["source_type"].strip())
            sections.append(
                f"| {title_cell} | {diff_cell} | {phase_cell} | {tools_cell} | {source_cell} |"
            )

        sections.append("")

    return "\n".join(sections).rstrip()


def render_category_meta(cat_rows: list[dict[str, str]]) -> str:
    """Render concise stats block for an individual category page."""
    diff_counts = Counter(r["difficulty"].strip() for r in cat_rows)
    diff_text = ", ".join(
        f"{diff_counts[d]} {d}"
        for d in ALLOWED_DIFFICULTIES
        if diff_counts.get(d, 0) > 0
    )
    phases = sorted(
        {r["learning_phase"].strip() for r in cat_rows},
        key=lambda p: ALLOWED_PHASES.index(p),
    )
    phase_text = ", ".join(phases)
    latest_date = max(r["verified_date"].strip() for r in cat_rows)
    return (
        f"- **Listed projects**: {len(cat_rows)}\n"
        f"- **Difficulty mix**: {diff_text}\n"
        f"- **Learning phases covered**: {phase_text}\n"
        f"- **Latest dataset check date**: {latest_date}"
    )


def render_category_table(cat_rows: list[dict[str, str]]) -> str:
    """Render the project table for docs/categories/<slug>.md."""
    lines = [
        "| ID | Title | Difficulty | Phase | Tools | Source type | Description | Notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in cat_rows:
        pid = row["id"].strip()
        title = escape_md_cell(row["title"].strip())
        url = row["url"].strip()
        hint = navigation_hint(row)
        title_cell = f"[{title}]({url}){hint}"

        difficulty = row["difficulty"].strip()
        diff_badge = DIFFICULTY_BADGE_MAP[difficulty]
        diff_cell = (
            f'<img src="../../assets/badges/{diff_badge}" alt="{difficulty}" height="18" />'
        )

        phase = row["learning_phase"].strip()
        phase_short = phase.split(" - ", 1)[0]
        phase_anchor = PHASE_ANCHORS[phase]
        phase_cell = f"[{phase_short}](../learning-path.md#{phase_anchor})"

        tools_cell = format_tools(row["tools_and_skills"])
        source_cell = escape_md_cell(row["source_type"].strip())
        desc_cell = escape_md_cell(row["description"].strip())
        notes_raw = row.get("notes", "").strip()
        notes_cell = escape_md_cell(notes_raw) if notes_raw else "None"

        lines.append(
            f"| {pid} | {title_cell} | {diff_cell} | {phase_cell} | {tools_cell} | {source_cell} | {desc_cell} | {notes_cell} |"
        )
    return "\n".join(lines)


def render_learning_phase_table(phase_rows: list[dict[str, str]]) -> str:
    """Render the project table for one phase in docs/learning-path.md."""
    lines = [
        "| ID | Title | Category | Difficulty | Tools | Notes |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in phase_rows:
        pid = row["id"].strip()
        title = escape_md_cell(row["title"].strip())
        url = row["url"].strip()
        hint = navigation_hint(row)
        title_cell = f"[{title}]({url}){hint}"

        cat = row["category"].strip()
        slug = CATEGORY_TO_SLUG[cat]
        cat_cell = f"[{cat}](categories/{slug}.md)"

        difficulty = row["difficulty"].strip()
        diff_badge = DIFFICULTY_BADGE_MAP[difficulty]
        diff_cell = (
            f'<img src="../assets/badges/{diff_badge}" alt="{difficulty}" height="18" />'
        )

        tools_cell = format_tools(row["tools_and_skills"])
        notes_raw = row.get("notes", "").strip()
        notes_cell = escape_md_cell(notes_raw) if notes_raw else "None"

        lines.append(
            f"| {pid} | {title_cell} | {cat_cell} | {diff_cell} | {tools_cell} | {notes_cell} |"
        )
    return "\n".join(lines)


def build_outputs(root: Path, rows: list[dict[str, str]]) -> dict[Path, str]:
    """Compute desired contents for all generated files without mutating disk."""
    sorted_rows = sort_rows(rows)
    outputs: dict[Path, str] = {}

    project_count = str(len(sorted_rows))
    latest_date = max(r["verified_date"].strip() for r in sorted_rows)

    outputs[root / "assets" / "badges" / "projects-count.svg"] = build_shield_svg(
        title=f"Projects: {project_count}",
        desc=f"Shield badge displaying {project_count} curated n8n projects.",
        left_text="projects",
        right_text=project_count,
        right_bg="#B91C1C",
    )
    outputs[root / "assets" / "badges" / "last-updated.svg"] = build_shield_svg(
        title=f"Last verified: {latest_date}",
        desc=f"Shield badge displaying dataset verification date {latest_date}.",
        left_text="verified",
        right_text=latest_date,
        right_bg="#DC2626",
    )

    readme_path = root / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    readme_text = replace_marked_section(readme_text, "BADGES", render_readme_badges(sorted_rows))
    readme_text = replace_marked_section(
        readme_text, "CATEGORIES", render_categories_overview(sorted_rows)
    )
    readme_text = replace_marked_section(
        readme_text, "LEARNING_PATH", render_readme_learning_path(sorted_rows)
    )
    readme_text = replace_marked_section(
        readme_text, "PROJECTS", render_readme_directory(sorted_rows)
    )
    outputs[readme_path] = readme_text

    by_cat: dict[str, list[dict[str, str]]] = {}
    for row in sorted_rows:
        by_cat.setdefault(row["category"].strip(), []).append(row)

    for category, slug in CATEGORY_SPECS:
        cat_path = root / "docs" / "categories" / f"{slug}.md"
        cat_text = cat_path.read_text(encoding="utf-8")
        cat_rows = by_cat.get(category, [])
        cat_text = replace_marked_section(
            cat_text, "CATEGORY_META", render_category_meta(cat_rows)
        )
        cat_text = replace_marked_section(
            cat_text, "PROJECTS", render_category_table(cat_rows)
        )
        outputs[cat_path] = cat_text

    lp_path = root / "docs" / "learning-path.md"
    lp_text = lp_path.read_text(encoding="utf-8")
    for idx, phase in enumerate(ALLOWED_PHASES, start=1):
        phase_rows = [r for r in sorted_rows if r["learning_phase"].strip() == phase]
        lp_text = replace_marked_section(
            lp_text, f"PHASE_{idx}", render_learning_phase_table(phase_rows)
        )
    outputs[lp_path] = lp_text

    return outputs


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Regenerate CSV-driven sections in README.md, category pages, learning-path.md, and SVG badges."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=repo_root,
        help="Repository root directory.",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=None,
        help="Path to n8n_list.csv (default: <root>/data/n8n_list.csv).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether generated files are up to date without modifying them.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Entry point for CLI execution."""
    configure_utf8_stdio()
    args = parse_args(argv)
    root = args.root.resolve()
    csv_path = (args.csv or (root / "data" / "n8n_list.csv")).resolve()

    if not csv_path.is_file():
        print(f"ERROR: CSV file not found: {csv_path}", file=sys.stderr)
        return 2

    try:
        fieldnames, rows, has_bom = load_csv_rows(csv_path)
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        print(f"ERROR: Failed to read {csv_path}: {exc}", file=sys.stderr)
        return 2

    errors, _ = validate_rows(fieldnames=fieldnames, rows=rows, has_bom=has_bom)
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    try:
        planned = build_outputs(root=root, rows=rows)
    except (OSError, ValueError) as exc:
        print(f"ERROR: Failed while building generated sections: {exc}", file=sys.stderr)
        return 2

    changed: list[Path] = []
    for path, new_content in planned.items():
        current_content = path.read_text(encoding="utf-8") if path.is_file() else None
        if current_content != new_content:
            changed.append(path)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("w", encoding="utf-8", newline="\n") as handle:
                    handle.write(new_content)

    if args.check:
        if changed:
            print("Generated documentation is out of date:", file=sys.stderr)
            for path in changed:
                print(f"  - {path.relative_to(root)}", file=sys.stderr)
            return 1
        print(f"OK: All {len(planned)} generated files are up to date.")
        return 0

    print(
        f"OK: Processed {len(planned)} generated files from {len(rows)} CSV rows ({len(changed)} updated)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
