---
title: "igraph (R)"
layout: default
parent: Tools
---

{% raw %}
# igraph (R)

| Field | Value |
|---|---|
| Identifier | `igraph` |
| Language | R over C |
| Version tested | 2.3.4 |
| License | GPL-2.0-or-later |
| Homepage | <https://r.igraph.org> |
| Role | checked |
| Citation | [csardi2006igraph](../references.html#csardi2006igraph) |

## How it was run

Called from R through exported functions on igraph objects.

Capabilities listed by introspection of R package igraph: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 35 |
| checked, differs by convention (≠) | 7 |
| checked, no value on some inputs (∅) | 27 |
| reported in docs (·) | 143 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention | `betweenness` |
| Centrality | [Bonacich](../measures/bonacich.html) | ✓ checked, agrees | `bonpow; power_centrality` |
| Centrality | [Closeness](../measures/closeness.html) | ✓ checked, agrees | `closeness` |
| Centrality | [Communicability](../measures/cx_communicability.html) | · reported in docs | `subgraph_centrality` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | ✓ checked, agrees | `edge_betweenness` |
| Centrality | [Eigenvector](../measures/eigenvector.html) | ∅ checked, no value on some inputs | `eigen_centrality; evcent` |
| Centrality | [Harmonic](../measures/harmonic.html) | ✓ checked, agrees | `harmonic_centrality` |
| Centrality | [Hits](../measures/hits.html) | ∅ checked, no value on some inputs | `authority_score; hits_scores; hub_score` |
| Centrality | [Katz](../measures/katz.html) | ∅ checked, no value on some inputs | `alpha_centrality` |
| Centrality | [Pagerank](../measures/pagerank.html) | ∅ checked, no value on some inputs | `page_rank` |
| Centrality | [Reach](../measures/reach.html) | ✓ checked, agrees | `count_reachable` |
| Centrality | [Strength](../measures/strength.html) | ∅ checked, no value on some inputs | `strength` |
| Centrality | [Theoretical maximum of centralization](../measures/centralization_tmax.html) | · reported in docs | `centr_betw_tmax; centr_clo_tmax; centr_degree_tmax; centr_eigen_tmax` |
| Cohesion and subgroups | [Clique number](../measures/clique_number.html) | ✓ checked, agrees | `clique_num; weighted_clique_num` |
| Cohesion and subgroups | [Cocitation and bibliographic coupling](../measures/cocitation.html) | · reported in docs | `bibcoupling; cocitation` |
| Cohesion and subgroups | [Cohesive blocks](../measures/cat_blocks_cohesive.html) | · reported in docs | `cohesive_blocks` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ✓ checked, agrees | `coreness` |
| Cohesion and subgroups | [Count max cliques](../measures/cat_clique_count_max.html) | · reported in docs | `count_max_cliques` |
| Cohesion and subgroups | [Graphlet basis and projection](../measures/graphlets.html) | · reported in docs | `graphlet_basis; graphlet_proj` |
| Cohesion and subgroups | [Is clique](../measures/cat_clique_is.html) | · reported in docs | `is_clique` |
| Cohesion and subgroups | [Lambda connectivity](../measures/lambda_connectivity.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Largest weighted cliques](../measures/cat_clique_largest_weighted.html) | · reported in docs | `largest_weighted_cliques` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | ✓ checked, agrees | `clique_size_counts; cliques; largest_cliques; max_cliques` |
| Cohesion and subgroups | [Motif census](../measures/motif_census.html) | · reported in docs | `count_motifs; graphlets; motifs; sample_motifs` |
| Cohesion and subgroups | [Weighted cliques](../measures/cat_clique_weighted.html) | · reported in docs | `weighted_cliques` |
| Communities | [Compare partitions](../measures/compare_partitions.html) | ≠ checked, differs by convention | `compare; split_join_distance` |
| Communities | [Fast greedy](../measures/fast_greedy.html) | ≠ checked, differs by convention | `cluster_fast_greedy` |
| Communities | [Fluid communities](../measures/fluid_communities.html) | ✓ checked, agrees | `cluster_fluid_communities` |
| Communities | [Girvan newman](../measures/girvan_newman.html) | ✓ checked, agrees | `cluster_edge_betweenness` |
| Communities | [Girvan newman cut](../measures/girvan_newman_cut.html) | ✓ checked, agrees |  |
| Communities | [Infomap](../measures/infomap.html) | ∅ checked, no value on some inputs | `cluster_infomap` |
| Communities | [Label propagation](../measures/label_propagation.html) | ∅ checked, no value on some inputs | `cluster_label_prop` |
| Communities | [Leading eigen](../measures/leading_eigen.html) | ✓ checked, agrees | `cluster_leading_eigen` |
| Communities | [Leiden](../measures/leiden.html) | ∅ checked, no value on some inputs | `cluster_leiden` |
| Communities | [Louvain modularity](../measures/louvain_modularity.html) | · reported in docs | `cluster_louvain` |
| Communities | [Louvain quality](../measures/louvain_quality.html) | ≠ checked, differs by convention |  |
| Communities | [Modularity](../measures/modularity.html) | ✓ checked, agrees | `modularity` |
| Communities | [Optimal modularity](../measures/optimal_modularity.html) | ✓ checked, agrees | `cluster_optimal` |
| Communities | [Spinglass](../measures/spinglass.html) | ✓ checked, agrees | `cluster_spinglass` |
| Communities | [Voronoi](../measures/voronoi.html) | ≠ checked, differs by convention |  |
| Communities | [Walktrap](../measures/walktrap.html) | ≠ checked, differs by convention | `cluster_walktrap` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | ✓ checked, agrees | `biconnected_components` |
| Components and connectivity | [Bridges](../measures/bridges.html) | ∅ checked, no value on some inputs | `bridges` |
| Components and connectivity | [Cohesive blocking (Moody-White)](../measures/cohesive_blocking.html) | · reported in docs |  |
| Components and connectivity | [Connectivity](../measures/connectivity.html) | · reported in docs | `adhesion; cohesion; edge_connectivity; vertex_connectivity` |
| Components and connectivity | [Count components](../measures/cat_component_count.html) | · reported in docs | `count_components` |
| Components and connectivity | [Cut points](../measures/cut_points.html) | ∅ checked, no value on some inputs | `articulation_points` |
| Components and connectivity | [Disjoint paths](../measures/disjoint_paths.html) | · reported in docs | `edge_disjoint_paths; vertex_disjoint_paths` |
| Components and connectivity | [Fragmentation](../measures/fragmentation.html) | ∅ checked, no value on some inputs |  |
| Components and connectivity | [Max flow](../measures/max_flow.html) | · reported in docs | `max_flow` |
| Components and connectivity | [Min cut](../measures/min_cut.html) | · reported in docs | `min_cut` |
| Components and connectivity | [Node cut](../measures/node_cut.html) | · reported in docs | `is_min_separator; is_separator; min_separators; min_st_separators; stCuts; st_cuts; st_min_cuts` |
| Components and connectivity | [St Mincuts](../measures/cat_mincuts_st.html) | · reported in docs | `stMincuts` |
| Data transforms | [Graph complement](../measures/op_complement.html) | · reported in docs | `complementer` |
| Data transforms | [Line graph](../measures/line_graph.html) | · reported in docs | `line_graph; make_line_graph` |
| Data transforms | [Op compose](../measures/op_compose.html) | · reported in docs | `compose` |
| Data transforms | [Op difference](../measures/op_difference.html) | · reported in docs | `difference` |
| Data transforms | [Op intersection](../measures/op_intersection.html) | · reported in docs | `intersection` |
| Data transforms | [Op union](../measures/op_union.html) | · reported in docs | `disjoint_union; union` |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ∅ checked, no value on some inputs |  |
| Descriptive statistics | [Centralization / betweenness](../measures/centralization-betweenness.html) | ✓ checked, agrees | `centr_betw` |
| Descriptive statistics | [Centralization / closeness](../measures/centralization-closeness.html) | ✓ checked, agrees | `centr_clo` |
| Descriptive statistics | [Centralization / degree](../measures/centralization-degree.html) | ∅ checked, no value on some inputs | `centr_degree` |
| Descriptive statistics | [Centralization eigenvector](../measures/centralization_eigenvector.html) | ≠ checked, differs by convention | `centr_eigen` |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ∅ checked, no value on some inputs |  |
| Descriptive statistics | [Compactness](../measures/compactness.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Components](../measures/components.html) | ∅ checked, no value on some inputs | `clusters; component_distribution; components; decompose; is_biconnected; is_connected; largest_component; subcomponent` |
| Descriptive statistics | [Degree](../measures/degree.html) | ∅ checked, no value on some inputs | `degree; degree_distribution` |
| Descriptive statistics | [Density](../measures/density.html) | ∅ checked, no value on some inputs | `edge_density` |
| Descriptive statistics | [Dyad census (mutual, asymmetric, null)](../measures/dyad_census.html) | · reported in docs | `dyad_census` |
| Descriptive statistics | [Ego size](../measures/ego_size.html) | ✓ checked, agrees | `ego_size` |
| Descriptive statistics | [Knn](../measures/cat_knn.html) | · reported in docs | `knn` |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | ∅ checked, no value on some inputs | `reciprocity` |
| Descriptive statistics | [Small world observed](../measures/small_world_observed.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ∅ checked, no value on some inputs | `transitivity` |
| Descriptive statistics | [Triad census](../measures/triad_census.html) | ∅ checked, no value on some inputs | `triad_census` |
| Descriptive statistics | [Triangles](../measures/nxo_triangles.html) | · reported in docs | `count_triangles; triangles` |
| Generators and rewiring | [Bipartite degree-sequence realization](../measures/gen_realize_bipartite.html) | · reported in docs | `realize_bipartite_degseq` |
| Generators and rewiring | [Chordal ring generator](../measures/gen_chordal_ring.html) | · reported in docs | `chordal_ring; make_chordal_ring` |
| Generators and rewiring | [Chung-Lu (expected degree) generator](../measures/gen_chung_lu.html) | · reported in docs | `chung_lu; sample_chung_lu` |
| Generators and rewiring | [Circulant graph generator](../measures/gen_circulant.html) | · reported in docs | `circulant; make_circulant` |
| Generators and rewiring | [Citation-type growth generators](../measures/gen_citation.html) | · reported in docs | `cit_cit_types; cit_types; full_citation_graph; last_cit; make_full_citation_graph; sample_cit_cit_types; sample_cit_types; sample_last_cit` |
| Generators and rewiring | [Complete multipartite graph generator](../measures/gen_complete_multipartite.html) | · reported in docs | `make_full_multipartite` |
| Generators and rewiring | [Configuration model](../measures/gen_configuration.html) | · reported in docs | `sample_degseq` |
| Generators and rewiring | [Correlated and bipartite random graph generators](../measures/gen_correlated_bipartite.html) | · reported in docs | `sample_bipartite_gnm; sample_bipartite_gnp; sample_correlated_gnp; sample_correlated_gnp_pair` |
| Generators and rewiring | [De Bruijn graph generator](../measures/gen_de_bruijn.html) | · reported in docs | `de_bruijn_graph; make_de_bruijn_graph` |
| Generators and rewiring | [Deterministic generators](../measures/deterministic_generators.html) | · reported in docs | `empty_graph; make_empty_graph; make_full_bipartite_graph; make_full_graph; make_ring; make_star; make_tree; make_wheel; ring; star; tree; wheel` |
| Generators and rewiring | [Deterministic realisation of a degree sequence](../measures/gen_degree_realization.html) | · reported in docs | `realize_degseq` |
| Generators and rewiring | [Forest fire generator](../measures/gen_forest_fire.html) | · reported in docs | `sample_forestfire` |
| Generators and rewiring | [Full bipartite graph](../measures/cat_bipartite_full.html) | · reported in docs | `full_bipartite_graph` |
| Generators and rewiring | [Full graph](../measures/cat_full.html) | · reported in docs | `full_graph` |
| Generators and rewiring | [Full multipartite](../measures/cat_full_multipartite.html) | · reported in docs | `full_multipartite` |
| Generators and rewiring | [G(n, m) random graph](../measures/gen_gnm.html) | · reported in docs | `sample_gnm` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `sample_gnp` |
| Generators and rewiring | [Gnm](../measures/cat_gnm.html) | · reported in docs | `gnm` |
| Generators and rewiring | [Gnp](../measures/cat_gnp.html) | · reported in docs | `gnp` |
| Generators and rewiring | [Growing random graph generator](../measures/gen_growing.html) | · reported in docs | `growing; sample_growing` |
| Generators and rewiring | [Is complete](../measures/cat_complete_is.html) | · reported in docs | `is_complete` |
| Generators and rewiring | [Kautz graph generator](../measures/gen_kautz.html) | · reported in docs | `kautz_graph; make_kautz_graph` |
| Generators and rewiring | [Latent-space generators (dot product, sphere, islands)](../measures/gen_latent_space.html) | · reported in docs | `dot_product; sample_dirichlet; sample_dot_product; sample_islands; sample_sphere_surface; sample_sphere_volume` |
| Generators and rewiring | [Lattice generator](../measures/gen_lattice.html) | · reported in docs | `lattice; make_lattice` |
| Generators and rewiring | [Preference (types) random graph generator](../measures/gen_preference.html) | · reported in docs | `asym_pref; pref; sample_asym_pref; sample_pref` |
| Generators and rewiring | [Preferential attachment generator](../measures/gen_preferential.html) | · reported in docs | `sample_pa; sample_pa_age` |
| Generators and rewiring | [Random bipartite graph generator](../measures/gen_random_bipartite.html) | · reported in docs | `bipartite_gnm; bipartite_gnp; sample_bipartite` |
| Generators and rewiring | [Random geometric graph generator](../measures/gen_geometric.html) | · reported in docs | `grg; sample_grg` |
| Generators and rewiring | [Random regular graph generator](../measures/gen_regular.html) | · reported in docs | `sample_k_regular` |
| Generators and rewiring | [Random tree generator](../measures/gen_random_tree.html) | · reported in docs | `sample_tree` |
| Generators and rewiring | [Sample seq](../measures/cat_sample_seq.html) | · reported in docs | `sample_seq` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `sample_smallworld; smallworld` |
| Generators and rewiring | [Static fitness and static power-law generators](../measures/gen_static_fitness.html) | · reported in docs | `sample_fitness; sample_fitness_pl` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `hierarchical_sbm; sample_hierarchical_sbm; sample_sbm; sbm` |
| Generators and rewiring | [Swap contract](../measures/swap_contract.html) | · reported in docs | `rewire` |
| Generators and rewiring | [Trait-based (Callaway) growth generator](../measures/gen_traits.html) | · reported in docs | `sample_traits; sample_traits_callaway; traits; traits_callaway` |
| Generators and rewiring | [Turan graph generator](../measures/gen_turan.html) | · reported in docs | `make_turan; turan` |
| Graph theory and combinatorics | [Automorphism group, count and canonical form](../measures/automorphisms.html) | · reported in docs | `automorphism_group; automorphisms; canonical_permutation; count_automorphisms` |
| Graph theory and combinatorics | [Check matching](../measures/check_matching.html) | · reported in docs | `is_matching; is_max_matching` |
| Graph theory and combinatorics | [Contracted nodes](../measures/nxs_contracted_nodes.html) | · reported in docs | `contract` |
| Graph theory and combinatorics | [Degseq](../measures/cat_degseq.html) | · reported in docs | `degseq` |
| Graph theory and combinatorics | [Diversity](../measures/cat_diversity.html) | · reported in docs | `diversity` |
| Graph theory and combinatorics | [Euler](../measures/nxs_euler.html) | · reported in docs | `eulerian_cycle; eulerian_path; has_eulerian_cycle; has_eulerian_path` |
| Graph theory and combinatorics | [Farthest vertices](../measures/cat_farthest.html) | · reported in docs | `farthest_vertices` |
| Graph theory and combinatorics | [Feedback arc and vertex sets](../measures/feedback_sets.html) | · reported in docs | `feedback_arc_set; feedback_vertex_set` |
| Graph theory and combinatorics | [Find cycle](../measures/find_cycle.html) | · reported in docs | `find_cycle` |
| Graph theory and combinatorics | [Forest flags](../measures/nxs_forest_flags.html) | · reported in docs | `is_forest; is_tree` |
| Graph theory and combinatorics | [From prufer](../measures/nxs_from_prufer.html) | · reported in docs | `make_from_prufer` |
| Graph theory and combinatorics | [Girth](../measures/girth.html) | · reported in docs | `girth` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | · reported in docs | `greedy_vertex_coloring` |
| Graph theory and combinatorics | [Is degseq](../measures/cat_degseq_is.html) | · reported in docs | `is_degseq` |
| Graph theory and combinatorics | [Is graphical](../measures/cat_graphical_is.html) | · reported in docs | `is_graphical` |
| Graph theory and combinatorics | [Is hierarchical](../measures/cat_hierarchical_is.html) | · reported in docs | `is_hierarchical` |
| Graph theory and combinatorics | [Is ivs](../measures/cat_is_ivs.html) | · reported in docs | `is_ivs` |
| Graph theory and combinatorics | [Link prediction](../measures/link_prediction.html) | · reported in docs | `similarity` |
| Graph theory and combinatorics | [Local scan](../measures/cat_local_scan.html) | · reported in docs | `local_scan` |
| Graph theory and combinatorics | [Loop and multi-edge detection](../measures/multi_loop_detection.html) | · reported in docs | `any_loop; any_multiple; count_loops; count_multiple; is_simple; which_loop; which_multiple; which_mutual` |
| Graph theory and combinatorics | [Match vertices](../measures/cat_match.html) | · reported in docs | `match_vertices` |
| Graph theory and combinatorics | [Maxcohesion](../measures/cat_maxcohesion.html) | · reported in docs | `maxcohesion` |
| Graph theory and combinatorics | [Mis](../measures/mis.html) | · reported in docs | `independence_number; ivs; largest_ivs; max_ivs; maximal_ivs` |
| Graph theory and combinatorics | [Pa](../measures/cat_pa.html) | · reported in docs | `pa` |
| Graph theory and combinatorics | [Pa age](../measures/cat_age_pa.html) | · reported in docs | `pa_age` |
| Graph theory and combinatorics | [Scan stat](../measures/cat_scan_stat.html) | · reported in docs | `scan_stat` |
| Graph theory and combinatorics | [Simple cycles](../measures/simple_cycles.html) | · reported in docs | `simple_cycles` |
| Graph theory and combinatorics | [Sir](../measures/cat_sir.html) | · reported in docs | `sir` |
| Graph theory and combinatorics | [St chordal](../measures/st_chordal.html) | · reported in docs | `is_chordal` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | · reported in docs | `count_isomorphisms; count_subgraph_isomorphisms; is_isomorphic_to; is_subgraph_isomorphic_to; isomorphism_class; isomorphisms; subgraph_isomorphisms` |
| Graph theory and combinatorics | [Voronoi cells](../measures/cat_cells_voronoi.html) | · reported in docs | `voronoi_cells` |
| Input and output | [Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list](../measures/io_text_formats.html) | · reported in docs |  |
| Input and output | [GML read and write](../measures/io_gml.html) | · reported in docs |  |
| Input and output | [GraphML read and write](../measures/io_graphml.html) | · reported in docs |  |
| Input and output | [Pajek .net read and write](../measures/io_pajek.html) | · reported in docs |  |
| Layout | [Circle, tree and two-mode (barycenter) layouts](../measures/layout_simple.html) | · reported in docs | `layout_as_bipartite; layout_as_star; layout_as_tree; layout_in_circle` |
| Layout | [Davidson-Harel layout](../measures/layout_dh.html) | · reported in docs | `layout_with_dh` |
| Layout | [DrL (OpenOrd) layout](../measures/layout_drl.html) | · reported in docs | `layout_with_drl` |
| Layout | [Fruchterman-Reingold layout](../measures/layout_fruchterman_reingold.html) | · reported in docs | `layout_nicely; layout_with_fr` |
| Layout | [GEM layout](../measures/layout_gem.html) | · reported in docs | `layout_with_gem` |
| Layout | [Graphopt layout](../measures/layout_graphopt.html) | · reported in docs | `layout_with_graphopt` |
| Layout | [Grid layout](../measures/layout_grid.html) | · reported in docs | `layout_on_grid` |
| Layout | [Kamada-Kawai layout](../measures/layout_kamada_kawai.html) | · reported in docs | `layout_with_kk` |
| Layout | [Large graph layout (LGL)](../measures/layout_lgl.html) | · reported in docs | `layout_with_lgl` |
| Layout | [Multidimensional scaling layout](../measures/layout_mds.html) | · reported in docs | `layout_with_mds` |
| Layout | [Random layout](../measures/layout_random.html) | · reported in docs | `layout_randomly` |
| Layout | [Sphere layout](../measures/layout_sphere.html) | · reported in docs | `layout_on_sphere` |
| Layout | [Sugiyama layered layout](../measures/layout_sugiyama.html) | · reported in docs | `layout_with_sugiyama` |
| Matrices and spectra | [Adjacency](../measures/gm_adjacency.html) | · reported in docs | `as_adjacency_matrix` |
| Matrices and spectra | [Gm laplacian](../measures/gm_laplacian.html) | · reported in docs | `laplacian_matrix` |
| Matrices and spectra | [Gm modularity](../measures/gm_modularity.html) | · reported in docs | `modularity_matrix` |
| Matrices and spectra | [Graph spectrum (eigenvalues of a graph matrix)](../measures/graph_spectrum.html) | · reported in docs | `embed_adjacency_matrix; embed_laplacian_matrix; spectrum` |
| Matrices and spectra | [Incidence](../measures/gm_incidence.html) | · reported in docs | `as_biadjacency_matrix; as_incidence_matrix` |
| Matrices and spectra | [Stochastic matrix](../measures/cat_matrix_stochastic.html) | · reported in docs | `stochastic_matrix` |
| Mixing and assortativity | [Assortativity degree](../measures/assortativity_degree.html) | ∅ checked, no value on some inputs |  |
| Mixing and assortativity | [Assortativity nominal](../measures/assortativity_nominal.html) | ∅ checked, no value on some inputs |  |
| Mixing and assortativity | [Assortativity values](../measures/assortativity_values.html) | ∅ checked, no value on some inputs | `assortativity; assortativity_degree; assortativity_nominal` |
| Paths and distances | [Center](../measures/dm_center.html) | · reported in docs | `graph_center` |
| Paths and distances | [Diameter](../measures/diameter.html) | ✓ checked, agrees | `diameter; get_diameter` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees | `distances` |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ✓ checked, agrees | `eccentricity` |
| Paths and distances | [Global and local efficiency](../measures/efficiency_global.html) | · reported in docs | `average_local_efficiency; global_efficiency; local_efficiency` |
| Paths and distances | [Mean distance](../measures/mean_distance.html) | ✓ checked, agrees | `mean_distance` |
| Paths and distances | [Paths all pairs](../measures/paths_all_pairs.html) | · reported in docs | `distance_table` |
| Paths and distances | [Paths all shortest](../measures/paths_all_shortest.html) | · reported in docs | `all_shortest_paths` |
| Paths and distances | [Paths k shortest](../measures/paths_k_shortest.html) | · reported in docs | `k_shortest_paths` |
| Paths and distances | [Paths simple](../measures/paths_simple.html) | · reported in docs | `all_simple_paths` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `shortest_paths` |
| Paths and distances | [Radius](../measures/radius.html) | ✓ checked, agrees | `radius` |
| Paths and distances | [Reachability](../measures/reachability.html) | ✓ checked, agrees |  |
| Roles and positions | [Constraint](../measures/constraint.html) | ✓ checked, agrees | `constraint` |
| Roles and positions | [Hierarchy](../measures/hierarchy.html) | · reported in docs | `hierarchy` |
| Statistical fitting | [Hierarchical random graph (fit, sample, predict)](../measures/hrg.html) | · reported in docs | `fit_hrg; hrg; hrg_tree; predict_edges; sample_hrg` |
| Statistical fitting | [Power-law fit of a degree distribution](../measures/power_law_fit.html) | · reported in docs | `fit_power_law` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `bfs` |
| Traversal, trees and DAGs | [Closure](../measures/closure.html) | · reported in docs | `transitive_closure` |
| Traversal, trees and DAGs | [Consensus tree](../measures/cat_consensus_tree.html) | · reported in docs | `consensus_tree` |
| Traversal, trees and DAGs | [Edge dfs](../measures/trav_edge_dfs.html) | · reported in docs | `dfs` |
| Traversal, trees and DAGs | [Idom](../measures/idom.html) | · reported in docs | `dominator_tree` |
| Traversal, trees and DAGs | [Is dag](../measures/is_dag.html) | · reported in docs | `is_acyclic; is_dag` |
| Traversal, trees and DAGs | [Random spanning tree](../measures/random_spanning_tree.html) | · reported in docs | `sample_spanning_tree` |
| Traversal, trees and DAGs | [Random walks](../measures/random_walk.html) | · reported in docs | `random_edge_walk; random_walk` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | · reported in docs | `mst` |
| Traversal, trees and DAGs | [Topological sort](../measures/topological_sort.html) | · reported in docs | `topo_sort` |
| Traversal, trees and DAGs | [Unfold tree](../measures/cat_tree_unfold.html) | · reported in docs | `unfold_tree` |
| Two-mode and bipartite | [Bipartite](../measures/cat_bipartite.html) | · reported in docs | `bipartite` |
| Two-mode and bipartite | [Bipartite color](../measures/bipartite_color.html) | · reported in docs | `bipartite_mapping; is_bipartite` |
| Two-mode and bipartite | [Ego members](../measures/ego_members.html) | ✓ checked, agrees | `ego; make_ego_graph` |
| Two-mode and bipartite | [Ego\_summary / betweenness](../measures/ego_summary-betweenness.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Ego\_summary / components](../measures/ego_summary-components.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Ego\_summary / density](../measures/ego_summary-density.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Ego\_summary / ties](../measures/ego_summary-ties.html) | ✓ checked, agrees |  |
| Two-mode and bipartite | [Hopcroft karp](../measures/hopcroft_karp.html) | · reported in docs | `max_bipartite_match` |
| Two-mode and bipartite | [Project](../measures/project.html) | ∅ checked, no value on some inputs | `bipartite_projection; bipartite_projection_size` |
| Two-mode and bipartite | [Twomode / betweenness](../measures/twomode-betweenness.html) | ∅ checked, no value on some inputs |  |
| Two-mode and bipartite | [Twomode / closeness](../measures/twomode-closeness.html) | ∅ checked, no value on some inputs |  |
| Two-mode and bipartite | [Twomode / degree](../measures/twomode-degree.html) | ∅ checked, no value on some inputs |  |
| Two-mode and bipartite | [Twomode / eigenvector](../measures/twomode-eigenvector.html) | ✓ checked, agrees |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F010](../findings.html#f010) | defect | Walktrap skips minimal merge pairs on mid-size random networks |
| [F011](../findings.html#f011) | convention | Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance |
| [F036](../findings.html#f036) | convention | Adjusted Rand index is NaN on all-singleton partitions |
| [F038](../findings.html#f038) | convention | Spinglass reads the network as simple |
| [F039](../findings.html#f039) | defect | Triad census on multigraphs differs from the definition |
| [F040](../findings.html#f040) | convention | HITS returns 1 for an edgeless network |
{% endraw %}
