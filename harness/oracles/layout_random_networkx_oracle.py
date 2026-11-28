#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for the random layout entries of
manifest/layout.yaml (derived/layout_random.py): `nx.random_layout`, run as a black box.
The tool draws from its own random stream, so the coordinates are not compared;
the same statements the engine must satisfy (inside the box, repeatable,
independent of the edges, seed-dependent, and uniform) are evaluated on its
output, mapped to the box [-1, 1).

    python3 oracles/layout_random_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import layout_random as L  # noqa: E402

ORACLE = "networkx"
LOW, HIGH = L.BOX


def layout_of(fx):
    def layout(n, edgeless, seed):
        g = nx.empty_graph(n) if edgeless or n != fx.n else nx.Graph()
        if not edgeless and n == fx.n:
            g.add_nodes_from(range(n))
            g.add_edges_from(zip(fx.src, fx.tgt))
        pos = nx.random_layout(g, seed=seed)
        return LOW + (HIGH - LOW) * np.array([pos[v] for v in range(n)]).reshape(n, 2)
    return layout


def compute(fx, engine):
    if engine["mode"] == "distribution":
        return [L.distribution_flags(layout_of(fx), LOW, HIGH)]
    return [L.property_flags(layout_of(fx), fx.n, LOW, HIGH)]


def main() -> None:
    spec = load_area("layout")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if (ORACLE not in v["oracles"] or not applies(v, fx)
                    or v["params"]["fn"] != "layout_random"):
                continue
            if "only_on" in v["oracles"][ORACLE] and name not in v["oracles"][ORACLE]["only_on"]:
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (layout, random): wrote {count} golden files")


if __name__ == "__main__":
    main()
