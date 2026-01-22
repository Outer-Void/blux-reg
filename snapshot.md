# Repository Snapshot

## 1) Metadata
- Repository name: blux-reg
- Organization / owner: unknown
- Default branch: work
- HEAD commit hash: 35242c9329bfba8cc52a647daafe7e29f1443770
- Snapshot timestamp (UTC): 2026-01-22T05:17:37Z
- Total file count (excluding directories): 35
- Description: Trust kernel for capability tokens with local-first cryptographic issuance, verification, provenance, and revocation.

## 2) Repository Tree
.github/
  workflows/
    ci.yml [text]
.gitignore [text]
COMMERCIAL.md [text]
LICENSE [text]
LICENSE-APACHE [text]
LICENSE-COMMERCIAL [text]
NOTICE [text]
README.md [text]
ROLE.md [text]
bin/
  blux-reg [text]
docs/
  CONTRACT.md [text]
  roles.md [text]
plan.md [text]
pyproject.toml [text]
requirements-dev.txt [text]
requirements.txt [text]
scripts/
  demo_unified_reg.sh [text]
  physics_check.sh [text]
src/
  blux_reg/
    __init__.py [text]
    api.py [text]
    cli.py [text]
    config.py [text]
    crypto.py [text]
    ledger.py [text]
    manifest.py [text]
    tokens.py [text]
    trust_store.py [text]
    util.py [text]
tests/
  conftest.py [text]
  test_boundary_ci.py [text]
  test_crypto.py [text]
  test_flow.py [text]
  test_ledger.py [text]
  test_tokens.py [text]
  test_trust_store.py [text]

## 3) FULL FILE CONTENTS (MANDATORY)

FILE: .github/workflows/ci.yml
Kind: text
Size: 593
Last modified: 2026-01-21T18:09:23Z

CONTENT:
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt
      - name: Run physics check
        run: |
          scripts/physics_check.sh
      - name: Run tests
        env:
          BLUX_CONFIG_HOME: ${{ runner.temp }}/blux-config
        run: |
          pytest -q

FILE: .gitignore
Kind: text
Size: 37
Last modified: 2026-01-21T18:09:23Z

CONTENT:
__pycache__/
*.pyc
*.pyo
*.egg-info/

FILE: COMMERCIAL.md
Kind: text
Size: 669
Last modified: 2026-01-21T18:09:23Z

CONTENT:
# Commercial Licensing

blux-reg is dual-licensed. You may use it under the open-source Apache License 2.0 for
community and non-commercial purposes. Commercial uses require a separate commercial
license from the project maintainer.

## When you need a commercial license
- Embedding blux-reg into a paid or closed-source product
- Offering blux-reg as part of a paid service or platform
- Large-scale internal deployments where terms beyond Apache-2.0 are required
- Any redistribution of modified or unmodified versions for commercial advantage

## How to obtain a commercial license
Email theoutervoid@outlook.com to discuss terms and obtain a commercial agreement.

FILE: LICENSE
Kind: text
Size: 334
Last modified: 2026-01-21T18:09:23Z

CONTENT:
This project is dual-licensed.

- Open-source use is governed by the Apache License, Version 2.0. See LICENSE-APACHE for full terms.
- Commercial use requires a separate commercial agreement. See LICENSE-COMMERCIAL for details.

Unless otherwise noted, source files include a copyright notice reflecting the project copyright holder.

FILE: LICENSE-APACHE
Kind: text
Size: 11342
Last modified: 2026-01-21T18:09:23Z

CONTENT:
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2025 - Outer-Void

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

FILE: LICENSE-COMMERCIAL
Kind: text
Size: 1721
Last modified: 2026-01-21T18:09:23Z

CONTENT:
Proprietary Commercial License

Copyright (c) 2025 - Outer-Void. All rights reserved.

1. Grant of License. Subject to a separate written commercial agreement with the Licensor,
   you are granted a limited, non-exclusive, non-transferable license to use the Software
   for commercial purposes. No rights are granted for redistribution, sublicensing,
   public offering, or making derivative commercial products except as expressly
   permitted in such agreement.

2. Restrictions. Without a commercial agreement, you may not: (a) use the Software to
   provide paid services; (b) integrate or embed the Software into commercial products;
   (c) redistribute the Software or derivative works for commercial advantage; or
   (d) sublicense, rent, lease, or otherwise transfer rights in the Software.

3. Ownership. The Software is licensed, not sold. The Licensor retains all right, title,
   and interest in and to the Software, including all intellectual property rights.

4. Termination. Any breach of this license automatically terminates your rights. Upon
   termination, you must cease all use and destroy all copies of the Software.

5. Disclaimer of Warranty. THE SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
   WHETHER EXPRESS, IMPLIED, OR STATUTORY, INCLUDING WITHOUT LIMITATION WARRANTIES OF
   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.

6. Limitation of Liability. TO THE MAXIMUM EXTENT PERMITTED BY LAW, IN NO EVENT SHALL THE
   LICENSOR BE LIABLE FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES
   ARISING OUT OF OR RELATED TO THIS LICENSE OR THE USE OF THE SOFTWARE.

7. Contact. To obtain a commercial license, contact: theoutervoid@outlook.com

FILE: NOTICE
Kind: text
Size: 188
Last modified: 2026-01-21T18:09:23Z

CONTENT:
blux-reg
Copyright (c) 2025 - Outer-Void

This product includes software developed by the blux-reg project.
Licensed under the Apache License, Version 2.0. See LICENSE-APACHE for details.

FILE: README.md
Kind: text
Size: 4817
Last modified: 2026-01-22T05:16:02Z

CONTENT:
# BLUX-Reg

> **Trust Kernel for Capability Tokens**  
> Local-first cryptographic issuance, verification, provenance, and revocation.

[![License](https://img.shields.io/badge/License-Dual-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Cryptography](https://img.shields.io/badge/Crypto-Ed25519-green.svg)](#cryptographic-foundation)

---

## 🎯 Overview

BLUX-Reg is the **engine-free trust kernel** for the BLUX ecosystem. It issues and verifies capability tokens and capability token references, maintains append-only provenance records, and manages revocations for offline verification. It does **not** execute work, enforce policy, route requests, or judge outcomes.

**Scope guarantees:**
- ✅ Issues/verifies capability tokens, token references, and verification reports.
- ✅ Maintains append-only provenance and revocation data.
- ❌ Does not execute, enforce, route, or judge.
- ❌ Does not perform policy, discernment, enforcement, orchestration, or execution.
- ❌ Does not emit guard receipts or authorization decisions.
- ❌ Does not copy canonical contracts (references `blux://` IDs only from the blux-ecosystem).

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

FILE: ROLE.md
Kind: text
Size: 147
Last modified: 2026-01-21T18:09:23Z

CONTENT:
# ROLE

BLUX-Reg is a trust kernel for capability tokens, provenance, and revocation only.

No execution, no routing, no enforcement, no judgment.

FILE: bin/blux-reg
Kind: text
Size: 365
Last modified: 2026-01-21T18:09:23Z

CONTENT:
#!/usr/bin/env python3
"""BLUX-Reg ecosystem identity and trust CLI."""

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
SRC_ROOT = os.path.join(REPO_ROOT, "src")
if SRC_ROOT not in sys.path:
    sys.path.insert(0, SRC_ROOT)

from blux_reg.cli import app

if __name__ == "__main__":
    raise SystemExit(app())

FILE: docs/CONTRACT.md
Kind: text
Size: 4299
Last modified: 2026-01-21T18:09:23Z

CONTENT:
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

FILE: docs/roles.md
Kind: text
Size: 1066
Last modified: 2026-01-22T05:16:02Z

CONTENT:
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

FILE: plan.md
Kind: text
Size: 964
Last modified: 2026-01-21T18:09:23Z

CONTENT:
---

## **blux-reg/plan.md** (Governance backbone milestones)

# BLUX-Reg Roadmap

## v1.0 — Identity Backbone
- [x] Ed25519 key management with Argon2 passphrase protection
- [x] JSONL append-only ledgers for keys, artifacts, and revocations
- [x] Offline verification workflow with detached signatures
- [x] Revocation pipeline compatible with BLUX-Quantum and BLUX-Guard

## v1.1 — Ecosystem Integrations
- [ ] Federation sync tooling for replicating ledgers
- [ ] Trust authoring kit (contract-driven)
- [ ] Quantum attestation bridges

## v1.2 — Developer Experience
- [ ] Python API for programmatic signing and verification
- [ ] Rich TUI for identity lifecycle operations
- [ ] Automated rotation schedules and timed attestations

## v2.0 — Multi-tenant Governance
- [ ] Distributed quorum approvals for high-risk actions
- [ ] Ledger anchoring to external transparency logs
- [ ] Automated guard-rail enforcement via BLUX-Guard verification hooks

FILE: pyproject.toml
Kind: text
Size: 577
Last modified: 2026-01-21T18:09:23Z

CONTENT:
[project]
name = "blux-reg"
version = "0.2.0"
description = "Local-first registry signer + audit chain for BLUX demos"
authors = [{name = "BLUX"}]
readme = "README.md"
license = {file = "LICENSE"}
requires-python = ">=3.9"
dependencies = [
  "click>=8",
  "cryptography>=42",
]

[project.scripts]
blux-reg = "blux_reg.cli:app"

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.package-dir]
"" = "src"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"

FILE: requirements-dev.txt
Kind: text
Size: 27
Last modified: 2026-01-21T18:09:23Z

CONTENT:
-r requirements.txt
pytest

FILE: requirements.txt
Kind: text
Size: 55
Last modified: 2026-01-21T18:09:23Z

CONTENT:
cryptography>=42.0.0
argon2-cffi>=23.1.0
pynacl>=1.5.0

FILE: scripts/demo_unified_reg.sh
Kind: text
Size: 593
Last modified: 2026-01-21T18:09:23Z

CONTENT:
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

CONFIG_DIR=${BLUX_REG_CONFIG_DIR:-"$HOME/.config/blux-reg"}
export BLUX_REG_CONFIG_DIR="$CONFIG_DIR"

command -v blux-reg >/dev/null 2>&1 || {
  echo "blux-reg entrypoint not installed; try 'pip install -e .' first" >&2
  exit 1
}

blux-reg init

python - <<'PY'
from blux_reg import config, crypto

config.refresh_paths()
crypto.generate_keypair("demo", force=True)
PY

token_out="$CONFIG_DIR/token.json"

blux-reg issue demo publish outer-void/blux-example 3600 --output "$token_out"
blux-reg hash "$token_out"
blux-reg verify "$token_out"

FILE: scripts/physics_check.sh
Kind: text
Size: 1845
Last modified: 2026-01-22T05:16:02Z

CONTENT:
#!/usr/bin/env bash
set -euo pipefail

code_globs=(
  --glob "src/**"
  --glob "tests/**"
  --glob "scripts/**"
  --glob "bin/**"
  --glob "!scripts/physics_check.sh"
  --glob "!tests/test_boundary_ci.py"
  --glob "!**/__pycache__/**"
)

execution_pattern='\bsubprocess\b|os\.system|\bexec\(|\bshell\b|\bchild_process\b'
repo_pattern='\bblux_ca\b|\bblux_guard\b|\bblux_lite\b|\bblux_quantum\b|\bblux_doctrine\b'
intent_pattern='\bposture\b|\bethic|\benforce\b|\ballow\b[[:space:][:punct:]]+\bintent\b|\bdeny\b[[:space:][:punct:]]+\bintent\b|doctrine[[:space:][:punct:]]+engine'
role_pattern='guard_receipt|discernment_report|\bexecute\b|\brouter\b|\borchestr|\bpolicy\b|\bquantum\b|\bdoctrine\b|\blite\b'

if rg -n -i --hidden "${code_globs[@]}" "$execution_pattern" .; then
  echo "Physics check failed: execution primitives detected in code."
  exit 1
fi

if rg -n -i --hidden "${code_globs[@]}" "$repo_pattern" .; then
  echo "Physics check failed: sibling repo references detected."
  exit 1
fi

if rg -n -i --hidden "${code_globs[@]}" "$intent_pattern" .; then
  echo "Physics check failed: policy or intent reasoning keywords detected in code."
  exit 1
fi

if rg -n -i --hidden "${code_globs[@]}" "$role_pattern" .; then
  echo "Physics check failed: prohibited role keywords detected in code."
  exit 1
fi

if [[ -d "contracts" ]]; then
  echo "Physics check failed: contracts directory detected."
  exit 1
fi

if rg -n --hidden "\\$id\s*:\s*\"blux://contracts/" .; then
  echo "Physics check failed: canonical contract identifiers detected."
  exit 1
fi

schema_files=$(find . -type f -name "*.schema.json" ! -path "./tests/fixtures/*" ! -path "./.git/*")
if [[ -n "${schema_files}" ]]; then
  echo "Physics check failed: schema files detected outside tests/fixtures."
  echo "${schema_files}"
  exit 1
fi

echo "Physics check passed."

FILE: src/blux_reg/__init__.py
Kind: text
Size: 312
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""blux-reg package."""

from .api import issue_token, load_trust_store, revoke_token, save_trust_store, verify_token

__all__ = [
    "config",
    "crypto",
    "issue_token",
    "ledger",
    "load_trust_store",
    "manifest",
    "revoke_token",
    "save_trust_store",
    "tokens",
    "verify_token",
]

FILE: src/blux_reg/api.py
Kind: text
Size: 3564
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Public API surface for BLUX-Reg trust kernel."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from . import tokens
from .trust_store import (
    TrustStore,
    load_trust_store as _load_trust_store,
    new_token_revocation,
    save_trust_store as _save_trust_store,
    trust_store_index,
)


def issue_token(
    claims: Dict[str, Any],
    issuer_key: str,
    ttl: int,
    constraints: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Issue a capability token from structured claims.

    Required claim fields: ``capability`` and ``audience``.
    """
    if not isinstance(claims, dict):
        raise ValueError("claims must be a dict")
    capability = claims.get("capability")
    audience = claims.get("audience")
    if not capability or not audience:
        raise ValueError("claims must include capability and audience")
    token, token_hash, path = tokens.issue_capability_token(
        key_name=issuer_key,
        capability=capability,
        audience=audience,
        ttl_seconds=ttl,
        constraints=constraints or claims.get("constraints") or {},
    )
    return {"token": token, "token_hash": token_hash, "path": str(path)}


def verify_token(
    token: Dict[str, Any],
    trust_store: TrustStore | Path | str,
    now: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Verify a capability token against a trust store."""
    store = _resolve_store(trust_store)
    index = trust_store_index(store)
    try:
        result = tokens.verify_capability_token(
            token,
            now=now,
            trust_anchors=index["trusted_issuers"] or None,
            revoked_tokens=index["revoked_tokens"] or None,
        )
        return {
            "valid": True,
            "reason_codes": [],
            "token_hash": result.get("token_hash"),
            "capability": result.get("capability"),
            "audience": result.get("audience"),
            "expires_at": result.get("expires_at"),
        }
    except ValueError as exc:
        return {
            "valid": False,
            "reason_codes": [_reason_code(str(exc))],
        }


def revoke_token(token_id: str, reason: str, store: TrustStore | Path | str) -> Dict[str, Any]:
    """Revoke a token by hash in the trust store."""
    trust_store = _resolve_store(store)
    entry = trust_store.add_entry(new_token_revocation(token_id, reason))
    save_trust_store(trust_store.path, trust_store)
    return entry


def load_trust_store(path: Path | str) -> TrustStore:
    return _load_trust_store(Path(path))


def save_trust_store(path: Path | str, store: TrustStore) -> None:
    _save_trust_store(Path(path), store)


def _resolve_store(store: TrustStore | Path | str) -> TrustStore:
    if isinstance(store, TrustStore):
        return store
    return _load_trust_store(Path(store))


def _reason_code(message: str) -> str:
    lowered = message.lower()
    if "missing fields" in lowered:
        return "missing_fields"
    if "token type" in lowered:
        return "token_type_mismatch"
    if "unsupported token schema" in lowered:
        return "unsupported_schema"
    if "missing issuer public key" in lowered:
        return "missing_issuer_key"
    if "signature verification" in lowered:
        return "invalid_signature"
    if "expired" in lowered:
        return "expired"
    if "revoked" in lowered:
        return "revoked"
    if "issuer not trusted" in lowered:
        return "untrusted_issuer"
    return "invalid"

FILE: src/blux_reg/cli.py
Kind: text
Size: 2708
Last modified: 2026-01-21T18:09:23Z

CONTENT:
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import click

from . import config, tokens


@click.group()
def app():
    """blux-reg: local-first trust kernel for capability tokens."""
    config.refresh_paths()


@app.command()
def init():
    """Initialize config directories."""
    config.ensure_directories()
    click.echo(f"config_dir: {config.CONFIG_ROOT}")
    click.echo(f"trust_dir:  {config.TRUST_DIR}")


def _parse_constraints(raw: str) -> dict:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid constraints JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise click.ClickException("Constraints must be a JSON object")
    return data


@app.command()
@click.argument("key_name")
@click.argument("capability")
@click.argument("audience")
@click.argument("ttl_seconds", type=int)
@click.option("--constraints", default="{}", help="JSON constraints object")
@click.option("--output", type=click.Path(), help="Output path for token JSON")
def issue(key_name: str, capability: str, audience: str, ttl_seconds: int, constraints: str, output: Optional[str]):
    """Issue a capability token offline."""
    token, token_hash, path = tokens.issue_capability_token(
        key_name=key_name,
        capability=capability,
        audience=audience,
        ttl_seconds=ttl_seconds,
        constraints=_parse_constraints(constraints),
        output_path=Path(output) if output else None,
    )
    click.echo(
        json.dumps({"token_hash": token_hash, "token_path": str(path), "token": token}, indent=2, sort_keys=True)
    )


@app.command(name="hash")
@click.argument("token_path", type=click.Path(exists=True))
def hash_token(token_path: str):
    """Hash a token (canonical JSON sha256)."""
    token_hash = tokens.hash_token_file(Path(token_path))
    click.echo(token_hash)


@app.command()
@click.argument("token_path", type=click.Path(exists=True))
def verify(token_path: str):
    """Verify a capability token offline."""
    token = tokens.load_token(Path(token_path))
    result = tokens.verify_capability_token(token)
    click.echo(json.dumps(result, indent=2, sort_keys=True))


@app.command()
@click.argument("token_hash")
@click.option("--reason", default="unspecified")
@click.option("--revoker", default="anonymous", help="Identifier for the revocation")
def revoke(token_hash: str, reason: str, revoker: str):
    """Revoke a capability token offline."""
    entry = tokens.revoke_capability_token(token_hash, reason, revoker)
    click.echo(json.dumps(entry, indent=2, sort_keys=True))


if __name__ == "__main__":
    app()

FILE: src/blux_reg/config.py
Kind: text
Size: 1879
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Configuration and path helpers for blux-reg.

Centralizes default paths with environment overrides to keep the CLI portable
across Linux, macOS, and Termux. All paths are derived from the configuration
root so tests can redirect state with the ``BLUX_REG_CONFIG_DIR`` environment
variable.
"""
from __future__ import annotations

import os
from pathlib import Path

SCHEMA_VERSION = "1.0"


def _resolve_root() -> Path:
    env_root = os.environ.get("BLUX_REG_CONFIG_DIR")
    if env_root:
        return Path(env_root).expanduser()
    return Path.home() / ".config" / "blux-reg"


CONFIG_ROOT = _resolve_root()
KEYS_DIR = CONFIG_ROOT / "keys"
MANIFEST_DIR = CONFIG_ROOT / "manifests"
TRUST_DIR = CONFIG_ROOT / "trust"
LEDGER_PATH = TRUST_DIR / "ledger.jsonl"
CACHE_DIR = CONFIG_ROOT / "cache"
TOKENS_DIR = TRUST_DIR / "tokens"
REVOCATIONS_PATH = TRUST_DIR / "token_revocations.jsonl"
TRUST_STORE_PATH = TRUST_DIR / "trust_store.jsonl"


def refresh_paths() -> None:
    """Refresh module-level paths from the current environment.

    Useful for tests that temporarily override ``BLUX_REG_CONFIG_DIR``.
    """
    global CONFIG_ROOT, KEYS_DIR, MANIFEST_DIR, TRUST_DIR, LEDGER_PATH, CACHE_DIR, TOKENS_DIR, REVOCATIONS_PATH
    global TRUST_STORE_PATH
    CONFIG_ROOT = _resolve_root()
    KEYS_DIR = CONFIG_ROOT / "keys"
    MANIFEST_DIR = CONFIG_ROOT / "manifests"
    TRUST_DIR = CONFIG_ROOT / "trust"
    LEDGER_PATH = TRUST_DIR / "ledger.jsonl"
    CACHE_DIR = CONFIG_ROOT / "cache"
    TOKENS_DIR = TRUST_DIR / "tokens"
    REVOCATIONS_PATH = TRUST_DIR / "token_revocations.jsonl"
    TRUST_STORE_PATH = TRUST_DIR / "trust_store.jsonl"


def ensure_directories() -> None:
    """Create required directories if they do not exist."""
    for path in (CONFIG_ROOT, KEYS_DIR, MANIFEST_DIR, TRUST_DIR, CACHE_DIR, TOKENS_DIR):
        path.mkdir(parents=True, exist_ok=True)

FILE: src/blux_reg/crypto.py
Kind: text
Size: 4920
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Key management helpers using Ed25519."""
from __future__ import annotations

import base64
from pathlib import Path
from typing import List, Optional

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

from . import config
from .util import sha256_hex


class KeyInfo:
    def __init__(self, name: str, private_path: Path, public_path: Path, fingerprint: str):
        self.name = name
        self.private_path = private_path
        self.public_path = public_path
        self.fingerprint = fingerprint

    def as_dict(self):
        return {
            "name": self.name,
            "private_path": str(self.private_path),
            "public_path": str(self.public_path),
            "fingerprint": self.fingerprint,
        }


def _key_paths(name: str) -> tuple[Path, Path]:
    priv = config.KEYS_DIR / f"{name}.pem"
    pub = config.KEYS_DIR / f"{name}.pub.pem"
    return priv, pub


def fingerprint_public_key(public_key: ed25519.Ed25519PublicKey) -> str:
    raw = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )
    return sha256_hex(raw)


def generate_keypair(name: str, force: bool = False) -> KeyInfo:
    config.ensure_directories()
    priv_path, pub_path = _key_paths(name)
    if not force and (priv_path.exists() or pub_path.exists()):
        raise FileExistsError(f"Key '{name}' already exists")
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    fingerprint = fingerprint_public_key(public_key)

    priv_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pub_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    priv_path.write_bytes(priv_bytes)
    pub_path.write_bytes(pub_bytes)
    priv_path.chmod(0o600)
    return KeyInfo(name, priv_path, pub_path, fingerprint)


def list_keys() -> List[KeyInfo]:
    infos: List[KeyInfo] = []
    if not config.KEYS_DIR.exists():
        return infos
    for priv_path in sorted(config.KEYS_DIR.glob("*.pem")):
        if priv_path.name.endswith(".pub.pem"):
            continue
        name = priv_path.stem
        pub_path = config.KEYS_DIR / f"{name}.pub.pem"
        if not pub_path.exists():
            continue
        public_key = load_public_key(name)
        fingerprint = fingerprint_public_key(public_key)
        infos.append(KeyInfo(name, priv_path, pub_path, fingerprint))
    return infos


def load_private_key(name: str) -> ed25519.Ed25519PrivateKey:
    priv_path, _ = _key_paths(name)
    data = priv_path.read_bytes()
    return serialization.load_pem_private_key(data, password=None)


def load_public_key(name: str) -> ed25519.Ed25519PublicKey:
    _, pub_path = _key_paths(name)
    data = pub_path.read_bytes()
    return serialization.load_pem_public_key(data)


def find_public_key_by_fingerprint(fingerprint: str) -> Optional[ed25519.Ed25519PublicKey]:
    for info in list_keys():
        if info.fingerprint == fingerprint:
            return load_public_key(info.name)
    return None


def export_key(name: str, public: bool = True) -> bytes:
    if public:
        _, pub = _key_paths(name)
        return pub.read_bytes()
    priv, _ = _key_paths(name)
    return priv.read_bytes()


def import_private_key(path: Path, name: str) -> KeyInfo:
    data = Path(path).read_bytes()
    private_key = serialization.load_pem_private_key(data, password=None)
    if not isinstance(private_key, ed25519.Ed25519PrivateKey):
        raise ValueError("Only Ed25519 private keys are supported")
    public_key = private_key.public_key()
    fingerprint = fingerprint_public_key(public_key)
    priv_path, pub_path = _key_paths(name)
    priv_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pub_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    priv_path.write_bytes(priv_bytes)
    pub_path.write_bytes(pub_bytes)
    priv_path.chmod(0o600)
    return KeyInfo(name, priv_path, pub_path, fingerprint)


def sign_message(name: str, message: bytes) -> str:
    private_key = load_private_key(name)
    signature = private_key.sign(message)
    return base64.b64encode(signature).decode()


def verify_signature(public_key: ed25519.Ed25519PublicKey, message: bytes, signature_b64: str) -> bool:
    try:
        public_key.verify(base64.b64decode(signature_b64), message)
        return True
    except Exception:
        return False

FILE: src/blux_reg/ledger.py
Kind: text
Size: 2316
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Append-only audit ledger utilities."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

from . import config
from .util import canonical_json, sha256_hex


def _iter_entries() -> Iterable[Dict]:
    if not config.LEDGER_PATH.exists():
        return []
    with config.LEDGER_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def _last_entry_hash() -> str | None:
    last_hash = None
    for entry in _iter_entries():
        last_hash = entry.get("entry_hash")
    return last_hash


def _compute_entry_hash(entry: Dict) -> str:
    data = dict(entry)
    data.pop("entry_hash", None)
    return sha256_hex(canonical_json(data).encode())


def append_entry(
    action: str,
    actor: str,
    payload_summary: str,
    artifact_hash: str | None = None,
    manifest_hash: str | None = None,
    extra: Dict | None = None,
) -> Dict:
    config.ensure_directories()
    prev_hash = _last_entry_hash()
    entry = {
        "ts": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "action": action,
        "actor": actor,
        "payload_summary": payload_summary,
        "artifact_hash": artifact_hash,
        "manifest_hash": manifest_hash,
        "prev_hash": prev_hash,
    }
    if extra:
        entry.update(extra)
    entry_hash = _compute_entry_hash(entry)
    entry["entry_hash"] = entry_hash
    with config.LEDGER_PATH.open("a", encoding="utf-8") as f:
        f.write(canonical_json(entry) + "\n")
    return entry


def tail_entries(limit: int = 10) -> List[Dict]:
    entries = list(_iter_entries())
    if limit <= 0:
        return entries
    return entries[-limit:]


def verify_chain() -> bool:
    prev_hash = None
    for entry in _iter_entries():
        expected_prev = entry.get("prev_hash")
        if expected_prev != prev_hash:
            return False
        computed_hash = _compute_entry_hash(entry)
        if computed_hash != entry.get("entry_hash"):
            return False
        prev_hash = entry.get("entry_hash")
    return True


def ledger_size() -> int:
    return len(list(_iter_entries()))


def last_hash() -> str | None:
    return _last_entry_hash()

FILE: src/blux_reg/manifest.py
Kind: text
Size: 3083
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Manifest creation and verification."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Tuple

from . import config, crypto, ledger
from .util import canonical_json, sha256_hex, write_json


REQUIRED_FIELDS = {
    "schema_version",
    "artifact_path",
    "artifact_sha256",
    "created_at",
    "key_fingerprint",
    "signature",
}


def _artifact_hash(path: Path) -> str:
    data = path.read_bytes()
    return sha256_hex(data)


def sign_artifact(artifact_path: Path, key_name: str, output: Path | None = None) -> Tuple[Path, Dict[str, str]]:
    artifact_path = artifact_path.expanduser().resolve()
    if not artifact_path.exists():
        raise FileNotFoundError(f"Artifact not found: {artifact_path}")
    config.ensure_directories()
    artifact_hash = _artifact_hash(artifact_path)
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    manifest = {
        "schema_version": config.SCHEMA_VERSION,
        "artifact_path": artifact_path.name,
        "artifact_sha256": artifact_hash,
        "created_at": created_at,
        "key_fingerprint": crypto.fingerprint_public_key(crypto.load_public_key(key_name)),
    }
    message = canonical_json(manifest).encode()
    signature = crypto.sign_message(key_name, message)
    manifest["signature"] = signature
    manifest_path = output or artifact_path.with_suffix(artifact_path.suffix + ".blux-manifest.json")
    write_json(manifest_path, manifest)
    manifest_hash = sha256_hex(canonical_json(manifest).encode())
    ledger.append_entry(
        action="sign",
        actor=manifest["key_fingerprint"],
        payload_summary=f"manifest:{manifest_path.name}",
        artifact_hash=artifact_hash,
        manifest_hash=manifest_hash,
    )
    return manifest_path, manifest


def _resolve_artifact(manifest_path: Path, artifact_name: str) -> Path:
    candidate = manifest_path.parent / artifact_name
    return candidate


def verify_manifest(manifest_path: Path) -> bool:
    manifest_path = manifest_path.expanduser().resolve()
    with manifest_path.open("r", encoding="utf-8") as f:
        manifest = json.load(f)
    missing = REQUIRED_FIELDS - manifest.keys()
    if missing:
        raise ValueError(f"Manifest missing fields: {sorted(missing)}")
    artifact_path = _resolve_artifact(manifest_path, manifest["artifact_path"])
    if not artifact_path.exists():
        raise FileNotFoundError(f"Artifact referenced in manifest not found: {artifact_path}")
    expected_hash = _artifact_hash(artifact_path)
    if expected_hash != manifest["artifact_sha256"]:
        return False
    public_key = crypto.find_public_key_by_fingerprint(manifest["key_fingerprint"])
    if public_key is None:
        raise FileNotFoundError("No public key with matching fingerprint found")
    message_fields = {k: manifest[k] for k in manifest if k != "signature"}
    message = canonical_json(message_fields).encode()
    return crypto.verify_signature(public_key, message, manifest["signature"])

FILE: src/blux_reg/tokens.py
Kind: text
Size: 6209
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Capability token issuance and verification."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

from cryptography.hazmat.primitives import serialization

from . import config, crypto, ledger
from .util import canonical_json, load_json, sha256_hex, write_json


TOKEN_SCHEMA_VERSION = "1.0"
TOKEN_TYPE = "capability"
REQUIRED_FIELDS = {
    "schema_version",
    "token_type",
    "issued_at",
    "expires_at",
    "ttl_seconds",
    "capability",
    "audience",
    "constraints",
    "issuer",
    "signature",
}


def _token_dirs() -> Tuple[Path, Path]:
    return config.TOKENS_DIR, config.REVOCATIONS_PATH


def _parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def _payload_from_token(token: Dict[str, Any]) -> Dict[str, Any]:
    return {k: token[k] for k in token if k != "signature"}


def token_ref(token: Dict[str, Any]) -> str:
    return sha256_hex(canonical_json(token).encode())


def hash_token_file(path: Path) -> str:
    token = load_json(path)
    return token_ref(token)


def _issuer_block(key_name: str) -> Dict[str, str]:
    public_bytes = crypto.export_key(key_name, public=True)
    public_key = crypto.load_public_key(key_name)
    return {
        "key_name": key_name,
        "fingerprint": crypto.fingerprint_public_key(public_key),
        "public_key": public_bytes.decode("utf-8"),
    }


def issue_capability_token(
    key_name: str,
    capability: str,
    audience: str,
    ttl_seconds: int,
    constraints: Optional[Dict[str, Any]] = None,
    output_path: Optional[Path] = None,
) -> Tuple[Dict[str, Any], str, Path]:
    if ttl_seconds <= 0:
        raise ValueError("ttl_seconds must be positive")
    config.ensure_directories()
    tokens_dir, _ = _token_dirs()
    tokens_dir.mkdir(parents=True, exist_ok=True)
    issued_at = datetime.now(timezone.utc).replace(microsecond=0)
    expires_at = issued_at + timedelta(seconds=ttl_seconds)
    payload = {
        "schema_version": TOKEN_SCHEMA_VERSION,
        "token_type": TOKEN_TYPE,
        "issued_at": issued_at.isoformat(),
        "expires_at": expires_at.isoformat(),
        "ttl_seconds": ttl_seconds,
        "capability": capability,
        "audience": audience,
        "constraints": constraints or {},
        "issuer": _issuer_block(key_name),
    }
    signature = crypto.sign_message(key_name, canonical_json(payload).encode())
    token = dict(payload)
    token["signature"] = signature
    token_hash = token_ref(token)
    path = output_path or (tokens_dir / f"{token_hash}.json")
    write_json(path, token)
    ledger.append_entry(
        action="token-issue",
        actor=payload["issuer"]["fingerprint"],
        payload_summary=f"capability:{capability}",
        extra={"token_hash": token_hash},
    )
    return token, token_hash, path


def load_token(path: Path) -> Dict[str, Any]:
    return load_json(path)


def _load_public_key(public_pem: str):
    return serialization.load_pem_public_key(public_pem.encode("utf-8"))


def is_token_revoked(token_hash: str) -> bool:
    _, revocations_path = _token_dirs()
    if not revocations_path.exists():
        return False
    with revocations_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            entry = json.loads(line)
            if entry.get("token_hash") == token_hash:
                return True
    return False


def revoke_capability_token(token_hash: str, reason: str, revoker: str) -> Dict[str, Any]:
    config.ensure_directories()
    _, revocations_path = _token_dirs()
    entry = {
        "schema_version": "1.0",
        "token_hash": token_hash,
        "revoked_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "reason": reason,
        "revoker": revoker,
    }
    revocations_path.parent.mkdir(parents=True, exist_ok=True)
    with revocations_path.open("a", encoding="utf-8") as fh:
        fh.write(canonical_json(entry) + "\n")
    ledger.append_entry(
        action="token-revoke",
        actor=revoker,
        payload_summary=f"token:{token_hash}",
        extra={"token_hash": token_hash, "reason": reason},
    )
    return entry


def verify_capability_token(
    token: Dict[str, Any],
    now: Optional[datetime] = None,
    trust_anchors: Optional[set[str]] = None,
    revoked_tokens: Optional[set[str]] = None,
) -> Dict[str, str]:
    missing = REQUIRED_FIELDS - token.keys()
    if missing:
        raise ValueError(f"Token missing fields: {sorted(missing)}")
    if token.get("token_type") != TOKEN_TYPE:
        raise ValueError("Token type mismatch")
    if token.get("schema_version") != TOKEN_SCHEMA_VERSION:
        raise ValueError("Unsupported token schema version")
    payload = _payload_from_token(token)
    issuer = payload.get("issuer", {})
    public_key_pem = issuer.get("public_key")
    if not public_key_pem:
        raise ValueError("Token missing issuer public key")
    public_key = _load_public_key(public_key_pem)
    message = canonical_json(payload).encode()
    if not crypto.verify_signature(public_key, message, token["signature"]):
        raise ValueError("Token signature verification failed")
    if trust_anchors is not None:
        issuer_fingerprint = issuer.get("fingerprint")
        if not issuer_fingerprint or issuer_fingerprint not in trust_anchors:
            raise ValueError("Token issuer not trusted")
    now_dt = now or datetime.now(timezone.utc).replace(microsecond=0)
    expires_at = _parse_iso(payload["expires_at"])
    if expires_at < now_dt:
        raise ValueError("Token has expired")
    token_hash = token_ref(token)
    if revoked_tokens is not None:
        if token_hash in revoked_tokens:
            raise ValueError("Token has been revoked")
    elif is_token_revoked(token_hash):
        raise ValueError("Token has been revoked")
    return {
        "status": "verified",
        "token_hash": token_hash,
        "capability": payload.get("capability"),
        "audience": payload.get("audience"),
        "expires_at": payload.get("expires_at"),
    }

FILE: src/blux_reg/trust_store.py
Kind: text
Size: 4288
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Append-only trust store for issuers and revocations."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set

from .util import canonical_json, sha256_hex

TRUST_STORE_SCHEMA_VERSION = "1.0"
TRUST_ANCHOR_TYPE = "trust_anchor"
TOKEN_REVOCATION_TYPE = "token_revocation"


@dataclass
class TrustStore:
    """In-memory trust store with append-only persistence."""

    path: Path
    entries: List[Dict[str, Any]] = field(default_factory=list)
    pending_entries: List[Dict[str, Any]] = field(default_factory=list)
    last_hash: Optional[str] = None

    def add_entry(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        data = dict(entry)
        data.setdefault("schema_version", TRUST_STORE_SCHEMA_VERSION)
        data["prev_hash"] = self.last_hash
        entry_hash = sha256_hex(canonical_json(data).encode())
        data["entry_hash"] = entry_hash
        self.entries.append(data)
        self.pending_entries.append(data)
        self.last_hash = entry_hash
        return data


def _iter_entries(path: Path) -> Iterable[Dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json_loads(line)


def _compute_entry_hash(entry: Dict[str, Any]) -> str:
    data = dict(entry)
    data.pop("entry_hash", None)
    return sha256_hex(canonical_json(data).encode())


def _verify_chain(entries: Iterable[Dict[str, Any]]) -> Optional[str]:
    prev_hash = None
    last_hash = None
    for entry in entries:
        if entry.get("prev_hash") != prev_hash:
            raise ValueError("Trust store hash chain mismatch")
        if _compute_entry_hash(entry) != entry.get("entry_hash"):
            raise ValueError("Trust store entry hash mismatch")
        last_hash = entry.get("entry_hash")
        prev_hash = last_hash
    return last_hash


def load_trust_store(path: Path) -> TrustStore:
    """Load an append-only trust store from disk."""
    entries = list(_iter_entries(path))
    last_hash = _verify_chain(entries)
    return TrustStore(path=path, entries=entries, last_hash=last_hash)


def save_trust_store(path: Path, store: TrustStore) -> None:
    """Append pending trust store entries to disk."""
    if not store.pending_entries:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        for entry in store.pending_entries:
            fh.write(canonical_json(entry) + "\n")
    store.pending_entries.clear()


def trust_store_index(store: TrustStore) -> Dict[str, Set[str]]:
    """Build index sets for trusted issuers and revoked tokens."""
    trusted_issuers: Set[str] = set()
    revoked_tokens: Set[str] = set()
    for entry in store.entries:
        if entry.get("entry_type") == TRUST_ANCHOR_TYPE:
            fingerprint = entry.get("fingerprint")
            if fingerprint:
                trusted_issuers.add(fingerprint)
        if entry.get("entry_type") == TOKEN_REVOCATION_TYPE:
            token_hash = entry.get("token_hash")
            if token_hash:
                revoked_tokens.add(token_hash)
    return {"trusted_issuers": trusted_issuers, "revoked_tokens": revoked_tokens}


def new_trust_anchor(fingerprint: str, public_key_pem: str, source: str = "local") -> Dict[str, Any]:
    """Create a trust anchor entry for an issuer fingerprint."""
    return {
        "entry_type": TRUST_ANCHOR_TYPE,
        "added_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "fingerprint": fingerprint,
        "public_key": public_key_pem,
        "source": source,
    }


def new_token_revocation(token_hash: str, reason: str) -> Dict[str, Any]:
    """Create a token revocation entry."""
    return {
        "entry_type": TOKEN_REVOCATION_TYPE,
        "revoked_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "token_hash": token_hash,
        "reason": reason,
    }


def json_loads(payload: str) -> Dict[str, Any]:
    """Parse JSON payloads without importing json at module import time."""
    import json

    return json.loads(payload)

FILE: src/blux_reg/util.py
Kind: text
Size: 784
Last modified: 2026-01-21T18:09:23Z

CONTENT:
"""Utility helpers for deterministic serialization and hashing."""
from __future__ import annotations

import json
import hashlib
from pathlib import Path
from typing import Any, Dict


def canonical_json(data: Any) -> str:
    """Return canonical JSON string (sorted keys, no spaces)."""
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")

FILE: tests/conftest.py
Kind: text
Size: 174
Last modified: 2026-01-21T18:09:23Z

CONTENT:
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

FILE: tests/test_boundary_ci.py
Kind: text
Size: 5024
Last modified: 2026-01-22T05:16:02Z

CONTENT:
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CODE_DIRS = [REPO_ROOT / "src", REPO_ROOT / "tests", REPO_ROOT / "scripts", REPO_ROOT / "bin"]

PROHIBITED_CONTENT_PATTERNS = [
    re.compile(r"\bsubprocess\b", re.IGNORECASE),
    re.compile(r"os\.system", re.IGNORECASE),
    re.compile(r"\bexec\(", re.IGNORECASE),
    re.compile(r"\bshell\b", re.IGNORECASE),
    re.compile(r"\bchild_process\b", re.IGNORECASE),
    re.compile(r"\bblux_ca\b", re.IGNORECASE),
    re.compile(r"\bblux_guard\b", re.IGNORECASE),
    re.compile(r"\bblux_lite\b", re.IGNORECASE),
    re.compile(r"\bblux_quantum\b", re.IGNORECASE),
    re.compile(r"\bblux_doctrine\b", re.IGNORECASE),
    re.compile(r"guard_receipt", re.IGNORECASE),
    re.compile(r"discernment_report", re.IGNORECASE),
    re.compile(r"\bexecute\b", re.IGNORECASE),
    re.compile(r"\brouter\b", re.IGNORECASE),
    re.compile(r"\borchestr", re.IGNORECASE),
    re.compile(r"\bpolicy\b", re.IGNORECASE),
    re.compile(r"\bposture\b", re.IGNORECASE),
    re.compile(r"\bethic", re.IGNORECASE),
    re.compile(r"\benforce\b", re.IGNORECASE),
    re.compile(r"\ballow\b[^\n]{0,50}\bintent\b", re.IGNORECASE),
    re.compile(r"\bdeny\b[^\n]{0,50}\bintent\b", re.IGNORECASE),
    re.compile(r"doctrine[^\n]{0,50}engine", re.IGNORECASE),
    re.compile(r"\bquantum\b", re.IGNORECASE),
    re.compile(r"\bdoctrine\b", re.IGNORECASE),
    re.compile(r"\blite\b", re.IGNORECASE),
]

PROHIBITED_PATH_PATTERNS = [
    re.compile(r"contracts", re.IGNORECASE),
    re.compile(r"\bblux_ca\b", re.IGNORECASE),
    re.compile(r"\bblux_guard\b", re.IGNORECASE),
    re.compile(r"\bblux_lite\b", re.IGNORECASE),
    re.compile(r"\bblux_quantum\b", re.IGNORECASE),
    re.compile(r"\bblux_doctrine\b", re.IGNORECASE),
    re.compile(r"guard_receipt", re.IGNORECASE),
    re.compile(r"discernment_report", re.IGNORECASE),
    re.compile(r"\bexecute\b", re.IGNORECASE),
    re.compile(r"\brouter\b", re.IGNORECASE),
    re.compile(r"\borchestr", re.IGNORECASE),
    re.compile(r"\bpolicy\b", re.IGNORECASE),
    re.compile(r"\bposture\b", re.IGNORECASE),
    re.compile(r"\bethic", re.IGNORECASE),
    re.compile(r"\benforce\b", re.IGNORECASE),
    re.compile(r"\ballow\b[^\n]{0,50}\bintent\b", re.IGNORECASE),
    re.compile(r"\bdeny\b[^\n]{0,50}\bintent\b", re.IGNORECASE),
    re.compile(r"doctrine[^\n]{0,50}engine", re.IGNORECASE),
    re.compile(r"\bquantum\b", re.IGNORECASE),
    re.compile(r"\bdoctrine\b", re.IGNORECASE),
    re.compile(r"\blite\b", re.IGNORECASE),
]

PROHIBITED_SCHEMA_ID = re.compile(r"\$id\s*:\s*\"blux://contracts/", re.IGNORECASE)

ALLOWLIST = {
    "tests/test_boundary_ci.py",
    "scripts/physics_check.sh",
}


def _iter_code_files():
    for root in CODE_DIRS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if "__pycache__" in path.parts:
                continue
            rel_path = path.relative_to(REPO_ROOT).as_posix()
            if rel_path in ALLOWLIST:
                continue
            yield path, rel_path


def test_boundary_no_forbidden_logic_or_contracts():
    violations = []

    if (REPO_ROOT / "contracts").exists():
        violations.append("path:contracts:contracts-directory")
    schema_files = []
    for path in REPO_ROOT.rglob("*.schema.json"):
        rel_parts = path.relative_to(REPO_ROOT).parts
        if len(rel_parts) >= 2 and rel_parts[0] == "tests" and rel_parts[1] == "fixtures":
            continue
        schema_files.append(path)
    for path in schema_files:
        rel_path = path.relative_to(REPO_ROOT).as_posix()
        violations.append(f"schema:{rel_path}:schema-file-outside-fixtures")

    for path, rel_path in _iter_code_files():
        for pattern in PROHIBITED_PATH_PATTERNS:
            if pattern.search(rel_path):
                violations.append(f"path:{rel_path}:{pattern.pattern}")
                break
        else:
            content = path.read_text(encoding="utf-8", errors="ignore")
            if PROHIBITED_SCHEMA_ID.search(content):
                violations.append(f"schema:{rel_path}:blux-contract-id")
                continue
            for pattern in PROHIBITED_CONTENT_PATTERNS:
                if pattern.search(content):
                    violations.append(f"content:{rel_path}:{pattern.pattern}")
                    break

    for path in REPO_ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if "__pycache__" in path.parts:
            continue
        if not path.is_file():
            continue
        rel_path = path.relative_to(REPO_ROOT).as_posix()
        if rel_path in ALLOWLIST:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        if PROHIBITED_SCHEMA_ID.search(content):
            violations.append(f"schema:{rel_path}:blux-contract-id")

    assert not violations, "Boundary violation(s) detected:\n" + "\n".join(violations)

FILE: tests/test_crypto.py
Kind: text
Size: 479
Last modified: 2026-01-21T18:09:23Z

CONTENT:
from blux_reg import config, crypto


def test_keygen_sign_verify(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()
    crypto.generate_keypair("test")

    message = b"hello"
    signature = crypto.sign_message("test", message)
    public_key = crypto.load_public_key("test")
    assert crypto.verify_signature(public_key, message, signature)
    assert not crypto.verify_signature(public_key, b"tamper", signature)

FILE: tests/test_flow.py
Kind: text
Size: 1688
Last modified: 2026-01-21T18:09:23Z

CONTENT:
import json
import os
from pathlib import Path

import pytest

from blux_reg import config, crypto, ledger, manifest


@pytest.fixture(autouse=True)
def temp_config(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path / "cfg"))
    config.refresh_paths()
    yield


def test_keygen_creates_keys():
    info = crypto.generate_keypair("test")
    assert info.private_path.exists()
    assert info.public_path.exists()
    assert info.fingerprint


def test_sign_and_verify(tmp_path):
    artifact = tmp_path / "sample.txt"
    artifact.write_text("hello")
    crypto.generate_keypair("test")
    manifest_path, data = manifest.sign_artifact(artifact, "test")
    assert manifest_path.exists()
    assert manifest.verify_manifest(manifest_path)
    assert data["artifact_sha256"]


def test_tamper_manifest(tmp_path):
    artifact = tmp_path / "sample.txt"
    artifact.write_text("hello")
    crypto.generate_keypair("test")
    manifest_path, _ = manifest.sign_artifact(artifact, "test")
    data = json.loads(manifest_path.read_text())
    data["artifact_sha256"] = "0" * 64
    manifest_path.write_text(json.dumps(data))
    assert not manifest.verify_manifest(manifest_path)


def test_ledger_tamper_detection(tmp_path):
    artifact = tmp_path / "sample.txt"
    artifact.write_text("hello")
    crypto.generate_keypair("test")
    manifest.sign_artifact(artifact, "test")
    assert ledger.verify_chain()
    # tamper first line
    ledger_path = config.LEDGER_PATH
    lines = ledger_path.read_text().splitlines()
    lines[0] = lines[0].replace("sign", "signx")
    ledger_path.write_text("\n".join(lines) + "\n")
    assert not ledger.verify_chain()

FILE: tests/test_ledger.py
Kind: text
Size: 677
Last modified: 2026-01-21T18:09:23Z

CONTENT:
import json

from blux_reg import config, ledger


def test_ledger_chain_and_tamper(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()

    ledger.append_entry(action="event", actor="tester", payload_summary="first")
    ledger.append_entry(action="event", actor="tester", payload_summary="second")

    assert ledger.verify_chain()

    ledger_path = config.LEDGER_PATH
    lines = ledger_path.read_text().splitlines()
    tampered = json.loads(lines[0])
    tampered["action"] = "tamper"
    lines[0] = json.dumps(tampered)
    ledger_path.write_text("\n".join(lines) + "\n")

    assert not ledger.verify_chain()

FILE: tests/test_tokens.py
Kind: text
Size: 2356
Last modified: 2026-01-21T18:09:23Z

CONTENT:
from datetime import datetime, timedelta, timezone

import pytest

from blux_reg import config, crypto, tokens


def _setup_key(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()
    crypto.generate_keypair("issuer")


def test_token_validates(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-example",
        3600,
        {"scope": "release"},
    )
    result = tokens.verify_capability_token(token)
    assert result["token_hash"] == token_hash


def test_token_expired_fails(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, _, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-example",
        1,
        {},
    )
    expires_at = datetime.fromisoformat(token["expires_at"])
    with pytest.raises(ValueError, match="expired"):
        tokens.verify_capability_token(token, now=expires_at + timedelta(seconds=1))


def test_token_revoked_fails(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-example",
        3600,
        {},
    )
    tokens.revoke_capability_token(token_hash, "compromised", "security-team")
    with pytest.raises(ValueError, match="revoked"):
        tokens.verify_capability_token(token)


def test_token_tampered_fails(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, _, _ = tokens.issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-example",
        3600,
        {},
    )
    token["capability"] = "delete"
    with pytest.raises(ValueError, match="signature"):
        tokens.verify_capability_token(token)


def test_token_hash_roundtrip(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, path = tokens.issue_capability_token(
        "issuer",
        "deploy",
        "outer-void/blux-example",
        3600,
        {},
    )
    assert tokens.hash_token_file(path) == token_hash
    now = datetime.now(timezone.utc).replace(microsecond=0)
    assert tokens.verify_capability_token(token, now=now)["status"] == "verified"

FILE: tests/test_trust_store.py
Kind: text
Size: 1357
Last modified: 2026-01-21T18:09:23Z

CONTENT:
from datetime import datetime, timezone

from blux_reg import config, crypto, load_trust_store, revoke_token, save_trust_store, verify_token
from blux_reg.trust_store import new_trust_anchor
from blux_reg.tokens import issue_capability_token


def _setup_key(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_REG_CONFIG_DIR", str(tmp_path))
    config.refresh_paths()
    crypto.generate_keypair("issuer")


def test_trust_store_revocation(tmp_path, monkeypatch):
    _setup_key(tmp_path, monkeypatch)
    token, token_hash, _ = issue_capability_token(
        "issuer",
        "publish",
        "outer-void/blux-example",
        3600,
        {},
    )
    store_path = tmp_path / "trust_store.jsonl"
    store = load_trust_store(store_path)

    public_key = crypto.load_public_key("issuer")
    public_pem = crypto.export_key("issuer", public=True).decode("utf-8")
    anchor = new_trust_anchor(crypto.fingerprint_public_key(public_key), public_pem)
    store.add_entry(anchor)
    save_trust_store(store_path, store)

    result = verify_token(token, store_path, now=datetime.now(timezone.utc))
    assert result["valid"] is True

    revoke_token(token_hash, "compromised", store_path)
    result = verify_token(token, store_path, now=datetime.now(timezone.utc))
    assert result["valid"] is False
    assert "revoked" in result["reason_codes"]

## 4) Workflow Inventory (index only)
.github/workflows/ci.yml
  triggers: pull_request, push

## 5) Search Index (raw results)

subprocess:
./tests/test_boundary_ci.py
./scripts/physics_check.sh

os.system:
none

exec(:
none

spawn:
none

shell:
./tests/test_boundary_ci.py
./scripts/physics_check.sh

child_process:
./tests/test_boundary_ci.py
./scripts/physics_check.sh

policy:
./docs/roles.md
./tests/test_boundary_ci.py
./README.md
./scripts/physics_check.sh

ethic:
./tests/test_boundary_ci.py
./scripts/physics_check.sh

enforce:
./docs/roles.md
./tests/test_boundary_ci.py
./ROLE.md
./README.md
./scripts/physics_check.sh
./plan.md

guard:
./tests/test_boundary_ci.py
./README.md
./scripts/physics_check.sh
./plan.md

receipt:
./docs/roles.md
./tests/test_boundary_ci.py
./README.md
./scripts/physics_check.sh

token:
./docs/CONTRACT.md
./docs/roles.md
./tests/test_tokens.py
./tests/test_trust_store.py
./ROLE.md
./README.md
./src/blux_reg/cli.py
./src/blux_reg/api.py
./src/blux_reg/config.py
./src/blux_reg/tokens.py
./src/blux_reg/__init__.py
./src/blux_reg/trust_store.py
./scripts/demo_unified_reg.sh

signature:
./docs/CONTRACT.md
./tests/test_tokens.py
./tests/test_crypto.py
./src/blux_reg/manifest.py
./README.md
./src/blux_reg/api.py
./src/blux_reg/crypto.py
./src/blux_reg/tokens.py
./plan.md

verify:
./docs/CONTRACT.md
./tests/test_tokens.py
./tests/test_trust_store.py
./tests/test_ledger.py
./tests/test_flow.py
./tests/test_crypto.py
./README.md
./src/blux_reg/manifest.py
./src/blux_reg/cli.py
./src/blux_reg/api.py
./src/blux_reg/crypto.py
./src/blux_reg/ledger.py
./src/blux_reg/tokens.py
./src/blux_reg/__init__.py
./src/blux_reg/trust_store.py
./scripts/demo_unified_reg.sh

capability:
./docs/CONTRACT.md
./docs/roles.md
./tests/test_tokens.py
./tests/test_trust_store.py
./ROLE.md
./src/blux_reg/cli.py
./README.md
./src/blux_reg/api.py
./src/blux_reg/tokens.py

key_id:
none

contract:
./docs/CONTRACT.md
./docs/roles.md
./LICENSE-APACHE
./tests/test_boundary_ci.py
./README.md
./scripts/physics_check.sh
./plan.md

schema:
./docs/CONTRACT.md
./tests/test_boundary_ci.py
./README.md
./src/blux_reg/manifest.py
./src/blux_reg/api.py
./src/blux_reg/tokens.py
./src/blux_reg/trust_store.py
./scripts/physics_check.sh

$schema:
none

json-schema:
none

router:
./tests/test_boundary_ci.py
./scripts/physics_check.sh

orchestr:
./docs/roles.md
./tests/test_boundary_ci.py
./README.md
./scripts/physics_check.sh

execute:
./docs/roles.md
./LICENSE-APACHE
./tests/test_boundary_ci.py
./README.md
./scripts/physics_check.sh

command:
./scripts/demo_unified_reg.sh
./src/blux_reg/cli.py

## 6) Notes
none
