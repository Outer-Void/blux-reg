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
