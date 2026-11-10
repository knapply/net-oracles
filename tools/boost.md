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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Approximate betweenness (sampling)](../measures/betweenness_approx.html) | · reported in docs | `betweenness_centrality_clustering` |
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention | `brandes_betweenness_centrality` |
| Centrality | [Closeness](../measures/closeness.html) | ≠ checked, differs by convention | `closeness_centrality` |
| Centrality | [Pagerank](../measures/pagerank.html) | · reported in docs | `page_rank` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | · reported in docs | `core_numbers` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | · reported in docs | `bron_kerbosch_all_cliques` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | · reported in docs | `biconnected_components` |
| Components and connectivity | [Condensation](../measures/condensation.html) | · reported in docs | `create_condensation_graph` |
| Components and connectivity | [Connectivity](../measures/connectivity.html) | · reported in docs | `edge_connectivity` |
| Components and connectivity | [Cut points](../measures/cut_points.html) | ✓ checked, agrees | `articulation_points` |
| Components and connectivity | [Max flow](../measures/max_flow.html) | · reported in docs | `boykov_kolmogorov_max_flow; edmonds_karp_max_flow; push_relabel_max_flow` |
| Components and connectivity | [Max flow min cost](../measures/max_flow_min_cost.html) | · reported in docs | `cycle_canceling; successive_shortest_path_nonnegative_weights` |
| Components and connectivity | [Min cut](../measures/min_cut.html) | · reported in docs | `stoer_wagner_min_cut` |
| Components and connectivity | [Strong partition](../measures/strong_partition.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ≠ checked, differs by convention | `clustering_coefficient` |
| Descriptive statistics | [Components](../measures/components.html) | · reported in docs | `connected_components; incremental_components; st_connected; strong_components` |
| Descriptive statistics | [Degree](../measures/degree.html) | · reported in docs | `degree_centrality` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `erdos_renyi_generator; erdos_renyi_iterator; sorted_erdos_renyi_iterator` |
| Generators and rewiring | [Make connected](../measures/cat_connected_make.html) | · reported in docs | `make_connected` |
| Generators and rewiring | [Mesh graph generator](../measures/cat_generator_mesh.html) | · reported in docs | `mesh_graph_generator` |
| Generators and rewiring | [Plod generator](../measures/cat_generator_plod.html) | · reported in docs | `plod_generator` |
| Generators and rewiring | [R-MAT generator](../measures/gen_rmat.html) | · reported in docs | `rmat_graph_generator` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `small_world_generator; small_world_iterator` |
| Generators and rewiring | [Ssca graph generator](../measures/cat_generator_ssca.html) | · reported in docs | `ssca_graph_generator` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | · reported in docs | `edge_coloring; sequential_vertex_coloring; smallest_last_ordering` |
| Graph theory and combinatorics | [Max weight matching](../measures/max_weight_matching.html) | · reported in docs | `maximum_weighted_matching` |
| Graph theory and combinatorics | [Planar](../measures/st_planar.html) | · reported in docs | `boyer_myrvold_planarity_test` |
| Graph theory and combinatorics | [Planarity testing, embedding and straight-line drawing](../measures/planarity.html) | · reported in docs | `chrobak_payne_straight_line_drawing; is_kuratowski_subgraph; is_straight_line_drawing; make_biconnected_planar; make_maximal_planar; planar_canonical_ordering; planar_face_traversal` |
| Graph theory and combinatorics | [Plod iterator](../measures/cat_iterator_plod.html) | · reported in docs | `plod_iterator` |
| Graph theory and combinatorics | [Simple cycles](../measures/simple_cycles.html) | · reported in docs | `find_odd_cycle; hawick_circuits; tiernan_all_cycles` |
| Graph theory and combinatorics | [Traveling salesman (exact and heuristic)](../measures/tsp.html) | · reported in docs | `metric_tsp_approx` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | · reported in docs | `isomorphism; vf2_sub_graph_iso` |
| Layout | [Circle, tree and two-mode (barycenter) layouts](../measures/layout_simple.html) | · reported in docs | `circle_layout` |
| Layout | [Fruchterman-Reingold layout](../measures/layout_fruchterman_reingold.html) | · reported in docs | `fruchterman_reingold_force_directed_layout` |
| Layout | [Gursoy atun layout](../measures/cat_atun_gursoy_layout.html) | · reported in docs | `gursoy_atun_layout` |
| Layout | [Kamada-Kawai layout](../measures/layout_kamada_kawai.html) | · reported in docs | `kamada_kawai_spring_layout` |
| Layout | [Random layout](../measures/layout_random.html) | · reported in docs | `random_graph_layout` |
| Matrices and spectra | [Sparse-matrix orderings and bandwidth/wavefront](../measures/matrix_bandwidth.html) | · reported in docs | `aver_wavefront; bandwidth; cuthill_mckee_ordering; ith_bandwidth; ith_wavefront; king_ordering; max_wavefront; minimum_degree_ordering; rms_wavefront; sloan_ordering` |
| Paths and distances | [Diameter](../measures/diameter.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees | `geodesic_distance` |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ≠ checked, differs by convention | `eccentricity` |
| Paths and distances | [Minimum/maximum cycle ratio and mean cycle](../measures/cycle_ratio.html) | · reported in docs | `howard_cycle_ratio; maximum_cycle_ratio; minimum_cycle_ratio` |
| Paths and distances | [Paths astar](../measures/paths_astar.html) | · reported in docs | `astar_search` |
| Paths and distances | [Paths floyd warshall](../measures/paths_floyd_warshall.html) | · reported in docs | `floyd_warshall_all_pairs_shortest_paths` |
| Paths and distances | [Paths johnson](../measures/paths_johnson.html) | · reported in docs | `johnson_all_pairs_shortest_paths` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `dag_shortest_paths; dijkstra_shortest_paths` |
| Paths and distances | [R c shortest paths](../measures/cat_c_path_r_shortest.html) | · reported in docs | `r_c_shortest_paths` |
| Paths and distances | [Radius](../measures/radius.html) | ≠ checked, differs by convention |  |
| Roles and positions | [Mcgregor common subgraphs](../measures/cat_common_mcgregor_subgraphs.html) | · reported in docs | `mcgregor_common_subgraphs` |
| Traversal, trees and DAGs | [Bellman ford](../measures/ord_bellman_ford.html) | · reported in docs | `bellman_ford_shortest_paths` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `breadth_first_search` |
| Traversal, trees and DAGs | [Closure](../measures/closure.html) | · reported in docs | `transitive_closure` |
| Traversal, trees and DAGs | [Edge dfs](../measures/trav_edge_dfs.html) | · reported in docs | `depth_first_search; undirected_dfs` |
| Traversal, trees and DAGs | [Idom](../measures/idom.html) | · reported in docs | `lengauer_tarjan_dominator_tree` |
| Traversal, trees and DAGs | [Random spanning tree](../measures/random_spanning_tree.html) | · reported in docs | `random_spanning_tree` |
| Traversal, trees and DAGs | [Random walk generation and sampling](../measures/random_walk_sampling.html) | · reported in docs | `loop_erased_random_walk` |
| Traversal, trees and DAGs | [Reduction](../measures/reduction.html) | · reported in docs | `transitive_reduction` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | · reported in docs | `kruskal_minimum_spanning_tree; prim_minimum_spanning_tree` |
| Traversal, trees and DAGs | [Spanning weight](../measures/spanning_weight.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Topological sort](../measures/topological_sort.html) | · reported in docs | `topological_sort` |
| Traversal, trees and DAGs | [Two graphs common spanning trees](../measures/cat_common_spanning_tree_two.html) | · reported in docs | `two_graphs_common_spanning_trees` |
| Traversal, trees and DAGs | [Vertex orderings (max cardinality, degeneracy)](../measures/vertex_orderings.html) | · reported in docs | `maximum_adjacency_search` |
| Two-mode and bipartite | [Bipartite](../measures/cat_bipartite.html) | · reported in docs | `bipartite` |
| Two-mode and bipartite | [Bipartite color](../measures/bipartite_color.html) | · reported in docs | `is_bipartite` |
| Two-mode and bipartite | [Hopcroft karp](../measures/hopcroft_karp.html) | · reported in docs | `edmonds_maximum_cardinality_matching` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F046](../findings.html#f046) | convention | relative\_betweenness\_centrality is twice the standard value on directed graphs |
| [F048](../findings.html#f048) | convention | Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair |
| [F050](../findings.html#f050) | convention | Eccentricity, radius and diameter return DBL\_MAX when a node is unreachable |
| [F052](../findings.html#f052) | convention | Clustering counts loops and parallel edges as extra neighbours |
{% endraw %}
