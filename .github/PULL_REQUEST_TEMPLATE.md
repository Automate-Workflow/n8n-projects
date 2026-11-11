## Summary

Describe the change made in this pull request and reference any related issue (`Closes #...`).

## Type of Change

- [ ] New project addition (`data/n8n_list.csv`)
- [ ] Link repair or metadata update (`data/n8n_list.csv`)
- [ ] Documentation update (`README.md`, `docs/`)
- [ ] Scripts or CI workflow update (`scripts/`, `.github/`)
- [ ] Design or SVG asset update (`assets/`)

## Checklist

- [ ] `python scripts/validate_csv.py` passes with exit code `0`.
- [ ] `python scripts/build_readme.py` was executed and `python scripts/build_readme.py --check` confirms no drift.
- [ ] All modified or added URLs were tested (`python scripts/check_links.py` or verified manually).
- [ ] No third-party workflow JSON files or upstream README text were copied into this repository.
- [ ] No secrets, tokens, or emoji were introduced anywhere.
- [ ] Commits follow Conventional Commits and include DCO sign-off (`git commit -s`).
