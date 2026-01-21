"""Append-only trust store for issuers and revocations."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set

from .util import canonical_json, sha256_hex

TRUST_STORE_SCHEMA_VERSION = "1.0"
TRUST_ANCHOR_TYPE = "trust_anchor"
TOKEN_REVOCATION_TYPE = "token_revocation"


@dataclass
class TrustStore:
    """In-memory trust store with append-only persistence."""

    path: Path
    entries: List[Dict[str, Any]] = field(default_factory=list)
    pending_entries: List[Dict[str, Any]] = field(default_factory=list)
    last_hash: Optional[str] = None

    def add_entry(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        data = dict(entry)
        data.setdefault("schema_version", TRUST_STORE_SCHEMA_VERSION)
        data["prev_hash"] = self.last_hash
        entry_hash = sha256_hex(canonical_json(data).encode())
        data["entry_hash"] = entry_hash
        self.entries.append(data)
        self.pending_entries.append(data)
        self.last_hash = entry_hash
        return data


def _iter_entries(path: Path) -> Iterable[Dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json_loads(line)


def _compute_entry_hash(entry: Dict[str, Any]) -> str:
    data = dict(entry)
    data.pop("entry_hash", None)
    return sha256_hex(canonical_json(data).encode())


def _verify_chain(entries: Iterable[Dict[str, Any]]) -> Optional[str]:
    prev_hash = None
    last_hash = None
    for entry in entries:
        if entry.get("prev_hash") != prev_hash:
            raise ValueError("Trust store hash chain mismatch")
        if _compute_entry_hash(entry) != entry.get("entry_hash"):
            raise ValueError("Trust store entry hash mismatch")
        last_hash = entry.get("entry_hash")
        prev_hash = last_hash
    return last_hash


def load_trust_store(path: Path) -> TrustStore:
    """Load an append-only trust store from disk."""
    entries = list(_iter_entries(path))
    last_hash = _verify_chain(entries)
    return TrustStore(path=path, entries=entries, last_hash=last_hash)


def save_trust_store(path: Path, store: TrustStore) -> None:
    """Append pending trust store entries to disk."""
    if not store.pending_entries:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        for entry in store.pending_entries:
            fh.write(canonical_json(entry) + "\n")
    store.pending_entries.clear()


def trust_store_index(store: TrustStore) -> Dict[str, Set[str]]:
    """Build index sets for trusted issuers and revoked tokens."""
    trusted_issuers: Set[str] = set()
    revoked_tokens: Set[str] = set()
    for entry in store.entries:
        if entry.get("entry_type") == TRUST_ANCHOR_TYPE:
            fingerprint = entry.get("fingerprint")
            if fingerprint:
                trusted_issuers.add(fingerprint)
        if entry.get("entry_type") == TOKEN_REVOCATION_TYPE:
            token_hash = entry.get("token_hash")
            if token_hash:
                revoked_tokens.add(token_hash)
    return {"trusted_issuers": trusted_issuers, "revoked_tokens": revoked_tokens}


def new_trust_anchor(fingerprint: str, public_key_pem: str, source: str = "local") -> Dict[str, Any]:
    """Create a trust anchor entry for an issuer fingerprint."""
    return {
        "entry_type": TRUST_ANCHOR_TYPE,
        "added_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "fingerprint": fingerprint,
        "public_key": public_key_pem,
        "source": source,
    }


def new_token_revocation(token_hash: str, reason: str) -> Dict[str, Any]:
    """Create a token revocation entry."""
    return {
        "entry_type": TOKEN_REVOCATION_TYPE,
        "revoked_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "token_hash": token_hash,
        "reason": reason,
    }


def json_loads(payload: str) -> Dict[str, Any]:
    """Parse JSON payloads without importing json at module import time."""
    import json

    return json.loads(payload)
