---
title: "Paths bidirectional"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths bidirectional

Family: Paths and distances. Identifier: `paths_bidirectional`.

## Definition

Paths bidirectional.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bidirectional_shortest_path` |  |
| [NetworKit](../tools/networkit.html) | · reported in docs | `BidirectionalBFS` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_bidirectional_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.bidirectional_shortest_path(G, s, t)) - 1 for every pair (no path: unreachable)` |  |
| `paths_bidirectional_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.bidirectional_dijkstra(G, s, t, weight = 'weight')[0] for every pair` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
