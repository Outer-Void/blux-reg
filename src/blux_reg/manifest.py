"""Manifest creation and verification."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Tuple

from . import config, crypto, ledger
from .util import canonical_json, sha256_hex, write_json


REQUIRED_FIELDS = {
    "schema_version",
    "artifact_path",
    "artifact_sha256",
    "created_at",
    "key_fingerprint",
    "signature",
}


def _artifact_hash(path: Path) -> str:
    data = path.read_bytes()
    return sha256_hex(data)


def sign_artifact(artifact_path: Path, key_name: str, output: Path | None = None) -> Tuple[Path, Dict[str, str]]:
    artifact_path = artifact_path.expanduser().resolve()
    if not artifact_path.exists():
        raise FileNotFoundError(f"Artifact not found: {artifact_path}")
    config.ensure_directories()
    artifact_hash = _artifact_hash(artifact_path)
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    manifest = {
        "schema_version": config.SCHEMA_VERSION,
        "artifact_path": artifact_path.name,
        "artifact_sha256": artifact_hash,
        "created_at": created_at,
        "key_fingerprint": crypto.fingerprint_public_key(crypto.load_public_key(key_name)),
    }
    message = canonical_json(manifest).encode()
    signature = crypto.sign_message(key_name, message)
    manifest["signature"] = signature
    manifest_path = output or artifact_path.with_suffix(artifact_path.suffix + ".blux-manifest.json")
    write_json(manifest_path, manifest)
    manifest_hash = sha256_hex(canonical_json(manifest).encode())
    ledger.append_entry(
        action="sign",
        actor=manifest["key_fingerprint"],
        payload_summary=f"manifest:{manifest_path.name}",
        artifact_hash=artifact_hash,
        manifest_hash=manifest_hash,
    )
    return manifest_path, manifest


def _resolve_artifact(manifest_path: Path, artifact_name: str) -> Path:
    candidate = manifest_path.parent / artifact_name
    return candidate


def verify_manifest(manifest_path: Path) -> bool:
    manifest_path = manifest_path.expanduser().resolve()
    with manifest_path.open("r", encoding="utf-8") as f:
        manifest = json.load(f)
    missing = REQUIRED_FIELDS - manifest.keys()
    if missing:
        raise ValueError(f"Manifest missing fields: {sorted(missing)}")
    artifact_path = _resolve_artifact(manifest_path, manifest["artifact_path"])
    if not artifact_path.exists():
        raise FileNotFoundError(f"Artifact referenced in manifest not found: {artifact_path}")
    expected_hash = _artifact_hash(artifact_path)
    if expected_hash != manifest["artifact_sha256"]:
        return False
    public_key = crypto.find_public_key_by_fingerprint(manifest["key_fingerprint"])
    if public_key is None:
        raise FileNotFoundError("No public key with matching fingerprint found")
    message_fields = {k: manifest[k] for k in manifest if k != "signature"}
    message = canonical_json(message_fields).encode()
    return crypto.verify_signature(public_key, message, manifest["signature"])
