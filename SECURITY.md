# Security Policy

## Supported Versions

Security updates and link integrity fixes apply exclusively to the default branch:

| Branch / Version | Supported |
| --- | --- |
| `main` | Yes |
| Forks and historical snapshots | No |

## Reporting a Vulnerability or Unsafe Listing

Please **do not** report security vulnerabilities, leaked credentials, or malicious third-party links in public GitHub issues.

Report privately using one of these channels:

1. **GitHub Private Vulnerability Reporting**: Open the repository **Security** tab at `https://github.com/Automate-Workflow/n8n-projects/security/advisories/new` (once Private Vulnerability Reporting is enabled in repository settings).
2. **Email**: Send details to `ayush_24a12res897@iitp.ac` with the subject prefix `[SECURITY n8n-projects]`.

Include:

- Affected project ID (`data/n8n_list.csv`), file path, or GitHub Actions workflow.
- Description of the risk, reproduction steps, or proof of exposure.
- Any suggested remediation (such as link removal or script patch).

## What Counts as a Security Issue

For this curated directory, valid security reports include:

- **Malicious or compromised linked project**: A listed repository, file, or template that contains malware, credential exfiltration, hidden backdoors, or deceptive code.
- **Leaked credentials in a linked workflow**: Upstream JSON templates or repositories that accidentally expose live API keys, tokens, or private webhook URLs.
- **Phishing or hijacked domains**: Expired or transferred domains/accounts redirecting users to deceptive sites.
- **Repository tooling vulnerabilities**: Bugs in `scripts/*.py` or `.github/workflows/*.yml` (such as command injection, untrusted workflow input execution, or path traversal).

## Response Targets and Coordinated Disclosure

- **Acknowledgement**: Within **3 business days** of receiving your report.
- **Triage and assessment**: Within **7 business days**, including severity classification and an action plan.
- **Coordinated disclosure**: If a third-party upstream workflow leaks credentials or has a vulnerability, maintainers will remove or flag the entry promptly and coordinate notice with the upstream maintainer where possible before publishing public details.

## Safe-Use Guidance for Importing Third-Party Workflows

Because almost every project linked from this directory is authored and maintained by third parties, follow strict hygiene before running any imported n8n workflow:

1. **Inspect every node before activation**: Review all `Code` (JavaScript/Python), `Execute Command`, `HTTP Request`, and community nodes to verify where data is sent.
2. **Never import into production**: Test unfamiliar workflows in an isolated local Docker or staging n8n instance with no production credentials attached.
3. **Use scoped test credentials**: Create restricted sandbox API keys and test webhooks with sample data only.
4. **Verify community nodes**: Check source code and npm/GitHub maintenance status before installing custom nodes such as unofficial messaging bridges.
5. **Rotate exposed keys immediately**: If you accidentally run a workflow against an unintended endpoint or paste a secret into a JSON file, revoke and rotate that credential immediately.
