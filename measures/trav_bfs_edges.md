---
title: "Bfs edges"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bfs edges

Family: Traversal, trees and DAGs. Identifier: `trav_bfs_edges`.

## Definition

Bfs edges.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bfs_edges; bfs_predecessors; bfs_successors; bfs_tree; edge_bfs` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `bfs` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `bfs; bfsiter` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `bfs_search` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `BFS` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `bfs_predecessors; bfs_search; bfs_successors; digraph_bfs_search; graph_bfs_search` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `breadth_first_search` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `BreadthFirstIterator; LexBreadthFirstIterator` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `breadth_first_search` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_bfs_edges` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_edges(M, 0)` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
