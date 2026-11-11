#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
traversals and the shortest-path functions whose results depend on how
ties are settled.

Graphs are NetworkX multigraphs of the fixture: nodes 0..n - 1, then the
edges in file order keyed by their position, with the fixture's weight as
the "weight" attribute. Encodings follow bindings/traversal.py.

    python3 oracles/traversal_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"
BFS_KIND = {"tree": 0, "level": 1, "forward": 2, "reverse": 3}
DFS_KIND = {"forward": 0, "nontree": 1, "reverse": 2}


def multigraph(fx):
    g = (nx.MultiDiGraph if fx.directed else nx.MultiGraph)()
    g.add_nodes_from(range(fx.n))
    for e, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        if fx.weighted:
            g.add_edge(a, b, key=e, weight=fx.weights[e])
        else:
            g.add_edge(a, b, key=e)
    return g


def compute(spec, fx):
    e = spec["params"]
    fn = e["fn"]
    M = multigraph(fx)
    w = "weight" if e.get("weighted", fn in ("ord_bidir_dijkstra", "ord_astar")) and fx.weighted \
        else None
    last = fx.n - 1
    if fx.n == 0 and fn != "trav_dfs_events" and not fn.startswith("trav_edge"):
        return []
    if fn == "trav_bfs_edges":
        return [(float(a), float(b)) for a, b in nx.bfs_edges(M, 0)]
    if fn == "trav_beam":
        return [(float(a), float(b))
                for a, b in nx.bfs_beam_edges(M, 0, lambda v: (v * 7) % 5, e.get("width", 2))]
    if fn == "trav_bfs_layers":
        return [tuple(float(v) for v in layer) for layer in nx.bfs_layers(M, [0])]
    if fn == "trav_bfs_labeled":
        return [(float(a), float(b), float(BFS_KIND[k])) for a, b, k in nx.bfs_labeled_edges(M, [0])]
    if fn == "trav_dfs_events":
        return [(float(a), float(b), float(DFS_KIND[k])) for a, b, k in nx.dfs_labeled_edges(M)]
    if fn in ("trav_edge_bfs", "trav_edge_dfs"):
        o = e.get("orientation", "none")
        o = None if o == "none" else o
        search = nx.edge_bfs if fn == "trav_edge_bfs" else nx.edge_dfs
        out = []
        for x in search(M, None, orientation=o):
            rev = 1.0 if len(x) > 3 and x[3] == "reverse" else 0.0
            out.append((float(x[0]), float(x[1]), float(x[2]), rev))
        return out
    if fn == "ord_dijkstra":
        if e.get("preds"):
            pred, _ = nx.dijkstra_predecessor_and_distance(M, 0, weight=w)
            return [tuple([float(v)] + [float(p) for p in ps]) for v, ps in pred.items()]
        dist, paths = nx.single_source_dijkstra(M, 0, weight=w)
        return [(float(v), float(d), float(paths[v][-2]) if len(paths[v]) > 1 else -1.0)
                for v, d in dist.items()]
    if fn == "ord_bellman_ford":
        pred, dist = nx.bellman_ford_predecessor_and_distance(M, 0, weight=w)
        return [tuple([float(v), float(dist[v])] + [float(p) for p in ps]) for v, ps in pred.items()]
    if fn == "ord_bidir_bfs":
        try:
            return [float(v) for v in nx.bidirectional_shortest_path(M, 0, last)]
        except nx.NetworkXNoPath:
            return []
    if fn == "ord_bidir_dijkstra":
        try:
            length, path = nx.bidirectional_dijkstra(M, 0, last, weight=w)
        except nx.NetworkXNoPath:
            return []
        return [float(v) for v in path] + [float(length)]
    if fn == "ord_astar":
        try:
            return [float(v) for v in nx.astar_path(M, 0, last, weight=w)]
        except nx.NetworkXNoPath:
            return []
    raise ValueError(fn)


def main() -> int:
    manifest = load_area("traversal")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        tags = set(fx.tags) | {"directed" if fx.directed else "undirected"}
        for variant, spec in manifest.items():
            ospec = spec["oracles"].get(ORACLE)
            if (ospec is None or not applies(spec, fx) or name in ospec.get("undefined_on", [])
                    or tags & set(ospec.get("undefined_when", []))):
                continue
            write_values(ORACLE, name, variant, compute(spec, fx))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (traversal): wrote {count} golden files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
