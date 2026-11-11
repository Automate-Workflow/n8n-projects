# Repository Maintenance Guide

This guide describes how maintainers validate `data/n8n_list.csv`, keep generated documentation synchronized, audit external links, and review pull requests.

## Single Source of Truth Workflow

All directory tables, category counts, learning-phase project lists, and dynamic SVG badges (`assets/badges/projects-count.svg`, `assets/badges/last-updated.svg`) derive exclusively from `data/n8n_list.csv`.

Never manually edit sections inside `<!-- ...:START -->` and `<!-- ...:END -->` markers in:

- `README.md`
- `docs/learning-path.md`
- `docs/categories/*.md`

## Adding or Updating a Project

1. Open `data/n8n_list.csv` using an editor or script that preserves **UTF-8 with BOM** (`utf-8-sig`).
2. Assign the next sequential positive integer `id` when adding a new entry (never reuse retired IDs).
3. Populate all required columns matching [data/README.md](../data/README.md).
4. Add accurate risk, compliance, or navigation notes in `notes` when relevant:
   - Multi-workflow repositories: `Repo with several workflows; open the named workflow`
   - Profile pages showcasing pinned repos: `Profile page; open the pinned repo named in the description`
   - Platform or privacy risks (WhatsApp unofficial APIs, LinkedIn scraping, HR PII/bias)
5. Set `verified_date` to today's ISO date (`YYYY-MM-DD`) and set `status` (for example `Verified`).
6. Run validation and regeneration:

```bash
python scripts/validate_csv.py --strict
python scripts/build_readme.py
python scripts/build_readme.py --check
```

## Running Link Checks

`scripts/check_links.py` checks unique URLs in `data/n8n_list.csv` using `HEAD` with `GET` fallback, configurable retries, and timeouts:

```bash
python scripts/check_links.py --output reports/link-check-report.md --json-output reports/link-check-report.json
```

### Handling Link Check Outcomes

- **OK (200) / Redirected (301/302)**: If a repository moved permanently (`301`), update `url` to the canonical destination and refresh `verified_date` and `status`.
- **WARN (403, 429, 5xx, timeout)**: Some platforms (such as `n8n.io` or rate-limited hosts) block automated requests or experience temporary timeouts. Verify manually in a browser before marking a link dead. `check_links.py` intentionally exits `0` on transient host warnings so CI does not fail on flaky hosts.
- **BROKEN (404 / 410)**: Verify whether the upstream file was renamed, moved to another folder, or deleted. Update the URL if relocated, or retire/replace the entry via PR with an explanation in `CHANGELOG.md`.

## Maintainer Review Checklist

When reviewing community pull requests:

- [ ] CI `Validate CSV and Check Sync` (`validate.yml`) and `Docs and Asset Integrity` (`build-docs.yml`) pass.
- [ ] All URLs added or modified open cleanly in a browser and point to genuine educational workflows.
- [ ] Upstream repo or template does not expose leaked API keys, passwords, or malicious code nodes.
- [ ] No third-party workflow JSON files or copied upstream READMEs were committed to this repository.
- [ ] No emoji appear in CSV text, Markdown, SVGs, Python scripts, or commit messages.
- [ ] `CHANGELOG.md` is updated for notable additions, link replacements, or documentation milestones.
