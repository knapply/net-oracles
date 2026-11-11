#!/usr/bin/env python3
# oracle-env: networkit
# oracle-entries: networkit
"""Golden values from NetworKit (Staudt, Sazonovs, and Meyerhenke 2016),
an independent C++ implementation. Only exact algorithms are used.

The fixture is loaded edge by edge into a NetworKit graph (parallel edges
and self-loops kept, edge ids in fixture order); a measure NetworKit
rejects on some input writes nothing for it, and the manifest records why.
Directed in-mode measures run on the reversed graph. Calls are written in
the manifest's `call` for each measure.

    ~/oracle-envs/networkit/bin/python oracles/networkit_oracle.py
"""

from __future__ import annotations

import math

import networkit as nk
import numpy as np

from tool_common import (adjacency, groups_of, has_loops, node_rule, run, simple_edges,
                         weights)

ORACLE = "networkit"
nk.engineering.setNumberOfThreads(1)


def build(fx, *, weighted=False, reverse=False, edges=None, directed=None):
    directed = fx.directed if directed is None else directed
    g = nk.Graph(fx.n, weighted=weighted, directed=directed)
    if edges is None:
        edges = list(zip(fx.src, fx.tgt, weights(fx)))
    for a, b, w in edges:
        if reverse:
            a, b = b, a
        if weighted:
            g.addEdge(a, b, w)
        else:
            g.addEdge(a, b)
    g.indexEdges()
    return g


def scores(algo):
    algo.run()
    return [float(x) for x in algo.scores()]


def distribute_sinks():
    """The enum member that spreads a dangling node's rank, whatever the
    release names it."""
    sh = nk.centrality.SinkHandling
    for name in dir(sh):
        if name.replace("_", "").lower() == "distributesinks":
            return getattr(sh, name)
    raise RuntimeError("no SinkHandling member distributes sinks: " + ", ".join(dir(sh)))


def lambda_max(a) -> float:
    return float(max(abs(np.linalg.eigvals(np.array(a)))))


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    fn = e["fn"]
    n = fx.n
    wt = bool(e.get("weighted"))
    pairs = [(a, b) if fx.directed or a <= b else (b, a) for a, b in zip(fx.src, fx.tgt)]
    messy = len(set(pairs)) < len(pairs) or any(a == b for a, b in pairs)
    # Left out, with the reason in docs/drafts/convention_atlas.md: edge
    # betweenness (scores follow NetworKit's own edge order), Katz, eigenvector
    # centrality (power iteration stops near 1e-7), degree assortativity, and
    # the loop and parallel-edge, directed and degenerate cases below.
    if fn in ("katz", "eigenvector", "assortativity_degree"):
        return None
    if fn == "edge_betweenness" and messy:
        return None  # edge ids are ambiguous for parallel edges
    if messy and (fn in ("betweenness", "cx_laplacian", "modularity", "max_cliques", "coreness")
                  or (fn == "degree" and not fx.directed)):
        return None
    if fn == "coreness" and fx.directed:
        return None
    if fn in ("max_cliques", "transitivity") and (not fx.src or (fn == "transitivity" and n < 3)):
        return None
    if fn == "betweenness" and e.get("normalized") and n < 3:
        return None
    if fn == "pagerank" and len(set(fx.src) | set(fx.tgt)) < n:
        return None  # rank lost at isolated nodes is spread differently
    if fn in ("density", "closeness", "harmonic") and n < 2:
        return None
    if fn == "max_cliques" and len(set(fx.src) | set(fx.tgt)) < n:
        return None  # MaximalCliques omits isolated nodes
    if (fn == "diameter" or fn == "cx_laplacian") and wt:
        return None
    if fn == "strength" and fx.directed and messy:
        return None
    if fn == "degree":
        g = build(fx)
        mode = e["mode"]
        if not e.get("loops", True):
            g.removeSelfLoops()
        if mode == "out":
            return [g.degreeOut(v) for v in range(n)]
        if mode == "in":
            return [g.degreeIn(v) for v in range(n)]
        if fx.directed:
            return [g.degreeIn(v) + g.degreeOut(v) for v in range(n)]
        return [g.degree(v) for v in range(n)]
    if fn == "strength":
        g = build(fx, weighted=True)
        if fx.directed:
            return [g.weightedDegree(v) + g.weightedInDegree(v) for v in range(n)]
        return [g.weightedDegree(v, True) for v in range(n)]
    if fn == "betweenness" and not e.get("weights_as"):
        g = build(fx, weighted=wt)
        b = scores(nk.centrality.Betweenness(g, normalized=e["normalized"]))
        # NetworKit counts both orderings of an undirected pair.
        return b if e["normalized"] or fx.directed else [x / 2 for x in b]
    if fn == "edge_betweenness" and not e.get("weights_as") and not e.get("normalized"):
        g = build(fx, weighted=wt)
        b = nk.centrality.Betweenness(g, normalized=False, computeEdgeCentrality=True)
        b.run()
        es = [float(x) for x in b.edgeScores()]
        # Scores are indexed by NetworKit's own edge ids, which follow its
        # adjacency order and not the insertion order: look each input edge
        # up. An undirected pair is counted from both ends (twice).
        out = [es[g.edgeId(a, b2)] for a, b2 in zip(fx.src, fx.tgt)]
        return out if fx.directed else [x / 2 for x in out]
    if fn in ("closeness", "harmonic"):
        if e.get("weights_as") or e.get("simple") or e.get("symmetrize"):
            return None
        mode = e.get("mode", "out")
        if fx.directed and mode == "all":
            g = build(fx, weighted=wt, directed=False)
        else:
            g = build(fx, weighted=wt, reverse=fx.directed and mode == "in")
        if fn == "harmonic":
            return scores(nk.centrality.HarmonicCloseness(g, normalized=e["normalized"]))
        unreach = e.get("unreachable")
        if unreach == "wasserman_faust":
            variant_ = nk.centrality.ClosenessVariant.GENERALIZED
        elif unreach == "ignore":
            variant_ = nk.centrality.ClosenessVariant.STANDARD
        else:
            return None
        # NetworKit 11 returns the normalized value, (n - 1) / sum of distances,
        # whatever `normalized` says; the unnormalized one is that over n - 1.
        c = scores(nk.centrality.Closeness(g, True, variant_))
        if unreach == "ignore" and not e["normalized"]:
            c = [x / (n - 1) for x in c]
        return c
    if fn == "eigenvector":
        if e.get("simple") or e.get("symmetrize") or e.get("mode", "in") not in ("in", "all"):
            return None
        directed = fx.directed and e.get("mode", "in") == "in"
        g = build(fx, weighted=wt, directed=directed)
        x = scores(nk.centrality.EigenvectorCentrality(g, tol=1e-15))
        if e.get("scale") == "max":
            top = max(abs(v) for v in x)
            return [abs(v) / top for v in x] if top else x
        norm = math.sqrt(sum(v * v for v in x))
        return [abs(v) / norm for v in x] if norm else x
    if fn == "pagerank":
        if e.get("personalization") or e.get("directed") is False:
            return None
        g = build(fx, weighted=wt)
        pr = nk.centrality.PageRank(g, damp=e.get("damping", 0.85), tol=1e-15,
                                    normalized=False,
                                    distributeSinks=distribute_sinks())
        pr.maxIterations = 100000
        return scores(pr)
    if fn == "katz":
        if e.get("mode", "in") != "in" or e.get("beta"):
            return None
        if e.get("weighted"):
            return None
        a = adjacency(fx, loops="once" if e.get("loops") == "once" else "ignore")
        alpha = e["alpha_fraction"] / lambda_max(a)
        edges = list(zip(fx.src, fx.tgt, weights(fx)))
        if e.get("loops") == "ignore":
            edges = [x for x in edges if x[0] != x[1]]
        g = build(fx, edges=edges)
        x = scores(nk.centrality.KatzCentrality(g, alpha=alpha, beta=1.0, tol=1e-15))
        return x
    if fn == "coreness":
        if e["mode"] != "all":
            return None
        # CoreDecomposition crashes (segmentation fault) on a directed
        # graph in NetworKit 11, so directed fixtures enter as their
        # undirected simple reading.
        g = build(fx, edges=simple_edges(fx, undirected=True), directed=False)
        return scores(nk.centrality.CoreDecomposition(g))
    if fn == "clustering":
        if e.get("weighting") != "none":
            return None
        g = build(fx, edges=simple_edges(fx, undirected=True), directed=False)
        c = scores(nk.centrality.LocalClusteringCoefficient(g, turbo=False))
        if e.get("undefined") == "nan":
            deg = [g.degree(v) for v in range(n)]
            c = [x if deg[v] >= 2 else math.nan for v, x in enumerate(c)]
        return c
    if fn == "average_clustering":
        if e.get("weighting") != "none" or e.get("undefined") != "zero":
            return None
        g = build(fx, edges=simple_edges(fx, undirected=True), directed=False)
        return [sum(scores(nk.centrality.LocalClusteringCoefficient(g, turbo=False))) / n]
    if fn == "transitivity":
        g = build(fx, edges=simple_edges(fx, undirected=True), directed=False)
        t = nk.globals.ClusteringCoefficient.exactGlobal(g)
        return [t]
    if fn == "components":
        g = build(fx)
        if not fx.directed:
            cc = nk.components.ConnectedComponents(g)
        elif e["kind"] == "weak":
            cc = nk.components.WeaklyConnectedComponents(g)
        else:
            cc = nk.components.StronglyConnectedComponents(g)
        cc.run()
        part = cc.getPartition()
        return [float(part[v]) for v in range(n)]
    if fn == "distances":
        if e.get("weights_as") or e["mode"] == "in":
            return None
        directed = fx.directed and e["mode"] == "out"
        g = build(fx, weighted=wt, directed=directed)
        apsp = nk.distance.APSP(g)
        apsp.run()
        d = apsp.getDistances()
        return [tuple(math.inf if x > 1e300 else float(x) for x in d[i]) for i in range(n)]
    if fn == "diameter":
        if e["mode"] != "out" or not e.get("unconnected") or fx.directed:
            return None
        g = build(fx, weighted=wt, edges=simple_edges(fx, keep="min"))
        if g.numberOfEdges() == 0:
            return [0.0]
        dm = nk.distance.Diameter(g, algo=nk.distance.DiameterAlgo.EXACT)
        dm.run()
        return [float(dm.getDiameter()[0])]
    if fn == "eccentricity":
        if fx.directed or wt:
            return None
        g = build(fx, edges=simple_edges(fx))
        return [float(nk.distance.Eccentricity.getValue(g, v)[1]) for v in range(n)]
    if fn == "density":
        if e.get("loops") or not e.get("simple"):
            return None
        g = build(fx, edges=simple_edges(fx))
        return [nk.graphtools.density(g)]
    if fn in ("max_cliques", "clique_number"):
        # NetworKit 11 crashes (segmentation fault) in MaximalCliques when
        # the graph has parallel edges, so the two directions of a
        # directed pair are merged first.
        g = build(fx, edges=simple_edges(fx, undirected=True), directed=False)
        mc = nk.clique.MaximalCliques(g)
        mc.run()
        cl = [tuple(sorted(c)) for c in mc.getCliques()]
        cl += [(v,) for v in range(n) if g.degree(v) == 0]
        if fn == "clique_number":
            return [max((len(c) for c in cl), default=0)]
        return [c for c in cl if len(c) >= e.get("min_size", 0)]
    if fn == "modularity":
        if fx.directed or e.get("resolution", 1.0) != 1.0:
            return None
        g = build(fx, weighted=wt)
        labels = node_rule(e["partition"], n)
        part = nk.Partition(n)
        part.setUpperBound(4)
        for v in range(n):
            part[v] = int(labels[v])
        return [nk.community.Modularity().getQuality(part, g)]
    if fn == "cx_laplacian":
        if fx.directed:
            return None
        g = build(fx, weighted=wt)
        return scores(nk.centrality.LaplacianCentrality(g, normalized=e.get("normalized", True)))
    if fn == "spanning_weight":
        if e.get("maximum"):
            return None
        g = build(fx, weighted=True, edges=None if wt else
                  [(a, b, 1.0) for a, b in zip(fx.src, fx.tgt)])
        msf = nk.graph.KruskalMSF(g)
        msf.run()
        return [msf.getTotalWeight()]
    if fn == "assortativity_degree":
        if e.get("weighted") or fx.directed or e.get("loops") != "twice":
            return None
        g = build(fx)
        deg = [float(g.degree(v)) for v in range(n)]
        a = nk.correlation.Assortativity(g, deg)
        a.run()
        return [a.getCoefficient()]
    if fn == "bicomponents":
        if fx.directed:
            return None
        g = build(fx, edges=simple_edges(fx))
        bc = nk.components.BiconnectedComponents(g)
        bc.run()
        return [tuple(sorted(c)) for c in bc.getComponents()]
    if fn == "group" and e["measure"] in ("degree", "closeness"):
        # The standard group of bindings/resilience.py.
        group = list(range(min(3, max(1, n - 2))))
        mode = e.get("mode", "out")
        if mode == "all" and fx.directed:
            return None
        g = build(fx, weighted=wt, reverse=fx.directed and mode == "in")
        if e["measure"] == "degree":
            gd = nk.centrality.GroupDegree(g, k=len(group), countGroupNodes=False)
            return [gd.scoreOfGroup(group) / (n - len(group))]
        return [nk.centrality.GroupCloseness(g, k=len(group)).scoreOfGroup(group)]
    return None


if __name__ == "__main__":
    run(ORACLE, f"networkit {nk.__version__}", compute)
