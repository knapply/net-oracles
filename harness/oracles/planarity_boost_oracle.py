#!/usr/bin/env python3
"""Golden values from the Boost Graph Library (Siek, Lee and Lumsdaine 2002)
for the planarity measures, run as a black box through a small C++ driver
(system/boost/planarity.cpp): boyer_myrvold_planarity_test (planarity, the
rotation system, the Kuratowski subgraph) and chrobak_payne_straight_line_
drawing after make_connected, make_biconnected_planar and make_maximal_planar.
The driver writes raw results; the checks of ../planarity_check.py turn them
into validity values (Boost's embeddings, certificates and drawings are
checked, never compared coordinate by coordinate). Needs the private tool
prefix (tools/oracle_env.sh: Boost headers); without it the script is
skipped and the committed goldens stay. Inputs and encodings:
../bindings/planarity.py.

    python3 oracles/planarity_boost_oracle.py
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import planarity_check as C  # noqa: E402
import system_run as sr  # noqa: E402
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "boost"
AREA = "planarity"
ORACLE_INPUTS = ["fixtures", "oracles/system/boost/planarity.cpp",
                 "oracles/system_run.py", "oracles/planarity_boost_oracle.py",
                 "planarity_check.py"]


def parse(text):
    out, cur = {}, None
    for line in text.splitlines():
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "fixture":
            cur = out.setdefault(parts[1], {"ring": {}, "point": {}, "kur": [], "error": None})
        elif parts[0] == "planar":
            cur["planar"] = int(parts[1])
        elif parts[0] == "ring":
            cur["ring"][int(parts[1])] = [int(x) for x in parts[3:]]
        elif parts[0] == "point":
            cur["point"][int(parts[1])] = (int(parts[2]), int(parts[3]))
        elif parts[0] == "kuratowski":
            cur["kur"].append((int(parts[1]), int(parts[2])))
        elif parts[0] == "error":
            cur["error"] = line
    return out


def main() -> None:
    gxx = sr.which("g++")
    if not gxx or not (sr.ENV / "include" / "boost" / "graph").exists():
        sr.skip("g++ or Boost headers not found (run tools/oracle_env.sh)")
    src = sr.ROOT / "oracles" / "system" / "boost" / "planarity.cpp"
    spec = load_area(AREA)
    fixtures = {name: load_fixture(name) for name in fixture_names()}
    with tempfile.TemporaryDirectory() as tmp:
        exe, inp, raw = Path(tmp) / "planarity", Path(tmp) / "in.txt", Path(tmp) / "out.txt"
        sr.run([gxx, "-std=c++17", "-O1", f"-isystem{sr.ENV}/include", str(src), "-o", str(exe)])
        lines = [str(len(fixtures))]
        for name, fx in fixtures.items():
            pairs = C.simple_pairs(fx.src, fx.tgt)
            lines.append(f"{name} {fx.n} {len(pairs)}")
            lines += [f"{a} {b}" for a, b in pairs]
        inp.write_text("\n".join(lines) + "\n")
        version = sr.run([str(exe), str(inp), str(raw)]).stdout.strip()
        results = parse(raw.read_text())
    count = 0
    for name, fx in fixtures.items():
        res = results[name]
        pairs = C.simple_pairs(fx.src, fx.tgt)
        values = {}
        if res["error"] is None or "planar" in res:
            planar = res.get("planar")
            values["pl_planar"] = [planar]
            if planar == 1:
                rings = [res["ring"][v] for v in range(fx.n)]
                values["pl_embedding_valid"] = [C.check_simple_embedding(fx.n, pairs, rings)]
                if len(res["point"]) == fx.n and fx.n >= 3:
                    pts = [res["point"][v] for v in range(fx.n)]
                    values["pl_layout_valid"] = C.check_drawing(fx.n, pts, pairs, rings)[:3] + [1]
                elif fx.n >= 3:
                    print(f"   {name}: no drawing ({res['error']})")
            else:
                values["pl_embedding_valid"] = [-1]
                values["pl_layout_valid"] = [-1]
                # Boost's isolator returns a non-planar subgraph that need not
                # be minimal (pendant paths, extra chords): check that it is
                # a non-planar subgraph of the input.
                edges = {(min(a, b), max(a, b)) for a, b in res["kur"]}
                g = nx.Graph(sorted(edges))
                good = edges <= set(pairs) and not nx.is_planar(g)
                values["pl_kuratowski_valid"] = [int(good), 1]
                if not good:
                    print(f"   {name}: Boost's Kuratowski edges are planar or not input edges")
            if planar == 1:
                values["pl_kuratowski_valid"] = [-1]
        for variant, v in spec.items():
            if ORACLE in v["oracles"] and applies(v, fx) and v["params"]["fn"] in values:
                write_values(ORACLE, name, variant, values[v["params"]["fn"]])
                count += 1
    write_version(ORACLE, version)
    print(f"{version}: wrote {count} golden files")


if __name__ == "__main__":
    main()
