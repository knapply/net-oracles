---
title: "Dijkstra"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Dijkstra

Family: Traversal, trees and DAGs. Identifier: `ord_dijkstra`.

## Definition

Dijkstra.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bfs_preds` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.dijkstra_predecessor_and_distance(M, 0, weight = None)[0]` |  |
| `ord_dijkstra_preds` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.dijkstra_predecessor_and_distance(M, 0)[0]` |  |
| `ord_dijkstra_unit` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.single_source_dijkstra(M, 0, weight = None): (node, distance, parent) in dict order` |  |
| `ord_dijkstra_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.single_source_dijkstra(M, 0)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
