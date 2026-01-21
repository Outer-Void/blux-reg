#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

CONFIG_DIR=${BLUX_REG_CONFIG_DIR:-"$HOME/.config/blux-reg"}
export BLUX_REG_CONFIG_DIR="$CONFIG_DIR"

command -v blux-reg >/dev/null 2>&1 || {
  echo "blux-reg entrypoint not installed; try 'pip install -e .' first" >&2
  exit 1
}

blux-reg init

python - <<'PY'
from blux_reg import config, crypto

config.refresh_paths()
crypto.generate_keypair("demo", force=True)
PY

token_out="$CONFIG_DIR/token.json"

blux-reg issue demo publish outer-void/blux-example 3600 --output "$token_out"
blux-reg hash "$token_out"
blux-reg verify "$token_out"
