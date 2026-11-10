---
title: "Prufer sequences"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Prufer sequences {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `prufer_sequence`. 2 measures.

## Definition {#concept-definition}

Prufer sequences. Entries grouped here: From prufer; Prufer.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [From prufer](#nxs_from_prufer) | `nxs_from_prufer` | 4 |
| [Prufer](#nxs_prufer) | `nxs_prufer` | 2 |

## From prufer {#nxs_from_prufer}

Measure id: `nxs_from_prufer`. Original family: Graph theory and combinatorics.

**Definition.** From prufer.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `make_from_prufer` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Prufer` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `PruferTreeGenerator` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_from_prufer` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[tuple(T.adj[v]) for v in T] for T = nx.from_prufer_sequence(seq): the neighbour order of each node, which records the order of adding edges` |  |
| `nxs_from_prufer_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted (min, max) pairs of nx.from_prufer_sequence(seq).edges()` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Prufer {#nxs_prufer}

Measure id: `nxs_prufer`. Original family: Graph theory and combinatorics.

**Definition.** Prufer.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `to_prufer` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_prufer` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.to_prufer_sequence(T) (nothing below three nodes)` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
