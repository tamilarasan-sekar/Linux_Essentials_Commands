#!/usr/bin/env bash
set -euo pipefail

# Install pre-commit (if not already installed) and enable pre-commit hooks for this repo
if ! command -v pre-commit >/dev/null 2>&1; then
  echo "pre-commit not found. Installing with pip..."
  python3 -m pip install --user pre-commit
fi

echo "Installing pre-commit hooks..."
python3 -m pre_commit install || true
echo "Done. Run 'pre-commit install' manually if the above fails."
