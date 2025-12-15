#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

CONFIG_DIR=${BLUX_REG_CONFIG_DIR:-"$HOME/.config/blux-reg"}
export BLUX_REG_CONFIG_DIR="$CONFIG_DIR"

bin_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

command -v blux-reg >/dev/null 2>&1 || {
  echo "blux-reg entrypoint not installed; try 'pip install -e .' first" >&2
  exit 1
}

echo "[1/6] init"
blux-reg init

echo "[2/6] keygen"
blux-reg keygen --name demo --force

sample="$CONFIG_DIR/sample.txt"
echo "demo artifact" > "$sample"

echo "[3/6] sign"
man_out="$sample.blux-manifest.json"
blux-reg sign "$sample" --key-name demo --output "$man_out"

echo "[4/6] verify"
blux-reg verify "$man_out"

echo "[5/6] audit tail"
blux-reg audit tail -n 5

echo "[6/6] audit verify-chain"
blux-reg audit verify-chain

