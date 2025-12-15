import os
import subprocess
from pathlib import Path

from blux_reg import paths


def test_demo_runs(tmp_path, monkeypatch):
    monkeypatch.setenv("BLUX_CONFIG_HOME", str(tmp_path))
    env = os.environ.copy()
    env["BLUX_CONFIG_HOME"] = str(tmp_path)
    result = subprocess.run(["python", "bin/blux-reg", "demo"], env=env, capture_output=True)
    assert result.returncode == 0, result.stderr.decode()
    artifacts_dir = paths.get_artifacts_dir()
    assert (artifacts_dir / "demo_manifest.json").exists()
    assert (artifacts_dir / "demo_patch.diff").exists()
    assert paths.get_ledger_path().exists()
