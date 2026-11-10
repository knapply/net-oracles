---
title: "Compare partitions"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Compare partitions

Family: Communities. Identifier: `compare_partitions`.

## Definition

Compare partitions.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ≠ checked, differs by convention | `compare; split_join_distance` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `compare_communities; split_join_distance` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `AdjustedRandIndex; AdjustedRandMeasure; GraphStructuralRandMeasure; JaccardMeasure; NMIDistance; NodeStructuralRandMeasure; OverlappingNMIDistance; compareCommunities` | API listing |
| [cdlib](../tools/cdlib.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `compare_adjusted_rand` | igraph (R) | any | differs | two\_nodes, (no value) null\_graph, (no value) one\_node | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'adjusted.rand')` | on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0; the reference reports 1, the value for every other pair of identical partitions (as scikit-learn's adjusted\_rand\_score() does), and igraph NaN igraph raises an error for fewer than two nodes; the reference reports NaN. |
| `compare_adjusted_rand` | cdlib | any | differs |  | defaults | abs 1e-14, rel 1e-12 | `cdlib.evaluation.adjusted_rand_index(blocks, stripes)` | For partitions of one element cdlib (through scikit-learn) returns 1.0; the adjusted Rand index is 0/0 there, and the reference, like igraph, reports it undefined. |
| `compare_ami` | cdlib | any | agrees |  |  | abs 1e-12, rel 1e-09 | `cdlib.evaluation.adjusted_mutual_information(blocks, stripes)` |  |
| `compare_nmi` | igraph (R) | any | no-value-on-some-inputs | (no value) null\_graph | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'nmi')` | Two partitions of no nodes: the reference reports undefined, igraph a value. |
| `compare_nmi` | cdlib | any | agrees |  |  | abs 1e-14, rel 1e-12 | `cdlib.evaluation.normalized_mutual_information(blocks, stripes)` |  |
| `compare_rand` | igraph (R) | any | no-value-on-some-inputs |  | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'rand')` | igraph raises an error for fewer than two nodes; the reference reports NaN. |
| `compare_rand` | cdlib | any | agrees |  |  | abs 1e-14, rel 1e-12 | `cdlib.evaluation.rand_index(blocks, stripes)` |  |
| `compare_split_join` | igraph (R) | any | no-value-on-some-inputs | (no value) null\_graph | defaults | abs 0, rel 0 | `sum(split_join_distance(a, b))` | Two partitions of no nodes: the reference reports undefined, igraph a value. |
| `compare_vi` | igraph (R) | any | no-value-on-some-inputs | (no value) null\_graph | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'vi')` | Two partitions of no nodes: the reference reports undefined, igraph a value. |
| `compare_vi` | cdlib | any | agrees |  |  | abs 1e-14, rel 1e-12 | `cdlib.evaluation.variation_of_information(blocks, stripes)` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F036](../findings.html#f036) | igraph (R) | convention | Adjusted Rand index is NaN on all-singleton partitions |
| [F037](../findings.html#f037) | cdlib | convention | Adjusted Rand index is 1 on degenerate partitions |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [staudt2016networkit](../references.html#staudt2016networkit), [tool_cdlib](../references.html#tool_cdlib)
{% endraw %}
