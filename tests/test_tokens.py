from datetime import datetime, timedelta, timezone

import pytest

from blux_reg import config, crypto, tokens


def _setup_key(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()
    crypto.generate_keypair("issuer")


def test_token_validates(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-guard",
        3600,
        {"scope": "release"},
    )
    result = tokens.verify_capability_token(token)
    assert result["token_hash"] == token_hash


def test_token_expired_fails(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, _, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-guard",
        1,
        {},
    )
    expires_at = datetime.fromisoformat(token["expires_at"])
    with pytest.raises(ValueError, match="expired"):
        tokens.verify_capability_token(token, now=expires_at + timedelta(seconds=1))


def test_token_revoked_fails(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-guard",
        3600,
        {},
    )
    tokens.revoke_capability_token(token_hash, "compromised", "security-team")
    with pytest.raises(ValueError, match="revoked"):
        tokens.verify_capability_token(token)


def test_token_tampered_fails(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, _, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-guard",
        3600,
        {},
    )
    token["capability"] = "delete"
    with pytest.raises(ValueError, match="signature"):
        tokens.verify_capability_token(token)


def test_token_hash_roundtrip(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, path = tokens.issue_capability_token(
        "issuer",
        "deploy",
        "outer-void/blux-guard",
        3600,
        {},
    )
    assert tokens.hash_token_file(path) == token_hash
    now = datetime.now(timezone.utc).replace(microsecond=0)
    assert tokens.verify_capability_token(token, now=now)["status"] == "verified"
