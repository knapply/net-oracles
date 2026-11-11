#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for graph
matrices and the Fiedler vector (see ../bindings/graph_matrices.py for the
encodings). Each fixture is read as a Graph or DiGraph, or a multigraph
when it has parallel edges; weighted variants pass weight="weight" and the
others weight=None (the Bethe Hessian always reads "weight", so the
unweighted variant builds the graph without weights).

    python3 oracles/graph_matrices_networkx_oracle.py
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
GAP = 1e-6
# Entries at most this fraction of the largest |entry| count as zero when
# the Fiedler vector's sign is chosen (the engine's SIGN_TIE).
SIGN_TIE = 1e-9


def signed(v):
    """Unit vector whose first entry above SIGN_TIE times the largest
    |entry| is negative."""
    x = v / np.linalg.norm(v)
    top = np.abs(x).max()
    first = next((e for e in x if abs(e) > SIGN_TIE * top), 0.0)
    return -x if first > 0 else x
# Fixtures on which NetworkX's normalized tracemin_pcg never converges (its
# loop has no iteration cap), declared undefined in the manifest.
NO_CONVERGENCE = {"gnp_dir_dense", "gnp_und_dense", "real_weights_dir", "weighted_dir"}


def build(fx, weighted=True, edge_out=None):
    pairs = list(zip(fx.src, fx.tgt))
    keys = {p if fx.directed else frozenset(p) for p in pairs}
    multi = len(keys) < len(pairs)
    cls = {(True, True): nx.MultiDiGraph, (True, False): nx.DiGraph,
           (False, True): nx.MultiGraph, (False, False): nx.Graph}[(fx.directed, multi)]
    g = cls()
    g.add_nodes_from(range(fx.n))
    for i, (a, b) in enumerate(pairs):
        if weighted and fx.weighted:
            k = g.add_edge(a, b, weight=fx.weights[i])
        else:
            k = g.add_edge(a, b)
        if edge_out is not None:
            edge_out.append((a, b, k) if multi else (a, b))
    return g


def enc(M):
    return [-999.0 if np.isnan(x) else float(x) for x in np.asarray(M, dtype=float).ravel()]


def compute(fx, e):
    fn = e["fn"]
    w = "weight" if e.get("weighted") else None
    edges = []
    G = build(fx, bool(e.get("weighted")), edges)
    if fn == "gm_adjacency":
        return enc(nx.adjacency_matrix(G, weight=w).toarray())
    if fn == "gm_laplacian":
        f = nx.normalized_laplacian_matrix if e.get("normalized") else nx.laplacian_matrix
        return enc(f(G, weight=w).toarray())
    if fn == "gm_incidence":
        # Columns in the fixture's edge order (the engine's).
        return enc(nx.incidence_matrix(G, edgelist=edges, oriented=bool(e.get("oriented")),
                                       weight=w).toarray())
    if fn == "gm_bethe_hessian":
        if G.number_of_edges() == 0:
            return [-999.0]
        return enc(nx.bethe_hessian_matrix(G).toarray())
    if fn == "gm_modularity":
        with np.errstate(divide="ignore", invalid="ignore"):
            f = nx.directed_modularity_matrix if fx.directed else nx.modularity_matrix
            return enc(f(G, weight=w))
    if fn == "gm_fiedler":
        if fx.n < 2:
            return [-999.0]
        norm = bool(e.get("normalized"))
        # algebraic_connectivity and fiedler_vector are not implemented for
        # directed graphs; NetworkX's own preprocessing (which
        # spectral_ordering applies to them) gives the undirected graph
        # whose Laplacian NetworkX reads (spectral_ordering reads the
        # attribute "weight" that the preprocessing writes).
        prep = nx.linalg.algebraicconnectivity._preprocess_graph
        if fx.directed:
            G, w = prep(G, w), "weight"
        if e.get("output", "value") == "value":
            return [nx.algebraic_connectivity(G, weight=w, normalized=norm, tol=1e-10,
                                              method="tracemin_lu")]
        P = prep(G, w)
        if not nx.is_connected(P):
            return [-999.0]
        L = nx.laplacian_matrix(P).toarray()
        if norm:
            h = 1 / np.sqrt(np.diag(L))
            L = h[:, None] * L * h[None, :]
        vals, vecs = np.linalg.eigh(L)
        if fx.n > 2 and not vals[2] - vals[1] > GAP * max(1.0, abs(vals[2])):
            return [-999.0]
        x = np.asarray(nx.fiedler_vector(G, weight=w, normalized=norm))
        # The vector is defined up to sign. NetworkX makes its first entry
        # negative, which leaves the sign to rounding when that entry is
        # zero; the engine's rule (first entry above 1e-9 of the largest
        # negative) is applied to the exact eigenvector, and NetworkX's
        # vector (accurate to about 2e-6) takes the sign that agrees with it.
        if float(np.dot(x, signed(vecs[:, 1]))) < 0:
            x = -x
        return list(x)
    if fn == "gm_class_matrix":
        return enc(nx.attr_matrix(G, edge_attr="weight" if e.get("weighted") else None,
                                  node_attr=lambda v: v % 3, rc_order=[0, 1, 2]))
    if fn == "gm_aperiodic":
        if fx.n == 0 or not nx.is_strongly_connected(G):
            return [-999.0]
        return [1.0 if nx.is_aperiodic(G) else 0.0]
    raise ValueError(fn)


def main() -> None:
    spec = load_area("graph_matrices")
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            if ORACLE not in v["oracles"] or not applies(v, fx):
                continue
            if fx.name in NO_CONVERGENCE and v["params"].get("output") == "vector" \
                    and v["params"].get("normalized"):
                continue
            if "multi_edges" in fx.tags and v["params"]["fn"] in ("gm_bethe_hessian",
                                                                 "gm_modularity"):
                continue  # not implemented for multigraphs (declared undefined)
            write_values(ORACLE, name, variant, compute(fx, v["params"]))
            count += 1
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (graph_matrices): wrote {count} golden files")


if __name__ == "__main__":
    main()
