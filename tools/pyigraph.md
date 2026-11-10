---
title: "igraph (Python)"
layout: default
parent: Tools
---

{% raw %}
# igraph (Python)

| Field | Value |
|---|---|
| Identifier | `pyigraph` |
| Language | Python over C |
| Version tested | 1.0.0 |
| License | GPL-2.0-or-later |
| Homepage | <https://python.igraph.org> |
| Role | checked |
| Citation | [csardi2006igraph](../references.html#csardi2006igraph) |

## How it was run

Imported in CPython; Graph methods and module functions called on graph objects.

Capabilities listed by introspection of python-igraph Graph methods and module functions.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 27 |
| checked, differs by convention (≠) | 3 |
| reported in docs (·) | 132 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ✓ checked, agrees | `betweenness` |
| Centrality | [Closeness](../measures/closeness.html) | ✓ checked, agrees | `closeness` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | · reported in docs | `edge_betweenness` |
| Centrality | [Eigenvector](../measures/eigenvector.html) | ≠ checked, differs by convention | `eigenvector_centrality` |
| Centrality | [Harmonic](../measures/harmonic.html) | ✓ checked, agrees | `harmonic_centrality` |
| Centrality | [Hits](../measures/hits.html) | ≠ checked, differs by convention | `authority_score; hub_score` |
| Centrality | [Load](../measures/cx_load.html) | · reported in docs | `Load` |
| Centrality | [Pagerank](../measures/pagerank.html) | ✓ checked, agrees | `pagerank; personalized_pagerank` |
| Centrality | [Strength](../measures/strength.html) | ✓ checked, agrees | `strength` |
| Cohesion and subgroups | [Clique number](../measures/clique_number.html) | ✓ checked, agrees | `clique_number` |
| Cohesion and subgroups | [Cocitation and bibliographic coupling](../measures/cocitation.html) | · reported in docs | `bibcoupling; cocitation` |
| Cohesion and subgroups | [Cohesive blocks](../measures/cat_blocks_cohesive.html) | · reported in docs | `cohesive_blocks` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ✓ checked, agrees | `coreness; k_core` |
| Cohesion and subgroups | [Is clique](../measures/cat_clique_is.html) | · reported in docs | `is_clique` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | ✓ checked, agrees | `cliques; largest_cliques; maximal_cliques` |
| Cohesion and subgroups | [Motif census](../measures/motif_census.html) | · reported in docs | `motifs_randesu; motifs_randesu_estimate; motifs_randesu_no` |
| Communities | [Community voronoi](../measures/cat_community_voronoi.html) | · reported in docs | `community_voronoi` |
| Communities | [Compare partitions](../measures/compare_partitions.html) | · reported in docs | `compare_communities; split_join_distance` |
| Communities | [Fast greedy](../measures/fast_greedy.html) | · reported in docs | `community_fastgreedy` |
| Communities | [Fluid communities](../measures/fluid_communities.html) | · reported in docs | `community_fluid_communities` |
| Communities | [Girvan newman](../measures/girvan_newman.html) | · reported in docs | `community_edge_betweenness` |
| Communities | [Infomap](../measures/infomap.html) | · reported in docs | `community_infomap` |
| Communities | [Label propagation](../measures/label_propagation.html) | · reported in docs | `community_label_propagation` |
| Communities | [Leading eigen](../measures/leading_eigen.html) | · reported in docs | `community_leading_eigenvector` |
| Communities | [Leiden](../measures/leiden.html) | · reported in docs | `community_leiden` |
| Communities | [Louvain modularity](../measures/louvain_modularity.html) | · reported in docs | `community_multilevel` |
| Communities | [Modularity](../measures/modularity.html) | ✓ checked, agrees | `modularity` |
| Communities | [Optimal modularity](../measures/optimal_modularity.html) | · reported in docs | `community_optimal_modularity` |
| Communities | [Spinglass](../measures/spinglass.html) | · reported in docs | `community_spinglass` |
| Communities | [Walktrap](../measures/walktrap.html) | · reported in docs | `community_walktrap` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | · reported in docs | `biconnected_components` |
| Components and connectivity | [Bridges](../measures/bridges.html) | · reported in docs | `bridges` |
| Components and connectivity | [Connectivity](../measures/connectivity.html) | · reported in docs | `adhesion; cohesion` |
| Components and connectivity | [Cut points](../measures/cut_points.html) | ✓ checked, agrees | `articulation_points` |
| Components and connectivity | [Dominator](../measures/cat_dominator.html) | · reported in docs | `dominator` |
| Components and connectivity | [Gomory hu](../measures/gomory_hu.html) | · reported in docs | `gomory_hu_tree` |
| Components and connectivity | [Max flow](../measures/max_flow.html) | · reported in docs | `maxflow; maxflow_value` |
| Components and connectivity | [Min cut](../measures/min_cut.html) | · reported in docs | `mincut; mincut_value; st_mincut` |
| Components and connectivity | [Node cut](../measures/node_cut.html) | · reported in docs | `all_minimal_st_separators; all_st_cuts; all_st_mincuts; is_minimal_separator; is_separator; minimum_size_separators` |
| Data transforms | [Graph complement](../measures/op_complement.html) | · reported in docs | `complementer` |
| Data transforms | [Line graph](../measures/line_graph.html) | · reported in docs | `linegraph` |
| Data transforms | [Op compose](../measures/op_compose.html) | · reported in docs | `compose` |
| Data transforms | [Op difference](../measures/op_difference.html) | · reported in docs | `difference` |
| Data transforms | [Op intersection](../measures/op_intersection.html) | · reported in docs | `intersection` |
| Data transforms | [Op union](../measures/op_union.html) | · reported in docs | `disjoint_union; union` |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ✓ checked, agrees | `transitivity_avglocal_undirected` |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ✓ checked, agrees | `transitivity_local_undirected` |
| Descriptive statistics | [Components](../measures/components.html) | ✓ checked, agrees | `components; decompose; is_biconnected; is_connected; subcomponent` |
| Descriptive statistics | [Degree](../measures/degree.html) | ✓ checked, agrees | `degree; degree_distribution; mean_degree` |
| Descriptive statistics | [Density](../measures/density.html) | ✓ checked, agrees | `density` |
| Descriptive statistics | [Dyad census (mutual, asymmetric, null)](../measures/dyad_census.html) | · reported in docs | `dyad_census` |
| Descriptive statistics | [Knn](../measures/cat_knn.html) | · reported in docs | `knn` |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | ✓ checked, agrees | `reciprocity` |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ✓ checked, agrees | `transitivity_undirected` |
| Descriptive statistics | [Triad census](../measures/triad_census.html) | ≠ checked, differs by convention | `triad_census` |
| Descriptive statistics | [Triangles](../measures/nxo_triangles.html) | · reported in docs | `list_triangles` |
| Generators and rewiring | [Bipartite degree-sequence realization](../measures/gen_realize_bipartite.html) | · reported in docs | `Realize_Bipartite_Degree_Sequence` |
| Generators and rewiring | [Chung-Lu (expected degree) generator](../measures/gen_chung_lu.html) | · reported in docs | `Chung_Lu` |
| Generators and rewiring | [Citation-type growth generators](../measures/gen_citation.html) | · reported in docs | `Full_Citation` |
| Generators and rewiring | [Configuration model](../measures/gen_configuration.html) | · reported in docs | `Degree_Sequence` |
| Generators and rewiring | [De Bruijn graph generator](../measures/gen_de_bruijn.html) | · reported in docs | `De_Bruijn` |
| Generators and rewiring | [Deterministic generators](../measures/deterministic_generators.html) | · reported in docs | `Full; Full_Bipartite; Hypercube; Ring; Star; Tree` |
| Generators and rewiring | [Deterministic realisation of a degree sequence](../measures/gen_degree_realization.html) | · reported in docs | `Realize_Degree_Sequence` |
| Generators and rewiring | [Forest fire generator](../measures/gen_forest_fire.html) | · reported in docs | `Forest_Fire` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `Erdos_Renyi` |
| Generators and rewiring | [Growing random graph generator](../measures/gen_growing.html) | · reported in docs | `Growing_Random` |
| Generators and rewiring | [Hexagonal lattice graph](../measures/cat_hexagonal_lattice.html) | · reported in docs | `Hexagonal_Lattice` |
| Generators and rewiring | [Is complete](../measures/cat_complete_is.html) | · reported in docs | `is_complete` |
| Generators and rewiring | [Kautz graph generator](../measures/gen_kautz.html) | · reported in docs | `Kautz` |
| Generators and rewiring | [Lattice generator](../measures/gen_lattice.html) | · reported in docs | `Lattice` |
| Generators and rewiring | [LCF notation graph generator](../measures/gen_lcf.html) | · reported in docs | `LCF` |
| Generators and rewiring | [Nearest Neighbor Graph](../measures/cat_nearest_neighbor.html) | · reported in docs | `Nearest_Neighbor_Graph` |
| Generators and rewiring | [Preference (types) random graph generator](../measures/gen_preference.html) | · reported in docs | `Asymmetric_Preference; Preference` |
| Generators and rewiring | [Preferential attachment generator](../measures/gen_preferential.html) | · reported in docs | `Barabasi; Recent_Degree` |
| Generators and rewiring | [Random bipartite graph generator](../measures/gen_random_bipartite.html) | · reported in docs | `Random_Bipartite` |
| Generators and rewiring | [Random geometric graph generator](../measures/gen_geometric.html) | · reported in docs | `GRG` |
| Generators and rewiring | [Random regular graph generator](../measures/gen_regular.html) | · reported in docs | `K_Regular` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `Watts_Strogatz` |
| Generators and rewiring | [Static fitness and static power-law generators](../measures/gen_static_fitness.html) | · reported in docs | `Static_Fitness; Static_Power_Law` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `SBM` |
| Generators and rewiring | [Swap contract](../measures/swap_contract.html) | · reported in docs | `rewire` |
| Generators and rewiring | [Tree Game](../measures/cat_game_tree.html) | · reported in docs | `Tree_Game` |
| Generators and rewiring | [Triangular lattice graph](../measures/cat_lattice_triangular.html) | · reported in docs | `Triangular_Lattice` |
| Graph theory and combinatorics | [Alpha](../measures/cat_alpha.html) | · reported in docs | `alpha` |
| Graph theory and combinatorics | [Automorphism group, count and canonical form](../measures/automorphisms.html) | · reported in docs | `automorphism_group; canonical_permutation; count_automorphisms` |
| Graph theory and combinatorics | [Contracted nodes](../measures/nxs_contracted_nodes.html) | · reported in docs | `contract_vertices` |
| Graph theory and combinatorics | [Convergence degree](../measures/cat_convergence_degree.html) | · reported in docs | `convergence_degree` |
| Graph theory and combinatorics | [Convergence field size](../measures/cat_convergence_field_size.html) | · reported in docs | `convergence_field_size` |
| Graph theory and combinatorics | [Convex hull](../measures/cat_convex_hull.html) | · reported in docs | `convex_hull` |
| Graph theory and combinatorics | [Diversity](../measures/cat_diversity.html) | · reported in docs | `diversity` |
| Graph theory and combinatorics | [Establishment](../measures/cat_establishment.html) | · reported in docs | `Establishment` |
| Graph theory and combinatorics | [Farthest points](../measures/cat_farthest_points.html) | · reported in docs | `farthest_points` |
| Graph theory and combinatorics | [Feedback arc and vertex sets](../measures/feedback_sets.html) | · reported in docs | `feedback_arc_set; feedback_vertex_set` |
| Graph theory and combinatorics | [Forest flags](../measures/nxs_forest_flags.html) | · reported in docs | `is_tree` |
| Graph theory and combinatorics | [From prufer](../measures/nxs_from_prufer.html) | · reported in docs | `Prufer` |
| Graph theory and combinatorics | [Girth](../measures/girth.html) | · reported in docs | `girth` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | · reported in docs | `vertex_coloring_greedy` |
| Graph theory and combinatorics | [Is bigraphical](../measures/cat_bigraphical_is.html) | · reported in docs | `is_bigraphical` |
| Graph theory and combinatorics | [Is graphical](../measures/cat_graphical_is.html) | · reported in docs | `is_graphical` |
| Graph theory and combinatorics | [Is independent vertex set](../measures/cat_independent_is_set.html) | · reported in docs | `is_independent_vertex_set` |
| Graph theory and combinatorics | [Link prediction](../measures/link_prediction.html) | · reported in docs | `similarity_dice; similarity_inverse_log_weighted; similarity_jaccard` |
| Graph theory and combinatorics | [Mis](../measures/mis.html) | · reported in docs | `independent_vertex_sets; largest_independent_vertex_sets; maximal_independent_vertex_sets` |
| Graph theory and combinatorics | [Prufer](../measures/nxs_prufer.html) | · reported in docs | `to_prufer` |
| Graph theory and combinatorics | [Simple cycles](../measures/simple_cycles.html) | · reported in docs | `fundamental_cycles; minimum_cycle_basis; simple_cycles` |
| Graph theory and combinatorics | [St chordal](../measures/st_chordal.html) | · reported in docs | `chordal_completion; is_chordal` |
| Graph theory and combinatorics | [Umap compute weights](../measures/cat_umap_weights.html) | · reported in docs | `umap_compute_weights` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | · reported in docs | `count_automorphisms_vf2; count_isomorphisms_vf2; count_subisomorphisms_vf2; get_automorphisms_vf2; get_isomorphisms_vf2; get_subisomorphisms_lad; get_subisomorphisms_vf2; isomorphic; isomorphic_bliss; isomorphic_vf2; subisomorphic_lad; subisomorphic_vf2` |
| Input and output | [ADJACENCY read and write](../measures/io_adjacency.html) | · reported in docs | `Read_Adjacency` |
| Input and output | [DIMACS read and write](../measures/io_dimacs.html) | · reported in docs | `Read_DIMACS; write_dimacs` |
| Input and output | [EDGELIST read and write](../measures/io_edgelist.html) | · reported in docs | `Read_Edgelist; write_edgelist` |
| Input and output | [GML read and write](../measures/io_gml.html) | · reported in docs | `Read_GML; write_gml` |
| Input and output | [GRAPHDB read and write](../measures/io_graphdb.html) | · reported in docs | `Read_GraphDB` |
| Input and output | [GraphML read and write](../measures/io_graphml.html) | · reported in docs | `Read_GraphML; Read_GraphMLz; write_graphml; write_graphmlz` |
| Input and output | [GRAPHVIZ read and write](../measures/io_graphviz.html) | · reported in docs | `write_dot` |
| Input and output | [LEDA read and write](../measures/io_leda.html) | · reported in docs | `write_leda` |
| Input and output | [LGL read and write](../measures/io_lgl.html) | · reported in docs | `Read_Lgl; write_lgl` |
| Input and output | [NCOL read and write](../measures/io_ncol.html) | · reported in docs | `Read_Ncol; write_ncol` |
| Input and output | [Pajek .net read and write](../measures/io_pajek.html) | · reported in docs | `Read_Pajek; write_pajek` |
| Input and output | [PICKLE read and write](../measures/io_pickle.html) | · reported in docs | `Read_Pickle; Read_Picklez; write_pickle; write_picklez` |
| Input and output | [SVG read and write](../measures/io_svg.html) | · reported in docs | `write_svg` |
| Input and output | [UCINET DL text read and write](../measures/io_dl.html) | · reported in docs | `Read_DL` |
| Layout | [Circle, tree and two-mode (barycenter) layouts](../measures/layout_simple.html) | · reported in docs | `layout_reingold_tilford; layout_reingold_tilford_circular` |
| Layout | [Davidson-Harel layout](../measures/layout_dh.html) | · reported in docs | `layout_davidson_harel` |
| Layout | [DrL (OpenOrd) layout](../measures/layout_drl.html) | · reported in docs | `layout_drl` |
| Layout | [Fruchterman-Reingold layout](../measures/layout_fruchterman_reingold.html) | · reported in docs | `layout_fruchterman_reingold; layout_fruchterman_reingold_3d` |
| Layout | [Graphopt layout](../measures/layout_graphopt.html) | · reported in docs | `layout_graphopt` |
| Layout | [Kamada-Kawai layout](../measures/layout_kamada_kawai.html) | · reported in docs | `layout_kamada_kawai; layout_kamada_kawai_3d` |
| Layout | [Large graph layout (LGL)](../measures/layout_lgl.html) | · reported in docs | `layout_lgl` |
| Layout | [Multidimensional scaling layout](../measures/layout_mds.html) | · reported in docs | `layout_mds` |
| Layout | [Sugiyama layered layout](../measures/layout_sugiyama.html) | · reported in docs | `layout_sugiyama` |
| Matrices and spectra | [Adjacency](../measures/gm_adjacency.html) | · reported in docs | `get_adjacency; get_adjacency_sparse` |
| Matrices and spectra | [Gm laplacian](../measures/gm_laplacian.html) | · reported in docs | `laplacian` |
| Matrices and spectra | [Gm modularity](../measures/gm_modularity.html) | · reported in docs | `modularity_matrix` |
| Matrices and spectra | [Graph spectrum (eigenvalues of a graph matrix)](../measures/graph_spectrum.html) | · reported in docs | `eigen_adjacency` |
| Matrices and spectra | [Incidence](../measures/gm_incidence.html) | · reported in docs | `get_biadjacency` |
| Mixing and assortativity | [Assortativity degree](../measures/assortativity_degree.html) | ✓ checked, agrees |  |
| Mixing and assortativity | [Assortativity nominal](../measures/assortativity_nominal.html) | ✓ checked, agrees |  |
| Mixing and assortativity | [Assortativity values](../measures/assortativity_values.html) | ✓ checked, agrees | `assortativity; assortativity_degree; assortativity_nominal` |
| Paths and distances | [Diameter](../measures/diameter.html) | ✓ checked, agrees | `diameter; get_diameter` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees | `distances` |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ✓ checked, agrees | `eccentricity` |
| Paths and distances | [Mean distance](../measures/mean_distance.html) | ✓ checked, agrees | `average_path_length; path_length_hist` |
| Paths and distances | [Paths all shortest](../measures/paths_all_shortest.html) | · reported in docs | `get_all_shortest_paths` |
| Paths and distances | [Paths astar](../measures/paths_astar.html) | · reported in docs | `get_shortest_path_astar` |
| Paths and distances | [Paths k shortest](../measures/paths_k_shortest.html) | · reported in docs | `get_k_shortest_paths` |
| Paths and distances | [Paths simple](../measures/paths_simple.html) | · reported in docs | `get_all_simple_paths` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `get_shortest_path; get_shortest_paths` |
| Paths and distances | [Radius](../measures/radius.html) | ✓ checked, agrees | `radius` |
| Paths and distances | [Reachability](../measures/reachability.html) | ✓ checked, agrees | `neighborhood_size` |
| Roles and positions | [Constraint](../measures/constraint.html) | ✓ checked, agrees | `constraint` |
| Statistical fitting | [Power-law fit of a degree distribution](../measures/power_law_fit.html) | · reported in docs | `power_law_fit` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `bfs; bfsiter` |
| Traversal, trees and DAGs | [Edge dfs](../measures/trav_edge_dfs.html) | · reported in docs | `dfs; dfsiter` |
| Traversal, trees and DAGs | [Is dag](../measures/is_dag.html) | · reported in docs | `is_acyclic; is_dag` |
| Traversal, trees and DAGs | [Maximum cardinality search](../measures/cat_cardinality_maximum_search.html) | · reported in docs | `maximum_cardinality_search` |
| Traversal, trees and DAGs | [Random walks](../measures/random_walk.html) | · reported in docs | `random_walk` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | · reported in docs | `spanning_tree` |
| Traversal, trees and DAGs | [Topological sort](../measures/topological_sort.html) | · reported in docs | `topological_sorting` |
| Traversal, trees and DAGs | [Unfold tree](../measures/cat_tree_unfold.html) | · reported in docs | `unfold_tree` |
| Two-mode and bipartite | [Bipartite color](../measures/bipartite_color.html) | · reported in docs | `is_bipartite` |
| Two-mode and bipartite | [Hopcroft karp](../measures/hopcroft_karp.html) | · reported in docs | `maximum_bipartite_matching` |
| Two-mode and bipartite | [Project](../measures/project.html) | · reported in docs | `bipartite_projection; bipartite_projection_size` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F074](../findings.html#f074) | limitation | assortativity\_nominal(normalized=False) raises SystemError; eigenvector\_centrality(directed=False) on a directed graph raises Invalid mode |
| [F075](../findings.html#f075) | limitation | Alpha and power centrality exist only in the R binding |
{% endraw %}
