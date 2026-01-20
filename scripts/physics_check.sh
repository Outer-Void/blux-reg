#!/usr/bin/env bash
set -euo pipefail

forbidden_pattern='safety policy|\b(ethic|morality|discern|posture|illusion|therapy|harm)\b'
if rg -n -i --hidden --glob '!.git/*' "$forbidden_pattern" .; then
  echo "Physics check failed: forbidden policy/discernment tokens detected."
  exit 1
fi

phase0_paths=(
  "contracts/envelope.schema.json"
  "contracts/request.schema.json"
  "contracts/discernment_report.schema.json"
  "contracts/guard_receipt.schema.json"
  "schemas/envelope.schema.json"
  "schemas/request.schema.json"
  "schemas/discernment_report.schema.json"
  "schemas/guard_receipt.schema.json"
)

for path in "${phase0_paths[@]}"; do
  if [[ -e "$path" ]]; then
    echo "Physics check failed: Phase 0 contract schema detected at $path."
    exit 1
  fi
done

echo "Physics check passed."
