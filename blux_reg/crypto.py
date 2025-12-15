from __future__ import annotations

import base64
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from nacl import signing

from .ledger import canonical_bytes

PASSWORD_HASHER = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=2, hash_len=32, salt_len=16)


@dataclass
class KeyMaterial:
    key_id: str
    key_type: str
    created_at: str
    public_key: str
    private_seed: str
    argon2_hash: str
    compatibility: dict

    def signing_key(self, passphrase: Optional[str] = None) -> signing.SigningKey:
        seed = base64.b64decode(self.private_seed)
        if passphrase is not None:
            verify_passphrase(self.argon2_hash, passphrase)
        return signing.SigningKey(seed)

    def verify_key(self) -> signing.VerifyKey:
        raw_public = base64.b64decode(self.public_key)
        return signing.VerifyKey(raw_public)


class PassphraseError(Exception):
    pass


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def generate_ed25519(passphrase: str, key_id: str, key_type: str, compatibility: Optional[dict] = None) -> KeyMaterial:
    signing_key = signing.SigningKey.generate()
    verify_key = signing_key.verify_key
    private_seed = signing_key.encode()
    public_bytes = verify_key.encode()
    argon_hash = PASSWORD_HASHER.hash(passphrase)
    return KeyMaterial(
        key_id=key_id,
        key_type=key_type,
        created_at=now_iso(),
        public_key=base64.b64encode(public_bytes).decode("ascii"),
        private_seed=base64.b64encode(private_seed).decode("ascii"),
        argon2_hash=argon_hash,
        compatibility=compatibility or {},
    )


def verify_passphrase(stored_hash: str, candidate: str) -> None:
    try:
        PASSWORD_HASHER.verify(stored_hash, candidate)
    except VerifyMismatchError as exc:
        raise PassphraseError("Invalid passphrase") from exc


def sign_payload(material: KeyMaterial, payload: dict, passphrase: str) -> str:
    signing_key = material.signing_key(passphrase)
    signature = signing_key.sign(canonical_bytes(payload)).signature
    return base64.b64encode(signature).decode("ascii")


def verify_signature(public_key_b64: str, payload: dict, signature_b64: str) -> bool:
    verify_key = signing.VerifyKey(base64.b64decode(public_key_b64))
    try:
        verify_key.verify(canonical_bytes(payload), base64.b64decode(signature_b64))
        return True
    except Exception:
        return False
