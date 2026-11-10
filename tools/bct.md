---
title: "BCT (Octave)"
layout: default
parent: Tools
---

{% raw %}
# BCT (Octave)

| Field | Value |
|---|---|
| Identifier | `bct` |
| Language | MATLAB code under Octave |
| Version tested | 2019-03-03 |
| License | not stated on the distribution site |
| Homepage | <https://www.brain-connectivity-toolbox.net> |
| Role | checked |
| Citation | [rubinov2010complex](../references.html#rubinov2010complex) |

## How it was run

The 2019-03-03 .m files run under GNU Octave 10.3 on binary or weighted adjacency matrices.

Capabilities listed by introspection of bctpy public functions (the Python port of the Brain Connectivity Toolbox function set).

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 1 |
| checked, differs by convention (≠) | 13 |
| reported in docs (·) | 58 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | ≠ checked, differs by convention | `betweenness_bin; betweenness_wei` |
| Centrality | Betweenness, load and flow | [Edge betweenness](../measures/centrality/edge_betweenness.html) | [Edge betweenness](../measures/centrality/edge_betweenness.html#edge_betweenness) | · reported in docs | `edge_betweenness_bin; edge_betweenness_wei` |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | ≠ checked, differs by convention | `degrees_dir; degrees_und; strengths_dir; strengths_und; strengths_und_sign` |
| Centrality | Local and structural scores | [Diffusion centrality and diffusion degree](../measures/centrality/diffusion_centrality.html) | [Diffusion efficiency](../measures/centrality/diffusion_centrality.html#cat_diffusion_efficiency) | · reported in docs | `diffusion_efficiency` |
| Centrality | Spectral and walk-based | [Communicability](../measures/centrality/communicability.html) | [Communicability](../measures/centrality/communicability.html#cx_communicability) | · reported in docs | `subgraph_centrality` |
| Centrality | Spectral and walk-based | [Eigenvector centrality](../measures/centrality/eigenvector_centrality.html) | [Eigenvector](../measures/centrality/eigenvector_centrality.html#eigenvector) | · reported in docs | `eigenvector_centrality_und` |
| Centrality | Spectral and walk-based | [PageRank](../measures/centrality/pagerank.html) | [Nxp pagerank](../measures/centrality/pagerank.html#nxp_pagerank) | · reported in docs | `pagerank_centrality` |
| Cohesion and subgroups | Cores, trusses and cohesive blocks | [K-core decomposition](../measures/cohesion-and-subgroups/k_core.html) | [Coreness](../measures/cohesion-and-subgroups/k_core.html#coreness) | ≠ checked, differs by convention | `kcore_bd; kcore_bu; kcoreness_centrality_bd; kcoreness_centrality_bu` |
| Cohesion and subgroups | Triads, motifs and local structure | [Motif census](../measures/cohesion-and-subgroups/motif_census.html) | [Motif census](../measures/cohesion-and-subgroups/motif_census.html#motif_census) | · reported in docs | `find_motif34; motif3funct_bin; motif3funct_wei; motif3struct_bin; motif3struct_wei; motif4funct_bin; motif4funct_wei; motif4struct_bin; motif4struct_wei` |
| Communities | Modularity-based detection | [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](../measures/communities/modularity_maximization.html) | [Louvain modularity](../measures/communities/modularity_maximization.html#louvain_modularity) | · reported in docs | `community_louvain; modularity_finetune_dir; modularity_finetune_und; modularity_finetune_und_sign; modularity_louvain_dir; modularity_louvain_und; modularity_louvain_und_sign; modularity_probtune_und_sign` |
| Communities | Other detection algorithms | [Clique percolation communities](../measures/communities/clique_percolation.html) | [Clique communities](../measures/communities/clique_percolation.html#cat_clique_community) | · reported in docs | `clique_communities` |
| Communities | Other detection algorithms | [Link communities](../measures/communities/link_communities.html) | [Link communities](../measures/communities/link_communities.html#cat_community_link) | · reported in docs | `link_communities` |
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | · reported in docs | `modularity_dir; modularity_und; modularity_und_sign` |
| Communities | Partition comparison and operations | [Agreement and consensus of partitions](../measures/communities/partition_agreement.html) | [Agreement](../measures/communities/partition_agreement.html#cat_agreement) | · reported in docs | `agreement` |
| Communities | Partition comparison and operations | [Agreement and consensus of partitions](../measures/communities/partition_agreement.html) | [Agreement weighted](../measures/communities/partition_agreement.html#cat_agreement_weighted) | · reported in docs | `agreement_weighted` |
| Communities | Partition comparison and operations | [Agreement and consensus of partitions](../measures/communities/partition_agreement.html) | [Consensus](../measures/communities/partition_agreement.html#cat_consensus) | · reported in docs | `consensus_und` |
| Communities | Partition comparison and operations | [Compare partitions](../measures/communities/compare_partitions.html) | [Partition distance](../measures/communities/compare_partitions.html#cat_distance_partition) | · reported in docs | `partition_distance` |
| Components and connectivity | Connected components | [Connected components](../measures/components-and-connectivity/connected_components.html) | [Components](../measures/components-and-connectivity/connected_components.html#components) | · reported in docs | `get_components; number_of_components` |
| Components and connectivity | Flows and flow trees | [Flow coefficient](../measures/components-and-connectivity/flow_coefficient.html) | [Flow coef](../measures/components-and-connectivity/flow_coefficient.html#cat_coef_flow) | · reported in docs | `flow_coef_bd` |
| Data transforms | Sparsification and backbones | [Statistical backbone extraction](../measures/data-transforms/statistical_backbone.html) | [Backbone](../measures/data-transforms/statistical_backbone.html#cat_backbone) | · reported in docs | `backbone_wu` |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Transitivity](../measures/descriptive-statistics/global_transitivity.html#transitivity) | ≠ checked, differs by convention | `transitivity_bd; transitivity_bu; transitivity_wd; transitivity_wu` |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | ≠ checked, differs by convention |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | ≠ checked, differs by convention | `clustering_coef_bd; clustering_coef_bu; clustering_coef_wd; clustering_coef_wu; clustering_coef_wu_sign` |
| Descriptive statistics | Density and degree distribution | [Cycle probability](../measures/descriptive-statistics/cycle_probability.html) | [Cycprob](../measures/descriptive-statistics/cycle_probability.html#cat_cycprob) | · reported in docs | `cycprob` |
| Descriptive statistics | Density and degree distribution | [Density](../measures/descriptive-statistics/density.html) | [Density](../measures/descriptive-statistics/density.html#density) | ≠ checked, differs by convention | `density_dir; density_und` |
| Descriptive statistics | Density and degree distribution | [Joint degree distribution](../measures/descriptive-statistics/joint_degree_distribution.html) | [Jdegree](../measures/descriptive-statistics/joint_degree_distribution.html#cat_jdegree) | · reported in docs | `jdegree` |
| Descriptive statistics | Density and degree distribution | [Rentian scaling](../measures/descriptive-statistics/rentian_scaling.html) | [Rentian scaling](../measures/descriptive-statistics/rentian_scaling.html#cat_rentian_scaling) | · reported in docs | `rentian_scaling` |
| Descriptive statistics | Efficiency, compactness and hierarchy | [Resource efficiency](../measures/descriptive-statistics/resource_efficiency.html) | [Resource efficiency](../measures/descriptive-statistics/resource_efficiency.html#cat_efficiency_resource) | · reported in docs | `resource_efficiency_bin` |
| Descriptive statistics | Efficiency, compactness and hierarchy | [Routing efficiency](../measures/descriptive-statistics/routing_efficiency.html) | [Rout efficiency](../measures/descriptive-statistics/routing_efficiency.html#cat_efficiency_rout) | · reported in docs | `rout_efficiency` |
| Generators and rewiring | Rewiring and randomization | [Edge swap and contract](../measures/generators-and-rewiring/swap_contract.html) | [Swap contract](../measures/generators-and-rewiring/swap_contract.html#swap_contract) | · reported in docs | `null_model_dir_sign; null_model_und_sign; randmio_dir; randmio_dir_connected; randmio_dir_signed; randmio_und; randmio_und_connected; randmio_und_signed; randomize_graph_partial_und; randomizer_bin_und` |
| Generators and rewiring | Rewiring and randomization | [Lattice-preserving rewiring](../measures/generators-and-rewiring/rewire_lattice.html) | [Lattice-preserving rewiring](../measures/generators-and-rewiring/rewire_lattice.html#rewire_lattice) | · reported in docs | `latmio_dir; latmio_dir_connected; latmio_und; latmio_und_connected` |
| Generators and rewiring | Rewiring and randomization | [Random matrix generators (density, even degree, fractal, Toeplitz)](../measures/generators-and-rewiring/bct_random_matrix.html) | [Generate fc](../measures/generators-and-rewiring/bct_random_matrix.html#cat_fc_generate) | · reported in docs | `generate_fc` |
| Generators and rewiring | Rewiring and randomization | [Random matrix generators (density, even degree, fractal, Toeplitz)](../measures/generators-and-rewiring/bct_random_matrix.html) | [Makeeven CIJ](../measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_makeeven) | · reported in docs | `makeevenCIJ` |
| Generators and rewiring | Rewiring and randomization | [Random matrix generators (density, even degree, fractal, Toeplitz)](../measures/generators-and-rewiring/bct_random_matrix.html) | [Makefractal CIJ](../measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_makefractal) | · reported in docs | `makefractalCIJ` |
| Generators and rewiring | Rewiring and randomization | [Random matrix generators (density, even degree, fractal, Toeplitz)](../measures/generators-and-rewiring/bct_random_matrix.html) | [Makerand CIJ](../measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_makerand) | · reported in docs | `makerandCIJ_dir; makerandCIJ_und` |
| Generators and rewiring | Rewiring and randomization | [Random matrix generators (density, even degree, fractal, Toeplitz)](../measures/generators-and-rewiring/bct_random_matrix.html) | [Makerand CIJdegreesfixed](../measures/generators-and-rewiring/bct_random_matrix.html#cat_ci_jdegreesfixed_makerand) | · reported in docs | `makerandCIJdegreesfixed` |
| Generators and rewiring | Rewiring and randomization | [Random matrix generators (density, even degree, fractal, Toeplitz)](../measures/generators-and-rewiring/bct_random_matrix.html) | [Maketoeplitz CIJ](../measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_maketoeplitz) | · reported in docs | `maketoeplitzCIJ` |
| Generators and rewiring | Small-world, lattice and geometric models | [Grid communities](../measures/generators-and-rewiring/grid_communities.html) | [Grid communities](../measures/generators-and-rewiring/grid_communities.html#cat_community_grid) | · reported in docs | `grid_communities` |
| Generators and rewiring | Small-world, lattice and geometric models | [Lattice graphs](../measures/generators-and-rewiring/lattice_graphs.html) | [Makeringlattice CIJ](../measures/generators-and-rewiring/lattice_graphs.html#cat_cij_makeringlattice) | · reported in docs | `makeringlatticeCIJ` |
| Graph theory and combinatorics | Similarity and link prediction | [Dice similarity](../measures/graph-theory-and-combinatorics/dice_similarity.html) | [Dice pairwise](../measures/graph-theory-and-combinatorics/dice_similarity.html#cat_dice_pairwise) | · reported in docs | `dice_pairwise_und` |
| Graph theory and combinatorics | Similarity and link prediction | [Edge neighborhood overlap](../measures/graph-theory-and-combinatorics/edge_neighborhood_overlap.html) | [Edge nei overlap](../measures/graph-theory-and-combinatorics/edge_neighborhood_overlap.html#cat_edge_nei_overlap) | · reported in docs | `edge_nei_overlap_bd; edge_nei_overlap_bu` |
| Graph theory and combinatorics | Similarity and link prediction | [Generalized topological overlap](../measures/graph-theory-and-combinatorics/topological_overlap.html) | [Gtom](../measures/graph-theory-and-combinatorics/topological_overlap.html#cat_gtom) | · reported in docs | `gtom` |
| Graph theory and combinatorics | Similarity and link prediction | [Matching index](../measures/graph-theory-and-combinatorics/matching_index.html) | [Matching ind](../measures/graph-theory-and-combinatorics/matching_index.html#cat_ind_matching) | · reported in docs | `matching_ind; matching_ind_und` |
| Graph theory and combinatorics | Unclassified procedures | [Score](../measures/graph-theory-and-combinatorics/score.html) | [Score](../measures/graph-theory-and-combinatorics/score.html#cat_score) | · reported in docs | `score_wu` |
| Mixing and assortativity | Assortativity | [Assortativity coefficient](../measures/mixing-and-assortativity/assortativity_coefficient.html) | [Assortativity degree](../measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_degree) | ≠ checked, differs by convention |  |
| Mixing and assortativity | Assortativity | [Assortativity coefficient](../measures/mixing-and-assortativity/assortativity_coefficient.html) | [Assortativity values](../measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_values) | · reported in docs | `assortativity_bin; assortativity_wei` |
| Mixing and assortativity | Assortativity | [Local assortativity](../measures/mixing-and-assortativity/local_assortativity.html) | [Local assortativity](../measures/mixing-and-assortativity/local_assortativity.html#cat_assortativity_local) | · reported in docs | `local_assortativity_wu_sign` |
| Mixing and assortativity | Rich club | [Rich club](../measures/mixing-and-assortativity/rich_club.html) | [Rich club](../measures/mixing-and-assortativity/rich_club.html#rich_club) | · reported in docs | `rich_club_bd; rich_club_bu; rich_club_wd; rich_club_wu` |
| Paths and distances | Distance summaries | [Diameter](../measures/paths-and-distances/diameter.html) | [Diameter](../measures/paths-and-distances/diameter.html#diameter) | ≠ checked, differs by convention | `charpath` |
| Paths and distances | Distance summaries | [Eccentricity](../measures/paths-and-distances/eccentricity.html) | [Eccentricity](../measures/paths-and-distances/eccentricity.html#eccentricity) | ≠ checked, differs by convention |  |
| Paths and distances | Distance summaries | [Greedy routing and navigation](../measures/paths-and-distances/greedy_routing.html) | [Navigation](../measures/paths-and-distances/greedy_routing.html#cat_navigation) | · reported in docs | `navigation_wu` |
| Paths and distances | Distance summaries | [Mean first passage time](../measures/paths-and-distances/mean_first_passage_time.html) | [Mean first passage time](../measures/paths-and-distances/mean_first_passage_time.html#cat_first_mean_passage_time) | · reported in docs | `mean_first_passage_time` |
| Paths and distances | Distance summaries | [Path transitivity](../measures/paths-and-distances/path_transitivity.html) | [Path transitivity](../measures/paths-and-distances/path_transitivity.html#cat_path_transitivity) | · reported in docs | `path_transitivity` |
| Paths and distances | Distance summaries | [Radius](../measures/paths-and-distances/radius.html) | [Radius](../measures/paths-and-distances/radius.html#radius) | ≠ checked, differs by convention |  |
| Paths and distances | Distance summaries | [Search information](../measures/paths-and-distances/search_information.html) | [Search information](../measures/paths-and-distances/search_information.html#cat_information_search) | · reported in docs | `search_information` |
| Paths and distances | Distance summaries | [Wiener index](../measures/paths-and-distances/wiener_index.html) | [Index](../measures/paths-and-distances/wiener_index.html#dm_index) | ≠ checked, differs by convention |  |
| Paths and distances | Efficiency and reachability | [Global and local efficiency](../measures/paths-and-distances/global_efficiency.html) | [Global and local efficiency](../measures/paths-and-distances/global_efficiency.html#efficiency_global) | · reported in docs | `efficiency_bin; efficiency_wei` |
| Paths and distances | Efficiency and reachability | [Local efficiency](../measures/paths-and-distances/local_efficiency.html) | [Local efficiency](../measures/paths-and-distances/local_efficiency.html#dm_local_efficiency) | ≠ checked, differs by convention |  |
| Paths and distances | Efficiency and reachability | [Reachability](../measures/paths-and-distances/reachability.html) | [Reachdist](../measures/paths-and-distances/reachability.html#cat_reachdist) | · reported in docs | `reachdist` |
| Paths and distances | Path enumeration and counting | [Bounded path and walk search](../measures/paths-and-distances/bounded_path_search.html) | [Findpaths](../measures/paths-and-distances/bounded_path_search.html#cat_findpaths) | · reported in docs | `findpaths` |
| Paths and distances | Path enumeration and counting | [Bounded path and walk search](../measures/paths-and-distances/bounded_path_search.html) | [Findwalks](../measures/paths-and-distances/bounded_path_search.html#cat_findwalks) | · reported in docs | `findwalks` |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | ✓ checked, agrees | `distance_bin; distance_wei; distance_wei_floyd` |
| Paths and distances | Shortest paths | [Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional)](../measures/paths-and-distances/shortest_paths.html) | [Retrieve shortest path](../measures/paths-and-distances/shortest_paths.html#cat_path_retrieve_shortest) | · reported in docs | `retrieve_shortest_path` |
| Roles and positions | Core-periphery | [Core-periphery (discrete)](../measures/roles-and-positions/core_periphery.html) | [Core periphery](../measures/roles-and-positions/core_periphery.html#core_periphery) | · reported in docs | `core_periphery_dir` |
| Roles and positions | Module-based roles | [Diversity coefficient](../measures/roles-and-positions/diversity_coefficient.html) | [Diversity coef](../measures/roles-and-positions/diversity_coefficient.html#cat_coef_diversity) | · reported in docs | `diversity_coef_sign` |
| Roles and positions | Module-based roles | [Gateway coefficient](../measures/roles-and-positions/gateway_coefficient.html) | [Gateway coef](../measures/roles-and-positions/gateway_coefficient.html#cat_coef_gateway) | · reported in docs | `gateway_coef_sign` |
| Roles and positions | Module-based roles | [Module degree z-score](../measures/roles-and-positions/module_degree_zscore.html) | [Module degree zscore](../measures/roles-and-positions/module_degree_zscore.html#cat_degree_module_zscore) | · reported in docs | `module_degree_zscore` |
| Roles and positions | Module-based roles | [Participation coefficient](../measures/roles-and-positions/participation_coefficient.html) | [Participation coef](../measures/roles-and-positions/participation_coefficient.html#cat_coef_participation) | · reported in docs | `participation_coef; participation_coef_sign` |
| Roles and positions | Module-based roles | [Participation coefficient](../measures/roles-and-positions/participation_coefficient.html) | [Participation coef sparse](../measures/roles-and-positions/participation_coefficient.html#cat_coef_participation_sparse) | · reported in docs | `participation_coef_sparse` |
| Statistical fitting | Model fitting | [Generative network models (fit and evaluate)](../measures/statistical-fitting/generative_model.html) | [Evaluate generative model](../measures/statistical-fitting/generative_model.html#cat_evaluate_generative_model) | · reported in docs | `evaluate_generative_model` |
| Statistical fitting | Model fitting | [Generative network models (fit and evaluate)](../measures/statistical-fitting/generative_model.html) | [Generative model](../measures/statistical-fitting/generative_model.html#cat_generative_model) | · reported in docs | `generative_model` |
| Statistical fitting | Model fitting | [Network-based statistic](../measures/statistical-fitting/bct_nbs.html) | [Nbs bct](../measures/statistical-fitting/bct_nbs.html#cat_bct_nbs) | · reported in docs | `nbs_bct` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F055](../findings.html#f055) | convention | Betweenness counts ordered pairs on undirected networks |
| [F056](../findings.html#f056) | convention | clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients |
| [F057](../findings.html#f057) | convention | charpath takes the longest finite distance; NaN for a node reaching nobody |
| [F058](../findings.html#f058) | convention | Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target |
| [F059](../findings.html#f059) | convention | Matrix-input calls carry no loops or parallel edges |
{% endraw %}
