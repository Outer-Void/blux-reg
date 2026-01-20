import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Boundary: prohibited keywords/paths that imply policy/ethics/discernment logic.
# This list is intentionally small and explicit to avoid false positives.
PROHIBITED_CONTENT_PATTERNS = [
    re.compile(r"\bpolicy[-_ ]engine\b", re.IGNORECASE),
    re.compile(r"\bpolicy[-_ ]as[-_ ]code\b", re.IGNORECASE),
    re.compile(r"\bposture[-_ ]scoring\b", re.IGNORECASE),
    re.compile(r"\bdiscernment\b", re.IGNORECASE),
    re.compile(r"\bethic(s|al)?\b", re.IGNORECASE),
    re.compile(r"\bmoral(ity)?\b", re.IGNORECASE),
]

PROHIBITED_PATH_PATTERNS = [
    re.compile(r"policy[-_ ]engine", re.IGNORECASE),
    re.compile(r"policy[-_ ]as[-_ ]code", re.IGNORECASE),
    re.compile(r"posture[-_ ]scoring", re.IGNORECASE),
    re.compile(r"discernment", re.IGNORECASE),
    re.compile(r"ethic", re.IGNORECASE),
    re.compile(r"moral", re.IGNORECASE),
]

ALLOWLIST = {
    "tests/test_boundary_ci.py",
    "scripts/physics_check.sh",
}


def _tracked_files():
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=REPO_ROOT)
    for entry in output.decode("utf-8").split("\x00"):
        if entry:
            yield entry


def test_boundary_no_policy_discernment_logic():
    violations = []

    for rel_path in _tracked_files():
        if rel_path in ALLOWLIST:
            continue
        for pattern in PROHIBITED_PATH_PATTERNS:
            if pattern.search(rel_path):
                violations.append(f"path:{rel_path}:{pattern.pattern}")
                break
        else:
            path = REPO_ROOT / rel_path
            if not path.is_file():
                continue
            content = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in PROHIBITED_CONTENT_PATTERNS:
                if pattern.search(content):
                    violations.append(f"content:{rel_path}:{pattern.pattern}")
                    break

    assert not violations, "Boundary violation(s) detected:\n" + "\n".join(violations)
