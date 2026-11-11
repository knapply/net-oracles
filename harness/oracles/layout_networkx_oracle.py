#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
layouts: the stress sum of a fixed probe layout with NetworkX distances, and
the optimally scaled stress of kamada_kawai_layout (Kamada and Kawai 1989).
See ../bindings/layout.py for the derived inputs and encodings.

    python3 oracles/layout_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkx"


def skeleton(n, src, tgt, weights):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for e, (a, b) in enumerate(zip(src, tgt)):
        if a == b:
            continue
        w = 1.0 if weights is None else weights[e]
        if G.has_edge(a, b):
            G[a][b]["weight"] = min(G[a][b]["weight"], w)
        else:
            G.add_edge(a, b, weight=w)
    return G


def dist(G, weighted):
    n = G.number_of_nodes()
    D = np.full((n, n), np.inf)
    lengths = (nx.all_pairs_dijkstra_path_length(G, weight="weight") if weighted
               else nx.all_pairs_shortest_path_length(G))
    for a, row in lengths:
        for b, d in row.items():
            D[a, b] = d
    return D


def stress(xy, D, rescale):
    iu = np.triu_indices(len(xy), 1)
    d = D[iu]
    e = np.sqrt(((xy[:, None, :] - xy[None, :, :]) ** 2).sum(-1))[iu]
    ok = np.isfinite(d) & (d > 0)
    d, e = d[ok], e[ok]
    if rescale and (e * e / (d * d)).sum() > 0:
        e = e * (e / d).sum() / (e * e / (d * d)).sum()
    return float((((e - d) / d) ** 2).sum())


def compute(fx, e):
    fn, weighted = e["fn"], bool(e.get("weighted"))
    w = list(fx.weights) if weighted else None
    if fn == "layout_stress_value":
        G = skeleton(fx.n, fx.src, fx.tgt, w)
        xy = np.array([[((7 * i) % 13) / 4.0, ((5 * i * i + 3 * i) % 11) / 3.0]
                       for i in range(fx.n)]).reshape(fx.n, 2)
        return [stress(xy, dist(G, weighted), False)]
    if fn == "layout_stress_quality":
        G = skeleton(fx.n, fx.src, fx.tgt, w)
        keep = sorted(max(nx.connected_components(G), key=lambda c: (len(c), -min(c))))
        if len(keep) < 3:
            return [0.0]
        H = nx.relabel_nodes(G.subgraph(keep).copy(), {v: i for i, v in enumerate(keep)})
        kk = nx.kamada_kawai_layout(H, weight="weight" if weighted else None)
        xy = np.array([kk[v] for v in range(len(keep))])
        return [stress(xy, dist(H, weighted), True)]
    return None


def main() -> None:
    spec = load_area("layout")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            values = compute(fx, v["params"])
            if values is not None:
                write_values(ORACLE, name, variant, values)
                count += 1
    print(f"networkx {nx.__version__} (layout): wrote {count} golden files")
    write_version(ORACLE, f"networkx {nx.__version__}")


if __name__ == "__main__":
    main()
