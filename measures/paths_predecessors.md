---
title: "Paths predecessors"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths predecessors

Family: Paths and distances. Identifier: `paths_predecessors`.

## Definition

Paths predecessors.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `predecessor` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_predecessors_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.predecessor(G, 0)` |  |
| `paths_predecessors_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.dijkstra_predecessor_and_distance(G, 0, weight = 'weight')[0]` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
