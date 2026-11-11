#!/usr/bin/env python3
"""Golden values from JGraphT 1.5.2 (Naveh and contributors), run as a black
box through a small Java driver (system/jgrapht/Oracle.java) that reads the
fixture files and writes golden files. Needs the private tool prefix
(tools/oracle_env.sh: OpenJDK) and downloads the pinned jars from Maven
Central. Without them the script is skipped and the committed goldens stay.

    python3 oracles/jgrapht_oracle.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import system_run as sr  # noqa: E402
from common import FIXTURES, GOLDEN, write_version  # noqa: E402

ORACLE = "jgrapht"
JGRAPHT = "1.5.2"
ORACLE_INPUTS = ["fixtures", "oracles/system/jgrapht",
                 "oracles/system_run.py", "oracles/jgrapht_oracle.py"]


def main() -> None:
    java, javac = sr.which("java"), sr.which("javac")
    if not (java and javac):
        sr.skip("java not found (run tools/oracle_env.sh)")
    src = sr.ROOT / "oracles" / "system" / "jgrapht"
    cp = sr.run(["bash", str(src.parent / "fetch_jars.sh")]).stdout.strip()
    with tempfile.TemporaryDirectory() as tmp:
        sr.run([javac, "-d", tmp, "-cp", cp, str(src / "Oracle.java")])
        out = Path(tmp) / "golden"
        sr.run([java, "-cp", f"{cp}:{tmp}", "Oracle", str(FIXTURES), str(out)])
        dst = GOLDEN / ORACLE
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(out, dst)
    jv = sr.run([java, "-version"]).stderr.splitlines()[0]
    write_version(ORACLE, f"JGraphT {JGRAPHT} ({jv})")
    print(f"jgrapht {JGRAPHT}: wrote {sum(1 for _ in (GOLDEN / ORACLE).rglob('*.csv'))} golden files")


if __name__ == "__main__":
    main()
