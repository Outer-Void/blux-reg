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
    parser.print_help()
    return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
