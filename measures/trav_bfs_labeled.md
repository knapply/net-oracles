---
title: "Bfs labeled"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bfs labeled

Family: Traversal, trees and DAGs. Identifier: `trav_bfs_labeled`.

## Definition

Bfs labeled.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bfs_labeled_edges` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `trav_bfs_labeled` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bfs_labeled_edges(M, [0])` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
