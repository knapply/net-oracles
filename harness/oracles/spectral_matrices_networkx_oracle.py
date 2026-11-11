#!/usr/bin/env python3
"""Golden values from NetworkX (Hagberg, Schult, and Swart 2008) for graph
matrices and spectra (manifest/spectral_matrices.yaml).

Matrices: the functions of graph_matrices_networkx_oracle.py (adjacency,
Laplacian, normalized Laplacian, incidence, modularity). Spectra:
nx.adjacency_spectrum (real parts), nx.laplacian_spectrum,
nx.normalized_laplacian_spectrum and nx.modularity_spectrum, sorted
increasing. Fixtures with parallel edges are read as multigraphs.

    python3 oracles/spectral_matrices_networkx_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import networkx as nx
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_matrices_networkx_oracle as gmn  # noqa: E402
from common import (applies, fixture_names, load_area, load_fixture,  # noqa: E402
                    write_values, write_version)

ORACLE = "networkx"
CAPI = {"adjacency": ("gm_adjacency", {}), "laplacian": ("gm_laplacian", {}),
        "normalized_laplacian": ("gm_laplacian", {"normalized": True}),
        "incidence": ("gm_incidence", {}),
        "oriented_incidence": ("gm_incidence", {"oriented": True}),
        "modularity": ("gm_modularity", {})}


def compute(fx, spec):
    weighted = bool(spec.get("weighted"))
    if spec["fn"] == "matrix_operators":
        fn, extra = CAPI[spec["kind"]]
        return gmn.compute(fx, dict({"fn": fn, "weighted": weighted}, **extra))
    kind = spec["kind"]
    if fx.n == 0 or (kind == "modularity" and not fx.src):
        return []
    g = gmn.build(fx, weighted)
    w = "weight" if weighted else None
    if kind == "adjacency":
        values = np.real(nx.adjacency_spectrum(g, weight=w))
    elif kind == "laplacian":
        values = nx.laplacian_spectrum(g, weight=w)
    elif kind == "normalized_laplacian":
        values = nx.normalized_laplacian_spectrum(g, weight=w)
    else:
        values = np.real(nx.modularity_spectrum(g))
    return [float(x) for x in np.sort(values)]


def main() -> None:
    spec = load_area("spectral_matrices")
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
    print(f"networkx (spectral matrices): wrote {count} golden files")


if __name__ == "__main__":
    main()
