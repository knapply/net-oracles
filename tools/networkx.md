---
title: "NetworkX"
layout: default
parent: Tools
---

{% raw %}
# NetworkX

| Field | Value |
|---|---|
| Identifier | `networkx` |
| Language | Python |
| Version tested | 3.7 |
| License | BSD-3-Clause |
| Homepage | <https://networkx.org> |
| Role | checked |
| Citation | [hagberg2008exploring](../references.html#hagberg2008exploring) |

## How it was run

Imported in CPython 3.12; public functions called on graph objects built from edge lists.

Capabilities listed by introspection of networkx public API (algorithms, generators, linalg, readwrite).

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 311 |
| checked, differs by convention (≠) | 33 |
| checked, no value on some inputs (∅) | 9 |
| reported in docs (·) | 163 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention | `betweenness_centrality` |
| Centrality | [Betweenness simple](../measures/betweenness_simple.html) | ✓ checked, agrees |  |
| Centrality | [Betweenness subset](../measures/cx_betweenness_subset.html) | ≠ checked, differs by convention | `betweenness_centrality_subset; edge_betweenness_centrality_subset` |
| Centrality | [Closeness](../measures/closeness.html) | ✓ checked, agrees | `closeness_centrality` |
| Centrality | [Communicability](../measures/cx_communicability.html) | ✓ checked, agrees | `communicability; communicability_exp; subgraph_centrality; subgraph_centrality_exp` |
| Centrality | [Communicability betweenness](../measures/cx_communicability_betweenness.html) | ✓ checked, agrees | `communicability_betweenness_centrality` |
| Centrality | [Current flow approx](../measures/cx_current_flow_approx.html) | ✓ checked, agrees | `approximate_current_flow_betweenness_centrality` |
| Centrality | [Current flow closeness](../measures/cx_current_flow_closeness.html) | ✓ checked, agrees | `current_flow_closeness_centrality` |
| Centrality | [Current flow subset](../measures/cx_current_flow_subset.html) | ✓ checked, agrees | `current_flow_betweenness_centrality_subset; edge_current_flow_betweenness_centrality_subset` |
| Centrality | [Cx current flow](../measures/cx_current_flow.html) | ✓ checked, agrees | `current_flow_betweenness_centrality; edge_current_flow_betweenness_centrality` |
| Centrality | [Cx laplacian](../measures/cx_laplacian.html) | ✓ checked, agrees | `laplacian_centrality` |
| Centrality | [Dispersion](../measures/cx_dispersion.html) | ≠ checked, differs by convention | `dispersion` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | ≠ checked, differs by convention | `edge_betweenness_centrality` |
| Centrality | [Edge load](../measures/cx_edge_load.html) | ✓ checked, agrees | `edge_load_centrality` |
| Centrality | [Eigenvector](../measures/eigenvector.html) | ∅ checked, no value on some inputs | `eigenvector_centrality; eigenvector_centrality_numpy` |
| Centrality | [Google](../measures/nxp_google.html) | ✓ checked, agrees | `google_matrix` |
| Centrality | [Group / betweenness](../measures/group-betweenness.html) | ≠ checked, differs by convention | `group_betweenness_centrality` |
| Centrality | [Group / closeness](../measures/group-closeness.html) | ✓ checked, agrees | `group_closeness_centrality` |
| Centrality | [Group / degree](../measures/group-degree.html) | ✓ checked, agrees | `group_degree_centrality; group_in_degree_centrality` |
| Centrality | [Group out degree centrality](../measures/cat_degree_group_out.html) | · reported in docs | `group_out_degree_centrality` |
| Centrality | [Harmonic](../measures/harmonic.html) | ✓ checked, agrees | `harmonic_centrality` |
| Centrality | [Hits](../measures/hits.html) | ✓ checked, agrees | `hits` |
| Centrality | [Incremental closeness centrality](../measures/cat_closeness_incremental.html) | · reported in docs | `incremental_closeness_centrality` |
| Centrality | [Information centrality](../measures/information_centrality.html) | ✓ checked, agrees |  |
| Centrality | [Katz](../measures/katz.html) | ✓ checked, agrees | `katz_centrality; katz_centrality_numpy` |
| Centrality | [Load](../measures/cx_load.html) | ✓ checked, agrees | `newman_betweenness_centrality` |
| Centrality | [Nxp eigenvector](../measures/nxp_eigenvector.html) | ✓ checked, agrees |  |
| Centrality | [Nxp hits](../measures/nxp_hits.html) | ✓ checked, agrees |  |
| Centrality | [Nxp katz](../measures/nxp_katz.html) | ✓ checked, agrees |  |
| Centrality | [Nxp pagerank](../measures/nxp_pagerank.html) | ✓ checked, agrees |  |
| Centrality | [Pagerank](../measures/pagerank.html) | ≠ checked, differs by convention | `pagerank` |
| Centrality | [Percolation](../measures/cx_percolation.html) | ✓ checked, agrees | `percolation_centrality` |
| Centrality | [Reach](../measures/reach.html) | ✓ checked, agrees | `ancestors; descendants; descendants_at_distance` |
| Centrality | [Reaching](../measures/cx_reaching.html) | ≠ checked, differs by convention | `global_reaching_centrality; local_reaching_centrality` |
| Centrality | [Resistance](../measures/cx_resistance.html) | ✓ checked, agrees | `resistance_distance` |
| Centrality | [Second order](../measures/cx_second_order.html) | ✓ checked, agrees | `second_order_centrality` |
| Centrality | [Strength](../measures/strength.html) | ✓ checked, agrees |  |
| Centrality | [Subgraph centrality and stress centrality](../measures/subgraph_stress_centrality.html) | · reported in docs |  |
| Centrality | [Trophic](../measures/cx_trophic.html) | ✓ checked, agrees | `trophic_differences; trophic_incoherence_parameter; trophic_levels` |
| Centrality | [Voterank](../measures/cx_voterank.html) | ✓ checked, agrees | `voterank` |
| Centrality | [Walks ppr](../measures/walks_ppr.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [All cliques](../measures/all_cliques.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [All triads](../measures/cat_all_triads.html) | · reported in docs | `all_triads` |
| Cohesion and subgroups | [Clique number](../measures/clique_number.html) | ✓ checked, agrees | `max_clique; max_weight_clique; node_clique_number; number_of_cliques` |
| Cohesion and subgroups | [Core subset](../measures/core_subset.html) | ≠ checked, differs by convention |  |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ≠ checked, differs by convention | `core_number; k_core; k_corona; k_crust; k_shell; onion_layers` |
| Cohesion and subgroups | [Cut quality (conductance, expansion, boundary)](../measures/cut_quality.html) | · reported in docs | `boundary_expansion; conductance; cut_size; edge_boundary; edge_expansion; mixing_expansion; node_boundary; node_expansion; normalized_cut_size; volume` |
| Cohesion and subgroups | [K truss](../measures/k_truss.html) | ✓ checked, agrees | `k_truss` |
| Cohesion and subgroups | [Lambda connectivity](../measures/lambda_connectivity.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Lambda sets](../measures/lambda_sets.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | ✓ checked, agrees | `enumerate_all_cliques; find_cliques; find_cliques_recursive` |
| Cohesion and subgroups | [Max weight clique](../measures/max_weight_clique.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Max weight clique nodes](../measures/max_weight_clique_nodes.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [N clans](../measures/n_clans.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [N cliques](../measures/n_cliques.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Node clique number](../measures/node_clique_number.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Nx cliques order](../measures/nx_cliques_order.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Onion](../measures/onion.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Triad type](../measures/cat_triad_type.html) | · reported in docs | `triad_type` |
| Cohesion and subgroups | [Triads by type](../measures/cat_triads_type.html) | · reported in docs | `triads_by_type` |
| Cohesion and subgroups | [Truss](../measures/truss.html) | ✓ checked, agrees |  |
| Communities | [Cnx current flow](../measures/cnx_current_flow.html) | ≠ checked, differs by convention | `edge_current_flow_betweenness_partition` |
| Communities | [Cnx edge betweenness](../measures/cnx_edge_betweenness.html) | ✓ checked, agrees |  |
| Communities | [Cnx girvan newman](../measures/cnx_girvan_newman.html) | ✓ checked, agrees |  |
| Communities | [Cnx label propagation](../measures/cnx_label_propagation.html) | ✓ checked, agrees |  |
| Communities | [Fast greedy](../measures/fast_greedy.html) | ∅ checked, no value on some inputs | `greedy_modularity_communities; naive_greedy_modularity_communities` |
| Communities | [Fluid communities](../measures/fluid_communities.html) | ✓ checked, agrees | `asyn_fluidc` |
| Communities | [Girvan newman](../measures/girvan_newman.html) | ✓ checked, agrees | `edge_betweenness_partition; girvan_newman` |
| Communities | [Greedy modularity](../measures/cnx_greedy_modularity.html) | ✓ checked, agrees |  |
| Communities | [Is partition (community)](../measures/cat_is_partition-community.html) | · reported in docs | `is_partition` |
| Communities | [K clique](../measures/cnx_k_clique.html) | ✓ checked, agrees | `k_clique_communities` |
| Communities | [Kernighan lin](../measures/cnx_kernighan_lin.html) | ✓ checked, agrees | `kernighan_lin_bisection` |
| Communities | [Label propagation](../measures/label_propagation.html) | ≠ checked, differs by convention | `asyn_lpa_communities; fast_label_propagation_communities; label_propagation_communities` |
| Communities | [Label spreading](../measures/nxo_label_spreading.html) | ✓ checked, agrees | `harmonic_function; local_and_global_consistency` |
| Communities | [Leiden](../measures/leiden.html) | ✓ checked, agrees | `leiden_communities; leiden_partitions` |
| Communities | [Leiden seeded](../measures/cnx_leiden_seeded.html) | ✓ checked, agrees |  |
| Communities | [Louvain modularity](../measures/louvain_modularity.html) | ≠ checked, differs by convention | `louvain_communities; louvain_partitions` |
| Communities | [Louvain quality](../measures/louvain_quality.html) | ≠ checked, differs by convention |  |
| Communities | [Louvain seeded](../measures/cnx_louvain_seeded.html) | ✓ checked, agrees |  |
| Communities | [Lukes](../measures/cnx_lukes.html) | ✓ checked, agrees | `lukes_partitioning` |
| Communities | [Modularity](../measures/modularity.html) | ≠ checked, differs by convention | `modularity` |
| Communities | [Modularity nx](../measures/cnx_modularity_nx.html) | ✓ checked, agrees |  |
| Communities | [Naive greedy](../measures/cnx_naive_greedy.html) | ≠ checked, differs by convention |  |
| Communities | [Naive greedy nx](../measures/cnx_naive_greedy_nx.html) | ✓ checked, agrees |  |
| Communities | [Overlapping](../measures/cnx_overlapping.html) | ✓ checked, agrees | `overlapping_modularity` |
| Communities | [Partition counts](../measures/cnx_partition_counts.html) | ✓ checked, agrees |  |
| Communities | [Partition quality (coverage, performance)](../measures/partition_quality.html) | · reported in docs | `partition_quality` |
| Communities | [Partition spanning tree](../measures/cat_partition_spanning_tree.html) | · reported in docs | `partition_spanning_tree` |
| Communities | [Randomized partitioning (approximate)](../measures/cat_partitioning_randomized-approximate.html) | · reported in docs | `randomized_partitioning` |
| Communities | [Seeded labels](../measures/cnx_seeded_labels.html) | ✓ checked, agrees |  |
| Communities | [Spectral modularity bipartition (community)](../measures/cat_bipartition_modularity_spectral-community.html) | · reported in docs | `spectral_modularity_bipartition` |
| Components and connectivity | [All node cuts (connectivity)](../measures/cat_all_cut-connectivity.html) | · reported in docs | `all_node_cuts` |
| Components and connectivity | [All pairs node](../measures/all_pairs_node.html) | ✓ checked, agrees |  |
| Components and connectivity | [Attracting](../measures/attracting.html) | ✓ checked, agrees | `attracting_components` |
| Components and connectivity | [Attracting flags](../measures/attracting_flags.html) | ✓ checked, agrees |  |
| Components and connectivity | [Average node](../measures/average_node.html) | ✓ checked, agrees |  |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | ✓ checked, agrees | `biconnected_component_edges; biconnected_components` |
| Components and connectivity | [Biconnected](../measures/nxo_biconnected.html) | ✓ checked, agrees |  |
| Components and connectivity | [Bridge components (connectivity)](../measures/cat_bridge_component-connectivity.html) | · reported in docs | `bridge_components` |
| Components and connectivity | [Bridges](../measures/bridges.html) | ✓ checked, agrees | `bridges; has_bridges; local_bridges` |
| Components and connectivity | [Condensation](../measures/condensation.html) | ✓ checked, agrees | `condensation` |
| Components and connectivity | [Connectivity](../measures/connectivity.html) | ✓ checked, agrees | `average_node_connectivity; edge_connectivity; is_k_edge_connected; local_edge_connectivity; local_node_connectivity; node_connectivity` |
| Components and connectivity | [Cut measures](../measures/cut_measures.html) | ✓ checked, agrees |  |
| Components and connectivity | [Cut points](../measures/cut_points.html) | ✓ checked, agrees | `articulation_points` |
| Components and connectivity | [Disjoint paths](../measures/disjoint_paths.html) | ✓ checked, agrees | `edge_disjoint_paths; node_disjoint_paths` |
| Components and connectivity | [Edge cut](../measures/edge_cut.html) | ✓ checked, agrees |  |
| Components and connectivity | [Find minimal d separator](../measures/cat_d_find_minimal_separator.html) | · reported in docs | `find_minimal_d_separator` |
| Components and connectivity | [Gomory hu](../measures/gomory_hu.html) | ✓ checked, agrees | `gomory_hu_tree` |
| Components and connectivity | [Gomory hu values](../measures/gomory_hu_values.html) | ✓ checked, agrees |  |
| Components and connectivity | [Is attracting component](../measures/cat_attracting_component_is.html) | · reported in docs | `is_attracting_component` |
| Components and connectivity | [Is kl connected](../measures/cat_connected_is_kl.html) | · reported in docs | `is_kl_connected` |
| Components and connectivity | [Is locally k edge connected (connectivity)](../measures/cat_connected_edge_is_k_locally-connectivity.html) | · reported in docs | `is_locally_k_edge_connected` |
| Components and connectivity | [Is minimal d separator](../measures/cat_d_is_minimal_separator.html) | · reported in docs | `is_minimal_d_separator` |
| Components and connectivity | [K components](../measures/k_components.html) | ✓ checked, agrees | `k_components` |
| Components and connectivity | [K edge components](../measures/k_edge_components.html) | ✓ checked, agrees | `k_edge_components` |
| Components and connectivity | [Local bridges](../measures/local_bridges.html) | ✓ checked, agrees |  |
| Components and connectivity | [Local connectivity](../measures/local_connectivity.html) | ✓ checked, agrees |  |
| Components and connectivity | [Max flow](../measures/max_flow.html) | ✓ checked, agrees | `boykov_kolmogorov; capacity_scaling; dinitz; edmonds_karp; maximum_flow; maximum_flow_value; preflow_push; shortest_augmenting_path` |
| Components and connectivity | [Max flow min cost](../measures/max_flow_min_cost.html) | ✓ checked, agrees | `cost_of_flow; max_flow_min_cost; min_cost_flow; min_cost_flow_cost; network_simplex` |
| Components and connectivity | [Min cut](../measures/min_cut.html) | ✓ checked, agrees | `minimum_cut; minimum_cut_value; stoer_wagner` |
| Components and connectivity | [Min node cut](../measures/min_node_cut.html) | ✓ checked, agrees |  |
| Components and connectivity | [Node cut](../measures/node_cut.html) | ✓ checked, agrees | `minimum_edge_cut; minimum_node_cut; minimum_st_edge_cut; minimum_st_node_cut` |
| Components and connectivity | [Number attracting components](../measures/cat_attracting_component.html) | · reported in docs | `number_attracting_components` |
| Components and connectivity | [Semiconnected](../measures/semiconnected.html) | ✓ checked, agrees | `is_semiconnected` |
| Components and connectivity | [St edge cut](../measures/st_edge_cut.html) | ✓ checked, agrees |  |
| Components and connectivity | [St node cut](../measures/st_node_cut.html) | ✓ checked, agrees |  |
| Data transforms | [Graph complement](../measures/op_complement.html) | · reported in docs | `complement` |
| Data transforms | [Graph products](../measures/op_graph_product.html) | · reported in docs | `cartesian_product; corona_product; lexicographic_product; modular_product; rooted_product; strong_product; tensor_product` |
| Data transforms | [Line graph](../measures/line_graph.html) | ✓ checked, agrees | `line_graph` |
| Data transforms | [Op compose](../measures/op_compose.html) | · reported in docs | `compose; compose_all` |
| Data transforms | [Op difference](../measures/op_difference.html) | ✓ checked, agrees | `difference; symmetric_difference` |
| Data transforms | [Op intersection](../measures/op_intersection.html) | ✓ checked, agrees | `intersection; intersection_all` |
| Data transforms | [Op union](../measures/op_union.html) | ✓ checked, agrees | `disjoint_union; disjoint_union_all; union; union_all` |
| Data transforms | [Power](../measures/cat_power.html) | · reported in docs | `power` |
| Data transforms | [Reverse](../measures/cat_reverse.html) | · reported in docs | `reverse` |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ✓ checked, agrees | `average_clustering` |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ✓ checked, agrees | `clustering` |
| Descriptive statistics | [Compactness](../measures/compactness.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Components](../measures/components.html) | ✓ checked, agrees | `connected_components; is_biconnected; is_connected; is_strongly_connected; is_weakly_connected; kosaraju_strongly_connected_components; node_connected_component; number_connected_components; number_strongly_connected_components; number_weakly_connected_components; strongly_connected_components; weakly_connected_components` |
| Descriptive statistics | [Degree](../measures/degree.html) | ✓ checked, agrees | `degree_centrality; degrees; in_degree_centrality; out_degree_centrality` |
| Descriptive statistics | [Density](../measures/density.html) | ≠ checked, differs by convention | `density` |
| Descriptive statistics | [Directed clustering](../measures/nxo_directed_clustering.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Effective resistance](../measures/cx_effective_resistance.html) | ✓ checked, agrees | `effective_graph_resistance` |
| Descriptive statistics | [Ego size](../measures/ego_size.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Kemeny](../measures/cx_kemeny.html) | ✓ checked, agrees | `kemeny_constant` |
| Descriptive statistics | [Node reciprocity](../measures/nxo_node_reciprocity.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | ✓ checked, agrees | `overall_reciprocity; reciprocity` |
| Descriptive statistics | [Small world observed](../measures/small_world_observed.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Square clustering](../measures/square_clustering.html) | ✓ checked, agrees | `square_clustering` |
| Descriptive statistics | [Successor transitivity](../measures/nxo_successor_transitivity.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ✓ checked, agrees | `transitivity` |
| Descriptive statistics | [Triad census](../measures/triad_census.html) | ✓ checked, agrees | `triadic_census` |
| Descriptive statistics | [Triangles](../measures/nxo_triangles.html) | ✓ checked, agrees | `all_triangles; triangles` |
| Generators and rewiring | [Barbell graph](../measures/cat_barbell.html) | · reported in docs | `barbell_graph` |
| Generators and rewiring | [Caveman graph](../measures/cat_caveman.html) | · reported in docs | `caveman_graph` |
| Generators and rewiring | [Chordal cycle graph](../measures/cat_chordal_cycle.html) | · reported in docs | `chordal_cycle_graph` |
| Generators and rewiring | [Chung-Lu (expected degree) generator](../measures/gen_chung_lu.html) | · reported in docs | `expected_degree_graph` |
| Generators and rewiring | [Circulant graph generator](../measures/gen_circulant.html) | · reported in docs | `circulant_graph` |
| Generators and rewiring | [Circular ladder graph](../measures/cat_circular_ladder.html) | · reported in docs | `circular_ladder_graph` |
| Generators and rewiring | [Complete multipartite graph generator](../measures/gen_complete_multipartite.html) | · reported in docs | `complete_multipartite_graph` |
| Generators and rewiring | [Configuration model](../measures/gen_configuration.html) | · reported in docs | `configuration_model; directed_configuration_model; random_degree_sequence_graph` |
| Generators and rewiring | [Connected caveman graph](../measures/cat_caveman_connected.html) | · reported in docs | `connected_caveman_graph` |
| Generators and rewiring | [Degree sequence tree](../measures/cat_degree_sequence_tree.html) | · reported in docs | `degree_sequence_tree` |
| Generators and rewiring | [Deterministic generators](../measures/deterministic_generators.html) | ✓ checked, agrees | `balanced_tree; complete_bipartite_graph; complete_graph; cycle_graph; empty_graph; full_rary_tree; hypercube_graph; ladder_graph; null_graph; path_graph; star_graph; trivial_graph` |
| Generators and rewiring | [Deterministic realisation of a degree sequence](../measures/gen_degree_realization.html) | · reported in docs | `alternating_havel_hakimi_graph; directed_havel_hakimi_graph; havel_hakimi_graph; reverse_havel_hakimi_graph` |
| Generators and rewiring | [Directed joint degree graph](../measures/cat_degree_directed_joint.html) | · reported in docs | `directed_joint_degree_graph` |
| Generators and rewiring | [Dorogovtsev goltsev mendes graph](../measures/cat_dorogovtsev_goltsev_mendes.html) | · reported in docs | `dorogovtsev_goltsev_mendes_graph` |
| Generators and rewiring | [Duplication divergence graph](../measures/cat_divergence_duplication.html) | · reported in docs | `duplication_divergence_graph` |
| Generators and rewiring | [Full join](../measures/cat_full_join.html) | · reported in docs | `full_join` |
| Generators and rewiring | [G(n, m) random graph](../measures/gen_gnm.html) | · reported in docs | `dense_gnm_random_graph; gnm_random_graph; gnmk_random_graph` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `fast_gnp_random_graph; gnp_random_graph` |
| Generators and rewiring | [Generalized petersen graph](../measures/cat_generalized_petersen.html) | · reported in docs | `generalized_petersen_graph` |
| Generators and rewiring | [Geometric soft configuration graph](../measures/cat_configuration_geometric_soft.html) | · reported in docs | `geometric_soft_configuration_graph` |
| Generators and rewiring | [Gn graph](../measures/cat_gn.html) | · reported in docs | `gn_graph` |
| Generators and rewiring | [Gnc graph](../measures/cat_gnc.html) | · reported in docs | `gnc_graph` |
| Generators and rewiring | [Gnr graph](../measures/cat_gnr.html) | · reported in docs | `gnr_graph` |
| Generators and rewiring | [Graph atlas](../measures/cat_atlas.html) | · reported in docs | `graph_atlas` |
| Generators and rewiring | [Graph atlas g](../measures/cat_atlas_g.html) | · reported in docs | `graph_atlas_g` |
| Generators and rewiring | [Greedy node swap bipartition (community)](../measures/cat_bipartition_greedy_swap-community.html) | · reported in docs | `greedy_node_swap_bipartition` |
| Generators and rewiring | [Hexagonal lattice graph](../measures/cat_hexagonal_lattice.html) | · reported in docs | `hexagonal_lattice_graph` |
| Generators and rewiring | [Hkn harary graph](../measures/cat_harary_hkn.html) | · reported in docs | `hkn_harary_graph` |
| Generators and rewiring | [Hnm harary graph](../measures/cat_harary_hnm.html) | · reported in docs | `hnm_harary_graph` |
| Generators and rewiring | [Interval graph](../measures/cat_interval.html) | · reported in docs | `interval_graph` |
| Generators and rewiring | [Inverse line graph](../measures/cat_inverse_line.html) | · reported in docs | `inverse_line_graph` |
| Generators and rewiring | [Joint degree graph](../measures/cat_degree_joint.html) | · reported in docs | `joint_degree_graph` |
| Generators and rewiring | [Kneser graph](../measures/cat_kneser.html) | · reported in docs | `kneser_graph` |
| Generators and rewiring | [Lattice generator](../measures/gen_lattice.html) | · reported in docs | `grid_2d_graph; grid_graph; lattice_reference` |
| Generators and rewiring | [LCF notation graph generator](../measures/gen_lcf.html) | · reported in docs | `LCF_graph` |
| Generators and rewiring | [Lollipop graph](../measures/cat_lollipop.html) | · reported in docs | `lollipop_graph` |
| Generators and rewiring | [Make max clique graph](../measures/cat_clique_make_max.html) | · reported in docs | `make_max_clique_graph` |
| Generators and rewiring | [Margulis gabber galil graph](../measures/cat_gabber_galil_margulis.html) | · reported in docs | `margulis_gabber_galil_graph` |
| Generators and rewiring | [Maybe regular expander graph](../measures/cat_expander_maybe_regular.html) | · reported in docs | `maybe_regular_expander_graph` |
| Generators and rewiring | [Mycielski graph](../measures/cat_mycielski.html) | · reported in docs | `mycielski_graph` |
| Generators and rewiring | [Navigable small world graph](../measures/cat_navigable_small_world.html) | · reported in docs | `navigable_small_world_graph` |
| Generators and rewiring | [Paley graph](../measures/cat_paley.html) | · reported in docs | `paley_graph` |
| Generators and rewiring | [Partial duplication graph](../measures/cat_duplication_partial.html) | · reported in docs | `partial_duplication_graph` |
| Generators and rewiring | [Powerlaw cluster graph](../measures/cat_cluster_powerlaw.html) | · reported in docs | `powerlaw_cluster_graph` |
| Generators and rewiring | [Preferential attachment generator](../measures/gen_preferential.html) | · reported in docs | `barabasi_albert_graph; dual_barabasi_albert_graph; extended_barabasi_albert_graph; scale_free_graph` |
| Generators and rewiring | [Preferential attachment graph (bipartite)](../measures/cat_attachment_preferential-bipartite.html) | · reported in docs | `preferential_attachment_graph` |
| Generators and rewiring | [Random clustered graph](../measures/cat_clustered_random.html) | · reported in docs | `random_clustered_graph` |
| Generators and rewiring | [Random geometric graph generator](../measures/gen_geometric.html) | · reported in docs | `geographical_threshold_graph; random_geometric_graph; soft_random_geometric_graph; thresholded_random_geometric_graph; waxman_graph` |
| Generators and rewiring | [Random internet as graph](../measures/cat_as_internet_random.html) | · reported in docs | `random_internet_as_graph` |
| Generators and rewiring | [Random intersection graph generator](../measures/gen_intersection.html) | · reported in docs | `general_random_intersection_graph; k_random_intersection_graph; uniform_random_intersection_graph` |
| Generators and rewiring | [Random k-out graph generator](../measures/gen_k_out.html) | · reported in docs | `random_k_out_graph` |
| Generators and rewiring | [Random kernel graph](../measures/cat_kernel_random.html) | · reported in docs | `random_kernel_graph` |
| Generators and rewiring | [Random lobster graph](../measures/cat_lobster_random.html) | · reported in docs | `random_lobster_graph` |
| Generators and rewiring | [Random regular expander graph](../measures/cat_expander_random_regular.html) | · reported in docs | `random_regular_expander_graph` |
| Generators and rewiring | [Random regular graph generator](../measures/gen_regular.html) | · reported in docs | `random_regular_graph` |
| Generators and rewiring | [Random shell graph](../measures/cat_random_shell.html) | · reported in docs | `random_shell_graph` |
| Generators and rewiring | [Random tree generator](../measures/gen_random_tree.html) | · reported in docs | `nonisomorphic_trees; random_labeled_rooted_tree; random_labeled_tree; random_unlabeled_rooted_tree; random_unlabeled_tree` |
| Generators and rewiring | [Relaxed caveman graph](../measures/cat_caveman_relaxed.html) | · reported in docs | `relaxed_caveman_graph` |
| Generators and rewiring | [Rich club](../measures/rich_club.html) | ✓ checked, agrees | `rich_club_coefficient` |
| Generators and rewiring | [Ring of cliques](../measures/cat_clique_ring.html) | · reported in docs | `ring_of_cliques` |
| Generators and rewiring | [Small world](../measures/small_world.html) | ✓ checked, agrees | `omega; sigma` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `connected_watts_strogatz_graph; newman_watts_strogatz_graph; watts_strogatz_graph` |
| Generators and rewiring | [Spectral ordering](../measures/cat_ordering_spectral.html) | · reported in docs | `spectral_ordering` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `LFR_benchmark_graph; gaussian_random_partition_graph; planted_partition_graph; random_partition_graph; stochastic_block_model` |
| Generators and rewiring | [Stochastic graph](../measures/cat_stochastic.html) | · reported in docs | `stochastic_graph` |
| Generators and rewiring | [Sudoku graph](../measures/cat_sudoku.html) | · reported in docs | `sudoku_graph` |
| Generators and rewiring | [Swap contract](../measures/swap_contract.html) | ✓ checked, agrees | `connected_double_edge_swap; directed_edge_swap; double_edge_swap` |
| Generators and rewiring | [Tadpole graph](../measures/cat_tadpole.html) | · reported in docs | `tadpole_graph` |
| Generators and rewiring | [Triangular lattice graph](../measures/cat_lattice_triangular.html) | · reported in docs | `triangular_lattice_graph` |
| Generators and rewiring | [Turan graph generator](../measures/gen_turan.html) | · reported in docs | `turan_graph` |
| Generators and rewiring | [Visibility graph](../measures/cat_visibility.html) | · reported in docs | `visibility_graph` |
| Generators and rewiring | [Windmill graph](../measures/cat_windmill.html) | · reported in docs | `windmill_graph` |
| Graph theory and combinatorics | [Antichains](../measures/cat_antichains.html) | · reported in docs | `antichains` |
| Graph theory and combinatorics | [Ap dominating set](../measures/ap_dominating_set.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Ap local connectivity](../measures/ap_local_connectivity.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Ap vertex cover](../measures/ap_vertex_cover.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Asteroidal](../measures/st_asteroidal.html) | ✓ checked, agrees | `find_asteroidal_triple` |
| Graph theory and combinatorics | [At free](../measures/st_at_free.html) | ✓ checked, agrees | `is_at_free` |
| Graph theory and combinatorics | [Basis](../measures/basis.html) | ≠ checked, differs by convention |  |
| Graph theory and combinatorics | [CD index](../measures/nxs_cd_index.html) | ≠ checked, differs by convention | `cd_index` |
| Graph theory and combinatorics | [Cds](../measures/st_cds.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Check matching](../measures/check_matching.html) | ✓ checked, agrees | `is_matching; is_maximal_matching; is_perfect_matching` |
| Graph theory and combinatorics | [Chordal order](../measures/st_chordal_order.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Chordless cycles](../measures/chordless_cycles.html) | ✓ checked, agrees | `chordless_cycles` |
| Graph theory and combinatorics | [Chromatic polynomial](../measures/cat_chromatic_polynomial.html) | · reported in docs | `chromatic_polynomial` |
| Graph theory and combinatorics | [Clique removal](../measures/ap_clique_removal.html) | ≠ checked, differs by convention | `clique_removal` |
| Graph theory and combinatorics | [Colliders](../measures/nxs_colliders.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Coloring](../measures/st_coloring.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Contracted nodes](../measures/nxs_contracted_nodes.html) | ✓ checked, agrees | `contracted_edge; contracted_nodes; quotient_graph` |
| Graph theory and combinatorics | [Could be iso](../measures/could_be_iso.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Counterexample](../measures/st_counterexample.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Cycle basis](../measures/cycle_basis.html) | ≠ checked, differs by convention | `cycle_basis` |
| Graph theory and combinatorics | [Dag reachability](../measures/nxs_dag_reachability.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Degree sequence test](../measures/nxs_degree_sequence_test.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Densest](../measures/ap_densest.html) | ✓ checked, agrees | `densest_subgraph` |
| Graph theory and combinatorics | [Di Graph Matcher](../measures/cat_di_matcher.html) | · reported in docs | `DiGraphMatcher` |
| Graph theory and combinatorics | [Dominating](../measures/st_dominating.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Dominating sets](../measures/dominating_set.html) | · reported in docs | `connected_dominating_set; dominating_set; is_connected_dominating_set; is_dominating_set; min_edge_dominating_set; min_weighted_dominating_set` |
| Graph theory and combinatorics | [Edge cover](../measures/edge_cover.html) | · reported in docs | `is_cover; is_edge_cover; min_edge_cover` |
| Graph theory and combinatorics | [Embedding](../measures/st_embedding.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Embedding euler](../measures/st_embedding_euler.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Euler](../measures/nxs_euler.html) | · reported in docs | `eulerian_circuit; eulerian_path; eulerize; has_eulerian_path; is_eulerian; is_semieulerian` |
| Graph theory and combinatorics | [Euler circuit](../measures/nxs_euler_circuit.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Fill](../measures/st_fill.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Find cycle](../measures/find_cycle.html) | ✓ checked, agrees | `find_cycle` |
| Graph theory and combinatorics | [Flow hierarchy](../measures/nxo_flow_hierarchy.html) | ✓ checked, agrees | `flow_hierarchy` |
| Graph theory and combinatorics | [Forest flags](../measures/nxs_forest_flags.html) | ✓ checked, agrees | `is_arborescence; is_branching; is_forest; is_tree` |
| Graph theory and combinatorics | [From prufer](../measures/nxs_from_prufer.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Fw tree](../measures/nxs_fw_tree.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Generalized degree](../measures/generalized_degree.html) | ✓ checked, agrees | `generalized_degree` |
| Graph theory and combinatorics | [Generic edge match](../measures/cat_edge_generic_match.html) | · reported in docs | `generic_edge_match` |
| Graph theory and combinatorics | [Generic multiedge match](../measures/cat_generic_match_multiedge.html) | · reported in docs | `generic_multiedge_match` |
| Graph theory and combinatorics | [Generic node match](../measures/cat_generic_match.html) | · reported in docs | `generic_node_match` |
| Graph theory and combinatorics | [Girth](../measures/girth.html) | ✓ checked, agrees | `girth` |
| Graph theory and combinatorics | [Graph edit distance](../measures/ged.html) | ✓ checked, agrees | `graph_edit_distance; optimal_edit_paths; optimize_edit_paths; optimize_graph_edit_distance` |
| Graph theory and combinatorics | [Graph Matcher](../measures/cat_matcher.html) | · reported in docs | `GraphMatcher` |
| Graph theory and combinatorics | [Greedy branching](../measures/nxs_greedy_branching.html) | ✓ checked, agrees | `greedy_branching` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | ≠ checked, differs by convention | `color; equitable_color; greedy_color; strategy_connected_sequential; strategy_connected_sequential_bfs; strategy_connected_sequential_dfs; strategy_independent_set; strategy_largest_first; strategy_random_sequential; strategy_saturation_largest_first; strategy_smallest_last` |
| Graph theory and combinatorics | [Greedy source expansion (community)](../measures/cat_expansion_greedy_source-community.html) | · reported in docs | `greedy_source_expansion` |
| Graph theory and combinatorics | [Hampath](../measures/st_hampath.html) | ✓ checked, agrees | `hamiltonian_path` |
| Graph theory and combinatorics | [Implicit family](../measures/implicit_family.html) | ∅ checked, no value on some inputs |  |
| Graph theory and combinatorics | [Intersection](../measures/st_intersection.html) | ✓ checked, agrees | `intersection_array` |
| Graph theory and combinatorics | [Is isolate](../measures/cat_is_isolate.html) | · reported in docs | `is_isolate` |
| Graph theory and combinatorics | [Is k regular](../measures/cat_is_k_regular.html) | · reported in docs | `is_k_regular` |
| Graph theory and combinatorics | [Is regular expander](../measures/cat_expander_is_regular.html) | · reported in docs | `is_regular_expander` |
| Graph theory and combinatorics | [Is simple path](../measures/nxs_is_simple_path.html) | ✓ checked, agrees | `is_simple_path` |
| Graph theory and combinatorics | [Is strongly regular](../measures/cat_is_regular_strongly.html) | · reported in docs | `is_strongly_regular` |
| Graph theory and combinatorics | [ISMAGS](../measures/cat_ismags.html) | · reported in docs | `ISMAGS` |
| Graph theory and combinatorics | [Junction](../measures/st_junction.html) | ✓ checked, agrees | `junction_tree` |
| Graph theory and combinatorics | [K edge augmentation (connectivity)](../measures/cat_augmentation_edge_k-connectivity.html) | · reported in docs | `k_edge_augmentation` |
| Graph theory and combinatorics | [Kfactor](../measures/st_kfactor.html) | ✓ checked, agrees | `k_factor` |
| Graph theory and combinatorics | [Kfactor edges](../measures/st_kfactor_edges.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Kl](../measures/st_kl.html) | ✓ checked, agrees | `kl_connected_subgraph` |
| Graph theory and combinatorics | [Kosaraju](../measures/nxo_kosaraju.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Kuratowski](../measures/st_kuratowski.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Large clique size](../measures/ap_large_clique_size.html) | ≠ checked, differs by convention | `large_clique_size` |
| Graph theory and combinatorics | [Link prediction](../measures/link_prediction.html) | ✓ checked, agrees | `adamic_adar_index; cn_soundarajan_hopcroft; common_neighbor_centrality; jaccard_coefficient; preferential_attachment; ra_index_soundarajan_hopcroft; resource_allocation_index; within_inter_cluster` |
| Graph theory and combinatorics | [Max weight matching](../measures/max_weight_matching.html) | ✓ checked, agrees | `max_weight_matching` |
| Graph theory and combinatorics | [Maximal matching](../measures/maximal_matching.html) | ✓ checked, agrees | `maximal_matching` |
| Graph theory and combinatorics | [Metric closure (approximate)](../measures/cat_closure_metric-approximate.html) | · reported in docs | `metric_closure` |
| Graph theory and combinatorics | [Min basis](../measures/min_basis.html) | ≠ checked, differs by convention |  |
| Graph theory and combinatorics | [Min basis weights](../measures/min_basis_weights.html) | ≠ checked, differs by convention |  |
| Graph theory and combinatorics | [Min maximal matching (approximate)](../measures/cat_matching_maximal_min-approximate.html) | · reported in docs | `min_maximal_matching` |
| Graph theory and combinatorics | [Min weight matching](../measures/min_weight_matching.html) | ✓ checked, agrees | `min_weight_matching` |
| Graph theory and combinatorics | [Mis](../measures/mis.html) | ✓ checked, agrees | `maximal_independent_set; maximum_independent_set` |
| Graph theory and combinatorics | [Multi Di Graph Matcher](../measures/cat_di_matcher_multi.html) | · reported in docs | `MultiDiGraphMatcher` |
| Graph theory and combinatorics | [Multi Graph Matcher](../measures/cat_matcher_multi.html) | · reported in docs | `MultiGraphMatcher` |
| Graph theory and combinatorics | [Mwm](../measures/st_mwm.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Mwm pairs](../measures/st_mwm_pairs.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Mycielskian](../measures/cat_mycielskian.html) | · reported in docs | `mycielskian` |
| Graph theory and combinatorics | [Node connectivity](../measures/ap_node_connectivity.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Non randomness](../measures/cat_non_randomness.html) | · reported in docs | `non_randomness` |
| Graph theory and combinatorics | [Numerical edge match](../measures/cat_edge_match_numerical.html) | · reported in docs | `numerical_edge_match` |
| Graph theory and combinatorics | [Numerical multiedge match](../measures/cat_match_multiedge_numerical.html) | · reported in docs | `numerical_multiedge_match` |
| Graph theory and combinatorics | [Numerical node match](../measures/cat_match_numerical.html) | · reported in docs | `numerical_node_match` |
| Graph theory and combinatorics | [Nx anneal](../measures/ap_nx_anneal.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Nx ramsey](../measures/ap_nx_ramsey.html) | ✓ checked, agrees | `ramsey_R2` |
| Graph theory and combinatorics | [Nx random](../measures/ap_nx_random.html) | ✓ checked, agrees | `random_graph` |
| Graph theory and combinatorics | [Nxs cycle basis](../measures/nxs_cycle_basis.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Nxs find cycle](../measures/nxs_find_cycle.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Nxs tree lca](../measures/nxs_tree_lca.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [One exchange (approximate)](../measures/cat_exchange_one-approximate.html) | · reported in docs | `one_exchange` |
| Graph theory and combinatorics | [Panther](../measures/panther.html) | ✓ checked, agrees | `panther_similarity; panther_vector_similarity` |
| Graph theory and combinatorics | [Perfect](../measures/st_perfect.html) | ✓ checked, agrees | `is_perfect_graph` |
| Graph theory and combinatorics | [Planar](../measures/st_planar.html) | ✓ checked, agrees | `PlanarEmbedding; check_planarity; is_planar` |
| Graph theory and combinatorics | [Polynomials](../measures/st_polynomials.html) | ✓ checked, agrees | `tutte_polynomial` |
| Graph theory and combinatorics | [Prominent group](../measures/nxo_prominent.html) | ✓ checked, agrees | `prominent_group` |
| Graph theory and combinatorics | [Prufer](../measures/nxs_prufer.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Random cograph](../measures/cat_cograph_random.html) | · reported in docs | `random_cograph` |
| Graph theory and combinatorics | [Random k lift](../measures/cat_k_lift_random.html) | · reported in docs | `random_k_lift` |
| Graph theory and combinatorics | [Random reference](../measures/cat_random_reference.html) | · reported in docs | `random_reference` |
| Graph theory and combinatorics | [Random tournament](../measures/cat_random_tournament.html) | · reported in docs | `random_tournament` |
| Graph theory and combinatorics | [Recursive cycles](../measures/nxs_recursive_cycles.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Regular](../measures/st_regular.html) | ✓ checked, agrees | `is_regular` |
| Graph theory and combinatorics | [S metric](../measures/cat_metric_s.html) | · reported in docs | `s_metric` |
| Graph theory and combinatorics | [Score sequence](../measures/cat_sequence.html) | · reported in docs | `score_sequence` |
| Graph theory and combinatorics | [Simple cycles](../measures/simple_cycles.html) | ✓ checked, agrees | `minimum_cycle_basis; recursive_simple_cycles; simple_cycles` |
| Graph theory and combinatorics | [Simrank](../measures/simrank.html) | ✓ checked, agrees | `simrank_similarity` |
| Graph theory and combinatorics | [St chordal](../measures/st_chordal.html) | ✓ checked, agrees | `chordal_graph_cliques; chordal_graph_treewidth; complete_to_chordal_graph; is_chordal` |
| Graph theory and combinatorics | [St edge cover](../measures/st_edge_cover.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [St tsp](../measures/st_tsp.html) | ✓ checked, agrees | `traveling_salesman_problem` |
| Graph theory and combinatorics | [Threshold graphs](../measures/threshold_graph.html) | · reported in docs | `find_threshold_graph; is_threshold_graph` |
| Graph theory and combinatorics | [Topological sorts](../measures/nxs_topological_sorts.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Tournament](../measures/st_tournament.html) | ✓ checked, agrees | `is_tournament` |
| Graph theory and combinatorics | [Traveling salesman (exact and heuristic)](../measures/tsp.html) | · reported in docs | `asadpour_atsp; christofides; greedy_tsp; simulated_annealing_tsp; threshold_accepting_tsp` |
| Graph theory and combinatorics | [Tree centroid](../measures/nxs_tree_centroid.html) | ✓ checked, agrees | `centroid` |
| Graph theory and combinatorics | [Tree iso](../measures/tree_iso.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Treewidth](../measures/ap_treewidth.html) | ✓ checked, agrees | `treewidth_min_fill_in` |
| Graph theory and combinatorics | [Triads](../measures/st_triads.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Triangle list](../measures/nxs_triangle_list.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Tw min degree](../measures/ap_tw_min_degree.html) | ✓ checked, agrees | `treewidth_min_degree` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | ✓ checked, agrees | `could_be_isomorphic; fast_could_be_isomorphic; faster_could_be_isomorphic; is_isomorphic; rooted_tree_isomorphism; tree_isomorphism; vf2pp_all_isomorphisms; vf2pp_all_monomorphisms; vf2pp_all_subgraph_isomorphisms; vf2pp_is_isomorphic; vf2pp_is_monomorphic; vf2pp_isomorphism` |
| Graph theory and combinatorics | [Voronoi cells](../measures/cat_cells_voronoi.html) | · reported in docs | `voronoi_cells` |
| Graph theory and combinatorics | [Wl hash](../measures/wl_hash.html) | ✓ checked, agrees | `weisfeiler_lehman_graph_hash; weisfeiler_lehman_subgraph_hashes` |
| Graph theory and combinatorics | [Wl subgraph](../measures/wl_subgraph.html) | ✓ checked, agrees |  |
| Input and output | [EDGELIST read and write](../measures/io_edgelist.html) | · reported in docs | `generate_adjlist; generate_edgelist; parse_adjlist; parse_edgelist; read_adjlist; read_edgelist; write_adjlist; write_edgelist` |
| Input and output | [GEXF read and write](../measures/io_gexf.html) | ✓ checked, agrees | `generate_gexf; read_gexf; write_gexf` |
| Input and output | [GML read and write](../measures/io_gml.html) | ✓ checked, agrees | `generate_gml; parse_gml; read_gml; write_gml` |
| Input and output | [GRAPH6 read and write](../measures/io_graph6.html) | · reported in docs | `from_graph6_bytes; from_sparse6_bytes; read_graph6; read_sparse6; to_graph6_bytes; to_sparse6_bytes; write_graph6; write_sparse6` |
| Input and output | [GraphML read and write](../measures/io_graphml.html) | ✓ checked, agrees | `generate_graphml; parse_graphml; read_graphml; write_graphml_lxml; write_graphml_xml` |
| Input and output | [LEDA read and write](../measures/io_leda.html) | · reported in docs | `parse_leda; read_leda` |
| Input and output | [Node-link JSON read and write](../measures/io_json.html) | ✓ checked, agrees |  |
| Input and output | [Pajek .net read and write](../measures/io_pajek.html) | ✓ checked, agrees | `generate_pajek; parse_pajek; read_pajek; write_pajek` |
| Layout | [Circle, tree and two-mode (barycenter) layouts](../measures/layout_simple.html) | · reported in docs |  |
| Layout | [Fruchterman-Reingold layout](../measures/layout_fruchterman_reingold.html) | · reported in docs |  |
| Layout | [Layout stress quality](../measures/layout_stress_quality.html) | ∅ checked, no value on some inputs |  |
| Layout | [Layout stress value](../measures/layout_stress_value.html) | ∅ checked, no value on some inputs |  |
| Layout | [Stress-majorization layout (Kamada-Kawai energy)](../measures/layout_stress.html) | ✓ checked, agrees |  |
| Matrices and spectra | [Adjacency](../measures/gm_adjacency.html) | ✓ checked, agrees | `adjacency_graph; adjacency_matrix` |
| Matrices and spectra | [Bethe hessian](../measures/gm_bethe_hessian.html) | ✓ checked, agrees | `bethe_hessian_matrix` |
| Matrices and spectra | [Class matrix](../measures/gm_class_matrix.html) | ✓ checked, agrees | `attr_matrix` |
| Matrices and spectra | [Estrada index](../measures/estrada_index.html) | · reported in docs | `estrada_index` |
| Matrices and spectra | [Fiedler](../measures/gm_fiedler.html) | ≠ checked, differs by convention | `algebraic_connectivity; fiedler_vector; spectral_bisection` |
| Matrices and spectra | [Gm aperiodic](../measures/gm_aperiodic.html) | ✓ checked, agrees |  |
| Matrices and spectra | [Gm laplacian](../measures/gm_laplacian.html) | ✓ checked, agrees | `directed_combinatorial_laplacian_matrix; directed_laplacian_matrix; laplacian_matrix; normalized_laplacian_matrix` |
| Matrices and spectra | [Gm modularity](../measures/gm_modularity.html) | ✓ checked, agrees | `directed_modularity_matrix; modularity_matrix` |
| Matrices and spectra | [Graph spectrum (eigenvalues of a graph matrix)](../measures/graph_spectrum.html) | · reported in docs | `adjacency_spectrum; bethe_hessian_spectrum; laplacian_spectrum; magnetic_spectrum; modularity_spectrum; normalized_laplacian_spectrum` |
| Matrices and spectra | [Incidence](../measures/gm_incidence.html) | ✓ checked, agrees | `biadjacency_matrix; incidence_matrix` |
| Matrices and spectra | [Magnetic laplacian matrix](../measures/cat_laplacian_magnetic_matrix.html) | · reported in docs | `magnetic_laplacian_matrix` |
| Matrices and spectra | [Spectral graph forge](../measures/cat_forge_spectral.html) | · reported in docs | `spectral_graph_forge` |
| Matrices and spectra | [Tournament matrix](../measures/cat_matrix_tournament.html) | · reported in docs | `tournament_matrix` |
| Mixing and assortativity | [Assort](../measures/assort.html) | ✓ checked, agrees | `degree_pearson_correlation_coefficient` |
| Mixing and assortativity | [Assortativity degree](../measures/assortativity_degree.html) | ✓ checked, agrees |  |
| Mixing and assortativity | [Assortativity nominal](../measures/assortativity_nominal.html) | ≠ checked, differs by convention |  |
| Mixing and assortativity | [Assortativity values](../measures/assortativity_values.html) | ✓ checked, agrees | `attribute_assortativity_coefficient; degree_assortativity_coefficient; numeric_assortativity_coefficient` |
| Mixing and assortativity | [Attribute mixing matrix](../measures/cat_attribute_matrix_mixing.html) | · reported in docs | `attribute_mixing_matrix` |
| Mixing and assortativity | [Avg deg conn](../measures/avg_deg_conn.html) | ≠ checked, differs by convention | `average_degree_connectivity` |
| Mixing and assortativity | [Avg nbr deg](../measures/avg_nbr_deg.html) | ≠ checked, differs by convention | `average_neighbor_degree` |
| Mixing and assortativity | [Degree mixing matrix](../measures/cat_degree_matrix_mixing.html) | · reported in docs | `degree_mixing_matrix` |
| Mixing and assortativity | [Mixing](../measures/mixing.html) | ✓ checked, agrees | `attribute_mixing_dict; degree_mixing_dict` |
| Paths and distances | [Barycenter](../measures/dm_barycenter.html) | ✓ checked, agrees |  |
| Paths and distances | [Center](../measures/dm_center.html) | ✓ checked, agrees | `center` |
| Paths and distances | [Closeness vitality](../measures/dm_closeness_vitality.html) | ✓ checked, agrees | `closeness_vitality` |
| Paths and distances | [Diameter](../measures/diameter.html) | ✓ checked, agrees | `diameter; harmonic_diameter` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees |  |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ✓ checked, agrees | `eccentricity` |
| Paths and distances | [Global and local efficiency](../measures/efficiency_global.html) | · reported in docs | `efficiency; global_efficiency; local_efficiency` |
| Paths and distances | [Index](../measures/dm_index.html) | ✓ checked, agrees | `gutman_index; hyper_wiener_index; schultz_index; wiener_index` |
| Paths and distances | [Is distance regular](../measures/cat_distance_is_regular.html) | · reported in docs | `is_distance_regular` |
| Paths and distances | [Johnson lengths](../measures/nxs_johnson_lengths.html) | ✓ checked, agrees |  |
| Paths and distances | [Local efficiency](../measures/dm_local_efficiency.html) | ✓ checked, agrees |  |
| Paths and distances | [Mean distance](../measures/mean_distance.html) | ✓ checked, agrees | `average_shortest_path_length` |
| Paths and distances | [Paths all pairs](../measures/paths_all_pairs.html) | ✓ checked, agrees | `all_pairs_all_shortest_paths; all_pairs_bellman_ford_path; all_pairs_bellman_ford_path_length; all_pairs_dijkstra; all_pairs_dijkstra_path; all_pairs_dijkstra_path_length; all_pairs_lowest_common_ancestor; all_pairs_node_connectivity; all_pairs_shortest_path; all_pairs_shortest_path_length; floyd_warshall_numpy` |
| Paths and distances | [Paths all shortest](../measures/paths_all_shortest.html) | ✓ checked, agrees | `all_shortest_paths` |
| Paths and distances | [Paths astar](../measures/paths_astar.html) | ✓ checked, agrees | `astar_path; astar_path_length` |
| Paths and distances | [Paths bidirectional](../measures/paths_bidirectional.html) | ✓ checked, agrees | `bidirectional_shortest_path` |
| Paths and distances | [Paths count](../measures/paths_count.html) | ✓ checked, agrees |  |
| Paths and distances | [Paths floyd warshall](../measures/paths_floyd_warshall.html) | ✓ checked, agrees | `floyd_warshall; floyd_warshall_predecessor_and_distance; floyd_warshall_tree` |
| Paths and distances | [Paths johnson](../measures/paths_johnson.html) | ✓ checked, agrees | `johnson` |
| Paths and distances | [Paths k shortest](../measures/paths_k_shortest.html) | ✓ checked, agrees | `shortest_simple_paths` |
| Paths and distances | [Paths multi source](../measures/paths_multi_source.html) | ✓ checked, agrees |  |
| Paths and distances | [Paths negative](../measures/paths_negative.html) | ✓ checked, agrees | `goldberg_radzik` |
| Paths and distances | [Paths negative cycle](../measures/paths_negative_cycle.html) | ✓ checked, agrees | `find_negative_cycle; negative_edge_cycle` |
| Paths and distances | [Paths predecessors](../measures/paths_predecessors.html) | ✓ checked, agrees | `predecessor` |
| Paths and distances | [Paths simple](../measures/paths_simple.html) | ✓ checked, agrees | `all_simple_edge_paths; all_simple_paths` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | ✓ checked, agrees | `bidirectional_dijkstra; dijkstra_path; dijkstra_path_length; dijkstra_predecessor_and_distance; multi_source_dijkstra; multi_source_dijkstra_path; multi_source_dijkstra_path_length; shortest_path; shortest_path_length; single_source_all_shortest_paths; single_source_dijkstra; single_source_dijkstra_path` |
| Paths and distances | [Periphery](../measures/dm_periphery.html) | ✓ checked, agrees | `periphery` |
| Paths and distances | [Radius](../measures/radius.html) | · reported in docs | `radius` |
| Paths and distances | [Reachability](../measures/reachability.html) | ✓ checked, agrees | `has_path; is_reachable` |
| Roles and positions | [Categorical edge match](../measures/cat_categorical_edge_match.html) | · reported in docs | `categorical_edge_match` |
| Roles and positions | [Categorical multiedge match](../measures/cat_categorical_match_multiedge.html) | · reported in docs | `categorical_multiedge_match` |
| Roles and positions | [Categorical node match](../measures/cat_categorical_match.html) | · reported in docs | `categorical_node_match` |
| Roles and positions | [Constraint](../measures/constraint.html) | ≠ checked, differs by convention | `constraint; local_constraint` |
| Roles and positions | [Effective size](../measures/effective_size.html) | ≠ checked, differs by convention | `effective_size` |
| Roles and positions | [Efficiency](../measures/efficiency.html) | ≠ checked, differs by convention |  |
| Statistical fitting | [Constant potts model (community)](../measures/cat_constant_model_potts-community.html) | · reported in docs | `constant_potts_model` |
| Temporal and events | [Time Respecting Di Graph Matcher](../measures/cat_di_matcher_respecting_time.html) | · reported in docs | `TimeRespectingDiGraphMatcher` |
| Temporal and events | [Time Respecting Graph Matcher](../measures/cat_matcher_respecting_time.html) | · reported in docs | `TimeRespectingGraphMatcher` |
| Traversal, trees and DAGs | [All topological](../measures/all_topological.html) | ✓ checked, agrees | `all_topological_sorts` |
| Traversal, trees and DAGs | [Antichain width](../measures/gb_antichain_width.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Astar](../measures/ord_astar.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Beam](../measures/trav_beam.html) | ✓ checked, agrees | `bfs_beam_edges` |
| Traversal, trees and DAGs | [Bellman ford](../measures/ord_bellman_ford.html) | ✓ checked, agrees | `bellman_ford_path; bellman_ford_path_length; bellman_ford_predecessor_and_distance; single_source_bellman_ford; single_source_bellman_ford_path; single_source_bellman_ford_path_length` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | ✓ checked, agrees | `bfs_edges; bfs_predecessors; bfs_successors; bfs_tree; edge_bfs` |
| Traversal, trees and DAGs | [Bfs labeled](../measures/trav_bfs_labeled.html) | ✓ checked, agrees | `bfs_labeled_edges` |
| Traversal, trees and DAGs | [Bfs layers](../measures/trav_bfs_layers.html) | ✓ checked, agrees | `bfs_layers` |
| Traversal, trees and DAGs | [Bidir bfs](../measures/ord_bidir_bfs.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Bidir dijkstra](../measures/ord_bidir_dijkstra.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Binomial tree](../measures/cat_binomial_tree.html) | · reported in docs | `binomial_tree` |
| Traversal, trees and DAGs | [Branching](../measures/branching.html) | ✓ checked, agrees | `maximum_branching; maximum_spanning_arborescence; minimal_branching; minimum_branching; minimum_spanning_arborescence` |
| Traversal, trees and DAGs | [Branching weight](../measures/gb_branching_weight.html) | ✓ checked, agrees | `branching_weight` |
| Traversal, trees and DAGs | [Broadcast time](../measures/gb_broadcast_time.html) | ✓ checked, agrees | `tree_broadcast_time` |
| Traversal, trees and DAGs | [Chain count](../measures/gb_chain_count.html) | ✓ checked, agrees | `chain_decomposition` |
| Traversal, trees and DAGs | [Closure](../measures/closure.html) | ✓ checked, agrees | `transitive_closure; transitive_closure_dag` |
| Traversal, trees and DAGs | [Cycle count](../measures/gb_cycle_count.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [D separated](../measures/gb_d_separated.html) | ✓ checked, agrees | `is_d_separator` |
| Traversal, trees and DAGs | [Dag lca](../measures/dag_lca.html) | ≠ checked, differs by convention | `lowest_common_ancestor; tree_all_pairs_lowest_common_ancestor` |
| Traversal, trees and DAGs | [Dag to branching](../measures/cat_branching_dag_to.html) | · reported in docs | `dag_to_branching` |
| Traversal, trees and DAGs | [Dedensify](../measures/gb_dedensify.html) | ✓ checked, agrees | `dedensify` |
| Traversal, trees and DAGs | [Dfs events](../measures/trav_dfs_events.html) | ✓ checked, agrees | `dfs_labeled_edges` |
| Traversal, trees and DAGs | [Dijkstra](../measures/ord_dijkstra.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Edge bfs](../measures/trav_edge_bfs.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Edge dfs](../measures/trav_edge_dfs.html) | ✓ checked, agrees | `dfs_edges; dfs_postorder_nodes; dfs_predecessors; dfs_preorder_nodes; dfs_successors; dfs_tree; edge_dfs` |
| Traversal, trees and DAGs | [Frontiers](../measures/frontiers.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Gb aperiodic](../measures/gb_aperiodic.html) | ✓ checked, agrees | `is_aperiodic` |
| Traversal, trees and DAGs | [Gb disjoint paths](../measures/gb_disjoint_paths.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Generations](../measures/generations.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Idom](../measures/idom.html) | ✓ checked, agrees | `dominance_frontiers; immediate_dominators` |
| Traversal, trees and DAGs | [Is dag](../measures/is_dag.html) | ✓ checked, agrees | `is_directed_acyclic_graph` |
| Traversal, trees and DAGs | [Is eulerian](../measures/gb_is_eulerian.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Isolates](../measures/gb_isolates.html) | ✓ checked, agrees | `isolates; number_of_isolates` |
| Traversal, trees and DAGs | [Join trees](../measures/cat_join_tree.html) | · reported in docs | `join_trees` |
| Traversal, trees and DAGs | [K edge subgraphs](../measures/gb_k_edge_subgraphs.html) | ✓ checked, agrees | `k_edge_subgraphs` |
| Traversal, trees and DAGs | [Lex topo](../measures/gb_lex_topo.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Lexicographic](../measures/lexicographic.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Longest length](../measures/longest_length.html) | ✓ checked, agrees | `dag_longest_path_length` |
| Traversal, trees and DAGs | [Longest path](../measures/longest_path.html) | ✓ checked, agrees | `dag_longest_path` |
| Traversal, trees and DAGs | [Longest path len](../measures/gb_longest_path_len.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Maxflow](../measures/gb_maxflow.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Mcb weight](../measures/gb_mcb_weight.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Mincost](../measures/gb_mincost.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Moral edges](../measures/gb_moral_edges.html) | ✓ checked, agrees | `moral_graph` |
| Traversal, trees and DAGs | [Mst weight](../measures/gb_mst_weight.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Node boundary](../measures/gb_node_boundary.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Number of nonisomorphic trees](../measures/cat_nonisomorphic_tree.html) | · reported in docs | `number_of_nonisomorphic_trees` |
| Traversal, trees and DAGs | [Quotient internal](../measures/gb_quotient_internal.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Random labeled rooted forest](../measures/cat_forest_labeled_random_rooted.html) | · reported in docs | `random_labeled_rooted_forest` |
| Traversal, trees and DAGs | [Random powerlaw tree](../measures/cat_powerlaw_random_tree.html) | · reported in docs | `random_powerlaw_tree` |
| Traversal, trees and DAGs | [Random powerlaw tree sequence](../measures/cat_powerlaw_random_sequence_tree.html) | · reported in docs | `random_powerlaw_tree_sequence` |
| Traversal, trees and DAGs | [Random spanning tree](../measures/random_spanning_tree.html) | · reported in docs | `random_spanning_tree` |
| Traversal, trees and DAGs | [Random unlabeled rooted forest](../measures/cat_forest_random_rooted_unlabeled.html) | · reported in docs | `random_unlabeled_rooted_forest` |
| Traversal, trees and DAGs | [Random walks](../measures/random_walk.html) | · reported in docs | `generate_random_paths; random_walk` |
| Traversal, trees and DAGs | [Reduction](../measures/reduction.html) | ✓ checked, agrees | `transitive_reduction` |
| Traversal, trees and DAGs | [Rst edge freq](../measures/rst_edge_freq.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Snap groups](../measures/gb_snap_groups.html) | ✓ checked, agrees | `snap_aggregation` |
| Traversal, trees and DAGs | [Spanner ok](../measures/gb_spanner_ok.html) | ✓ checked, agrees | `spanner` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | ✓ checked, agrees | `maximum_spanning_edges; maximum_spanning_tree; minimum_spanning_edges; minimum_spanning_tree` |
| Traversal, trees and DAGs | [Spanning trees](../measures/gb_spanning_trees.html) | ✓ checked, agrees | `number_of_spanning_trees` |
| Traversal, trees and DAGs | [Spanning weight](../measures/spanning_weight.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Steiner tree](../measures/steiner_tree.html) | · reported in docs | `steiner_tree` |
| Traversal, trees and DAGs | [Stoer wagner](../measures/gb_stoer_wagner.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Topo levels](../measures/gb_topo_levels.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Topological sort](../measures/topological_sort.html) | ✓ checked, agrees | `lexicographical_topological_sort; topological_generations; topological_sort` |
| Traversal, trees and DAGs | [Tree broadcast center](../measures/cat_broadcast_center_tree.html) | · reported in docs | `tree_broadcast_center` |
| Traversal, trees and DAGs | [Tree lca](../measures/tree_lca.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Walks](../measures/gb_walks.html) | ✓ checked, agrees | `number_of_walks` |
| Two-mode and bipartite | [Bipartite color](../measures/bipartite_color.html) | ✓ checked, agrees | `is_bipartite` |
| Two-mode and bipartite | [Bipartite modularity](../measures/bipartite_modularity.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Birank](../measures/birank.html) | ✓ checked, agrees | `birank` |
| Two-mode and bipartite | [Butterflies](../measures/butterflies.html) | ✓ checked, agrees | `butterflies` |
| Two-mode and bipartite | [Ego members](../measures/ego_members.html) | ✓ checked, agrees | `ego_graph` |
| Two-mode and bipartite | [Ego\_summary / betweenness](../measures/ego_summary-betweenness.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Ego\_summary / components](../measures/ego_summary-components.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Ego\_summary / density](../measures/ego_summary-density.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Ego\_summary / ties](../measures/ego_summary-ties.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Hopcroft karp](../measures/hopcroft_karp.html) | ✓ checked, agrees | `eppstein_matching; hopcroft_karp_matching` |
| Two-mode and bipartite | [Is bipartite node set (bipartite)](../measures/cat_bipartite_is_set-bipartite.html) | · reported in docs | `is_bipartite_node_set` |
| Two-mode and bipartite | [Latapy clustering](../measures/latapy_clustering.html) | ✓ checked, agrees | `latapy_clustering` |
| Two-mode and bipartite | [Maximal extendability](../measures/maximal_extendability.html) | ✓ checked, agrees | `maximal_extendability` |
| Two-mode and bipartite | [Min weight full matching](../measures/min_weight_full_matching.html) | ✓ checked, agrees | `minimum_weight_full_matching` |
| Two-mode and bipartite | [Node redundancy](../measures/node_redundancy.html) | ✓ checked, agrees | `node_redundancy` |
| Two-mode and bipartite | [Nx eppstein](../measures/nx_eppstein.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Nx eppstein size](../measures/nx_eppstein_size.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Nx hk mates](../measures/nx_hk_mates.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Project](../measures/project.html) | ∅ checked, no value on some inputs | `collaboration_weighted_projected_graph; generic_weighted_projected_graph; overlap_weighted_projected_graph; projected_graph; weighted_projected_graph` |
| Two-mode and bipartite | [Projection](../measures/projection.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Robins alexander](../measures/robins_alexander.html) | ✓ checked, agrees | `robins_alexander_clustering` |
| Two-mode and bipartite | [Spectral bipartivity](../measures/spectral_bipartivity.html) | ✓ checked, agrees | `spectral_bipartivity` |
| Two-mode and bipartite | [Twomode / betweenness](../measures/twomode-betweenness.html) | ∅ checked, no value on some inputs |  |
| Two-mode and bipartite | [Twomode / closeness](../measures/twomode-closeness.html) | ≠ checked, differs by convention |  |
| Two-mode and bipartite | [Twomode / degree](../measures/twomode-degree.html) | ∅ checked, no value on some inputs |  |
| Two-mode and bipartite | [Twomode / density](../measures/twomode-density.html) | ∅ checked, no value on some inputs |  |
| Two-mode and bipartite | [Vertex cover](../measures/vertex_cover.html) | ✓ checked, agrees | `min_weighted_vertex_cover; to_vertex_cover` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F001](../findings.html#f001) | defect | group\_betweenness\_centrality compares float path lengths exactly |
| [F002](../findings.html#f002) | defect | prominent\_group misses the best group on disconnected graphs |
| [F003](../findings.html#f003) | defect | graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost |
| [F004](../findings.html#f004) | defect | goldberg\_radzik raises NetworkXUnbounded for any negative self-loop |
| [F005](../findings.html#f005) | convention | PageRank stops on an L1 change below n \* tol |
| [F007](../findings.html#f007) | convention | Undirected self-loop is one arc |
| [F023](../findings.html#f023) | defect | hyper\_wiener\_index is twice the published value |
| [F024](../findings.html#f024) | defect | edge\_betweenness\_centrality\_subset deviates from its documented formula |
| [F025](../findings.html#f025) | defect | effective\_size is wrong for weighted or directed graphs on its vectorized path |
| [F026](../findings.html#f026) | defect | Network simplex can misreport feasibility with float weights |
| [F027](../findings.html#f027) | defect | maximum\_spanning\_arborescence occasionally misses the maximum |
| [F028](../findings.html#f028) | limitation | k\_edge\_components hits the recursion limit near n = 1000 |
| [F029](../findings.html#f029) | convention | Ties are broken by Python set or insertion order |
| [F030](../findings.html#f030) | defect | group\_betweenness\_centrality can vary with PYTHONHASHSEED |
| [F031](../findings.html#f031) | defect | approximation.node\_connectivity starts from a bound that can exceed the connectivity |
| [F032](../findings.html#f032) | convention | cd\_index pools every citer of the references, whatever its time |
| [F033](../findings.html#f033) | convention | Weighted betweenness counts one shortest path per neighbour pair with parallel edges |
| [F034](../findings.html#f034) | convention | hypercube\_graph nodes are bit tuples; dimension 0 is the null graph |
| [F035](../findings.html#f035) | convention | Returns 0 for modularity, Louvain, density and nominal assortativity on edgeless input |
{% endraw %}
