import argparse
import json
from pathlib import Path
from typing import Any

from .crypto import (
    CryptoError,
    DEFAULT_PRIVATE,
    DEFAULT_PUBLIC,
    generate_ed25519_keypair,
    sign_bytes,
    sign_file,
    verify_file,
)
from .doctor import run_doctor
from .ledger import append_entry, tail_entries, verify_chain
from .paths import APP_NAME, ensure_directories, get_artifacts_dir, get_keys_dir, get_ledger_path


class CLIError(Exception):
    pass


def _print(msg: str) -> None:
    print(msg)


def command_keygen(args: argparse.Namespace) -> None:
    ensure_directories()
    key_dir = get_keys_dir()
    try:
        paths = generate_ed25519_keypair(key_dir)
        _print(f"[+] Generated ed25519 keypair at {paths.private_key} and {paths.public_key}")
    except CryptoError as exc:
        _print(f"[!] {exc}")
        raise SystemExit(1)


def command_sign(args: argparse.Namespace) -> None:
    ensure_directories()
    key_dir = get_keys_dir()
    private_path = key_dir / DEFAULT_PRIVATE
    if not private_path.exists():
        _print("Private key missing. Run 'blux-reg keygen' first.")
        raise SystemExit(1)
    target = Path(args.file)
    if not target.exists():
        _print(f"File not found: {target}")
        raise SystemExit(1)
    signature, sig_path = sign_file(target, private_path)
    append_entry(
        entry_type="sign",
        payload={"file": str(target)},
        signature=signature.hex(),
        public_key_path=key_dir / DEFAULT_PUBLIC,
    )
    _print(f"[+] Signed {target} -> {sig_path}")


def command_verify(args: argparse.Namespace) -> None:
    key_dir = get_keys_dir()
    public_path = key_dir / DEFAULT_PUBLIC
    if not public_path.exists():
        _print("Public key missing. Run 'blux-reg keygen' first.")
        raise SystemExit(1)
    file_path = Path(args.file)
    sig_path = Path(args.signature)
    if not file_path.exists() or not sig_path.exists():
        _print("File or signature not found.")
        raise SystemExit(1)
    ok = verify_file(file_path, sig_path, public_path)
    _print("VERIFY -> OK" if ok else "VERIFY -> FAIL")
    if not ok:
        raise SystemExit(1)


def command_audit_add(args: argparse.Namespace) -> None:
    ensure_directories()
    key_dir = get_keys_dir()
    private_path = key_dir / DEFAULT_PRIVATE
    public_path = key_dir / DEFAULT_PUBLIC
    if not private_path.exists() or not public_path.exists():
        _print("Keys missing. Run 'blux-reg keygen' first.")
        raise SystemExit(1)
    try:
        payload = json.loads(args.payload)
    except json.JSONDecodeError as exc:
        _print(f"Invalid JSON payload: {exc}")
        raise SystemExit(1)
    payload_bytes = json.dumps(payload, sort_keys=True).encode()
    signature = sign_bytes(payload_bytes, private_path)
    append_entry("event", payload, signature.hex(), public_path)
    _print("[+] Audit event appended")


def command_audit_tail(args: argparse.Namespace) -> None:
    entries = tail_entries(limit=args.limit)
    for entry in entries:
        _print(json.dumps(entry.to_dict(), indent=2))


def command_audit_verify(args: argparse.Namespace) -> None:
    ok = verify_chain()
    _print("LEDGER OK" if ok else "LEDGER CORRUPTED")
    if not ok:
        raise SystemExit(1)


def command_doctor(args: argparse.Namespace) -> None:
    ok, messages = run_doctor()
    if ok:
        _print("doctor: all checks passed")
    else:
        _print("doctor: issues detected")
        for msg in messages:
            _print(f" - {msg}")
        raise SystemExit(1)


def _write_artifact(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    _print(f"[artifact] {path}")


def command_demo(args: argparse.Namespace) -> None:
    ensure_directories()
    key_dir = get_keys_dir()
    try:
        if not (key_dir / DEFAULT_PRIVATE).exists():
            generate_ed25519_keypair(key_dir)
            _print("[demo] generated keys")
    except CryptoError as exc:
        _print(f"[demo] key generation failed: {exc}")
        raise SystemExit(1)

    artifacts_dir = get_artifacts_dir()
    manifest_path = artifacts_dir / "demo_manifest.json"
    patch_path = artifacts_dir / "demo_patch.diff"

    manifest = {
        "component": "demo",
        "version": "1.0.0",
        "description": "Unified Demo manifest",
    }
    _write_artifact(manifest_path, json.dumps(manifest, indent=2))
    _write_artifact(patch_path, "--- a/demo.txt\n+++ b/demo.txt\n@@\n-hello\n+hello world\n")

    private_path = key_dir / DEFAULT_PRIVATE
    public_path = key_dir / DEFAULT_PUBLIC

    manifest_sig, manifest_sig_path = sign_file(manifest_path, private_path)
    patch_sig, patch_sig_path = sign_file(patch_path, private_path)

    append_entry("sign-manifest", {"file": str(manifest_path)}, manifest_sig.hex(), public_path)
    append_entry("sign-patch", {"file": str(patch_path)}, patch_sig.hex(), public_path)

    manifest_ok = verify_file(manifest_path, manifest_sig_path, public_path)
    patch_ok = verify_file(patch_path, patch_sig_path, public_path)

    chain_ok = verify_chain()

    _print("[demo] manifest verify: " + ("OK" if manifest_ok else "FAIL"))
    _print("[demo] patch verify: " + ("OK" if patch_ok else "FAIL"))
    _print("[demo] ledger chain: " + ("OK" if chain_ok else "FAIL"))

    if not (manifest_ok and patch_ok and chain_ok):
        _print("[demo] FAILED")
        raise SystemExit(1)

    _print("DEMO PASS")
    _print(f"Artifacts at {artifacts_dir}")
    _print(f"Ledger at {get_ledger_path()}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="blux-reg", description=f"{APP_NAME} CLI")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("keygen", help="Generate ed25519 keys")

    sign_p = sub.add_parser("sign", help="Sign a file")
    sign_p.add_argument("file")

    verify_p = sub.add_parser("verify", help="Verify a signature")
    verify_p.add_argument("file")
    verify_p.add_argument("signature")

    sub.add_parser("demo", help="Run the unified demo")

    sub.add_parser("doctor", help="Run system checks")

    audit = sub.add_parser("audit", help="Ledger operations")
    audit_sub = audit.add_subparsers(dest="audit_cmd")

    add_event = audit_sub.add_parser("add-event", help="Append an audit event")
    add_event.add_argument("payload", help="JSON payload string")

    tail = audit_sub.add_parser("tail", help="Tail audit log")
    tail.add_argument("--limit", type=int, default=10)

    audit_sub.add_parser("verify-chain", help="Verify ledger integrity")

    return parser


def main(argv: Any = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "keygen":
        command_keygen(args)
    elif args.command == "sign":
        command_sign(args)
    elif args.command == "verify":
        command_verify(args)
    elif args.command == "demo":
        command_demo(args)
    elif args.command == "doctor":
        command_doctor(args)
    elif args.command == "audit":
        if args.audit_cmd == "add-event":
            command_audit_add(args)
        elif args.audit_cmd == "tail":
            command_audit_tail(args)
        elif args.audit_cmd == "verify-chain":
            command_audit_verify(args)
        else:
            parser.print_help()
            raise SystemExit(1)
    else:
        parser.print_help()
        raise SystemExit(1)


if __name__ == "__main__":
    main()
