---
title: "Depth-first search"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Depth-first search {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Traversal and orderings. Concept id: `depth_first_search`. 3 measures.

## Definition {#concept-definition}

Depth-first search. Entries grouped here: Dfs events; Dfs iterator; Edge dfs.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Dfs events](#trav_dfs_events) | `trav_dfs_events` | 2 |
| [Dfs iterator](#cat_dfs_iterator) | `cat_dfs_iterator` | 1 |
| [Edge dfs](#trav_edge_dfs) | `trav_edge_dfs` | 6 |

## Dfs events {#trav_dfs_events}

Measure id: `trav_dfs_events`. Original family: Traversal, trees and DAGs.

**Definition.** Dfs events.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `dfs_labeled_edges` |  |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `DepthFirstIterator` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_dfs_events` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.dfs_labeled_edges(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Dfs iterator {#cat_dfs_iterator}

Measure id: `cat_dfs_iterator`. Original family: Traversal, trees and DAGs.

**Definition.** Dfs iterator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `dfs_iterator` | API listing |

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Edge dfs {#trav_edge_dfs}

Measure id: `trav_edge_dfs`. Original family: Traversal, trees and DAGs.

**Definition.** Edge dfs.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `dfs_edges; dfs_postorder_nodes; dfs_predecessors; dfs_preorder_nodes; dfs_successors; dfs_tree; edge_dfs` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `dfs` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `dfs; dfsiter` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `dfs_search` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `dfs_edges; dfs_search; digraph_dfs_edges; digraph_dfs_search; graph_dfs_edges; graph_dfs_search` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `depth_first_search; undirected_dfs` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_edge_dfs` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_dfs(M)` |  |
| `trav_edge_dfs_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_dfs(M, orientation = 'ignore')` |  |
| `trav_edge_dfs_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_dfs(M, orientation = 'reverse')` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
