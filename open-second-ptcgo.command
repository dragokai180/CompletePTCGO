#!/usr/bin/env bash
# Open a second (or additional) Pokemon TCG Online instance on macOS.
# Double-click this file in Finder, or run it from a terminal.
set -euo pipefail

APP_NAME="Pokemon Trading Card Game Online"
APP_PATH="/Applications/${APP_NAME}.app"
BIN_PATH="${APP_PATH}/Contents/MacOS/${APP_NAME}"

if [[ ! -d "$APP_PATH" ]]; then
  echo "error: ${APP_PATH} not found."
  echo "Install PTCGO under /Applications, or edit APP_PATH in this script."
  read -r -p "Press Return to close…"
  exit 1
fi

# -n forces a new instance even if one is already running.
# -a targets the app by name; -g keeps this launcher's terminal from stealing focus.
if open -n -g -a "$APP_NAME"; then
  echo "Launched another ${APP_NAME} instance."
else
  echo "open -n failed; starting the binary directly…"
  nohup "$BIN_PATH" >/dev/null 2>&1 &
  echo "Launched via ${BIN_PATH} (pid $!)."
fi

# Brief pause so a double-clicked Terminal window shows the message.
sleep 1
