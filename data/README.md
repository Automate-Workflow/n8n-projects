# Dataset Schema: `data/n8n_list.csv`

`data/n8n_list.csv` is the single source of truth for all project listings in this repository. Both [README.md](../README.md) and the category and learning-path pages in [docs/](../docs/) are generated from this file via [scripts/build_readme.py](../scripts/build_readme.py).

Do not hand-edit generated Markdown tables outside this CSV; update `data/n8n_list.csv` and regenerate the documentation instead.

## File Format

- **Encoding**: UTF-8 with BOM (`utf-8-sig` in Python). Preserving the BOM ensures Microsoft Excel and LibreOffice Calc display characters correctly on Windows and macOS.
- **Delimiter**: Comma (`,`), RFC 4180 quoting (`"` around fields containing commas or quotes).
- **Header row**: Required, exact column names in the order listed below.

## Column Definitions

| Column | Required | Type / Format | Allowed Values and Rules |
| --- | --- | --- | --- |
| `id` | Yes | Positive integer | Unique sequential identifier (`1`, `2`, `3`, ...). Never reuse an ID if an entry is retired. |
| `title` | Yes | Plain text | Concise project name. No emoji. Avoid unescaped pipes or line breaks. |
| `category` | Yes | Enum (string) | One of: `WhatsApp`, `LinkedIn`, `Resume/HR`, `Text/Classification`, `Voice`, `Image`, `Computer Vision`, `Video`, `Paper`. |
| `difficulty` | Yes | Enum (string) | One of: `Beginner`, `Intermediate`, `Advanced`. |
| `learning_phase` | Yes | Enum (string) | One of: `Phase 1 - Foundations`, `Phase 2 - Chatbots and Voice`, `Phase 3 - Documents, Vision and Data`, `Phase 4 - Advanced Agents and Integrations`. |
| `tools_and_skills` | Yes | Semicolon-separated list | Key integrations, models, or techniques (for example `n8n; Gmail; OpenAI; Google Sheets`). |
| `description` | Yes | Plain text | One-sentence summary of what the workflow does. If a multi-workflow repo requires opening a specific file, include the filename in parentheses when known. |
| `source_type` | Yes | Enum (string) | One of: `GitHub file`, `GitHub folder`, `GitHub repo`, `GitHub profile (pinned repo)`, `n8n.io template`. |
| `url` | Yes | HTTP/HTTPS URL | Direct URL to the workflow file, folder, repository, pinned profile, or n8n.io template page. |
| `notes` | No | Semicolon-separated notes | Operational caveats, compliance reminders, license notes, or navigation hints such as `Repo with several workflows; open the named workflow` or `Profile page; open the pinned repo named in the description`. |
| `verified_date` | Yes | Date (`YYYY-MM-DD`) | ISO 8601 date of the most recent manual or automated verification. |
| `status` | Yes | Plain text | Current verification status (for example `Verified`, `Link seen in search or README; re-check before publishing`, or `Upstream archived; needs replacement`). |

## Category-to-Slug Mapping

Each `category` value maps deterministically to an icon in `assets/icons/<slug>.svg` and a documentation page in `docs/categories/<slug>.md`:

| CSV `category` | Slug | Icon Path | Category Page |
| --- | --- | --- | --- |
| `WhatsApp` | `whatsapp` | `assets/icons/whatsapp.svg` | [docs/categories/whatsapp.md](../docs/categories/whatsapp.md) |
| `LinkedIn` | `linkedin` | `assets/icons/linkedin.svg` | [docs/categories/linkedin.md](../docs/categories/linkedin.md) |
| `Resume/HR` | `resume-hr` | `assets/icons/resume-hr.svg` | [docs/categories/resume-hr.md](../docs/categories/resume-hr.md) |
| `Text/Classification` | `text-classification` | `assets/icons/text-classification.svg` | [docs/categories/text-classification.md](../docs/categories/text-classification.md) |
| `Voice` | `voice` | `assets/icons/voice.svg` | [docs/categories/voice.md](../docs/categories/voice.md) |
| `Image` | `image` | `assets/icons/image.svg` | [docs/categories/image.md](../docs/categories/image.md) |
| `Computer Vision` | `computer-vision` | `assets/icons/computer-vision.svg` | [docs/categories/computer-vision.md](../docs/categories/computer-vision.md) |
| `Video` | `video` | `assets/icons/video.svg` | [docs/categories/video.md](../docs/categories/video.md) |
| `Paper` | `paper` | `assets/icons/paper.svg` | [docs/categories/paper.md](../docs/categories/paper.md) |

## Special Cases in `notes`

Some rows legitimately share an upstream URL:

- **Multi-workflow repositories**: Repositories such as `lucaswalter/n8n-ai-automations` host multiple workflows. Keep the `Repo with several workflows; open the named workflow` hint in `notes` and name the target workflow in `title` or `description`.
- **Profile pages**: Authors who showcase workflows as pinned repositories (such as `StructUK`) keep `GitHub profile (pinned repo)` in `source_type` and `Profile page; open the pinned repo named in the description` in `notes`.

## Validation

Run the schema validator before opening a pull request:

```bash
python scripts/validate_csv.py
```
