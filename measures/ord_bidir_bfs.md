---
title: "Bidir bfs"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bidir bfs

Family: Traversal, trees and DAGs. Identifier: `ord_bidir_bfs`.

## Definition

Bidir bfs.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bidir_bfs` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bidirectional_shortest_path(M, 0, n - 1)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
