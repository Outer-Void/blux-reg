# BLUX Reg Contract

This document specifies the public contract for the unified BLUX registry demo. Paths, schemas, and the append-only audit rules are stable and versioned at `schema_version: 1.0`.

## Default paths
- Config root: `~/.config/blux-reg/` (override with `BLUX_REG_CONFIG_DIR`)
- Keys: `~/.config/blux-reg/keys/`
- Manifests: `~/.config/blux-reg/manifests/`
- Ledger: `~/.config/blux-reg/trust/ledger.jsonl`
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
`keygen`, `key-import`, `sign`, `event`, plus future actions that follow the schema above.

## CLI contract
- `blux-reg init` — create config dirs
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

Exit codes are stable: `0` success, `1` on verification/chain failures.
