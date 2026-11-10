---
title: "Paths sssp"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths sssp

Family: Paths and distances. Identifier: `paths_sssp`.

## Definition

Shortest-path lengths from one node by Delta-stepping; infinity for unreached nodes.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bidirectional_dijkstra; dijkstra_path; dijkstra_path_length; dijkstra_predecessor_and_distance; multi_source_dijkstra; multi_source_dijkstra_path; multi_source_dijkstra_path_length; shortest_path; shortest_path_length; single_source_all_shortest_paths; single_source_dijkstra; single_source_dijkstra_path` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `shortest_paths` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `get_shortest_path; get_shortest_paths` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `all_predecessors; dijkstra_iterator; dijkstra_search; random_shortest_path; shortest_distance; shortest_path` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `BidirectionalDijkstra; Dijkstra; DynDijkstra; MultiTargetBFS; MultiTargetDijkstra; SSSP` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_dijkstra_search; digraph_dijkstra_shortest_path_lengths; digraph_dijkstra_shortest_paths; digraph_single_source_all_shortest_paths; dijkstra_search; dijkstra_shortest_path_lengths; dijkstra_shortest_paths; graph_dijkstra_search; graph_dijkstra_shortest_path_lengths; graph_dijkstra_shortest_paths; graph_single_source_all_shortest_paths; single_source_all_shortest_paths` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `get_shortest_path` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `BFSShortestPath; BidirectionalDijkstraShortestPath; ClosestFirstIterator; ContractionHierarchyBidirectionalDijkstra; DeltaSteppingShortestPath; DijkstraManyToManyShortestPaths; DijkstraShortestPath; IntVertexDijkstraShortestPath; MartinShortestPath` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `dag_shortest_paths; dijkstra_shortest_paths` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_sssp_cutoff_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.single_source_shortest_path_length(G, s, cutoff = 2) for every s` |  |
| `paths_sssp_cutoff_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_dijkstra_path_length(G, s, cutoff = 2.5, weight = 'weight') for every s` |  |
| `paths_sssp_strength` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_dijkstra_path_length(G, s, weight = lambda u, v, d: min(1 / w)) for every s` |  |
| `paths_sssp_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.single_source_shortest_path_length(G, s) for every s` |  |
| `paths_sssp_unweighted_all` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.single_source_shortest_path_length(G.to_undirected(), s) for every s` |  |
| `paths_sssp_unweighted_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.single_target_shortest_path_length(G, s) for every s` |  |
| `paths_sssp_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_dijkstra_path_length(G, s, weight = 'weight') for every s` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
