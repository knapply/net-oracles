---
title: "Bidir dijkstra"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bidir dijkstra

Family: Traversal, trees and DAGs. Identifier: `ord_bidir_dijkstra`.

## Definition

Bidir dijkstra.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bidir_dijkstra` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bidirectional_dijkstra(M, 0, n - 1): path, then length` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
