# blux-reg

**Portable, auditable registry + signing/audit chain for BLUX projects**

blux-reg is a local-first registry that lets you:

- Generate cryptographic keys (ed25519 / RSA)
- Sign manifests and patch-diffs
- Maintain an append-only audit chain (`audit.log`)
- Wire into any BLUX project (BLG or standalone)

## Features

- CLI-based (`bin/blux-reg`)
- Audit chaining (`prev_audit_sha256` verification)
- Manifest-based system: all patches, events, and installed components are logged
- Easily integrated into BLUX Lite GOLD via hooks
- Portable across any BLUX project

## Installation

```bash
# Clone or move your code
git clone <repo-url> ~/code/blux-reg
cd ~/code/blux-reg

# Initialize keys (default: ~/.config/blux-reg/keys)
bin/blux-reg keygen

# Add your first manifest
bin/blux-reg add-manifest manifests/first.yaml
```

## Hooks (BLG Integration)

Patch-diff signing: call after each patch-diff

Event logging: call on first_start, auto-start, TUI/legacy events

See scripts/hooks/after_patch_apply.sh and scripts/hooks/log_event.sh for examples.

## License

MIT


---
