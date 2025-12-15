import json
import os
from pathlib import Path

import pytest

from blux_reg import config, crypto, ledger, manifest


@pytest.fixture(autouse=True)
def temp_config(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path / "cfg"))
    config.refresh_paths()
    yield


def test_keygen_creates_keys():
    info = crypto.generate_keypair("test")
    assert info.private_path.exists()
    assert info.public_path.exists()
    assert info.fingerprint


def test_sign_and_verify(tmp_path):
    artifact = tmp_path / "sample.txt"
    artifact.write_text("hello")
    crypto.generate_keypair("test")
    manifest_path, data = manifest.sign_artifact(artifact, "test")
    assert manifest_path.exists()
    assert manifest.verify_manifest(manifest_path)
    assert data["artifact_sha256"]


def test_tamper_manifest(tmp_path):
    artifact = tmp_path / "sample.txt"
    artifact.write_text("hello")
    crypto.generate_keypair("test")
    manifest_path, _ = manifest.sign_artifact(artifact, "test")
    data = json.loads(manifest_path.read_text())
    data["artifact_sha256"] = "0" * 64
    manifest_path.write_text(json.dumps(data))
    assert not manifest.verify_manifest(manifest_path)


def test_ledger_tamper_detection(tmp_path):
    artifact = tmp_path / "sample.txt"
    artifact.write_text("hello")
    crypto.generate_keypair("test")
    manifest.sign_artifact(artifact, "test")
    assert ledger.verify_chain()
    # tamper first line
    ledger_path = config.LEDGER_PATH
    lines = ledger_path.read_text().splitlines()
    lines[0] = lines[0].replace("sign", "signx")
    ledger_path.write_text("\n".join(lines) + "\n")
    assert not ledger.verify_chain()
