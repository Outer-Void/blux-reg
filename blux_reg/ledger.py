from __future__ import annotations

import json
import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Optional

from .paths import LEDGER_PATHS

CANONICAL_SEPARATORS = (",", ":")


def canonical_dumps(data: dict) -> str:
    return json.dumps(data, sort_keys=True, separators=CANONICAL_SEPARATORS)


def canonical_bytes(data: dict) -> bytes:
    return canonical_dumps(data).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass
class LedgerEntry:
    raw: dict

    @property
    def prev_hash(self) -> Optional[str]:
        return self.raw.get("prev_hash")

    @property
    def chain_hash(self) -> Optional[str]:
        return self.raw.get("chain_hash")

    def payload_bytes(self) -> bytes:
        payload = dict(self.raw)
        payload.pop("chain_hash", None)
        return canonical_bytes(payload)


class Ledger:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _iter_lines(self) -> Iterator[str]:
        if not self.path.exists():
            return iter(())
        with self.path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    yield line

    def entries(self) -> List[LedgerEntry]:
        return [LedgerEntry(json.loads(line)) for line in self._iter_lines()]

    def last_hash(self) -> Optional[str]:
        last_line = None
        for last_line in self._iter_lines():
            pass
        if last_line is None:
            return None
        payload = json.loads(last_line)
        payload.pop("chain_hash", None)
        return sha256_hex(canonical_bytes(payload))

    def append(self, entry: dict) -> LedgerEntry:
        entry = dict(entry)
        prev_hash = self.last_hash()
        if prev_hash:
            entry.setdefault("prev_hash", prev_hash)
        elif "prev_hash" in entry and entry["prev_hash"] is None:
            entry.pop("prev_hash")
        payload_bytes = canonical_bytes(entry)
        chain_hash = sha256_hex(payload_bytes)
        entry_with_hash = dict(entry)
        entry_with_hash["chain_hash"] = chain_hash
        line = canonical_dumps(entry_with_hash)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
        return LedgerEntry(entry_with_hash)

    def verify_chain(self) -> bool:
        prev_hash = None
        for entry in self.entries():
            payload = dict(entry.raw)
            chain_hash = payload.pop("chain_hash", None)
            payload_bytes = canonical_bytes(payload)
            computed_hash = sha256_hex(payload_bytes)
            if computed_hash != chain_hash:
                return False
            if prev_hash != payload.get("prev_hash"):
                if prev_hash is None and payload.get("prev_hash") in (None, ""):
                    pass
                else:
                    return False
            prev_hash = computed_hash
        return True


LEDGERS = {name: Ledger(path) for name, path in LEDGER_PATHS.items()}


def get_ledger(name: str) -> Ledger:
    try:
        return LEDGERS[name]
    except KeyError:
        raise ValueError(f"Unknown ledger '{name}'. Known: {', '.join(sorted(LEDGERS))}")
