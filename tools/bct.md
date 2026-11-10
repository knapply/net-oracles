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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention | `betweenness_bin; betweenness_wei` |
| Centrality | [Communicability](../measures/cx_communicability.html) | · reported in docs | `subgraph_centrality` |
| Centrality | [Diffusion efficiency](../measures/cat_diffusion_efficiency.html) | · reported in docs | `diffusion_efficiency` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | · reported in docs | `edge_betweenness_bin; edge_betweenness_wei` |
| Centrality | [Eigenvector](../measures/eigenvector.html) | · reported in docs | `eigenvector_centrality_und` |
| Centrality | [Nxp pagerank](../measures/nxp_pagerank.html) | · reported in docs | `pagerank_centrality` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ≠ checked, differs by convention | `kcore_bd; kcore_bu; kcoreness_centrality_bd; kcoreness_centrality_bu` |
| Cohesion and subgroups | [Motif census](../measures/motif_census.html) | · reported in docs | `find_motif34; motif3funct_bin; motif3funct_wei; motif3struct_bin; motif3struct_wei; motif4funct_bin; motif4funct_wei; motif4struct_bin; motif4struct_wei` |
| Communities | [Clique communities](../measures/cat_clique_community.html) | · reported in docs | `clique_communities` |
| Communities | [Link communities](../measures/cat_community_link.html) | · reported in docs | `link_communities` |
| Communities | [Louvain modularity](../measures/louvain_modularity.html) | · reported in docs | `community_louvain; modularity_finetune_dir; modularity_finetune_und; modularity_finetune_und_sign; modularity_louvain_dir; modularity_louvain_und; modularity_louvain_und_sign; modularity_probtune_und_sign` |
| Communities | [Modularity](../measures/modularity.html) | · reported in docs | `modularity_dir; modularity_und; modularity_und_sign` |
| Communities | [Partition distance](../measures/cat_distance_partition.html) | · reported in docs | `partition_distance` |
| Components and connectivity | [Flow coef](../measures/cat_coef_flow.html) | · reported in docs | `flow_coef_bd` |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ≠ checked, differs by convention | `clustering_coef_bd; clustering_coef_bu; clustering_coef_wd; clustering_coef_wu; clustering_coef_wu_sign` |
| Descriptive statistics | [Components](../measures/components.html) | · reported in docs | `get_components; number_of_components` |
| Descriptive statistics | [Degree](../measures/degree.html) | ≠ checked, differs by convention | `degrees_dir; degrees_und; strengths_dir; strengths_und; strengths_und_sign` |
| Descriptive statistics | [Density](../measures/density.html) | ≠ checked, differs by convention | `density_dir; density_und` |
| Descriptive statistics | [Resource efficiency](../measures/cat_efficiency_resource.html) | · reported in docs | `resource_efficiency_bin` |
| Descriptive statistics | [Rout efficiency](../measures/cat_efficiency_rout.html) | · reported in docs | `rout_efficiency` |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ≠ checked, differs by convention | `transitivity_bd; transitivity_bu; transitivity_wd; transitivity_wu` |
| Generators and rewiring | [Grid communities](../measures/cat_community_grid.html) | · reported in docs | `grid_communities` |
| Generators and rewiring | [Lattice-preserving rewiring](../measures/rewire_lattice.html) | · reported in docs | `latmio_dir; latmio_dir_connected; latmio_und; latmio_und_connected` |
| Generators and rewiring | [Makeringlattice CIJ](../measures/cat_cij_makeringlattice.html) | · reported in docs | `makeringlatticeCIJ` |
| Generators and rewiring | [Rich club](../measures/rich_club.html) | · reported in docs | `rich_club_bd; rich_club_bu; rich_club_wd; rich_club_wu` |
| Generators and rewiring | [Search information](../measures/cat_information_search.html) | · reported in docs | `search_information` |
| Generators and rewiring | [Swap contract](../measures/swap_contract.html) | · reported in docs | `null_model_dir_sign; null_model_und_sign; randmio_dir; randmio_dir_connected; randmio_dir_signed; randmio_und; randmio_und_connected; randmio_und_signed; randomize_graph_partial_und; randomizer_bin_und` |
| Graph theory and combinatorics | [Agreement](../measures/cat_agreement.html) | · reported in docs | `agreement` |
| Graph theory and combinatorics | [Agreement weighted](../measures/cat_agreement_weighted.html) | · reported in docs | `agreement_weighted` |
| Graph theory and combinatorics | [Backbone](../measures/cat_backbone.html) | · reported in docs | `backbone_wu` |
| Graph theory and combinatorics | [Consensus](../measures/cat_consensus.html) | · reported in docs | `consensus_und` |
| Graph theory and combinatorics | [Cycprob](../measures/cat_cycprob.html) | · reported in docs | `cycprob` |
| Graph theory and combinatorics | [Dice pairwise](../measures/cat_dice_pairwise.html) | · reported in docs | `dice_pairwise_und` |
| Graph theory and combinatorics | [Diversity coef](../measures/cat_coef_diversity.html) | · reported in docs | `diversity_coef_sign` |
| Graph theory and combinatorics | [Edge nei overlap](../measures/cat_edge_nei_overlap.html) | · reported in docs | `edge_nei_overlap_bd; edge_nei_overlap_bu` |
| Graph theory and combinatorics | [Gateway coef](../measures/cat_coef_gateway.html) | · reported in docs | `gateway_coef_sign` |
| Graph theory and combinatorics | [Generate fc](../measures/cat_fc_generate.html) | · reported in docs | `generate_fc` |
| Graph theory and combinatorics | [Gtom](../measures/cat_gtom.html) | · reported in docs | `gtom` |
| Graph theory and combinatorics | [Jdegree](../measures/cat_jdegree.html) | · reported in docs | `jdegree` |
| Graph theory and combinatorics | [Makeeven CIJ](../measures/cat_cij_makeeven.html) | · reported in docs | `makeevenCIJ` |
| Graph theory and combinatorics | [Makefractal CIJ](../measures/cat_cij_makefractal.html) | · reported in docs | `makefractalCIJ` |
| Graph theory and combinatorics | [Makerand CIJ](../measures/cat_cij_makerand.html) | · reported in docs | `makerandCIJ_dir; makerandCIJ_und` |
| Graph theory and combinatorics | [Makerand CIJdegreesfixed](../measures/cat_ci_jdegreesfixed_makerand.html) | · reported in docs | `makerandCIJdegreesfixed` |
| Graph theory and combinatorics | [Maketoeplitz CIJ](../measures/cat_cij_maketoeplitz.html) | · reported in docs | `maketoeplitzCIJ` |
| Graph theory and combinatorics | [Matching ind](../measures/cat_ind_matching.html) | · reported in docs | `matching_ind; matching_ind_und` |
| Graph theory and combinatorics | [Module degree zscore](../measures/cat_degree_module_zscore.html) | · reported in docs | `module_degree_zscore` |
| Graph theory and combinatorics | [Navigation](../measures/cat_navigation.html) | · reported in docs | `navigation_wu` |
| Graph theory and combinatorics | [Nbs bct](../measures/cat_bct_nbs.html) | · reported in docs | `nbs_bct` |
| Graph theory and combinatorics | [Participation coef](../measures/cat_coef_participation.html) | · reported in docs | `participation_coef; participation_coef_sign` |
| Graph theory and combinatorics | [Participation coef sparse](../measures/cat_coef_participation_sparse.html) | · reported in docs | `participation_coef_sparse` |
| Graph theory and combinatorics | [Rentian scaling](../measures/cat_rentian_scaling.html) | · reported in docs | `rentian_scaling` |
| Graph theory and combinatorics | [Score](../measures/cat_score.html) | · reported in docs | `score_wu` |
| Mixing and assortativity | [Assortativity degree](../measures/assortativity_degree.html) | ≠ checked, differs by convention |  |
| Mixing and assortativity | [Assortativity values](../measures/assortativity_values.html) | · reported in docs | `assortativity_bin; assortativity_wei` |
| Mixing and assortativity | [Local assortativity](../measures/cat_assortativity_local.html) | · reported in docs | `local_assortativity_wu_sign` |
| Paths and distances | [Diameter](../measures/diameter.html) | ≠ checked, differs by convention | `charpath` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees | `distance_bin; distance_wei; distance_wei_floyd` |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Findpaths](../measures/cat_findpaths.html) | · reported in docs | `findpaths` |
| Paths and distances | [Findwalks](../measures/cat_findwalks.html) | · reported in docs | `findwalks` |
| Paths and distances | [Global and local efficiency](../measures/efficiency_global.html) | · reported in docs | `efficiency_bin; efficiency_wei` |
| Paths and distances | [Index](../measures/dm_index.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Local efficiency](../measures/dm_local_efficiency.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Path transitivity](../measures/cat_path_transitivity.html) | · reported in docs | `path_transitivity` |
| Paths and distances | [Radius](../measures/radius.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Reachdist](../measures/cat_reachdist.html) | · reported in docs | `reachdist` |
| Paths and distances | [Retrieve shortest path](../measures/cat_path_retrieve_shortest.html) | · reported in docs | `retrieve_shortest_path` |
| Roles and positions | [Core periphery](../measures/core_periphery.html) | · reported in docs | `core_periphery_dir` |
| Statistical fitting | [Evaluate generative model](../measures/cat_evaluate_generative_model.html) | · reported in docs | `evaluate_generative_model` |
| Statistical fitting | [Generative model](../measures/cat_generative_model.html) | · reported in docs | `generative_model` |
| Temporal and events | [Mean first passage time](../measures/cat_first_mean_passage_time.html) | · reported in docs | `mean_first_passage_time` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F055](../findings.html#f055) | convention | Betweenness counts ordered pairs on undirected networks |
| [F056](../findings.html#f056) | convention | clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients |
| [F057](../findings.html#f057) | convention | charpath takes the longest finite distance; NaN for a node reaching nobody |
| [F058](../findings.html#f058) | convention | Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target |
| [F059](../findings.html#f059) | convention | Matrix-input calls carry no loops or parallel edges |
{% endraw %}
