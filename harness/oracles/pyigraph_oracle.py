#!/usr/bin/env python3
# oracle-env: pyigraph
# oracle-entries: pyigraph
"""Golden values from python-igraph (the `igraph` package on PyPI), the
Python binding of the same C core the R igraph oracle uses.

Its value is in separating binding conventions from the C core: each
variant repeats the R oracle's call (oracles/r_*.R) through the
Python binding, on the same graph built the same way, with undefined values written as
each area's markers, as the R oracle writes them. Where the
two disagree, the difference is in a binding's defaults or argument
handling, not in the core. Variants whose R call has no Python
counterpart are left out and noted in docs/drafts/convention_atlas.md.

    ~/oracle-envs/pyigraph/bin/python oracles/pyigraph_oracle.py
"""

from __future__ import annotations

import math

import igraph as ig
import numpy as np

from tool_common import node_rule, run

ORACLE = "pyigraph"


def build(fx, weighted=True):
    g = ig.Graph(n=fx.n, edges=list(zip(fx.src, fx.tgt)), directed=fx.directed)
    if fx.weighted and weighted:
        g.es["weight"] = list(fx.weights)
    return g


def simple_undirected(fx):
    g = build(fx, weighted=False)
    if g.is_directed():
        g.to_undirected(mode="collapse")
    g.simplify()
    return g


def flat(m):
    return [tuple(float(x) for x in row) for row in m]


def spectral_radius_noloops(fx):
    n = fx.n
    a = np.zeros((n, n))
    for u, v in zip(fx.src, fx.tgt):
        if u == v:
            continue
        a[u, v] += 1
        if not fx.directed:
            a[v, u] += 1
    return max(abs(np.linalg.eigvals(a))) if n else 0.0


def compute(variant: str, spec: dict, fx):
    e = spec["params"]
    n = fx.n
    d = fx.directed
    g = build(fx)
    gu = build(fx, weighted=False)
    w = "weight" if fx.weighted else None
    su = simple_undirected(fx)
    simple = build(fx, weighted=False).simplify()
    everything = max(n, 1)
    blocks = [int(x) for x in node_rule("blocks3", n)]
    v0 = list(range(n))
    table = {
        # core (r_core.R)
        "degree_all": lambda: g.degree(mode="all", loops=True),
        "degree_all_noloops": lambda: g.degree(mode="all", loops=False),
        "degree_out": lambda: g.degree(mode="out", loops=True),
        "degree_in": lambda: g.degree(mode="in", loops=True),
        "strength_all": lambda: g.strength(mode="all", loops=True, weights=w),
        "betweenness": lambda: gu.betweenness(directed=d),
        "betweenness_weighted": lambda: g.betweenness(directed=d, weights=w),
        "betweenness_weighted_strength": lambda: g.betweenness(
            directed=d, weights=[1 / x for x in g.es["weight"]]),
        "triad_census": lambda: list(g.triad_census()),
        # descriptive (r_descriptive.R)
        "reciprocity": lambda: [simple.reciprocity(mode="default")] if simple.ecount() else None,
        "reciprocity_ratio": lambda: [simple.reciprocity(mode="ratio")] if simple.ecount() else None,
        "transitivity": lambda: (None if sum(k * (k - 1) for k in su.degree()) == 0
                                 else [su.transitivity_undirected(mode="nan")]),
        "clustering": lambda: su.transitivity_local_undirected(mode="nan"),
        "clustering_zero": lambda: su.transitivity_local_undirected(mode="zero"),
        "average_clustering": lambda: [su.transitivity_avglocal_undirected(mode="nan")],
        "average_clustering_zero": lambda: [su.transitivity_avglocal_undirected(mode="zero")],
        "clustering_barrat": lambda: g.transitivity_local_undirected(mode="nan", weights=w),
        "distances": lambda: flat(gu.distances(mode="out")),
        "distances_in": lambda: flat(gu.distances(mode="in")),
        "distances_all": lambda: flat(gu.distances(mode="all")),
        "distances_weighted": lambda: flat(g.distances(mode="out", weights=w)),
        "distances_weighted_strength": lambda: flat(g.distances(
            mode="out", weights=[1 / x for x in g.es["weight"]])),
        "mean_distance": lambda: [gu.average_path_length(directed=True, unconn=True)],
        "mean_distance_all": lambda: [gu.average_path_length(directed=False, unconn=True)],
        "mean_distance_connected": lambda: [gu.average_path_length(directed=True, unconn=False)],
        "mean_distance_weighted": lambda: [g.average_path_length(directed=True, unconn=True,
                                                                 weights=w)],
        "diameter": lambda: [gu.diameter(directed=True, unconn=True)],
        "diameter_connected": lambda: [gu.diameter(directed=True, unconn=False)],
        "diameter_all": lambda: [gu.diameter(directed=False, unconn=True)],
        "diameter_weighted": lambda: [g.diameter(directed=True, unconn=True, weights=w)],
        "eccentricity": lambda: gu.eccentricity(mode="all"),
        "eccentricity_out": lambda: gu.eccentricity(mode="out"),
        "radius": lambda: [gu.radius(mode="all")],
        "reachability": lambda: [x - 1 for x in gu.neighborhood_size(order=everything, mode="out")],
        "reachability_in": lambda: [x - 1 for x in gu.neighborhood_size(order=everything,
                                                                         mode="in")],
        "reachability_all": lambda: [x - 1 for x in gu.neighborhood_size(order=everything,
                                                                          mode="all")],
        "cut_points": lambda: sorted(float(v) for v in su.articulation_points()),
        # topography (r_topography.R)
        "density": lambda: [g.density(loops=False)],
        "density_loops": lambda: [g.density(loops=True)],
        "components_weak": lambda: g.connected_components(mode="weak").membership,
        "components_strong": lambda: g.connected_components(mode="strong").membership,
        "closeness": lambda: g.closeness(mode="out", weights=None, normalized=False),
        "closeness_normalized": lambda: g.closeness(mode="out", weights=None, normalized=True),
        "closeness_in": lambda: g.closeness(mode="in", weights=None, normalized=True),
        "closeness_all": lambda: g.closeness(mode="all", weights=None, normalized=True),
        "closeness_weighted": lambda: g.closeness(mode="out", weights=w, normalized=True),
        "closeness_weighted_strength": lambda: g.closeness(
            mode="out", weights=[1 / x for x in g.es["weight"]], normalized=True),
        "harmonic": lambda: g.harmonic_centrality(mode="out", weights=None, normalized=False),
        "harmonic_normalized": lambda: g.harmonic_centrality(mode="out", weights=None,
                                                             normalized=True),
        "harmonic_in": lambda: g.harmonic_centrality(mode="in", weights=None, normalized=False),
        "harmonic_weighted": lambda: g.harmonic_centrality(mode="out", weights=w,
                                                           normalized=False),
        "eigenvector": lambda: g.eigenvector_centrality(directed=True, weights=None),
        "eigenvector_weighted": lambda: g.eigenvector_centrality(directed=True, weights=w),
        # spectral (r_spectral.R)
        "pagerank": lambda: g.pagerank(damping=0.85, weights=None),
        "pagerank_weighted": lambda: g.pagerank(damping=0.85, weights=w),
        "pagerank_personalized": lambda: g.personalized_pagerank(
            damping=0.85, weights=None, reset=node_rule("mod3plus1", n)),
        "pagerank_undirected": lambda: g.pagerank(damping=0.85, directed=False, weights=None),
        "hits_authorities": lambda: gu.authority_score(scale=True),
        "hits_hubs": lambda: gu.hub_score(scale=True),
        "assortativity_degree": lambda: [g.assortativity_degree(directed=True)],
        "assortativity_degree_undirected": lambda: [g.assortativity_degree(directed=False)],
        "assortativity_nominal": lambda: [g.assortativity_nominal(
            [v % 3 for v in v0], directed=True)],
        "assortativity_nominal_undirected": lambda: [g.assortativity_nominal(
            [v % 3 for v in v0], directed=False)],
        "assortativity_values": lambda: [g.assortativity([(7 * v) % 11 for v in v0],
                                                         directed=True)],
        "assortativity_values_in": lambda: [g.assortativity(
            [(7 * v) % 11 for v in v0], [(3 * v) % 5 for v in v0], directed=True)],
        "assortativity_covariance": lambda: [g.assortativity(
            [(7 * v) % 11 for v in v0], directed=True, normalized=False)],
        # subgroups (r_subgroups.R)
        "coreness_all": lambda: g.coreness(mode="all"),
        "coreness_out": lambda: g.coreness(mode="out"),
        "coreness_in": lambda: g.coreness(mode="in"),
        "max_cliques": lambda: [tuple(sorted(c)) for c in g.maximal_cliques(min=0)],
        "max_cliques_min3": lambda: [tuple(sorted(c)) for c in g.maximal_cliques(min=3)],
        "clique_number": lambda: [g.clique_number()],
        "modularity": lambda: [g.modularity(blocks, weights=None, resolution=1.0,
                                            directed=True)],
        "modularity_resolution": lambda: [g.modularity(blocks, weights=None, resolution=0.5,
                                                       directed=True)],
        "modularity_weighted": lambda: [g.modularity(blocks, weights=w, resolution=1.0,
                                                     directed=True)],
        # positions (r_positions.R)
        "constraint": lambda: gu.constraint(),
        "constraint_weighted": lambda: g.constraint(weights=w),
    }
    # Left out, with the R call they would repeat: alpha_centrality and
    # power_centrality (R binding only), assortativity_nominal(normalized =
    # False) (python-igraph 1.0.0 raises SystemError on the argument), and
    # eigenvector_centrality(directed = False) on a directed graph (raises
    # InternalError "Invalid mode"). See docs/drafts/convention_atlas.md.
    f = table.get(variant)
    if f is None:
        return None
    if variant.startswith("hits_") and not hasattr(gu, "authority_score"):
        return None
    out = f()
    if out is None:
        return None
    return [float(x) if not isinstance(x, tuple) else x for x in out]


if __name__ == "__main__":
    run(ORACLE, f"python-igraph {ig.__version__}", compute)
