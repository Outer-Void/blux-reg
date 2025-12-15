import os
from pathlib import Path


APP_NAME = "blux-reg"
CONFIG_ENV = "BLUX_CONFIG_HOME"
DEFAULT_CONFIG_ROOT = Path(os.environ.get(CONFIG_ENV) or Path.home() / ".config" / APP_NAME)


def get_config_root() -> Path:
    return Path(os.environ.get(CONFIG_ENV) or DEFAULT_CONFIG_ROOT)


def get_keys_dir() -> Path:
    return get_config_root() / "keys"


def get_ledger_path() -> Path:
    return get_config_root() / "trust" / "ledger.jsonl"


def get_artifacts_dir() -> Path:
    return get_config_root() / "artifacts"


def ensure_directories() -> None:
    keys = get_keys_dir()
    ledger_path = get_ledger_path()
    artifacts = get_artifacts_dir()

    keys.mkdir(parents=True, exist_ok=True)
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    artifacts.mkdir(parents=True, exist_ok=True)


__all__ = [
    "APP_NAME",
    "CONFIG_ENV",
    "get_config_root",
    "get_keys_dir",
    "get_ledger_path",
    "get_artifacts_dir",
    "ensure_directories",
]
