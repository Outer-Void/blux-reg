"""Public API surface for BLUX-Reg trust kernel."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from . import tokens
from .trust_store import (
    TrustStore,
    load_trust_store as _load_trust_store,
    new_token_revocation,
    save_trust_store as _save_trust_store,
    trust_store_index,
)


def issue_token(
    claims: Dict[str, Any],
    issuer_key: str,
    ttl: int,
    constraints: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Issue a capability token from structured claims.

    Required claim fields: ``capability`` and ``audience``.
    """
    if not isinstance(claims, dict):
        raise ValueError("claims must be a dict")
    capability = claims.get("capability")
    audience = claims.get("audience")
    if not capability or not audience:
        raise ValueError("claims must include capability and audience")
    token, token_hash, path = tokens.issue_capability_token(
        key_name=issuer_key,
        capability=capability,
        audience=audience,
        ttl_seconds=ttl,
        constraints=constraints or claims.get("constraints") or {},
    )
    return {"token": token, "token_hash": token_hash, "path": str(path)}


def verify_token(
    token: Dict[str, Any],
    trust_store: TrustStore | Path | str,
    now: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Verify a capability token against a trust store."""
    store = _resolve_store(trust_store)
    index = trust_store_index(store)
    try:
        result = tokens.verify_capability_token(
            token,
            now=now,
            trust_anchors=index["trusted_issuers"] or None,
            revoked_tokens=index["revoked_tokens"] or None,
        )
        return {
            "valid": True,
            "reason_codes": [],
            "token_hash": result.get("token_hash"),
            "capability": result.get("capability"),
            "audience": result.get("audience"),
            "expires_at": result.get("expires_at"),
        }
    except ValueError as exc:
        return {
            "valid": False,
            "reason_codes": [_reason_code(str(exc))],
        }


def revoke_token(token_id: str, reason: str, store: TrustStore | Path | str) -> Dict[str, Any]:
    """Revoke a token by hash in the trust store."""
    trust_store = _resolve_store(store)
    entry = trust_store.add_entry(new_token_revocation(token_id, reason))
    save_trust_store(trust_store.path, trust_store)
    return entry


def load_trust_store(path: Path | str) -> TrustStore:
    return _load_trust_store(Path(path))


def save_trust_store(path: Path | str, store: TrustStore) -> None:
    _save_trust_store(Path(path), store)


def _resolve_store(store: TrustStore | Path | str) -> TrustStore:
    if isinstance(store, TrustStore):
        return store
    return _load_trust_store(Path(store))


def _reason_code(message: str) -> str:
    lowered = message.lower()
    if "missing fields" in lowered:
        return "missing_fields"
    if "token type" in lowered:
        return "token_type_mismatch"
    if "unsupported token schema" in lowered:
        return "unsupported_schema"
    if "missing issuer public key" in lowered:
        return "missing_issuer_key"
    if "signature verification" in lowered:
        return "invalid_signature"
    if "expired" in lowered:
        return "expired"
    if "revoked" in lowered:
        return "revoked"
    if "issuer not trusted" in lowered:
        return "untrusted_issuer"
    return "invalid"
