---
title: "Perfect graphs"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Perfect graphs {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Chordal, perfect and special graph classes. Concept id: `perfect_graph`. 2 measures.

## Definition {#concept-definition}

Perfect graphs. Entries grouped here: Perfect-graph (Berge) tests; Perfect.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Perfect-graph (Berge) tests](#perfect_graph) | `perfect_graph` | 1 |
| [Perfect](#st_perfect) | `st_perfect` | 1 |

## Perfect-graph (Berge) tests {#perfect_graph}

Measure id: `perfect_graph`. Original family: Graph theory and combinatorics.

**Definition.** Perfect-graph (Berge) tests.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `BergeGraphInspector` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Perfect {#st_perfect}

Measure id: `st_perfect`. Original family: Graph theory and combinatorics.

**Definition.** Perfect.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `is_perfect_graph` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_perfect` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.is_perfect_graph(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
