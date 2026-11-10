---
title: "Edge bfs"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Edge bfs

Family: Traversal, trees and DAGs. Identifier: `trav_edge_bfs`.

## Definition

Edge bfs.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_edge_bfs` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_bfs(M)` |  |
| `trav_edge_bfs_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_bfs(M, orientation = 'ignore')` |  |
| `trav_edge_bfs_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 1e-12 | `nx.edge_bfs(M, orientation = 'reverse')` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
