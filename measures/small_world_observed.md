---
title: "Small world observed"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Small world observed

Family: Descriptive statistics. Identifier: `small_world_observed`.

## Definition

Small world observed.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `small_world_observed` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-13 | `nx.transitivity and the mean of nx.shortest_path_length over connected pairs (simple undirected graph)` |  |
| `small_world_observed` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-13 | `igraph::transitivity(type = 'global') and mean_distance(unconnected = TRUE) on simplify(as_undirected(g))` |  |
| `small_world_observed_local` | NetworkX | any | agrees |  |  | abs 1e-15, rel 1e-13 | `nx.average_clustering and the mean of nx.shortest_path_length over connected pairs` |  |
| `small_world_observed_local` | igraph (R) | any | agrees |  |  | abs 1e-15, rel 1e-13 | `igraph::transitivity(type = 'average', isolates = 'zero') and mean_distance(unconnected = TRUE)` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
