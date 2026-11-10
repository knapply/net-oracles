---
title: "Paths floyd warshall"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths floyd warshall

Family: Paths and distances. Identifier: `paths_floyd_warshall`.

## Definition

Paths floyd warshall.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `floyd_warshall; floyd_warshall_predecessor_and_distance; floyd_warshall_tree` |  |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_floyd_warshall; digraph_floyd_warshall_successor_and_distance; floyd_warshall; floyd_warshall_successor_and_distance; graph_floyd_warshall; graph_floyd_warshall_successor_and_distance` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `FloydWarshallShortestPaths` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `floyd_warshall_all_pairs_shortest_paths` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_floyd_warshall_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall(G, weight = 'len')` |  |
| `paths_floyd_warshall_shift` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall(G, weight = 'len'); NetworkXUnbounded is a negative cycle` |  |
| `paths_floyd_warshall_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall(G, weight = 'weight')` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
