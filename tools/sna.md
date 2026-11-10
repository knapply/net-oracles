---
title: "sna"
layout: default
parent: Tools
---

{% raw %}
# sna

| Field | Value |
|---|---|
| Identifier | `sna` |
| Language | R |
| Version tested | 2.8 |
| License | GPL-2.0-or-later |
| Homepage | <https://cran.r-project.org/package=sna> |
| Role | checked |
| Citation | [butts2008sna](../references.html#butts2008sna) |

## How it was run

Called from R on adjacency matrices (the package works on matrices and edge arrays).

Capabilities listed by introspection of R package sna: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 12 |
| checked, differs by convention (≠) | 10 |
| reported in docs (·) | 48 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | ≠ checked, differs by convention | `betweenness` |
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness simple](../measures/centrality/betweenness.html#betweenness_simple) | ✓ checked, agrees |  |
| Centrality | Betweenness, load and flow | [Flow betweenness](../measures/centrality/flow_betweenness.html) | [Flow betweenness](../measures/centrality/flow_betweenness.html#flow_betweenness) | ≠ checked, differs by convention | `flowbet` |
| Centrality | Betweenness, load and flow | [Load centrality](../measures/centrality/load_centrality.html) | [Loadcent](../measures/centrality/load_centrality.html#cat_loadcent) | · reported in docs | `loadcent` |
| Centrality | Betweenness, load and flow | [Stress centrality](../measures/centrality/stress_centrality.html) | [Stresscent](../measures/centrality/stress_centrality.html#cat_stresscent) | · reported in docs | `stresscent` |
| Centrality | Centralization and tables | [Centralization](../measures/centrality/centralization.html) | [Centralization / betweenness](../measures/centrality/centralization.html#centralization-betweenness) | ≠ checked, differs by convention | `centralization` |
| Centrality | Centralization and tables | [Centralization](../measures/centrality/centralization.html) | [Centralization / closeness](../measures/centrality/centralization.html#centralization-closeness) | ✓ checked, agrees |  |
| Centrality | Centralization and tables | [Centralization](../measures/centrality/centralization.html) | [Centralization / degree](../measures/centrality/centralization.html#centralization-degree) | ✓ checked, agrees |  |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | ≠ checked, differs by convention | `degree` |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree simple](../measures/centrality/degree.html#degree_simple) | ✓ checked, agrees |  |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | ✓ checked, agrees | `closeness` |
| Centrality | Distance-based | [Graph centrality (inverse eccentricity)](../measures/centrality/graph_centrality.html) | [Graphcent](../measures/centrality/graph_centrality.html#cat_graphcent) | · reported in docs | `graphcent` |
| Centrality | Distance-based | [Harmonic centrality](../measures/centrality/harmonic_centrality.html) | [Harmonic](../measures/centrality/harmonic_centrality.html#harmonic) | ≠ checked, differs by convention |  |
| Centrality | Distance-based | [Reach and m-reach](../measures/centrality/reach_centrality.html) | [Reach](../measures/centrality/reach_centrality.html#reach) | · reported in docs | `reachability` |
| Centrality | Local and structural scores | [Gil-Schmidt power index](../measures/centrality/gil_schmidt_power.html) | [Gilschmidt](../measures/centrality/gil_schmidt_power.html#cat_gilschmidt) | · reported in docs | `gilschmidt` |
| Centrality | Local and structural scores | [Prestige](../measures/centrality/prestige.html) | [Prestige](../measures/centrality/prestige.html#cat_prestige) | · reported in docs | `prestige` |
| Centrality | Resistance and information | [Information centrality (current-flow closeness)](../measures/centrality/information_centrality.html) | [Information centrality](../measures/centrality/information_centrality.html#information_centrality) | ≠ checked, differs by convention | `infocent` |
| Centrality | Spectral and walk-based | [Bonacich power centrality](../measures/centrality/bonacich_power.html) | [Bonacich](../measures/centrality/bonacich_power.html#bonacich) | ✓ checked, agrees | `bonpow` |
| Centrality | Spectral and walk-based | [Eigenvector centrality](../measures/centrality/eigenvector_centrality.html) | [Eigenvector](../measures/centrality/eigenvector_centrality.html#eigenvector) | ≠ checked, differs by convention | `evcent` |
| Cohesion and subgroups | Cliques | [Clique census](../measures/cohesion-and-subgroups/clique_census.html) | [Clique census](../measures/cohesion-and-subgroups/clique_census.html#cat_census_clique) | · reported in docs | `clique.census` |
| Cohesion and subgroups | Cores, trusses and cohesive blocks | [K-core decomposition](../measures/cohesion-and-subgroups/k_core.html) | [Coreness](../measures/cohesion-and-subgroups/k_core.html#coreness) | · reported in docs | `kcores` |
| Cohesion and subgroups | Relaxed cliques and subgroups | [Simmelian ties](../measures/cohesion-and-subgroups/simmelian_ties.html) | [Simmelian ties](../measures/cohesion-and-subgroups/simmelian_ties.html#simmelian) | · reported in docs | `simmelian` |
| Components and connectivity | Articulation points, bridges and biconnected components | [Biconnected components](../measures/components-and-connectivity/biconnected_components.html) | [Bicomponents](../measures/components-and-connectivity/biconnected_components.html#bicomponents) | · reported in docs | `bicomponent.dist` |
| Components and connectivity | Articulation points, bridges and biconnected components | [Cut points (articulation points)](../measures/components-and-connectivity/cut_points.html) | [Cut points](../measures/components-and-connectivity/cut_points.html#cut_points) | ✓ checked, agrees | `cutpoints` |
| Components and connectivity | Connected components | [Connected components](../measures/components-and-connectivity/connected_components.html) | [Components](../measures/components-and-connectivity/connected_components.html#components) | · reported in docs | `component.dist; component.largest; component.size.byvertex; components; is.connected` |
| Components and connectivity | Flows and flow trees | [Maximum flow](../measures/components-and-connectivity/max_flow.html) | [Max flow](../measures/components-and-connectivity/max_flow.html#max_flow) | · reported in docs | `maxflow` |
| Data transforms | Matrix and tie transformations | [Symmetrize](../measures/data-transforms/symmetrize.html) | [Full symmetrize method set and dichotomize by density](../measures/data-transforms/symmetrize.html#symmetrize_methods) | · reported in docs | `symmetrize` |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Transitivity](../measures/descriptive-statistics/global_transitivity.html#transitivity) | · reported in docs | `gt; gtrans` |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Weak and strong transitivity; directed and weighted clustering conventions](../measures/descriptive-statistics/global_transitivity.html#sna_transitivity) | · reported in docs |  |
| Descriptive statistics | Density and degree distribution | [Central graph](../measures/descriptive-statistics/central_graph.html) | [Centralgraph](../measures/descriptive-statistics/central_graph.html#cat_centralgraph) | · reported in docs | `centralgraph` |
| Descriptive statistics | Density and degree distribution | [Density](../measures/descriptive-statistics/density.html) | [Density](../measures/descriptive-statistics/density.html#density) | ≠ checked, differs by convention | `gden` |
| Descriptive statistics | Density and degree distribution | [Structure statistics](../measures/descriptive-statistics/structure_statistics.html) | [Structure statistics](../measures/descriptive-statistics/structure_statistics.html#cat_statistics_structure) | · reported in docs | `structure.statistics` |
| Descriptive statistics | Efficiency, compactness and hierarchy | [Krackhardt graph-theoretic dimensions](../measures/descriptive-statistics/krackhardt_dimensions.html) | [Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)](../measures/descriptive-statistics/krackhardt_dimensions.html#krackhardt_dimensions) | · reported in docs | `connectedness; lubness` |
| Descriptive statistics | Reciprocity, dyad and triad census | [Dyad census](../measures/descriptive-statistics/dyad_census.html) | [Dyad census (mutual, asymmetric, null)](../measures/descriptive-statistics/dyad_census.html#dyad_census) | · reported in docs | `dyad.census` |
| Descriptive statistics | Reciprocity, dyad and triad census | [Reciprocity](../measures/descriptive-statistics/reciprocity.html) | [Reciprocity](../measures/descriptive-statistics/reciprocity.html#reciprocity) | ≠ checked, differs by convention | `grecip; mutuality` |
| Descriptive statistics | Reciprocity, dyad and triad census | [Triad census](../measures/descriptive-statistics/triad_census.html) | [Triad census](../measures/descriptive-statistics/triad_census.html#triad_census) | ≠ checked, differs by convention | `triad.census; triad.classify` |
| Ego networks | Ego measures | [Ego network members](../measures/ego-networks/ego_members.html) | [Ego members](../measures/ego-networks/ego_members.html#ego_members) | · reported in docs | `ego.extract` |
| Generators and rewiring | Classic random graphs | [G(n, m) random graph](../measures/generators-and-rewiring/gnm_random_graph.html) | [G(n, m) random graph](../measures/generators-and-rewiring/gnm_random_graph.html#gen_gnm) | · reported in docs | `rgnm` |
| Generators and rewiring | Classic random graphs | [G(n, p) random graph](../measures/generators-and-rewiring/gnp_random_graph.html) | [G(n, p) random graph](../measures/generators-and-rewiring/gnp_random_graph.html#gen_gnp) | · reported in docs | `rgraph` |
| Generators and rewiring | Classic random graphs | [Random graph with mixing (rgnmix)](../measures/generators-and-rewiring/mixing_model_generator.html) | [Rgnmix](../measures/generators-and-rewiring/mixing_model_generator.html#cat_rgnmix) | · reported in docs | `rgnmix` |
| Generators and rewiring | Classic random graphs | [Random graph with uniform MAN distribution](../measures/generators-and-rewiring/uman_random_graph.html) | [Rguman](../measures/generators-and-rewiring/uman_random_graph.html#cat_rguman) | · reported in docs | `rguman` |
| Generators and rewiring | Rewiring and randomization | [Edge swap and contract](../measures/generators-and-rewiring/swap_contract.html) | [Swap contract](../measures/generators-and-rewiring/swap_contract.html#swap_contract) | · reported in docs | `rewire.ud` |
| Generators and rewiring | Small-world, lattice and geometric models | [Interval graph](../measures/generators-and-rewiring/interval_graph.html) | [Interval graph](../measures/generators-and-rewiring/interval_graph.html#cat_interval) | · reported in docs | `interval.graph` |
| Generators and rewiring | Small-world, lattice and geometric models | [Small-world generator](../measures/generators-and-rewiring/small_world_generator.html) | [Small-world generator](../measures/generators-and-rewiring/small_world_generator.html#gen_small_world) | · reported in docs | `rewire.ws; rgws` |
| Graph theory and combinatorics | Cycles | [Cycle census and count](../measures/graph-theory-and-combinatorics/cycle_census.html) | [Kcycle census](../measures/graph-theory-and-combinatorics/cycle_census.html#cat_census_kcycle) | · reported in docs | `kcycle.census` |
| Graph theory and combinatorics | Degree sequences and predicates | [Isolates](../measures/graph-theory-and-combinatorics/isolates.html) | [Isolates](../measures/graph-theory-and-combinatorics/isolates.html#gb_isolates) | · reported in docs | `isolates` |
| Graph theory and combinatorics | Distances between graphs | [Distances between graphs (Hamming, structural)](../measures/graph-theory-and-combinatorics/graph_distance.html) | [Hdist](../measures/graph-theory-and-combinatorics/graph_distance.html#cat_hdist) | · reported in docs | `hdist` |
| Graph theory and combinatorics | Distances between graphs | [Distances between graphs (Hamming, structural)](../measures/graph-theory-and-combinatorics/graph_distance.html) | [Sdmat](../measures/graph-theory-and-combinatorics/graph_distance.html#cat_sdmat) | · reported in docs | `sdmat` |
| Graph theory and combinatorics | Distances between graphs | [Distances between graphs (Hamming, structural)](../measures/graph-theory-and-combinatorics/graph_distance.html) | [Structdist](../measures/graph-theory-and-combinatorics/graph_distance.html#cat_structdist) | · reported in docs | `structdist` |
| Inference (QAP, null models) | QAP and permutation tests | [Conditional uniform graph tests and null models](../measures/inference-qap-null-models/cug_null_models.html) | [Conditional uniform graph tests and null models](../measures/inference-qap-null-models/cug_null_models.html#cug_null_models) | · reported in docs | `cug.test; cugtest` |
| Inference (QAP, null models) | QAP and permutation tests | [Logistic MR-QAP](../measures/inference-qap-null-models/logistic_qap.html) | [Logistic MR-QAP](../measures/inference-qap-null-models/logistic_qap.html#lr_qap) | · reported in docs | `netlogit` |
| Inference (QAP, null models) | QAP and permutation tests | [MR-QAP regression](../measures/inference-qap-null-models/qap_regression.html) | [MR-QAP regression (Y-permutation, double semi-partialling)](../measures/inference-qap-null-models/qap_regression.html#qap_regression) | · reported in docs | `netlm` |
| Inference (QAP, null models) | QAP and permutation tests | [Network autocorrelation](../measures/inference-qap-null-models/network_autocorrelation.html) | [Network autocorrelation: lag/error model, Moran, Geary](../measures/inference-qap-null-models/network_autocorrelation.html#network_autocorrelation) | · reported in docs | `lnam; nacf` |
| Inference (QAP, null models) | QAP and permutation tests | [QAP correlation](../measures/inference-qap-null-models/qap_correlation.html) | [QAP correlation (Y-permutation, exact and Monte Carlo)](../measures/inference-qap-null-models/qap_correlation.html#qap_correlation) | · reported in docs | `gcor; gcov; gscor; gscov; qaptest` |
| Paths and distances | Efficiency and reachability | [Global and local efficiency](../measures/paths-and-distances/global_efficiency.html) | [Global and local efficiency](../measures/paths-and-distances/global_efficiency.html#efficiency_global) | · reported in docs | `efficiency` |
| Paths and distances | Path enumeration and counting | [K-path census](../measures/paths-and-distances/path_census.html) | [Kpath census](../measures/paths-and-distances/path_census.html#cat_census_kpath) | · reported in docs | `kpath.census` |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | ✓ checked, agrees | `geodist` |
| Roles and positions | Blockmodels | [Block density](../measures/roles-and-positions/block_density.html) | [Block density](../measures/roles-and-positions/block_density.html#block_density) | ✓ checked, agrees | `blockmodel` |
| Roles and positions | Equivalence and clustering | [Equivalence clustering](../measures/roles-and-positions/equivalence_clustering.html) | [Equiv clust](../measures/roles-and-positions/equivalence_clustering.html#cat_clust_equiv) | · reported in docs | `equiv.clust` |
| Roles and positions | Equivalence and clustering | [Regular equivalence (REGE, CATREGE)](../measures/roles-and-positions/regular_equivalence.html) | [Regular equivalence](../measures/roles-and-positions/regular_equivalence.html#regular_equivalence) | ✓ checked, agrees | `redist` |
| Roles and positions | Equivalence and clustering | [Structural equivalence](../measures/roles-and-positions/structural_equivalence.html) | [Structural equivalence](../measures/roles-and-positions/structural_equivalence.html#structural_equivalence) | ✓ checked, agrees | `sedist` |
| Roles and positions | Scaling and clustering | [Cognitive social structures with accuracy](../measures/roles-and-positions/css_accuracy.html) | [Cognitive social structures with accuracy measures](../measures/roles-and-positions/css_accuracy.html#css_accuracy) | · reported in docs | `consensus` |
| Roles and positions | Structural holes and brokerage | [Brokerage](../measures/roles-and-positions/brokerage.html) | [Brokerage](../measures/roles-and-positions/brokerage.html#brokerage) | ✓ checked, agrees | `brokerage` |
| Roles and positions | Structural holes and brokerage | [Hierarchy](../measures/roles-and-positions/hierarchy_krackhardt.html) | [Hierarchy](../measures/roles-and-positions/hierarchy_krackhardt.html#hierarchy) | · reported in docs | `hierarchy` |
| Statistical fitting | Model fitting | [Bayesian network accuracy model (BBNAM)](../measures/statistical-fitting/bbnam.html) | [Bbnam](../measures/statistical-fitting/bbnam.html#cat_bbnam) | · reported in docs | `bbnam` |
| Statistical fitting | Model fitting | [Bayesian network accuracy model (BBNAM)](../measures/statistical-fitting/bbnam.html) | [Bbnam bf](../measures/statistical-fitting/bbnam.html#cat_bbnam_bf) | · reported in docs | `bbnam.bf` |
| Statistical fitting | Model fitting | [Biased net models](../measures/statistical-fitting/biased_net_model.html) | [Bn](../measures/statistical-fitting/biased_net_model.html#cat_bn) | · reported in docs | `bn` |
| Statistical fitting | Model fitting | [Biased net models](../measures/statistical-fitting/biased_net_model.html) | [Rgbn](../measures/statistical-fitting/biased_net_model.html#cat_rgbn) | · reported in docs | `rgbn` |
| Statistical fitting | Model fitting | [Network canonical correlation](../measures/statistical-fitting/canonical_correlation.html) | [Netcancor](../measures/statistical-fitting/canonical_correlation.html#cat_netcancor) | · reported in docs | `netcancor` |
| Statistical fitting | Model fitting | [p-star models](../measures/statistical-fitting/pstar.html) | [Pstar](../measures/statistical-fitting/pstar.html#cat_pstar) | · reported in docs | `pstar` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F041](../findings.html#f041) | defect | Information centrality fails on singular inputs |
| [F042](../findings.html#f042) | convention | Degree reads an adjacency matrix: parallel edges collapse and the diagonal is ignored by default |
| [F043](../findings.html#f043) | convention | Closeness and centralization normalizations differ from other tools |
| [F044](../findings.html#f044) | convention | Reciprocity correlation is 0 on a single arc |
{% endraw %}
