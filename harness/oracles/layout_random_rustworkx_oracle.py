#!/usr/bin/env python3
# oracle-env: rustworkx
"""Golden values from rustworkx (Treinish et al. 2022) for the random layout entries of
manifest/layout.yaml (derived/layout_random.py): `rustworkx.random_layout`, run as a black box.
The tool draws from its own random stream, so the coordinates are not compared;
the same statements the engine must satisfy (inside the box, repeatable,
independent of the edges, seed-dependent, and uniform) are evaluated on its
output, mapped to the box [-1, 1).

    ~/oracle-envs/rustworkx/bin/python oracles/layout_random_rustworkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
try:
    import rustworkx as rx
except ImportError:  # the tool is not installed here
    print("rustworkx is not installed")
    sys.exit(3)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import layout_random as L  # noqa: E402

ORACLE = "rustworkx"
LOW, HIGH = L.BOX


def layout_of(fx):
    def layout(n, edgeless, seed):
        g = rx.PyGraph(multigraph=True)
        g.add_nodes_from(list(range(n)))
        if not edgeless and n == fx.n:
            g.add_edges_from([(a, b, None) for a, b in zip(fx.src, fx.tgt)])
        pos = rx.random_layout(g, seed=seed)
        return LOW + (HIGH - LOW) * np.array([list(pos[v]) for v in range(n)]).reshape(n, 2)
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
    write_version(ORACLE, f"rustworkx {rx.__version__}")
    print(f"rustworkx (layout, random): wrote {count} golden files")


if __name__ == "__main__":
    main()
