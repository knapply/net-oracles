---
title: "Paths all pairs"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths all pairs

Family: Paths and distances. Identifier: `paths_all_pairs`.

## Definition

Paths all pairs.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `all_pairs_all_shortest_paths; all_pairs_bellman_ford_path; all_pairs_bellman_ford_path_length; all_pairs_dijkstra; all_pairs_dijkstra_path; all_pairs_dijkstra_path_length; all_pairs_lowest_common_ancestor; all_pairs_node_connectivity; all_pairs_shortest_path; all_pairs_shortest_path_length; floyd_warshall_numpy` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `distance_table` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `APSP; DynAPSP` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `all_pairs_all_simple_paths; all_pairs_bellman_ford_path_lengths; all_pairs_bellman_ford_shortest_paths; all_pairs_dijkstra_path_lengths; all_pairs_dijkstra_shortest_paths; digraph_all_pairs_all_simple_paths; digraph_all_pairs_bellman_ford_path_lengths; digraph_all_pairs_bellman_ford_shortest_paths; digraph_all_pairs_dijkstra_path_lengths; digraph_all_pairs_dijkstra_shortest_paths; digraph_distance_matrix; digraph_floyd_warshall_numpy` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_all_pairs_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `dict(nx.all_pairs_shortest_path_length(G))` |  |
| `paths_all_pairs_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `dict(nx.all_pairs_dijkstra_path_length(G, weight = 'weight'))` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
