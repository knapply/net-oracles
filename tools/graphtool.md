---
title: "graph-tool"
layout: default
parent: Tools
---

{% raw %}
# graph-tool

| Field | Value |
|---|---|
| Identifier | `graphtool` |
| Language | C++ / Python |
| Version tested | 3.9 |
| License | LGPL-3.0-or-later |
| Homepage | <https://graph-tool.skewed.de> |
| Role | checked |
| Citation | [peixoto2014graphtool](../references.html#peixoto2014graphtool) |

## How it was run

Imported in CPython from a container image with the tool installed; public functions called on Graph objects.

Capabilities listed by introspection of graph-tool public classes and functions.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 3 |
| reported in docs (·) | 165 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | · reported in docs | `betweenness` |
| Centrality | [Closeness](../measures/closeness.html) | · reported in docs | `closeness` |
| Centrality | [Edge percolation](../measures/cat_edge_percolation.html) | · reported in docs | `edge_percolation` |
| Centrality | [Eigenvector](../measures/eigenvector.html) | · reported in docs | `eigenvector` |
| Centrality | [Hits](../measures/hits.html) | · reported in docs | `hits` |
| Centrality | [Katz](../measures/katz.html) | · reported in docs | `katz` |
| Centrality | [Pagerank](../measures/pagerank.html) | · reported in docs | `pagerank` |
| Centrality | [Percolation](../measures/cx_percolation.html) | · reported in docs | `vertex_percolation` |
| Cohesion and subgroups | [Clique State](../measures/cat_clique_state.html) | · reported in docs | `CliqueState` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | · reported in docs | `kcore_decomposition` |
| Cohesion and subgroups | [Generate triadic closure](../measures/cat_closure_generate_triadic.html) | · reported in docs | `generate_triadic_closure` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | · reported in docs | `max_cliques` |
| Cohesion and subgroups | [Motif census](../measures/motif_census.html) | · reported in docs | `motif_significance; motifs` |
| Communities | [Modularity](../measures/modularity.html) | · reported in docs | `modularity` |
| Communities | [Modularity State](../measures/cat_modularity_state.html) | · reported in docs | `ModularityState` |
| Communities | [Nested partition overlap](../measures/cat_nested_overlap_partition.html) | · reported in docs | `nested_partition_overlap` |
| Communities | [Nested partition overlap center](../measures/cat_center_nested_overlap_partition.html) | · reported in docs | `nested_partition_overlap_center` |
| Communities | [Partition Centroid State](../measures/cat_centroid_partition_state.html) | · reported in docs | `PartitionCentroidState` |
| Communities | [Partition entropy](../measures/cat_entropy_partition.html) | · reported in docs | `partition_entropy` |
| Communities | [Partition Mode State](../measures/cat_mode_partition_state.html) | · reported in docs | `PartitionModeState` |
| Communities | [Partition overlap](../measures/cat_overlap_partition.html) | · reported in docs | `partition_overlap` |
| Communities | [Partition overlap center](../measures/cat_center_overlap_partition.html) | · reported in docs | `partition_overlap_center` |
| Components and connectivity | [Average node](../measures/average_node.html) | · reported in docs | `vertex_average` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | · reported in docs | `label_biconnected_components` |
| Components and connectivity | [Condensation](../measures/condensation.html) | · reported in docs | `condensation_graph` |
| Components and connectivity | [Max flow](../measures/max_flow.html) | · reported in docs | `boykov_kolmogorov_max_flow; edmonds_karp_max_flow; push_relabel_max_flow` |
| Components and connectivity | [Min cut](../measures/min_cut.html) | · reported in docs | `min_cut; min_st_cut` |
| Components and connectivity | [Norm Cut State](../measures/cat_cut_norm_state.html) | · reported in docs | `NormCutState` |
| Data transforms | [Graph sym difference](../measures/cat_difference_sym.html) | · reported in docs | `graph_sym_difference` |
| Data transforms | [Line graph](../measures/line_graph.html) | · reported in docs | `line_graph` |
| Data transforms | [Op difference](../measures/op_difference.html) | · reported in docs | `graph_difference` |
| Data transforms | [Op intersection](../measures/op_intersection.html) | · reported in docs | `graph_intersection` |
| Data transforms | [Op union](../measures/op_union.html) | · reported in docs | `graph_union` |
| Descriptive statistics | [Clustering](../measures/clustering.html) | · reported in docs | `local_clustering` |
| Descriptive statistics | [Components](../measures/components.html) | · reported in docs | `extract_largest_component; label_components; label_largest_component; label_out_component` |
| Descriptive statistics | [Generate knn](../measures/cat_generate_knn.html) | · reported in docs | `generate_knn` |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | · reported in docs | `edge_reciprocity` |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | · reported in docs | `global_clustering` |
| Descriptive statistics | [Trust transitivity](../measures/cat_transitivity_trust.html) | · reported in docs | `trust_transitivity` |
| Generators and rewiring | [Contingency graph](../measures/cat_contingency.html) | · reported in docs | `contingency_graph` |
| Generators and rewiring | [Deterministic generators](../measures/deterministic_generators.html) | · reported in docs | `circular_graph; complete_graph` |
| Generators and rewiring | [Extended clustering](../measures/cat_clustering_extended.html) | · reported in docs | `extended_clustering` |
| Generators and rewiring | [Lattice generator](../measures/gen_lattice.html) | · reported in docs | `lattice` |
| Generators and rewiring | [Mutual information](../measures/cat_information_mutual.html) | · reported in docs | `mutual_information` |
| Generators and rewiring | [Preferential attachment generator](../measures/gen_preferential.html) | · reported in docs | `price_network` |
| Generators and rewiring | [Random edge addition and removal](../measures/random_edge_edit.html) | · reported in docs | `add_random_edges; remove_random_edges` |
| Generators and rewiring | [Random geometric graph generator](../measures/gen_geometric.html) | · reported in docs | `geometric_graph` |
| Generators and rewiring | [Reduced mutual information](../measures/cat_information_mutual_reduced.html) | · reported in docs | `reduced_mutual_information` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `generate_maxent_sbm; generate_sbm; solve_sbm_fugacities` |
| Generators and rewiring | [Swap contract](../measures/swap_contract.html) | · reported in docs | `random_rewire` |
| Generators and rewiring | [Variation information](../measures/cat_information_variation.html) | · reported in docs | `variation_information` |
| Graph theory and combinatorics | [Axelrod State](../measures/cat_axelrod_state.html) | · reported in docs | `AxelrodState` |
| Graph theory and combinatorics | [Binary Threshold State](../measures/cat_binary_state_threshold.html) | · reported in docs | `BinaryThresholdState` |
| Graph theory and combinatorics | [Boolean State](../measures/cat_boolean_state.html) | · reported in docs | `BooleanState` |
| Graph theory and combinatorics | [Central point dominance](../measures/cat_central_dominance_point.html) | · reported in docs | `central_point_dominance` |
| Graph theory and combinatorics | [CIsing Glauber Block State](../measures/cat_block_c_glauber_ising_state.html) | · reported in docs | `CIsingGlauberBlockState` |
| Graph theory and combinatorics | [CIsing Glauber State](../measures/cat_c_glauber_ising_state.html) | · reported in docs | `CIsingGlauberState` |
| Graph theory and combinatorics | [Draw Block State](../measures/cat_block_draw_state.html) | · reported in docs | `DrawBlockState` |
| Graph theory and combinatorics | [Edge average](../measures/cat_average_edge.html) | · reported in docs | `edge_average` |
| Graph theory and combinatorics | [Em infer](../measures/cat_em_infer.html) | · reported in docs | `em_infer` |
| Graph theory and combinatorics | [EMBlock State](../measures/cat_block_em_state.html) | · reported in docs | `EMBlockState` |
| Graph theory and combinatorics | [Epidemics Block State](../measures/cat_block_epidemics_state.html) | · reported in docs | `EpidemicsBlockState` |
| Graph theory and combinatorics | [Gen Potts BPState](../measures/cat_bp_gen_potts_state.html) | · reported in docs | `GenPottsBPState` |
| Graph theory and combinatorics | [Generalized Binary State](../measures/cat_binary_generalized_state.html) | · reported in docs | `GeneralizedBinaryState` |
| Graph theory and combinatorics | [Get block edge gradient](../measures/cat_block_edge_gradient.html) | · reported in docs | `get_block_edge_gradient` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | · reported in docs | `sequential_vertex_coloring` |
| Graph theory and combinatorics | [Ising BPState](../measures/cat_bp_ising_state.html) | · reported in docs | `IsingBPState` |
| Graph theory and combinatorics | [Ising Glauber Block State](../measures/cat_block_glauber_ising_state.html) | · reported in docs | `IsingGlauberBlockState` |
| Graph theory and combinatorics | [Ising Glauber State](../measures/cat_glauber_ising_state.html) | · reported in docs | `IsingGlauberState` |
| Graph theory and combinatorics | [Ising Metropolis State](../measures/cat_ising_metropolis_state.html) | · reported in docs | `IsingMetropolisState` |
| Graph theory and combinatorics | [Kirman State](../measures/cat_kirman_state.html) | · reported in docs | `KirmanState` |
| Graph theory and combinatorics | [Kuramoto State](../measures/cat_kuramoto_state.html) | · reported in docs | `KuramotoState` |
| Graph theory and combinatorics | [Linear Normal Block State](../measures/cat_block_linear_normal_state.html) | · reported in docs | `LinearNormalBlockState` |
| Graph theory and combinatorics | [Linear Normal State](../measures/cat_linear_normal_state.html) | · reported in docs | `LinearNormalState` |
| Graph theory and combinatorics | [Linear State](../measures/cat_linear_state.html) | · reported in docs | `LinearState` |
| Graph theory and combinatorics | [Link prediction](../measures/link_prediction.html) | · reported in docs | `similarity; vertex_similarity` |
| Graph theory and combinatorics | [LVBlock State](../measures/cat_block_lv_state.html) | · reported in docs | `LVBlockState` |
| Graph theory and combinatorics | [LVState](../measures/cat_lv_state.html) | · reported in docs | `LVState` |
| Graph theory and combinatorics | [Majority Voter State](../measures/cat_majority_state_voter.html) | · reported in docs | `MajorityVoterState` |
| Graph theory and combinatorics | [Marginal graph lprob](../measures/cat_lprob_marginal.html) | · reported in docs | `marginal_graph_lprob` |
| Graph theory and combinatorics | [Marginal graph sample](../measures/cat_marginal_sample.html) | · reported in docs | `marginal_graph_sample` |
| Graph theory and combinatorics | [Marginal multigraph entropy](../measures/cat_entropy_marginal_multigraph.html) | · reported in docs | `marginal_multigraph_entropy` |
| Graph theory and combinatorics | [Marginal multigraph lprob](../measures/cat_lprob_marginal_multigraph.html) | · reported in docs | `marginal_multigraph_lprob` |
| Graph theory and combinatorics | [Marginal multigraph sample](../measures/cat_marginal_multigraph_sample.html) | · reported in docs | `marginal_multigraph_sample` |
| Graph theory and combinatorics | [Max weight matching](../measures/max_weight_matching.html) | · reported in docs | `max_cardinality_matching` |
| Graph theory and combinatorics | [Measured Block State](../measures/cat_block_measured_state.html) | · reported in docs | `MeasuredBlockState` |
| Graph theory and combinatorics | [Measured Closure Block State](../measures/cat_block_closure_measured_state.html) | · reported in docs | `MeasuredClosureBlockState` |
| Graph theory and combinatorics | [Mf entropy](../measures/cat_entropy_mf.html) | · reported in docs | `mf_entropy` |
| Graph theory and combinatorics | [Microstate entropy](../measures/cat_entropy_microstate.html) | · reported in docs | `microstate_entropy` |
| Graph theory and combinatorics | [Mis](../measures/mis.html) | · reported in docs | `max_independent_vertex_set` |
| Graph theory and combinatorics | [Mixed Measured Block State](../measures/cat_block_measured_mixed_state.html) | · reported in docs | `MixedMeasuredBlockState` |
| Graph theory and combinatorics | [Mode Cluster State](../measures/cat_cluster_mode_state.html) | · reported in docs | `ModeClusterState` |
| Graph theory and combinatorics | [Nested Block State](../measures/cat_block_nested_state.html) | · reported in docs | `NestedBlockState` |
| Graph theory and combinatorics | [Normal BPState](../measures/cat_bp_normal_state.html) | · reported in docs | `NormalBPState` |
| Graph theory and combinatorics | [Normal Glauber Block State](../measures/cat_block_glauber_normal_state.html) | · reported in docs | `NormalGlauberBlockState` |
| Graph theory and combinatorics | [Normal State](../measures/cat_normal_state.html) | · reported in docs | `NormalState` |
| Graph theory and combinatorics | [Nx random](../measures/ap_nx_random.html) | · reported in docs | `random_graph` |
| Graph theory and combinatorics | [Openmp context](../measures/cat_context_openmp.html) | · reported in docs | `openmp_context` |
| Graph theory and combinatorics | [Overlap Block State](../measures/cat_block_overlap_state.html) | · reported in docs | `OverlapBlockState` |
| Graph theory and combinatorics | [Planar](../measures/st_planar.html) | · reported in docs | `is_planar` |
| Graph theory and combinatorics | [Planarity testing, embedding and straight-line drawing](../measures/planarity.html) | · reported in docs | `make_maximal_planar` |
| Graph theory and combinatorics | [Potts Glauber Block State](../measures/cat_block_glauber_potts_state.html) | · reported in docs | `PottsGlauberBlockState` |
| Graph theory and combinatorics | [Potts Glauber State](../measures/cat_glauber_potts_state.html) | · reported in docs | `PottsGlauberState` |
| Graph theory and combinatorics | [Potts Metropolis State](../measures/cat_metropolis_potts_state.html) | · reported in docs | `PottsMetropolisState` |
| Graph theory and combinatorics | [Potts State](../measures/cat_potts_state.html) | · reported in docs | `PottsState` |
| Graph theory and combinatorics | [PPBlock State](../measures/cat_block_pp_state.html) | · reported in docs | `PPBlockState` |
| Graph theory and combinatorics | [Pseudo CIsing Block State](../measures/cat_block_c_ising_pseudo_state.html) | · reported in docs | `PseudoCIsingBlockState` |
| Graph theory and combinatorics | [Pseudo Ising Block State](../measures/cat_block_ising_pseudo_state.html) | · reported in docs | `PseudoIsingBlockState` |
| Graph theory and combinatorics | [Pseudo Normal Block State](../measures/cat_block_normal_pseudo_state.html) | · reported in docs | `PseudoNormalBlockState` |
| Graph theory and combinatorics | [Pseudo Potts Block State](../measures/cat_block_potts_pseudo_state.html) | · reported in docs | `PseudoPottsBlockState` |
| Graph theory and combinatorics | [Ranked Block State](../measures/cat_block_ranked_state.html) | · reported in docs | `RankedBlockState` |
| Graph theory and combinatorics | [Simple cycles](../measures/simple_cycles.html) | · reported in docs | `all_circuits` |
| Graph theory and combinatorics | [SIRSState](../measures/cat_sirs_state.html) | · reported in docs | `SIRSState` |
| Graph theory and combinatorics | [SIRState](../measures/cat_sir_state.html) | · reported in docs | `SIRState` |
| Graph theory and combinatorics | [SISState](../measures/cat_sis_state.html) | · reported in docs | `SISState` |
| Graph theory and combinatorics | [SIState](../measures/cat_si_state.html) | · reported in docs | `SIState` |
| Graph theory and combinatorics | [Triangulation](../measures/cat_triangulation.html) | · reported in docs | `triangulation` |
| Graph theory and combinatorics | [Tsp tour](../measures/cat_tour_tsp.html) | · reported in docs | `tsp_tour` |
| Graph theory and combinatorics | [Uncertain Block State](../measures/cat_block_state_uncertain.html) | · reported in docs | `UncertainBlockState` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | · reported in docs | `isomorphism; subgraph_isomorphism` |
| Graph theory and combinatorics | [Voter State](../measures/cat_state_voter.html) | · reported in docs | `VoterState` |
| Graph theory and combinatorics | [Weighted Block State](../measures/cat_block_state_weighted.html) | · reported in docs | `WeightedBlockState` |
| Graph theory and combinatorics | [Weighted Overlap Block State](../measures/cat_block_overlap_state_weighted.html) | · reported in docs | `WeightedOverlapBlockState` |
| Inference (QAP, null models) | [Mcmc anneal](../measures/cat_anneal_mcmc.html) | · reported in docs | `mcmc_anneal` |
| Inference (QAP, null models) | [Mcmc equilibrate](../measures/cat_equilibrate_mcmc.html) | · reported in docs | `mcmc_equilibrate` |
| Matrices and spectra | [Adjacency](../measures/gm_adjacency.html) | · reported in docs | `adjacency` |
| Matrices and spectra | [Bethe entropy](../measures/cat_bethe_entropy.html) | · reported in docs | `bethe_entropy` |
| Matrices and spectra | [Eigentrust](../measures/cat_eigentrust.html) | · reported in docs | `eigentrust` |
| Matrices and spectra | [Gm laplacian](../measures/gm_laplacian.html) | · reported in docs | `laplacian` |
| Matrices and spectra | [Gm modularity](../measures/gm_modularity.html) | · reported in docs | `modularity_matrix` |
| Matrices and spectra | [Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence)](../measures/matrix_operators.html) | · reported in docs | `AdjacencyOperator; CompactHashimotoOperator; HashimotoOperator; IncidenceOperator; LaplacianOperator; TransitionOperator; hashimoto; transition` |
| Matrices and spectra | [Incidence](../measures/gm_incidence.html) | · reported in docs | `incidence` |
| Mixing and assortativity | [Assortativity values](../measures/assortativity_values.html) | · reported in docs | `assortativity; scalar_assortativity` |
| Mixing and assortativity | [Degree and property correlation histograms](../measures/correlation_histograms.html) | · reported in docs | `avg_combined_corr; avg_neighbor_corr; combined_corr_hist; corr_hist; edge_hist; vertex_hist` |
| Paths and distances | [Bfs iterator](../measures/cat_bfs_iterator.html) | · reported in docs | `bfs_iterator` |
| Paths and distances | [Diameter](../measures/diameter.html) | · reported in docs | `pseudo_diameter` |
| Paths and distances | [Distance histogram](../measures/cat_distance_histogram.html) | · reported in docs | `distance_histogram` |
| Paths and distances | [Paths all shortest](../measures/paths_all_shortest.html) | · reported in docs | `all_shortest_paths` |
| Paths and distances | [Paths astar](../measures/paths_astar.html) | · reported in docs | `astar_iterator; astar_search` |
| Paths and distances | [Paths count](../measures/paths_count.html) | · reported in docs | `count_shortest_paths` |
| Paths and distances | [Paths simple](../measures/paths_simple.html) | · reported in docs | `all_paths` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `all_predecessors; dijkstra_iterator; dijkstra_search; random_shortest_path; shortest_distance; shortest_path` |
| Roles and positions | [Minimize nested blockmodel dl](../measures/cat_blockmodel_dl_minimize_nested.html) | · reported in docs | `minimize_nested_blockmodel_dl` |
| Signed and multilayer | [Layered Block State](../measures/cat_block_layered_state.html) | · reported in docs | `LayeredBlockState` |
| Signed and multilayer | [Layered Overlap Block State](../measures/cat_block_layered_overlap_state.html) | · reported in docs | `LayeredOverlapBlockState` |
| Signed and multilayer | [Layered Weighted Block State](../measures/cat_block_layered_state_weighted.html) | · reported in docs | `LayeredWeightedBlockState` |
| Signed and multilayer | [Layered Weighted Overlap Block State](../measures/cat_block_layered_overlap_state_weighted.html) | · reported in docs | `LayeredWeightedOverlapBlockState` |
| Statistical fitting | [Latent Closure Block State](../measures/cat_block_closure_latent_state.html) | · reported in docs | `LatentClosureBlockState` |
| Statistical fitting | [Latent Mask Block State](../measures/cat_block_latent_mask_state.html) | · reported in docs | `LatentMaskBlockState` |
| Statistical fitting | [Latent multigraph](../measures/cat_latent_multigraph.html) | · reported in docs | `latent_multigraph` |
| Statistical fitting | [Latent Multigraph Block State](../measures/cat_block_latent_multigraph_state.html) | · reported in docs | `LatentMultigraphBlockState` |
| Statistical fitting | [Sbm description length](../measures/sbm_description_length.html) | ✓ checked, agrees | `BlockState` |
| Statistical fitting | [Sbm fit](../measures/sbm_fit.html) | ✓ checked, agrees | `minimize_blockmodel_dl` |
| Statistical fitting | [Sbm move delta](../measures/sbm_move_delta.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Bellman ford](../measures/ord_bellman_ford.html) | · reported in docs | `bellman_ford_search` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `bfs_search` |
| Traversal, trees and DAGs | [Closure](../measures/closure.html) | · reported in docs | `transitive_closure` |
| Traversal, trees and DAGs | [Dfs iterator](../measures/cat_dfs_iterator.html) | · reported in docs | `dfs_iterator` |
| Traversal, trees and DAGs | [Edge dfs](../measures/trav_edge_dfs.html) | · reported in docs | `dfs_search` |
| Traversal, trees and DAGs | [Get hierarchy tree](../measures/cat_hierarchy_tree.html) | · reported in docs | `get_hierarchy_tree` |
| Traversal, trees and DAGs | [Idom](../measures/idom.html) | · reported in docs | `dominator_tree` |
| Traversal, trees and DAGs | [Is dag](../measures/is_dag.html) | · reported in docs | `is_DAG` |
| Traversal, trees and DAGs | [Predecessor tree](../measures/cat_predecessor_tree.html) | · reported in docs | `predecessor_tree` |
| Traversal, trees and DAGs | [Random spanning tree](../measures/random_spanning_tree.html) | · reported in docs | `random_spanning_tree` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | · reported in docs | `min_spanning_tree` |
| Traversal, trees and DAGs | [Topological sort](../measures/topological_sort.html) | · reported in docs | `topological_sort` |
| Two-mode and bipartite | [Bipartite color](../measures/bipartite_color.html) | · reported in docs | `is_bipartite` |
| Two-mode and bipartite | [Projection](../measures/projection.html) | · reported in docs | `graph_projection` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F090](../findings.html#f090) | convention | Betweenness normalization can differ by a factor 2 from the Freeman convention |
{% endraw %}
