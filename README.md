# blux-reg

**Portable, auditable registry + signing/audit chain for BLUX projects**

blux-reg is a local-first registry that lets you:

- Generate cryptographic keys (ed25519 / RSA optional)
- Sign manifests and patch-diffs
- Maintain an append-only audit chain (`ledger.jsonl`)
- Wire into any BLUX project (BLG or standalone)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Quickstart

```bash
# generate keys under ~/.config/blux-reg/keys/
bin/blux-reg keygen

# sign a file
bin/blux-reg sign path/to/file

# verify a signature
bin/blux-reg verify path/to/file path/to/file.sig
```

### Paths
- Config root: `~/.config/blux-reg/` (override with `BLUX_CONFIG_HOME`)
- Keys: `~/.config/blux-reg/keys/`
- Ledger: `~/.config/blux-reg/trust/ledger.jsonl`
- Artifacts: `~/.config/blux-reg/artifacts/`

## Demo (Unified Demo Eligible)
The demo performs key generation (if missing), creates a manifest and patch diff artifact, signs both, verifies signatures, appends ledger entries with prev-hash chaining, and verifies chain integrity.

```bash
bin/blux-reg demo
```

## Doctor
Run health checks for Python version, dependencies, and directory permissions. Exits non-zero with fixes if anything is wrong.

```bash
bin/blux-reg doctor
```

## Audit commands
- `bin/blux-reg audit add-event '{"event":"something"}'`
- `bin/blux-reg audit tail`
- `bin/blux-reg audit verify-chain`

## Artifacts
Demo artifacts and signatures are written under `~/.config/blux-reg/artifacts/`.

## Integration Hooks
- **Lite hook:** call `bin/blux-reg sign <file>` after generating manifests or patches to keep the ledger in sync.
- **Guard hook:** call `bin/blux-reg audit verify-chain` during CI or startup to ensure the trust spine has not been tampered with.

## Support
outervoid.blux@gmail.com

## License
MIT
