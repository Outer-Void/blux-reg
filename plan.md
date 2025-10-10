
---

## **blux-reg/plan.md** (BLG integration plan)


# blux-reg / BLG Integration Plan

## v0.1 — Baseline
- [x] CLI: `keygen`, `add-manifest`, `verify-line`
- [x] Audit chain (SHA256 prev pointers)
- [x] Local storage: `~/.config/blux-reg/keys`, `manifests/`, `audit.log`

## v0.1.1
- [ ] Sign arbitrary payloads
- [ ] ed25519 key option
- [ ] CLI improvements, verbose / debug

## v0.2
- [ ] Install flow: `~/.local/blux/components`
- [ ] Capability tags / metadata
- [ ] Auto-versioning of manifests

## v0.3
- [ ] HTTP serve mode for remote verification
- [ ] How-to doc for remote verify

## v0.4 — BLG hooks
- [ ] Patch-diff hook integration
- [ ] Launcher event logging hooks
- [ ] Optional auto-sign for components

## v1.0 — Governance-ready
- [ ] Full manifest spec (YAML schema)
- [ ] Key rotation + ed25519 rotation
- [ ] Test suite, CI/CD, hardening
- [ ] Publish interoperability spec
