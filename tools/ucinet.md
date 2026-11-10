---
title: "UCINET"
layout: default
parent: Tools
---

{% raw %}
# UCINET

| Field | Value |
|---|---|
| Identifier | `ucinet` |
| Language | Windows desktop application |
| Version tested | 6.x (documentation audit) |
| License | proprietary |
| Homepage | none recorded |
| Role | documented-only |
| Citation | [borgatti2002ucinet](../references.html#borgatti2002ucinet) |

## How it was run

Not run. Capabilities are taken from the published help pages and the program documentation.

Capabilities listed by documentation audit of published help pages and program documentation.

## Coverage

| State | Measures |
|---|---|
| reported in docs (·) | 162 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | · reported in docs | `Betweenness: Freeman nodes, edges, normalized (percent), distance-weighted betweenness (6.798 fixes), flow betweenness, Newman random-walk betweenness, induced ; betw` |
| Centrality | [Bonacich](../measures/bonacich.html) | · reported in docs | `Bonacich power / beta centrality; betacent; bonamat` |
| Centrality | [Centralization](../measures/cat_centralization.html) | · reported in docs | `centralization` |
| Centrality | [Closeness](../measures/closeness.html) | · reported in docs | `Closeness: Freeman (inverse of total distance), unreachable set to max observed + 1 (default), n, or ignored; InClose/OutClose; reciprocal-distance variant` |
| Centrality | [Concent](../measures/cat_concent.html) | · reported in docs | `concent` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | · reported in docs |  |
| Centrality | [Eigenvector](../measures/eigenvector.html) | · reported in docs | `Eigenvector; symmetrized by max for directed; lambda-squared scores for several components (6.831 handles disconnected networks)` |
| Centrality | [Flow betweenness](../measures/flow_betweenness.html) | · reported in docs |  |
| Centrality | [Harmonic](../measures/harmonic.html) | · reported in docs | `fcent` |
| Centrality | [Hits](../measures/hits.html) | · reported in docs | `Hubs and authorities, SVD (two-mode fixes 6.748)` |
| Centrality | [Induced centrality](../measures/induced_centrality.html) | · reported in docs |  |
| Centrality | [Information centrality](../measures/information_centrality.html) | · reported in docs | `Information centrality (fails on singular input)` |
| Centrality | [Katz](../measures/katz.html) | · reported in docs | `Katz family (replaced Katz-Hubbell, 6.771)` |
| Centrality | [Kpp\_optimum / fragmentation](../measures/kpp_optimum-fragmentation.html) | · reported in docs |  |
| Centrality | [Kpp\_single / fragmentation](../measures/kpp_single-fragmentation.html) | · reported in docs | `Key player / group centrality; exhaustivekp` |
| Centrality | [Net\_centrality\_table() (raw and normalised columns)](../measures/centrality_table.html) | · reported in docs | `Multiple Measures (one table; no centralization); centrality` |
| Centrality | [Pagerank](../measures/pagerank.html) | · reported in docs | `PageRank` |
| Centrality | [Reach](../measures/reach.html) | · reported in docs |  |
| Centrality | [Strength](../measures/strength.html) | · reported in docs |  |
| Centrality | [Valente-Foreman integration and radiality](../measures/valente_foreman.html) | · reported in docs |  |
| Cohesion and subgroups | [Clique co-membership and overlap matrices](../measures/clique_overlap.html) | · reported in docs |  |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | · reported in docs | `Cohesion: k-cores, lambda sets, bicomponents, cut points, n-cliques, n-clans, k-plexes, cliques, factions; kcorelev` |
| Cohesion and subgroups | [Factions](../measures/cat_factions.html) | · reported in docs | `factions` |
| Cohesion and subgroups | [Factions errors](../measures/factions_errors.html) | · reported in docs |  |
| Cohesion and subgroups | [K plexes](../measures/k_plexes.html) | · reported in docs | `kplex` |
| Cohesion and subgroups | [Lambda sets](../measures/lambda_sets.html) | · reported in docs |  |
| Cohesion and subgroups | [Liststriads](../measures/cat_liststriads.html) | · reported in docs | `liststriads` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | · reported in docs | `cliqueoverlap; cliques` |
| Cohesion and subgroups | [N clans](../measures/n_clans.html) | · reported in docs |  |
| Cohesion and subgroups | [N cliques](../measures/n_cliques.html) | · reported in docs | `ncliques` |
| Cohesion and subgroups | [Simmelian ties](../measures/simmelian.html) | · reported in docs | `bowtie` |
| Communities | [Allpaths](../measures/cat_allpaths.html) | · reported in docs | `allpaths` |
| Communities | [Block (blockmodel from partition), Reduce](../measures/cat_block_blockmodel_from_partition_reduce.html) | · reported in docs | `Block (blockmodel from partition), Reduce` |
| Communities | [Fast greedy](../measures/fast_greedy.html) | · reported in docs | `Community detection (6.7xx): FastGreedy, LabelProp, LocalGreedy (6.809), Louvain-type, Moca, Girvan-Newman, factor-analysis clustering, polish partitions, Initi; FastGreedy` |
| Communities | [Girvan newman](../measures/girvan_newman.html) | · reported in docs |  |
| Communities | [Label propagation](../measures/label_propagation.html) | · reported in docs | `labelprop` |
| Communities | [Leading eigen](../measures/leading_eigen.html) | · reported in docs | `NCD` |
| Communities | [Leiden](../measures/leiden.html) | · reported in docs | `localgreedy` |
| Communities | [LocalGreedy, Moca, partition polishing, initial partitions](../measures/ucinet_community_extras.html) | · reported in docs |  |
| Communities | [Louvain modularity](../measures/louvain_modularity.html) | · reported in docs |  |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | · reported in docs |  |
| Components and connectivity | [Connectivity](../measures/connectivity.html) | · reported in docs | `cohesion` |
| Components and connectivity | [Cut points](../measures/cut_points.html) | · reported in docs | `cutpoints` |
| Components and connectivity | [Experienceflows](../measures/cat_experienceflows.html) | · reported in docs | `experienceflows` |
| Components and connectivity | [Flowsim](../measures/cat_flowsim.html) | · reported in docs | `flowsim` |
| Components and connectivity | [Fragmentation](../measures/fragmentation.html) | · reported in docs | `fragcent` |
| Data transforms | [Attribute to matrix (same, difference, sender, receiver)](../measures/attribute_matrix.html) | · reported in docs | `Node attribute editor, attribute to matrix (att2mat: same, difference, etc.)` |
| Data transforms | [Dichotomize](../measures/cat_dichotomize.html) | · reported in docs | `Dichotomize` |
| Data transforms | [Full symmetrize method set and dichotomize by density](../measures/symmetrize_methods.html) | · reported in docs | `Symmetrize` |
| Data transforms | [Local sparsification (L-Spar)](../measures/local_sparsification.html) | · reported in docs | `Local sparsification (6.831); lspar` |
| Data transforms | [Multiplex coding of several relations into one matrix](../measures/multiplex_coding.html) | · reported in docs | `Multiplex (super-sociomatrix coding, 0-3 for two binary relations)` |
| Data transforms | [Normalize ties (row, column, matrix; sum, mean, max, z, Euclidean, IPF)](../measures/normalize_ties.html) | · reported in docs | `Recode, Diagonal (set/ignore), Normalize (row, column, matrix; sum, mean, max, z, Euclidean, IPF)` |
| Data transforms | [Tucker congruence, factor rotation, iterative proportional fitting, state transitions](../measures/matrix_utils.html) | · reported in docs |  |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | · reported in docs |  |
| Descriptive statistics | [Centralization / betweenness](../measures/centralization-betweenness.html) | · reported in docs |  |
| Descriptive statistics | [Centralization / closeness](../measures/centralization-closeness.html) | · reported in docs |  |
| Descriptive statistics | [Centralization / degree](../measures/centralization-degree.html) | · reported in docs |  |
| Descriptive statistics | [Centralization eigenvector](../measures/centralization_eigenvector.html) | · reported in docs |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | · reported in docs | `Clustering coefficient (ClusteringCoefficient, nordcp, fagiolocc, oldcc CLI)` |
| Descriptive statistics | [Compactness](../measures/compactness.html) | · reported in docs |  |
| Descriptive statistics | [Components](../measures/components.html) | · reported in docs | `component; numcomp` |
| Descriptive statistics | [Degree](../measures/degree.html) | · reported in docs | `Degree (Freeman), in/out, normalized, centralization; degree; indeg; outdeg` |
| Descriptive statistics | [Density](../measures/density.html) | · reported in docs | `Density (overall; also average degree in CLI, 6.790); density` |
| Descriptive statistics | [Dyad census (mutual, asymmetric, null)](../measures/dyad_census.html) | · reported in docs |  |
| Descriptive statistics | [Ego size](../measures/ego_size.html) | · reported in docs | `Ego network density, size, ties, ego betweenness, ego composition (egocomp, 6.845), alter heterogeneity (IQV, Blau, Shannon; option to ignore ego's category, 6.` |
| Descriptive statistics | [Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)](../measures/krackhardt_dimensions.html) | · reported in docs | `Fragmentation, Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)` |
| Descriptive statistics | [Node reciprocity](../measures/nxo_node_reciprocity.html) | · reported in docs | `Reciprocity (arc vs dyad question has its own FAQ), normalized reciprocity (6.834); indrecip` |
| Descriptive statistics | [Normalized reciprocity and transitivity, DKS transitivity, cyclicity](../measures/ucinet_cohesion_variants.html) | · reported in docs |  |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | · reported in docs |  |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | · reported in docs | `Transitivity, normalized transitivity (6.831), Dekker-Krackhardt-Snijders transitivity (6.840), cyclicity (6.834, cyclicity); transitivity` |
| Descriptive statistics | [Triad census](../measures/triad_census.html) | · reported in docs | `Triad census, dyad census, hierarchy; nodetriadcensus` |
| Ego networks | [Ego composition: alter shares, Blau and Shannon heterogeneity, IQV](../measures/ego_composition.html) | · reported in docs |  |
| Generators and rewiring | [Clique, regular and bow-tie generators; all graphs of size n](../measures/misc_generators.html) | · reported in docs |  |
| Generators and rewiring | [Deterministic generators](../measures/deterministic_generators.html) | · reported in docs | `cycle; makeclique; path; star` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `ER; Random matrix generators (Erdos-Renyi, etc.)` |
| Generators and rewiring | [Random regular graph generator](../measures/gen_regular.html) | · reported in docs | `makeregular` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `smallworld` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `makeclumpy` |
| Graph theory and combinatorics | [Aic](../measures/cat_aic.html) | · reported in docs | `aic` |
| Graph theory and combinatorics | [Allgraphs](../measures/cat_allgraphs.html) | · reported in docs | `allgraphs` |
| Graph theory and combinatorics | [Combining similar relations](../measures/cat_combining_relations_similar.html) | · reported in docs | `Combining similar relations` |
| Graph theory and combinatorics | [Congru](../measures/cat_congru.html) | · reported in docs | `congru` |
| Graph theory and combinatorics | [Cpa](../measures/cat_cpa.html) | · reported in docs | `cpa` |
| Graph theory and combinatorics | [Dlbet](../measures/cat_dlbet.html) | · reported in docs | `dlbet` |
| Graph theory and combinatorics | [Dyconst](../measures/cat_dyconst.html) | · reported in docs | `dyconst` |
| Graph theory and combinatorics | [Facd](../measures/cat_facd.html) | · reported in docs | `facd` |
| Graph theory and combinatorics | [Groupden](../measures/cat_groupden.html) | · reported in docs | `groupden` |
| Graph theory and combinatorics | [Hiclus](../measures/cat_hiclus.html) | · reported in docs | `hiclus` |
| Graph theory and combinatorics | [Ipf](../measures/cat_ipf.html) | · reported in docs | `ipf` |
| Graph theory and combinatorics | [Makebowtie](../measures/cat_makebowtie.html) | · reported in docs | `makebowtie` |
| Graph theory and combinatorics | [Makeup](../measures/cat_makeup.html) | · reported in docs | `makeup` |
| Graph theory and combinatorics | [Numties](../measures/cat_numties.html) | · reported in docs | `numties` |
| Graph theory and combinatorics | [Opp](../measures/cat_opp.html) | · reported in docs | `opp` |
| Graph theory and combinatorics | [Ordinalassoc](../measures/cat_ordinalassoc.html) | · reported in docs | `ordinalassoc` |
| Graph theory and combinatorics | [Polish](../measures/cat_polish.html) | · reported in docs | `polish` |
| Graph theory and combinatorics | [Psi](../measures/cat_psi.html) | · reported in docs | `psi` |
| Graph theory and combinatorics | [Randomize](../measures/cat_randomize.html) | · reported in docs | `randomize` |
| Graph theory and combinatorics | [Rowlas](../measures/cat_rowlas.html) | · reported in docs | `rowlas` |
| Graph theory and combinatorics | [Rsh](../measures/cat_rsh.html) | · reported in docs | `rsh` |
| Graph theory and combinatorics | [Rwb](../measures/cat_rwb.html) | · reported in docs | `rwb` |
| Graph theory and combinatorics | [Socialprox](../measures/cat_socialprox.html) | · reported in docs | `socialprox` |
| Inference (QAP, null models) | [ANOVA density models (constant/variable homophily, structural blockmodel)](../measures/anova_density.html) | · reported in docs |  |
| Inference (QAP, null models) | [Conditional uniform graph tests and null models](../measures/cug_null_models.html) | · reported in docs | `Conditional uniform graph tests, TERGM/ERGM are not UCINET` |
| Inference (QAP, null models) | [Group-level permutation tests](../measures/node_permutation_tests.html) | · reported in docs | `Network-level hypothesis tests: t-test on densities, bootstrap, permutation of node labels` |
| Inference (QAP, null models) | [Logistic MR-QAP](../measures/lr_qap.html) | · reported in docs | `LR-QAP (logistic, 6.763 help file, 6.839 three times faster)` |
| Inference (QAP, null models) | [MR-QAP regression (Y-permutation, double semi-partialling)](../measures/qap_regression.html) | · reported in docs | `Logistic regression with 2-tailed tests (6.751), OLS regression, univariate statistics, correlation, ANOVA/density-by-group (blocks), contingency tables with od; logistic; regress` |
| Inference (QAP, null models) | [Network autocorrelation: lag/error model, Moran, Geary](../measures/network_autocorrelation.html) | · reported in docs | `Geary; Network autocorrelation (continuous, 6.753): Moran, Geary; lautocorr` |
| Inference (QAP, null models) | [QAP correlation (Y-permutation, exact and Monte Carlo)](../measures/qap_correlation.html) | · reported in docs | `QAP; QAP correlation (2-tailed default since 6.839), QAP regression (MR-QAP rewritten 6.829; seed fix 6.805; "count in dyad" effect 6.833; FAQ on how coefficients ar; corr; corrmat; rectqap` |
| Input and output | [Excel (xlsx) reader and writer](../measures/io_xlsx.html) | · reported in docs |  |
| Input and output | [Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA](../measures/io_ucinet_multi.html) | · reported in docs |  |
| Input and output | [UCINET binary dataset reader (.##h / .##d)](../measures/io_ucinet_binary.html) | · reported in docs |  |
| Input and output | [UCINET DL text read and write](../measures/io_dl.html) | · reported in docs |  |
| Matrices and spectra | [Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence)](../measures/matrix_operators.html) | · reported in docs | `transition` |
| Matrices and spectra | [Incidence](../measures/gm_incidence.html) | · reported in docs | `bipartite` |
| Mixing and assortativity | [Assortativity nominal](../measures/assortativity_nominal.html) | · reported in docs | `categonethomophily; homophily` |
| Mixing and assortativity | [Ei index](../measures/ei_index.html) | · reported in docs | `E-I index; EI` |
| Mixing and assortativity | [Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed)](../measures/cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected.html) | · reported in docs | `Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed)` |
| Mixing and assortativity | [Mixing](../measures/mixing.html) | · reported in docs | `Homophily: categorical (categonethomophily), continuous attributes (own FAQ), PropSame (6.793), mixing matrices / tables (6.813, 6.837)` |
| Paths and distances | [Diameter](../measures/diameter.html) | · reported in docs |  |
| Paths and distances | [Distances](../measures/distances.html) | · reported in docs | `Distance: geodesics (parallel routine 6.745), reachability, diameter, mean distance, compactness, breadth; floyd; geo` |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | · reported in docs | `Eccentricity, Radiality, Integration, Delta/fragmentation (fragcent CLI 6.746), DW fragmentation and reach` |
| Paths and distances | [Mean distance](../measures/mean_distance.html) | · reported in docs |  |
| Paths and distances | [Proximity](../measures/proximity.html) | · reported in docs | `Prestige: proximity prestige, rank, domain` |
| Paths and distances | [Reachability](../measures/reachability.html) | · reported in docs |  |
| Paths and distances | [Structural equivalence: profile (correlation, Euclidean, etc ), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row](../measures/cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural.html) | · reported in docs | `Structural equivalence: profile (correlation, Euclidean, etc.), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row` |
| Roles and positions | [Automorphic (Max Sim) and regular equivalence (REGE, CATREGE)](../measures/cat_automorphic_catrege_equivalence_max_rege_regular_sim.html) | · reported in docs | `Automorphic (MaxSim) and regular equivalence (REGE, CATREGE)` |
| Roles and positions | [Automorphic equivalence](../measures/automorphic_equivalence.html) | · reported in docs | `orbits` |
| Roles and positions | [Block density](../measures/block_density.html) | · reported in docs |  |
| Roles and positions | [Bridging centrality](../measures/bridging_centrality.html) | · reported in docs | `Bridging measures (6.843); bridging` |
| Roles and positions | [Bridging coefficient](../measures/bridging_coefficient.html) | · reported in docs |  |
| Roles and positions | [Brokerage](../measures/brokerage.html) | · reported in docs | `Brokerage: Gould-Fernandez roles (five or six); brokerageconcentration` |
| Roles and positions | [Classical mds](../measures/classical_mds.html) | · reported in docs | `MDS (metric, classic, non-metric), Guttman scaling (6.831), correspondence analysis, factor analysis; classicmds` |
| Roles and positions | [Cognitive social structures with accuracy measures](../measures/css_accuracy.html) | · reported in docs | `Zegers CLI, cultural consonance model, CSS (cognitive social structures) with accuracy measures` |
| Roles and positions | [Concor](../measures/concor.html) | · reported in docs | `CONCOR, hierarchical clustering, blockmodels, optimization; ccsplit` |
| Roles and positions | [Constraint](../measures/constraint.html) | · reported in docs | `constraint` |
| Roles and positions | [Core periphery](../measures/core_periphery.html) | · reported in docs | `Core/periphery: categorical (Borgatti-Everett), continuous coreness, Estevez-Nordlund variant (6.833); catcp` |
| Roles and positions | [Core periphery continuous](../measures/core_periphery_continuous.html) | · reported in docs | `contcp` |
| Roles and positions | [Direct blockmodel search (structural, regular, generalised block types)](../measures/blockmodel_search.html) | · reported in docs |  |
| Roles and positions | [Effective size](../measures/effective_size.html) | · reported in docs | `structuralholes` |
| Roles and positions | [Efficiency](../measures/efficiency.html) | · reported in docs |  |
| Roles and positions | [Egotize (6 750), Ego network extraction with tab "Ego"](../measures/cat_6_750_ego_egotize_extraction_tab_with.html) | · reported in docs | `Egotize (6.750), Ego network extraction with tab "Ego"` |
| Roles and positions | [Equivalence measures: matches, positive matches, overlaps, cross-products, coverage](../measures/equivalence_extra.html) | · reported in docs |  |
| Roles and positions | [Estevez-Nordlund variant](../measures/core_periphery_en.html) | · reported in docs | `enordcp` |
| Roles and positions | [Guttman scaling, K-means and quick clustering](../measures/guttman_kmeans.html) | · reported in docs | `K-means, quick clustering (quickclus, 6.770); guttman; kmeans; quickclus` |
| Roles and positions | [Hierarchy](../measures/hierarchy.html) | · reported in docs |  |
| Roles and positions | [Makeegonets](../measures/cat_makeegonets.html) | · reported in docs | `makeegonets` |
| Roles and positions | [Non-metric MDS with stress-1](../measures/mds_nonmetric.html) | · reported in docs |  |
| Roles and positions | [Regular equivalence](../measures/regular_equivalence.html) | · reported in docs |  |
| Roles and positions | [Structural equivalence](../measures/structural_equivalence.html) | · reported in docs | `SE` |
| Roles and positions | [Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6 798), "corrected constraint" FA](../measures/cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural.html) | · reported in docs | `Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6.798), "corrected constraint" FA` |
| Signed and multilayer | [Positive-negative centrality (signed ties)](../measures/pn_centrality.html) | · reported in docs | `pncent` |
| Two-mode and bipartite | [Ego\_summary / betweenness](../measures/ego_summary-betweenness.html) | · reported in docs |  |
| Two-mode and bipartite | [Ego\_summary / density](../measures/ego_summary-density.html) | · reported in docs | `egodensity` |
| Two-mode and bipartite | [Ego\_summary / ties](../measures/ego_summary-ties.html) | · reported in docs |  |
| Two-mode and bipartite | [Project](../measures/project.html) | · reported in docs | `Affiliations (2-mode to 1-mode): co-membership values 0-4; cosine similarity (6.833); old routine "to avoid"; bprod; bxtx; bxxt; xtx; xxt` |
| Two-mode and bipartite | [Two-mode core-periphery, bi-cliques, two-mode equivalence](../measures/twomode_core_biclique.html) | · reported in docs | `Two-mode core-periphery, bi-cliques, factions; biclique` |
| Two-mode and bipartite | [Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine)](../measures/projection_weights.html) | · reported in docs |  |
| Two-mode and bipartite | [Twomode / betweenness](../measures/twomode-betweenness.html) | · reported in docs |  |
| Two-mode and bipartite | [Twomode / closeness](../measures/twomode-closeness.html) | · reported in docs |  |
| Two-mode and bipartite | [Twomode / degree](../measures/twomode-degree.html) | · reported in docs | `2-mode centrality` |
| Two-mode and bipartite | [Twomode / density](../measures/twomode-density.html) | · reported in docs | `2-mode eigenvector, SVD, matching 2-mode, bipartite/density` |
| Two-mode and bipartite | [Twomode / eigenvector](../measures/twomode-eigenvector.html) | · reported in docs |  |
{% endraw %}
