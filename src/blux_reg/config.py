"""Configuration and path helpers for blux-reg.

Centralizes default paths with environment overrides to keep the CLI portable
across Linux, macOS, and Termux. All paths are derived from the configuration
root so tests can redirect state with the ``BLUX_REG_CONFIG_DIR`` environment
variable.
"""
from __future__ import annotations

import os
from pathlib import Path

SCHEMA_VERSION = "1.0"


def _resolve_root() -> Path:
    env_root = os.environ.get("BLUX_REG_CONFIG_DIR")
    if env_root:
        return Path(env_root).expanduser()
    return Path.home() / ".config" / "blux-reg"


CONFIG_ROOT = _resolve_root()
KEYS_DIR = CONFIG_ROOT / "keys"
MANIFEST_DIR = CONFIG_ROOT / "manifests"
TRUST_DIR = CONFIG_ROOT / "trust"
LEDGER_PATH = TRUST_DIR / "ledger.jsonl"
CACHE_DIR = CONFIG_ROOT / "cache"


def refresh_paths() -> None:
    """Refresh module-level paths from the current environment.

    Useful for tests that temporarily override ``BLUX_REG_CONFIG_DIR``.
    """
    global CONFIG_ROOT, KEYS_DIR, MANIFEST_DIR, TRUST_DIR, LEDGER_PATH, CACHE_DIR
    CONFIG_ROOT = _resolve_root()
    KEYS_DIR = CONFIG_ROOT / "keys"
    MANIFEST_DIR = CONFIG_ROOT / "manifests"
    TRUST_DIR = CONFIG_ROOT / "trust"
    LEDGER_PATH = TRUST_DIR / "ledger.jsonl"
    CACHE_DIR = CONFIG_ROOT / "cache"


def ensure_directories() -> None:
    """Create required directories if they do not exist."""
    for path in (CONFIG_ROOT, KEYS_DIR, MANIFEST_DIR, TRUST_DIR, CACHE_DIR):
        path.mkdir(parents=True, exist_ok=True)
