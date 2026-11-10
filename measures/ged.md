---
title: "Graph edit distance"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Graph edit distance

Family: Graph theory and combinatorics. Identifier: `ged`.

## Definition

Graph edit distance.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `graph_edit_distance; optimal_edit_paths; optimize_edit_paths; optimize_graph_edit_distance` |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `ZhangShashaTreeEditDistance` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ged` | NetworkX | any | differs | loops | self\_loops | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2) with G2 = ged_pair(fixture)` | NetworkX's graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes |
| `ged_labels` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2, node_match = equal labels, edge_match = equal labels) with G2 = ged_pair(fixture)` | exact edit distance is exponential; networks of at most 10 nodes |
| `ged_node_labels` | NetworkX | any | differs | loops | self\_loops | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2, node_match = equal labels) with G2 = ged_pair(fixture)` | NetworkX's graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F003](../findings.html#f003) | NetworkX | defect | graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht)
{% endraw %}
