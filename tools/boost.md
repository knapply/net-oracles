---
title: "Boost Graph Library"
layout: default
parent: Tools
---

{% raw %}

# Boost Graph Library

| Field | Value |
|---|---|
| Identifier | `boost` |
| Language | C++ |
| Version tested | 1.90 |
| License | BSL-1.0 |
| Homepage | <https://www.boost.org/libs/graph/> |
| Role | checked |
| Citation | [siek2002boost](../references.html#siek2002boost) |

## How it was run

Small C++ driver programs compiled against the headers.

Capabilities listed by documentation of Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 4 |
| checked, differs by convention (≠) | 7 |
| reported in docs (·) | 55 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Approximate betweenness (sampling)](../measures/centrality/betweenness.html#betweenness_approx) | · reported in docs | `betweenness_centrality_clustering` |
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | ≠ checked, differs by convention | `brandes_betweenness_centrality` |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | · reported in docs | `degree_centrality` |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | ≠ checked, differs by convention | `closeness_centrality` |
| Centrality | Spectral and walk-based | [PageRank](../measures/centrality/pagerank.html) | [Pagerank](../measures/centrality/pagerank.html#pagerank) | · reported in docs | `page_rank` |
| Cohesion and subgroups | Cliques | [Maximal cliques](../measures/cohesion-and-subgroups/maximal_cliques.html) | [Max cliques](../measures/cohesion-and-subgroups/maximal_cliques.html#max_cliques) | · reported in docs | `bron_kerbosch_all_cliques` |
| Cohesion and subgroups | Cores, trusses and cohesive blocks | [K-core decomposition](../measures/cohesion-and-subgroups/k_core.html) | [Coreness](../measures/cohesion-and-subgroups/k_core.html#coreness) | · reported in docs | `core_numbers` |
| Components and connectivity | Articulation points, bridges and biconnected components | [Biconnected components](../measures/components-and-connectivity/biconnected_components.html) | [Bicomponents](../measures/components-and-connectivity/biconnected_components.html#bicomponents) | · reported in docs | `biconnected_components` |
| Components and connectivity | Articulation points, bridges and biconnected components | [Cut points (articulation points)](../measures/components-and-connectivity/cut_points.html) | [Cut points](../measures/components-and-connectivity/cut_points.html#cut_points) | ✓ checked, agrees | `articulation_points` |
| Components and connectivity | Connected components | [Condensation of strong components](../measures/components-and-connectivity/condensation.html) | [Condensation](../measures/components-and-connectivity/condensation.html#condensation) | · reported in docs | `create_condensation_graph` |
| Components and connectivity | Connected components | [Connected components](../measures/components-and-connectivity/connected_components.html) | [Components](../measures/components-and-connectivity/connected_components.html#components) | · reported in docs | `connected_components; incremental_components; st_connected; strong_components` |
| Components and connectivity | Connected components | [Connected components](../measures/components-and-connectivity/connected_components.html) | [Strong partition](../measures/components-and-connectivity/connected_components.html#strong_partition) | ✓ checked, agrees |  |
| Components and connectivity | Connectivity numbers | [Edge connectivity](../measures/components-and-connectivity/edge_connectivity.html) | [Connectivity](../measures/components-and-connectivity/edge_connectivity.html#connectivity) | · reported in docs | `edge_connectivity` |
| Components and connectivity | Cuts and separators | [Global minimum cut](../measures/components-and-connectivity/global_min_cut.html) | [Min cut](../measures/components-and-connectivity/global_min_cut.html#min_cut) | · reported in docs | `stoer_wagner_min_cut` |
| Components and connectivity | Dominators | [Dominators and dominance frontiers](../measures/components-and-connectivity/dominators.html) | [Idom](../measures/components-and-connectivity/dominators.html#idom) | · reported in docs | `lengauer_tarjan_dominator_tree` |
| Components and connectivity | Flows and flow trees | [Maximum flow](../measures/components-and-connectivity/max_flow.html) | [Max flow](../measures/components-and-connectivity/max_flow.html#max_flow) | · reported in docs | `boykov_kolmogorov_max_flow; edmonds_karp_max_flow; push_relabel_max_flow` |
| Components and connectivity | Flows and flow trees | [Minimum-cost flow](../measures/components-and-connectivity/min_cost_flow.html) | [Max flow min cost](../measures/components-and-connectivity/min_cost_flow.html#max_flow_min_cost) | · reported in docs | `cycle_canceling; successive_shortest_path_nonnegative_weights` |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | ≠ checked, differs by convention |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | ≠ checked, differs by convention | `clustering_coefficient` |
| Generators and rewiring | Classic random graphs | [G(n, p) random graph](../measures/generators-and-rewiring/gnp_random_graph.html) | [G(n, p) random graph](../measures/generators-and-rewiring/gnp_random_graph.html#gen_gnp) | · reported in docs | `erdos_renyi_generator; erdos_renyi_iterator; sorted_erdos_renyi_iterator` |
| Generators and rewiring | Growth and attachment models | [PLOD generator](../measures/generators-and-rewiring/plod.html) | [Plod generator](../measures/generators-and-rewiring/plod.html#cat_generator_plod) | · reported in docs | `plod_generator` |
| Generators and rewiring | Growth and attachment models | [PLOD generator](../measures/generators-and-rewiring/plod.html) | [Plod iterator](../measures/generators-and-rewiring/plod.html#cat_iterator_plod) | · reported in docs | `plod_iterator` |
| Generators and rewiring | Growth and attachment models | [R-MAT](../measures/generators-and-rewiring/rmat.html) | [R-MAT generator](../measures/generators-and-rewiring/rmat.html#gen_rmat) | · reported in docs | `rmat_graph_generator` |
| Generators and rewiring | Growth and attachment models | [SSCA graph generator](../measures/generators-and-rewiring/ssca.html) | [Ssca graph generator](../measures/generators-and-rewiring/ssca.html#cat_generator_ssca) | · reported in docs | `ssca_graph_generator` |
| Generators and rewiring | Named and deterministic graphs | [Make connected](../measures/generators-and-rewiring/make_connected.html) | [Make connected](../measures/generators-and-rewiring/make_connected.html#cat_connected_make) | · reported in docs | `make_connected` |
| Generators and rewiring | Small-world, lattice and geometric models | [Lattice graphs](../measures/generators-and-rewiring/lattice_graphs.html) | [Mesh graph generator](../measures/generators-and-rewiring/lattice_graphs.html#cat_generator_mesh) | · reported in docs | `mesh_graph_generator` |
| Generators and rewiring | Small-world, lattice and geometric models | [Small-world generator](../measures/generators-and-rewiring/small_world_generator.html) | [Small-world generator](../measures/generators-and-rewiring/small_world_generator.html#gen_small_world) | · reported in docs | `small_world_generator; small_world_iterator` |
| Graph theory and combinatorics | Coloring | [Bipartite coloring and test](../measures/graph-theory-and-combinatorics/bipartite_coloring.html) | [Bipartite](../measures/graph-theory-and-combinatorics/bipartite_coloring.html#cat_bipartite) | · reported in docs | `bipartite` |
| Graph theory and combinatorics | Coloring | [Bipartite coloring and test](../measures/graph-theory-and-combinatorics/bipartite_coloring.html) | [Bipartite color](../measures/graph-theory-and-combinatorics/bipartite_coloring.html#bipartite_color) | · reported in docs | `is_bipartite` |
| Graph theory and combinatorics | Coloring | [Vertex coloring](../measures/graph-theory-and-combinatorics/vertex_coloring.html) | [Greedy color](../measures/graph-theory-and-combinatorics/vertex_coloring.html#greedy_color) | · reported in docs | `edge_coloring; sequential_vertex_coloring; smallest_last_ordering` |
| Graph theory and combinatorics | Cycles | [Simple cycles](../measures/graph-theory-and-combinatorics/simple_cycles.html) | [Simple cycles](../measures/graph-theory-and-combinatorics/simple_cycles.html#simple_cycles) | · reported in docs | `find_odd_cycle; hawick_circuits; tiernan_all_cycles` |
| Graph theory and combinatorics | Eulerian paths, Hamiltonian paths and tours | [Traveling salesman](../measures/graph-theory-and-combinatorics/traveling_salesman.html) | [Traveling salesman (exact and heuristic)](../measures/graph-theory-and-combinatorics/traveling_salesman.html#tsp) | · reported in docs | `metric_tsp_approx` |
| Graph theory and combinatorics | Isomorphism and subgraph matching | [Graph isomorphism](../measures/graph-theory-and-combinatorics/graph_isomorphism.html) | [Vf2pp](../measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp) | · reported in docs | `isomorphism; vf2_sub_graph_iso` |
| Graph theory and combinatorics | Isomorphism and subgraph matching | [McGregor common subgraphs](../measures/graph-theory-and-combinatorics/common_subgraphs.html) | [Mcgregor common subgraphs](../measures/graph-theory-and-combinatorics/common_subgraphs.html#cat_common_mcgregor_subgraphs) | · reported in docs | `mcgregor_common_subgraphs` |
| Graph theory and combinatorics | Matching | [Bipartite maximum matching](../measures/graph-theory-and-combinatorics/bipartite_maximum_matching.html) | [Hopcroft karp](../measures/graph-theory-and-combinatorics/bipartite_maximum_matching.html#hopcroft_karp) | · reported in docs | `edmonds_maximum_cardinality_matching` |
| Graph theory and combinatorics | Matching | [Maximum-weight matching](../measures/graph-theory-and-combinatorics/maximum_weight_matching.html) | [Max weight matching](../measures/graph-theory-and-combinatorics/maximum_weight_matching.html#max_weight_matching) | · reported in docs | `maximum_weighted_matching` |
| Graph theory and combinatorics | Planarity | [Planarity test](../measures/graph-theory-and-combinatorics/planarity_test.html) | [Planar](../measures/graph-theory-and-combinatorics/planarity_test.html#st_planar) | · reported in docs | `boyer_myrvold_planarity_test` |
| Graph theory and combinatorics | Planarity | [Planarity test](../measures/graph-theory-and-combinatorics/planarity_test.html) | [Planarity testing, embedding and straight-line drawing](../measures/graph-theory-and-combinatorics/planarity_test.html#planarity) | · reported in docs | `chrobak_payne_straight_line_drawing; is_kuratowski_subgraph; is_straight_line_drawing; make_biconnected_planar; make_maximal_planar; planar_canonical_ordering; planar_face_traversal` |
| Layout | Layout algorithms | [Force-directed layouts](../measures/layout/force_directed_layout.html) | [Fruchterman-Reingold layout](../measures/layout/force_directed_layout.html#layout_fruchterman_reingold) | · reported in docs | `fruchterman_reingold_force_directed_layout` |
| Layout | Layout algorithms | [Force-directed layouts](../measures/layout/force_directed_layout.html) | [Gursoy atun layout](../measures/layout/force_directed_layout.html#cat_atun_gursoy_layout) | · reported in docs | `gursoy_atun_layout` |
| Layout | Layout algorithms | [Force-directed layouts](../measures/layout/force_directed_layout.html) | [Kamada-Kawai layout](../measures/layout/force_directed_layout.html#layout_kamada_kawai) | · reported in docs | `kamada_kawai_spring_layout` |
| Layout | Layout algorithms | [Grid, random, circle and sphere layouts](../measures/layout/geometric_layout.html) | [Circle, tree and two-mode (barycenter) layouts](../measures/layout/geometric_layout.html#layout_simple) | · reported in docs | `circle_layout` |
| Layout | Layout algorithms | [Grid, random, circle and sphere layouts](../measures/layout/geometric_layout.html) | [Random layout](../measures/layout/geometric_layout.html#layout_random) | · reported in docs | `random_graph_layout` |
| Matrices and spectra | Graph matrices | [Sparse-matrix orderings and bandwidth](../measures/matrices-and-spectra/matrix_bandwidth.html) | [Sparse-matrix orderings and bandwidth/wavefront](../measures/matrices-and-spectra/matrix_bandwidth.html#matrix_bandwidth) | · reported in docs | `aver_wavefront; bandwidth; cuthill_mckee_ordering; ith_bandwidth; ith_wavefront; king_ordering; max_wavefront; minimum_degree_ordering; rms_wavefront; sloan_ordering` |
| Paths and distances | Distance summaries | [Diameter](../measures/paths-and-distances/diameter.html) | [Diameter](../measures/paths-and-distances/diameter.html#diameter) | ≠ checked, differs by convention |  |
| Paths and distances | Distance summaries | [Eccentricity](../measures/paths-and-distances/eccentricity.html) | [Eccentricity](../measures/paths-and-distances/eccentricity.html#eccentricity) | ≠ checked, differs by convention | `eccentricity` |
| Paths and distances | Distance summaries | [Radius](../measures/paths-and-distances/radius.html) | [Radius](../measures/paths-and-distances/radius.html#radius) | ≠ checked, differs by convention |  |
| Paths and distances | Path enumeration and counting | [Minimum and maximum cycle ratio](../measures/paths-and-distances/cycle_ratio.html) | [Minimum/maximum cycle ratio and mean cycle](../measures/paths-and-distances/cycle_ratio.html#cycle_ratio) | · reported in docs | `howard_cycle_ratio; maximum_cycle_ratio; minimum_cycle_ratio` |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | ✓ checked, agrees | `geodesic_distance` |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Paths floyd warshall](../measures/paths-and-distances/geodesic_distances.html#paths_floyd_warshall) | · reported in docs | `floyd_warshall_all_pairs_shortest_paths` |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Paths johnson](../measures/paths-and-distances/geodesic_distances.html#paths_johnson) | · reported in docs | `johnson_all_pairs_shortest_paths` |
| Paths and distances | Shortest paths | [Resource-constrained shortest path](../measures/paths-and-distances/resource_constrained_shortest_path.html) | [R c shortest paths](../measures/paths-and-distances/resource_constrained_shortest_path.html#cat_c_path_r_shortest) | · reported in docs | `r_c_shortest_paths` |
| Paths and distances | Shortest paths | [Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional)](../measures/paths-and-distances/shortest_paths.html) | [Bellman ford](../measures/paths-and-distances/shortest_paths.html#ord_bellman_ford) | · reported in docs | `bellman_ford_shortest_paths` |
| Paths and distances | Shortest paths | [Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional)](../measures/paths-and-distances/shortest_paths.html) | [Paths astar](../measures/paths-and-distances/shortest_paths.html#paths_astar) | · reported in docs | `astar_search` |
| Paths and distances | Shortest paths | [Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional)](../measures/paths-and-distances/shortest_paths.html) | [Paths sssp](../measures/paths-and-distances/shortest_paths.html#paths_sssp) | · reported in docs | `dag_shortest_paths; dijkstra_shortest_paths` |
| Traversal, trees and DAGs | DAGs and topological order | [Topological sort](../measures/traversal-trees-and-dags/topological_sort.html) | [Topological sort](../measures/traversal-trees-and-dags/topological_sort.html#topological_sort) | · reported in docs | `topological_sort` |
| Traversal, trees and DAGs | DAGs and topological order | [Transitive closure](../measures/traversal-trees-and-dags/transitive_closure.html) | [Closure](../measures/traversal-trees-and-dags/transitive_closure.html#closure) | · reported in docs | `transitive_closure` |
| Traversal, trees and DAGs | DAGs and topological order | [Transitive reduction](../measures/traversal-trees-and-dags/transitive_reduction.html) | [Reduction](../measures/traversal-trees-and-dags/transitive_reduction.html#reduction) | · reported in docs | `transitive_reduction` |
| Traversal, trees and DAGs | Spanning trees and branchings | [Common spanning trees of two graphs](../measures/traversal-trees-and-dags/common_spanning_trees.html) | [Two graphs common spanning trees](../measures/traversal-trees-and-dags/common_spanning_trees.html#cat_common_spanning_tree_two) | · reported in docs | `two_graphs_common_spanning_trees` |
| Traversal, trees and DAGs | Spanning trees and branchings | [Minimum spanning tree](../measures/traversal-trees-and-dags/minimum_spanning_tree.html) | [Spanning tree](../measures/traversal-trees-and-dags/minimum_spanning_tree.html#spanning_tree) | · reported in docs | `kruskal_minimum_spanning_tree; prim_minimum_spanning_tree` |
| Traversal, trees and DAGs | Spanning trees and branchings | [Minimum spanning tree](../measures/traversal-trees-and-dags/minimum_spanning_tree.html) | [Spanning weight](../measures/traversal-trees-and-dags/minimum_spanning_tree.html#spanning_weight) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | Spanning trees and branchings | [Random spanning tree](../measures/traversal-trees-and-dags/random_spanning_tree.html) | [Random spanning tree](../measures/traversal-trees-and-dags/random_spanning_tree.html#random_spanning_tree) | · reported in docs | `random_spanning_tree` |
| Traversal, trees and DAGs | Traversal and orderings | [Breadth-first search](../measures/traversal-trees-and-dags/breadth_first_search.html) | [Bfs edges](../measures/traversal-trees-and-dags/breadth_first_search.html#trav_bfs_edges) | · reported in docs | `breadth_first_search` |
| Traversal, trees and DAGs | Traversal and orderings | [Depth-first search](../measures/traversal-trees-and-dags/depth_first_search.html) | [Edge dfs](../measures/traversal-trees-and-dags/depth_first_search.html#trav_edge_dfs) | · reported in docs | `depth_first_search; undirected_dfs` |
| Traversal, trees and DAGs | Traversal and orderings | [Random walks](../measures/traversal-trees-and-dags/random_walks.html) | [Random walk generation and sampling](../measures/traversal-trees-and-dags/random_walks.html#random_walk_sampling) | · reported in docs | `loop_erased_random_walk` |
| Traversal, trees and DAGs | Traversal and orderings | [Vertex orderings (max cardinality, degeneracy)](../measures/traversal-trees-and-dags/vertex_orderings.html) | [Vertex orderings (max cardinality, degeneracy)](../measures/traversal-trees-and-dags/vertex_orderings.html#vertex_orderings) | · reported in docs | `maximum_adjacency_search` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F046](../findings.html#f046) | convention | relative\_betweenness\_centrality is twice the standard value on directed graphs |
| [F048](../findings.html#f048) | convention | Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair |
| [F050](../findings.html#f050) | convention | Eccentricity, radius and diameter return DBL\_MAX when a node is unreachable |
| [F052](../findings.html#f052) | convention | Clustering counts loops and parallel edges as extra neighbours |
{% endraw %}
