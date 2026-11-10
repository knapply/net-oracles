---
title: "Paths multi source"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths multi source

Family: Paths and distances. Identifier: `paths_multi_source`.

## Definition

Paths multi source.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_multi_source_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.multi_source_dijkstra_path_length(G, {0, n - 1}, weight = None)` |  |
| `paths_multi_source_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.multi_source_dijkstra_path_length(G, {0, n - 1}, weight = 'weight')` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
