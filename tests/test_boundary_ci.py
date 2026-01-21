import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CODE_DIRS = [REPO_ROOT / "src", REPO_ROOT / "tests", REPO_ROOT / "scripts", REPO_ROOT / "bin"]

PROHIBITED_CONTENT_PATTERNS = [
    re.compile(r"\bsubprocess\b", re.IGNORECASE),
    re.compile(r"os\.system", re.IGNORECASE),
    re.compile(r"\bexec\(", re.IGNORECASE),
    re.compile(r"\bshell\b", re.IGNORECASE),
    re.compile(r"\bchild_process\b", re.IGNORECASE),
    re.compile(r"guard_receipt", re.IGNORECASE),
    re.compile(r"discernment_report", re.IGNORECASE),
    re.compile(r"\bexecute\b", re.IGNORECASE),
    re.compile(r"\brouter\b", re.IGNORECASE),
    re.compile(r"\borchestr", re.IGNORECASE),
    re.compile(r"\bpolicy\b", re.IGNORECASE),
    re.compile(r"\bethic", re.IGNORECASE),
    re.compile(r"\bquantum\b", re.IGNORECASE),
    re.compile(r"\bdoctrine\b", re.IGNORECASE),
    re.compile(r"\blite\b", re.IGNORECASE),
]

PROHIBITED_PATH_PATTERNS = [
    re.compile(r"contracts", re.IGNORECASE),
    re.compile(r"guard_receipt", re.IGNORECASE),
    re.compile(r"discernment_report", re.IGNORECASE),
    re.compile(r"\bexecute\b", re.IGNORECASE),
    re.compile(r"\brouter\b", re.IGNORECASE),
    re.compile(r"\borchestr", re.IGNORECASE),
    re.compile(r"\bpolicy\b", re.IGNORECASE),
    re.compile(r"\bethic", re.IGNORECASE),
    re.compile(r"\bquantum\b", re.IGNORECASE),
    re.compile(r"\bdoctrine\b", re.IGNORECASE),
    re.compile(r"\blite\b", re.IGNORECASE),
]

PROHIBITED_SCHEMA_ID = re.compile(r"\$id\s*:\s*\"blux://contracts/", re.IGNORECASE)

ALLOWLIST = {
    "tests/test_boundary_ci.py",
    "scripts/physics_check.sh",
}


def _iter_code_files():
    for root in CODE_DIRS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if "__pycache__" in path.parts:
                continue
            rel_path = path.relative_to(REPO_ROOT).as_posix()
            if rel_path in ALLOWLIST:
                continue
            yield path, rel_path


def test_boundary_no_forbidden_logic_or_contracts():
    violations = []

    if (REPO_ROOT / "contracts").exists():
        violations.append("path:contracts:contracts-directory")

    for path, rel_path in _iter_code_files():
        for pattern in PROHIBITED_PATH_PATTERNS:
            if pattern.search(rel_path):
                violations.append(f"path:{rel_path}:{pattern.pattern}")
                break
        else:
            content = path.read_text(encoding="utf-8", errors="ignore")
            if PROHIBITED_SCHEMA_ID.search(content):
                violations.append(f"schema:{rel_path}:blux-contract-id")
                continue
            for pattern in PROHIBITED_CONTENT_PATTERNS:
                if pattern.search(content):
                    violations.append(f"content:{rel_path}:{pattern.pattern}")
                    break

    for path in REPO_ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if "__pycache__" in path.parts:
            continue
        if not path.is_file():
            continue
        rel_path = path.relative_to(REPO_ROOT).as_posix()
        if rel_path in ALLOWLIST:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        if PROHIBITED_SCHEMA_ID.search(content):
            violations.append(f"schema:{rel_path}:blux-contract-id")

    assert not violations, "Boundary violation(s) detected:\n" + "\n".join(violations)
