# blux-reg

Local-first signing, verification, and append-only auditing for BLUX (Lite / Commander / Quantum / Guard / Doctrine) demos.

## Highlights
- Ed25519 key management with import/export and stable fingerprints
- Deterministic artifact manifests (JSON) and verification
- Append-only JSONL ledger with tamper-evident hash chain
- CLI entrypoint `blux-reg` (non-interactive by default)
- Works on Linux, macOS, and Termux with no network access required

## Installation

```bash
python -m pip install --upgrade pip
pip install -e .
```

## Quickstart

```bash
# initialize local state
blux-reg init

# create a demo key
blux-reg keygen --name demo

# sign a file
echo "hello" > /tmp/example.txt
blux-reg sign /tmp/example.txt --key-name demo

# verify the manifest that was emitted next to the file
blux-reg verify /tmp/example.txt.blux-manifest.json

# inspect the audit chain
blux-reg audit tail
blux-reg audit verify-chain
```

## CLI reference
- `blux-reg status [--json]`
- `blux-reg keygen [--name NAME] [--force]`
- `blux-reg key list`
- `blux-reg key export --name NAME [--public/--private] [--output FILE]`
- `blux-reg key import PATH [--name NAME]`
- `blux-reg sign <artifact> [--key-name NAME] [--output FILE]`
- `blux-reg verify <manifest>`
- `blux-reg audit add-event "message" [--actor FINGERPRINT]`
- `blux-reg audit tail [-n N] [--json]`
- `blux-reg audit verify-chain`

See [`docs/CONTRACT.md`](docs/CONTRACT.md) for the stable schemas and path layout.

## Integration notes (BLUX Lite / Commander)
- Prefer `BLUX_REG_CONFIG_DIR` to isolate per-project state in CI or demos.
- `blux-reg status --json` provides machine-readable health (key count, ledger size, last hash).
- A signed manifest includes `artifact_path`, `artifact_sha256`, `key_fingerprint`, and a base64 signature; verification recomputes all fields.
- The ledger is JSONL and append-only: `prev_hash` must match the prior `entry_hash` or `audit verify-chain` will fail.

## Demo script
Run the fast start-to-finish demo:

```bash
./scripts/demo_unified_reg.sh
```

## Local-first trust
All state (keys, manifests, ledger) lives under `~/.config/blux-reg/` by default. Nothing is fetched from the network; every operation is deterministic for the same inputs and keys. Tampering with either manifests or the ledger is detectable via `verify` and `audit verify-chain`.

## License

Apache-2.0 (see [LICENSE](LICENSE)).
