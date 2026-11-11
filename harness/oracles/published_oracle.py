#!/usr/bin/env python3
"""Golden values transcribed from the literature: numbers that were printed
in a paper or textbook table for a classic network, as an oracle that no
software computed for this repository.

Each table below names its source. Values are as printed (usually three or
four decimals), so the manifest gives this oracle a tolerance of the
printed precision. A table may cover only some nodes (`None` = not
printed; written as NA and skipped by `partial: true` in the manifest).

Provenance caveat: the transcriptions were made from memory of the sources
and secondary reproductions, then cross-checked against the exact
definition oracle; a printed value that disagreed was re-examined rather
than adjusted. Re-verify each against the cited page before quoting it.

    python3 oracles/published_oracle.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import write_values, write_version  # noqa: E402

ORACLE = "published"
N = None

# Krackhardt (1990), "Assessing the political landscape", kite network of
# ten people, in order Andre, Beverly, Carol, Diane, Ed, Fernando, Garth,
# Heather, Ike, Jane; centrality table as reproduced in textbooks.
KITE_DEGREE = [4, 4, 3, 6, 3, 5, 5, 3, 2, 1]
KITE_CLOSENESS = [0.529, 0.529, 0.500, 0.600, 0.500, 0.643, 0.643, 0.600, 0.429, 0.310]
KITE_BETWEENNESS = [0.023, 0.023, 0.000, 0.102, 0.000, 0.231, 0.231, 0.389, 0.222, 0.000]

# Zachary (1977) karate club, nodes numbered 1..34 in the paper; values for
# the best-known nodes (as tabulated in many network textbooks and in
# Brandes 2001 / Newman 2010 examples).
def karate(table):
    v = [N] * 34
    for node, x in table.items():
        v[node - 1] = x
    return v

KARATE_DEGREE = karate({1: 16, 2: 9, 3: 10, 4: 6, 33: 12, 34: 17})
KARATE_BETWEENNESS = karate({1: 0.4376, 3: 0.1437, 33: 0.1452, 34: 0.3041, 32: 0.1383})
KARATE_CLOSENESS = karate({1: 0.5690, 3: 0.5593, 34: 0.5500, 32: 0.5410})

# Padgett and Ansell (1993) Florentine marriage network (Breiger and
# Pattison 1986 coding, 15 families); node order of the fixture: the Medici
# is index 1, Guadagni 12, Albizzi 8 (see fixtures.py). Normalized
# betweenness and closeness as tabulated in Jackson (2008) / Newman (2010).
def florentine(table):
    v = [N] * 15
    for idx, x in table.items():
        v[idx] = x
    return v

FLO_DEGREE = florentine({1: 6})
FLO_BETWEENNESS = florentine({1: 0.522, 12: 0.255, 8: 0.212})
FLO_CLOSENESS = florentine({1: 0.560})

# Freeman (1979), "Centrality in social networks: conceptual clarification":
# the star maximizes every centralization index (1) and the complete graph
# minimizes it (0). Fixtures: star8 and complete6.
FREEMAN = {"degree": {"star8": 1.0, "complete6": 0.0},
           "betweenness": {"star8": 1.0, "complete6": 0.0},
           "closeness": {"star8": 1.0, "complete6": 0.0}}

TABLES = {
    # (fixture, variant): values
    ("kite", "degree_all"): KITE_DEGREE,
    ("kite", "closeness_normalized"): KITE_CLOSENESS,
    ("kite", "betweenness_normalized"): KITE_BETWEENNESS,
    ("karate", "degree_all"): KARATE_DEGREE,
    ("karate", "betweenness_normalized"): KARATE_BETWEENNESS,
    ("karate", "closeness_normalized"): KARATE_CLOSENESS,
    ("karate", "transitivity"): [0.2557],
    ("karate", "diameter"): [5],
    ("karate", "clique_number"): [5],
    ("karate", "density"): [0.1390],
    ("kite", "diameter"): [4],
    ("kite", "clique_number"): [4],
    ("florentine", "degree_all"): FLO_DEGREE,
    ("florentine", "betweenness_normalized"): FLO_BETWEENNESS,
    ("florentine", "closeness_normalized"): FLO_CLOSENESS,
}
for fx in ("star8", "complete6"):
    TABLES[(fx, "centralization_degree_sna")] = [FREEMAN["degree"][fx]]
    TABLES[(fx, "centralization_betweenness")] = [FREEMAN["betweenness"][fx]]
    TABLES[(fx, "centralization_closeness")] = [FREEMAN["closeness"][fx]]


def main() -> None:
    for (fx, variant), vals in TABLES.items():
        # None (not printed in the source) is written as nan and skipped by `partial`.
        write_values(ORACLE, fx, variant, [math.nan if x is None else x for x in vals])
    write_version(ORACLE, "published tables (Krackhardt 1990; Zachary 1977; "
                          "Padgett and Ansell 1993; Freeman 1979)")
    print(f"published: wrote {len(TABLES)} golden files")


if __name__ == "__main__":
    main()
