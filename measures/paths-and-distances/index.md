---
title: "Paths and distances"
layout: default
parent: Measures
has_children: true
nav_order: 15
permalink: /measures/paths-and-distances/
---

{% raw %}
# Paths and distances

65 measures in 39 concepts and 6 subfamilies. Each concept page has a section per measure (variant); the anchor of a section is the measure id (characters other than letters, digits, underscore, dot and hyphen become hyphens).

## Distance summaries

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Barycenter](barycenter.html) | 1 | 2 | The nodes of smallest total distance to the others, and every node's total distance. |
| [Closeness vitality](closeness_vitality.html) | 1 | 2 | Wiener index of the network minus that of the network without the node, for every node. |
| [Diameter](diameter.html) | 1 | 11 | Longest shortest-path distance. |
| [Distance histogram](distance_histogram.html) | 1 | 1 | Distance histogram. Entries grouped here: Distance histogram. |
| [Eccentricity](eccentricity.html) | 1 | 10 | Each node's largest distance to the nodes it reaches. |
| [Graph center](graph_center.html) | 1 | 2 | Nodes of smallest eccentricity; empty unless the network is (strongly) connected, as in NetworkX. |
| [Graph periphery](graph_periphery.html) | 1 | 1 | Nodes of largest eccentricity; empty unless the network is (strongly) connected, as in NetworkX. |
| [Greedy routing and navigation](greedy_routing.html) | 3 | 2 | Greedy routing and navigation. Entries grouped here: Hyperbolic greedy routing; Hyperbolic greedy success rate; Navigation. |
| [Mean distance](mean_distance.html) | 1 | 7 | Mean shortest-path distance over ordered pairs of distinct nodes joined by a path. |
| [Mean first passage time](mean_first_passage_time.html) | 1 | 1 | Mean first passage time. Entries grouped here: Mean first passage time. |
| [Neighborhood function and effective diameter](neighborhood_function.html) | 1 | 1 | Neighborhood function and effective diameter. Entries grouped here: Neighborhood function, hop plot, effective diameter. |
| [Path transitivity](path_transitivity.html) | 1 | 1 | Path transitivity. Entries grouped here: Path transitivity. |
| [Radius](radius.html) | 1 | 8 | The smallest eccentricity (NaN for a network without nodes). |
| [Search information](search_information.html) | 1 | 1 | Search information. Entries grouped here: Search information. |
| [Social proximity](social_proximity.html) | 1 | 1 | Social proximity. Entries grouped here: Socialprox. |
| [Wiener index](wiener_index.html) | 1 | 3 | Sum of the distances over unordered pairs (ordered pairs in a directed network); infinite unless connected. |

## Efficiency and reachability

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Global and local efficiency](global_efficiency.html) | 2 | 5 | Global and local efficiency. Entries grouped here: Global and local efficiency; Swan efficiency. |
| [Local efficiency](local_efficiency.html) | 1 | 3 | Mean over the nodes of the global efficiency of the subgraph induced by each node's neighbors. |
| [Reachability](reachability.html) | 3 | 7 | Reachability. Entries grouped here: Reachability; Reachable Nodes; Reachdist. |

## Geometry

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Edge lengths (geometry)](edge_lengths.html) | 1 | 2 | Edge lengths (geometry). Entries grouped here: Edge lengths. |
| [Group geometry](group_geometry.html) | 1 | 2 | Group geometry. Entries grouped here: Group geometry. |
| [Proximity](proximity.html) | 1 | 3 | Proximity. Entries grouped here: Proximity. |

## Path enumeration and counting

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [All paths](all_paths.html) | 3 | 8 | All paths. Entries grouped here: All Directed Paths; Allpaths; Paths simple. |
| [Bounded path and walk search](bounded_path_search.html) | 2 | 1 | Bounded path and walk search. Entries grouped here: Findpaths; Findwalks. |
| [Complex paths](complex_paths.html) | 1 | 1 | Complex paths. Entries grouped here: Complex Paths. |
| [K-path census](path_census.html) | 1 | 1 | K-path census. Entries grouped here: Kpath census. |
| [Longest simple path](longest_simple_path.html) | 1 | 1 | Longest simple path. Entries grouped here: Longest simple path. |
| [Minimum and maximum cycle ratio](cycle_ratio.html) | 1 | 2 | Minimum and maximum cycle ratio. Entries grouped here: Minimum/maximum cycle ratio and mean cycle. |
| [Path counting in DAGs](dag_path_count.html) | 1 | 1 | Path counting in DAGs. Entries grouped here: Dag All Paths Counter. |
| [Path counts](path_counts.html) | 1 | 2 | Path counts. Entries grouped here: Paths count. |

## Resistance and spectral distances

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Kemeny constant](kemeny_constant.html) | 1 | 1 | Kemeny's constant of the random walk: the expected steps to reach a stationary-distributed node, the same from every start. |
| [Resistance distance and effective resistance](resistance_distance.html) | 3 | 3 | Resistance distance between every pair of nodes, infinite across components (Klein and Randic 1993). |

## Shortest paths

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [All shortest paths](all_shortest_paths.html) | 1 | 5 | All shortest paths. Entries grouped here: Paths all shortest. |
| [Geodesic distances](geodesic_distances.html) | 6 | 15 | Geodesic distances. Entries grouped here: Distances; Fw tree; Johnson lengths; Paths all pairs; Paths floyd warshall; Paths johnson. |
| [K shortest paths](k_shortest_paths.html) | 1 | 5 | K shortest paths. Entries grouped here: Paths k shortest. |
| [Many-to-many and hierarchy-based shortest paths](hierarchical_shortest_paths.html) | 1 | 1 | Many-to-many and hierarchy-based shortest paths. Entries grouped here: Many-to-many and hierarchy-based shortest paths. |
| [Negative cycle detection](negative_cycle.html) | 1 | 2 | Negative cycle detection. Entries grouped here: Paths negative cycle. |
| [Resource-constrained shortest path](resource_constrained_shortest_path.html) | 1 | 1 | Resource-constrained shortest path. Entries grouped here: R c shortest paths. |
| [Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional)](shortest_paths.html) | 12 | 10 | Shortest-path lengths from one node by Delta-stepping; infinity for unreached nodes. |
{% endraw %}
