# BLUX-Reg Role Definition

## What BLUX-Reg Does
- Issues and verifies cryptographic capability tokens and token references.
- Maintains append-only provenance and revocation records.
- Performs local-first verification so tokens can be validated offline.
- Produces token artifacts and verification reports only.

## What BLUX-Reg Does **Not** Do
- It does **not** execute workloads or dispatch actions.
- It does **not** perform policy, discernment, enforcement, orchestration, or execution logic.
- It does **not** enforce policy or issue authorization receipts.
- It does **not** route requests or make judgments.
- It does **not** copy canonical BLUX contracts.

## Contract Referencing
BLUX-Reg references canonical BLUX-ecosystem contracts by `blux://` identifier only. Contract definitions are **never** copied into this repository.

## Boundary Enforcement
Boundary checks scan code directories for prohibited execution, routing, or governance keywords and for copied contract identifiers. The checks are intentionally narrow and focus on code paths only.
