# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-11

### Added

- Initial curated dataset (`data/n8n_list.csv`) covering 50 n8n workflows across 9 categories (`WhatsApp`, `LinkedIn`, `Resume/HR`, `Text/Classification`, `Voice`, `Image`, `Computer Vision`, `Video`, `Paper`) and 4 learning phases.
- Dataset schema documentation in `data/README.md`.
- Hand-written red-themed SVG assets in `assets/` (`banner.svg`, `logo.svg`, `divider.svg`, 9 category icons, and difficulty/phase/status badges) compatible with GitHub light and dark modes.
- Python 3 standard-library scripts in `scripts/`: `validate_csv.py`, `build_readme.py`, and `check_links.py`.
- Documentation suite in `docs/`: `getting-started.md`, `learning-path.md`, `maintenance.md`, and 9 category guides under `docs/categories/`.
- Generated `README.md` with category overview, 4-phase learning path summary, full directory tables, safe-usage guide, and third-party licensing notice.
- Governance, community, and CI files: `LICENSE` (MIT), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1), `SECURITY.md`, `SUPPORT.md`, `CITATION.cff`, `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/CODEOWNERS`, `.github/dependabot.yml`, and `.github/workflows/`.
