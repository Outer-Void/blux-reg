import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Iterable, List, Optional

from .crypto import fingerprint_from_public_key
from .paths import ensure_directories, get_ledger_path


@dataclass
class LedgerEntry:
    ts: str
    type: str
    payload: dict
    prev_hash: Optional[str]
    signer_fingerprint: str
    signature: str
    algo: dict
    hash: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


def _canonical_json(data: dict) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def _compute_hash(entry_dict: dict) -> str:
    temp = dict(entry_dict)
    temp["hash"] = None
    payload = _canonical_json(temp)
    return sha256(payload.encode()).hexdigest()


def load_entries(path: Optional[Path] = None) -> List[LedgerEntry]:
    ledger_path = path or get_ledger_path()
    if not ledger_path.exists():
        return []
    entries = []
    with ledger_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            entries.append(LedgerEntry(**data))
    return entries


def append_entry(entry_type: str, payload: dict, signature: str, public_key_path: Path) -> LedgerEntry:
    ensure_directories()
    ledger_path = get_ledger_path()
    entries = load_entries(ledger_path)
    prev_hash = entries[-1].hash if entries else None
    signer_fp = fingerprint_from_public_key(public_key_path)
    entry = LedgerEntry(
        ts=datetime.now(timezone.utc).isoformat(),
        type=entry_type,
        payload=payload,
        prev_hash=prev_hash,
        signer_fingerprint=signer_fp,
        signature=signature,
        algo={
            "hash": {"name": "sha256", "version": 1},
            "sig": {"name": "ed25519", "version": 1},
        },
    )
    entry.hash = _compute_hash(entry.to_dict())
    with ledger_path.open("a", encoding="utf-8") as f:
        f.write(_canonical_json(entry.to_dict()) + "\n")
    return entry


def verify_chain(path: Optional[Path] = None) -> bool:
    entries = load_entries(path)
    prev_hash = None
    for entry in entries:
        expected_hash = _compute_hash(entry.to_dict())
        if entry.hash != expected_hash:
            return False
        if entry.prev_hash != prev_hash:
            return False
        prev_hash = entry.hash
    return True


def tail_entries(limit: int = 10, path: Optional[Path] = None) -> Iterable[LedgerEntry]:
    entries = load_entries(path)
    return entries[-limit:]


__all__ = [
    "LedgerEntry",
    "append_entry",
    "verify_chain",
    "tail_entries",
    "load_entries",
]
