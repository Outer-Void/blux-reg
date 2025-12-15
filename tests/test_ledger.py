import json
from pathlib import Path

from blux_reg import paths
from blux_reg.crypto import DEFAULT_PRIVATE, DEFAULT_PUBLIC, generate_ed25519_keypair, sign_bytes
from blux_reg.ledger import append_entry, load_entries, verify_chain


def test_ledger_chain_and_tamper(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_CONFIG_HOME", str(tmp_path))
    key_dir = paths.get_keys_dir()
    generate_ed25519_keypair(key_dir)
    public_path = key_dir / DEFAULT_PUBLIC
    private_path = key_dir / DEFAULT_PRIVATE

    payload1 = {"event": "first"}
    sig1 = sign_bytes(json.dumps(payload1, sort_keys=True).encode(), private_path)
    append_entry("event", payload1, sig1.hex(), public_path)

    payload2 = {"event": "second"}
    sig2 = sign_bytes(json.dumps(payload2, sort_keys=True).encode(), private_path)
    append_entry("event", payload2, sig2.hex(), public_path)

    assert verify_chain()

    ledger_path = paths.get_ledger_path()
    lines = ledger_path.read_text().splitlines()
    # tamper first line
    tampered = json.loads(lines[0])
    tampered["payload"]["event"] = "tamper"
    lines[0] = json.dumps(tampered)
    ledger_path.write_text("\n".join(lines) + "\n")

    assert not verify_chain()
