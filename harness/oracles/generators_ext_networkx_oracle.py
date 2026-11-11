#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for
manifest/generators_ext.yaml (encodings in bindings/generators_ext.py, case
tables and node numbering in derived/generators_ext.py): the named graph
generators, Pruefer coding, graphicality tests, complement and the four graph
products. The lattices label nodes by pairs; the integer is the rank of the
pair in lexicographic order.

    python3 oracles/generators_ext_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)
from derived import generators_ext as D  # noqa: E402

ORACLE = "networkx"


def relabel_ranks(g):
    """Integer graph with the nodes numbered by the rank of their label."""
    order = {node: i for i, node in enumerate(sorted(g.nodes))}
    return g.number_of_nodes(), [(order[a], order[b]) for a, b in g.edges()]


def from_graph(g, directed=False):
    nodes, edges = relabel_ranks(g)
    return D.pack(nodes, D.normalize(edges, directed))


def nx_graph(n, edges, directed):
    g = nx.DiGraph() if directed else nx.Graph()
    g.add_nodes_from(range(n))
    g.add_edges_from(edges)
    return g


def product(op, first, second):
    (na, ea, da), (nb, eb, db) = D.graph(first), D.graph(second)
    g, h = nx_graph(na, ea, da), nx_graph(nb, eb, db)
    f = {0: nx.cartesian_product, 1: nx.tensor_product, 2: nx.strong_product,
         3: nx.lexicographic_product}[op]
    p = f(g, h)
    edges = [(a[0] * nb + a[1], b[0] * nb + b[1]) for a, b in p.edges()]
    return D.pack(na * nb, D.normalize(edges, da))


def compute(engine):
    fn, family = engine["fn"], engine.get("family")
    out = []
    if family == "barbell":
        for m1, m2 in D.BARBELL:
            out += from_graph(nx.barbell_graph(m1, m2))
    elif family == "lollipop":
        for m, n in D.LOLLIPOP:
            out += from_graph(nx.lollipop_graph(m, n))
    elif family == "generalized_petersen":
        for n, k in D.PETERSEN:
            out += from_graph(nx.generalized_petersen_graph(n, k))
    elif family == "turan":
        for n, r in D.TURAN:
            out += from_graph(nx.turan_graph(n, r))
    elif family == "lcf":
        for n, shifts, repeats in D.LCF:
            out += from_graph(nx.LCF_graph(n, shifts, repeats))
    elif family == "dgm":
        for g in D.DGM:
            out += from_graph(nx.dorogovtsev_goltsev_mendes_graph(g))
    elif family == "hexagonal":
        for m, n, periodic in D.HEXAGONAL:
            out += from_graph(nx.hexagonal_lattice_graph(m, n, periodic=periodic,
                                                         with_positions=False))
    elif family == "triangular":
        for m, n, periodic in D.TRIANGULAR:
            out += from_graph(nx.triangular_lattice_graph(m, n, periodic=periodic,
                                                          with_positions=False))
    elif family == "prufer_decode":
        for sequence in D.PRUFER_DECODE:
            out += from_graph(nx.from_prufer_sequence(sequence))
    elif family == "prufer_encode":
        for sequence in D.PRUFER_ENCODE:
            sequence = list(nx.to_prufer_sequence(nx.from_prufer_sequence(sequence)))
            out += [(len(sequence),)] + [(int(v),) for v in sequence]
    elif family == "graphical":
        for sequence in D.GRAPHICAL:
            eg, hh = nx.is_graphical(sequence, "eg"), nx.is_graphical(sequence, "hh")
            assert eg == hh
            out.append((int(eg),))
    elif family == "digraphical":
        for inn, outd in D.DIGRAPHICAL:
            out.append((int(nx.is_digraphical(inn, outd)),))
    elif family == "complement":
        for name, loops in D.COMPLEMENT:
            if bool(loops) != bool(engine.get("loops", False)):
                continue
            n, edges, directed = D.graph(name)
            out += from_graph(nx.complement(nx_graph(n, edges, directed)), directed)
    elif family == "product":
        for first, second in D.PRODUCT_PAIRS:
            if D.graph(first)[2] == D.graph(second)[2]:
                out += product(engine["op"], first, second)
    else:
        raise ValueError(family or fn)
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
    write_version(ORACLE, f"networkx {nx.__version__}")
    print(f"networkx (generators_ext): wrote {count} golden files")


if __name__ == "__main__":
    main()
