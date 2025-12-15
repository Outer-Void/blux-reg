import os
from pathlib import Path

from blux_reg import paths
from blux_reg.crypto import DEFAULT_PRIVATE, DEFAULT_PUBLIC, generate_ed25519_keypair, sign_file, verify_file


def test_keygen_sign_verify(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_CONFIG_HOME", str(tmp_path))
    key_dir = paths.get_keys_dir()
    generate_ed25519_keypair(key_dir)

    target = tmp_path / "sample.txt"
    target.write_text("hello")

    signature, sig_path = sign_file(target, key_dir / DEFAULT_PRIVATE)
    assert sig_path.exists()
    assert verify_file(target, sig_path, key_dir / DEFAULT_PUBLIC)

    # signature should fail on modification
    target.write_text("tamper")
    assert not verify_file(target, sig_path, key_dir / DEFAULT_PUBLIC)
