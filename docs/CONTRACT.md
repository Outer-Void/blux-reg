# BLUX-Reg Contract

This document specifies the public contract for the BLUX-Reg trust kernel. Token schema, trust-store format, and append-only audit rules are stable at `schema_version: 1.0`.

## Default paths
- Config root: `~/.config/blux-reg/` (override with `BLUX_REG_CONFIG_DIR`)
- Keys: `~/.config/blux-reg/keys/`
- Manifests: `~/.config/blux-reg/manifests/`
- Ledger: `~/.config/blux-reg/trust/ledger.jsonl`
- Trust store: `~/.config/blux-reg/trust/trust_store.jsonl`
- Token revocations: `~/.config/blux-reg/trust/token_revocations.jsonl`
- Cache/temp: `~/.config/blux-reg/cache/` (safe to clear, never used for trust state)

## Key material
- Default algorithm: Ed25519 (deterministic signatures)
- Stored as PEM: `<name>.pem` (private, 0600) + `<name>.pub.pem` (public)
- Fingerprint: `sha256(raw_public_key)` hex
- Import/export permitted via PEM. No password prompts in default flows.

## Manifest schema (`schema_version: 1.0`)
```json
{
  "schema_version": "1.0",
  "artifact_path": "example.txt",
  "artifact_sha256": "<sha256 hex of artifact bytes>",
  "created_at": "2025-01-01T00:00:00+00:00",
  "key_fingerprint": "<sha256 raw public key>",
  "signature": "<base64 ed25519 signature over canonical manifest without signature>"
}
```
- Canonicalization: JSON serialized with sorted keys and `",":"` separators.
- Signature input: canonical JSON of all manifest fields **excluding** `signature`.
- Manifest hash (for the ledger): SHA-256 of canonical JSON including the signature.

## Capability token schema (`schema_version: 1.0`)
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
    "public_key": "<pem ed25519 public key>"
  },
  "signature": "<base64 ed25519 signature over canonical token payload>"
}
```
- Canonicalization: JSON serialized with sorted keys and `",":"` separators.
- Signature input: canonical JSON of all token fields **excluding** `signature`.
- Token hash (`capability_token_ref`): SHA-256 of canonical JSON including the signature.
- Tokens are offline-verifiable, scoped, and time-bound. Secrets must not be embedded in tokens.

## Trust store schema (JSONL, append-only)
Each line is canonical JSON with sorted keys. Entries are chained with `prev_hash` and `entry_hash`.

### Trust anchor entry
```json
{
  "schema_version": "1.0",
  "entry_type": "trust_anchor",
  "added_at": "2025-01-01T00:00:00+00:00",
  "fingerprint": "<sha256 raw public key>",
  "public_key": "<pem ed25519 public key>",
  "source": "local",
  "prev_hash": null,
  "entry_hash": "<sha256 hash of entry without entry_hash>"
}
```

### Token revocation entry
```json
{
  "schema_version": "1.0",
  "entry_type": "token_revocation",
  "revoked_at": "2025-01-01T00:00:00+00:00",
  "token_hash": "<sha256 canonical token JSON>",
  "reason": "compromised",
  "prev_hash": "<previous entry hash>",
  "entry_hash": "<sha256 hash of entry without entry_hash>"
}
```

## Ledger schema (JSONL, append-only)
Each line is canonical JSON with sorted keys.

Required fields:
- `ts` (ISO-8601 UTC)
- `action` (e.g., `keygen`, `sign`, `event`)
- `actor` (key fingerprint or actor id)
- `payload_summary` (short description)
- `artifact_hash` (optional)
- `manifest_hash` (optional)
- `prev_hash` (SHA-256 of previous **entry** JSON; `null` for first entry)
- `entry_hash` (SHA-256 of canonical JSON for this entry **without** `entry_hash`)

### Hash-chain rule
`prev_hash` of entry `n` **must equal** `entry_hash` of entry `n-1`. Any deviation invalidates the chain.

### Allowed actions
`keygen`, `key-import`, `sign`, `event`, `token-issue`, `token-revoke`, plus future actions that follow the schema above.

## CLI contract
- `blux-reg init` — create config dirs
- `blux-reg issue <key_name> <capability> <audience> <ttl_seconds> [--constraints JSON]`
- `blux-reg hash <token_path>`
- `blux-reg verify <token_path>`
- `blux-reg revoke <token_hash> [--reason REASON] [--revoker ID]`

Exit codes are stable: `0` success, `1` on verification/chain failures.
