#!/usr/bin/env bash
# Build (venv + deps + cert + DB) and start the SpiritPTCGO server.
# Drag this file into Terminal and press Return, or double-click it in Finder.
set -euo pipefail

cd "$(dirname "$0")"

if [[ ! -f ./run.sh ]]; then
  echo "error: run.sh not found next to this file ($(pwd))."
  read -r -p "Press Return to close…"
  exit 1
fi

chmod +x ./run.sh
exec ./run.sh
