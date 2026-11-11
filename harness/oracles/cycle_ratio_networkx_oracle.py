#!/usr/bin/env python3
"""Golden values for cycle ratios by enumerating the simple cycles with
NetworkX (Hagberg, Schult, and Swart 2008; nx.simple_cycles, Johnson 1975)
and taking the least or greatest total cost over total time; the optimum is
attained on a simple cycle. Only the small fixtures without parallel edges
(manifest/cycle_ratio.yaml, `only_on`); synthetic costs and
times as in ../bindings/cycle_ratio.py.

    python3 oracles/cycle_ratio_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"


def cost(e):
    return float(((7 * e + 3) % 11) - 3)


def time(e):
    return float(1 + e % 3)


def compute(fx, spec):
    if not fx.directed:
        return []
    m = len(fx.src)
    use_time = spec.get("times", "none") == "pattern"
    g = nx.DiGraph()
    g.add_nodes_from(range(fx.n))
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        g.add_edge(a, b, c=cost(e), t=time(e) if use_time else 1.0)
    values = []
    for cycle in nx.simple_cycles(g):
        pairs = list(zip(cycle, cycle[1:] + cycle[:1]))
        values.append(sum(g[a][b]["c"] for a, b in pairs) / sum(g[a][b]["t"] for a, b in pairs))
    if not values:
        return [-999.0]
    return [max(values) if spec.get("extreme") == "maximum" else min(values)]


def main() -> None:
    spec = load_area("cycle_ratio")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            o = v["oracles"].get(ORACLE)
            if o is None or not applies(v, fx):
                continue
            if "only_on" in o and name not in o["only_on"]:
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (cycle ratio): wrote {count} golden files")


if __name__ == "__main__":
    main()
