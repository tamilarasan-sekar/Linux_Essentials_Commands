# Linux_Essentials_Commands
Commands from the Linux Essentials Course

## Developer setup

This repository includes a text formatter and pre-commit configuration to help keep documentation consistent.

Steps to enable and verify pre-commit locally:

```bash
# Install and enable pre-commit
bash scripts/install-pre-commit.sh
# or manually:
# python3 -m pip install --user pre-commit
# python3 -m pre_commit install
```

To run the formatter manually across all text files in the repo:

```bash
python3 scripts/format_text_files.py
```

To check whether formatting is needed:

```bash
git diff --exit-code

### Linting Markdown (optional)

To enable the markdown linter locally, install Node.js and run:

```bash
brew install node
npx markdownlint-cli -c ./.markdownlint.json "**/*.md"
```

```

