from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import click

from . import config, crypto, ledger, manifest
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


@app.command()
@click.argument("manifest_path", type=click.Path(exists=True))
def verify(manifest_path: str):
    ok = manifest.verify_manifest(Path(manifest_path))
    if ok:
        click.echo("verified")
        raise SystemExit(0)
    click.echo("verification failed", err=True)
    raise SystemExit(1)


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
