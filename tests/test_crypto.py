from blux_reg import config, crypto


def test_keygen_sign_verify(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()
    crypto.generate_keypair("test")

    message = b"hello"
    signature = crypto.sign_message("test", message)
    public_key = crypto.load_public_key("test")
    assert crypto.verify_signature(public_key, message, signature)
    assert not crypto.verify_signature(public_key, b"tamper", signature)
