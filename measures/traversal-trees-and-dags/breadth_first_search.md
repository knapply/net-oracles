---
title: "Breadth-first search"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Breadth-first search {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Traversal and orderings. Concept id: `breadth_first_search`. 8 measures.

## Definition {#concept-definition}

Levels, parents and counts of a breadth-first search from one node (direction-optimizing).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Beam](#trav_beam) | `trav_beam` | 1 |
| [Bfs edges](#trav_bfs_edges) | `trav_bfs_edges` | 9 |
| [Bfs iterator](#cat_bfs_iterator) | `cat_bfs_iterator` | 1 |
| [Bfs labeled](#trav_bfs_labeled) | `trav_bfs_labeled` | 1 |
| [Bfs layers](#trav_bfs_layers) | `trav_bfs_layers` | 2 |
| [Edge bfs](#trav_edge_bfs) | `trav_edge_bfs` | 1 |
| [Random BFS](#cat_bfs_random) | `cat_bfs_random` | 1 |
| [Reverse BFS](#cat_bfs_reverse) | `cat_bfs_reverse` | 1 |

## References {#concept-references}

[luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [schank2005approximating](../../references.html#schank2005approximating), [staudt2016networkit](../../references.html#staudt2016networkit)

## Beam {#trav_beam}

Measure id: `trav_beam`. Original family: Traversal, trees and DAGs.

**Definition.** Beam.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `bfs_beam_edges` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_beam` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_beam_edges(M, 0, lambda v: (v * 7) % 5, 2)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Bfs edges {#trav_bfs_edges}

Measure id: `trav_bfs_edges`. Original family: Traversal, trees and DAGs.

**Definition.** Bfs edges.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `bfs_edges; bfs_predecessors; bfs_successors; bfs_tree; edge_bfs` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `bfs` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `bfs; bfsiter` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `bfs_search` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `BFS` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `bfs_predecessors; bfs_search; bfs_successors; digraph_bfs_search; graph_bfs_search` | API listing |
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `breadth_first_search` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `BreadthFirstIterator; LexBreadthFirstIterator` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `breadth_first_search` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_bfs_edges` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_edges(M, 0)` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Bfs iterator {#cat_bfs_iterator}

Measure id: `cat_bfs_iterator`. Original family: Paths and distances.

**Definition.** Bfs iterator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `bfs_iterator` | API listing |

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Bfs labeled {#trav_bfs_labeled}

Measure id: `trav_bfs_labeled`. Original family: Traversal, trees and DAGs.

**Definition.** Bfs labeled.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `bfs_labeled_edges` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_bfs_labeled` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_labeled_edges(M, [0])` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Bfs layers {#trav_bfs_layers}

Measure id: `trav_bfs_layers`. Original family: Traversal, trees and DAGs.

**Definition.** Levels, parents and counts of a breadth-first search from one node (direction-optimizing).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `bfs_layers` |  |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `bfs_layers; digraph_bfs_layers; graph_bfs_layers` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_bfs_layers` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_layers(M, [0])` |  |

**References:** [luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [schank2005approximating](../../references.html#schank2005approximating), [staudt2016networkit](../../references.html#staudt2016networkit)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Edge bfs {#trav_edge_bfs}

Measure id: `trav_edge_bfs`. Original family: Traversal, trees and DAGs.

**Definition.** Edge bfs.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_edge_bfs` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_bfs(M)` |  |
| `trav_edge_bfs_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_bfs(M, orientation = 'ignore')` |  |
| `trav_edge_bfs_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_bfs(M, orientation = 'reverse')` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Random BFS {#cat_bfs_random}

Measure id: `cat_bfs_random`. Original family: Paths and distances.

**Definition.** Random BFS.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `RandomBFS` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Reverse BFS {#cat_bfs_reverse}

Measure id: `cat_bfs_reverse`. Original family: Paths and distances.

**Definition.** Reverse BFS.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `ReverseBFS` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
