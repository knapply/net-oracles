#!/usr/bin/env python3
# oracle-env: pyigraph
"""Golden values from python-igraph (Csardi and Nepusz 2006) for the graph
theory and combinatorics measures: completeness and cliques, the minimum
feedback arc set size (exact integer program), diversity, and power-law fits
(plfit). Inputs and encodings: ../bindings/graph_theory.py. igraph is run as a
black box.

    ~/oracle-envs/pyigraph/bin/python oracles/graph_theory_pyigraph_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import igraph as ig
except ImportError:  # the tool is not installed here
    print("python-igraph is not installed")
    sys.exit(3)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "pyigraph"
AREA = "graph_theory"
MEASURES = {}


def measure(*names):
    def wrap(f):
        for name in names:
            MEASURES[name] = f
        return f
    return wrap


def build(fx):
    g = ig.Graph(n=fx.n, edges=list(zip(fx.src, fx.tgt)), directed=fx.directed)
    if fx.weighted:
        g.es["weight"] = list(fx.weights)
    return g


def candidate(rule, n):
    return {"all": None, "even": [v for v in range(n) if v % 2 == 0],
            "first3": list(range(min(3, n)))}[rule]


@measure("gt_is_complete")
def _complete(fx, e):
    return [int(build(fx).is_complete())]


@measure("gt_is_clique_all", "gt_is_clique_even", "gt_is_clique_first3", "gt_is_clique_even_mutual")
def _clique(fx, e):
    return [int(build(fx).is_clique(candidate(e["candidate"], fx.n), directed=bool(e.get("directed"))))]


@measure("gt_fas_size")
def _fas(fx, e):
    # The exact (integer programming) method; the keyword was renamed from
    # `algo` to `method` between python-igraph releases.
    g = build(fx)
    try:
        return [len(g.feedback_arc_set(method="ip"))]
    except TypeError:
        return [len(g.feedback_arc_set(algo="ip"))]


def degrees(fx):
    d = [0] * fx.n
    for a, b in zip(fx.src, fx.tgt):
        d[a] += 1
        d[b] += 1
    return d


def below_two_edges_undefined(fx, values):
    """The normalized entropy of fewer than two edge shares is 0 / 0. igraph
    fills it by convention (1.0 for every node of the unweighted call, 0.0 for
    one edge of the weighted call, NaN for none); the engine leaves it NaN, so
    these nodes carry no igraph value and are written as NaN."""
    return [float("nan") if d < 2 else float(x) for x, d in zip(values, degrees(fx))]


@measure("gt_diversity")
def _diversity(fx, e):
    return below_two_edges_undefined(fx, build(fx).diversity(weights=None))


@measure("gt_diversity_weighted")
def _diversity_weighted(fx, e):
    return below_two_edges_undefined(fx, build(fx).diversity(weights="weight"))


def fit(fx, xmin, method):
    positive = [x for x in degrees(fx) if x >= 1]
    if len({x for x in positive if x >= max(xmin or 1, 1)}) < 2:
        return None
    return ig.power_law_fit(positive, xmin=xmin, method=method)


def plfit_runner(attribute):
    def run(fx, e):
        xmin = e.get("xmin")
        method = "discrete" if e.get("discrete", True) else "continuous"
        result = fit(fx, float(xmin) if xmin else None, method)
        return [-1] if result is None else [float(getattr(result, attribute))]
    return run


# igraph applies the finite-size correction alpha (n - 1) / n + 1 / n when the data
# vector has fewer than 50 entries, so alpha and the log-likelihood are compared
# with the engine's `small_sample_below: 50` variants.
measure("gt_plfit_alpha_small", "gt_plfit_alpha_continuous_small")(plfit_runner("alpha"))
measure("gt_plfit_loglik_small")(plfit_runner("L"))
measure("gt_plfit_distance")(plfit_runner("D"))
measure("gt_plfit_xmin")(plfit_runner("xmin"))


def main() -> None:
    spec = load_area(AREA)
    count = 0
    for name in fixture_names():
        fx = load_fixture(name)
        for variant, v in spec.items():
            ospec = v["oracles"].get(ORACLE)
            if ospec is None or not applies(v, fx) or name in ospec.get("undefined_on", []):
                continue
            if set(fx.tags) & set(ospec.get("undefined_when", [])):
                continue
            f = MEASURES.get(variant)
            if f is None:
                continue
            write_values(ORACLE, name, variant, f(fx, v["params"]))
            count += 1
    print(f"python-igraph {ig.__version__} ({AREA}): wrote {count} golden files")
    write_version(ORACLE, f"python-igraph {ig.__version__}")


if __name__ == "__main__":
    main()
