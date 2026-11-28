#!/usr/bin/env python3
"""Golden values from the Boost Graph Library (Siek, Lee and Lumsdaine 2002) for
the random layout entries of manifest/layout.yaml (derived/layout_random.py):
`random_graph_layout` over a `rectangle_topology` of [-1, 1]^2, run as a black
box through a small C++ driver (system/boost/random_layout.cpp). The driver
writes the layouts; the statements every tool must satisfy (inside the box,
repeatable, independent of the edges, seed dependent, uniform) are evaluated
here on them. Boost's function takes the graph only for its node set, so the
"edges" calls use a path on the same nodes. Needs the private tool prefix
(tools/oracle_env.sh: Boost headers); without it the script is skipped and the
committed goldens stay.

    python3 oracles/layout_random_boost_oracle.py
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import system_run as sr  # noqa: E402
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import layout_random as L  # noqa: E402

ORACLE = "boost"
ORACLE_INPUTS = ["fixtures", "oracles/system/boost/random_layout.cpp",
                 "oracles/system_run.py", "oracles/layout_random_boost_oracle.py",
                 "derived/layout_random.py"]
LOW, HIGH = L.BOX


def parse(path):
    """n -> the layouts of that size, in the order the driver wrote them."""
    out, lines, i = {}, Path(path).read_text().splitlines(), 0
    while i < len(lines):
        _, n, seed, edges = lines[i].split()
        n = int(n)
        rows = [[float(x) for x in lines[i + 1 + k].split()] for k in range(n)]
        out.setdefault(n, []).append(np.array(rows).reshape(n, 2))
        i += 1 + n
    return out


def main() -> None:
    gxx = sr.which("g++")
    if not gxx or not (sr.ENV / "include" / "boost" / "graph").exists():
        sr.skip("g++ or Boost headers not found (run tools/oracle_env.sh)")
    names = fixture_names()
    sizes = sorted({load_fixture(name).n for name in names} | {L.SAMPLE})
    src = sr.ROOT / "oracles" / "system" / "boost" / "random_layout.cpp"
    with tempfile.TemporaryDirectory() as tmp:
        exe = Path(tmp) / "random_layout"
        sr.run([gxx, "-std=c++17", "-O1", f"-isystem{sr.ENV}/include", str(src), "-o", str(exe)])
        version = sr.run([str(exe), str(Path(tmp) / "layouts.txt")] + [str(n) for n in sizes]).stdout.strip()
        layouts = parse(Path(tmp) / "layouts.txt")
    spec = load_area("layout")
    count = 0
    for name in names:
        fx = load_fixture(name)
        for variant, v in spec.items():
            if (ORACLE not in v["oracles"] or not applies(v, fx)
                    or v["params"]["fn"] != "layout_random"):
                continue
            if "only_on" in v["oracles"][ORACLE] and name not in v["oracles"][ORACLE]["only_on"]:
                continue
            if v["params"]["mode"] == "distribution":
                # The last layout of the sample size: seed 1, no edges.
                values = [L.unit_uniform_flags(*(((layouts[L.SAMPLE][4] - LOW) / (HIGH - LOW)).T))]
            else:
                queue = list(layouts[fx.n][:4])
                values = [L.property_flags(lambda n, edgeless, seed: queue.pop(0), fx.n, LOW, HIGH)]
            write_values(ORACLE, name, variant, values)
            count += 1
    write_version(ORACLE, version)
    print(f"{version}: wrote {count} golden files")


if __name__ == "__main__":
    main()
