---
title: "Maximum-weight matching"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximum-weight matching {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `maximum_weight_matching`. 3 measures.

## Definition {#concept-definition}

A maximum-weight matching of an undirected network, as input edge positions (blossom algorithm).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Max weight matching](#max_weight_matching) | `max_weight_matching` | 5 |
| [Mwm](#st_mwm) | `st_mwm` | 1 |
| [Mwm pairs](#st_mwm_pairs) | `st_mwm_pairs` | 1 |

## References {#concept-references}

[edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Max weight matching {#max_weight_matching}

Measure id: `max_weight_matching`. Original family: Graph theory and combinatorics.

**Definition.** A maximum-weight matching of an undirected network, as input edge positions (blossom algorithm).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `max_weight_matching` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `max_cardinality_matching` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `max_weight_matching` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `DenseEdmondsMaximumCardinalityMatching; GreedyMaximumCardinalityMatching; GreedyWeightedMatching; KuhnMunkresMinimalWeightBipartitePerfectMatching; MaximumWeightBipartiteMatching; SparseEdmondsMaximumCardinalityMatching` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `maximum_weighted_matching` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `matching_max` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.max_weight_matching(G) on unit weights: (size, size, 1 if nx.is_matching)` |  |
| `matching_max_weight` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.max_weight_matching(G, weight = 'weight')` |  |
| `matching_max_weight_card` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.max_weight_matching(G, maxcardinality = True, weight = 'weight')` |  |

**References:** [edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Mwm {#st_mwm}

Measure id: `st_mwm`. Original family: Graph theory and combinatorics.

**Definition.** Mwm.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_mwm` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `the same totals and sizes from nx.max_weight_matching(G), (G, True), nx.min_weight_matching(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Mwm pairs {#st_mwm_pairs}

Measure id: `st_mwm_pairs`. Original family: Graph theory and combinatorics.

**Definition.** Mwm pairs.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_mwm_pairs` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted oriented pairs of max_weight_matching(G), then of (G, True), then of min_weight_matching(G), each list with its length first` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
