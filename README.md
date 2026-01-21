# BLUX-Reg

> **Trust Kernel for Capability Tokens**  
> Local-first cryptographic issuance, verification, provenance, and revocation.

[![License](https://img.shields.io/badge/License-Dual-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Cryptography](https://img.shields.io/badge/Crypto-Ed25519-green.svg)](#cryptographic-foundation)

---

## 🎯 Overview

BLUX-Reg is the **engine-free trust kernel** for the BLUX ecosystem. It issues and verifies capability tokens, maintains append-only provenance records, and manages revocations for offline verification. It does **not** execute work, enforce policy, route requests, or judge outcomes.

**Scope guarantees:**
- ✅ Issues/verifies capability tokens and verification reports.
- ✅ Maintains append-only provenance and revocation data.
- ❌ Does not execute, enforce, route, or judge.
- ❌ Does not emit guard receipts or authorization decisions.
- ❌ Does not copy canonical contracts (references `blux://` IDs only).

**Outputs are limited to:** token artifacts and verification reports (no receipts).

---

## ✨ Core Capabilities

- 🎟️ **Capability Tokens** - Deterministic, offline-verifiable tokens with constraints.
- 📓 **Append-Only Provenance** - Hash-chained JSONL ledgers for audits.
- ♻️ **Revocation** - Token revocations recorded as append-only events.
- 🧭 **Offline Verification** - No network dependency for validation.

---

## 🔐 Token Format (Deterministic)

Tokens are canonical JSON (sorted keys, no extra whitespace). The signed payload excludes the `signature` field.

```json
{
  "schema_version": "1.0",
  "token_type": "capability",
  "issued_at": "2025-01-01T00:00:00+00:00",
  "expires_at": "2025-01-02T00:00:00+00:00",
  "ttl_seconds": 86400,
  "capability": "publish",
  "audience": "outer-void/blux-example",
  "constraints": {
    "scope": "release"
  },
  "issuer": {
    "key_name": "issuer",
    "fingerprint": "<sha256 raw public key>",
    "public_key": "<pem public key>"
  },
  "signature": "<base64 ed25519 signature>"
}
```

Token reference (`token_hash`) = SHA-256 of canonical JSON including the signature.

---

## 🧾 Trust Store (Append-Only)

The trust store is a local JSONL file with a hash chain. It contains:
- **Trust anchors**: issuer public keys + fingerprints.
- **Token revocations**: `token_hash` + reason.

This store is append-only, local-first, and auditable. It contains no user identity data by default.

---

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### CLI (Token CRUD + Verification Reports)

```bash
# Issue a token
bin/blux-reg issue issuer publish outer-void/blux-example 3600 \
  --constraints '{"scope":"release"}'

# Hash a token
bin/blux-reg hash /path/to/token.json

# Verify a token
bin/blux-reg verify /path/to/token.json

# Revoke a token
bin/blux-reg revoke <token_hash> --reason "compromised"
```

### Python API

```python
from pathlib import Path
from blux_reg import issue_token, verify_token, load_trust_store, save_trust_store
from blux_reg import crypto
from blux_reg.trust_store import new_trust_anchor

crypto.generate_keypair("issuer")
store_path = Path("./trust_store.jsonl")
store = load_trust_store(store_path)

public_key = crypto.load_public_key("issuer")
public_pem = crypto.export_key("issuer", public=True).decode("utf-8")
store.add_entry(new_trust_anchor(crypto.fingerprint_public_key(public_key), public_pem))
save_trust_store(store_path, store)

artifact = issue_token(
    {"capability": "publish", "audience": "outer-void/blux-example"},
    issuer_key="issuer",
    ttl=3600,
)
report = verify_token(artifact["token"], store_path)
print(report)
```

---

## 📁 Directory Structure

```
~/.config/blux-reg/
├── trust/
│   ├── ledger.jsonl             # Append-only provenance ledger
│   ├── tokens/                  # Issued token artifacts
│   ├── token_revocations.jsonl  # Legacy token revocations (append-only)
│   └── trust_store.jsonl        # Trust anchors + revocations (append-only)
├── keys/                        # Local issuer keys
└── manifests/                   # Artifact manifests (optional provenance)
```

---

## 🔐 Cryptographic Foundation

### Key Generation
- **Algorithm:** Ed25519 (deterministic signatures)
- **Fingerprints:** SHA-256 of raw public key bytes

---

## 📜 Contract Referencing

Canonical BLUX contracts live in the `blux-ecosystem` repository. BLUX-Reg only references them by `blux://` IDs in documentation or tests and never copies contract definitions into this repository.
