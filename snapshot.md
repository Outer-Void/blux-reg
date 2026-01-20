# Repository Snapshot

## 1) Metadata
- Repository name: blux-reg
- Organization / owner: unknown
- Default branch: unknown
- HEAD commit hash: 47cddb32429e916600275796a48feabb9cf6653e
- Snapshot timestamp (UTC): 2026-01-20T13:56:39Z
- Total file count (excluding directories): 45
- Short description: **Identity and Trust Backbone for the BLUX Ecosystem**

## 2) Repository Tree
blux-reg/
├── .github/
│   └── workflows/
│       └── ci.yml [text]
├── .gitignore [text]
├── COMMERCIAL.md [text]
├── LICENSE [text]
├── LICENSE-APACHE [text]
├── LICENSE-COMMERCIAL [text]
├── NOTICE [text]
├── README.md [text]
├── ROLE.md [text]
├── bin/
│   └── blux-reg [text]
├── blux_reg/
│   ├── __init__.py [text]
│   ├── cli.py [text]
│   ├── crypto.py [text]
│   ├── doctor.py [text]
│   ├── keystore.py [text]
│   ├── ledger.py [text]
│   ├── paths.py [text]
│   ├── registry.py [text]
│   └── tokens.py [text]
├── docs/
│   ├── CONTRACT.md [text]
│   └── roles.md [text]
├── plan.md [text]
├── pyproject.toml [text]
├── requirements-dev.txt [text]
├── requirements.txt [text]
├── schemas/
│   ├── capability_manifest.schema.json [text]
│   ├── capability_token.schema.json [text]
│   └── revocation.schema.json [text]
├── scripts/
│   ├── demo_unified_reg.sh [text]
│   └── physics_check.sh [text]
├── snapshot.md [text]
├── src/
│   └── blux_reg/
│       ├── __init__.py [text]
│       ├── cli.py [text]
│       ├── config.py [text]
│       ├── crypto.py [text]
│       ├── ledger.py [text]
│       ├── manifest.py [text]
│       ├── tokens.py [text]
│       └── util.py [text]
└── tests/
    ├── conftest.py [text]
    ├── test_boundary_ci.py [text]
    ├── test_crypto.py [text]
    ├── test_flow.py [text]
    ├── test_ledger.py [text]
    └── test_tokens.py [text]

## 3) FULL FILE CONTENTS (MANDATORY)

FILE: .github/workflows/ci.yml
Kind: text
Size: 593
Last modified: 2026-01-20T13:55:06Z

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
Last modified: 2026-01-20T06:55:50Z

CONTENT:
__pycache__/
*.pyc
*.pyo
*.egg-info/

FILE: COMMERCIAL.md
Kind: text
Size: 669
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T06:55:50Z

CONTENT:
This project is dual-licensed.

- Open-source use is governed by the Apache License, Version 2.0. See LICENSE-APACHE for full terms.
- Commercial use requires a separate commercial agreement. See LICENSE-COMMERCIAL for details.

Unless otherwise noted, source files include a copyright notice reflecting the project copyright holder.

FILE: LICENSE-APACHE
Kind: text
Size: 11342
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T06:55:50Z

CONTENT:
blux-reg
Copyright (c) 2025 - Outer-Void

This product includes software developed by the blux-reg project.
Licensed under the Apache License, Version 2.0. See LICENSE-APACHE for details.

FILE: README.md
Kind: text
Size: 15920
Last modified: 2026-01-20T13:55:06Z

CONTENT:
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

FILE: ROLE.md
Kind: text
Size: 175
Last modified: 2026-01-20T13:55:06Z

CONTENT:
# ROLE

BLUX-Reg is a trust kernel for capability tokens only: it issues, hashes, verifies, and revokes tokens offline.

No policy decisions; no judgment logic; no execution.

FILE: bin/blux-reg
Kind: text
Size: 365
Last modified: 2026-01-20T13:55:06Z

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

FILE: blux_reg/__init__.py
Kind: text
Size: 315
Last modified: 2026-01-20T06:55:50Z

CONTENT:
"""BLUX-Reg core package."""

from .tokens import (
    issue_capability_token,
    load_token,
    revoke_capability_token,
    show_token,
    verify_capability_token,
)

__all__ = [
    "issue_capability_token",
    "load_token",
    "revoke_capability_token",
    "show_token",
    "verify_capability_token",
]

FILE: blux_reg/cli.py
Kind: text
Size: 9946
Last modified: 2026-01-20T06:55:50Z

CONTENT:
from __future__ import annotations

import argparse
import json
import sys
from getpass import getpass
from pathlib import Path

from .crypto import PassphraseError
from .keystore import KeyStore
from .ledger import LEDGERS, get_ledger
from .registry import (
    create_key,
    ensure_structure,
    export_public_key,
    list_keys,
    revoke_key,
    sign_artifact,
    verify_artifact,
)
from .tokens import issue_capability_token, load_token, revoke_capability_token, show_token, verify_capability_token

KEY_TYPES = {"project", "plugin", "user"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="BLUX-Reg identity and trust CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("init", help="initialise BLUX-Reg directories and ledgers")

    keys = sub.add_parser("keys", help="manage key material")
    keys_sub = keys.add_subparsers(dest="keys_cmd")

    create = keys_sub.add_parser("create", help="create a new Ed25519 keypair")
    create.add_argument("key_id", help="identifier for the key (e.g. project slug)")
    create.add_argument("key_type", choices=sorted(KEY_TYPES), help="key classification")
    create.add_argument("--passphrase", help="passphrase protecting the key (optional)")

    keys_sub.add_parser("list", help="list known keys")

    export = keys_sub.add_parser("export", help="export a public key as JSON")
    export.add_argument("key_id")
    export.add_argument("--key-type", choices=sorted(KEY_TYPES))

    revoke = keys_sub.add_parser("revoke", help="revoke a key via append-only ledger")
    revoke.add_argument("key_id")
    revoke.add_argument("--reason", default="unspecified")
    revoke.add_argument("--revoker", required=True, help="identifier authorising the revocation")

    sign_parser = sub.add_parser("sign", help="sign an artifact and append to ledger")
    sign_parser.add_argument("path", type=Path)
    sign_parser.add_argument("key_id")
    sign_parser.add_argument("key_type", choices=sorted(KEY_TYPES))
    sign_parser.add_argument("context", help="description of what is being signed (project/plugin/user)")
    sign_parser.add_argument("--passphrase")

    verify_parser = sub.add_parser("verify", help="offline verification of a signed artifact")
    verify_parser.add_argument("path", type=Path)
    verify_parser.add_argument("--signature", type=Path, help="explicit signature JSON to verify")

    chain_parser = sub.add_parser("audit", help="inspect ledger health")
    chain_parser.add_argument("ledger", choices=sorted(LEDGERS.keys()))

    token_parser = sub.add_parser("token", help="manage capability tokens")
    token_sub = token_parser.add_subparsers(dest="token_cmd")

    token_issue = token_sub.add_parser("issue", help="issue a capability token")
    token_issue.add_argument("key_id")
    token_issue.add_argument("key_type", choices=sorted(KEY_TYPES))
    token_issue.add_argument("capability", help="capability name")
    token_issue.add_argument("audience_repo", help="audience repository")
    token_issue.add_argument("ttl_seconds", type=int, help="token lifetime in seconds")
    token_issue.add_argument("--constraints", default="{}", help="JSON constraints object")
    token_issue.add_argument("--passphrase")

    token_verify = token_sub.add_parser("verify", help="verify a capability token")
    token_verify.add_argument("token_path", type=Path)

    token_revoke = token_sub.add_parser("revoke", help="revoke a capability token")
    token_revoke.add_argument("token_hash")
    token_revoke.add_argument("--reason", default="unspecified")
    token_revoke.add_argument("--revoker", required=True)

    token_show = token_sub.add_parser("show", help="show a capability token")
    token_show.add_argument("token_path", type=Path)

    return parser


def handle_init(args: argparse.Namespace) -> int:
    ensure_structure()
    print("[*] BLUX-Reg directories ready")
    for name, ledger in LEDGERS.items():
        print(f"    - ledger {name}: {ledger.path}")
    return 0


def prompt_passphrase(existing: bool = False, provided: str | None = None) -> str:
    if provided is not None:
        return provided
    prompt = "Passphrase: " if existing else "New passphrase: "
    confirm = "Confirm passphrase: "
    pwd = getpass(prompt)
    if not existing:
        confirm_pwd = getpass(confirm)
        if pwd != confirm_pwd:
            raise ValueError("Passphrases did not match")
    if not pwd:
        raise ValueError("Passphrase may not be empty")
    return pwd


def handle_keys(args: argparse.Namespace) -> int:
    ks = KeyStore()
    if args.keys_cmd == "create":
        try:
            passphrase = prompt_passphrase(provided=args.passphrase)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        material = create_key(args.key_id, args.key_type, passphrase, keystore=ks)
        print(f"[+] Created {args.key_type} key '{args.key_id}'")
        print(json.dumps(export_public_key(material), indent=2, sort_keys=True))
        return 0
    if args.keys_cmd == "list":
        rows = list(list_keys(keystore=ks))
        if not rows:
            print("(no keys found)")
            return 0
        for material in rows:
            print(f"- {material.key_id} [{material.key_type}] created {material.created_at}")
        return 0
    if args.keys_cmd == "export":
        try:
            material = ks.load(args.key_id, args.key_type)
        except FileNotFoundError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(json.dumps(export_public_key(material), indent=2, sort_keys=True))
        return 0
    if args.keys_cmd == "revoke":
        entry = revoke_key(args.key_id, args.reason, args.revoker)
        print(f"[!] Revoked key {args.key_id} (chain hash: {entry.chain_hash})")
        return 0
    print("usage: blux-reg keys [create|list|export|revoke]", file=sys.stderr)
    return 1


def handle_sign(args: argparse.Namespace) -> int:
    try:
        passphrase = prompt_passphrase(existing=True, provided=args.passphrase)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    try:
        signature_path = sign_artifact(args.key_id, args.key_type, args.path, passphrase, args.context)
    except FileNotFoundError:
        print(f"artifact {args.path} not found", file=sys.stderr)
        return 1
    except PassphraseError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(f"[+] Signed artifact -> {signature_path}")
    return 0


def handle_verify(args: argparse.Namespace) -> int:
    try:
        outcome = verify_artifact(args.path, args.signature)
    except Exception as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(outcome, indent=2, sort_keys=True))
    return 0


def handle_audit(args: argparse.Namespace) -> int:
    ledger = get_ledger(args.ledger)
    ok = ledger.verify_chain()
    print(f"Ledger {args.ledger}: {'OK' if ok else 'BROKEN'}")
    print(f"Entries: {len(ledger.entries())}")
    return 0 if ok else 2


def _parse_constraints(raw: str) -> dict:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid constraints JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Constraints must be a JSON object")
    return data


def handle_token(args: argparse.Namespace) -> int:
    if args.token_cmd == "issue":
        try:
            passphrase = prompt_passphrase(existing=True, provided=args.passphrase)
            constraints = _parse_constraints(args.constraints)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        try:
            token, token_hash, path = issue_capability_token(
                args.key_id,
                args.key_type,
                passphrase,
                args.capability,
                args.audience_repo,
                args.ttl_seconds,
                constraints,
            )
        except (FileNotFoundError, PassphraseError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(json.dumps({"token_hash": token_hash, "token_path": str(path), "token": token}, indent=2))
        return 0
    if args.token_cmd == "verify":
        try:
            token = load_token(args.token_path)
            outcome = verify_capability_token(token)
        except Exception as exc:
            print(f"verification failed: {exc}", file=sys.stderr)
            return 1
        print(json.dumps(outcome, indent=2, sort_keys=True))
        return 0
    if args.token_cmd == "revoke":
        revoke_capability_token(args.token_hash, args.reason, args.revoker)
        print(f"[!] Revoked token {args.token_hash}")
        return 0
    if args.token_cmd == "show":
        try:
            payload = show_token(args.token_path)
        except FileNotFoundError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0
    print("usage: blux-reg token [issue|verify|revoke|show]", file=sys.stderr)
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.cmd is None:
        parser.print_help()
        return 1
    if args.cmd == "init":
        return handle_init(args)
    if args.cmd == "keys":
        return handle_keys(args)
    if args.cmd == "sign":
        return handle_sign(args)
    if args.cmd == "verify":
        return handle_verify(args)
    if args.cmd == "audit":
        return handle_audit(args)
    if args.cmd == "token":
        return handle_token(args)
    parser.print_help()
    return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())

FILE: blux_reg/crypto.py
Kind: text
Size: 2601
Last modified: 2026-01-20T06:55:50Z

CONTENT:
from __future__ import annotations

import base64
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from nacl import signing

from .ledger import canonical_bytes

PASSWORD_HASHER = PasswordHasher(time_cost=3, memory_cost=2**16, parallelism=2, hash_len=32, salt_len=16)


@dataclass
class KeyMaterial:
    key_id: str
    key_type: str
    created_at: str
    public_key: str
    private_seed: str
    argon2_hash: str
    compatibility: dict

    def signing_key(self, passphrase: Optional[str] = None) -> signing.SigningKey:
        seed = base64.b64decode(self.private_seed)
        if passphrase is not None:
            verify_passphrase(self.argon2_hash, passphrase)
        return signing.SigningKey(seed)

    def verify_key(self) -> signing.VerifyKey:
        raw_public = base64.b64decode(self.public_key)
        return signing.VerifyKey(raw_public)


class PassphraseError(Exception):
    pass


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def generate_ed25519(passphrase: str, key_id: str, key_type: str, compatibility: Optional[dict] = None) -> KeyMaterial:
    signing_key = signing.SigningKey.generate()
    verify_key = signing_key.verify_key
    private_seed = signing_key.encode()
    public_bytes = verify_key.encode()
    argon_hash = PASSWORD_HASHER.hash(passphrase)
    return KeyMaterial(
        key_id=key_id,
        key_type=key_type,
        created_at=now_iso(),
        public_key=base64.b64encode(public_bytes).decode("ascii"),
        private_seed=base64.b64encode(private_seed).decode("ascii"),
        argon2_hash=argon_hash,
        compatibility=compatibility or {},
    )


def verify_passphrase(stored_hash: str, candidate: str) -> None:
    try:
        PASSWORD_HASHER.verify(stored_hash, candidate)
    except VerifyMismatchError as exc:
        raise PassphraseError("Invalid passphrase") from exc


def sign_payload(material: KeyMaterial, payload: dict, passphrase: str) -> str:
    signing_key = material.signing_key(passphrase)
    signature = signing_key.sign(canonical_bytes(payload)).signature
    return base64.b64encode(signature).decode("ascii")


def verify_signature(public_key_b64: str, payload: dict, signature_b64: str) -> bool:
    verify_key = signing.VerifyKey(base64.b64decode(public_key_b64))
    try:
        verify_key.verify(canonical_bytes(payload), base64.b64decode(signature_b64))
        return True
    except Exception:
        return False

FILE: blux_reg/doctor.py
Kind: text
Size: 1863
Last modified: 2026-01-20T06:55:50Z

CONTENT:
import importlib
import sys
from pathlib import Path
from typing import List, Tuple

from .paths import CONFIG_ENV, get_artifacts_dir, get_config_root, get_keys_dir, get_ledger_path


class DoctorIssue(Exception):
    pass


def _check_python_version(min_major=3, min_minor=10) -> Tuple[bool, str]:
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (min_major, min_minor)
    return ok, f"Python >= {min_major}.{min_minor} required (found {major}.{minor})"


def _check_dependency(module: str) -> Tuple[bool, str]:
    try:
        importlib.import_module(module)
        return True, ""
    except ImportError:
        return False, f"Install dependency: pip install {module}"


def _check_directory(path: Path) -> Tuple[bool, str]:
    try:
        path.mkdir(parents=True, exist_ok=True)
        test_file = path / ".__blux_perm_test"
        test_file.write_text("ok")
        test_file.unlink()
        return True, ""
    except Exception as exc:
        return False, f"Directory not writable: {path} ({exc})"


def run_doctor() -> Tuple[bool, List[str]]:
    messages: List[str] = []
    checks: List[Tuple[bool, str]] = []
    checks.append(_check_python_version())
    checks.append(_check_dependency("cryptography"))

    config_root = get_config_root()
    keys_dir = get_keys_dir()
    ledger_dir = get_ledger_path().parent
    artifacts_dir = get_artifacts_dir()

    for path in [config_root, keys_dir, ledger_dir, artifacts_dir]:
        checks.append(_check_directory(path))

    ok = True
    for passed, msg in checks:
        if not passed:
            ok = False
            messages.append(msg)
    if not ok:
        messages.append(
            "Set BLUX_CONFIG_HOME to override config root if needed: "
            f"export {CONFIG_ENV}=<path>"
        )
    return ok, messages


__all__ = ["run_doctor", "DoctorIssue"]

FILE: blux_reg/keystore.py
Kind: text
Size: 1656
Last modified: 2026-01-20T06:55:50Z

CONTENT:
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Iterable, Optional

from .crypto import KeyMaterial
from .paths import KEYSTORE_ROOT


class KeyStore:
    def __init__(self, root: Path = KEYSTORE_ROOT):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def _path_for(self, key_id: str, key_type: str) -> Path:
        safe_id = key_id.replace("/", "_")
        safe_type = key_type.replace("/", "_")
        return self.root / f"{safe_type}-{safe_id}.json"

    def save(self, material: KeyMaterial) -> Path:
        path = self._path_for(material.key_id, material.key_type)
        payload = asdict(material)
        with path.open("w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, sort_keys=True)
        return path

    def load(self, key_id: str, key_type: Optional[str] = None) -> KeyMaterial:
        candidates = []
        if key_type:
            candidates.append(self._path_for(key_id, key_type))
        else:
            pattern = f"*-{key_id.replace('/', '_')}.json"
            candidates.extend(self.root.glob(pattern))
        for path in candidates:
            if path.exists():
                with path.open("r", encoding="utf-8") as fh:
                    data = json.load(fh)
                return KeyMaterial(**data)
        raise FileNotFoundError(f"Key {key_id} not found in keystore")

    def list(self) -> Iterable[KeyMaterial]:
        for path in sorted(self.root.glob("*.json")):
            with path.open("r", encoding="utf-8") as fh:
                yield KeyMaterial(**json.load(fh))

FILE: blux_reg/ledger.py
Kind: text
Size: 3362
Last modified: 2026-01-20T06:55:50Z

CONTENT:
from __future__ import annotations

import json
import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Optional

from .paths import LEDGER_PATHS

CANONICAL_SEPARATORS = (",", ":")


def canonical_dumps(data: dict) -> str:
    return json.dumps(data, sort_keys=True, separators=CANONICAL_SEPARATORS)


def canonical_bytes(data: dict) -> bytes:
    return canonical_dumps(data).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass
class LedgerEntry:
    raw: dict

    @property
    def prev_hash(self) -> Optional[str]:
        return self.raw.get("prev_hash")

    @property
    def chain_hash(self) -> Optional[str]:
        return self.raw.get("chain_hash")

    def payload_bytes(self) -> bytes:
        payload = dict(self.raw)
        payload.pop("chain_hash", None)
        return canonical_bytes(payload)


class Ledger:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _iter_lines(self) -> Iterator[str]:
        if not self.path.exists():
            return iter(())
        with self.path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    yield line

    def entries(self) -> List[LedgerEntry]:
        return [LedgerEntry(json.loads(line)) for line in self._iter_lines()]

    def last_hash(self) -> Optional[str]:
        last_line = None
        for last_line in self._iter_lines():
            pass
        if last_line is None:
            return None
        payload = json.loads(last_line)
        payload.pop("chain_hash", None)
        return sha256_hex(canonical_bytes(payload))

    def append(self, entry: dict) -> LedgerEntry:
        entry = dict(entry)
        prev_hash = self.last_hash()
        if prev_hash:
            entry.setdefault("prev_hash", prev_hash)
        elif "prev_hash" in entry and entry["prev_hash"] is None:
            entry.pop("prev_hash")
        payload_bytes = canonical_bytes(entry)
        chain_hash = sha256_hex(payload_bytes)
        entry_with_hash = dict(entry)
        entry_with_hash["chain_hash"] = chain_hash
        line = canonical_dumps(entry_with_hash)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
        return LedgerEntry(entry_with_hash)

    def verify_chain(self) -> bool:
        prev_hash = None
        for entry in self.entries():
            payload = dict(entry.raw)
            chain_hash = payload.pop("chain_hash", None)
            payload_bytes = canonical_bytes(payload)
            computed_hash = sha256_hex(payload_bytes)
            if computed_hash != chain_hash:
                return False
            if prev_hash != payload.get("prev_hash"):
                if prev_hash is None and payload.get("prev_hash") in (None, ""):
                    pass
                else:
                    return False
            prev_hash = computed_hash
        return True


LEDGERS = {name: Ledger(path) for name, path in LEDGER_PATHS.items()}


def get_ledger(name: str) -> Ledger:
    try:
        return LEDGERS[name]
    except KeyError:
        raise ValueError(f"Unknown ledger '{name}'. Known: {', '.join(sorted(LEDGERS))}")

FILE: blux_reg/paths.py
Kind: text
Size: 577
Last modified: 2026-01-20T06:55:50Z

CONTENT:
from __future__ import annotations

from pathlib import Path

HOME = Path.home()
REGROOT = HOME / "blux-reg"
REGISTRY_ROOT = REGROOT / "registry"
KEYSTORE_ROOT = HOME / ".config" / "blux-reg" / "keys"
SIGNATURES_ROOT = REGROOT / "signatures"
TOKENS_ROOT = REGROOT / "tokens"

LEDGER_PATHS = {
    "keys": REGISTRY_ROOT / "keys.jsonl",
    "artifacts": REGISTRY_ROOT / "artifacts.jsonl",
    "revocations": REGISTRY_ROOT / "revocations.jsonl",
    "tokens": REGISTRY_ROOT / "tokens.jsonl",
}

REQUIRED_COMPATIBILITY = {
    "BLUX-Quantum": ">=1.0",
    "BLUX-Guard": ">=1.0",
}

FILE: blux_reg/registry.py
Kind: text
Size: 5890
Last modified: 2026-01-20T06:55:50Z

CONTENT:
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, Optional

from .crypto import KeyMaterial, generate_ed25519, now_iso, sign_payload, verify_signature
from .keystore import KeyStore
from .ledger import LedgerEntry, get_ledger
from .paths import LEDGER_PATHS, REQUIRED_COMPATIBILITY, SIGNATURES_ROOT, TOKENS_ROOT


def ensure_structure() -> None:
    SIGNATURES_ROOT.mkdir(parents=True, exist_ok=True)
    TOKENS_ROOT.mkdir(parents=True, exist_ok=True)
    for path in LEDGER_PATHS.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.touch()


def create_key(key_id: str, key_type: str, passphrase: str, keystore: Optional[KeyStore] = None) -> KeyMaterial:
    ensure_structure()
    ks = keystore or KeyStore()
    compatibility = {
        "BLUX-Quantum": REQUIRED_COMPATIBILITY["BLUX-Quantum"],
        "BLUX-Guard": REQUIRED_COMPATIBILITY["BLUX-Guard"],
    }
    material = generate_ed25519(passphrase, key_id=key_id, key_type=key_type, compatibility=compatibility)
    ks.save(material)
    payload = {
        "event": "key_issued",
        "timestamp": material.created_at,
        "key_id": material.key_id,
        "key_type": material.key_type,
        "public_key": material.public_key,
        "compatibility": compatibility,
    }
    signature = sign_payload(material, payload, passphrase)
    get_ledger("keys").append({
        "timestamp": material.created_at,
        "issuer": material.key_id,
        "role": material.key_type,
        "payload": payload,
        "signature": signature,
    })
    return material


def list_keys(keystore: Optional[KeyStore] = None) -> Iterable[KeyMaterial]:
    ks = keystore or KeyStore()
    yield from ks.list()


def export_public_key(material: KeyMaterial) -> dict:
    return {
        "key_id": material.key_id,
        "key_type": material.key_type,
        "public_key": material.public_key,
        "created_at": material.created_at,
        "compatibility": material.compatibility,
    }


def sign_artifact(
    key_id: str,
    key_type: str,
    path: Path,
    passphrase: str,
    context: str,
    keystore: Optional[KeyStore] = None,
) -> Path:
    ensure_structure()
    ks = keystore or KeyStore()
    material = ks.load(key_id, key_type)
    payload = {
        "event": "artifact_signed",
        "timestamp": now_iso(),
        "artifact": {
            "path": str(path.resolve()),
            "sha256": compute_file_sha256(path),
            "context": context,
        },
        "key_id": material.key_id,
        "key_type": material.key_type,
        "compatibility": material.compatibility,
    }
    signature = sign_payload(material, payload, passphrase)
    entry = {
        "timestamp": payload["timestamp"],
        "issuer": material.key_id,
        "role": material.key_type,
        "payload": payload,
        "signature": signature,
    }
    get_ledger("artifacts").append(entry)
    signature_path = SIGNATURES_ROOT / f"{path.name}.sig.json"
    signature_payload = {
        "payload": payload,
        "signature": signature,
        "public_key": material.public_key,
    }
    with signature_path.open("w", encoding="utf-8") as fh:
        json.dump(signature_payload, fh, indent=2, sort_keys=True)
    return signature_path


def compute_file_sha256(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def revoke_key(key_id: str, reason: str, revoker: str) -> LedgerEntry:
    ensure_structure()
    payload = {
        "event": "key_revoked",
        "timestamp": now_iso(),
        "revoked_key_id": key_id,
        "reason": reason,
        "revoker": revoker,
    }
    entry = {
        "timestamp": payload["timestamp"],
        "issuer": revoker,
        "role": "revocation",
        "payload": payload,
    }
    return get_ledger("revocations").append(entry)


def is_key_revoked(key_id: str) -> bool:
    ledger = get_ledger("revocations")
    for entry in ledger.entries():
        payload = entry.raw.get("payload", {})
        if payload.get("event") == "key_revoked" and payload.get("revoked_key_id") == key_id:
            return True
    return False


def verify_artifact(path: Path, signature_path: Optional[Path] = None) -> Dict[str, str]:
    ensure_structure()
    if signature_path is None:
        signature_path = SIGNATURES_ROOT / f"{path.name}.sig.json"
    if not signature_path.exists():
        raise FileNotFoundError(f"Signature file {signature_path} not found")
    with signature_path.open("r", encoding="utf-8") as fh:
        signed = json.load(fh)
    payload = signed["payload"]
    signature = signed["signature"]
    public_key = signed["public_key"]
    expected_sha = compute_file_sha256(path)
    if payload["artifact"]["sha256"] != expected_sha:
        raise ValueError("Artifact digest mismatch")
    key_id = payload.get("key_id")
    if is_key_revoked(key_id):
        raise ValueError(f"Key {key_id} has been revoked")
    if not verify_signature(public_key, payload, signature):
        raise ValueError("Signature verification failed")
    if not check_ledger_membership(payload, signature):
        raise ValueError("Signature not present in append-only ledger")
    return {
        "status": "verified",
        "key_id": key_id,
        "key_type": payload.get("key_type"),
        "timestamp": payload.get("timestamp"),
        "context": payload["artifact"].get("context"),
    }


def check_ledger_membership(payload: dict, signature: str) -> bool:
    ledger = get_ledger("artifacts")
    for entry in ledger.entries():
        if entry.raw.get("signature") == signature and entry.raw.get("payload") == payload:
            return True
    return False

FILE: blux_reg/tokens.py
Kind: text
Size: 6090
Last modified: 2026-01-20T06:55:50Z

CONTENT:
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from .crypto import now_iso, sign_payload, verify_signature
from .keystore import KeyStore
from .ledger import canonical_bytes, sha256_hex, get_ledger
from .paths import TOKENS_ROOT
from .registry import ensure_structure, is_key_revoked

TOKEN_SCHEMA_VERSION = "1.0"
TOKEN_TYPE = "capability"

REQUIRED_FIELDS = {
    "schema_version",
    "token_type",
    "issued_at",
    "expires_at",
    "ttl_seconds",
    "capability",
    "audience_repo",
    "constraints",
    "issuer",
    "signature",
}


def _parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def token_ref(token: Dict[str, Any]) -> str:
    return sha256_hex(canonical_bytes(token))


def _payload_from_token(token: Dict[str, Any]) -> Dict[str, Any]:
    return {k: token[k] for k in token if k != "signature"}


def _token_path_for(hash_ref: str) -> Path:
    return TOKENS_ROOT / f"{hash_ref}.token.json"


def issue_capability_token(
    key_id: str,
    key_type: str,
    passphrase: str,
    capability: str,
    audience_repo: str,
    ttl_seconds: int,
    constraints: Optional[Dict[str, Any]] = None,
    keystore: Optional[KeyStore] = None,
    output_path: Optional[Path] = None,
) -> tuple[Dict[str, Any], str, Path]:
    if ttl_seconds <= 0:
        raise ValueError("ttl_seconds must be positive")
    ensure_structure()
    TOKENS_ROOT.mkdir(parents=True, exist_ok=True)
    ks = keystore or KeyStore()
    material = ks.load(key_id, key_type)
    issued_at_dt = datetime.now(timezone.utc).replace(microsecond=0)
    expires_at_dt = issued_at_dt + timedelta(seconds=ttl_seconds)
    payload = {
        "schema_version": TOKEN_SCHEMA_VERSION,
        "token_type": TOKEN_TYPE,
        "issued_at": issued_at_dt.isoformat(),
        "expires_at": expires_at_dt.isoformat(),
        "ttl_seconds": ttl_seconds,
        "capability": capability,
        "audience_repo": audience_repo,
        "constraints": constraints or {},
        "issuer": {
            "key_id": material.key_id,
            "key_type": material.key_type,
            "public_key": material.public_key,
            "compatibility": material.compatibility,
        },
    }
    signature = sign_payload(material, payload, passphrase)
    token = dict(payload)
    token["signature"] = signature
    hash_ref = token_ref(token)
    entry = {
        "timestamp": payload["issued_at"],
        "issuer": material.key_id,
        "role": material.key_type,
        "token_hash": hash_ref,
        "payload": payload,
        "signature": signature,
    }
    get_ledger("tokens").append(entry)
    path = output_path or _token_path_for(hash_ref)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(token, fh, indent=2, sort_keys=True)
    return token, hash_ref, path


def load_token(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def is_token_revoked(token_hash: str) -> bool:
    ledger = get_ledger("revocations")
    for entry in ledger.entries():
        payload = entry.raw.get("payload", {})
        if payload.get("event") == "token_revoked" and payload.get("token_hash") == token_hash:
            return True
    return False


def revoke_capability_token(token_hash: str, reason: str, revoker: str):
    ensure_structure()
    payload = {
        "event": "token_revoked",
        "timestamp": now_iso(),
        "token_hash": token_hash,
        "reason": reason,
        "revoker": revoker,
    }
    entry = {
        "timestamp": payload["timestamp"],
        "issuer": revoker,
        "role": "revocation",
        "payload": payload,
    }
    return get_ledger("revocations").append(entry)


def check_token_ledger_membership(token_hash: str, payload: Dict[str, Any], signature: str) -> bool:
    ledger = get_ledger("tokens")
    for entry in ledger.entries():
        if entry.raw.get("token_hash") == token_hash:
            if entry.raw.get("payload") == payload and entry.raw.get("signature") == signature:
                return True
    return False


def verify_capability_token(
    token: Dict[str, Any],
    now: Optional[datetime] = None,
    require_ledger: bool = True,
) -> Dict[str, str]:
    missing = REQUIRED_FIELDS - token.keys()
    if missing:
        raise ValueError(f"Token missing fields: {sorted(missing)}")
    if token.get("token_type") != TOKEN_TYPE:
        raise ValueError("Token type mismatch")
    if token.get("schema_version") != TOKEN_SCHEMA_VERSION:
        raise ValueError("Unsupported token schema version")
    payload = _payload_from_token(token)
    signature = token["signature"]
    issuer = payload.get("issuer", {})
    public_key = issuer.get("public_key")
    if not public_key:
        raise ValueError("Token missing issuer public key")
    if not verify_signature(public_key, payload, signature):
        raise ValueError("Token signature verification failed")
    if is_key_revoked(issuer.get("key_id")):
        raise ValueError(f"Key {issuer.get('key_id')} has been revoked")
    now_dt = now or datetime.now(timezone.utc).replace(microsecond=0)
    expires_at = _parse_iso(payload["expires_at"])
    if expires_at < now_dt:
        raise ValueError("Token has expired")
    token_hash = token_ref(token)
    if is_token_revoked(token_hash):
        raise ValueError("Token has been revoked")
    if require_ledger and not check_token_ledger_membership(token_hash, payload, signature):
        raise ValueError("Token not present in append-only ledger")
    return {
        "status": "verified",
        "token_hash": token_hash,
        "capability": payload.get("capability"),
        "audience_repo": payload.get("audience_repo"),
        "expires_at": payload.get("expires_at"),
    }


def show_token(path: Path) -> Dict[str, Any]:
    token = load_token(path)
    return {
        "token": token,
        "token_hash": token_ref(token),
    }

FILE: docs/CONTRACT.md
Kind: text
Size: 4764
Last modified: 2026-01-20T06:55:50Z

CONTENT:
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

## Capability token schema (`schema_version: 1.0`)
```json
{
  "schema_version": "1.0",
  "token_type": "capability",
  "issued_at": "2025-01-01T00:00:00+00:00",
  "expires_at": "2025-01-02T00:00:00+00:00",
  "ttl_seconds": 86400,
  "capability": "publish",
  "audience_repo": "Outer-Void/blux-guard",
  "constraints": {
    "scope": "release"
  },
  "issuer": {
    "key_id": "project-alpha",
    "key_type": "project",
    "public_key": "<base64 ed25519 public key>",
    "compatibility": {
      "BLUX-Quantum": ">=1.0",
      "BLUX-Guard": ">=1.0"
    }
  },
  "signature": "<base64 ed25519 signature over canonical token payload>"
}
```
- Canonicalization: JSON serialized with sorted keys and `",":"` separators.
- Signature input: canonical JSON of all token fields **excluding** `signature`.
- Token hash (`capability_token_ref`): SHA-256 of canonical JSON including the signature.
- Tokens are offline-verifiable, scoped, and time-bound. Secrets must not be embedded in tokens.

### Token ledger entry (append-only)
```json
{
  "timestamp": "2025-01-01T00:00:00+00:00",
  "issuer": "project-alpha",
  "role": "project",
  "token_hash": "<sha256 canonical token JSON>",
  "payload": "<token payload without signature>",
  "signature": "<base64 signature over payload>"
}
```

### Token revocation entry (append-only)
```json
{
  "timestamp": "2025-01-01T00:00:00+00:00",
  "issuer": "security-team",
  "role": "revocation",
  "payload": {
    "event": "token_revoked",
    "timestamp": "2025-01-01T00:00:00+00:00",
    "token_hash": "<sha256 canonical token JSON>",
    "reason": "compromised",
    "revoker": "security-team"
  }
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

## Envelope reference
Artifacts that require delegated capabilities should reference tokens by hash:

```json
{
  "capability_token_ref": "<sha256 hash of canonical token JSON>"
}
```

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
- `blux-reg token issue <key_id> <key_type> <capability> <audience_repo> <ttl_seconds> [--constraints JSON]`
- `blux-reg token verify <token_path>`
- `blux-reg token revoke <token_hash> [--reason REASON] --revoker ID`
- `blux-reg token show <token_path>`

Exit codes are stable: `0` success, `1` on verification/chain failures.

FILE: docs/roles.md
Kind: text
Size: 1304
Last modified: 2026-01-20T13:55:06Z

CONTENT:
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

FILE: plan.md
Kind: text
Size: 964
Last modified: 2026-01-20T13:55:06Z

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
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T06:55:50Z

CONTENT:
-r requirements.txt
pytest

FILE: requirements.txt
Kind: text
Size: 55
Last modified: 2026-01-20T06:55:50Z

CONTENT:
cryptography>=42.0.0
argon2-cffi>=23.1.0
pynacl>=1.5.0

FILE: schemas/capability_manifest.schema.json
Kind: text
Size: 502
Last modified: 2026-01-20T13:55:06Z

CONTENT:
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Capability Manifest",
  "type": "object",
  "required": [
    "schema_version",
    "generated_at",
    "tokens"
  ],
  "properties": {
    "schema_version": {
      "type": "string"
    },
    "generated_at": {
      "type": "string",
      "format": "date-time"
    },
    "tokens": {
      "type": "array",
      "items": {
        "$ref": "capability_token.schema.json"
      }
    }
  },
  "additionalProperties": false
}

FILE: schemas/capability_token.schema.json
Kind: text
Size: 1295
Last modified: 2026-01-20T13:55:06Z

CONTENT:
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Capability Token",
  "type": "object",
  "required": [
    "schema_version",
    "token_type",
    "issued_at",
    "expires_at",
    "ttl_seconds",
    "capability",
    "audience",
    "constraints",
    "issuer",
    "signature"
  ],
  "properties": {
    "schema_version": {
      "type": "string"
    },
    "token_type": {
      "const": "capability"
    },
    "issued_at": {
      "type": "string",
      "format": "date-time"
    },
    "expires_at": {
      "type": "string",
      "format": "date-time"
    },
    "ttl_seconds": {
      "type": "integer",
      "minimum": 1
    },
    "capability": {
      "type": "string"
    },
    "audience": {
      "type": "string"
    },
    "constraints": {
      "type": "object"
    },
    "issuer": {
      "type": "object",
      "required": [
        "key_name",
        "fingerprint",
        "public_key"
      ],
      "properties": {
        "key_name": {
          "type": "string"
        },
        "fingerprint": {
          "type": "string"
        },
        "public_key": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "signature": {
      "type": "string"
    }
  },
  "additionalProperties": false
}

FILE: schemas/revocation.schema.json
Kind: text
Size: 599
Last modified: 2026-01-20T13:55:06Z

CONTENT:
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Capability Token Revocation",
  "type": "object",
  "required": [
    "schema_version",
    "token_hash",
    "revoked_at",
    "reason",
    "revoker"
  ],
  "properties": {
    "schema_version": {
      "type": "string"
    },
    "token_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "revoked_at": {
      "type": "string",
      "format": "date-time"
    },
    "reason": {
      "type": "string"
    },
    "revoker": {
      "type": "string"
    }
  },
  "additionalProperties": false
}

FILE: scripts/demo_unified_reg.sh
Kind: text
Size: 774
Last modified: 2026-01-20T06:55:50Z

CONTENT:
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

CONFIG_DIR=${BLUX_REG_CONFIG_DIR:-"$HOME/.config/blux-reg"}
export BLUX_REG_CONFIG_DIR="$CONFIG_DIR"

bin_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

command -v blux-reg >/dev/null 2>&1 || {
  echo "blux-reg entrypoint not installed; try 'pip install -e .' first" >&2
  exit 1
}

echo "[1/6] init"
blux-reg init

echo "[2/6] keygen"
blux-reg keygen --name demo --force

sample="$CONFIG_DIR/sample.txt"
echo "demo artifact" > "$sample"

echo "[3/6] sign"
man_out="$sample.blux-manifest.json"
blux-reg sign "$sample" --key-name demo --output "$man_out"

echo "[4/6] verify"
blux-reg verify "$man_out"

echo "[5/6] audit tail"
blux-reg audit tail -n 5

echo "[6/6] audit verify-chain"
blux-reg audit verify-chain


FILE: scripts/physics_check.sh
Kind: text
Size: 799
Last modified: 2026-01-20T13:55:06Z

CONTENT:
#!/usr/bin/env bash
set -euo pipefail

forbidden_pattern='safety policy|\b(ethic|morality|discern|posture|illusion|therapy|harm)\b'
if rg -n -i --hidden --glob '!.git/*' "$forbidden_pattern" .; then
  echo "Physics check failed: forbidden policy/discernment tokens detected."
  exit 1
fi

phase0_paths=(
  "contracts/envelope.schema.json"
  "contracts/request.schema.json"
  "contracts/discernment_report.schema.json"
  "contracts/guard_receipt.schema.json"
  "schemas/envelope.schema.json"
  "schemas/request.schema.json"
  "schemas/discernment_report.schema.json"
  "schemas/guard_receipt.schema.json"
)

for path in "${phase0_paths[@]}"; do
  if [[ -e "$path" ]]; then
    echo "Physics check failed: Phase 0 contract schema detected at $path."
    exit 1
  fi
done

echo "Physics check passed."

FILE: src/blux_reg/__init__.py
Kind: text
Size: 88
Last modified: 2026-01-20T13:55:06Z

CONTENT:
"""blux-reg package."""

__all__ = ["config", "crypto", "ledger", "manifest", "tokens"]

FILE: src/blux_reg/cli.py
Kind: text
Size: 7294
Last modified: 2026-01-20T13:55:06Z

CONTENT:
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import click

from . import config, crypto, ledger, manifest, tokens
from .util import canonical_json


@click.group()
def app():
    """blux-reg: local-first signing + audit CLI."""
    config.refresh_paths()


@app.command()
def init():
    """Initialize config directories."""
    config.ensure_directories()
    click.echo(f"config_dir: {config.CONFIG_ROOT}")
    click.echo(f"keys_dir:   {config.KEYS_DIR}")
    click.echo(f"ledger:     {config.LEDGER_PATH}")


@app.command()
@click.option("--json-output", is_flag=True, help="Return status as JSON")
def status(json_output: bool = False):
    """Show registry status."""
    config.ensure_directories()
    keys = crypto.list_keys()
    info = {
        "config_root": str(config.CONFIG_ROOT),
        "keys": [k.as_dict() for k in keys],
        "ledger_entries": ledger.ledger_size(),
        "ledger_last_hash": ledger.last_hash(),
    }
    if json_output:
        click.echo(json.dumps(info, indent=2))
    else:
        click.echo(f"config: {info['config_root']}")
        click.echo(f"keys: {len(keys)} available")
        click.echo(f"ledger entries: {info['ledger_entries']}")
        click.echo(f"last hash: {info['ledger_last_hash']}")


@app.group()
def key():
    """Key management commands."""


def _run_keygen(name: str, force: bool):
    config.ensure_directories()
    info = crypto.generate_keypair(name=name, force=force)
    ledger.append_entry(
        action="keygen",
        actor=info.fingerprint,
        payload_summary=f"key:{name}",
    )
    click.echo(f"generated {name} ({info.fingerprint})")


@key.command()
@click.option("--name", default="default", help="Key name")
@click.option("--force", is_flag=True, help="Overwrite existing key")
def keygen(name: str, force: bool):
    _run_keygen(name, force)


@app.command(name="keygen")
@click.option("--name", default="default", help="Key name")
@click.option("--force", is_flag=True, help="Overwrite existing key")
def keygen_root(name: str, force: bool):
    _run_keygen(name, force)


@key.command(name="list")
def key_list():
    keys = crypto.list_keys()
    if not keys:
        click.echo("no keys found")
        return
    for info in keys:
        click.echo(f"{info.name}\t{info.fingerprint}\t{info.public_path}")


@key.command()
@click.option("--name", default="default", help="Key name")
@click.option("--public/--private", default=True, help="Export public or private key")
@click.option("--output", type=click.Path(), help="Output path (defaults to stdout)")
def export(name: str, public: bool, output: Optional[str]):
    data = crypto.export_key(name, public=public)
    if output:
        Path(output).write_bytes(data)
    else:
        click.echo(data.decode())


@key.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--name", default="imported", help="Name to store key under")
def import_key(path: str, name: str):
    info = crypto.import_private_key(Path(path), name)
    ledger.append_entry(
        action="key-import",
        actor=info.fingerprint,
        payload_summary=f"key:{name}",
    )
    click.echo(f"imported {name} ({info.fingerprint})")


@app.command()
@click.argument("artifact", type=click.Path(exists=True))
@click.option("--key-name", default="default", help="Key to use")
@click.option("--output", type=click.Path(), help="Manifest output path")
def sign(artifact: str, key_name: str, output: Optional[str]):
    manifest_path, data = manifest.sign_artifact(Path(artifact), key_name, Path(output) if output else None)
    click.echo(f"manifest: {manifest_path}")
    click.echo(f"fingerprint: {data['key_fingerprint']}")


@app.command(name="verify-manifest")
@click.argument("manifest_path", type=click.Path(exists=True))
def verify_manifest(manifest_path: str):
    ok = manifest.verify_manifest(Path(manifest_path))
    if ok:
        click.echo("verified")
        raise SystemExit(0)
    click.echo("verification failed", err=True)
    raise SystemExit(1)


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
@click.option("--revoker", required=True, help="Identifier for the revocation")
def revoke(token_hash: str, reason: str, revoker: str):
    """Revoke a capability token offline."""
    entry = tokens.revoke_capability_token(token_hash, reason, revoker)
    click.echo(json.dumps(entry, indent=2, sort_keys=True))


@app.group()
def audit():
    """Audit ledger commands."""


@audit.command("add-event")
@click.argument("message")
@click.option("--actor", help="Fingerprint or actor id", default="anonymous")
def add_event(message: str, actor: str):
    ledger.append_entry(action="event", actor=actor, payload_summary=message)
    click.echo("event logged")


@audit.command("tail")
@click.option("-n", "--lines", default=10, help="Number of entries to show")
@click.option("--json-output", is_flag=True, help="Output JSON")
def audit_tail(lines: int, json_output: bool):
    entries = ledger.tail_entries(lines)
    if json_output:
        click.echo(json.dumps(entries, indent=2))
        return
    for entry in entries:
        click.echo(canonical_json(entry))


@audit.command("verify-chain")
def audit_verify_chain():
    ok = ledger.verify_chain()
    if ok:
        click.echo("ledger ok")
        raise SystemExit(0)
    click.echo("ledger tampered", err=True)
    raise SystemExit(1)


if __name__ == "__main__":
    app()

FILE: src/blux_reg/config.py
Kind: text
Size: 1745
Last modified: 2026-01-20T13:55:06Z

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


def refresh_paths() -> None:
    """Refresh module-level paths from the current environment.

    Useful for tests that temporarily override ``BLUX_REG_CONFIG_DIR``.
    """
    global CONFIG_ROOT, KEYS_DIR, MANIFEST_DIR, TRUST_DIR, LEDGER_PATH, CACHE_DIR, TOKENS_DIR, REVOCATIONS_PATH
    CONFIG_ROOT = _resolve_root()
    KEYS_DIR = CONFIG_ROOT / "keys"
    MANIFEST_DIR = CONFIG_ROOT / "manifests"
    TRUST_DIR = CONFIG_ROOT / "trust"
    LEDGER_PATH = TRUST_DIR / "ledger.jsonl"
    CACHE_DIR = CONFIG_ROOT / "cache"
    TOKENS_DIR = TRUST_DIR / "tokens"
    REVOCATIONS_PATH = TRUST_DIR / "token_revocations.jsonl"


def ensure_directories() -> None:
    """Create required directories if they do not exist."""
    for path in (CONFIG_ROOT, KEYS_DIR, MANIFEST_DIR, TRUST_DIR, CACHE_DIR, TOKENS_DIR):
        path.mkdir(parents=True, exist_ok=True)

FILE: src/blux_reg/crypto.py
Kind: text
Size: 4920
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T06:55:50Z

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
Size: 5748
Last modified: 2026-01-20T13:55:06Z

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


def verify_capability_token(token: Dict[str, Any], now: Optional[datetime] = None) -> Dict[str, str]:
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
    now_dt = now or datetime.now(timezone.utc).replace(microsecond=0)
    expires_at = _parse_iso(payload["expires_at"])
    if expires_at < now_dt:
        raise ValueError("Token has expired")
    token_hash = token_ref(token)
    if is_token_revoked(token_hash):
        raise ValueError("Token has been revoked")
    return {
        "status": "verified",
        "token_hash": token_hash,
        "capability": payload.get("capability"),
        "audience": payload.get("audience"),
        "expires_at": payload.get("expires_at"),
    }

FILE: src/blux_reg/util.py
Kind: text
Size: 784
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T13:55:06Z

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
Size: 2062
Last modified: 2026-01-20T13:55:06Z

CONTENT:
import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Boundary: prohibited keywords/paths that imply policy/ethics/discernment logic.
# This list is intentionally small and explicit to avoid false positives.
PROHIBITED_CONTENT_PATTERNS = [
    re.compile(r"\bpolicy[-_ ]engine\b", re.IGNORECASE),
    re.compile(r"\bpolicy[-_ ]as[-_ ]code\b", re.IGNORECASE),
    re.compile(r"\bposture[-_ ]scoring\b", re.IGNORECASE),
    re.compile(r"\bdiscernment\b", re.IGNORECASE),
    re.compile(r"\bethic(s|al)?\b", re.IGNORECASE),
    re.compile(r"\bmoral(ity)?\b", re.IGNORECASE),
]

PROHIBITED_PATH_PATTERNS = [
    re.compile(r"policy[-_ ]engine", re.IGNORECASE),
    re.compile(r"policy[-_ ]as[-_ ]code", re.IGNORECASE),
    re.compile(r"posture[-_ ]scoring", re.IGNORECASE),
    re.compile(r"discernment", re.IGNORECASE),
    re.compile(r"ethic", re.IGNORECASE),
    re.compile(r"moral", re.IGNORECASE),
]

ALLOWLIST = {
    "tests/test_boundary_ci.py",
    "scripts/physics_check.sh",
}


def _tracked_files():
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=REPO_ROOT)
    for entry in output.decode("utf-8").split("\x00"):
        if entry:
            yield entry


def test_boundary_no_policy_discernment_logic():
    violations = []

    for rel_path in _tracked_files():
        if rel_path in ALLOWLIST:
            continue
        for pattern in PROHIBITED_PATH_PATTERNS:
            if pattern.search(rel_path):
                violations.append(f"path:{rel_path}:{pattern.pattern}")
                break
        else:
            path = REPO_ROOT / rel_path
            if not path.is_file():
                continue
            content = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in PROHIBITED_CONTENT_PATTERNS:
                if pattern.search(content):
                    violations.append(f"content:{rel_path}:{pattern.pattern}")
                    break

    assert not violations, "Boundary violation(s) detected:\n" + "\n".join(violations)

FILE: tests/test_crypto.py
Kind: text
Size: 479
Last modified: 2026-01-20T13:55:06Z

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
Last modified: 2026-01-20T06:55:50Z

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
Last modified: 2026-01-20T13:55:06Z

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
Size: 2346
Last modified: 2026-01-20T13:55:06Z

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
        "outer-void/blux-guard",
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
        "outer-void/blux-guard",
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
        "outer-void/blux-guard",
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
        "outer-void/blux-guard",
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
        "outer-void/blux-guard",
        3600,
        {},
    )
    assert tokens.hash_token_file(path) == token_hash
    now = datetime.now(timezone.utc).replace(microsecond=0)
    assert tokens.verify_capability_token(token, now=now)["status"] == "verified"

## 4) Workflow Inventory (index only)
- .github/workflows/ci.yml: pull_request, push

## 5) Search Index (raw results)
subprocess:
tests/test_boundary_ci.py

os.system:
none

exec(:
none

spawn:
none

shell:
none

child_process:
none

policy:
README.md
ROLE.md
scripts/physics_check.sh
tests/test_boundary_ci.py

ethic:
scripts/physics_check.sh
tests/test_boundary_ci.py

enforce:
plan.md

guard:
README.md
docs/CONTRACT.md
plan.md
scripts/physics_check.sh
tests/test_tokens.py

receipt:
scripts/physics_check.sh

token:
README.md
ROLE.md
blux_reg/__init__.py
blux_reg/cli.py
blux_reg/paths.py
blux_reg/tokens.py
docs/CONTRACT.md
docs/roles.md
schemas/capability_manifest.schema.json
schemas/capability_token.schema.json
schemas/revocation.schema.json
scripts/physics_check.sh
src/blux_reg/__init__.py
src/blux_reg/cli.py
src/blux_reg/config.py
src/blux_reg/tokens.py
tests/test_tokens.py

signature:
README.md
blux_reg/cli.py
blux_reg/crypto.py
blux_reg/paths.py
blux_reg/registry.py
blux_reg/tokens.py
docs/CONTRACT.md
docs/roles.md
plan.md
schemas/capability_token.schema.json
src/blux_reg/crypto.py
src/blux_reg/manifest.py
src/blux_reg/tokens.py
tests/test_crypto.py
tests/test_tokens.py

verify:
README.md
blux_reg/__init__.py
blux_reg/cli.py
blux_reg/crypto.py
blux_reg/ledger.py
blux_reg/registry.py
blux_reg/tokens.py
docs/CONTRACT.md
scripts/demo_unified_reg.sh
src/blux_reg/cli.py
src/blux_reg/crypto.py
src/blux_reg/ledger.py
src/blux_reg/manifest.py
src/blux_reg/tokens.py
tests/test_crypto.py
tests/test_flow.py
tests/test_ledger.py
tests/test_tokens.py

capability:
README.md
ROLE.md
blux_reg/__init__.py
blux_reg/cli.py
blux_reg/tokens.py
docs/CONTRACT.md
docs/roles.md
schemas/capability_manifest.schema.json
schemas/capability_token.schema.json
src/blux_reg/cli.py
src/blux_reg/tokens.py
tests/test_tokens.py

key_id:
README.md
blux_reg/cli.py
blux_reg/crypto.py
blux_reg/keystore.py
blux_reg/registry.py
blux_reg/tokens.py
docs/CONTRACT.md

contract:
LICENSE-APACHE
docs/CONTRACT.md
docs/roles.md
plan.md
scripts/physics_check.sh

schema:
blux_reg/tokens.py
docs/CONTRACT.md
schemas/capability_manifest.schema.json
schemas/capability_token.schema.json
schemas/revocation.schema.json
scripts/physics_check.sh
src/blux_reg/manifest.py
src/blux_reg/tokens.py

$schema:
schemas/capability_manifest.schema.json
schemas/capability_token.schema.json
schemas/revocation.schema.json

json-schema:
schemas/capability_manifest.schema.json
schemas/capability_token.schema.json
schemas/revocation.schema.json

router:
none

orchestr:
README.md

execute:
LICENSE-APACHE
docs/roles.md

command:
scripts/demo_unified_reg.sh
src/blux_reg/cli.py

## 6) Notes
none
