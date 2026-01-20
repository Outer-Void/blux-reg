import importlib
from datetime import datetime, timedelta

import pytest


def _reload_modules(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    import blux_reg.paths as paths
    importlib.reload(paths)
    import blux_reg.ledger as ledger
    importlib.reload(ledger)
    import blux_reg.keystore as keystore
    importlib.reload(keystore)
    import blux_reg.registry as registry
    importlib.reload(registry)
    import blux_reg.tokens as tokens
    importlib.reload(tokens)
    return registry, tokens


def _setup_key(registry):
    return registry.create_key("project-alpha", "project", "secret")


def test_token_validates(tmp_path, monkeypatch):
    registry, tokens = _reload_modules(tmp_path, monkeypatch)
    _setup_key(registry)
    token, token_hash, _ = tokens.issue_capability_token(
        "project-alpha",
        "project",
        "secret",
        "publish",
        "outer-void/blux-guard",
        3600,
        {"scope": "release"},
    )
    result = tokens.verify_capability_token(token)
    assert result["token_hash"] == token_hash


def test_token_expired_fails(tmp_path, monkeypatch):
    registry, tokens = _reload_modules(tmp_path, monkeypatch)
    _setup_key(registry)
    token, _, _ = tokens.issue_capability_token(
        "project-alpha",
        "project",
        "secret",
        "publish",
        "outer-void/blux-guard",
        1,
        {},
    )
    expires_at = datetime.fromisoformat(token["expires_at"])
    with pytest.raises(ValueError, match="expired"):
        tokens.verify_capability_token(token, now=expires_at + timedelta(seconds=1))


def test_token_revoked_fails(tmp_path, monkeypatch):
    registry, tokens = _reload_modules(tmp_path, monkeypatch)
    _setup_key(registry)
    token, token_hash, _ = tokens.issue_capability_token(
        "project-alpha",
        "project",
        "secret",
        "publish",
        "outer-void/blux-guard",
        3600,
        {},
    )
    tokens.revoke_capability_token(token_hash, "compromised", "security-team")
    with pytest.raises(ValueError, match="revoked"):
        tokens.verify_capability_token(token)


def test_token_tampered_fails(tmp_path, monkeypatch):
    registry, tokens = _reload_modules(tmp_path, monkeypatch)
    _setup_key(registry)
    token, _, _ = tokens.issue_capability_token(
        "project-alpha",
        "project",
        "secret",
        "publish",
        "outer-void/blux-guard",
        3600,
        {},
    )
    token["capability"] = "delete"
    with pytest.raises(ValueError, match="signature"):
        tokens.verify_capability_token(token)
