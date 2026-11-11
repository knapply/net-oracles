#!/usr/bin/env python3
"""Golden values from the Brain Connectivity Toolbox (Rubinov and Sporns
2010; release 2019-03-03) run under GNU Octave through a small driver
(system/bct/oracle.m). The toolbox is downloaded at run time from its
author's page (it carries no redistributable license, so it is never
committed; only the numbers it returns are). Inputs are binary adjacency
matrices without loops or parallel edges, which is all a BCT call can carry.
Without Octave the script is skipped and the committed goldens stay.

    python3 oracles/bct_oracle.py
"""
from __future__ import annotations

import hashlib
import os
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import system_run as sr  # noqa: E402
from common import FIXTURES, GOLDEN, write_version  # noqa: E402

ORACLE = "bct"
RELEASE = "2019_03_03"
URL = "https://drive.usercontent.google.com/download?id=1DmMvRnferBfGe057O-sZwB5jL4j8w1Hu&export=download&confirm=t"
SHA256 = ""  # filled in after the first verified download


def main() -> None:
    octave = sr.which("octave")
    if not octave:
        sr.skip("octave not found (run tools/oracle_env.sh)")
    cache = Path.home() / ".cache" / "bct"
    cache.mkdir(parents=True, exist_ok=True)
    zpath = cache / f"BCT_{RELEASE}.zip"
    if not zpath.exists():
        urllib.request.urlretrieve(URL, zpath)
    digest = hashlib.sha256(zpath.read_bytes()).hexdigest()
    if SHA256 and digest != SHA256:
        raise SystemExit(f"BCT archive hash {digest} != pinned {SHA256}")
    print(f"   BCT archive sha256 {digest}")
    src = sr.ROOT / "oracles" / "system" / "bct" / "oracle.m"
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(zpath) as z:
            z.extractall(tmp)
        out = Path(tmp) / "golden"
        env = dict(os.environ, FIXTURES=str(FIXTURES), OUT=str(out), BCT=tmp, BCT_RELEASE=RELEASE)
        os.environ.update(env)
        res = sr.run([octave, "--no-gui", "--quiet", str(src)])
        version = res.stdout.strip().splitlines()[-1]
        dst = GOLDEN / ORACLE
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(out, dst)
    write_version(ORACLE, version)
    print(f"{version}: wrote {sum(1 for _ in (GOLDEN / ORACLE).rglob('*.csv'))} golden files")


if __name__ == "__main__":
    main()
