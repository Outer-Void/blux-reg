from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from .crypto import now_iso, sign_payload, verify_signature
from .keystore import KeyStore
from .ledger import canonical_bytes, sha256_hex, get_ledger
from .paths import TOKENS_ROOT
from .registry import ensure_structure, is_key_revoked

TOKEN_SCHEMA_VERSION = "1.0"
TOKEN_TYPE = "capability"

REQUIRED_FIELDS = {
    "schema_version",
    "token_type",
    "issued_at",
    "expires_at",
    "ttl_seconds",
    "capability",
    "audience_repo",
    "constraints",
    "issuer",
    "signature",
}


def _parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def token_ref(token: Dict[str, Any]) -> str:
    return sha256_hex(canonical_bytes(token))


def _payload_from_token(token: Dict[str, Any]) -> Dict[str, Any]:
    return {k: token[k] for k in token if k != "signature"}


def _token_path_for(hash_ref: str) -> Path:
    return TOKENS_ROOT / f"{hash_ref}.token.json"


def issue_capability_token(
    key_id: str,
    key_type: str,
    passphrase: str,
    capability: str,
    audience_repo: str,
    ttl_seconds: int,
    constraints: Optional[Dict[str, Any]] = None,
    keystore: Optional[KeyStore] = None,
    output_path: Optional[Path] = None,
) -> tuple[Dict[str, Any], str, Path]:
    if ttl_seconds <= 0:
        raise ValueError("ttl_seconds must be positive")
    ensure_structure()
    TOKENS_ROOT.mkdir(parents=True, exist_ok=True)
    ks = keystore or KeyStore()
    material = ks.load(key_id, key_type)
    issued_at_dt = datetime.now(timezone.utc).replace(microsecond=0)
    expires_at_dt = issued_at_dt + timedelta(seconds=ttl_seconds)
    payload = {
        "schema_version": TOKEN_SCHEMA_VERSION,
        "token_type": TOKEN_TYPE,
        "issued_at": issued_at_dt.isoformat(),
        "expires_at": expires_at_dt.isoformat(),
        "ttl_seconds": ttl_seconds,
        "capability": capability,
        "audience_repo": audience_repo,
        "constraints": constraints or {},
        "issuer": {
            "key_id": material.key_id,
            "key_type": material.key_type,
            "public_key": material.public_key,
            "compatibility": material.compatibility,
        },
    }
    signature = sign_payload(material, payload, passphrase)
    token = dict(payload)
    token["signature"] = signature
    hash_ref = token_ref(token)
    entry = {
        "timestamp": payload["issued_at"],
        "issuer": material.key_id,
        "role": material.key_type,
        "token_hash": hash_ref,
        "payload": payload,
        "signature": signature,
    }
    get_ledger("tokens").append(entry)
    path = output_path or _token_path_for(hash_ref)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(token, fh, indent=2, sort_keys=True)
    return token, hash_ref, path


def load_token(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def is_token_revoked(token_hash: str) -> bool:
    ledger = get_ledger("revocations")
    for entry in ledger.entries():
        payload = entry.raw.get("payload", {})
        if payload.get("event") == "token_revoked" and payload.get("token_hash") == token_hash:
            return True
    return False


def revoke_capability_token(token_hash: str, reason: str, revoker: str):
    ensure_structure()
    payload = {
        "event": "token_revoked",
        "timestamp": now_iso(),
        "token_hash": token_hash,
        "reason": reason,
        "revoker": revoker,
    }
    entry = {
        "timestamp": payload["timestamp"],
        "issuer": revoker,
        "role": "revocation",
        "payload": payload,
    }
    return get_ledger("revocations").append(entry)


def check_token_ledger_membership(token_hash: str, payload: Dict[str, Any], signature: str) -> bool:
    ledger = get_ledger("tokens")
    for entry in ledger.entries():
        if entry.raw.get("token_hash") == token_hash:
            if entry.raw.get("payload") == payload and entry.raw.get("signature") == signature:
                return True
    return False


def verify_capability_token(
    token: Dict[str, Any],
    now: Optional[datetime] = None,
    require_ledger: bool = True,
) -> Dict[str, str]:
    missing = REQUIRED_FIELDS - token.keys()
    if missing:
        raise ValueError(f"Token missing fields: {sorted(missing)}")
    if token.get("token_type") != TOKEN_TYPE:
        raise ValueError("Token type mismatch")
    if token.get("schema_version") != TOKEN_SCHEMA_VERSION:
        raise ValueError("Unsupported token schema version")
    payload = _payload_from_token(token)
    signature = token["signature"]
    issuer = payload.get("issuer", {})
    public_key = issuer.get("public_key")
    if not public_key:
        raise ValueError("Token missing issuer public key")
    if not verify_signature(public_key, payload, signature):
        raise ValueError("Token signature verification failed")
    if is_key_revoked(issuer.get("key_id")):
        raise ValueError(f"Key {issuer.get('key_id')} has been revoked")
    now_dt = now or datetime.now(timezone.utc).replace(microsecond=0)
    expires_at = _parse_iso(payload["expires_at"])
    if expires_at < now_dt:
        raise ValueError("Token has expired")
    token_hash = token_ref(token)
    if is_token_revoked(token_hash):
        raise ValueError("Token has been revoked")
    if require_ledger and not check_token_ledger_membership(token_hash, payload, signature):
        raise ValueError("Token not present in append-only ledger")
    return {
        "status": "verified",
        "token_hash": token_hash,
        "capability": payload.get("capability"),
        "audience_repo": payload.get("audience_repo"),
        "expires_at": payload.get("expires_at"),
    }


def show_token(path: Path) -> Dict[str, Any]:
    token = load_token(path)
    return {
        "token": token,
        "token_hash": token_ref(token),
    }
