#!/usr/bin/env python3
# oracle-env: networkit
"""Golden values from NetworKit (Staudt, Sazonovs and Meyerhenke 2016) for the
greedy b-matching: BSuitorMatcher, a 1/2-approximate maximum-weight
b-matching by the b-Suitor algorithm (Khan et al. 2016), which matches the
greedy choice by decreasing weight when no two weights tie. The weight is
that of the matched edges, and the matching is checked with `isProper`.
Capacity b(v) = 1 + v % 3 (../bindings/bmatching.py). NetworKit is run as a
black box.

    ~/oracle-envs/networkit/bin/python oracles/bmatching_networkit_oracle.py
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import networkit as nk
except ImportError:  # the tool is not installed here
    print("networkit is not installed")
    sys.exit(3)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (applies, fixture_names, load_area, load_fixture, write_values,  # noqa: E402
                    write_version)

ORACLE = "networkit"
AREA = "bmatching"


def b_suitor_weight(fx):
    g = nk.Graph(fx.n, weighted=True, directed=False)
    for i, (a, b) in enumerate(zip(fx.src, fx.tgt)):
        g.addEdge(a, b, fx.weights[i] if fx.weights else 1.0)
    matcher = nk.matching.BSuitorMatcher(g, [1 + v % 3 for v in range(fx.n)])
    matcher.run()
    m = matcher.getBMatching()
    assert m.isProper()
    return float(sum(w for a, b, w in g.iterEdgesWeights() if m.areMatched(a, b)))


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
            write_values(ORACLE, name, variant, [b_suitor_weight(fx)])
            count += 1
    print(f"networkit {nk.__version__} ({AREA}): wrote {count} golden files")
    write_version(ORACLE, f"networkit {nk.__version__}")


if __name__ == "__main__":
    main()
