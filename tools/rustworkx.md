---
title: "rustworkx"
layout: default
parent: Tools
---

{% raw %}
# rustworkx

| Field | Value |
|---|---|
| Identifier | `rustworkx` |
| Language | Rust / Python |
| Version tested | 0.18.1 |
| License | Apache-2.0 |
| Homepage | <https://www.rustworkx.org> |
| Role | checked |
| Citation | [tool_rustworkx](../references.html#tool_rustworkx) |

## How it was run

Imported in CPython; public functions called on PyGraph and PyDiGraph objects.

Capabilities listed by introspection of rustworkx public functions and generators.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 11 |
| checked, differs by convention (≠) | 2 |
| checked, no value on some inputs (∅) | 2 |
| reported in docs (·) | 85 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ✓ checked, agrees | `betweenness_centrality; digraph_betweenness_centrality; graph_betweenness_centrality` |
| Centrality | [Closeness](../measures/closeness.html) | ✓ checked, agrees | `closeness_centrality; digraph_closeness_centrality; graph_closeness_centrality` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | ✓ checked, agrees | `digraph_edge_betweenness_centrality; edge_betweenness_centrality; graph_edge_betweenness_centrality` |
| Centrality | [Eigenvector](../measures/eigenvector.html) | ✓ checked, agrees | `digraph_eigenvector_centrality; eigenvector_centrality; graph_eigenvector_centrality` |
| Centrality | [Group / betweenness](../measures/group-betweenness.html) | · reported in docs | `digraph_group_betweenness_centrality; graph_group_betweenness_centrality; group_betweenness_centrality` |
| Centrality | [Group / closeness](../measures/group-closeness.html) | · reported in docs | `digraph_group_closeness_centrality; graph_group_closeness_centrality; group_closeness_centrality` |
| Centrality | [Group / degree](../measures/group-degree.html) | · reported in docs | `digraph_group_degree_centrality; graph_group_degree_centrality; group_degree_centrality` |
| Centrality | [Hits](../measures/hits.html) | ∅ checked, no value on some inputs | `hits` |
| Centrality | [Katz](../measures/katz.html) | ∅ checked, no value on some inputs | `digraph_katz_centrality; graph_katz_centrality; katz_centrality` |
| Centrality | [Newman weighted closeness centrality](../measures/cat_closeness_newman_weighted.html) | · reported in docs | `digraph_newman_weighted_closeness_centrality; graph_newman_weighted_closeness_centrality; newman_weighted_closeness_centrality` |
| Centrality | [Pagerank](../measures/pagerank.html) | ≠ checked, differs by convention | `pagerank` |
| Centrality | [Reach](../measures/reach.html) | · reported in docs | `ancestors; descendants` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ≠ checked, differs by convention | `core_number; digraph_core_number; graph_core_number` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | · reported in docs | `biconnected_components` |
| Components and connectivity | [Bridges](../measures/bridges.html) | ✓ checked, agrees | `bridges` |
| Components and connectivity | [Condensation](../measures/condensation.html) | · reported in docs | `condensation; digraph_condensation; graph_condensation` |
| Components and connectivity | [Cut points](../measures/cut_points.html) | ✓ checked, agrees | `articulation_points` |
| Components and connectivity | [Is semi connected](../measures/cat_connected_is_semi.html) | · reported in docs | `is_semi_connected` |
| Components and connectivity | [Min cut](../measures/min_cut.html) | · reported in docs | `stoer_wagner_min_cut` |
| Data transforms | [Graph complement](../measures/op_complement.html) | · reported in docs | `complement; digraph_complement; graph_complement` |
| Data transforms | [Graph products](../measures/op_graph_product.html) | · reported in docs | `cartesian_product; digraph_cartesian_product; digraph_tensor_product; graph_cartesian_product; graph_tensor_product; tensor_product` |
| Data transforms | [Line graph](../measures/line_graph.html) | · reported in docs | `graph_line_graph` |
| Data transforms | [Op union](../measures/op_union.html) | · reported in docs | `digraph_union; graph_union; union` |
| Descriptive statistics | [Components](../measures/components.html) | ✓ checked, agrees | `connected_components; connected_subgraphs; is_connected; is_strongly_connected; is_weakly_connected; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components` |
| Descriptive statistics | [Degree](../measures/degree.html) | · reported in docs | `degree_centrality; digraph_degree_centrality; graph_degree_centrality; in_degree_centrality; out_degree_centrality` |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ✓ checked, agrees | `digraph_transitivity; graph_transitivity; transitivity` |
| Generators and rewiring | [Barbell graph](../measures/cat_barbell.html) | · reported in docs | `barbell_graph` |
| Generators and rewiring | [Deterministic generators](../measures/deterministic_generators.html) | · reported in docs | `complete_graph; cycle_graph; directed_complete_graph; directed_cycle_graph; directed_empty_graph; directed_path_graph; directed_star_graph; empty_graph; full_rary_tree; path_graph; star_graph` |
| Generators and rewiring | [Dorogovtsev goltsev mendes graph](../measures/cat_dorogovtsev_goltsev_mendes.html) | · reported in docs | `dorogovtsev_goltsev_mendes_graph` |
| Generators and rewiring | [G(n, m) random graph](../measures/gen_gnm.html) | · reported in docs | `directed_gnm_random_graph; undirected_gnm_random_graph` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `directed_gnp_random_graph; undirected_gnp_random_graph` |
| Generators and rewiring | [Generalized petersen graph](../measures/cat_generalized_petersen.html) | · reported in docs | `generalized_petersen_graph` |
| Generators and rewiring | [Heavy hex graph](../measures/cat_heavy_hex.html) | · reported in docs | `directed_heavy_hex_graph; heavy_hex_graph` |
| Generators and rewiring | [Heavy square graph](../measures/cat_heavy_square.html) | · reported in docs | `directed_heavy_square_graph; heavy_square_graph` |
| Generators and rewiring | [Hexagonal lattice graph](../measures/cat_hexagonal_lattice.html) | · reported in docs | `directed_hexagonal_lattice_graph; hexagonal_lattice_graph` |
| Generators and rewiring | [Hyperbolic greedy routing](../measures/cat_greedy_hyperbolic_routing.html) | · reported in docs | `hyperbolic_greedy_routing` |
| Generators and rewiring | [Hyperbolic greedy success rate](../measures/cat_greedy_hyperbolic_rate_success.html) | · reported in docs | `hyperbolic_greedy_success_rate` |
| Generators and rewiring | [Hyperbolic random graph generator](../measures/gen_hyperbolic.html) | · reported in docs | `hyperbolic_random_graph` |
| Generators and rewiring | [Lattice generator](../measures/gen_lattice.html) | · reported in docs | `directed_grid_graph; grid_graph` |
| Generators and rewiring | [Lollipop graph](../measures/cat_lollipop.html) | · reported in docs | `lollipop_graph` |
| Generators and rewiring | [Mesh graph](../measures/cat_mesh.html) | · reported in docs | `directed_mesh_graph; mesh_graph` |
| Generators and rewiring | [Preferential attachment generator](../measures/gen_preferential.html) | · reported in docs | `barabasi_albert_graph; directed_barabasi_albert_graph` |
| Generators and rewiring | [Random bipartite graph generator](../measures/gen_random_bipartite.html) | · reported in docs | `directed_random_bipartite_graph; undirected_random_bipartite_graph` |
| Generators and rewiring | [Random geometric graph generator](../measures/gen_geometric.html) | · reported in docs | `random_geometric_graph` |
| Generators and rewiring | [Random regular graph generator](../measures/gen_regular.html) | · reported in docs | `random_regular_graph` |
| Generators and rewiring | [Sbm random graph](../measures/cat_random_sbm.html) | · reported in docs | `directed_sbm_random_graph` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `undirected_sbm_random_graph` |
| Graph theory and combinatorics | [Check matching](../measures/check_matching.html) | · reported in docs | `is_matching; is_maximal_matching` |
| Graph theory and combinatorics | [Contracted nodes](../measures/nxs_contracted_nodes.html) | · reported in docs | `local_complement` |
| Graph theory and combinatorics | [Cycle basis](../measures/cycle_basis.html) | · reported in docs | `cycle_basis` |
| Graph theory and combinatorics | [Find cycle](../measures/find_cycle.html) | · reported in docs | `digraph_find_cycle` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | · reported in docs | `graph_greedy_color` |
| Graph theory and combinatorics | [Greedy edge color](../measures/cat_color_edge_greedy.html) | · reported in docs | `graph_greedy_edge_color` |
| Graph theory and combinatorics | [Max weight matching](../measures/max_weight_matching.html) | · reported in docs | `max_weight_matching` |
| Graph theory and combinatorics | [Maximum bisimulation](../measures/cat_bisimulation_maximum.html) | · reported in docs | `digraph_maximum_bisimulation` |
| Graph theory and combinatorics | [Misra gries edge color](../measures/cat_color_edge_gries_misra.html) | · reported in docs | `graph_misra_gries_edge_color` |
| Graph theory and combinatorics | [Planar](../measures/st_planar.html) | · reported in docs | `is_planar` |
| Graph theory and combinatorics | [Simple cycles](../measures/simple_cycles.html) | · reported in docs | `simple_cycles` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | · reported in docs | `digraph_is_isomorphic; digraph_is_subgraph_isomorphic; digraph_vf2_mapping; graph_is_isomorphic; graph_is_subgraph_isomorphic; graph_vf2_mapping; is_isomorphic; is_isomorphic_node_match; is_subgraph_isomorphic; vf2_mapping` |
| Input and output | [GraphML read and write](../measures/io_graphml.html) | · reported in docs | `read_graphml` |
| Input and output | [MATRIXMARKET read and write](../measures/io_matrixmarket.html) | · reported in docs | `read_matrix_market; read_matrix_market_file` |
| Input and output | [NODELINKJSON read and write](../measures/io_nodelinkjson.html) | · reported in docs | `from_node_link_json_file` |
| Layout | [Circle, tree and two-mode (barycenter) layouts](../measures/layout_simple.html) | · reported in docs | `bipartite_layout; circular_layout; digraph_bipartite_layout; digraph_circular_layout; digraph_shell_layout; digraph_spiral_layout; graph_bipartite_layout; graph_circular_layout; graph_shell_layout; graph_spiral_layout; shell_layout; spiral_layout` |
| Layout | [Fruchterman-Reingold layout](../measures/layout_fruchterman_reingold.html) | · reported in docs | `digraph_spring_layout; graph_spring_layout; spring_layout` |
| Layout | [Kamada-Kawai layout](../measures/layout_kamada_kawai.html) | · reported in docs | `digraph_kamada_kawai_layout; graph_kamada_kawai_layout; kamada_kawai_layout` |
| Layout | [Random layout](../measures/layout_random.html) | · reported in docs | `digraph_random_layout; graph_random_layout; random_layout` |
| Matrices and spectra | [Adjacency](../measures/gm_adjacency.html) | · reported in docs | `adjacency_matrix; digraph_adjacency_matrix; graph_adjacency_matrix` |
| Paths and distances | [Dag longest path](../measures/cat_dag_longest_path.html) | · reported in docs | `dag_longest_path` |
| Paths and distances | [Dag longest path length](../measures/cat_dag_length_longest_path.html) | · reported in docs | `dag_longest_path_length` |
| Paths and distances | [Dag weighted longest path](../measures/cat_dag_longest_path_weighted.html) | · reported in docs | `dag_weighted_longest_path` |
| Paths and distances | [Dag weighted longest path length](../measures/cat_dag_length_longest_path_weighted.html) | · reported in docs | `dag_weighted_longest_path_length` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees |  |
| Paths and distances | [Longest simple path](../measures/paths_longest_simple.html) | · reported in docs | `digraph_longest_simple_path; graph_longest_simple_path; longest_simple_path` |
| Paths and distances | [Mean distance](../measures/mean_distance.html) | · reported in docs | `digraph_unweighted_average_shortest_path_length; graph_unweighted_average_shortest_path_length; unweighted_average_shortest_path_length` |
| Paths and distances | [Paths all pairs](../measures/paths_all_pairs.html) | · reported in docs | `all_pairs_all_simple_paths; all_pairs_bellman_ford_path_lengths; all_pairs_bellman_ford_shortest_paths; all_pairs_dijkstra_path_lengths; all_pairs_dijkstra_shortest_paths; digraph_all_pairs_all_simple_paths; digraph_all_pairs_bellman_ford_path_lengths; digraph_all_pairs_bellman_ford_shortest_paths; digraph_all_pairs_dijkstra_path_lengths; digraph_all_pairs_dijkstra_shortest_paths; digraph_distance_matrix; digraph_floyd_warshall_numpy` |
| Paths and distances | [Paths all shortest](../measures/paths_all_shortest.html) | · reported in docs | `all_shortest_paths; digraph_all_shortest_paths; digraph_num_shortest_paths_unweighted; graph_all_shortest_paths; graph_num_shortest_paths_unweighted; num_shortest_paths_unweighted` |
| Paths and distances | [Paths astar](../measures/paths_astar.html) | · reported in docs | `astar_shortest_path; digraph_astar_shortest_path; graph_astar_shortest_path` |
| Paths and distances | [Paths floyd warshall](../measures/paths_floyd_warshall.html) | · reported in docs | `digraph_floyd_warshall; digraph_floyd_warshall_successor_and_distance; floyd_warshall; floyd_warshall_successor_and_distance; graph_floyd_warshall; graph_floyd_warshall_successor_and_distance` |
| Paths and distances | [Paths k shortest](../measures/paths_k_shortest.html) | · reported in docs | `digraph_k_shortest_path_lengths; graph_k_shortest_path_lengths; k_shortest_path_lengths` |
| Paths and distances | [Paths negative cycle](../measures/paths_negative_cycle.html) | · reported in docs | `find_negative_cycle; negative_edge_cycle` |
| Paths and distances | [Paths simple](../measures/paths_simple.html) | · reported in docs | `all_simple_paths; digraph_all_simple_paths; graph_all_simple_paths` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `digraph_dijkstra_search; digraph_dijkstra_shortest_path_lengths; digraph_dijkstra_shortest_paths; digraph_single_source_all_shortest_paths; dijkstra_search; dijkstra_shortest_path_lengths; dijkstra_shortest_paths; graph_dijkstra_search; graph_dijkstra_shortest_path_lengths; graph_dijkstra_shortest_paths; graph_single_source_all_shortest_paths; single_source_all_shortest_paths` |
| Paths and distances | [Reachability](../measures/reachability.html) | · reported in docs | `digraph_has_path; graph_has_path; has_path` |
| Roles and positions | [Chain decomposition](../measures/cat_chain_decomposition.html) | · reported in docs | `chain_decomposition` |
| Traversal, trees and DAGs | [Bellman ford](../measures/ord_bellman_ford.html) | · reported in docs | `bellman_ford_shortest_path_lengths; bellman_ford_shortest_paths; digraph_bellman_ford_shortest_path_lengths; digraph_bellman_ford_shortest_paths; graph_bellman_ford_shortest_path_lengths; graph_bellman_ford_shortest_paths` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `bfs_predecessors; bfs_search; bfs_successors; digraph_bfs_search; graph_bfs_search` |
| Traversal, trees and DAGs | [Bfs layers](../measures/trav_bfs_layers.html) | · reported in docs | `bfs_layers; digraph_bfs_layers; graph_bfs_layers` |
| Traversal, trees and DAGs | [Binomial tree](../measures/cat_binomial_tree.html) | · reported in docs | `binomial_tree_graph; directed_binomial_tree_graph` |
| Traversal, trees and DAGs | [Edge dfs](../measures/trav_edge_dfs.html) | · reported in docs | `dfs_edges; dfs_search; digraph_dfs_edges; digraph_dfs_search; graph_dfs_edges; graph_dfs_search` |
| Traversal, trees and DAGs | [Idom](../measures/idom.html) | · reported in docs | `dominance_frontiers; immediate_dominators` |
| Traversal, trees and DAGs | [Is dag](../measures/is_dag.html) | ✓ checked, agrees | `is_directed_acyclic_graph` |
| Traversal, trees and DAGs | [Isolates](../measures/gb_isolates.html) | · reported in docs | `digraph_isolates; graph_isolates; isolates` |
| Traversal, trees and DAGs | [Random walks](../measures/random_walk.html) | · reported in docs | `digraph_generate_random_path; generate_random_path; graph_generate_random_path` |
| Traversal, trees and DAGs | [Reduction](../measures/reduction.html) | · reported in docs | `transitive_reduction` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | · reported in docs | `minimum_spanning_edges; minimum_spanning_tree` |
| Traversal, trees and DAGs | [Spanning weight](../measures/spanning_weight.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Steiner tree](../measures/steiner_tree.html) | · reported in docs | `steiner_tree` |
| Traversal, trees and DAGs | [Topological sort](../measures/topological_sort.html) | · reported in docs | `lexicographical_topological_sort; topological_generations; topological_sort` |
| Two-mode and bipartite | [Bipartite color](../measures/bipartite_color.html) | · reported in docs | `digraph_is_bipartite; digraph_two_color; graph_is_bipartite; graph_two_color; is_bipartite; two_color` |
| Two-mode and bipartite | [Bipartite edge color](../measures/cat_bipartite_color_edge.html) | · reported in docs | `graph_bipartite_edge_color` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F006](../findings.html#f006) | convention | PageRank stops on an L1 change below n \* tol |
| [F008](../findings.html#f008) | convention | Undirected self-loop is one arc |
{% endraw %}
