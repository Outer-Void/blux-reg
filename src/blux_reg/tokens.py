"""Capability token issuance and verification."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

from cryptography.hazmat.primitives import serialization

from . import config, crypto, ledger
from .util import canonical_json, load_json, sha256_hex, write_json


TOKEN_SCHEMA_VERSION = "1.0"
TOKEN_TYPE = "capability"
REQUIRED_FIELDS = {
    "schema_version",
    "token_type",
    "issued_at",
    "expires_at",
    "ttl_seconds",
    "capability",
    "audience",
    "constraints",
    "issuer",
    "signature",
}


def _token_dirs() -> Tuple[Path, Path]:
    return config.TOKENS_DIR, config.REVOCATIONS_PATH


def _parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def _payload_from_token(token: Dict[str, Any]) -> Dict[str, Any]:
    return {k: token[k] for k in token if k != "signature"}


def token_ref(token: Dict[str, Any]) -> str:
    return sha256_hex(canonical_json(token).encode())


def hash_token_file(path: Path) -> str:
    token = load_json(path)
    return token_ref(token)


def _issuer_block(key_name: str) -> Dict[str, str]:
    public_bytes = crypto.export_key(key_name, public=True)
    public_key = crypto.load_public_key(key_name)
    return {
        "key_name": key_name,
        "fingerprint": crypto.fingerprint_public_key(public_key),
        "public_key": public_bytes.decode("utf-8"),
    }


def issue_capability_token(
    key_name: str,
    capability: str,
    audience: str,
    ttl_seconds: int,
    constraints: Optional[Dict[str, Any]] = None,
    output_path: Optional[Path] = None,
) -> Tuple[Dict[str, Any], str, Path]:
    if ttl_seconds <= 0:
        raise ValueError("ttl_seconds must be positive")
    config.ensure_directories()
    tokens_dir, _ = _token_dirs()
    tokens_dir.mkdir(parents=True, exist_ok=True)
    issued_at = datetime.now(timezone.utc).replace(microsecond=0)
    expires_at = issued_at + timedelta(seconds=ttl_seconds)
    payload = {
        "schema_version": TOKEN_SCHEMA_VERSION,
        "token_type": TOKEN_TYPE,
        "issued_at": issued_at.isoformat(),
        "expires_at": expires_at.isoformat(),
        "ttl_seconds": ttl_seconds,
        "capability": capability,
        "audience": audience,
        "constraints": constraints or {},
        "issuer": _issuer_block(key_name),
    }
    signature = crypto.sign_message(key_name, canonical_json(payload).encode())
    token = dict(payload)
    token["signature"] = signature
    token_hash = token_ref(token)
    path = output_path or (tokens_dir / f"{token_hash}.json")
    write_json(path, token)
    ledger.append_entry(
        action="token-issue",
        actor=payload["issuer"]["fingerprint"],
        payload_summary=f"capability:{capability}",
        extra={"token_hash": token_hash},
    )
    return token, token_hash, path


def load_token(path: Path) -> Dict[str, Any]:
    return load_json(path)


def _load_public_key(public_pem: str):
    return serialization.load_pem_public_key(public_pem.encode("utf-8"))


def is_token_revoked(token_hash: str) -> bool:
    _, revocations_path = _token_dirs()
    if not revocations_path.exists():
        return False
    with revocations_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            entry = json.loads(line)
            if entry.get("token_hash") == token_hash:
                return True
    return False


def revoke_capability_token(token_hash: str, reason: str, revoker: str) -> Dict[str, Any]:
    config.ensure_directories()
    _, revocations_path = _token_dirs()
    entry = {
        "schema_version": "1.0",
        "token_hash": token_hash,
        "revoked_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "reason": reason,
        "revoker": revoker,
    }
    revocations_path.parent.mkdir(parents=True, exist_ok=True)
    with revocations_path.open("a", encoding="utf-8") as fh:
        fh.write(canonical_json(entry) + "\n")
    ledger.append_entry(
        action="token-revoke",
        actor=revoker,
        payload_summary=f"token:{token_hash}",
        extra={"token_hash": token_hash, "reason": reason},
    )
    return entry


def verify_capability_token(
    token: Dict[str, Any],
    now: Optional[datetime] = None,
    trust_anchors: Optional[set[str]] = None,
    revoked_tokens: Optional[set[str]] = None,
) -> Dict[str, str]:
    missing = REQUIRED_FIELDS - token.keys()
    if missing:
        raise ValueError(f"Token missing fields: {sorted(missing)}")
    if token.get("token_type") != TOKEN_TYPE:
        raise ValueError("Token type mismatch")
    if token.get("schema_version") != TOKEN_SCHEMA_VERSION:
        raise ValueError("Unsupported token schema version")
    payload = _payload_from_token(token)
    issuer = payload.get("issuer", {})
    public_key_pem = issuer.get("public_key")
    if not public_key_pem:
        raise ValueError("Token missing issuer public key")
    public_key = _load_public_key(public_key_pem)
    message = canonical_json(payload).encode()
    if not crypto.verify_signature(public_key, message, token["signature"]):
        raise ValueError("Token signature verification failed")
    if trust_anchors is not None:
        issuer_fingerprint = issuer.get("fingerprint")
        if not issuer_fingerprint or issuer_fingerprint not in trust_anchors:
            raise ValueError("Token issuer not trusted")
    now_dt = now or datetime.now(timezone.utc).replace(microsecond=0)
    expires_at = _parse_iso(payload["expires_at"])
    if expires_at < now_dt:
        raise ValueError("Token has expired")
    token_hash = token_ref(token)
    if revoked_tokens is not None:
        if token_hash in revoked_tokens:
            raise ValueError("Token has been revoked")
    elif is_token_revoked(token_hash):
        raise ValueError("Token has been revoked")
    return {
        "status": "verified",
        "token_hash": token_hash,
        "capability": payload.get("capability"),
        "audience": payload.get("audience"),
        "expires_at": payload.get("expires_at"),
    }
