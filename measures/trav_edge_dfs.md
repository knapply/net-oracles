---
title: "Edge dfs"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Edge dfs

Family: Traversal, trees and DAGs. Identifier: `trav_edge_dfs`.

## Definition

Edge dfs.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `dfs_edges; dfs_postorder_nodes; dfs_predecessors; dfs_preorder_nodes; dfs_successors; dfs_tree; edge_dfs` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `dfs` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `dfs; dfsiter` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `dfs_search` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `dfs_edges; dfs_search; digraph_dfs_edges; digraph_dfs_search; graph_dfs_edges; graph_dfs_search` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `depth_first_search; undirected_dfs` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_edge_dfs` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_dfs(M)` |  |
| `trav_edge_dfs_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_dfs(M, orientation = 'ignore')` |  |
| `trav_edge_dfs_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_dfs(M, orientation = 'reverse')` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
