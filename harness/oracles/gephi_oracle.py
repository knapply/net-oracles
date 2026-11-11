#!/usr/bin/env python3
# oracle-entries: gephi
"""Golden values from the Gephi toolkit 0.11.3 (Gephi contributors), run as a
black box through a small Java driver (system/gephi/Oracle.java) that reads the
fixture files and writes golden files. The toolkit is GPL-3 / CDDL: only its
published jar and public API are used, never its source. Needs the private
tool prefix (tools/oracle_env.sh: OpenJDK) and downloads the pinned jar from
Maven Central. Without them the script is skipped and the committed goldens
stay.

    python3 oracles/gephi_oracle.py
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

ORACLE = "gephi"
GEPHI = "0.11.3"
ORACLE_INPUTS = ["fixtures", "oracles/system/gephi",
                 "oracles/system_run.py", "oracles/gephi_oracle.py"]


def main() -> None:
    java, javac = sr.which("java"), sr.which("javac")
    if not (java and javac):
        sr.skip("java not found (run tools/oracle_env.sh)")
    src = sr.ROOT / "oracles" / "system" / "gephi"
    jar = sr.run(["bash", str(src / "fetch_jar.sh")]).stdout.strip()
    with tempfile.TemporaryDirectory() as tmp:
        sr.run([javac, "-d", tmp, "-cp", jar, str(src / "Oracle.java"), str(src / "Louvain20.java")])
        out = Path(tmp) / "golden"
        sr.run([java, "-Djava.awt.headless=true", "-cp", f"{jar}:{tmp}", "Oracle", str(FIXTURES), str(out)])
        dst = GOLDEN / ORACLE
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(out, dst)
    jv = sr.run([java, "-version"]).stderr.splitlines()[0]
    write_version(ORACLE, f"Gephi toolkit {GEPHI} ({jv})")
    print(f"gephi {GEPHI}: wrote {sum(1 for _ in (GOLDEN / ORACLE).rglob('*.csv'))} golden files")


if __name__ == "__main__":
    main()
