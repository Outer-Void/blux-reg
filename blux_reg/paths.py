from __future__ import annotations

from pathlib import Path

HOME = Path.home()
REGROOT = HOME / "blux-reg"
REGISTRY_ROOT = REGROOT / "registry"
KEYSTORE_ROOT = HOME / ".config" / "blux-reg" / "keys"
SIGNATURES_ROOT = REGROOT / "signatures"
TOKENS_ROOT = REGROOT / "tokens"

LEDGER_PATHS = {
    "keys": REGISTRY_ROOT / "keys.jsonl",
    "artifacts": REGISTRY_ROOT / "artifacts.jsonl",
    "revocations": REGISTRY_ROOT / "revocations.jsonl",
    "tokens": REGISTRY_ROOT / "tokens.jsonl",
}

REQUIRED_COMPATIBILITY = {
    "BLUX-Quantum": ">=1.0",
    "BLUX-Guard": ">=1.0",
}
