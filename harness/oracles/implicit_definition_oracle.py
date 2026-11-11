#!/usr/bin/env python3
"""Golden values from the definitions for manifest/implicit.yaml (encodings
in bindings/implicit.py, case tables and node numbering in
derived/implicit.py): each family's edge set from its defining rule on the
node pairs or words.

    python3 oracles/implicit_definition_oracle.py
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (DEFINITION_VERSION, applies, fixture_names, load_area,  # noqa: E402
                    load_fixture, write_values, write_version)
from derived import implicit as D  # noqa: E402

ORACLE = "definition"


def pairs(n, directed, joined):
    return D.normalize(((a, b) for a in range(n) for b in range(n)
                        if a != b and joined(a, b)), directed)


def build(family, directed, case):
    """(node count, edges) from the defining rule."""
    if family == "complete_bipartite":
        left, right = case
        return left + right, pairs(left + right, directed, lambda a, b: a < left <= b)
    if family == "complete_multipartite":
        part = [p for p, size in enumerate(case[0]) for _ in range(size)]
        return len(part), pairs(len(part), False, lambda a, b: part[a] != part[b])
    if family == "star":
        return case[0] + 1, pairs(case[0] + 1, False, lambda a, b: a == 0)
    if family == "path":
        n = case[0]
        return n, pairs(n, directed, lambda a, b: b == a + 1 or (not directed and a == b + 1))
    if family == "wheel":
        n = case[0]
        rim = lambda a, b: (abs(a - b) == 1 or {a, b} == {1, n - 1})  # noqa: E731
        return n, pairs(n, False, lambda a, b: a == 0 or b == 0 or rim(a, b))
    if family == "hypercube":
        d = case[0]
        return 1 << d, pairs(1 << d, False, lambda a, b: bin(a ^ b).count("1") == 1)
    if family == "circulant":
        n, offsets = case
        steps = {o % n for o in offsets} | {(-o) % n for o in offsets}
        return n, pairs(n, False, lambda a, b: (a - b) % n in steps)
    if family == "de_bruijn":
        k, order = case
        arcs = [(D.debruijn_id(w, k), D.debruijn_id(w[1:] + (c,), k))
                for w in itertools.product(range(k), repeat=order) for c in range(k)]
        return k ** order, D.normalize(arcs, True)
    if family == "kautz":
        m, order = case
        words = [w for w in itertools.product(range(m + 1), repeat=order + 1)
                 if all(a != b for a, b in zip(w, w[1:]))]
        arcs = [(D.kautz_id(w, m), D.kautz_id(w[1:] + (c,), m))
                for w in words for c in range(m + 1) if c != w[-1]]
        return len(words), D.normalize(arcs, True)
    raise ValueError(family)


def compute(engine):
    fn = engine["fn"]
    if fn == "implicit_family":
        out = []
        for case in D.cases(engine["family"]):
            out += D.pack(*build(engine["family"], bool(engine.get("directed")), case))
        return out
    if fn == "implicit_q0":
        return D.pack(1, [])  # the empty bit string: one node, no edge
    if fn == "implicit_invalid":
        return [1 for _ in D.INVALID]  # each is outside the documented domain
    raise ValueError(fn)


def main() -> None:
    spec = load_area("implicit")
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
    write_version(ORACLE, DEFINITION_VERSION)
    print(f"definition (implicit): wrote {count} golden files")


if __name__ == "__main__":
    main()
