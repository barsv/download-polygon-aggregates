#!/usr/bin/env bash

# Ensure the script is run with bash (not sh)
if [ -z "${BASH_VERSION:-}" ]; then
  echo "Please run with bash: bash tools/jupytext_sync.sh" 1>&2
  exit 1
fi

set -euo pipefail

# Sync paired .ipynb <-> .py (percent) under research/
# Requires: pip install jupytext

if ! command -v jupytext >/dev/null 2>&1; then
  echo "jupytext is not installed. Run: pip install jupytext" 1>&2
  exit 1
fi

# Ensure paired scripts directory exists (per Jupytext config)
mkdir -p research/pyfiles

find research -type f -name '*.ipynb' -print0 | while IFS= read -r -d '' nb; do
  echo "Syncing $nb"
  jupytext --sync "$nb"
done

echo "Done."
