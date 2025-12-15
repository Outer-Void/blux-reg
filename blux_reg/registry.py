from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, Optional

from .crypto import KeyMaterial, generate_ed25519, now_iso, sign_payload, verify_signature
from .keystore import KeyStore
from .ledger import LedgerEntry, get_ledger
from .paths import LEDGER_PATHS, REQUIRED_COMPATIBILITY, SIGNATURES_ROOT


def ensure_structure() -> None:
    SIGNATURES_ROOT.mkdir(parents=True, exist_ok=True)
    for path in LEDGER_PATHS.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.touch()


def create_key(key_id: str, key_type: str, passphrase: str, keystore: Optional[KeyStore] = None) -> KeyMaterial:
    ensure_structure()
    ks = keystore or KeyStore()
    compatibility = {
        "BLUX-Quantum": REQUIRED_COMPATIBILITY["BLUX-Quantum"],
        "BLUX-Guard": REQUIRED_COMPATIBILITY["BLUX-Guard"],
    }
    material = generate_ed25519(passphrase, key_id=key_id, key_type=key_type, compatibility=compatibility)
    ks.save(material)
    payload = {
        "event": "key_issued",
        "timestamp": material.created_at,
        "key_id": material.key_id,
        "key_type": material.key_type,
        "public_key": material.public_key,
        "compatibility": compatibility,
    }
    signature = sign_payload(material, payload, passphrase)
    get_ledger("keys").append({
        "timestamp": material.created_at,
        "issuer": material.key_id,
        "role": material.key_type,
        "payload": payload,
        "signature": signature,
    })
    return material


def list_keys(keystore: Optional[KeyStore] = None) -> Iterable[KeyMaterial]:
    ks = keystore or KeyStore()
    yield from ks.list()


def export_public_key(material: KeyMaterial) -> dict:
    return {
        "key_id": material.key_id,
        "key_type": material.key_type,
        "public_key": material.public_key,
        "created_at": material.created_at,
        "compatibility": material.compatibility,
    }


def sign_artifact(
    key_id: str,
    key_type: str,
    path: Path,
    passphrase: str,
    context: str,
    keystore: Optional[KeyStore] = None,
) -> Path:
    ensure_structure()
    ks = keystore or KeyStore()
    material = ks.load(key_id, key_type)
    payload = {
        "event": "artifact_signed",
        "timestamp": now_iso(),
        "artifact": {
            "path": str(path.resolve()),
            "sha256": compute_file_sha256(path),
            "context": context,
        },
        "key_id": material.key_id,
        "key_type": material.key_type,
        "compatibility": material.compatibility,
    }
    signature = sign_payload(material, payload, passphrase)
    entry = {
        "timestamp": payload["timestamp"],
        "issuer": material.key_id,
        "role": material.key_type,
        "payload": payload,
        "signature": signature,
    }
    get_ledger("artifacts").append(entry)
    signature_path = SIGNATURES_ROOT / f"{path.name}.sig.json"
    signature_payload = {
        "payload": payload,
        "signature": signature,
        "public_key": material.public_key,
    }
    with signature_path.open("w", encoding="utf-8") as fh:
        json.dump(signature_payload, fh, indent=2, sort_keys=True)
    return signature_path


def compute_file_sha256(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def revoke_key(key_id: str, reason: str, revoker: str) -> LedgerEntry:
    ensure_structure()
    payload = {
        "event": "key_revoked",
        "timestamp": now_iso(),
        "revoked_key_id": key_id,
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


def is_key_revoked(key_id: str) -> bool:
    ledger = get_ledger("revocations")
    for entry in ledger.entries():
        payload = entry.raw.get("payload", {})
        if payload.get("event") == "key_revoked" and payload.get("revoked_key_id") == key_id:
            return True
    return False


def verify_artifact(path: Path, signature_path: Optional[Path] = None) -> Dict[str, str]:
    ensure_structure()
    if signature_path is None:
        signature_path = SIGNATURES_ROOT / f"{path.name}.sig.json"
    if not signature_path.exists():
        raise FileNotFoundError(f"Signature file {signature_path} not found")
    with signature_path.open("r", encoding="utf-8") as fh:
        signed = json.load(fh)
    payload = signed["payload"]
    signature = signed["signature"]
    public_key = signed["public_key"]
    expected_sha = compute_file_sha256(path)
    if payload["artifact"]["sha256"] != expected_sha:
        raise ValueError("Artifact digest mismatch")
    key_id = payload.get("key_id")
    if is_key_revoked(key_id):
        raise ValueError(f"Key {key_id} has been revoked")
    if not verify_signature(public_key, payload, signature):
        raise ValueError("Signature verification failed")
    if not check_ledger_membership(payload, signature):
        raise ValueError("Signature not present in append-only ledger")
    return {
        "status": "verified",
        "key_id": key_id,
        "key_type": payload.get("key_type"),
        "timestamp": payload.get("timestamp"),
        "context": payload["artifact"].get("context"),
    }


def check_ledger_membership(payload: dict, signature: str) -> bool:
    ledger = get_ledger("artifacts")
    for entry in ledger.entries():
        if entry.raw.get("signature") == signature and entry.raw.get("payload") == payload:
            return True
    return False
