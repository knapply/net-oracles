#!/usr/bin/env python3
# oracle-env: rustworkx
"""Golden values from rustworkx (Treinish et al. 2022) for the binomial tree of
manifest/generators_ext.yaml (encodings in bindings/generators_ext.py, cases
in derived/generators_ext.py): `rustworkx.generators.binomial_tree_graph`,
run as a black box, nodes numbered as the library numbers them.

    ~/oracle-envs/rustworkx/bin/python oracles/generators_ext_rustworkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import rustworkx as rx
except ImportError:  # the tool is not installed here
    print("rustworkx is not installed")
    sys.exit(3)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import generators_ext as D  # noqa: E402

ORACLE = "rustworkx"


def compute(engine):
    family = engine.get("family")
    out = []
    if family == "binomial_tree":
        for order in D.BINOMIAL_TREE:
            g = rx.generators.binomial_tree_graph(order)
            edges = [(int(a), int(b)) for a, b in g.edge_list()]
            out += D.pack(g.num_nodes(), D.normalize(edges, False))
    else:
        raise ValueError(family or engine["fn"])
    return out


def main() -> None:
    spec = load_area("generators_ext")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            if "only_on" in v["oracles"][ORACLE] and name not in v["oracles"][ORACLE]["only_on"]:
                continue
            write_values(ORACLE, name, variant, compute(v["params"]))
            count += 1
    write_version(ORACLE, f"rustworkx {rx.__version__}")
    print(f"rustworkx (generators_ext): wrote {count} golden files")


if __name__ == "__main__":
    main()
