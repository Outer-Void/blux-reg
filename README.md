# BLUX-Reg

**Identity and trust backbone for the BLUX ecosystem.**

BLUX-Reg now unifies project validation, plugin signing, and user verification
into a local-first workflow powered by modern cryptography. It couples
Ed25519 keys with Argon2-protected passphrases and records every trust event in
append-only JSONL ledgers under `~/blux-reg/registry/`, ensuring compatibility
with BLUX-Quantum and BLUX-Guard stakeholders.

## Highlights

- 🛡️ **Role-specific keys** – generate project, plugin, and user keypairs with
  Ed25519, protected by Argon2 passphrases.
- 📓 **Append-only audit ledgers** – JSON Lines registries for keys, artifacts,
  and revocations, each hashed into a tamper-evident chain.
- 🔐 **Offline trust** – signatures include their public keys and ledger
  membership proofs so artifacts can be validated without network access.
- ♻️ **Revocable identities** – append revocation records that invalidate keys
  across the ecosystem.
- 🤝 **BLUX-Quantum & BLUX-Guard ready** – compatibility data is embedded in
  every ledger record for downstream tooling.

## Getting started

```bash
# Initialise directories and ledgers
bin/blux-reg init

# Create a project key (prompts for a new passphrase)
bin/blux-reg keys create my-project project

# List and export keys
bin/blux-reg keys list
bin/blux-reg keys export my-project --key-type project

# Sign an artifact (manifest, plugin bundle, release archive, etc.)
bin/blux-reg sign path/to/artifact.zip my-project project "release"

# Verify offline – uses the saved signature JSON + registry audit
bin/blux-reg verify path/to/artifact.zip

# Revoke a compromised key
bin/blux-reg keys revoke my-project --reason "compromised" --revoker trust-board

# Inspect ledger integrity
bin/blux-reg audit artifacts
```

Signature files are written to `~/blux-reg/signatures/` and include the
payload, signature, and public key to enable air-gapped verification. Every
operation appends to the appropriate ledger under `~/blux-reg/registry/` which
can be replicated or inspected independently.

## Directory layout

```
~/blux-reg/
├── registry/
│   ├── keys.jsonl        # key issuance events
│   ├── artifacts.jsonl   # signed artifacts + compatibility metadata
│   └── revocations.jsonl # key revocation log
├── signatures/           # detached signature bundles (.sig.json)
└── manifests/, bin/, …   # optional project-specific files
```

## License

MIT
