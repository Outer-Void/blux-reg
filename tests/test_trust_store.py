from datetime import datetime, timezone

from blux_reg import config, crypto, load_trust_store, revoke_token, save_trust_store, verify_token
from blux_reg.trust_store import new_trust_anchor
from blux_reg.tokens import issue_capability_token


def _setup_key(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()
    crypto.generate_keypair("issuer")


def test_trust_store_revocation(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, _ = issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-example",
        3600,
        {},
    )
    store_path = tmp_path / "trust_store.jsonl"
    store = load_trust_store(store_path)

    public_key = crypto.load_public_key("issuer")
    public_pem = crypto.export_key("issuer", public=True).decode("utf-8")
    anchor = new_trust_anchor(crypto.fingerprint_public_key(public_key), public_pem)
    store.add_entry(anchor)
    save_trust_store(store_path, store)

    result = verify_token(token, store_path, now=datetime.now(timezone.utc))
    assert result["valid"] is True

    revoke_token(token_hash, "compromised", store_path)
    result = verify_token(token, store_path, now=datetime.now(timezone.utc))
    assert result["valid"] is False
    assert "revoked" in result["reason_codes"]
