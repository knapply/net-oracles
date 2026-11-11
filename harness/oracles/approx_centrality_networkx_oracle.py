#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for sampled
and pruned centralities (manifest/approx_centrality.yaml, entries
with a `networkx` oracle).

  bcapprox_all[_weighted]  nx.betweenness_centrality(G, normalized = False)
  clapprox_all             nx.closeness_centrality(G, wf_improved = False)
  cltopk_*                 nx.harmonic_centrality(G), ranked by value rounded
                           to nine places and then id
  grpcl_value              nx.group_closeness_centrality(G, S) for the
                           greedy group S chosen from the definition (the
                           oracle's own brute-force greedy, not NetworkX's)

NetworkX reads the fixture as a simple graph (nx.Graph or nx.DiGraph).

    python3 oracles/approx_centrality_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from approx_centrality_definition_oracle import group  # noqa: E402
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"
TOP = 5


def simple(fx, weighted):
    g = nx.DiGraph() if fx.directed else nx.Graph()
    g.add_nodes_from(range(fx.n))
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        g.add_edge(a, b, weight=fx.weights[e] if weighted and fx.weighted else 1.0)
    return g


def compute(fx, spec):
    if fx.n == 0:
        return []
    weighted = bool(spec.get("weighted"))
    if weighted and fx.weighted and any(w <= 0 for w in fx.weights):
        return []
    g = simple(fx, weighted)
    fn, stat = spec["fn"], spec["stat"]
    if fn == "betweenness_approx":
        c = nx.betweenness_centrality(g, normalized=False, weight="weight" if weighted else None)
        return [c[v] for v in range(fx.n)]
    if fn == "closeness_approx":
        c = nx.closeness_centrality(g, wf_improved=False)
        return [c[v] for v in range(fx.n)]
    if fn == "closeness_top_k":
        c = nx.harmonic_centrality(g)
        order = sorted(range(fx.n), key=lambda v: (-round(c[v], 9), v))[:TOP]
        return [c[v] for v in order] if stat == "values" else order
    result = group(fx)
    if result is None:
        return []
    return [nx.group_closeness_centrality(g, result[0])]


def main() -> None:
    spec = load_area("approx_centrality")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            o = v["oracles"].get(ORACLE)
            if o is None or not applies(v, fx):
                continue
            if ("only_on" in o and name not in o["only_on"]) or \
                    set(fx.tags) & set(o.get("undefined_when", [])):
                continue
            try:
                values = compute(fx, v["params"])
            except Exception as exc:  # NetworkX fails where the answer is undefined
                print(f"  {name} {variant}: {type(exc).__name__}")
                continue
            write_values(ORACLE, name, variant, values)
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (approximate centralities): wrote {count} golden files")


if __name__ == "__main__":
    main()
