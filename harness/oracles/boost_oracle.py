#!/usr/bin/env python3
"""Golden values from the Boost Graph Library, run as a black box through a
small C++ driver (system/boost/oracle.cpp) that reads the fixture files and
writes golden files. Needs the private tool prefix (tools/oracle_env.sh:
Boost headers; the system or prefix g++). Without them the script is
skipped and the committed goldens stay.

    python3 oracles/boost_oracle.py
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import system_run as sr  # noqa: E402
from common import FIXTURES, GOLDEN, write_version  # noqa: E402

ORACLE = "boost"
ORACLE_INPUTS = ["fixtures", "oracles/system/boost",
                 "oracles/system_run.py", "oracles/boost_oracle.py"]


def main() -> None:
    gxx = sr.which("g++")
    if not gxx or not (sr.ENV / "include" / "boost" / "graph").exists():
        sr.skip("g++ or Boost headers not found (run tools/oracle_env.sh)")
    src = sr.ROOT / "oracles" / "system" / "boost" / "oracle.cpp"
    with tempfile.TemporaryDirectory() as tmp:
        exe = Path(tmp) / "oracle"
        sr.run([gxx, "-std=c++17", "-O1", f"-isystem{sr.ENV}/include", str(src), "-o", str(exe)])
        out = Path(tmp) / "golden"
        version = sr.run([str(exe), str(FIXTURES), str(out)]).stdout.strip()
        dst = GOLDEN / ORACLE
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(out, dst)
    write_version(ORACLE, version)
    print(f"{version}: wrote {sum(1 for _ in (GOLDEN / ORACLE).rglob('*.csv'))} golden files")


if __name__ == "__main__":
    main()
