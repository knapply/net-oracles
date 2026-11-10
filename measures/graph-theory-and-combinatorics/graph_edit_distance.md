---
title: "Graph edit distance"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph edit distance {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `graph_edit_distance`. 2 measures.

## Definition {#concept-definition}

Graph edit distance. Entries grouped here: Ged Walk; Graph edit distance.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Ged Walk](#cat_ged_walk) | `cat_ged_walk` | 1 |
| [Graph edit distance](#ged) | `ged` | 2 |

## Ged Walk {#cat_ged_walk}

Measure id: `cat_ged_walk`. Original family: Paths and distances.

**Definition.** Ged Walk.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `GedWalk` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Graph edit distance {#ged}

Measure id: `ged`. Original family: Graph theory and combinatorics.

**Definition.** Graph edit distance.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `graph_edit_distance; optimal_edit_paths; optimize_edit_paths; optimize_graph_edit_distance` |  |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `ZhangShashaTreeEditDistance` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ged` | NetworkX | any | differs | loops | self\_loops | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2) with G2 = ged_pair(fixture)` | NetworkX's graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes |
| `ged_labels` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2, node_match = equal labels, edge_match = equal labels) with G2 = ged_pair(fixture)` | exact edit distance is exponential; networks of at most 10 nodes |
| `ged_node_labels` | NetworkX | any | differs | loops | self\_loops | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2, node_match = equal labels) with G2 = ged_pair(fixture)` | NetworkX's graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F003](../../findings.html#f003) | NetworkX | defect | graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
