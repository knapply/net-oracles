---
title: "Global minimum cut"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Global minimum cut {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Cuts and separators. Concept id: `global_min_cut`. 3 measures.

## Definition {#concept-definition}

Minimum cut between a set of sources and a set of sinks: its capacity, the source side and the crossing edges.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Cut measures](#cut_measures) | `cut_measures` | 1 |
| [Min cut](#min_cut) | `min_cut` | 7 |
| [Stoer wagner](#gb_stoer_wagner) | `gb_stoer_wagner` | 1 |

## References {#concept-references}

[dinic1970algorithm](../../references.html#dinic1970algorithm), [ford1956maximal](../../references.html#ford1956maximal), [ford1962flows](../../references.html#ford1962flows), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Cut measures {#cut_measures}

Measure id: `cut_measures`. Original family: Components and connectivity.

**Definition.** Cut measures.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cut_measures` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.cut_size, volume, normalized_cut_size, conductance, edge_expansion, mixing_expansion, node_expansion, boundary_expansion with S = even nodes, T = the rest` |  |
| `cut_measures_overlap` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `the same functions with T = nodes v % 3 == 1` |  |
| `cut_measures_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `the same functions with weight = 'weight'` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min cut {#min_cut}

Measure id: `min_cut`. Original family: Components and connectivity.

**Definition.** Minimum cut between a set of sources and a set of sinks: its capacity, the source side and the crossing edges.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `minimum_cut; minimum_cut_value; stoer_wagner` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `min_cut` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `mincut; mincut_value; st_mincut` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `min_cut; min_st_cut` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `stoer_wagner_min_cut` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `StoerWagnerMinimumCut` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `stoer_wagner_min_cut` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_min_cut_largest` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.minimum_cut(G, 0, n - 1)[1][0] as 1/0 flags` |  |
| `flow_min_cut_largest_multi` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.minimum_cut(H, 'S', 'T')[1][0] without S, as 1/0 flags` |  |
| `flow_min_cut_smallest` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nodes reachable from 0 over arcs with flow < capacity in nx.flow.edmonds_karp(G, 0, n - 1)` |  |

**References:** [dinic1970algorithm](../../references.html#dinic1970algorithm), [ford1956maximal](../../references.html#ford1956maximal), [ford1962flows](../../references.html#ford1962flows), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Stoer wagner {#gb_stoer_wagner}

Measure id: `gb_stoer_wagner`. Original family: Traversal, trees and DAGs.

**Definition.** Stoer wagner.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_stoer_wagner` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.stoer_wagner(nx.Graph(M))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
