"""Utility helpers for deterministic serialization and hashing."""
from __future__ import annotations

import json
import hashlib
from pathlib import Path
from typing import Any, Dict


def canonical_json(data: Any) -> str:
    """Return canonical JSON string (sorted keys, no spaces)."""
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")
