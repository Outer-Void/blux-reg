"""Append-only audit ledger utilities."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

from . import config
from .util import canonical_json, sha256_hex


def _iter_entries() -> Iterable[Dict]:
    if not config.LEDGER_PATH.exists():
        return []
    with config.LEDGER_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def _last_entry_hash() -> str | None:
    last_hash = None
    for entry in _iter_entries():
        last_hash = entry.get("entry_hash")
    return last_hash


def _compute_entry_hash(entry: Dict) -> str:
    data = dict(entry)
    data.pop("entry_hash", None)
    return sha256_hex(canonical_json(data).encode())


def append_entry(
    action: str,
    actor: str,
    payload_summary: str,
    artifact_hash: str | None = None,
    manifest_hash: str | None = None,
    extra: Dict | None = None,
) -> Dict:
    config.ensure_directories()
    prev_hash = _last_entry_hash()
    entry = {
        "ts": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "action": action,
        "actor": actor,
        "payload_summary": payload_summary,
        "artifact_hash": artifact_hash,
        "manifest_hash": manifest_hash,
        "prev_hash": prev_hash,
    }
    if extra:
        entry.update(extra)
    entry_hash = _compute_entry_hash(entry)
    entry["entry_hash"] = entry_hash
    with config.LEDGER_PATH.open("a", encoding="utf-8") as f:
        f.write(canonical_json(entry) + "\n")
    return entry


def tail_entries(limit: int = 10) -> List[Dict]:
    entries = list(_iter_entries())
    if limit <= 0:
        return entries
    return entries[-limit:]


def verify_chain() -> bool:
    prev_hash = None
    for entry in _iter_entries():
        expected_prev = entry.get("prev_hash")
        if expected_prev != prev_hash:
            return False
        computed_hash = _compute_entry_hash(entry)
        if computed_hash != entry.get("entry_hash"):
            return False
        prev_hash = entry.get("entry_hash")
    return True


def ledger_size() -> int:
    return len(list(_iter_entries()))


def last_hash() -> str | None:
    return _last_entry_hash()
