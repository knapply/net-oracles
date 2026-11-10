---
title: "Chordal graphs"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Chordal graphs {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Chordal, perfect and special graph classes. Concept id: `chordal_graphs`. 4 measures.

## Definition {#concept-definition}

Chordal graphs. Entries grouped here: Chordal order; Chordal-graph tests and algorithms; Fill; St chordal.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Chordal order](#st_chordal_order) | `st_chordal_order` | 1 |
| [Chordal-graph tests and algorithms](#chordal) | `chordal` | 1 |
| [Fill](#st_fill) | `st_fill` | 1 |
| [St chordal](#st_chordal) | `st_chordal` | 3 |

## Chordal order {#st_chordal_order}

Measure id: `st_chordal_order`. Original family: Graph theory and combinatorics.

**Definition.** Chordal order.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_chordal_order` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.chordal_graph_cliques(nx.complete_to_chordal_graph(G)[0]): each clique sorted, in NetworkX's order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Chordal-graph tests and algorithms {#chordal}

Measure id: `chordal`. Original family: Graph theory and combinatorics.

**Definition.** Chordal-graph tests and algorithms.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `ChordalGraphIndependentSetFinder; ChordalGraphMaxCliqueFinder; ChordalGraphMinimalVertexSeparatorFinder; ChordalityInspector; CliqueMinimalSeparatorDecomposition; WeakChordalityInspector` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Fill {#st_fill}

Measure id: `st_fill`. Original family: Graph theory and combinatorics.

**Definition.** Fill.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_fill` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.complete_to_chordal_graph(G): [fill edges, alpha of each node]` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## St chordal {#st_chordal}

Measure id: `st_chordal`. Original family: Graph theory and combinatorics.

**Definition.** St chordal.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `chordal_graph_cliques; chordal_graph_treewidth; complete_to_chordal_graph; is_chordal` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `is_chordal` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `chordal_completion; is_chordal` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_chordal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `[nx.is_chordal(G), nx.chordal_graph_treewidth(G)]` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
