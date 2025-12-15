import base64
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519


@dataclass
class KeyPaths:
    private_key: Path
    public_key: Path


DEFAULT_PRIVATE = "ed25519_private.pem"
DEFAULT_PUBLIC = "ed25519_public.pem"


class CryptoError(Exception):
    pass


def generate_ed25519_keypair(key_dir: Path) -> KeyPaths:
    key_dir.mkdir(parents=True, exist_ok=True)
    private_path = key_dir / DEFAULT_PRIVATE
    public_path = key_dir / DEFAULT_PUBLIC

    if private_path.exists() or public_path.exists():
        # do not overwrite silently
        raise CryptoError("Keys already exist; refusing to overwrite")

    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    private_path.write_bytes(private_bytes)
    public_path.write_bytes(public_bytes)

    private_path.chmod(0o600)
    return KeyPaths(private_key=private_path, public_key=public_path)


def load_private_key(path: Path) -> ed25519.Ed25519PrivateKey:
    try:
        data = path.read_bytes()
        return serialization.load_pem_private_key(data, password=None)
    except Exception as exc:  # pragma: no cover - narrow context
        raise CryptoError(f"Failed to load private key: {exc}") from exc


def load_public_key(path: Path) -> ed25519.Ed25519PublicKey:
    try:
        data = path.read_bytes()
        return serialization.load_pem_public_key(data)
    except Exception as exc:  # pragma: no cover - narrow context
        raise CryptoError(f"Failed to load public key: {exc}") from exc


def sign_bytes(data: bytes, private_key_path: Path) -> bytes:
    priv = load_private_key(private_key_path)
    return priv.sign(data)


def verify_bytes(data: bytes, signature: bytes, public_key_path: Path) -> bool:
    pub = load_public_key(public_key_path)
    try:
        pub.verify(signature, data)
        return True
    except Exception:
        return False


def fingerprint_from_public_key(public_key_path: Path) -> str:
    pub_bytes = load_public_key(public_key_path).public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    digest = hashes.Hash(hashes.SHA256())
    digest.update(pub_bytes)
    return digest.finalize().hex()


def sign_file(path: Path, private_key_path: Path) -> Tuple[bytes, Path]:
    data = path.read_bytes()
    signature = sign_bytes(data, private_key_path)
    sig_path = path.with_suffix(path.suffix + ".sig")
    sig_path.write_bytes(base64.b64encode(signature))
    return signature, sig_path


def verify_file(path: Path, signature_path: Path, public_key_path: Path) -> bool:
    data = path.read_bytes()
    sig_bytes = base64.b64decode(signature_path.read_bytes())
    return verify_bytes(data, sig_bytes, public_key_path)


__all__ = [
    "KeyPaths",
    "CryptoError",
    "DEFAULT_PRIVATE",
    "DEFAULT_PUBLIC",
    "generate_ed25519_keypair",
    "load_private_key",
    "load_public_key",
    "sign_bytes",
    "verify_bytes",
    "sign_file",
    "verify_file",
    "fingerprint_from_public_key",
]
