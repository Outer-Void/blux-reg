# BLUX-Reg Role Definition

## What BLUX-Reg Does
- Issues and verifies cryptographic signatures for artifacts, manifests, and capability tokens.
- Maintains append-only ledgers for provenance, verification, and revocation records.
- Performs local-first validation so artifacts can be verified offline without centralized services.
- Tracks capability token references by deterministic hashes for delegation without sharing secrets.

## What BLUX-Reg Does **Not** Do
- It does **not** make value judgments or governance decisions.
- It does **not** perform human-like judgment or scoring.
- It does **not** execute or deploy artifacts; it only signs and verifies.
- It does **not** host, distribute, or mutate BLUX-ecosystem contracts.

## Contract Referencing
BLUX-Reg references BLUX-ecosystem contracts by `$id` only. Contract definitions are **never** copied into this repository. When validation is needed, BLUX-Reg uses the `$id` to locate the authoritative contract in the upstream BLUX-ecosystem.

## Boundary Enforcement
A boundary CI test scans tracked files for prohibited keywords and paths that would imply governance or scoring logic. The check is regex-based, documented in the test itself, and intentionally narrow to avoid false positives while still blocking prohibited functionality.
