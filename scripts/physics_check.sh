#!/usr/bin/env bash
set -euo pipefail

code_globs=(
  --glob "src/**"
  --glob "tests/**"
  --glob "scripts/**"
  --glob "bin/**"
  --glob "!scripts/physics_check.sh"
  --glob "!tests/test_boundary_ci.py"
  --glob "!**/__pycache__/**"
)

execution_pattern='\bsubprocess\b|os\.system|\bexec\(|\bshell\b|\bchild_process\b'
repo_pattern='\bblux_ca\b|\bblux_guard\b|\bblux_lite\b|\bblux_quantum\b|\bblux_doctrine\b'
intent_pattern='\bposture\b|\bethic|\benforce\b|\ballow\b[[:space:][:punct:]]+\bintent\b|\bdeny\b[[:space:][:punct:]]+\bintent\b|doctrine[[:space:][:punct:]]+engine'
role_pattern='guard_receipt|discernment_report|\bexecute\b|\brouter\b|\borchestr|\bpolicy\b|\bquantum\b|\bdoctrine\b|\blite\b'

if rg -n -i --hidden "${code_globs[@]}" "$execution_pattern" .; then
  echo "Physics check failed: execution primitives detected in code."
  exit 1
fi

if rg -n -i --hidden "${code_globs[@]}" "$repo_pattern" .; then
  echo "Physics check failed: sibling repo references detected."
  exit 1
fi

if rg -n -i --hidden "${code_globs[@]}" "$intent_pattern" .; then
  echo "Physics check failed: policy or intent reasoning keywords detected in code."
  exit 1
fi

if rg -n -i --hidden "${code_globs[@]}" "$role_pattern" .; then
  echo "Physics check failed: prohibited role keywords detected in code."
  exit 1
fi

if [[ -d "contracts" ]]; then
  echo "Physics check failed: contracts directory detected."
  exit 1
fi

if rg -n --hidden "\\$id\s*:\s*\"blux://contracts/" .; then
  echo "Physics check failed: canonical contract identifiers detected."
  exit 1
fi

schema_files=$(find . -type f -name "*.schema.json" ! -path "./tests/fixtures/*" ! -path "./.git/*")
if [[ -n "${schema_files}" ]]; then
  echo "Physics check failed: schema files detected outside tests/fixtures."
  echo "${schema_files}"
  exit 1
fi

echo "Physics check passed."
