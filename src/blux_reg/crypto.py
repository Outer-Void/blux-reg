"""Key management helpers using Ed25519."""
from __future__ import annotations

import base64
from pathlib import Path
from typing import List, Optional

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

from . import config
from .util import sha256_hex


class KeyInfo:
    def __init__(self, name: str, private_path: Path, public_path: Path, fingerprint: str):
        self.name = name
        self.private_path = private_path
        self.public_path = public_path
        self.fingerprint = fingerprint

    def as_dict(self):
        return {
            "name": self.name,
            "private_path": str(self.private_path),
            "public_path": str(self.public_path),
            "fingerprint": self.fingerprint,
        }


def _key_paths(name: str) -> tuple[Path, Path]:
    priv = config.KEYS_DIR / f"{name}.pem"
    pub = config.KEYS_DIR / f"{name}.pub.pem"
    return priv, pub


def fingerprint_public_key(public_key: ed25519.Ed25519PublicKey) -> str:
    raw = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )
    return sha256_hex(raw)


def generate_keypair(name: str, force: bool = False) -> KeyInfo:
    config.ensure_directories()
    priv_path, pub_path = _key_paths(name)
    if not force and (priv_path.exists() or pub_path.exists()):
        raise FileExistsError(f"Key '{name}' already exists")
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    fingerprint = fingerprint_public_key(public_key)

    priv_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pub_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    priv_path.write_bytes(priv_bytes)
    pub_path.write_bytes(pub_bytes)
    priv_path.chmod(0o600)
    return KeyInfo(name, priv_path, pub_path, fingerprint)


def list_keys() -> List[KeyInfo]:
    infos: List[KeyInfo] = []
    if not config.KEYS_DIR.exists():
        return infos
    for priv_path in sorted(config.KEYS_DIR.glob("*.pem")):
        if priv_path.name.endswith(".pub.pem"):
            continue
        name = priv_path.stem
        pub_path = config.KEYS_DIR / f"{name}.pub.pem"
        if not pub_path.exists():
            continue
        public_key = load_public_key(name)
        fingerprint = fingerprint_public_key(public_key)
        infos.append(KeyInfo(name, priv_path, pub_path, fingerprint))
    return infos


def load_private_key(name: str) -> ed25519.Ed25519PrivateKey:
    priv_path, _ = _key_paths(name)
    data = priv_path.read_bytes()
    return serialization.load_pem_private_key(data, password=None)


def load_public_key(name: str) -> ed25519.Ed25519PublicKey:
    _, pub_path = _key_paths(name)
    data = pub_path.read_bytes()
    return serialization.load_pem_public_key(data)


def find_public_key_by_fingerprint(fingerprint: str) -> Optional[ed25519.Ed25519PublicKey]:
    for info in list_keys():
        if info.fingerprint == fingerprint:
            return load_public_key(info.name)
    return None


def export_key(name: str, public: bool = True) -> bytes:
    if public:
        _, pub = _key_paths(name)
        return pub.read_bytes()
    priv, _ = _key_paths(name)
    return priv.read_bytes()


def import_private_key(path: Path, name: str) -> KeyInfo:
    data = Path(path).read_bytes()
    private_key = serialization.load_pem_private_key(data, password=None)
    if not isinstance(private_key, ed25519.Ed25519PrivateKey):
        raise ValueError("Only Ed25519 private keys are supported")
    public_key = private_key.public_key()
    fingerprint = fingerprint_public_key(public_key)
    priv_path, pub_path = _key_paths(name)
    priv_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pub_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    priv_path.write_bytes(priv_bytes)
    pub_path.write_bytes(pub_bytes)
    priv_path.chmod(0o600)
    return KeyInfo(name, priv_path, pub_path, fingerprint)


def sign_message(name: str, message: bytes) -> str:
    private_key = load_private_key(name)
    signature = private_key.sign(message)
    return base64.b64encode(signature).decode()


def verify_signature(public_key: ed25519.Ed25519PublicKey, message: bytes, signature_b64: str) -> bool:
    try:
        public_key.verify(base64.b64decode(signature_b64), message)
        return True
    except Exception:
        return False
