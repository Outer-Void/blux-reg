# BLUX-Reg

> **Identity and Trust Backbone for the BLUX Ecosystem**  
> Local-first cryptographic verification for projects, plugins, and users.

[![License](https://img.shields.io/badge/License-Dual-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Cryptography](https://img.shields.io/badge/Crypto-Ed25519%20%7C%20Argon2-green.svg)](#cryptographic-foundation)

---

## 🎯 Overview

BLUX-Reg is the cryptographic trust layer that unifies project validation, plugin signing, and user verification across the BLUX ecosystem. Built on modern cryptography and append-only ledgers, it enables secure, local-first identity management without requiring centralized infrastructure.

**Core Capabilities:**
- 🔐 **Cryptographic Identity** - Ed25519 keypairs protected by Argon2 passphrases
- 📓 **Tamper-Evident Ledgers** - Append-only JSONL audit trails with hash chains
- 🛡️ **Offline Verification** - Air-gapped artifact validation with embedded proofs
- 🎟️ **Capability Tokens** - Offline-verifiable, time-bound delegation tokens
- ♻️ **Revocable Trust** - Ecosystem-wide key revocation with audit trails
- 🤝 **Ecosystem Integration** - Native compatibility with BLUX-Quantum and BLUX-Guard

---

## ✨ Highlights

### 🛡️ Role-Specific Keys
Generate dedicated keypairs for different trust contexts:
- **Project Keys** - For official project releases and distributions
- **Plugin Keys** - For extension and module signing
- **User Keys** - For personal identity and contribution verification

All keys use Ed25519 signatures with Argon2-protected passphrases for defense against brute-force attacks.

### 📓 Append-Only Audit Ledgers
Every trust operation is recorded in immutable JSONL ledgers:
- `keys.jsonl` - Key issuance and registration events
- `artifacts.jsonl` - Signed artifacts with compatibility metadata
- `revocations.jsonl` - Key revocation log with audit trail

Each record is hashed into a tamper-evident chain, enabling cryptographic verification of the entire trust history.

### 🔐 Offline Trust Model
Signatures are self-contained and include:
- Cryptographic signature
- Public key for verification
- Ledger membership proof
- Compatibility metadata

This enables artifact validation without network access or centralized registries.

### 🎟️ Capability Tokens
Issue scoped, time-bound tokens to delegate actions without sharing secrets:
- Signed with Ed25519 and verified offline
- Bound to a capability name, audience repo, and constraints
- Referenced by `capability_token_ref` hash inside envelopes

### ♻️ Revocable Identities
Compromised or expired keys can be revoked with:
- Timestamped revocation records
- Reason and authority documentation
- Ecosystem-wide propagation through ledger synchronization

### 🤝 BLUX Ecosystem Integration
Built-in compatibility metadata ensures seamless integration with:
- **BLUX-Quantum** - Quantum-resistant cryptographic operations
- **BLUX-Guard** - Security monitoring and threat detection
- **BLUX Core** - Project orchestration and workflow automation

---

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/Outer-Void/blux-reg.git
cd blux-reg

# Install dependencies
pip install -r requirements.txt

# For development
pip install -r requirements-dev.txt
```

### Quick Start

```bash
# Initialize directories and ledgers
bin/blux-reg init

# Create a project key (prompts for a new passphrase)
bin/blux-reg keys create my-project project

# List all registered keys
bin/blux-reg keys list

# Export a public key for distribution
bin/blux-reg keys export my-project --key-type project
```

### Signing Artifacts

```bash
# Sign a release artifact
bin/blux-reg sign path/to/artifact.zip my-project project "release"

# Sign with additional metadata
bin/blux-reg sign plugin.tar.gz plugin-dev plugin "v1.2.3" \
  --metadata '{"compatible_versions": ["1.0", "2.0"]}'
```

### Verifying Artifacts

```bash
# Verify an artifact manifest offline
bin/blux-reg verify-manifest path/to/artifact.blux-manifest.json
```

### Capability Tokens

```bash
# Issue a token for a repository capability
bin/blux-reg issue my-project publish Outer-Void/blux-guard 3600 \
  --constraints '{"scope":"release"}'

# Hash a token (deterministic reference)
bin/blux-reg hash /path/to/token.json

# Verify a token offline
bin/blux-reg verify /path/to/token.json

# Revoke a token by hash
bin/blux-reg revoke <token_hash> --revoker security-team
```

### Key Management

```bash
# Revoke a compromised key
bin/blux-reg keys revoke my-project \
  --reason "key-compromise" \
  --revoker security-team

# Rotate keys (revoke old, create new)
bin/blux-reg keys rotate my-project project

# Export key for backup (encrypted with passphrase)
bin/blux-reg keys export my-project --include-private --output backup.key
```

### Ledger Operations

```bash
# Inspect ledger integrity
bin/blux-reg audit artifacts

# Verify complete ledger chain
bin/blux-reg audit keys --verify-chain

# Export ledger for replication
bin/blux-reg ledger export --output registry-backup.tar.gz

# Sync ledgers between systems
bin/blux-reg ledger sync --remote user@server:/blux-reg/registry/
```

### Envelope Reference

Artifacts that require delegated capabilities should reference issued tokens by hash:

```json
{
  "capability_token_ref": "<sha256 hash of canonical token JSON>"
}
```

### Token Lifecycle

1. **Issue** a token offline with a capability and audience.
2. **Hash** the token to compute the deterministic reference (`token_hash`).
3. **Verify** the token offline using the embedded public key.
4. **Revoke** the token hash if access must be withdrawn.

---

## 📁 Directory Structure

```
~/blux-reg/
├── registry/                    # Append-only ledgers
│   ├── keys.jsonl              # Key issuance events
│   ├── artifacts.jsonl         # Signed artifacts + metadata
│   └── revocations.jsonl       # Key revocation log
├── signatures/                  # Detached signature bundles
│   └── *.sig.json              # Self-contained signature files
├── keys/                        # Encrypted private keys (optional)
└── config/                      # Configuration files
    └── blux-reg.yaml           # System configuration
```

### Ledger Format

Each ledger uses JSON Lines format for append-only operation:

```json
{"type": "key_issuance", "timestamp": "2025-01-15T10:30:00Z", "key_id": "proj-abc123", "key_type": "project", "public_key": "...", "hash_prev": "..."}
{"type": "artifact_signed", "timestamp": "2025-01-15T11:00:00Z", "artifact_hash": "sha256:...", "key_id": "proj-abc123", "signature": "...", "hash_prev": "..."}
{"type": "key_revoked", "timestamp": "2025-01-15T12:00:00Z", "key_id": "proj-abc123", "reason": "compromised", "revoker": "security", "hash_prev": "..."}
```

---

## 🔐 Cryptographic Foundation

### Key Generation
- **Algorithm:** Ed25519 (Edwards-curve Digital Signature Algorithm)
- **Key Size:** 256-bit private keys, 256-bit public keys
- **Performance:** ~6,000 signatures/sec, ~15,000 verifications/sec

### Passphrase Protection
- **KDF:** Argon2id (memory-hard, GPU-resistant)
- **Parameters:** 
  - Memory: 64 MB
  - Iterations: 3
  - Parallelism: 4 threads
  - Salt: 16-byte random

### Signature Format
```json
{
  "version": "1.0",
  "algorithm": "Ed25519",
  "key_id": "project-id",
  "key_type": "project",
  "public_key": "base64-encoded-public-key",
  "signature": "base64-encoded-signature",
  "artifact_hash": "sha256:...",
  "timestamp": "2025-01-15T10:30:00Z",
  "metadata": {
    "compatible_with": ["blux-quantum", "blux-guard"],
    "version": "1.2.3"
  }
}
```

---

## 🔄 Workflow Examples

### Project Release Workflow

```bash
# 1. Initialize project key (once)
bin/blux-reg keys create myproject project

# 2. Build release artifact
make build  # Creates dist/myproject-1.0.0.tar.gz

# 3. Sign the release
bin/blux-reg sign dist/myproject-1.0.0.tar.gz myproject project "1.0.0"

# 4. Distribute both artifact and signature
# - dist/myproject-1.0.0.tar.gz
# - ~/blux-reg/signatures/myproject-1.0.0.tar.gz.sig.json

# 5. Users verify before installation
bin/blux-reg verify myproject-1.0.0.tar.gz
```

### Plugin Development Workflow

```bash
# Developer creates plugin key
bin/blux-reg keys create my-plugin plugin

# Sign plugin bundle
bin/blux-reg sign my-plugin.zip my-plugin plugin "1.0"

# Export public key for distribution
bin/blux-reg keys export my-plugin --output my-plugin.pub

# Users import plugin developer's public key
bin/blux-reg keys import my-plugin.pub

# Verify plugin before installation
bin/blux-reg verify my-plugin.zip
```

### Multi-Signer Workflow

```bash
# Multiple maintainers can sign releases
bin/blux-reg sign release.tar.gz maintainer-1 project "v2.0"
bin/blux-reg sign release.tar.gz maintainer-2 project "v2.0"

# Verification requires threshold signatures
bin/blux-reg verify release.tar.gz --require-signers 2
```

---

## 🔍 Audit and Compliance

### Ledger Integrity

```bash
# Verify all ledger hash chains
bin/blux-reg audit --all

# Detect tampering attempts
bin/blux-reg audit --check-integrity

# Generate audit report
bin/blux-reg audit --report --output audit-report.json
```

### Trust Chain Verification

```bash
# Trace an artifact's trust chain
bin/blux-reg trace artifact.zip

# Show all keys that signed an artifact
bin/blux-reg show-signers artifact.zip

# List all artifacts signed by a key
bin/blux-reg list-signatures --key-id myproject
```

### Compliance Export

```bash
# Export complete trust history
bin/blux-reg export --format compliance --output trust-archive.zip

# Generate cryptographic proof bundle
bin/blux-reg proof artifact.zip --output artifact-proof.json
```

---

## 🛠️ Advanced Usage

### Custom Metadata

Embed compatibility and versioning data in signatures:

```bash
bin/blux-reg sign plugin.zip my-plugin plugin "1.0" \
  --metadata '{
    "compatible_with": ["blux-guard>=0.5"],
    "requires": ["python>=3.9"],
    "platform": ["linux", "macos"],
    "checksum_algorithm": "sha256"
  }'
```

### Batch Operations

```bash
# Sign multiple artifacts
for file in dist/*.tar.gz; do
  bin/blux-reg sign "$file" myproject project "1.0"
done

# Verify directory of artifacts
bin/blux-reg verify-batch dist/ --recursive
```

### Integration with CI/CD

```yaml
# .github/workflows/release.yml
- name: Sign Release
  run: |
    echo "$SIGNING_KEY" | bin/blux-reg keys import --stdin
    bin/blux-reg sign dist/release.tar.gz ci-bot project "$VERSION"
    
- name: Upload Signature
  uses: actions/upload-artifact@v3
  with:
    name: signatures
    path: ~/blux-reg/signatures/
```

---

## 🔗 Ecosystem Integration

### BLUX-Guard Integration

BLUX-Reg provides cryptographic verification for BLUX-Guard's security policies:

```bash
# Sign security policy
bin/blux-reg sign security-policy.yaml security-team project "1.0"

# BLUX-Guard verifies before applying
blux-guard verify-policy security-policy.yaml
```

### BLUX-Quantum Integration

Post-quantum cryptographic algorithms are supported through metadata:

```bash
bin/blux-reg sign artifact.zip my-key project "1.0" \
  --quantum-resistant \
  --metadata '{"pq_algorithm": "dilithium3"}'
```

---

## 📚 API and Library Usage

### Python API

```python
from blux_reg import Registry, KeyType

# Initialize registry
registry = Registry("~/blux-reg")

# Create and register a key
key = registry.create_key("my-project", KeyType.PROJECT, passphrase="secret")

# Sign an artifact
signature = registry.sign_artifact(
    "artifact.zip",
    key_id="my-project",
    key_type=KeyType.PROJECT,
    metadata={"version": "1.0.0"}
)

# Verify an artifact
is_valid = registry.verify_artifact("artifact.zip", signature)
```

---

## 🐛 Troubleshooting

### Common Issues

**"Key not found" error**
```bash
# List all registered keys
bin/blux-reg keys list

# Check key exists in ledger
grep "key_id" ~/blux-reg/registry/keys.jsonl
```

**Verification fails**
```bash
# Check signature file exists
ls ~/blux-reg/signatures/

# Verify ledger integrity first
bin/blux-reg audit keys

# Check for revocations
bin/blux-reg keys list --show-revoked
```

**Passphrase not working**
```bash
# Reset passphrase (requires old passphrase)
bin/blux-reg keys change-passphrase my-key

# Emergency key recovery (if backed up)
bin/blux-reg keys recover --from-backup backup.key
```

---

## 🗺️ Roadmap

| Phase | Feature | Status |
|-------|---------|--------|
| **v0.1** | Basic Ed25519 signing | ✅ Complete |
| **v0.2** | Append-only ledgers | ✅ Complete |
| **v0.3** | Key revocation | ✅ Complete |
| **v0.4** | Multi-signature support | 🚧 In Progress |
| **v0.5** | Post-quantum algorithms | 📋 Planned |
| **v0.6** | Distributed ledger sync | 📋 Planned |
| **v1.0** | Complete ecosystem integration | 📋 Planned |

---

## 🤝 Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes and add tests
4. Run the test suite: `pytest tests/`
5. Commit with signed commits: `git commit -S -m "Add feature"`
6. Push and create a pull request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Run linters
black blux_reg/
flake8 blux_reg/
mypy blux_reg/

# Build documentation
cd docs && make html
```

---

## 🔐 Security

### Reporting Vulnerabilities

**DO NOT** open public issues for security vulnerabilities.

Instead, email security details to: **theoutervoid@outlook.com**

We will respond within 48 hours and coordinate disclosure.

### Security Best Practices

1. **Never commit private keys** to version control
2. **Use strong passphrases** (minimum 20 characters)
3. **Backup keys securely** with encrypted storage
4. **Rotate keys regularly** (every 6-12 months)
5. **Verify all artifacts** before execution
6. **Monitor ledgers** for unauthorized entries

---

## ⚖️ Licensing

BLUX-Reg is dual-licensed:

- **Open-source use:** [Apache License 2.0](LICENSE-APACHE)
- **Commercial use:** Requires separate agreement (see [LICENSE-COMMERCIAL](LICENSE-COMMERCIAL))

### Apache 2.0 Usage

You may use, modify, and redistribute the software for open and internal purposes, provided that you preserve notices, include the license, and accept the disclaimers of warranty and liability.

### Commercial Usage

Commercial use—such as embedding in paid products, offering hosted services, or other monetized deployments—requires a commercial license. Please review [COMMERCIAL.md](COMMERCIAL.md) for details and contact **theoutervoid@outlook.com** to arrange terms.

---

## 📖 Documentation

- **[API Reference](docs/api/)** - Complete Python API documentation
- **[Security Model](docs/security.md)** - Cryptographic design and threat model
- **[Ledger Specification](docs/ledger-spec.md)** - JSONL format and hash chain structure
- **[Integration Guide](docs/integration.md)** - Integrating with BLUX ecosystem
- **[Migration Guide](docs/migration.md)** - Upgrading from previous versions

---

## 💬 Support

- **Issues:** [GitHub Issues](https://github.com/Outer-Void/blux-reg/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Outer-Void/blux-reg/discussions)
- **Email:** outervoid.blux@gmail.com

---

## 🙏 Acknowledgments

BLUX-Reg is built on:
- **PyNaCl** - Python bindings for libsodium
- **Argon2** - Password hashing library
- **jsonlines** - JSON Lines format support

---

## 📄 License

Dual-licensed under Apache-2.0 OR Commercial License.  
See [LICENSE](LICENSE), [LICENSE-APACHE](LICENSE-APACHE), and [LICENSE-COMMERCIAL](LICENSE-COMMERCIAL) for details.

---

**BLUX-Reg** — *Trust, verified. Locally.*
