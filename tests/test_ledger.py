import json

from blux_reg import config, ledger


def test_ledger_chain_and_tamper(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()

    ledger.append_entry(action="event", actor="tester", payload_summary="first")
    ledger.append_entry(action="event", actor="tester", payload_summary="second")

    assert ledger.verify_chain()

    ledger_path = config.LEDGER_PATH
    lines = ledger_path.read_text().splitlines()
    tampered = json.loads(lines[0])
    tampered["action"] = "tamper"
    lines[0] = json.dumps(tampered)
    ledger_path.write_text("\n".join(lines) + "\n")

    assert not ledger.verify_chain()
