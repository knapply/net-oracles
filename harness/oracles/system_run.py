"""Shared helper for the system-tool oracle scripts (JGraphT, Boost, nauty,
Octave): bootstrap the private tool prefix and run a driver.

Each oracle script declares its inputs in an `ORACLE_INPUTS` constant (paths
relative to the repository root) so an incremental runner can hash them, and
writes the tool version with write_version(), which is itself part of the
golden directory; goldens are committed and regenerated only when an input
or the tool version changes.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV = Path(os.environ.get("ORACLE_ENV", Path.home() / ".cache" / "oracle-env"))


def tool_path() -> str:
    """PATH with the private prefix first, bootstrapping it if requested
    (ORACLE_BOOTSTRAP=1) and missing."""
    if os.environ.get("ORACLE_BOOTSTRAP") == "1" and not (ENV / "conda-meta").exists():
        subprocess.run(["bash", "-c", f"source {ROOT}/tools/oracle_env.sh"], check=True)
    return f"{ENV}/bin:{os.environ['PATH']}"


def which(name: str) -> str | None:
    return shutil.which(name, path=tool_path())


def skip(reason: str) -> None:
    print(f"   skipped: {reason} (committed goldens are kept)")
    sys.exit(3)   # run_oracles.py: skipped, nothing recorded


def run(cmd, **kw) -> subprocess.CompletedProcess:
    env = dict(os.environ, PATH=tool_path(), OCTAVE_HOME=str(ENV))  # conda Octave needs its prefix told
    r = subprocess.run(cmd, text=True, capture_output=True, env=env, **kw)
    if r.returncode:
        sys.stderr.write(r.stdout[-3000:] + r.stderr[-6000:])
        raise subprocess.CalledProcessError(r.returncode, cmd)
    return r


def replace_outputs(out: Path, dst: Path) -> None:
    """Install a driver's golden files from `out` into `dst` (golden/<oracle>)
    without touching files another script wrote there: two scripts may share
    one oracle directory (boost_oracle.py and planarity_boost_oracle.py both
    write golden/boost). Every file in `dst` of a variant the driver wrote
    (same file name, any fixture) is removed first, so a variant that no
    longer applies to a fixture leaves no stale file; other files stay."""
    produced = {p.name for p in out.rglob("*") if p.is_file()}
    if dst.exists():
        for p in dst.rglob("*"):
            if p.is_file() and p.name in produced:
                p.unlink()
    shutil.copytree(out, dst, dirs_exist_ok=True)
