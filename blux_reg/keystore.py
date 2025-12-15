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
