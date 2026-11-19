#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
centrality across sampled possible worlds (manifest/
worlds.yaml, entries with a `networkx` oracle), on the materialized worlds.

The worlds are drawn as the definition oracle draws them
(worlds_definition_oracle.world_edges); each world becomes an nx.Graph or
nx.DiGraph with every node, and then

  worlds_closeness  nx.closeness_centrality(G, wf_improved = True)
  worlds_harmonic   nx.harmonic_centrality(G)
  worlds_reach      len(nx.ancestors(G, v)) (directed), else the size of
                    v's component minus 1

NetworkX's closeness and harmonic centrality use the distances into a node
in directed graphs; the engine runs with mode `in` there.

    python3 oracles/worlds_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from worlds_definition_oracle import world_edges  # noqa: E402

ORACLE = "networkx"


def world_graph(fx, spec, world):
    g = nx.DiGraph() if fx.directed else nx.Graph()
    g.add_nodes_from(range(fx.n))
    g.add_edges_from(world_edges(fx, spec, world))
    return g


def values(g, stat, n):
    if stat == "closeness":
        c = nx.closeness_centrality(g, wf_improved=True)
        return [c[v] for v in range(n)]
    if stat == "harmonic":
        c = nx.harmonic_centrality(g)
        return [c[v] for v in range(n)]
    if g.is_directed():
        return [float(len(nx.ancestors(g, v))) for v in range(n)]
    return [float(len(nx.node_connected_component(g, v)) - 1) for v in range(n)]


def compute(fx, spec):
    if fx.n == 0:
        return []
    worlds = int(spec["worlds"])
    matrix = [values(world_graph(fx, spec, w), spec["stat"], fx.n) for w in range(worlds)]
    return [matrix[w][v] for v in range(fx.n) for w in range(worlds)]


def main() -> None:
    spec = load_area("worlds")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if "networkx" not in v["oracles"] or not applies(v, fx):
                continue
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (possible worlds): wrote {count} golden files")


if __name__ == "__main__":
    main()
