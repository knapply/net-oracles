---
title: "Disjoint paths"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Disjoint paths {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connectivity numbers. Concept id: `disjoint_paths`. 2 measures.

## Definition {#concept-definition}

Disjoint paths. Entries grouped here: Disjoint paths; Gb disjoint paths.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Disjoint paths](#disjoint_paths) | `disjoint_paths` | 3 |
| [Gb disjoint paths](#gb_disjoint_paths) | `gb_disjoint_paths` | 1 |

## Disjoint paths {#disjoint_paths}

Measure id: `disjoint_paths`. Original family: Components and connectivity.

**Definition.** Disjoint paths.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `edge_disjoint_paths; node_disjoint_paths` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `edge_disjoint_paths; vertex_disjoint_paths` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `BhandariKDisjointShortestPaths; SuurballeKDisjointShortestPaths` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_edge_disjoint_paths` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[len(list(nx.edge_disjoint_paths(G, 0, n - 1))), 1], 0 paths on NetworkXNoPath` |  |
| `conn_node_disjoint_paths` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[len(list(nx.node_disjoint_paths(G, 0, n - 1))), 1], 0 paths on NetworkXNoPath` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Gb disjoint paths {#gb_disjoint_paths}

Measure id: `gb_disjoint_paths`. Original family: Traversal, trees and DAGs.

**Definition.** Gb disjoint paths.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_edge_disjoint` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.edge_disjoint_paths(M, 0, n - 1)))` |  |
| `gb_node_disjoint` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.node_disjoint_paths(M, 0, n - 1)))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
