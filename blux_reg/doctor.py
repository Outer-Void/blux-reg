import importlib
import sys
from pathlib import Path
from typing import List, Tuple

from .paths import CONFIG_ENV, get_artifacts_dir, get_config_root, get_keys_dir, get_ledger_path


class DoctorIssue(Exception):
    pass


def _check_python_version(min_major=3, min_minor=10) -> Tuple[bool, str]:
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (min_major, min_minor)
    return ok, f"Python >= {min_major}.{min_minor} required (found {major}.{minor})"


def _check_dependency(module: str) -> Tuple[bool, str]:
    try:
        importlib.import_module(module)
        return True, ""
    except ImportError:
        return False, f"Install dependency: pip install {module}"


def _check_directory(path: Path) -> Tuple[bool, str]:
    try:
        path.mkdir(parents=True, exist_ok=True)
        test_file = path / ".__blux_perm_test"
        test_file.write_text("ok")
        test_file.unlink()
        return True, ""
    except Exception as exc:
        return False, f"Directory not writable: {path} ({exc})"


def run_doctor() -> Tuple[bool, List[str]]:
    messages: List[str] = []
    checks: List[Tuple[bool, str]] = []
    checks.append(_check_python_version())
    checks.append(_check_dependency("cryptography"))

    config_root = get_config_root()
    keys_dir = get_keys_dir()
    ledger_dir = get_ledger_path().parent
    artifacts_dir = get_artifacts_dir()

    for path in [config_root, keys_dir, ledger_dir, artifacts_dir]:
        checks.append(_check_directory(path))

    ok = True
    for passed, msg in checks:
        if not passed:
            ok = False
            messages.append(msg)
    if not ok:
        messages.append(
            "Set BLUX_CONFIG_HOME to override config root if needed: "
            f"export {CONFIG_ENV}=<path>"
        )
    return ok, messages


__all__ = ["run_doctor", "DoctorIssue"]
