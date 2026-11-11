# Contributing to n8n-projects

Thank you for helping grow and maintain this curated directory of n8n automation projects. All contributions, whether proposing a new project, fixing a broken link, or improving documentation and tooling, follow the process below.

## Ways to Contribute

1. **Propose a new project**: Open an issue using the **New Project Proposal** form (`.github/ISSUE_TEMPLATE/new_project.yml`) or submit a pull request adding a row to `data/n8n_list.csv`.
2. **Report a broken or changed link**: Use the **Broken Link Report** form (`.github/ISSUE_TEMPLATE/broken_link.yml`) or submit a pull request updating `url`, `verified_date`, and `status`.
3. **Improve docs or scripts**: Open an issue or pull request for documentation clarifications, accessibility improvements, or Python validation and build tooling enhancements.

## Inclusion Criteria

Every listed project must satisfy all of the following rules:

- **Open source or freely importable**: The workflow JSON, repository, or n8n.io template must be publicly accessible and importable without purchasing a closed bundle.
- **Working and reachable**: The link must resolve cleanly and point to an active repository, workflow file, folder, template page, or documented pinned profile.
- **Documented**: The upstream source explains what the workflow does, which nodes/services it uses, and what credentials are required.
- **Educational value**: Demonstrates practical n8n patterns (routing, error handling, RAG, multimodal pipelines, webhooks, agents, or structured extraction).
- **No leaked secrets**: Do not submit workflows or links that expose API keys, webhook secrets, or personal credentials.
- **No malicious or deceptive content**: No obfuscated payloads, phishing, credential harvesting, or misleading claims.
- **Respects third-party terms**: Entries touching platforms with strict automation restrictions (for example unofficial WhatsApp APIs or LinkedIn scraping) must carry an accurate warning in `notes`.
- **Links only, no redistribution**: Do not copy third-party workflow JSON files or upstream README text into this repository.

## Required Project Fields (`data/n8n_list.csv`)

Project proposals and CSV additions must supply values matching the schema documented in [data/README.md](data/README.md):

| Column | Required | Expectation |
| --- | --- | --- |
| `id` | Yes | Next unique sequential integer (`max + 1`). |
| `title` | Yes | Concise project name (plain text, no emoji). |
| `category` | Yes | One of: `WhatsApp`, `LinkedIn`, `Resume/HR`, `Text/Classification`, `Voice`, `Image`, `Computer Vision`, `Video`, `Paper`. |
| `difficulty` | Yes | `Beginner`, `Intermediate`, or `Advanced`. |
| `learning_phase` | Yes | `Phase 1 - Foundations`, `Phase 2 - Chatbots and Voice`, `Phase 3 - Documents, Vision and Data`, or `Phase 4 - Advanced Agents and Integrations`. |
| `tools_and_skills` | Yes | Semicolon-separated list (for example `n8n; Gemini; Notion`). |
| `description` | Yes | Concise one-sentence summary of the workflow behavior. |
| `source_type` | Yes | `GitHub file`, `GitHub folder`, `GitHub repo`, `GitHub profile (pinned repo)`, or `n8n.io template`. |
| `url` | Yes | Direct HTTP/HTTPS URL to the project source. |
| `notes` | Optional | Compliance caveats, license reminders, or navigation hints such as `Repo with several workflows; open the named workflow`. |
| `verified_date` | Yes | ISO date (`YYYY-MM-DD`) when you tested or verified the link. |
| `status` | Yes | Current status (for example `Verified`). |

## Editing `data/n8n_list.csv` Safely

`data/n8n_list.csv` is the single source of truth. Never hand-edit the auto-generated sections inside `README.md`, `docs/learning-path.md`, or `docs/categories/*.md`.

- Preserve **UTF-8 with BOM** (`utf-8-sig`) encoding when editing the CSV.
- Quote any field containing commas or double quotes according to RFC 4180.
- Do not include emoji anywhere in CSV text, Markdown, SVG assets, code comments, or commit messages.
- Regenerate documentation locally after editing the CSV and commit both the CSV change and the regenerated files.

## Running Validation and Build Scripts Locally

The scripts use Python 3 standard library modules only (no `pip install` needed).

### Windows PowerShell

```powershell
python scripts/validate_csv.py
python scripts/build_readme.py
python scripts/build_readme.py --check
python scripts/check_links.py
```

### Linux and macOS

```bash
python3 scripts/validate_csv.py
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 scripts/check_links.py
```

## Branch Naming and Commit Conventions

Use descriptive branches off `main`:

- `feat/add-project-<slug>` for new workflow additions
- `fix/update-link-<id>` for link repairs or status updates
- `docs/<topic>` for documentation improvements
- `chore/<topic>` or `ci/<topic>` for tooling and workflow updates

Use **Conventional Commits** with plain text only (no emoji):

- `feat: add invoice parsing workflow to paper category`
- `fix: update broken workflow link for id 14`
- `docs: clarify docker volume setup in getting-started`
- `chore: refine csv validator error messages`

## Pull Request Checklist

Before requesting review, confirm:

- [ ] `python scripts/validate_csv.py` exits with status `0`.
- [ ] `python scripts/build_readme.py` ran cleanly and `python scripts/build_readme.py --check` reports no pending diff.
- [ ] All newly added or updated URLs were verified with `python scripts/check_links.py` or manually checked in a browser.
- [ ] No third-party workflow JSON files, upstream README text, secrets, or emoji were added.
- [ ] Hand-written prose outside `<!-- ...:START -->` / `<!-- ...:END -->` markers remains intact and passes Markdown formatting cleanly.

## Review Process and Response Expectations

- Pull requests trigger automated CI validation (`.github/workflows/validate.yml` and `.github/workflows/build-docs.yml`) that checks CSV schema rules and ensures generated docs match `data/n8n_list.csv`.
- Maintainers aim to provide an initial response on issues and pull requests within **5 to 7 business days**.
- If a PR proposes replacing or retiring an entry, explain why (archived repository, deleted file, or superseded upstream source) in the PR description.

## Developer Certificate of Origin (DCO) Sign-Off

By submitting a contribution to this repository, you certify under the Developer Certificate of Origin (DCO 1.1) that you wrote the contribution or otherwise have the right to submit it under the repository's MIT License, and that it includes no unauthorized third-party workflow code or proprietary secrets.

Sign off commits with `git commit -s` (adding `Signed-off-by: Your Name <you@example.com>`).
