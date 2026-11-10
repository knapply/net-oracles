---
title: Capability matrix
layout: default
nav_order: 2
---

{% raw %}
# Capability matrix

✓ checked, agrees; ≠ checked, differs by a documented convention; ✗ checked, defect found; ∅ checked, no value on the compared inputs; · reported in the tool's documentation (not run); blank: not known to implement it.

Columns are tool identifiers (see [Tools](tools/)). Rows are measures, grouped by family, subfamily and concept; the concept name links to its page and each variant links to its section.

## Centrality

142 measures in 76 concepts.

### Betweenness, load and flow

20 measures in 11 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | rsiena | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | bct | bctpy | gephi | ucinet | tnet | netrankr | centiserve |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Betweenness](measures/centrality/betweenness.html) | [Betweenness](measures/centrality/betweenness.html#betweenness) | ≠ | ≠ | ✓ | ≠ | · | · | ∅ | ✓ | · | ≠ | ≠ | ≠ | ≠ | ≠ | · | ✓ | ≠ |  |
|  | [Approximate betweenness (sampling)](measures/centrality/betweenness.html#betweenness_approx) |  |  |  |  |  |  | · |  |  | · | · |  |  |  |  |  |  |  |
|  | [Betweenness simple](measures/centrality/betweenness.html#betweenness_simple) | ✓ |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Betweenness subset](measures/centrality/betweenness.html#cx_betweenness_subset) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Twomode / betweenness](measures/centrality/betweenness.html#twomode-betweenness) | ∅ | ∅ |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Communicability betweenness](measures/centrality/communicability_betweenness.html) | [Communicability betweenness](measures/centrality/communicability_betweenness.html#cx_communicability_betweenness) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |
| [Current-flow betweenness](measures/centrality/current_flow_betweenness.html) | [Current flow approx](measures/centrality/current_flow_betweenness.html#cx_current_flow_approx) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Current flow subset](measures/centrality/current_flow_betweenness.html#cx_current_flow_subset) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Cx current flow](measures/centrality/current_flow_betweenness.html#cx_current_flow) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |
| [Edge betweenness](measures/centrality/edge_betweenness.html) | [Edge betweenness](measures/centrality/edge_betweenness.html#edge_betweenness) | ≠ | ✓ | · |  |  |  | ✓ | ✓ |  | · |  | · |  |  | · |  |  |  |
| [Edge load centrality](measures/centrality/edge_load_centrality.html) | [Edge load](measures/centrality/edge_load_centrality.html#cx_edge_load) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Flow betweenness](measures/centrality/flow_betweenness.html) | [Flow betweenness](measures/centrality/flow_betweenness.html#flow_betweenness) |  |  |  | ≠ |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Group betweenness centrality](measures/centrality/group_betweenness.html) | [Group / betweenness](measures/centrality/group_betweenness.html#group-betweenness) | ≠ |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [K-path centrality](measures/centrality/k_path_centrality.html) | [Geokpath](measures/centrality/k_path_centrality.html#cat_geokpath) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
|  | [KPath Centrality](measures/centrality/k_path_centrality.html#cat_k_path) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Load centrality](measures/centrality/load_centrality.html) | [Load](measures/centrality/load_centrality.html#cx_load) | ✓ |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Loadcent](measures/centrality/load_centrality.html#cat_loadcent) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Percolation centrality](measures/centrality/percolation_centrality.html) | [Percolation](measures/centrality/percolation_centrality.html#cx_percolation) | ✓ |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Stress centrality](measures/centrality/stress_centrality.html) | [Stresscent](measures/centrality/stress_centrality.html#cat_stresscent) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Subgraph centrality and stress centrality](measures/centrality/stress_centrality.html#subgraph_stress_centrality) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Centralization and tables

7 measures in 2 concepts.

| Concept | Variant | igraph | sna | ucinet |
|---|---|---|---|---|
| [Centrality table (raw and normalized)](measures/centrality/centrality_table.html) | [Net\_centrality\_table() (raw and normalised columns)](measures/centrality/centrality_table.html#centrality_table) |  |  | · |
| [Centralization](measures/centrality/centralization.html) | [Centralization](measures/centrality/centralization.html#cat_centralization) |  |  | · |
|  | [Centralization / betweenness](measures/centrality/centralization.html#centralization-betweenness) | ✓ | ≠ | · |
|  | [Centralization / closeness](measures/centrality/centralization.html#centralization-closeness) | ✓ | ✓ | · |
|  | [Centralization / degree](measures/centrality/centralization.html#centralization-degree) | ∅ | ✓ | · |
|  | [Centralization eigenvector](measures/centrality/centralization.html#centralization_eigenvector) | ≠ |  | · |
|  | [Theoretical maximum of centralization](measures/centrality/centralization.html#centralization_tmax) | · |  |  |

### Degree and strength

7 measures in 4 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | ergm | networkit | rustworkx | boost | bct | gephi | ucinet | tnet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Alpha-tuned degree and closeness](measures/centrality/weighted_degree_alpha.html) | [Opsahl alpha-tuned degree and closeness](measures/centrality/weighted_degree_alpha.html#opsahl_alpha) |  |  |  |  |  |  |  |  |  |  |  | · |
| [Degree](measures/centrality/degree.html) | [Degree](measures/centrality/degree.html#degree) | ✓ | ∅ | ✓ | ≠ | · | ✓ | · | · | ≠ | ✓ | · | · |
|  | [Degree simple](measures/centrality/degree.html#degree_simple) |  |  |  | ✓ |  |  |  |  |  |  |  |  |
|  | [Twomode / degree](measures/centrality/degree.html#twomode-degree) | ∅ | ∅ |  |  |  |  |  |  |  |  | · |  |
| [Group degree centrality](measures/centrality/group_degree.html) | [Group / degree](measures/centrality/group_degree.html#group-degree) | ✓ |  |  |  |  | ✓ | · |  |  |  |  |  |
|  | [Group out degree centrality](measures/centrality/group_degree.html#cat_degree_group_out) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Strength (weighted degree)](measures/centrality/strength.html) | [Strength](measures/centrality/strength.html#strength) | ✓ | ∅ | ✓ |  |  | ∅ |  |  |  | ✓ | · | ✓ |

### Distance-based

21 measures in 10 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | gephi | ucinet | tnet | netrankr | keyplayer | centiserve |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Average distance centrality](measures/centrality/average_distance_centrality.html) | [Averagedis](measures/centrality/average_distance_centrality.html#cat_averagedis) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
|  | [Pairwisedis](measures/centrality/average_distance_centrality.html#cat_pairwisedis) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Bottleneck centrality](measures/centrality/bottleneck_centrality.html) | [Bottleneck](measures/centrality/bottleneck_centrality.html#cat_bottleneck) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Centroid centrality](measures/centrality/centroid_centrality.html) | [Centroid](measures/centrality/centroid_centrality.html#cat_centroid) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Closeness](measures/centrality/closeness.html) | [Closeness](measures/centrality/closeness.html#closeness) | ✓ | ✓ | ✓ | ✓ | · | ✓ | ✓ | ≠ | ≠ | ≠ | ≠ | · | · | ≠ |  | · |
|  | [Approximate, top-k and group closeness](measures/centrality/closeness.html#closeness_approx) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
|  | [Closeness latora](measures/centrality/closeness.html#cat_closeness_latora) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
|  | [Closeness residual](measures/centrality/closeness.html#cat_closeness_residual) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
|  | [Incremental closeness centrality](measures/centrality/closeness.html#cat_closeness_incremental) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Newman weighted closeness centrality](measures/centrality/closeness.html#cat_closeness_newman_weighted) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
|  | [Swan closeness](measures/centrality/closeness.html#cat_closeness_swan) |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
|  | [Twomode / closeness](measures/centrality/closeness.html#twomode-closeness) | ≠ | ∅ |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Decay centrality](measures/centrality/decay_centrality.html) | [Decay](measures/centrality/decay_centrality.html#cat_decay) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Graph centrality (inverse eccentricity)](measures/centrality/graph_centrality.html) | [Graphcent](measures/centrality/graph_centrality.html#cat_graphcent) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Group closeness centrality](measures/centrality/group_closeness.html) | [Group / closeness](measures/centrality/group_closeness.html#group-closeness) | ✓ |  |  |  |  | ✓ | · |  |  |  |  |  |  |  |  |  |
| [Harmonic centrality](measures/centrality/harmonic_centrality.html) | [Harmonic](measures/centrality/harmonic_centrality.html#harmonic) | ✓ | ✓ | ✓ | ≠ |  | ✓ |  |  | ✓ |  | ≠ | · |  | ✓ |  | ✓ |
| [Radiality and integration](measures/centrality/radiality.html) | [Radiality](measures/centrality/radiality.html#cat_radiality) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
|  | [Valente-Foreman integration and radiality](measures/centrality/radiality.html#valente_foreman) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Reach and m-reach](measures/centrality/reach_centrality.html) | [Mreach closeness](measures/centrality/reach_centrality.html#cat_closeness_mreach) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
|  | [Mreach degree](measures/centrality/reach_centrality.html#cat_degree_mreach) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
|  | [Reach](measures/centrality/reach_centrality.html#reach) | ✓ | ✓ |  | · |  |  | · |  |  |  |  | · |  |  |  |  |

### Group centrality

1 measures in 1 concepts.

| Concept | Variant | networkx |
|---|---|---|
| [Prominent group](measures/centrality/group_prominence.html) | [Prominent group](measures/centrality/group_prominence.html#nxo_prominent) | ✓ |

### Key players

9 measures in 2 concepts.

| Concept | Variant | ucinet | keyplayer |
|---|---|---|---|
| [Key player set (KPP)](measures/centrality/key_player_set.html) | [Kpp\_optimum / distance\_fragmentation](measures/centrality/key_player_set.html#kpp_optimum-distance_fragmentation) |  | ✓ |
|  | [Kpp\_optimum / distance\_reach](measures/centrality/key_player_set.html#kpp_optimum-distance_reach) |  | ✓ |
|  | [Kpp\_optimum / fragmentation](measures/centrality/key_player_set.html#kpp_optimum-fragmentation) | · |  |
|  | [Kpp\_optimum / m\_reach](measures/centrality/key_player_set.html#kpp_optimum-m_reach) |  | ✓ |
|  | [Kpset](measures/centrality/key_player_set.html#cat_kpset) |  | · |
| [Key player single-node scores (KPP)](measures/centrality/key_player_single.html) | [Kpp\_single / distance\_fragmentation](measures/centrality/key_player_single.html#kpp_single-distance_fragmentation) |  | ≠ |
|  | [Kpp\_single / distance\_reach](measures/centrality/key_player_single.html#kpp_single-distance_reach) |  | ≠ |
|  | [Kpp\_single / fragmentation](measures/centrality/key_player_single.html#kpp_single-fragmentation) | · |  |
|  | [Kpp\_single / m\_reach](measures/centrality/key_player_single.html#kpp_single-m_reach) |  | ✓ |

### Local and structural scores

28 measures in 25 concepts.

| Concept | Variant | networkx | pyigraph | sna | networkit | sknetwork | bct | ucinet | keyplayer | centiserve |
|---|---|---|---|---|---|---|---|---|---|---|
| [Alpha centrality](measures/centrality/alpha_centrality.html) | [Alpha](measures/centrality/alpha_centrality.html#cat_alpha) |  | · |  |  |  |  |  |  |  |
| [Bridging centrality](measures/centrality/bridging_centrality.html) | [Bridging centrality](measures/centrality/bridging_centrality.html#bridging_centrality) |  |  |  |  |  |  | · |  |  |
| [Bridging coefficient](measures/centrality/bridging_coefficient.html) | [Bridging coefficient](measures/centrality/bridging_coefficient.html#bridging_coefficient) |  |  |  |  |  |  | · |  |  |
| [Community-based centrality](measures/centrality/community_centrality.html) | [Communitycent](measures/centrality/community_centrality.html#cat_communitycent) |  |  |  |  |  |  |  |  | · |
| [Concentration](measures/centrality/concentration.html) | [Concent](measures/centrality/concentration.html#cat_concent) |  |  |  |  |  |  | · |  |  |
| [Cross-clique centrality](measures/centrality/cross_clique_centrality.html) | [Crossclique](measures/centrality/cross_clique_centrality.html#cat_crossclique) |  |  |  |  |  |  |  |  | · |
| [Diffusion centrality and diffusion degree](measures/centrality/diffusion_centrality.html) | [Diffusion](measures/centrality/diffusion_centrality.html#cat_diffusion) |  |  |  |  | · |  |  | · |  |
|  | [Diffusion degree](measures/centrality/diffusion_centrality.html#cat_degree_diffusion) |  |  |  |  |  |  |  |  | · |
|  | [Diffusion efficiency](measures/centrality/diffusion_centrality.html#cat_diffusion_efficiency) |  |  |  |  |  | · |  |  |  |
| [Dispersion](measures/centrality/dispersion.html) | [Dispersion](measures/centrality/dispersion.html#cx_dispersion) | ≠ |  |  |  |  |  |  |  |  |
| [Edge percolated component](measures/centrality/epc.html) | [Epc](measures/centrality/epc.html#cat_epc) |  |  |  |  |  |  |  |  | · |
| [Entropy centrality](measures/centrality/entropy_centrality.html) | [Entropy](measures/centrality/entropy_centrality.html#cat_entropy) |  |  |  |  |  |  |  |  | · |
| [Gil-Schmidt power index](measures/centrality/gil_schmidt_power.html) | [Gilschmidt](measures/centrality/gil_schmidt_power.html#cat_gilschmidt) |  |  | · |  |  |  |  |  |  |
| [Induced centrality](measures/centrality/induced_centrality.html) | [Induced centrality](measures/centrality/induced_centrality.html#induced_centrality) |  |  |  |  |  |  | · |  |  |
| [Laplacian centrality](measures/centrality/laplacian_centrality.html) | [Cx laplacian](measures/centrality/laplacian_centrality.html#cx_laplacian) | ✓ |  |  | ✓ |  |  |  |  |  |
| [Leverage centrality](measures/centrality/leverage_centrality.html) | [Leverage](measures/centrality/leverage_centrality.html#cat_leverage) |  |  |  |  |  |  |  |  | · |
| [Lin centrality](measures/centrality/lin_centrality.html) | [Lincent](measures/centrality/lin_centrality.html#cat_lincent) |  |  |  |  |  |  |  |  | · |
| [Lobby index](measures/centrality/lobby_index.html) | [Lobby](measures/centrality/lobby_index.html#cat_lobby) |  |  |  |  |  |  |  |  | · |
| [Local reaching centrality](measures/centrality/local_reaching_centrality.html) | [Reaching](measures/centrality/local_reaching_centrality.html#cx_reaching) | ≠ |  |  |  |  |  |  |  |  |
| [MNC and DMNC](measures/centrality/mnc_dmnc.html) | [Dmnc](measures/centrality/mnc_dmnc.html#cat_dmnc) |  |  |  |  |  |  |  |  | · |
|  | [Mnc](measures/centrality/mnc_dmnc.html#cat_mnc) |  |  |  |  |  |  |  |  | · |
| [Permanence](measures/centrality/permanence.html) | [Permanence Centrality](measures/centrality/permanence.html#cat_permanence) |  |  |  | · |  |  |  |  |  |
| [Prestige](measures/centrality/prestige.html) | [Prestige](measures/centrality/prestige.html#cat_prestige) |  |  | · |  |  |  |  |  |  |
| [Second-order centrality](measures/centrality/second_order_centrality.html) | [Second order](measures/centrality/second_order_centrality.html#cx_second_order) | ✓ |  |  |  |  |  |  |  |  |
| [Semi-local centrality](measures/centrality/semilocal_centrality.html) | [Semilocal](measures/centrality/semilocal_centrality.html#cat_semilocal) |  |  |  |  |  |  |  |  | · |
| [Topological coefficient](measures/centrality/topological_coefficient.html) | [Topocoefficient](measures/centrality/topological_coefficient.html#cat_topocoefficient) |  |  |  |  |  |  |  |  | · |
| [Trophic levels and incoherence](measures/centrality/trophic_levels.html) | [Trophic](measures/centrality/trophic_levels.html#cx_trophic) | ✓ |  |  |  |  |  |  |  |  |
| [VoteRank](measures/centrality/voterank.html) | [Voterank](measures/centrality/voterank.html#cx_voterank) | ✓ |  |  |  |  |  |  |  |  |

### Partial rankings (netrankr)

16 measures in 6 concepts.

| Concept | Variant | netrankr |
|---|---|---|
| [Hyperbolic index](measures/centrality/hyperbolic_index.html) | [Hyperbolic index](measures/centrality/hyperbolic_index.html#cat_hyperbolic) | · |
| [Neighborhood inclusion](measures/centrality/neighborhood_inclusion.html) | [Neighborhood inclusion](measures/centrality/neighborhood_inclusion.html#cat_inclusion_neighborhood) | · |
|  | [Neighborhood inclusion, positional dominance, rank intervals](measures/centrality/neighborhood_inclusion.html#partial_ranking) | · |
| [Positional dominance](measures/centrality/positional_dominance.html) | [Positional dominance](measures/centrality/positional_dominance.html#cat_dominance_positional) | · |
| [Rank comparison and ordering](measures/centrality/rank_comparison.html) | [Comparable pairs](measures/centrality/rank_comparison.html#cat_comparable_pairs) | · |
|  | [Compare ranks](measures/centrality/rank_comparison.html#cat_compare_ranks) | · |
|  | [Get rankings](measures/centrality/rank_comparison.html#cat_rankings) | · |
|  | [Incomparable pairs](measures/centrality/rank_comparison.html#cat_incomparable_pairs) | · |
|  | [Index builder](measures/centrality/rank_comparison.html#cat_builder) | · |
|  | [Is preserved](measures/centrality/rank_comparison.html#cat_is_preserved) | · |
|  | [Majorization gap](measures/centrality/rank_comparison.html#cat_gap_majorization) | · |
| [Rank intervals](measures/centrality/rank_intervals.html) | [Rank intervals](measures/centrality/rank_intervals.html#cat_intervals_rank) | · |
| [Rank probabilities and expected ranks](measures/centrality/rank_probabilities.html) | [Approx rank expected](measures/centrality/rank_probabilities.html#cat_approx_expected_rank) | · |
|  | [Approx rank relative](measures/centrality/rank_probabilities.html#cat_approx_rank_relative) | · |
|  | [Exact rank prob](measures/centrality/rank_probabilities.html#cat_exact_prob_rank) | · |
|  | [Mcmc rank prob](measures/centrality/rank_probabilities.html#cat_mcmc_prob_rank) | · |

### Resistance and information

2 measures in 1 concepts.

| Concept | Variant | networkx | sna | ucinet | netrankr | centiserve |
|---|---|---|---|---|---|---|
| [Information centrality (current-flow closeness)](measures/centrality/information_centrality.html) | [Information centrality](measures/centrality/information_centrality.html#information_centrality) | ✓ | ≠ | · | ✓ |  |
|  | [Current flow closeness](measures/centrality/information_centrality.html#cx_current_flow_closeness) | ✓ |  |  | ✓ | · |

### Spectral and walk-based

20 measures in 12 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | graphblas | bct | gephi | ucinet | netrankr | centiserve |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Bonacich power centrality](measures/centrality/bonacich_power.html) | [Bonacich](measures/centrality/bonacich_power.html#bonacich) |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  | · |  |  |
| [ClusterRank](measures/centrality/clusterrank.html) | [Clusterrank](measures/centrality/clusterrank.html#cat_clusterrank) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Communicability](measures/centrality/communicability.html) | [Communicability](measures/centrality/communicability.html#cx_communicability) | ✓ | · |  |  |  |  |  |  |  |  |  | · |  |  | ≠ |  |
| [EigenTrust](measures/centrality/eigentrust.html) | [Eigentrust](measures/centrality/eigentrust.html#cat_eigentrust) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Eigenvector centrality](measures/centrality/eigenvector_centrality.html) | [Eigenvector](measures/centrality/eigenvector_centrality.html#eigenvector) | ∅ | ∅ | ≠ | ≠ | · | · | ✓ |  | · |  | ≠ | · | ≠ | · |  |  |
|  | [Nxp eigenvector](measures/centrality/eigenvector_centrality.html#nxp_eigenvector) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Twomode / eigenvector](measures/centrality/eigenvector_centrality.html#twomode-eigenvector) |  | ✓ |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [HITS hubs and authorities](measures/centrality/hits.html) | [Hits](measures/centrality/hits.html#hits) | ✓ | ∅ | ≠ |  | · |  | ∅ | ≠ |  |  | ≠ |  | ≠ | · |  |  |
|  | [Nxp hits](measures/centrality/hits.html#nxp_hits) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hubbell centrality](measures/centrality/hubbell_centrality.html) | [Hubbell](measures/centrality/hubbell_centrality.html#cat_hubbell) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Katz centrality](measures/centrality/katz_centrality.html) | [Katz](measures/centrality/katz_centrality.html#katz) | ✓ | ∅ |  |  | · | · | ∅ | · | · |  | ≠ |  |  | · |  | ✓ |
|  | [Nxp katz](measures/centrality/katz_centrality.html#nxp_katz) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [LeaderRank](measures/centrality/leaderrank.html) | [Leaderrank](measures/centrality/leaderrank.html#cat_leaderrank) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Markov centrality](measures/centrality/markov_centrality.html) | [Markovcent](measures/centrality/markov_centrality.html#cat_markovcent) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [PageRank](measures/centrality/pagerank.html) | [Pagerank](measures/centrality/pagerank.html#pagerank) | ≠ | ∅ | ✓ |  | · | ∅ | ≠ | ≠ | ✓ | · | ≠ |  | ✗ | · |  |  |
|  | [Google](measures/centrality/pagerank.html#nxp_google) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Local and approximate PageRank](measures/centrality/pagerank.html#local_pagerank) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
|  | [Nxp pagerank](measures/centrality/pagerank.html#nxp_pagerank) | ✓ |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
|  | [Walks ppr](measures/centrality/pagerank.html#walks_ppr) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [SALSA](measures/centrality/salsa.html) | [Salsa](measures/centrality/salsa.html#cat_salsa) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |

### Walk-based and distance-based indices (netrankr)

11 measures in 2 concepts.

| Concept | Variant | netrankr |
|---|---|---|
| [Distance transformations for indices](measures/centrality/distance_transform_indices.html) | [Dist 2pow](measures/centrality/distance_transform_indices.html#cat_2pow_dist) | · |
|  | [Dist dpow](measures/centrality/distance_transform_indices.html#cat_dist_dpow) | · |
|  | [Dist inv](measures/centrality/distance_transform_indices.html#cat_dist_inv) | · |
|  | [Dist powd](measures/centrality/distance_transform_indices.html#cat_dist_powd) | · |
|  | [Swan combinatory](measures/centrality/distance_transform_indices.html#cat_combinatory_swan) | · |
| [Walk-based index components](measures/centrality/walk_indices.html) | [Walks attenuated](measures/centrality/walk_indices.html#cat_attenuated_walk) | · |
|  | [Walks exp](measures/centrality/walk_indices.html#cat_exp_walk) | · |
|  | [Walks exp even](measures/centrality/walk_indices.html#cat_even_exp_walk) | · |
|  | [Walks exp odd](measures/centrality/walk_indices.html#cat_exp_odd_walk) | · |
|  | [Walks limit prop](measures/centrality/walk_indices.html#cat_limit_prop_walk) | · |
|  | [Walks uptok](measures/centrality/walk_indices.html#cat_uptok_walk) | · |

## Cohesion and subgroups

41 measures in 29 concepts.

### Cliques

16 measures in 11 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | sknetwork | jgrapht | boost | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [All cliques (not only maximal)](measures/cohesion-and-subgroups/all_cliques.html) | [All cliques](measures/cohesion-and-subgroups/all_cliques.html#all_cliques) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Nx cliques order](measures/cohesion-and-subgroups/all_cliques.html#nx_cliques_order) | ✓ |  |  |  |  |  |  |  |  |  |
| [Clique census](measures/cohesion-and-subgroups/clique_census.html) | [Clique census](measures/cohesion-and-subgroups/clique_census.html#cat_census_clique) |  |  |  | · |  |  |  |  |  |  |
| [Clique co-membership and overlap](measures/cohesion-and-subgroups/clique_overlap.html) | [Clique co-membership and overlap matrices](measures/cohesion-and-subgroups/clique_overlap.html#clique_overlap) |  |  |  |  |  |  |  |  |  | · |
| [Clique decomposition state](measures/cohesion-and-subgroups/clique_state.html) | [Clique State](measures/cohesion-and-subgroups/clique_state.html#cat_clique_state) |  |  |  |  | · |  |  |  |  |  |
| [Clique number](measures/cohesion-and-subgroups/clique_number.html) | [Clique number](measures/cohesion-and-subgroups/clique_number.html#clique_number) | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |  |
|  | [Node clique number](measures/cohesion-and-subgroups/clique_number.html#node_clique_number) | ✓ |  |  |  |  |  |  |  |  |  |
| [Clique test](measures/cohesion-and-subgroups/is_clique.html) | [Is clique](measures/cohesion-and-subgroups/is_clique.html#cat_clique_is) |  | · | · |  |  |  |  |  |  |  |
| [Maximal cliques](measures/cohesion-and-subgroups/maximal_cliques.html) | [Clique Detect](measures/cohesion-and-subgroups/maximal_cliques.html#cat_clique_detect) |  |  |  |  |  | · |  |  |  |  |
|  | [Max cliques](measures/cohesion-and-subgroups/maximal_cliques.html#max_cliques) | ✓ | ✓ | ✓ |  | · | ∅ | · | ✓ | · | · |
| [Maximum cohesion](measures/cohesion-and-subgroups/max_cohesion.html) | [Maxcohesion](measures/cohesion-and-subgroups/max_cohesion.html#cat_maxcohesion) |  | · |  |  |  |  |  |  |  |  |
| [Maximum-weight clique](measures/cohesion-and-subgroups/max_weight_clique.html) | [Max weight clique](measures/cohesion-and-subgroups/max_weight_clique.html#max_weight_clique) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Largest weighted cliques](measures/cohesion-and-subgroups/max_weight_clique.html#cat_clique_largest_weighted) |  | · |  |  |  |  |  |  |  |  |
|  | [Max weight clique nodes](measures/cohesion-and-subgroups/max_weight_clique.html#max_weight_clique_nodes) | ✓ |  |  |  |  |  |  |  |  |  |
| [Number of largest cliques](measures/cohesion-and-subgroups/largest_clique_count.html) | [Count max cliques](measures/cohesion-and-subgroups/largest_clique_count.html#cat_clique_count_max) |  | · |  |  |  |  |  |  |  |  |
| [Weighted cliques](measures/cohesion-and-subgroups/weighted_cliques.html) | [Weighted cliques](measures/cohesion-and-subgroups/weighted_cliques.html#cat_clique_weighted) |  | · |  |  |  |  |  |  |  |  |

### Cores, trusses and cohesive blocks

8 measures in 4 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | bct | bctpy | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Cohesive blocking (Moody-White)](measures/cohesion-and-subgroups/cohesive_blocking.html) | [Cohesive blocking (Moody-White)](measures/cohesion-and-subgroups/cohesive_blocking.html#cohesive_blocking) |  | · |  |  |  |  |  |  |  |  |  |  |  |
|  | [Cohesive blocks](measures/cohesion-and-subgroups/cohesive_blocking.html#cat_blocks_cohesive) |  | · | · |  |  |  |  |  |  |  |  |  |  |
| [K-core decomposition](measures/cohesion-and-subgroups/k_core.html) | [Core Decomposition Sequence](measures/cohesion-and-subgroups/k_core.html#cat_core_decomposition_sequence) |  |  |  |  |  | · |  |  |  |  |  |  |  |
|  | [Core subset](measures/cohesion-and-subgroups/k_core.html#core_subset) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Coreness](measures/cohesion-and-subgroups/k_core.html#coreness) | ≠ | ✓ | ✓ | · | · | ∅ | ≠ | ≠ | ✓ | · | ≠ | ≠ | · |
| [K-truss](measures/cohesion-and-subgroups/k_truss.html) | [K truss](measures/cohesion-and-subgroups/k_truss.html#k_truss) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Truss](measures/cohesion-and-subgroups/k_truss.html#truss) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Onion decomposition](measures/cohesion-and-subgroups/onion_decomposition.html) | [Onion](measures/cohesion-and-subgroups/onion_decomposition.html#onion) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |

### Relaxed cliques and subgroups

9 measures in 8 concepts.

| Concept | Variant | networkx | igraph | sna | ergm | networkit | ucinet |
|---|---|---|---|---|---|---|---|
| [Cut quality (conductance, expansion, boundary)](measures/cohesion-and-subgroups/cut_quality.html) | [Cut quality (conductance, expansion, boundary)](measures/cohesion-and-subgroups/cut_quality.html#cut_quality) | · |  |  |  | · |  |
| [Factions](measures/cohesion-and-subgroups/factions.html) | [Factions](measures/cohesion-and-subgroups/factions.html#cat_factions) |  |  |  |  |  | · |
|  | [Factions errors](measures/cohesion-and-subgroups/factions.html#factions_errors) |  |  |  |  |  | · |
| [K-plexes](measures/cohesion-and-subgroups/k_plexes.html) | [K plexes](measures/cohesion-and-subgroups/k_plexes.html#k_plexes) |  |  |  |  |  | · |
| [Lambda connectivity matrix](measures/cohesion-and-subgroups/lambda_connectivity.html) | [Lambda connectivity](measures/cohesion-and-subgroups/lambda_connectivity.html#lambda_connectivity) | ✓ | ✓ |  |  |  |  |
| [Lambda sets](measures/cohesion-and-subgroups/lambda_sets.html) | [Lambda sets](measures/cohesion-and-subgroups/lambda_sets.html#lambda_sets) | ✓ |  |  |  |  | · |
| [N-clans](measures/cohesion-and-subgroups/n_clans.html) | [N clans](measures/cohesion-and-subgroups/n_clans.html#n_clans) | ✓ |  |  |  |  | · |
| [N-cliques](measures/cohesion-and-subgroups/n_cliques.html) | [N cliques](measures/cohesion-and-subgroups/n_cliques.html#n_cliques) | ✓ |  |  |  |  | · |
| [Simmelian ties](measures/cohesion-and-subgroups/simmelian_ties.html) | [Simmelian ties](measures/cohesion-and-subgroups/simmelian_ties.html#simmelian) |  |  | · | · |  | · |

### Triads, motifs and local structure

8 measures in 6 concepts.

| Concept | Variant | networkx | igraph | pyigraph | rsiena | graphtool | bct | ucinet |
|---|---|---|---|---|---|---|---|---|
| [Cocitation and bibliographic coupling](measures/cohesion-and-subgroups/cocitation_coupling.html) | [Cocitation and bibliographic coupling](measures/cohesion-and-subgroups/cocitation_coupling.html#cocitation) |  | · | · |  |  |  |  |
| [Graphlets](measures/cohesion-and-subgroups/graphlets.html) | [Graphlet basis and projection](measures/cohesion-and-subgroups/graphlets.html#graphlets) |  | · |  |  |  |  |  |
| [Mixed triad census](measures/cohesion-and-subgroups/mixed_triad_census.html) | [Mixed Triad Census](measures/cohesion-and-subgroups/mixed_triad_census.html#cat_census_mixed_triad) |  |  |  | · |  |  |  |
| [Motif census](measures/cohesion-and-subgroups/motif_census.html) | [Motif census](measures/cohesion-and-subgroups/motif_census.html#motif_census) |  | · | · |  | · | · |  |
| [Triad enumeration](measures/cohesion-and-subgroups/triad_enumeration.html) | [All triads](measures/cohesion-and-subgroups/triad_enumeration.html#cat_all_triads) | · |  |  |  |  |  |  |
|  | [Liststriads](measures/cohesion-and-subgroups/triad_enumeration.html#cat_liststriads) |  |  |  |  |  |  | · |
| [Triad type classification](measures/cohesion-and-subgroups/triad_type.html) | [Triad type](measures/cohesion-and-subgroups/triad_type.html#cat_triad_type) | · |  |  |  |  |  |  |
|  | [Triads by type](measures/cohesion-and-subgroups/triad_type.html#cat_triads_type) | · |  |  |  |  |  |  |

## Communities

89 measures in 45 concepts.

### Graph bisection and partitioning

8 measures in 6 concepts.

| Concept | Variant | networkx | networkit | jgrapht |
|---|---|---|---|---|
| [Bipartite partitioning](measures/communities/bipartite_partitioning.html) | [Bipartite Partitioning](measures/communities/bipartite_partitioning.html#cat_bipartite_partitioning) |  |  | · |
| [Graph bisection](measures/communities/graph_bisection.html) | [Greedy node swap bipartition (community)](measures/communities/graph_bisection.html#cat_bipartition_greedy_swap-community) | · |  |  |
|  | [Kernighan lin](measures/communities/graph_bisection.html#cnx_kernighan_lin) | ✓ |  |  |
|  | [Spectral Partitioner](measures/communities/graph_bisection.html#cat_partitioner_spectral) |  | · |  |
| [Lukes tree partitioning](measures/communities/lukes_partitioning.html) | [Lukes](measures/communities/lukes_partitioning.html#cnx_lukes) | ✓ |  |  |
| [Partition counts](measures/communities/partition_counts.html) | [Partition counts](measures/communities/partition_counts.html#cnx_partition_counts) | ✓ |  |  |
| [Randomized partitioning](measures/communities/randomized_partitioning.html) | [Randomized partitioning (approximate)](measures/communities/randomized_partitioning.html#cat_partitioning_randomized-approximate) | · |  |  |
| [Spectral modularity bipartition](measures/communities/spectral_modularity_bipartition.html) | [Spectral modularity bipartition (community)](measures/communities/spectral_modularity_bipartition.html#cat_bipartition_modularity_spectral-community) | · |  |  |

### Modularity-based detection

14 measures in 2 concepts.

| Concept | Variant | networkx | igraph | pyigraph | networkit | sknetwork | jgrapht | bct | gephi | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|
| [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](measures/communities/modularity_maximization.html) | [Fast greedy](measures/communities/modularity_maximization.html#fast_greedy) | ∅ | ≠ | · |  |  |  |  |  | · |
|  | [Greedy modularity](measures/communities/modularity_maximization.html#cnx_greedy_modularity) | ✓ |  |  |  |  | · |  |  |  |
|  | [Leading eigen](measures/communities/modularity_maximization.html#leading_eigen) |  | ✓ | · |  |  |  |  |  | · |
|  | [Leiden](measures/communities/modularity_maximization.html#leiden) | ✓ | ∅ | · | · | · |  |  |  | · |
|  | [Leiden seeded](measures/communities/modularity_maximization.html#cnx_leiden_seeded) | ✓ |  |  |  |  |  |  |  |  |
|  | [Louvain Hierarchy](measures/communities/modularity_maximization.html#cat_hierarchy_louvain) |  |  |  |  | · |  |  |  |  |
|  | [Louvain Iteration](measures/communities/modularity_maximization.html#cat_iteration_louvain) |  |  |  |  | · |  |  |  |  |
|  | [Louvain modularity](measures/communities/modularity_maximization.html#louvain_modularity) | ≠ | · | · | · | · |  | · |  | · |
|  | [Louvain quality](measures/communities/modularity_maximization.html#louvain_quality) | ≠ | ≠ |  |  |  |  |  | ≠ |  |
|  | [Louvain seeded](measures/communities/modularity_maximization.html#cnx_louvain_seeded) | ✓ |  |  |  |  |  |  |  |  |
|  | [Naive greedy](measures/communities/modularity_maximization.html#cnx_naive_greedy) | ≠ |  |  |  |  |  |  |  |  |
|  | [Naive greedy nx](measures/communities/modularity_maximization.html#cnx_naive_greedy_nx) | ✓ |  |  |  |  |  |  |  |  |
|  | [Optimal modularity](measures/communities/modularity_maximization.html#optimal_modularity) |  | ✓ | · |  |  |  |  |  |  |
| [Spinglass](measures/communities/spinglass.html) | [Spinglass](measures/communities/spinglass.html#spinglass) |  | ✓ | · |  |  |  |  |  |  |

### Other detection algorithms

34 measures in 20 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | sknetwork | jgrapht | bct | ucinet | infomap |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Clique percolation communities](measures/communities/clique_percolation.html) | [Clique communities](measures/communities/clique_percolation.html#cat_clique_community) |  |  |  |  |  |  |  | · |  |  |
|  | [K clique](measures/communities/clique_percolation.html#cnx_k_clique) | ✓ |  |  |  |  |  |  |  |  |  |
| [Cluster mode state](measures/communities/cluster_mode_state.html) | [Mode Cluster State](measures/communities/cluster_mode_state.html#cat_cluster_mode_state) |  |  |  | · |  |  |  |  |  |  |
| [Combined SCD](measures/communities/scd_combined.html) | [Combined SCD](measures/communities/scd_combined.html#cat_combined_scd) |  |  |  |  | · |  |  |  |  |  |
| [Constant Potts model](measures/communities/constant_potts_model.html) | [Constant potts model (community)](measures/communities/constant_potts_model.html#cat_constant_model_potts-community) | · |  |  |  |  |  |  |  |  |  |
| [Cut clustering](measures/communities/cut_clustering.html) | [Cut Clustering](measures/communities/cut_clustering.html#cat_clustering_cut) |  |  |  |  | · |  |  |  |  |  |
| [Dasgupta cost and score](measures/communities/dasgupta_cost.html) | [Dasgupta cost](measures/communities/dasgupta_cost.html#cat_cost_dasgupta) |  |  |  |  |  | · |  |  |  |  |
|  | [Dasgupta score](measures/communities/dasgupta_cost.html#cat_dasgupta) |  |  |  |  |  | · |  |  |  |  |
| [Fluid communities](measures/communities/fluid_communities.html) | [Fluid communities](measures/communities/fluid_communities.html#fluid_communities) | ✓ | ✓ | · |  |  |  |  |  |  |  |
| [Girvan-Newman edge removal](measures/communities/girvan_newman.html) | [Girvan newman](measures/communities/girvan_newman.html#girvan_newman) | ✓ | ✓ | · |  |  |  | · |  | · |  |
|  | [Cnx current flow](measures/communities/girvan_newman.html#cnx_current_flow) | ≠ |  |  |  |  |  |  |  |  |  |
|  | [Cnx edge betweenness](measures/communities/girvan_newman.html#cnx_edge_betweenness) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Cnx girvan newman](measures/communities/girvan_newman.html#cnx_girvan_newman) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Girvan newman cut](measures/communities/girvan_newman.html#girvan_newman_cut) |  | ✓ |  |  |  |  |  |  |  |  |
| [Infomap](measures/communities/infomap.html) | [Infomap](measures/communities/infomap.html#infomap) |  | ∅ | · |  |  |  |  |  |  | ✓ |
| [K-core community detection](measures/communities/core_community_detection.html) | [K Core Community Detection](measures/communities/core_community_detection.html#cat_community_core_detection_k) |  |  |  |  | · |  |  |  |  |  |
| [K-spanning-tree clustering](measures/communities/k_spanning_tree_clustering.html) | [KSpanning Tree Clustering](measures/communities/k_spanning_tree_clustering.html#cat_clustering_k_spanning_tree) |  |  |  |  |  |  | · |  |  |  |
| [Label propagation](measures/communities/label_propagation.html) | [Label propagation](measures/communities/label_propagation.html#label_propagation) | ≠ | ∅ | · |  | · | · | · |  | · |  |
|  | [Cnx label propagation](measures/communities/label_propagation.html#cnx_label_propagation) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Seeded labels](measures/communities/label_propagation.html#cnx_seeded_labels) | ✓ |  |  |  |  |  |  |  |  |  |
| [Label spreading](measures/communities/label_spreading.html) | [Label spreading](measures/communities/label_spreading.html#nxo_label_spreading) | ✓ |  |  |  |  |  |  |  |  |  |
| [Link communities](measures/communities/link_communities.html) | [Link communities](measures/communities/link_communities.html#cat_community_link) |  |  |  |  |  |  |  | · |  |  |
| [LocalGreedy, MOCA and partition polishing](measures/communities/ucinet_community_extras.html) | [LocalGreedy, Moca, partition polishing, initial partitions](measures/communities/ucinet_community_extras.html#ucinet_community_extras) |  |  |  |  |  |  |  |  | · |  |
|  | [Polish](measures/communities/ucinet_community_extras.html#cat_polish) |  |  |  |  |  |  |  |  | · |  |
| [Overlapping communities](measures/communities/overlapping_communities.html) | [Overlapping](measures/communities/overlapping_communities.html#cnx_overlapping) | ✓ |  |  |  |  |  |  |  |  |  |
| [Overlapping seed expansion (LFM, GCE)](measures/communities/overlapping_seed_expansion.html) | [GCE](measures/communities/overlapping_seed_expansion.html#cat_gce) |  |  |  |  | · |  |  |  |  |  |
|  | [Greedy source expansion (community)](measures/communities/overlapping_seed_expansion.html#cat_expansion_greedy_source-community) | · |  |  |  |  |  |  |  |  |  |
|  | [LFM](measures/communities/overlapping_seed_expansion.html#cat_lfm) |  |  |  |  | · |  |  |  |  |  |
|  | [LFMLocal](measures/communities/overlapping_seed_expansion.html#cat_lfm_local) |  |  |  |  | · |  |  |  |  |  |
| [Paris hierarchical clustering](measures/communities/paris.html) | [Paris](measures/communities/paris.html#cat_paris) |  |  |  |  |  | · |  |  |  |  |
| [Voronoi communities](measures/communities/voronoi_communities.html) | [Community voronoi](measures/communities/voronoi_communities.html#cat_community_voronoi) |  |  | · |  |  |  |  |  |  |  |
|  | [Voronoi](measures/communities/voronoi_communities.html#voronoi) |  | ≠ |  |  |  |  |  |  |  |  |
|  | [Voronoi cells](measures/communities/voronoi_communities.html#cat_cells_voronoi) | · | · |  |  |  |  |  |  |  |  |
| [Walktrap](measures/communities/walktrap.html) | [Walktrap](measures/communities/walktrap.html#walktrap) |  | ≠ | · |  |  |  |  |  |  |  |

### Partition and cover quality

15 measures in 10 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | sknetwork | jgrapht | bct | gephi | cdlib | graspologic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Conductance](measures/communities/conductance.html) | [Isolated Interpartition Conductance](measures/communities/conductance.html#cat_conductance_interpartition_isolated) |  |  |  |  | · |  |  |  |  |  |  |
|  | [Set Conductance](measures/communities/conductance.html#cat_conductance_set) |  |  |  |  | · |  |  |  |  |  |  |
| [Expansion](measures/communities/expansion.html) | [Isolated Interpartition Expansion](measures/communities/expansion.html#cat_expansion_interpartition_isolated) |  |  |  |  | · |  |  |  |  |  |  |
| [Hub dominance](measures/communities/hub_dominance.html) | [Cover Hub Dominance](measures/communities/hub_dominance.html#cat_cover_dominance_hub) |  |  |  |  | · |  |  |  |  |  |  |
|  | [Hub Dominance](measures/communities/hub_dominance.html#cat_dominance_hub) |  |  |  |  | · |  |  |  |  |  |  |
|  | [Partition Hub Dominance](measures/communities/hub_dominance.html#cat_dominance_hub_partition) |  |  |  |  | · |  |  |  |  |  |  |
| [Intrapartition density](measures/communities/intrapartition_density.html) | [Intrapartition Density](measures/communities/intrapartition_density.html#cat_density_intrapartition) |  |  |  |  | · |  |  |  |  |  |  |
| [Local partition coverage](measures/communities/local_partition_coverage.html) | [Local Partition Coverage](measures/communities/local_partition_coverage.html#cat_coverage_local_partition) |  |  |  |  | · |  |  |  |  |  |  |
| [Local tightness expansion](measures/communities/local_tightness_expansion.html) | [Local Tightness Expansion](measures/communities/local_tightness_expansion.html#cat_expansion_local_tightness) |  |  |  |  | · |  |  |  |  |  |  |
| [Modularity](measures/communities/modularity.html) | [Modularity](measures/communities/modularity.html#modularity) | ≠ | ✓ | ✓ | · | ∅ | ≠ | · | · | · | ≠ | ≠ |
|  | [Modularity nx](measures/communities/modularity.html#cnx_modularity_nx) | ✓ |  |  |  |  |  |  |  |  |  |  |
|  | [Modularity State](measures/communities/modularity.html#cat_modularity_state) |  |  |  | · |  |  |  |  |  |  |  |
| [Partition entropy](measures/communities/partition_entropy.html) | [Partition entropy](measures/communities/partition_entropy.html#cat_entropy_partition) |  |  |  | · |  |  |  |  |  |  |  |
| [Partition fragmentation](measures/communities/partition_fragmentation.html) | [Partition Fragmentation](measures/communities/partition_fragmentation.html#cat_fragmentation_partition) |  |  |  |  | · |  |  |  |  |  |  |
| [Partition quality (coverage, performance)](measures/communities/partition_quality.html) | [Partition quality (coverage, performance)](measures/communities/partition_quality.html#partition_quality) | · |  |  |  | · |  |  |  |  |  |  |

### Partition comparison and operations

18 measures in 7 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | bct | cdlib |
|---|---|---|---|---|---|---|---|---|
| [Agreement and consensus of partitions](measures/communities/partition_agreement.html) | [Agreement](measures/communities/partition_agreement.html#cat_agreement) |  |  |  |  |  | · |  |
|  | [Agreement weighted](measures/communities/partition_agreement.html#cat_agreement_weighted) |  |  |  |  |  | · |  |
|  | [Consensus](measures/communities/partition_agreement.html#cat_consensus) |  |  |  |  |  | · |  |
| [Compare partitions](measures/communities/compare_partitions.html) | [Compare partitions](measures/communities/compare_partitions.html#compare_partitions) |  | ≠ | · |  | · |  | ≠ |
|  | [Mutual information](measures/communities/compare_partitions.html#cat_information_mutual) |  |  |  | · |  |  |  |
|  | [Partition distance](measures/communities/compare_partitions.html#cat_distance_partition) |  |  |  |  |  | · |  |
|  | [Reduced mutual information](measures/communities/compare_partitions.html#cat_information_mutual_reduced) |  |  |  | · |  |  |  |
|  | [Same Community Index](measures/communities/compare_partitions.html#cat_community_same) |  |  |  |  | · |  |  |
|  | [Variation information](measures/communities/compare_partitions.html#cat_information_variation) |  |  |  | · |  |  |  |
| [Cover comparison and ground truth](measures/communities/cover_comparison.html) | [Cover F1 Similarity](measures/communities/cover_comparison.html#cat_cover_f1_similarity) |  |  |  |  | · |  |  |
|  | [SCDGround Truth Comparison](measures/communities/cover_comparison.html#cat_comparison_ground_scd_truth) |  |  |  |  | · |  |  |
| [Partition mode and centroid state](measures/communities/partition_consensus_state.html) | [Partition Centroid State](measures/communities/partition_consensus_state.html#cat_centroid_partition_state) |  |  |  | · |  |  |  |
|  | [Partition Mode State](measures/communities/partition_consensus_state.html#cat_mode_partition_state) |  |  |  | · |  |  |  |
| [Partition overlap](measures/communities/partition_overlap.html) | [Nested partition overlap](measures/communities/partition_overlap.html#cat_nested_overlap_partition) |  |  |  | · |  |  |  |
|  | [Partition overlap](measures/communities/partition_overlap.html#cat_overlap_partition) |  |  |  | · |  |  |  |
| [Partition overlap center](measures/communities/partition_center.html) | [Nested partition overlap center](measures/communities/partition_center.html#cat_center_nested_overlap_partition) |  |  |  | · |  |  |  |
|  | [Partition overlap center](measures/communities/partition_center.html#cat_center_overlap_partition) |  |  |  | · |  |  |  |
| [Partition test](measures/communities/is_partition.html) | [Is partition (community)](measures/communities/is_partition.html#cat_is_partition-community) | · |  |  |  |  |  |  |

## Components and connectivity

68 measures in 39 concepts.

### Articulation points, bridges and biconnected components

6 measures in 5 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | jgrapht | boost | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Biconnected components](measures/components-and-connectivity/biconnected_components.html) | [Bicomponents](measures/components-and-connectivity/biconnected_components.html#bicomponents) | ✓ | ✓ | · | · | · | ∅ | · | · | · | · |
|  | [Biconnected](measures/components-and-connectivity/biconnected_components.html#nxo_biconnected) | ✓ |  |  |  |  |  |  |  |  |  |
| [Bridge components](measures/components-and-connectivity/bridge_components.html) | [Bridge components (connectivity)](measures/components-and-connectivity/bridge_components.html#cat_bridge_component-connectivity) | · |  |  |  |  |  |  |  |  |  |
| [Bridges](measures/components-and-connectivity/bridges.html) | [Bridges](measures/components-and-connectivity/bridges.html#bridges) | ✓ | ∅ | · |  |  |  | ✓ |  |  |  |
| [Cut points (articulation points)](measures/components-and-connectivity/cut_points.html) | [Cut points](measures/components-and-connectivity/cut_points.html#cut_points) | ✓ | ∅ | ✓ | ✓ |  |  | ✓ |  | ✓ | · |
| [Local bridges](measures/components-and-connectivity/local_bridges.html) | [Local bridges](measures/components-and-connectivity/local_bridges.html#local_bridges) | ✓ |  |  |  |  |  |  |  |  |  |

### Connected components

18 measures in 9 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | bct | gephi | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Attracting components](measures/components-and-connectivity/attracting_components.html) | [Attracting](measures/components-and-connectivity/attracting_components.html#attracting) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Attracting flags](measures/components-and-connectivity/attracting_components.html#attracting_flags) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Is attracting component](measures/components-and-connectivity/attracting_components.html#cat_attracting_component_is) | · |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Number attracting components](measures/components-and-connectivity/attracting_components.html#cat_attracting_component) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Condensation of strong components](measures/components-and-connectivity/condensation.html) | [Condensation](measures/components-and-connectivity/condensation.html#condensation) | ✓ |  |  |  | · |  | · |  |  | · |  |  |  |
| [Connected components](measures/components-and-connectivity/connected_components.html) | [Components](measures/components-and-connectivity/connected_components.html#components) | ✓ | ∅ | ✓ | · | · | ✓ | ✓ | ✓ | · | · | · | ✓ | · |
|  | [Count components](measures/components-and-connectivity/connected_components.html#cat_component_count) |  | · |  |  |  |  |  |  |  |  |  |  |  |
|  | [Kosaraju](measures/components-and-connectivity/connected_components.html#nxo_kosaraju) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Parallel Connected Components](measures/components-and-connectivity/connected_components.html#cat_component_connected_parallel) |  |  |  |  |  | · |  |  |  |  |  |  |  |
|  | [Strong partition](measures/components-and-connectivity/connected_components.html#strong_partition) |  |  |  |  |  |  |  |  | ✓ | ✓ |  |  |  |
| [Fragmentation](measures/components-and-connectivity/fragmentation.html) | [Fragmentation](measures/components-and-connectivity/fragmentation.html#fragmentation) |  | ∅ |  |  |  |  |  |  |  |  |  |  | · |
| [K-components](measures/components-and-connectivity/k_components.html) | [K components](measures/components-and-connectivity/k_components.html#k_components) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [K-connectivity tests](measures/components-and-connectivity/k_connected_tests.html) | [Is kl connected](measures/components-and-connectivity/k_connected_tests.html#cat_connected_is_kl) | · |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Is locally k edge connected (connectivity)](measures/components-and-connectivity/k_connected_tests.html#cat_connected_edge_is_k_locally-connectivity) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [K-edge subgraphs](measures/components-and-connectivity/k_edge_subgraphs.html) | [K edge subgraphs](measures/components-and-connectivity/k_edge_subgraphs.html#gb_k_edge_subgraphs) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [K-edge-connected components](measures/components-and-connectivity/k_edge_components.html) | [K edge components](measures/components-and-connectivity/k_edge_components.html#k_edge_components) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Semiconnected graphs](measures/components-and-connectivity/semiconnected.html) | [Semiconnected](measures/components-and-connectivity/semiconnected.html#semiconnected) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Is semi connected](measures/components-and-connectivity/semiconnected.html#cat_connected_is_semi) |  |  |  |  |  |  | · |  |  |  |  |  |  |

### Connectivity numbers

11 measures in 7 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | jgrapht | boost | ucinet | netrankr |
|---|---|---|---|---|---|---|---|---|---|
| [Approximate node connectivity](measures/components-and-connectivity/node_connectivity.html) | [Node connectivity](measures/components-and-connectivity/node_connectivity.html#ap_node_connectivity) | ✓ |  |  |  |  |  |  |  |
| [Disjoint paths](measures/components-and-connectivity/disjoint_paths.html) | [Disjoint paths](measures/components-and-connectivity/disjoint_paths.html#disjoint_paths) | ✓ | · |  |  | · |  |  |  |
|  | [Gb disjoint paths](measures/components-and-connectivity/disjoint_paths.html#gb_disjoint_paths) | ✓ |  |  |  |  |  |  |  |
| [Dynamic tree connectivity](measures/components-and-connectivity/dynamic_tree_connectivity.html) | [Tree Dynamic Connectivity](measures/components-and-connectivity/dynamic_tree_connectivity.html#cat_connectivity_dynamic_tree) |  |  |  |  | · |  |  |  |
| [Edge connectivity](measures/components-and-connectivity/edge_connectivity.html) | [Connectivity](measures/components-and-connectivity/edge_connectivity.html#connectivity) | ✓ | · | · |  |  | · | · |  |
| [K-connectivity by flow](measures/components-and-connectivity/connectivity_flow_k.html) | [KConnectivity Flow Algorithm](measures/components-and-connectivity/connectivity_flow_k.html#cat_connectivity_flow_k) |  |  |  |  | · |  |  |  |
| [Local node connectivity](measures/components-and-connectivity/local_node_connectivity.html) | [All pairs node](measures/components-and-connectivity/local_node_connectivity.html#all_pairs_node) | ✓ |  |  |  |  |  |  |  |
|  | [Ap local connectivity](measures/components-and-connectivity/local_node_connectivity.html#ap_local_connectivity) | ✓ |  |  |  |  |  |  |  |
|  | [Average node](measures/components-and-connectivity/local_node_connectivity.html#average_node) | ✓ |  |  | · |  |  |  |  |
|  | [Local connectivity](measures/components-and-connectivity/local_node_connectivity.html#local_connectivity) | ✓ |  |  |  |  |  |  |  |
| [Swan connectivity](measures/components-and-connectivity/connectivity_swan.html) | [Swan connectivity](measures/components-and-connectivity/connectivity_swan.html#cat_connectivity_swan) |  |  |  |  |  |  |  | · |

### Cuts and separators

16 measures in 9 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | jgrapht | boost |
|---|---|---|---|---|---|---|---|---|---|
| [All minimum s-t cuts](measures/components-and-connectivity/st_min_cuts.html) | [St Mincuts](measures/components-and-connectivity/st_min_cuts.html#cat_mincuts_st) |  | · |  |  |  |  |  |  |
| [All node cuts](measures/components-and-connectivity/all_node_cuts.html) | [All node cuts (connectivity)](measures/components-and-connectivity/all_node_cuts.html#cat_all_cut-connectivity) | · |  |  |  |  |  |  |  |
| [D-separators](measures/components-and-connectivity/d_separator.html) | [D separated](measures/components-and-connectivity/d_separator.html#gb_d_separated) | ✓ |  |  |  |  |  |  |  |
|  | [Find minimal d separator](measures/components-and-connectivity/d_separator.html#cat_d_find_minimal_separator) | · |  |  |  |  |  |  |  |
|  | [Is minimal d separator](measures/components-and-connectivity/d_separator.html#cat_d_is_minimal_separator) | · |  |  |  |  |  |  |  |
| [Global minimum cut](measures/components-and-connectivity/global_min_cut.html) | [Cut measures](measures/components-and-connectivity/global_min_cut.html#cut_measures) | ✓ |  |  |  |  |  |  |  |
|  | [Min cut](measures/components-and-connectivity/global_min_cut.html#min_cut) | ✓ | · | · | · |  | · | · | · |
|  | [Stoer wagner](measures/components-and-connectivity/global_min_cut.html#gb_stoer_wagner) | ✓ |  |  |  |  |  |  |  |
| [K-edge augmentation](measures/components-and-connectivity/edge_augmentation.html) | [K edge augmentation (connectivity)](measures/components-and-connectivity/edge_augmentation.html#cat_augmentation_edge_k-connectivity) | · |  |  |  |  |  |  |  |
| [Minimum edge cut](measures/components-and-connectivity/minimum_edge_cut.html) | [Edge cut](measures/components-and-connectivity/minimum_edge_cut.html#edge_cut) | ✓ |  |  |  | · |  |  |  |
|  | [St edge cut](measures/components-and-connectivity/minimum_edge_cut.html#st_edge_cut) | ✓ |  |  |  |  |  |  |  |
| [Minimum node cut](measures/components-and-connectivity/minimum_node_cut.html) | [Min node cut](measures/components-and-connectivity/minimum_node_cut.html#min_node_cut) | ✓ |  |  |  |  |  |  |  |
|  | [Node cut](measures/components-and-connectivity/minimum_node_cut.html#node_cut) | ✓ | · | · |  |  |  |  |  |
|  | [St node cut](measures/components-and-connectivity/minimum_node_cut.html#st_node_cut) | ✓ |  |  |  |  |  |  |  |
| [Minimum odd cutset (Padberg-Rao)](measures/components-and-connectivity/odd_min_cutset.html) | [Padberg Rao Odd Minimum Cutset](measures/components-and-connectivity/odd_min_cutset.html#cat_cutset_minimum_odd_padberg_rao) |  |  |  |  |  |  | · |  |
| [Normalized cut state](measures/components-and-connectivity/normalized_cut_state.html) | [Norm Cut State](measures/components-and-connectivity/normalized_cut_state.html#cat_cut_norm_state) |  |  |  | · |  |  |  |  |

### Dominators

3 measures in 1 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | rustworkx | boost |
|---|---|---|---|---|---|---|---|
| [Dominators and dominance frontiers](measures/components-and-connectivity/dominators.html) | [Dominator](measures/components-and-connectivity/dominators.html#cat_dominator) |  |  | · |  |  |  |
|  | [Frontiers](measures/components-and-connectivity/dominators.html#frontiers) | ✓ |  |  |  |  |  |
|  | [Idom](measures/components-and-connectivity/dominators.html#idom) | ✓ | · |  | · | · | · |

### Flows and flow trees

12 measures in 6 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | jgrapht | boost | bct | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Experience flows](measures/components-and-connectivity/experience_flows.html) | [Experienceflows](measures/components-and-connectivity/experience_flows.html#cat_experienceflows) |  |  |  |  |  |  |  |  |  | · |
| [Flow coefficient](measures/components-and-connectivity/flow_coefficient.html) | [Flow coef](measures/components-and-connectivity/flow_coefficient.html#cat_coef_flow) |  |  |  |  |  |  |  |  | · |  |
| [Flow similarity](measures/components-and-connectivity/flow_similarity.html) | [Flowsim](measures/components-and-connectivity/flow_similarity.html#cat_flowsim) |  |  |  |  |  |  |  |  |  | · |
| [Gomory-Hu and equivalent-flow trees](measures/components-and-connectivity/gomory_hu_tree.html) | [Gomory hu](measures/components-and-connectivity/gomory_hu_tree.html#gomory_hu) | ✓ |  | · |  |  |  | · |  |  |  |
|  | [Gomory hu values](measures/components-and-connectivity/gomory_hu_tree.html#gomory_hu_values) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Gusfield Equivalent Flow Tree](measures/components-and-connectivity/gomory_hu_tree.html#cat_equivalent_flow_gusfield_tree) |  |  |  |  |  |  | · |  |  |  |
| [Maximum flow](measures/components-and-connectivity/max_flow.html) | [Max flow](measures/components-and-connectivity/max_flow.html#max_flow) | ✓ | · | · | · | · | · |  | · |  |  |
|  | [Maxflow](measures/components-and-connectivity/max_flow.html#gb_maxflow) | ✓ |  |  |  |  |  |  |  |  |  |
| [Minimum-cost flow](measures/components-and-connectivity/min_cost_flow.html) | [Ahuja Orlin Sharma Cyclic Exchange Local Augmentation](measures/components-and-connectivity/min_cost_flow.html#cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma) |  |  |  |  |  |  | · |  |  |  |
|  | [Capacity Scaling Minimum Cost Flow](measures/components-and-connectivity/min_cost_flow.html#cat_capacity_cost_flow_minimum_scaling) |  |  |  |  |  |  | · |  |  |  |
|  | [Max flow min cost](measures/components-and-connectivity/min_cost_flow.html#max_flow_min_cost) | ✓ |  |  |  |  |  |  | · |  |  |
|  | [Mincost](measures/components-and-connectivity/min_cost_flow.html#gb_mincost) | ✓ |  |  |  |  |  |  |  |  |  |

### Robustness and percolation

2 measures in 2 concepts.

| Concept | Variant | networkx | graphtool |
|---|---|---|---|
| [Edge percolation](measures/components-and-connectivity/edge_percolation.html) | [Edge percolation](measures/components-and-connectivity/edge_percolation.html#cat_edge_percolation) |  | · |
| [KL-connected subgraph](measures/components-and-connectivity/kl_connected_subgraph.html) | [Kl](measures/components-and-connectivity/kl_connected_subgraph.html#st_kl) | ✓ |  |

## Data transforms

53 measures in 23 concepts.

### Graph operators

14 measures in 12 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | jgrapht |
|---|---|---|---|---|---|---|---|---|
| [Graph complement](measures/data-transforms/graph_complement.html) | [Graph complement (graph\_complement)](measures/data-transforms/graph_complement.html#graph_complement) |  |  |  |  |  |  | · |
|  | [Graph complement (op\_complement)](measures/data-transforms/graph_complement.html#op_complement) | · | · | · |  |  | · |  |
| [Graph composition](measures/data-transforms/graph_composition.html) | [Op compose](measures/data-transforms/graph_composition.html#op_compose) | · | · | · |  |  |  |  |
| [Graph difference](measures/data-transforms/graph_difference.html) | [Op difference](measures/data-transforms/graph_difference.html#op_difference) | ✓ | · | · | · | · |  |  |
| [Graph intersection](measures/data-transforms/graph_intersection.html) | [Op intersection](measures/data-transforms/graph_intersection.html#op_intersection) | ✓ | · | · | · |  |  |  |
| [Graph power](measures/data-transforms/graph_power.html) | [Power](measures/data-transforms/graph_power.html#cat_power) | · |  |  |  |  |  |  |
| [Graph products](measures/data-transforms/graph_products.html) | [Graph products](measures/data-transforms/graph_products.html#op_graph_product) | · |  |  |  |  | · |  |
| [Graph reversal](measures/data-transforms/graph_reverse.html) | [Reverse](measures/data-transforms/graph_reverse.html#cat_reverse) | · |  |  |  |  |  |  |
| [Graph symmetric difference](measures/data-transforms/graph_symmetric_difference.html) | [Graph sym difference](measures/data-transforms/graph_symmetric_difference.html#cat_difference_sym) |  |  |  | · |  |  |  |
| [Graph union](measures/data-transforms/graph_union.html) | [Op union](measures/data-transforms/graph_union.html#op_union) | ✓ | · | · | · |  | · |  |
| [Inverse line graph](measures/data-transforms/inverse_line_graph.html) | [Inverse line graph](measures/data-transforms/inverse_line_graph.html#cat_inverse_line) | · |  |  |  |  |  |  |
| [Line graph](measures/data-transforms/line_graph.html) | [Line graph](measures/data-transforms/line_graph.html#line_graph) | ✓ | · | · | · |  | · | · |
| [Mycielskian](measures/data-transforms/mycielskian.html) | [Mycielski graph](measures/data-transforms/mycielskian.html#cat_mycielski) | · |  |  |  |  |  |  |
|  | [Mycielskian](measures/data-transforms/mycielskian.html#cat_mycielskian) | · |  |  |  |  |  |  |

### Matrix and tie transformations

9 measures in 7 concepts.

| Concept | Variant | sna | ergm | ucinet | tnet |
|---|---|---|---|---|---|
| [Attribute-to-matrix construction](measures/data-transforms/attribute_matrix.html) | [Attribute to matrix (same, difference, sender, receiver)](measures/data-transforms/attribute_matrix.html#attribute_matrix) |  |  | · |  |
| [Combining similar relations](measures/data-transforms/combining_relations.html) | [Combining similar relations](measures/data-transforms/combining_relations.html#cat_combining_relations_similar) |  |  | · |  |
| [Congruence, rotation, IPF and state transitions](measures/data-transforms/matrix_utils.html) | [Tucker congruence, factor rotation, iterative proportional fitting, state transitions](measures/data-transforms/matrix_utils.html#matrix_utils) |  |  | · |  |
| [Dichotomize](measures/data-transforms/dichotomize.html) | [Dichotomise](measures/data-transforms/dichotomize.html#cat_dichotomise) |  |  |  | · |
|  | [Dichotomize](measures/data-transforms/dichotomize.html#cat_dichotomize) |  |  | · |  |
| [Multiplex coding](measures/data-transforms/multiplex_coding.html) | [Multiplex coding of several relations into one matrix](measures/data-transforms/multiplex_coding.html#multiplex_coding) |  |  | · |  |
| [Normalize ties](measures/data-transforms/normalize_ties.html) | [Normalize ties (row, column, matrix; sum, mean, max, z, Euclidean, IPF)](measures/data-transforms/normalize_ties.html#normalize_ties) |  |  | · |  |
| [Symmetrize](measures/data-transforms/symmetrize.html) | [Full symmetrize method set and dichotomize by density](measures/data-transforms/symmetrize.html#symmetrize_methods) | · | · | · |  |
|  | [Symmetrise](measures/data-transforms/symmetrize.html#cat_symmetrise) |  |  |  | · |

### Missing data

1 measures in 1 concepts.

| Concept | Variant | ucinet |
|---|---|---|
| [Imputation of missing node-level data](measures/data-transforms/impute_missing.html) | [Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed)](measures/data-transforms/impute_missing.html#cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected) | · |

### Sparsification and backbones

29 measures in 3 concepts.

| Concept | Variant | networkit | bct | ucinet | backbone |
|---|---|---|---|---|---|
| [Graph sparsification (score-based edge filtering)](measures/data-transforms/graph_sparsification.html) | [Algebraic Distance Sparsifier](measures/data-transforms/graph_sparsification.html#cat_algebraic_distance_sparsifier) | · |  |  |  |
|  | [Degree Multiscale Sparsifier](measures/data-transforms/graph_sparsification.html#cat_degree_multiscale_sparsifier) | · |  |  |  |
|  | [Forest Fire Sparsifier](measures/data-transforms/graph_sparsification.html#cat_fire_forest_sparsifier) | · |  |  |  |
|  | [Global Threshold Filter](measures/data-transforms/graph_sparsification.html#cat_filter_global_threshold) | · |  |  |  |
|  | [Jaccard Similarity Sparsifier](measures/data-transforms/graph_sparsification.html#cat_jaccard_similarity_sparsifier) | · |  |  |  |
|  | [Local Degree Sparsifier](measures/data-transforms/graph_sparsification.html#cat_degree_local_sparsifier) | · |  |  |  |
|  | [Local Similarity Sparsifier](measures/data-transforms/graph_sparsification.html#cat_local_similarity_sparsifier) | · |  |  |  |
|  | [Local sparsification (L-Spar)](measures/data-transforms/graph_sparsification.html#local_sparsification) |  |  | · |  |
|  | [Multiscale Sparsifier](measures/data-transforms/graph_sparsification.html#cat_multiscale_sparsifier) | · |  |  |  |
|  | [Quadrilateral Simmelian Sparsifier](measures/data-transforms/graph_sparsification.html#cat_quadrilateral_simmelian_sparsifier) | · |  |  |  |
|  | [Random Edge Sparsifier](measures/data-transforms/graph_sparsification.html#cat_edge_random_sparsifier) | · |  |  |  |
|  | [SCANSparsifier](measures/data-transforms/graph_sparsification.html#cat_scan_sparsifier) | · |  |  |  |
|  | [Simmelian Multiscale Sparsifier](measures/data-transforms/graph_sparsification.html#cat_multiscale_simmelian_sparsifier) | · |  |  |  |
|  | [Simmelian Sparsifier Non Parametric](measures/data-transforms/graph_sparsification.html#cat_non_parametric_simmelian_sparsifier) | · |  |  |  |
|  | [Simmelian Sparsifier Parametric](measures/data-transforms/graph_sparsification.html#cat_parametric_simmelian_sparsifier) | · |  |  |  |
|  | [Triangle Sparsifier](measures/data-transforms/graph_sparsification.html#cat_sparsifier_triangle) | · |  |  |  |
| [Iterative proportional fitting](measures/data-transforms/ipf.html) | [Ipf](measures/data-transforms/ipf.html#cat_ipf) |  |  | · |  |
| [Statistical backbone extraction](measures/data-transforms/statistical_backbone.html) | [Backbone](measures/data-transforms/statistical_backbone.html#cat_backbone) |  | · |  |  |
|  | [Backbone extraction (SDSM/BiCM, FDSM, fixed-row/column/fill)](measures/data-transforms/statistical_backbone.html#backbone_extraction) |  |  |  | · |
|  | [Bicm](measures/data-transforms/statistical_backbone.html#cat_bicm) |  |  |  | · |
|  | [Disparity](measures/data-transforms/statistical_backbone.html#cat_disparity) |  |  |  | · |
|  | [Fastball](measures/data-transforms/statistical_backbone.html#cat_fastball) |  |  |  | · |
|  | [Fdsm](measures/data-transforms/statistical_backbone.html#cat_fdsm) |  |  |  | · |
|  | [Fixedcol](measures/data-transforms/statistical_backbone.html#cat_fixedcol) |  |  |  | · |
|  | [Fixedfill](measures/data-transforms/statistical_backbone.html#cat_fixedfill) |  |  |  | · |
|  | [Fixedrow](measures/data-transforms/statistical_backbone.html#cat_fixedrow) |  |  |  | · |
|  | [Lans](measures/data-transforms/statistical_backbone.html#cat_lans) |  |  |  | · |
|  | [Mlf](measures/data-transforms/statistical_backbone.html#cat_mlf) |  |  |  | · |
|  | [Sdsm](measures/data-transforms/statistical_backbone.html#cat_sdsm) |  |  |  | · |

## Descriptive statistics

37 measures in 28 concepts.

### Clustering and transitivity

14 measures in 8 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | ergm | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | graphblas | bct | bctpy | gephi | ucinet | tnet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Global transitivity](measures/descriptive-statistics/global_transitivity.html) | [Transitivity](measures/descriptive-statistics/global_transitivity.html#transitivity) | ✓ | ∅ | ✓ | · | ✓ | · | ✓ | ✓ |  | ≠ |  | ✓ | ≠ | ✓ |  | · |  |
|  | [Weak and strong transitivity; directed and weighted clustering conventions](measures/descriptive-statistics/global_transitivity.html#sna_transitivity) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Local clustering coefficient](measures/descriptive-statistics/local_clustering.html) | [Average clustering](measures/descriptive-statistics/local_clustering.html#average_clustering) | ✓ | ∅ | ✓ |  |  |  | ✓ |  |  | ≠ | ≠ | ✓ | ≠ | ✓ | ≠ | · |  |
|  | [Clustering](measures/descriptive-statistics/local_clustering.html#clustering) | ✓ | ∅ | ✓ |  |  | · | ✓ |  | · | ≠ | ≠ | ✓ | ≠ | ✓ | ≠ | · | ✓ |
|  | [Directed clustering](measures/descriptive-statistics/local_clustering.html#nxo_directed_clustering) | ✓ |  |  |  |  |  |  |  |  |  |  | ≠ |  | ✓ |  |  |  |
|  | [Extended clustering](measures/descriptive-statistics/local_clustering.html#cat_clustering_extended) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Normalized reciprocity, DKS transitivity and cyclicity](measures/descriptive-statistics/ucinet_cohesion_variants.html) | [Normalized reciprocity and transitivity, DKS transitivity, cyclicity](measures/descriptive-statistics/ucinet_cohesion_variants.html#ucinet_cohesion_variants) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Small-world quotient](measures/descriptive-statistics/small_world_index.html) | [Small world](measures/descriptive-statistics/small_world_index.html#small_world) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Small world observed](measures/descriptive-statistics/small_world_index.html#small_world_observed) | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Square clustering](measures/descriptive-statistics/square_clustering.html) | [Square clustering](measures/descriptive-statistics/square_clustering.html#square_clustering) | ✓ |  |  |  |  |  |  |  |  |  |  | ≠ |  |  |  |  |  |
|  | [Local Square Clustering Coefficient](measures/descriptive-statistics/square_clustering.html#cat_clustering_coefficient_local_square) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Successor transitivity](measures/descriptive-statistics/successor_transitivity.html) | [Successor transitivity](measures/descriptive-statistics/successor_transitivity.html#nxo_successor_transitivity) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Triangle count](measures/descriptive-statistics/triangle_count.html) | [Triangles](measures/descriptive-statistics/triangle_count.html#nxo_triangles) | ✓ | · | · |  | · |  |  |  | · |  |  | ✓ |  |  | ≠ |  |  |
| [Trust transitivity](measures/descriptive-statistics/trust_transitivity.html) | [Trust transitivity](measures/descriptive-statistics/trust_transitivity.html#cat_transitivity_trust) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |

### Density and degree distribution

14 measures in 13 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | ergm | rsiena | graphtool | networkit | bct | bctpy | gephi | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Central graph](measures/descriptive-statistics/central_graph.html) | [Centralgraph](measures/descriptive-statistics/central_graph.html#cat_centralgraph) |  |  |  | · |  |  |  |  |  |  |  |  |
| [Central point dominance](measures/descriptive-statistics/central_point_dominance.html) | [Central point dominance](measures/descriptive-statistics/central_point_dominance.html#cat_central_dominance_point) |  |  |  |  |  |  | · |  |  |  |  |  |
| [Cycle probability](measures/descriptive-statistics/cycle_probability.html) | [Cycprob](measures/descriptive-statistics/cycle_probability.html#cat_cycprob) |  |  |  |  |  |  |  |  | · |  |  |  |
| [Degree distribution and summary statistics](measures/descriptive-statistics/degree_distribution.html) | [Degree distribution and its summary statistics](measures/descriptive-statistics/degree_distribution.html#degree_distribution) |  |  |  |  |  |  |  | · |  |  |  |  |
| [Density](measures/descriptive-statistics/density.html) | [Density](measures/descriptive-statistics/density.html#density) | ≠ | ∅ | ✓ | ≠ | ≠ | · |  | ✓ | ≠ | ✓ | ✓ | · |
|  | [Twomode / density](measures/descriptive-statistics/density.html#twomode-density) | ∅ |  |  |  |  |  |  |  |  |  |  | · |
| [Diversity index](measures/descriptive-statistics/diversity_index.html) | [Diversity](measures/descriptive-statistics/diversity_index.html#cat_diversity) |  | · | · |  |  |  |  |  |  |  |  |  |
| [Edge average](measures/descriptive-statistics/edge_average.html) | [Edge average](measures/descriptive-statistics/edge_average.html#cat_average_edge) |  |  |  |  |  |  | · |  |  |  |  |  |
| [Group density](measures/descriptive-statistics/group_density.html) | [Groupden](measures/descriptive-statistics/group_density.html#cat_groupden) |  |  |  |  |  |  |  |  |  |  |  | · |
| [Joint degree distribution](measures/descriptive-statistics/joint_degree_distribution.html) | [Jdegree](measures/descriptive-statistics/joint_degree_distribution.html#cat_jdegree) |  |  |  |  |  |  |  |  | · |  |  |  |
| [Non-randomness](measures/descriptive-statistics/non_randomness.html) | [Non randomness](measures/descriptive-statistics/non_randomness.html#cat_non_randomness) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Number of ties](measures/descriptive-statistics/tie_count.html) | [Numties](measures/descriptive-statistics/tie_count.html#cat_numties) |  |  |  |  |  |  |  |  |  |  |  | · |
| [Rentian scaling](measures/descriptive-statistics/rentian_scaling.html) | [Rentian scaling](measures/descriptive-statistics/rentian_scaling.html#cat_rentian_scaling) |  |  |  |  |  |  |  |  | · |  |  |  |
| [Structure statistics](measures/descriptive-statistics/structure_statistics.html) | [Structure statistics](measures/descriptive-statistics/structure_statistics.html#cat_statistics_structure) |  |  |  | · |  |  |  |  |  |  |  |  |

### Efficiency, compactness and hierarchy

4 measures in 4 concepts.

| Concept | Variant | networkx | igraph | sna | bct | ucinet |
|---|---|---|---|---|---|---|
| [Compactness](measures/descriptive-statistics/compactness.html) | [Compactness](measures/descriptive-statistics/compactness.html#compactness) | ✓ | ✓ |  |  | · |
| [Krackhardt graph-theoretic dimensions](measures/descriptive-statistics/krackhardt_dimensions.html) | [Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)](measures/descriptive-statistics/krackhardt_dimensions.html#krackhardt_dimensions) |  |  | · |  | · |
| [Resource efficiency](measures/descriptive-statistics/resource_efficiency.html) | [Resource efficiency](measures/descriptive-statistics/resource_efficiency.html#cat_efficiency_resource) |  |  |  | · |  |
| [Routing efficiency](measures/descriptive-statistics/routing_efficiency.html) | [Rout efficiency](measures/descriptive-statistics/routing_efficiency.html#cat_efficiency_rout) |  |  |  | · |  |

### Reciprocity, dyad and triad census

5 measures in 3 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | ergm | rsiena | graphtool | graphblas | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|
| [Dyad census](measures/descriptive-statistics/dyad_census.html) | [Dyad census (mutual, asymmetric, null)](measures/descriptive-statistics/dyad_census.html#dyad_census) |  | · | · | · |  |  |  |  | · |
| [Reciprocity](measures/descriptive-statistics/reciprocity.html) | [Reciprocity](measures/descriptive-statistics/reciprocity.html#reciprocity) | ✓ | ∅ | ✓ | ≠ | ✓ |  | · | ✓ | · |
|  | [Node reciprocity](measures/descriptive-statistics/reciprocity.html#nxo_node_reciprocity) | ✓ |  |  |  |  |  |  | ✓ | · |
| [Triad census](measures/descriptive-statistics/triad_census.html) | [Triad census](measures/descriptive-statistics/triad_census.html#triad_census) | ✓ | ∅ | ≠ | ≠ | ✓ | · |  |  | · |
|  | [Triads](measures/descriptive-statistics/triad_census.html#st_triads) | ✓ |  |  |  |  |  |  |  |  |

## Ego networks

9 measures in 8 concepts.

### Ego measures

9 measures in 8 concepts.

| Concept | Variant | networkx | igraph | sna | ucinet | egor |
|---|---|---|---|---|---|---|
| [Ego betweenness](measures/ego-networks/ego_betweenness.html) | [Ego\_summary / betweenness](measures/ego-networks/ego_betweenness.html#ego_summary-betweenness) | ✓ | ✓ |  | · |  |
| [Ego composition and heterogeneity](measures/ego-networks/ego_composition.html) | [Ego composition: alter shares, Blau and Shannon heterogeneity, IQV](measures/ego-networks/ego_composition.html#ego_composition) |  |  |  | · | · |
| [Ego network components](measures/ego-networks/ego_components.html) | [Ego\_summary / components](measures/ego-networks/ego_components.html#ego_summary-components) | ✓ | ✓ |  |  |  |
| [Ego network density](measures/ego-networks/ego_density.html) | [Ego\_summary / density](measures/ego-networks/ego_density.html#ego_summary-density) | ✓ | ✓ |  | · | ✓ |
| [Ego network extraction](measures/ego-networks/ego_extraction.html) | [Egotize (6 750), Ego network extraction with tab "Ego"](measures/ego-networks/ego_extraction.html#cat_6_750_ego_egotize_extraction_tab_with) |  |  |  | · |  |
|  | [Makeegonets](measures/ego-networks/ego_extraction.html#cat_makeegonets) |  |  |  | · |  |
| [Ego network members](measures/ego-networks/ego_members.html) | [Ego members](measures/ego-networks/ego_members.html#ego_members) | ✓ | ✓ | · |  |  |
| [Ego network ties](measures/ego-networks/ego_ties.html) | [Ego\_summary / ties](measures/ego-networks/ego_ties.html#ego_summary-ties) | ✓ | ✓ |  | · |  |
| [Ego size](measures/ego-networks/ego_size.html) | [Ego size](measures/ego-networks/ego_size.html#ego_size) | ✓ | ✓ |  | · |  |

## Generators and rewiring

149 measures in 77 concepts.

### Block models

2 measures in 1 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | jgrapht | ucinet |
|---|---|---|---|---|---|---|---|---|---|
| [Stochastic block model generator](measures/generators-and-rewiring/sbm_generator.html) | [Sbm random graph](measures/generators-and-rewiring/sbm_generator.html#cat_random_sbm) |  |  |  |  |  | · |  |  |
|  | [Stochastic block model generator](measures/generators-and-rewiring/sbm_generator.html#gen_sbm) | · | · | · | · | · | · | · | · |

### Classic random graphs

16 measures in 12 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | networkit | rustworkx | jgrapht | boost | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|
| [G(n, m) random graph](measures/generators-and-rewiring/gnm_random_graph.html) | [G(n, m) random graph](measures/generators-and-rewiring/gnm_random_graph.html#gen_gnm) | · | · |  | · |  | · | · |  |  |
|  | [Gnm](measures/generators-and-rewiring/gnm_random_graph.html#cat_gnm) |  | · |  |  |  |  |  |  |  |
| [G(n, p) random graph](measures/generators-and-rewiring/gnp_random_graph.html) | [G(n, p) random graph](measures/generators-and-rewiring/gnp_random_graph.html#gen_gnp) | · | · | · | · | · | · | · | · | · |
|  | [Gnp](measures/generators-and-rewiring/gnp_random_graph.html#cat_gnp) |  | · |  |  |  |  |  |  |  |
| [Random bipartite graph](measures/generators-and-rewiring/random_bipartite_graph.html) | [Correlated and bipartite random graph generators](measures/generators-and-rewiring/random_bipartite_graph.html#gen_correlated_bipartite) |  | · |  |  |  |  |  |  |  |
|  | [Random bipartite graph generator](measures/generators-and-rewiring/random_bipartite_graph.html#gen_random_bipartite) |  | · | · |  |  | · | · |  |  |
| [Random clustered graph](measures/generators-and-rewiring/clustered_random_graph.html) | [Clustering Generator](measures/generators-and-rewiring/clustered_random_graph.html#cat_clustering_generator) |  |  |  |  | · |  |  |  |  |
|  | [Random clustered graph](measures/generators-and-rewiring/clustered_random_graph.html#cat_clustered_random) | · |  |  |  |  |  |  |  |  |
| [Random cograph](measures/generators-and-rewiring/random_cograph.html) | [Random cograph](measures/generators-and-rewiring/random_cograph.html#cat_cograph_random) | · |  |  |  |  |  |  |  |  |
| [Random graph with mixing (rgnmix)](measures/generators-and-rewiring/mixing_model_generator.html) | [Rgnmix](measures/generators-and-rewiring/mixing_model_generator.html#cat_rgnmix) |  |  |  | · |  |  |  |  |  |
| [Random graph with uniform MAN distribution](measures/generators-and-rewiring/uman_random_graph.html) | [Rguman](measures/generators-and-rewiring/uman_random_graph.html#cat_rguman) |  |  |  | · |  |  |  |  |  |
| [Random intersection graph](measures/generators-and-rewiring/random_intersection_graph.html) | [Random intersection graph generator](measures/generators-and-rewiring/random_intersection_graph.html#gen_intersection) | · |  |  |  |  |  |  |  |  |
| [Random k-out graph](measures/generators-and-rewiring/random_k_out_graph.html) | [Random k-out graph generator](measures/generators-and-rewiring/random_k_out_graph.html#gen_k_out) | · |  |  |  |  |  |  |  |  |
| [Random kernel graph](measures/generators-and-rewiring/random_kernel_graph.html) | [Random kernel graph](measures/generators-and-rewiring/random_kernel_graph.html#cat_kernel_random) | · |  |  |  |  |  |  |  |  |
| [Random regular graph](measures/generators-and-rewiring/random_regular_graph.html) | [Random regular graph generator](measures/generators-and-rewiring/random_regular_graph.html#gen_regular) | · | · | · |  |  | · | · |  | · |
| [Random tournament](measures/generators-and-rewiring/random_tournament.html) | [Random tournament](measures/generators-and-rewiring/random_tournament.html#cat_random_tournament) | · |  |  |  |  |  |  |  |  |

### Degree-sequence models

13 measures in 9 concepts.

| Concept | Variant | networkx | igraph | pyigraph | networkit |
|---|---|---|---|---|---|
| [Chung-Lu expected-degree model](measures/generators-and-rewiring/chung_lu.html) | [Chung-Lu (expected degree) generator](measures/generators-and-rewiring/chung_lu.html#gen_chung_lu) | · | · | · | · |
| [Configuration model](measures/generators-and-rewiring/configuration_model.html) | [Configuration model](measures/generators-and-rewiring/configuration_model.html#gen_configuration) | · | · | · |  |
|  | [Degseq](measures/generators-and-rewiring/configuration_model.html#cat_degseq) |  | · |  |  |
| [Deterministic degree-sequence realization](measures/generators-and-rewiring/degree_sequence_realization.html) | [Bipartite degree-sequence realization](measures/generators-and-rewiring/degree_sequence_realization.html#gen_realize_bipartite) |  | · | · |  |
|  | [Deterministic realisation of a degree sequence](measures/generators-and-rewiring/degree_sequence_realization.html#gen_degree_realization) | · | · | · |  |
|  | [Havel Hakimi Generator](measures/generators-and-rewiring/degree_sequence_realization.html#cat_generator_hakimi_havel) |  |  |  | · |
| [Geometric soft configuration model](measures/generators-and-rewiring/soft_configuration_geometric.html) | [Geometric soft configuration graph](measures/generators-and-rewiring/soft_configuration_geometric.html#cat_configuration_geometric_soft) | · |  |  |  |
| [Joint degree graph](measures/generators-and-rewiring/joint_degree_graph.html) | [Directed joint degree graph](measures/generators-and-rewiring/joint_degree_graph.html#cat_degree_directed_joint) | · |  |  |  |
|  | [Joint degree graph](measures/generators-and-rewiring/joint_degree_graph.html#cat_degree_joint) | · |  |  |  |
| [Power-law degree sequence](measures/generators-and-rewiring/powerlaw_degree_sequence.html) | [Powerlaw Degree Sequence](measures/generators-and-rewiring/powerlaw_degree_sequence.html#cat_degree_powerlaw_sequence) |  |  |  | · |
| [Sample sequence](measures/generators-and-rewiring/sample_sequence.html) | [Sample seq](measures/generators-and-rewiring/sample_sequence.html#cat_sample_seq) |  | · |  |  |
| [Static fitness and static power-law models](measures/generators-and-rewiring/static_fitness.html) | [Static fitness and static power-law generators](measures/generators-and-rewiring/static_fitness.html#gen_static_fitness) |  | · | · |  |
| [Tree from a degree sequence](measures/generators-and-rewiring/degree_sequence_tree.html) | [Degree sequence tree](measures/generators-and-rewiring/degree_sequence_tree.html#cat_degree_sequence_tree) | · |  |  |  |

### Growth and attachment models

31 measures in 17 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | jgrapht | boost | tnet |
|---|---|---|---|---|---|---|---|---|---|---|
| [BTER replicator](measures/generators-and-rewiring/bter.html) | [BTERReplicator](measures/generators-and-rewiring/bter.html#cat_bter_replicator) |  |  |  |  | · |  |  |  |  |
| [Dorogovtsev-Goltsev-Mendes graph](measures/generators-and-rewiring/dorogovtsev_goltsev_mendes.html) | [Dorogovtsev goltsev mendes graph](measures/generators-and-rewiring/dorogovtsev_goltsev_mendes.html#cat_dorogovtsev_goltsev_mendes) | · |  |  |  |  | · |  |  |  |
|  | [Dorogovtsev-Goltsev-Mendes graph](measures/generators-and-rewiring/dorogovtsev_goltsev_mendes.html#dorogovtsev_goltsev_mendes_graph) |  |  |  |  | · |  |  |  |  |
| [Duplication-divergence models](measures/generators-and-rewiring/duplication_divergence.html) | [Duplication divergence graph](measures/generators-and-rewiring/duplication_divergence.html#cat_divergence_duplication) | · |  |  |  |  |  |  |  |  |
|  | [Partial duplication graph](measures/generators-and-rewiring/duplication_divergence.html#cat_duplication_partial) | · |  |  |  |  |  |  |  |  |
| [Dynamic path generator](measures/generators-and-rewiring/dynamic_path_generator.html) | [Dynamic Path Generator](measures/generators-and-rewiring/dynamic_path_generator.html#cat_dynamic_generator_path) |  |  |  |  | · |  |  |  |  |
| [Forest fire model](measures/generators-and-rewiring/forest_fire.html) | [Forest fire generator](measures/generators-and-rewiring/forest_fire.html#gen_forest_fire) |  | · | · |  | · |  |  |  |  |
| [Growing network models (GN, citation, Callaway, establishment)](measures/generators-and-rewiring/growing_network_models.html) | [Citation-type growth generators](measures/generators-and-rewiring/growing_network_models.html#gen_citation) |  | · | · |  |  |  |  |  |  |
|  | [Establishment](measures/generators-and-rewiring/growing_network_models.html#cat_establishment) |  |  | · |  |  |  |  |  |  |
|  | [Gn graph](measures/generators-and-rewiring/growing_network_models.html#cat_gn) | · |  |  |  |  |  |  |  |  |
|  | [Gnc graph](measures/generators-and-rewiring/growing_network_models.html#cat_gnc) | · |  |  |  |  |  |  |  |  |
|  | [Gnr graph](measures/generators-and-rewiring/growing_network_models.html#cat_gnr) | · |  |  |  |  |  |  |  |  |
|  | [Growing random graph generator](measures/generators-and-rewiring/growing_network_models.html#gen_growing) |  | · | · |  |  |  |  |  |  |
|  | [Trait-based (Callaway) growth generator](measures/generators-and-rewiring/growing_network_models.html#gen_traits) |  | · |  |  |  |  |  |  |  |
| [Growth (tnet)](measures/generators-and-rewiring/growth_tnet.html) | [Growth](measures/generators-and-rewiring/growth_tnet.html#cat_growth) |  |  |  |  |  |  |  |  | · |
| [LFR benchmark generator](measures/generators-and-rewiring/lfr_benchmark.html) | [LFRGenerator](measures/generators-and-rewiring/lfr_benchmark.html#cat_generator_lfr) |  |  |  |  | · |  |  |  |  |
| [Mocnik generator](measures/generators-and-rewiring/mocnik.html) | [Mocnik Generator](measures/generators-and-rewiring/mocnik.html#cat_generator_mocnik) |  |  |  |  | · |  |  |  |  |
|  | [Mocnik Generator Basic](measures/generators-and-rewiring/mocnik.html#cat_basic_generator_mocnik) |  |  |  |  | · |  |  |  |  |
| [PLOD generator](measures/generators-and-rewiring/plod.html) | [Plod generator](measures/generators-and-rewiring/plod.html#cat_generator_plod) |  |  |  |  |  |  |  | · |  |
|  | [Plod iterator](measures/generators-and-rewiring/plod.html#cat_iterator_plod) |  |  |  |  |  |  |  | · |  |
| [Power-law cluster graph](measures/generators-and-rewiring/powerlaw_cluster.html) | [Powerlaw cluster graph](measures/generators-and-rewiring/powerlaw_cluster.html#cat_cluster_powerlaw) | · |  |  |  |  |  |  |  |  |
| [Preference (types) random graph](measures/generators-and-rewiring/preference_types.html) | [Preference (types) random graph generator](measures/generators-and-rewiring/preference_types.html#gen_preference) |  | · | · |  |  |  |  |  |  |
| [Preferential attachment](measures/generators-and-rewiring/preferential_attachment.html) | [Pa](measures/generators-and-rewiring/preferential_attachment.html#cat_pa) |  | · |  |  |  |  |  |  |  |
|  | [Pa age](measures/generators-and-rewiring/preferential_attachment.html#cat_age_pa) |  | · |  |  |  |  |  |  |  |
|  | [Preferential attachment generator](measures/generators-and-rewiring/preferential_attachment.html#gen_preferential) | · | · | · | · | · | · | · |  |  |
|  | [Preferential attachment graph (bipartite)](measures/generators-and-rewiring/preferential_attachment.html#cat_attachment_preferential-bipartite) | · |  |  |  |  |  |  |  |  |
| [Pub-web generator](measures/generators-and-rewiring/pub_web.html) | [Dynamic Pub Web Generator](measures/generators-and-rewiring/pub_web.html#cat_dynamic_generator_pub_web) |  |  |  |  | · |  |  |  |  |
|  | [Pub Web Generator](measures/generators-and-rewiring/pub_web.html#cat_generator_pub_web) |  |  |  |  | · |  |  |  |  |
| [R-MAT](measures/generators-and-rewiring/rmat.html) | [R-MAT generator](measures/generators-and-rewiring/rmat.html#gen_rmat) |  |  |  |  | · |  |  | · |  |
| [Random Internet AS graph](measures/generators-and-rewiring/internet_as_graph.html) | [Random internet as graph](measures/generators-and-rewiring/internet_as_graph.html#cat_as_internet_random) | · |  |  |  |  |  |  |  |  |
| [SSCA graph generator](measures/generators-and-rewiring/ssca.html) | [Ssca graph generator](measures/generators-and-rewiring/ssca.html#cat_generator_ssca) |  |  |  |  |  |  |  | · |  |

### Named and deterministic graphs

46 measures in 14 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | rustworkx | jgrapht | boost | ucinet | netrankr |
|---|---|---|---|---|---|---|---|---|---|---|
| [Algebraic and combinatorial named graphs (Kneser, Paley, Kautz, De Bruijn, LCF, Sudoku)](measures/generators-and-rewiring/algebraic_named_graphs.html) | [De Bruijn graph generator](measures/generators-and-rewiring/algebraic_named_graphs.html#gen_de_bruijn) |  | · | · |  |  |  |  |  |  |
|  | [Kautz graph generator](measures/generators-and-rewiring/algebraic_named_graphs.html#gen_kautz) |  | · | · |  |  |  |  |  |  |
|  | [Kneser graph](measures/generators-and-rewiring/algebraic_named_graphs.html#cat_kneser) | · |  |  |  |  |  |  |  |  |
|  | [LCF notation graph generator](measures/generators-and-rewiring/algebraic_named_graphs.html#gen_lcf) | · |  | · |  |  |  |  |  |  |
|  | [Paley graph](measures/generators-and-rewiring/algebraic_named_graphs.html#cat_paley) | · |  |  |  |  |  |  |  |  |
|  | [Sudoku graph](measures/generators-and-rewiring/algebraic_named_graphs.html#cat_sudoku) | · |  |  |  |  |  |  |  |  |
| [Circulant and ring graphs (ladder, chordal, Petersen, Harary)](measures/generators-and-rewiring/circulant_ring_graphs.html) | [Chordal cycle graph](measures/generators-and-rewiring/circulant_ring_graphs.html#cat_chordal_cycle) | · |  |  |  |  |  |  |  |  |
|  | [Chordal ring generator](measures/generators-and-rewiring/circulant_ring_graphs.html#gen_chordal_ring) |  | · |  |  |  |  |  |  |  |
|  | [Circulant graph generator](measures/generators-and-rewiring/circulant_ring_graphs.html#gen_circulant) | · | · |  |  |  |  |  |  |  |
|  | [Circular ladder graph](measures/generators-and-rewiring/circulant_ring_graphs.html#cat_circular_ladder) | · |  |  |  |  |  |  |  |  |
|  | [Generalized petersen graph](measures/generators-and-rewiring/circulant_ring_graphs.html#cat_generalized_petersen) | · |  |  |  | · |  |  |  |  |
|  | [Generalized Petersen graph generator](measures/generators-and-rewiring/circulant_ring_graphs.html#gen_generalized_petersen) |  |  |  |  |  | · |  |  |  |
|  | [Hkn harary graph](measures/generators-and-rewiring/circulant_ring_graphs.html#cat_harary_hkn) | · |  |  |  |  |  |  |  |  |
|  | [Hnm harary graph](measures/generators-and-rewiring/circulant_ring_graphs.html#cat_harary_hnm) | · |  |  |  |  |  |  |  |  |
|  | [Implicit family](measures/generators-and-rewiring/circulant_ring_graphs.html#implicit_family) | ∅ |  |  |  |  |  |  |  |  |
| [Clique composites (barbell, lollipop, tadpole, windmill, caveman, ring of cliques)](measures/generators-and-rewiring/clique_composite_graphs.html) | [Barbell graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_barbell) | · |  |  |  | · |  |  |  |  |
|  | [Caveman graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_caveman) | · |  |  |  |  |  |  |  |  |
|  | [Connected caveman graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_caveman_connected) | · |  |  |  |  |  |  |  |  |
|  | [Lollipop graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_lollipop) | · |  |  |  | · |  |  |  |  |
|  | [Make max clique graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_clique_make_max) | · |  |  |  |  |  |  |  |  |
|  | [Relaxed caveman graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_caveman_relaxed) | · |  |  |  |  |  |  |  |  |
|  | [Ring of cliques](measures/generators-and-rewiring/clique_composite_graphs.html#cat_clique_ring) | · |  |  |  |  |  |  |  |  |
|  | [Tadpole graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_tadpole) | · |  |  |  |  |  |  |  |  |
|  | [Windmill graph](measures/generators-and-rewiring/clique_composite_graphs.html#cat_windmill) | · |  |  |  |  |  |  |  |  |
|  | [Windmill graph generator](measures/generators-and-rewiring/clique_composite_graphs.html#gen_windmill) |  |  |  |  |  | · |  |  |  |
| [Clique, regular, bow-tie and all-graphs generators](measures/generators-and-rewiring/misc_generators.html) | [Clique, regular and bow-tie generators; all graphs of size n](measures/generators-and-rewiring/misc_generators.html#misc_generators) |  |  |  |  |  |  |  | · |  |
|  | [Allgraphs](measures/generators-and-rewiring/misc_generators.html#cat_allgraphs) |  |  |  |  |  |  |  | · |  |
|  | [Makebowtie](measures/generators-and-rewiring/misc_generators.html#cat_makebowtie) |  |  |  |  |  |  |  | · |  |
| [Complete and complete multipartite graphs](measures/generators-and-rewiring/complete_multipartite_graphs.html) | [Complete multipartite graph generator](measures/generators-and-rewiring/complete_multipartite_graphs.html#gen_complete_multipartite) | · | · |  |  |  |  |  |  |  |
|  | [Full bipartite graph](measures/generators-and-rewiring/complete_multipartite_graphs.html#cat_bipartite_full) |  | · |  |  |  |  |  |  |  |
|  | [Full graph](measures/generators-and-rewiring/complete_multipartite_graphs.html#cat_full) |  | · |  |  |  |  |  |  |  |
|  | [Full join](measures/generators-and-rewiring/complete_multipartite_graphs.html#cat_full_join) | · |  |  |  |  |  |  |  |  |
|  | [Full multipartite](measures/generators-and-rewiring/complete_multipartite_graphs.html#cat_full_multipartite) |  | · |  |  |  |  |  |  |  |
|  | [Turan graph generator](measures/generators-and-rewiring/complete_multipartite_graphs.html#gen_turan) | · | · |  |  |  |  |  |  |  |
| [Contingency graph](measures/generators-and-rewiring/contingency_graph.html) | [Contingency graph](measures/generators-and-rewiring/contingency_graph.html#cat_contingency) |  |  |  | · |  |  |  |  |  |
| [Deterministic generators](measures/generators-and-rewiring/deterministic_generators.html) | [Deterministic generators](measures/generators-and-rewiring/deterministic_generators.html#deterministic_generators) | ✓ | · | · | · | · | · |  | · |  |
| [Dominance graph](measures/generators-and-rewiring/dominance_graph.html) | [Dominance graph](measures/generators-and-rewiring/dominance_graph.html#cat_dominance) |  |  |  |  |  |  |  |  | · |
| [Expander graphs](measures/generators-and-rewiring/expander_graphs.html) | [Margulis gabber galil graph](measures/generators-and-rewiring/expander_graphs.html#cat_gabber_galil_margulis) | · |  |  |  |  |  |  |  |  |
|  | [Maybe regular expander graph](measures/generators-and-rewiring/expander_graphs.html#cat_expander_maybe_regular) | · |  |  |  |  |  |  |  |  |
|  | [Random regular expander graph](measures/generators-and-rewiring/expander_graphs.html#cat_expander_random_regular) | · |  |  |  |  |  |  |  |  |
| [Game tree](measures/generators-and-rewiring/game_tree.html) | [Tree Game](measures/generators-and-rewiring/game_tree.html#cat_game_tree) |  |  | · |  |  |  |  |  |  |
| [Graph atlas](measures/generators-and-rewiring/graph_atlas.html) | [Graph atlas](measures/generators-and-rewiring/graph_atlas.html#cat_atlas) | · |  |  |  |  |  |  |  |  |
|  | [Graph atlas g](measures/generators-and-rewiring/graph_atlas.html#cat_atlas_g) | · |  |  |  |  |  |  |  |  |
| [Linearized chord diagram graph](measures/generators-and-rewiring/linearized_chord_diagram.html) | [Linearized Chord Diagram Graph Generator](measures/generators-and-rewiring/linearized_chord_diagram.html#cat_chord_diagram_generator_linearized) |  |  |  |  |  | · |  |  |  |
| [Make connected](measures/generators-and-rewiring/make_connected.html) | [Make connected](measures/generators-and-rewiring/make_connected.html#cat_connected_make) |  |  |  |  |  |  | · |  |  |
| [Stochastic graph](measures/generators-and-rewiring/stochastic_graph.html) | [Stochastic graph](measures/generators-and-rewiring/stochastic_graph.html#cat_stochastic) | · |  |  |  |  |  |  |  |  |

### Random trees and forests

3 measures in 3 concepts.

| Concept | Variant | networkx | igraph |
|---|---|---|---|
| [Random lobster](measures/generators-and-rewiring/random_lobster.html) | [Random lobster graph](measures/generators-and-rewiring/random_lobster.html#cat_lobster_random) | · |  |
| [Random shell graph](measures/generators-and-rewiring/random_shell.html) | [Random shell graph](measures/generators-and-rewiring/random_shell.html#cat_random_shell) | · |  |
| [Random tree](measures/generators-and-rewiring/random_tree.html) | [Random tree generator](measures/generators-and-rewiring/random_tree.html#gen_random_tree) | · | · |

### Rewiring and randomization

16 measures in 9 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | bct | ucinet | tnet |
|---|---|---|---|---|---|---|---|---|---|---|
| [Edge swap and contract](measures/generators-and-rewiring/swap_contract.html) | [Swap contract](measures/generators-and-rewiring/swap_contract.html#swap_contract) | ✓ | · | · | · | · | · | · |  |  |
| [Lattice-preserving rewiring](measures/generators-and-rewiring/rewire_lattice.html) | [Lattice-preserving rewiring](measures/generators-and-rewiring/rewire_lattice.html#rewire_lattice) |  |  |  |  |  |  | · |  |  |
| [Random edge addition and removal](measures/generators-and-rewiring/random_edge_edit.html) | [Random edge addition and removal](measures/generators-and-rewiring/random_edge_edit.html#random_edge_edit) |  |  |  |  | · |  |  |  |  |
|  | [Random k lift](measures/generators-and-rewiring/random_edge_edit.html#cat_k_lift_random) | · |  |  |  |  |  |  |  |  |
| [Random matrix generators (density, even degree, fractal, Toeplitz)](measures/generators-and-rewiring/bct_random_matrix.html) | [Generate fc](measures/generators-and-rewiring/bct_random_matrix.html#cat_fc_generate) |  |  |  |  |  |  | · |  |  |
|  | [Makeeven CIJ](measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_makeeven) |  |  |  |  |  |  | · |  |  |
|  | [Makefractal CIJ](measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_makefractal) |  |  |  |  |  |  | · |  |  |
|  | [Makerand CIJ](measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_makerand) |  |  |  |  |  |  | · |  |  |
|  | [Makerand CIJdegreesfixed](measures/generators-and-rewiring/bct_random_matrix.html#cat_ci_jdegreesfixed_makerand) |  |  |  |  |  |  | · |  |  |
|  | [Maketoeplitz CIJ](measures/generators-and-rewiring/bct_random_matrix.html#cat_cij_maketoeplitz) |  |  |  |  |  |  | · |  |  |
| [Random reference graph](measures/generators-and-rewiring/random_reference.html) | [Random reference](measures/generators-and-rewiring/random_reference.html#cat_random_reference) | · |  |  |  |  |  |  |  |  |
| [Randomize network](measures/generators-and-rewiring/randomize_network.html) | [Randomize](measures/generators-and-rewiring/randomize_network.html#cat_randomize) |  |  |  |  |  |  |  | · |  |
| [Reinforcement](measures/generators-and-rewiring/reinforcement.html) | [Reinforcement](measures/generators-and-rewiring/reinforcement.html#cat_reinforcement) |  |  |  |  |  |  |  |  | · |
| [Triadic closure generation](measures/generators-and-rewiring/triadic_closure_generation.html) | [Generate triadic closure](measures/generators-and-rewiring/triadic_closure_generation.html#cat_closure_generate_triadic) |  |  |  |  | · |  |  |  |  |
| [Weighted reshuffling](measures/generators-and-rewiring/weighted_reshuffling.html) | [Rg](measures/generators-and-rewiring/weighted_reshuffling.html#cat_rg) |  |  |  |  |  |  |  |  | · |
|  | [Rg reshuffling](measures/generators-and-rewiring/weighted_reshuffling.html#cat_reshuffling_rg) |  |  |  |  |  |  |  |  | · |

### Small-world, lattice and geometric models

22 measures in 12 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | jgrapht | boost | bct | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Grid communities](measures/generators-and-rewiring/grid_communities.html) | [Grid communities](measures/generators-and-rewiring/grid_communities.html#cat_community_grid) |  |  |  |  |  |  |  |  |  | · |  |
| [Hyperbolic random graph](measures/generators-and-rewiring/hyperbolic_graph.html) | [Hyperbolic random graph generator](measures/generators-and-rewiring/hyperbolic_graph.html#gen_hyperbolic) |  |  |  |  |  | · | · |  |  |  |  |
| [Interval graph](measures/generators-and-rewiring/interval_graph.html) | [Interval graph](measures/generators-and-rewiring/interval_graph.html#cat_interval) | · |  |  | · |  |  |  |  |  |  |  |
| [K-nearest-neighbor graph](measures/generators-and-rewiring/knn_graph.html) | [Generate knn](measures/generators-and-rewiring/knn_graph.html#cat_generate_knn) |  |  |  |  | · |  |  |  |  |  |  |
|  | [Nearest Neighbor Graph](measures/generators-and-rewiring/knn_graph.html#cat_nearest_neighbor) |  |  | · |  |  |  |  |  |  |  |  |
| [Latent-space graphs](measures/generators-and-rewiring/latent_space_graph.html) | [Latent-space generators (dot product, sphere, islands)](measures/generators-and-rewiring/latent_space_graph.html#gen_latent_space) |  | · |  |  |  |  |  |  |  |  |  |
| [Lattice graphs](measures/generators-and-rewiring/lattice_graphs.html) | [Heavy hex graph](measures/generators-and-rewiring/lattice_graphs.html#cat_heavy_hex) |  |  |  |  |  |  | · |  |  |  |  |
|  | [Heavy square graph](measures/generators-and-rewiring/lattice_graphs.html#cat_heavy_square) |  |  |  |  |  |  | · |  |  |  |  |
|  | [Hexagonal lattice graph](measures/generators-and-rewiring/lattice_graphs.html#cat_hexagonal_lattice) | · |  | · |  |  |  | · |  |  |  |  |
|  | [Lattice generator](measures/generators-and-rewiring/lattice_graphs.html#gen_lattice) | · | · | · |  | · |  | · | · |  |  |  |
|  | [Makeringlattice CIJ](measures/generators-and-rewiring/lattice_graphs.html#cat_cij_makeringlattice) |  |  |  |  |  |  |  |  |  | · |  |
|  | [Mesh graph](measures/generators-and-rewiring/lattice_graphs.html#cat_mesh) |  |  |  |  |  |  | · |  |  |  |  |
|  | [Mesh graph generator](measures/generators-and-rewiring/lattice_graphs.html#cat_generator_mesh) |  |  |  |  |  |  |  |  | · |  |  |
|  | [Regular Ring Lattice Generator](measures/generators-and-rewiring/lattice_graphs.html#cat_generator_lattice_regular_ring) |  |  |  |  |  | · |  |  |  |  |  |
|  | [Triangular lattice graph](measures/generators-and-rewiring/lattice_graphs.html#cat_lattice_triangular) | · |  | · |  |  |  |  |  |  |  |  |
| [Navigable small-world graph](measures/generators-and-rewiring/navigable_small_world.html) | [Navigable small world graph](measures/generators-and-rewiring/navigable_small_world.html#cat_navigable_small_world) | · |  |  |  |  |  |  |  |  |  |  |
|  | [Navigable small-world generator](measures/generators-and-rewiring/navigable_small_world.html#gen_navigable_small_world) |  |  |  |  |  |  |  | · |  |  |  |
| [Random geometric graph](measures/generators-and-rewiring/geometric_graph.html) | [Random geometric graph generator](measures/generators-and-rewiring/geometric_graph.html#gen_geometric) | · | · | · |  | · |  | · |  |  |  |  |
| [Small-world generator](measures/generators-and-rewiring/small_world_generator.html) | [Small-world generator](measures/generators-and-rewiring/small_world_generator.html#gen_small_world) | · | · | · | · |  | · |  | · | · |  | · |
| [Spectral graph forge](measures/generators-and-rewiring/spectral_graph_forge.html) | [Spectral graph forge](measures/generators-and-rewiring/spectral_graph_forge.html#cat_forge_spectral) | · |  |  |  |  |  |  |  |  |  |  |
| [Triangulation](measures/generators-and-rewiring/delaunay_triangulation.html) | [Triangulation](measures/generators-and-rewiring/delaunay_triangulation.html#cat_triangulation) |  |  |  |  | · |  |  |  |  |  |  |
| [Visibility graph](measures/generators-and-rewiring/visibility_graph.html) | [Visibility graph](measures/generators-and-rewiring/visibility_graph.html#cat_visibility) | · |  |  |  |  |  |  |  |  |  |  |

## Graph theory and combinatorics

185 measures in 104 concepts.

### Chordal, perfect and special graph classes

12 measures in 7 concepts.

| Concept | Variant | networkx | igraph | pyigraph | jgrapht | netrankr |
|---|---|---|---|---|---|---|
| [Asteroidal triples and AT-free graphs](measures/graph-theory-and-combinatorics/asteroidal_triples.html) | [Asteroidal](measures/graph-theory-and-combinatorics/asteroidal_triples.html#st_asteroidal) | ✓ |  |  |  |  |
|  | [At free](measures/graph-theory-and-combinatorics/asteroidal_triples.html#st_at_free) | ✓ |  |  |  |  |
| [Chordal graphs](measures/graph-theory-and-combinatorics/chordal_graphs.html) | [Chordal order](measures/graph-theory-and-combinatorics/chordal_graphs.html#st_chordal_order) | ✓ |  |  |  |  |
|  | [Chordal-graph tests and algorithms](measures/graph-theory-and-combinatorics/chordal_graphs.html#chordal) |  |  |  | · |  |
|  | [Fill](measures/graph-theory-and-combinatorics/chordal_graphs.html#st_fill) | ✓ |  |  |  |  |
|  | [St chordal](measures/graph-theory-and-combinatorics/chordal_graphs.html#st_chordal) | ✓ | · | · |  |  |
| [Distance-regular intersection array](measures/graph-theory-and-combinatorics/intersection_array.html) | [Intersection](measures/graph-theory-and-combinatorics/intersection_array.html#st_intersection) | ✓ |  |  |  |  |
| [Distance-regular test](measures/graph-theory-and-combinatorics/distance_regular.html) | [Is distance regular](measures/graph-theory-and-combinatorics/distance_regular.html#cat_distance_is_regular) | · |  |  |  |  |
| [Junction tree](measures/graph-theory-and-combinatorics/junction_tree.html) | [Junction](measures/graph-theory-and-combinatorics/junction_tree.html#st_junction) | ✓ |  |  |  |  |
| [Perfect graphs](measures/graph-theory-and-combinatorics/perfect_graph.html) | [Perfect-graph (Berge) tests](measures/graph-theory-and-combinatorics/perfect_graph.html#perfect_graph) |  |  |  | · |  |
|  | [Perfect](measures/graph-theory-and-combinatorics/perfect_graph.html#st_perfect) | ✓ |  |  |  |  |
| [Threshold graphs](measures/graph-theory-and-combinatorics/threshold_graph.html) | [Threshold graphs](measures/graph-theory-and-combinatorics/threshold_graph.html#threshold_graph) | · |  |  |  | · |

### Coloring

10 measures in 4 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost |
|---|---|---|---|---|---|---|---|---|---|---|
| [Bipartite coloring and test](measures/graph-theory-and-combinatorics/bipartite_coloring.html) | [Bipartite](measures/graph-theory-and-combinatorics/bipartite_coloring.html#cat_bipartite) |  | · |  |  |  |  |  |  | · |
|  | [Bipartite color](measures/graph-theory-and-combinatorics/bipartite_coloring.html#bipartite_color) | ✓ | · | · | · |  | · | · |  | · |
|  | [Is bipartite node set (bipartite)](measures/graph-theory-and-combinatorics/bipartite_coloring.html#cat_bipartite_is_set-bipartite) | · |  |  |  |  |  |  |  |  |
| [Chromatic and Tutte polynomials](measures/graph-theory-and-combinatorics/graph_polynomials.html) | [Chromatic polynomial](measures/graph-theory-and-combinatorics/graph_polynomials.html#cat_chromatic_polynomial) | · |  |  |  |  |  |  |  |  |
|  | [Polynomials](measures/graph-theory-and-combinatorics/graph_polynomials.html#st_polynomials) | ✓ |  |  |  |  |  |  |  |  |
| [Edge coloring](measures/graph-theory-and-combinatorics/edge_coloring.html) | [Bipartite edge color](measures/graph-theory-and-combinatorics/edge_coloring.html#cat_bipartite_color_edge) |  |  |  |  |  | · |  |  |  |
|  | [Greedy edge color](measures/graph-theory-and-combinatorics/edge_coloring.html#cat_color_edge_greedy) |  |  |  |  |  | · |  |  |  |
|  | [Misra gries edge color](measures/graph-theory-and-combinatorics/edge_coloring.html#cat_color_edge_gries_misra) |  |  |  |  |  | · |  |  |  |
| [Vertex coloring](measures/graph-theory-and-combinatorics/vertex_coloring.html) | [Coloring](measures/graph-theory-and-combinatorics/vertex_coloring.html#st_coloring) | ✓ |  |  |  |  |  |  |  |  |
|  | [Greedy color](measures/graph-theory-and-combinatorics/vertex_coloring.html#greedy_color) | ≠ | · | · | · | · | · |  | · | · |

### Covers and dominating sets

10 measures in 5 concepts.

| Concept | Variant | networkx | networkit |
|---|---|---|---|
| [Connected dominating set](measures/graph-theory-and-combinatorics/connected_dominating_set.html) | [Cds](measures/graph-theory-and-combinatorics/connected_dominating_set.html#st_cds) | ✓ |  |
| [Dominating set](measures/graph-theory-and-combinatorics/dominating_set.html) | [Dominating sets](measures/graph-theory-and-combinatorics/dominating_set.html#dominating_set) | · |  |
|  | [Ap dominating set](measures/graph-theory-and-combinatorics/dominating_set.html#ap_dominating_set) | ✓ |  |
|  | [Dominating](measures/graph-theory-and-combinatorics/dominating_set.html#st_dominating) | ✓ |  |
| [Edge cover](measures/graph-theory-and-combinatorics/edge_cover.html) | [Edge cover](measures/graph-theory-and-combinatorics/edge_cover.html#edge_cover) | · |  |
|  | [St edge cover](measures/graph-theory-and-combinatorics/edge_cover.html#st_edge_cover) | ✓ |  |
| [K-factor](measures/graph-theory-and-combinatorics/k_factor.html) | [Kfactor](measures/graph-theory-and-combinatorics/k_factor.html#st_kfactor) | ✓ |  |
|  | [Kfactor edges](measures/graph-theory-and-combinatorics/k_factor.html#st_kfactor_edges) | ✓ |  |
| [Vertex cover](measures/graph-theory-and-combinatorics/vertex_cover.html) | [Vertex cover](measures/graph-theory-and-combinatorics/vertex_cover.html#vertex_cover) | ✓ |  |
|  | [Ap vertex cover](measures/graph-theory-and-combinatorics/vertex_cover.html#ap_vertex_cover) | ✓ | · |

### Cycles

16 measures in 9 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | ergm | graphtool | rustworkx | sknetwork | jgrapht | boost |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Chordless cycles](measures/graph-theory-and-combinatorics/chordless_cycles.html) | [Chordless cycles](measures/graph-theory-and-combinatorics/chordless_cycles.html#chordless_cycles) | ✓ |  |  |  |  |  |  |  |  |  |
| [Cycle basis](measures/graph-theory-and-combinatorics/cycle_basis.html) | [Cycle basis](measures/graph-theory-and-combinatorics/cycle_basis.html#cycle_basis) | ≠ |  |  |  |  |  | · |  | · |  |
|  | [Basis](measures/graph-theory-and-combinatorics/cycle_basis.html#basis) | ≠ |  |  |  |  |  |  |  |  |  |
|  | [Nxs cycle basis](measures/graph-theory-and-combinatorics/cycle_basis.html#nxs_cycle_basis) | ✓ |  |  |  |  |  |  |  |  |  |
| [Cycle census and count](measures/graph-theory-and-combinatorics/cycle_census.html) | [Cycle count](measures/graph-theory-and-combinatorics/cycle_census.html#gb_cycle_count) | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | [Kcycle census](measures/graph-theory-and-combinatorics/cycle_census.html#cat_census_kcycle) |  |  |  | · |  |  |  |  |  |  |
| [Feedback arc and vertex sets](measures/graph-theory-and-combinatorics/feedback_sets.html) | [Feedback arc and vertex sets](measures/graph-theory-and-combinatorics/feedback_sets.html#feedback_sets) |  | · | · |  |  |  |  |  |  |  |
|  | [Break cycles](measures/graph-theory-and-combinatorics/feedback_sets.html#cat_break_cycle) |  |  |  |  |  |  |  | · |  |  |
| [Find a cycle](measures/graph-theory-and-combinatorics/find_cycle.html) | [Find cycle](measures/graph-theory-and-combinatorics/find_cycle.html#find_cycle) | ✓ | · |  |  |  |  | · | · | · |  |
|  | [Nxs find cycle](measures/graph-theory-and-combinatorics/find_cycle.html#nxs_find_cycle) | ✓ |  |  |  |  |  |  |  |  |  |
| [Girth](measures/graph-theory-and-combinatorics/girth.html) | [Girth](measures/graph-theory-and-combinatorics/girth.html#girth) | ✓ | · | · |  |  |  |  |  |  |  |
| [Minimum cycle basis](measures/graph-theory-and-combinatorics/minimum_cycle_basis.html) | [Mcb weight](measures/graph-theory-and-combinatorics/minimum_cycle_basis.html#gb_mcb_weight) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Min basis](measures/graph-theory-and-combinatorics/minimum_cycle_basis.html#min_basis) | ≠ |  |  |  |  |  |  |  |  |  |
|  | [Min basis weights](measures/graph-theory-and-combinatorics/minimum_cycle_basis.html#min_basis_weights) | ≠ |  |  |  |  |  |  |  |  |  |
| [Recursive cycles](measures/graph-theory-and-combinatorics/recursive_cycles.html) | [Recursive cycles](measures/graph-theory-and-combinatorics/recursive_cycles.html#nxs_recursive_cycles) | ✓ |  |  |  |  |  |  |  |  |  |
| [Simple cycles](measures/graph-theory-and-combinatorics/simple_cycles.html) | [Simple cycles](measures/graph-theory-and-combinatorics/simple_cycles.html#simple_cycles) | ✓ | · | · |  |  | · | · |  | · | · |

### Degree sequences and predicates

19 measures in 13 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | ergm | rustworkx | graphblas |
|---|---|---|---|---|---|---|---|---|
| [Complete graph test](measures/graph-theory-and-combinatorics/is_complete.html) | [Is complete](measures/graph-theory-and-combinatorics/is_complete.html#cat_complete_is) |  | · | · |  |  |  |  |
| [Flow hierarchy](measures/graph-theory-and-combinatorics/flow_hierarchy.html) | [Flow hierarchy](measures/graph-theory-and-combinatorics/flow_hierarchy.html#nxo_flow_hierarchy) | ✓ |  |  |  |  |  |  |
| [Generalized degree](measures/graph-theory-and-combinatorics/generalized_degree.html) | [Generalized degree](measures/graph-theory-and-combinatorics/generalized_degree.html#generalized_degree) | ✓ |  |  |  |  |  | ✓ |
| [Graphical and bigraphical degree-sequence tests](measures/graph-theory-and-combinatorics/degree_sequence_tests.html) | [Degree sequence test](measures/graph-theory-and-combinatorics/degree_sequence_tests.html#nxs_degree_sequence_test) | ✓ |  |  |  |  |  |  |
|  | [Is bigraphical](measures/graph-theory-and-combinatorics/degree_sequence_tests.html#cat_bigraphical_is) |  |  | · |  |  |  |  |
|  | [Is degseq](measures/graph-theory-and-combinatorics/degree_sequence_tests.html#cat_degseq_is) |  | · |  |  |  |  |  |
|  | [Is graphical](measures/graph-theory-and-combinatorics/degree_sequence_tests.html#cat_graphical_is) |  | · | · |  |  |  |  |
| [Hierarchy test](measures/graph-theory-and-combinatorics/is_hierarchical.html) | [Is hierarchical](measures/graph-theory-and-combinatorics/is_hierarchical.html#cat_hierarchical_is) |  | · |  |  |  |  |  |
| [Isolates](measures/graph-theory-and-combinatorics/isolates.html) | [Is isolate](measures/graph-theory-and-combinatorics/isolates.html#cat_is_isolate) | · |  |  |  |  |  |  |
|  | [Isolates](measures/graph-theory-and-combinatorics/isolates.html#gb_isolates) | ✓ |  |  | · | · | · |  |
| [Loop and multi-edge detection](measures/graph-theory-and-combinatorics/multi_loop_detection.html) | [Loop and multi-edge detection](measures/graph-theory-and-combinatorics/multi_loop_detection.html#multi_loop_detection) |  | · |  |  |  |  |  |
| [Regular expander test](measures/graph-theory-and-combinatorics/is_regular_expander.html) | [Is regular expander](measures/graph-theory-and-combinatorics/is_regular_expander.html#cat_expander_is_regular) | · |  |  |  |  |  |  |
| [Regular graph tests](measures/graph-theory-and-combinatorics/is_regular.html) | [Is k regular](measures/graph-theory-and-combinatorics/is_regular.html#cat_is_k_regular) | · |  |  |  |  |  |  |
|  | [Is strongly regular](measures/graph-theory-and-combinatorics/is_regular.html#cat_is_regular_strongly) | · |  |  |  |  |  |  |
|  | [Regular](measures/graph-theory-and-combinatorics/is_regular.html#st_regular) | ✓ |  |  |  |  |  |  |
| [S-metric](measures/graph-theory-and-combinatorics/s_metric.html) | [S metric](measures/graph-theory-and-combinatorics/s_metric.html#cat_metric_s) | · |  |  |  |  |  |  |
| [Simple path test](measures/graph-theory-and-combinatorics/simple_path_test.html) | [Is simple path](measures/graph-theory-and-combinatorics/simple_path_test.html#nxs_is_simple_path) | ✓ |  |  |  |  |  |  |
| [Tournament score sequence](measures/graph-theory-and-combinatorics/tournament_score_sequence.html) | [Score sequence](measures/graph-theory-and-combinatorics/tournament_score_sequence.html#cat_sequence) | · |  |  |  |  |  |  |
| [Tournament tests](measures/graph-theory-and-combinatorics/tournament_tests.html) | [Tournament](measures/graph-theory-and-combinatorics/tournament_tests.html#st_tournament) | ✓ |  |  |  |  |  |  |

### Distances between graphs

3 measures in 1 concepts.

| Concept | Variant | sna |
|---|---|---|
| [Distances between graphs (Hamming, structural)](measures/graph-theory-and-combinatorics/graph_distance.html) | [Hdist](measures/graph-theory-and-combinatorics/graph_distance.html#cat_hdist) | · |
|  | [Sdmat](measures/graph-theory-and-combinatorics/graph_distance.html#cat_sdmat) | · |
|  | [Structdist](measures/graph-theory-and-combinatorics/graph_distance.html#cat_structdist) | · |

### Eulerian paths, Hamiltonian paths and tours

10 measures in 4 concepts.

| Concept | Variant | networkx | igraph | graphtool | networkit | jgrapht | boost |
|---|---|---|---|---|---|---|---|
| [Chinese postman](measures/graph-theory-and-combinatorics/chinese_postman.html) | [Chinese Postman](measures/graph-theory-and-combinatorics/chinese_postman.html#cat_chinese_postman) |  |  |  |  | · |  |
| [Eulerian circuits and paths](measures/graph-theory-and-combinatorics/eulerian.html) | [Eulerian circuits and paths](measures/graph-theory-and-combinatorics/eulerian.html#eulerian) |  |  |  |  | · |  |
|  | [Euler](measures/graph-theory-and-combinatorics/eulerian.html#nxs_euler) | · | · |  |  |  |  |
|  | [Euler circuit](measures/graph-theory-and-combinatorics/eulerian.html#nxs_euler_circuit) | ✓ |  |  |  |  |  |
|  | [Is eulerian](measures/graph-theory-and-combinatorics/eulerian.html#gb_is_eulerian) | ✓ |  |  |  |  |  |
| [Hamiltonian paths and cycles](measures/graph-theory-and-combinatorics/hamiltonian.html) | [Hampath](measures/graph-theory-and-combinatorics/hamiltonian.html#st_hampath) | ✓ |  |  |  |  |  |
|  | [Palmer Hamiltonian Cycle](measures/graph-theory-and-combinatorics/hamiltonian.html#cat_cycle_hamiltonian_palmer) |  |  |  |  | · |  |
| [Traveling salesman](measures/graph-theory-and-combinatorics/traveling_salesman.html) | [St tsp](measures/graph-theory-and-combinatorics/traveling_salesman.html#st_tsp) | ✓ |  |  |  |  |  |
|  | [Traveling salesman (exact and heuristic)](measures/graph-theory-and-combinatorics/traveling_salesman.html#tsp) | · |  |  | · | · | · |
|  | [Tsp tour](measures/graph-theory-and-combinatorics/traveling_salesman.html#cat_tour_tsp) |  |  | · |  |  |  |

### Geometry

3 measures in 2 concepts.

| Concept | Variant | igraph | pyigraph |
|---|---|---|---|
| [Convex hull](measures/graph-theory-and-combinatorics/convex_hull.html) | [Convex hull](measures/graph-theory-and-combinatorics/convex_hull.html#cat_convex_hull) |  | · |
| [Farthest vertices](measures/graph-theory-and-combinatorics/farthest_vertices.html) | [Farthest points](measures/graph-theory-and-combinatorics/farthest_vertices.html#cat_farthest_points) |  | · |
|  | [Farthest vertices](measures/graph-theory-and-combinatorics/farthest_vertices.html#cat_farthest) | · |  |

### Independent sets and approximation

17 measures in 7 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | sknetwork | jgrapht |
|---|---|---|---|---|---|---|---|
| [Approximate clique and independent set (Ramsey, clique removal)](measures/graph-theory-and-combinatorics/approx_clique_independent_set.html) | [Clique removal](measures/graph-theory-and-combinatorics/approx_clique_independent_set.html#ap_clique_removal) | ≠ |  |  |  |  |  |
|  | [Large clique size](measures/graph-theory-and-combinatorics/approx_clique_independent_set.html#ap_large_clique_size) | ≠ |  |  |  |  |  |
|  | [Nx ramsey](measures/graph-theory-and-combinatorics/approx_clique_independent_set.html#ap_nx_ramsey) | ✓ |  |  |  |  |  |
| [Approximation heuristics (annealing, random)](measures/graph-theory-and-combinatorics/approx_misc.html) | [Nx anneal](measures/graph-theory-and-combinatorics/approx_misc.html#ap_nx_anneal) | ✓ |  |  |  |  |  |
|  | [Nx random](measures/graph-theory-and-combinatorics/approx_misc.html#ap_nx_random) | ✓ |  |  | · |  |  |
| [Densest subgraph](measures/graph-theory-and-combinatorics/densest_subgraph.html) | [Densest](measures/graph-theory-and-combinatorics/densest_subgraph.html#ap_densest) | ✓ |  |  |  |  |  |
|  | [Goldberg Maximum Density Subgraph Algorithm](measures/graph-theory-and-combinatorics/densest_subgraph.html#cat_density_goldberg_maximum_subgraph) |  |  |  |  |  | · |
|  | [Goldberg Maximum Density Subgraph Algorithm Base](measures/graph-theory-and-combinatorics/densest_subgraph.html#cat_base_density_goldberg_maximum_subgraph) |  |  |  |  |  | · |
|  | [Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight](measures/graph-theory-and-combinatorics/densest_subgraph.html#cat_density_edge_goldberg_maximum_per_subgraph_weight) |  |  |  |  |  | · |
|  | [Goldberg Maximum Density Subgraph Algorithm Node Weights](measures/graph-theory-and-combinatorics/densest_subgraph.html#cat_density_goldberg_maximum_subgraph_weights) |  |  |  |  |  | · |
| [K-center and Gon heuristic](measures/graph-theory-and-combinatorics/k_center.html) | [Gon Heuristic](measures/graph-theory-and-combinatorics/k_center.html#cat_gon_heuristic) |  |  |  |  |  | · |
|  | [KCenters](measures/graph-theory-and-combinatorics/k_center.html#cat_centers_k) |  |  |  |  | · |  |
| [Maximal independent set](measures/graph-theory-and-combinatorics/independent_set.html) | [Is independent vertex set](measures/graph-theory-and-combinatorics/independent_set.html#cat_independent_is_set) |  |  | · |  |  |  |
|  | [Is ivs](measures/graph-theory-and-combinatorics/independent_set.html#cat_is_ivs) |  | · |  |  |  |  |
|  | [Mis](measures/graph-theory-and-combinatorics/independent_set.html#mis) | ✓ | · | · | · |  |  |
| [Metric closure](measures/graph-theory-and-combinatorics/metric_closure.html) | [Metric closure (approximate)](measures/graph-theory-and-combinatorics/metric_closure.html#cat_closure_metric-approximate) | · |  |  |  |  |  |
| [One-exchange approximation](measures/graph-theory-and-combinatorics/max_cut_approximation.html) | [One exchange (approximate)](measures/graph-theory-and-combinatorics/max_cut_approximation.html#cat_exchange_one-approximate) | · |  |  |  |  |  |

### Isomorphism and subgraph matching

27 measures in 10 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | nauty |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Automorphism group, count and canonical form](measures/graph-theory-and-combinatorics/automorphisms.html) | [Automorphism group, count and canonical form](measures/graph-theory-and-combinatorics/automorphisms.html#automorphisms) |  | · | · |  |  |  |  |  |  |  |
| [Graph edit distance](measures/graph-theory-and-combinatorics/graph_edit_distance.html) | [Ged Walk](measures/graph-theory-and-combinatorics/graph_edit_distance.html#cat_ged_walk) |  |  |  |  | · |  |  |  |  |  |
|  | [Graph edit distance](measures/graph-theory-and-combinatorics/graph_edit_distance.html#ged) | ✓ |  |  |  |  |  |  | · |  |  |
| [Graph isomorphism](measures/graph-theory-and-combinatorics/graph_isomorphism.html) | [Could be iso](measures/graph-theory-and-combinatorics/graph_isomorphism.html#could_be_iso) | ✓ |  |  |  |  |  |  |  |  |  |
|  | [Di Graph Matcher](measures/graph-theory-and-combinatorics/graph_isomorphism.html#cat_di_matcher) | · |  |  |  |  |  |  |  |  |  |
|  | [Graph Matcher](measures/graph-theory-and-combinatorics/graph_isomorphism.html#cat_matcher) | · |  |  |  |  |  |  |  |  |  |
|  | [Match vertices](measures/graph-theory-and-combinatorics/graph_isomorphism.html#cat_match) |  | · |  |  |  |  |  |  |  |  |
|  | [Multi Di Graph Matcher](measures/graph-theory-and-combinatorics/graph_isomorphism.html#cat_di_matcher_multi) | · |  |  |  |  |  |  |  |  |  |
|  | [Multi Graph Matcher](measures/graph-theory-and-combinatorics/graph_isomorphism.html#cat_matcher_multi) | · |  |  |  |  |  |  |  |  |  |
|  | [Vf2pp](measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp) | ✓ | · | · | · |  | · | · | · | · | ✓ |
| [Maximum bisimulation](measures/graph-theory-and-combinatorics/bisimulation.html) | [Maximum bisimulation](measures/graph-theory-and-combinatorics/bisimulation.html#cat_bisimulation_maximum) |  |  |  |  |  | · |  |  |  |  |
| [McGregor common subgraphs](measures/graph-theory-and-combinatorics/common_subgraphs.html) | [Mcgregor common subgraphs](measures/graph-theory-and-combinatorics/common_subgraphs.html#cat_common_mcgregor_subgraphs) |  |  |  |  |  |  |  |  | · |  |
| [Node and edge attribute match functions](measures/graph-theory-and-combinatorics/attribute_match_functions.html) | [Categorical edge match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_categorical_edge_match) | · |  |  |  |  |  |  |  |  |  |
|  | [Categorical multiedge match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_categorical_match_multiedge) | · |  |  |  |  |  |  |  |  |  |
|  | [Categorical node match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_categorical_match) | · |  |  |  |  |  |  |  |  |  |
|  | [Generic edge match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_edge_generic_match) | · |  |  |  |  |  |  |  |  |  |
|  | [Generic multiedge match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_generic_match_multiedge) | · |  |  |  |  |  |  |  |  |  |
|  | [Generic node match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_generic_match) | · |  |  |  |  |  |  |  |  |  |
|  | [Numerical edge match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_edge_match_numerical) | · |  |  |  |  |  |  |  |  |  |
|  | [Numerical multiedge match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_match_multiedge_numerical) | · |  |  |  |  |  |  |  |  |  |
|  | [Numerical node match](measures/graph-theory-and-combinatorics/attribute_match_functions.html#cat_match_numerical) | · |  |  |  |  |  |  |  |  |  |
| [Subgraph isomorphism (ISMAGS)](measures/graph-theory-and-combinatorics/subgraph_isomorphism_ismags.html) | [ISMAGS](measures/graph-theory-and-combinatorics/subgraph_isomorphism_ismags.html#cat_ismags) | · |  |  |  |  |  |  |  |  |  |
| [Time-respecting graph matching](measures/graph-theory-and-combinatorics/isomorphism_time_respecting.html) | [Time Respecting Di Graph Matcher](measures/graph-theory-and-combinatorics/isomorphism_time_respecting.html#cat_di_matcher_respecting_time) | · |  |  |  |  |  |  |  |  |  |
|  | [Time Respecting Graph Matcher](measures/graph-theory-and-combinatorics/isomorphism_time_respecting.html#cat_matcher_respecting_time) | · |  |  |  |  |  |  |  |  |  |
| [Tree isomorphism](measures/graph-theory-and-combinatorics/tree_isomorphism.html) | [Tree iso](measures/graph-theory-and-combinatorics/tree_isomorphism.html#tree_iso) | ✓ |  |  |  |  |  |  |  |  |  |
| [Weisfeiler-Lehman graph and subgraph hash](measures/graph-theory-and-combinatorics/isomorphism_hash.html) | [Wl hash](measures/graph-theory-and-combinatorics/isomorphism_hash.html#wl_hash) | ✓ |  |  |  |  |  | · | · |  |  |
|  | [Wl subgraph](measures/graph-theory-and-combinatorics/isomorphism_hash.html#wl_subgraph) | ✓ |  |  |  |  |  |  |  |  |  |

### Matching

15 measures in 8 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | jgrapht | boost |
|---|---|---|---|---|---|---|---|---|---|
| [Approximate and b-matching](measures/graph-theory-and-combinatorics/approximate_matching.html) | [Approximate and b-matching](measures/graph-theory-and-combinatorics/approximate_matching.html#matching_approx) |  |  |  |  | · |  | · |  |
| [Bipartite maximum matching](measures/graph-theory-and-combinatorics/bipartite_maximum_matching.html) | [Hopcroft karp](measures/graph-theory-and-combinatorics/bipartite_maximum_matching.html#hopcroft_karp) | ✓ | · | · |  |  |  | · | · |
|  | [Nx eppstein](measures/graph-theory-and-combinatorics/bipartite_maximum_matching.html#nx_eppstein) | ✓ |  |  |  |  |  |  |  |
|  | [Nx eppstein size](measures/graph-theory-and-combinatorics/bipartite_maximum_matching.html#nx_eppstein_size) | ✓ |  |  |  |  |  |  |  |
|  | [Nx hk mates](measures/graph-theory-and-combinatorics/bipartite_maximum_matching.html#nx_hk_mates) | ✓ |  |  |  |  |  |  |  |
| [Dulmage-Mendelsohn decomposition](measures/graph-theory-and-combinatorics/dulmage_mendelsohn.html) | [Dulmage Mendelsohn Decomposition](measures/graph-theory-and-combinatorics/dulmage_mendelsohn.html#cat_decomposition_dulmage_mendelsohn) |  |  |  |  |  |  | · |  |
| [Matching and perfect-matching tests](measures/graph-theory-and-combinatorics/matching_tests.html) | [Check matching](measures/graph-theory-and-combinatorics/matching_tests.html#check_matching) | ✓ | · |  |  | · | · |  |  |
| [Maximal extendability](measures/graph-theory-and-combinatorics/matching_extendability.html) | [Maximal extendability](measures/graph-theory-and-combinatorics/matching_extendability.html#maximal_extendability) | ✓ |  |  |  |  |  |  |  |
| [Maximal matching](measures/graph-theory-and-combinatorics/maximal_matching.html) | [Maximal matching](measures/graph-theory-and-combinatorics/maximal_matching.html#maximal_matching) | ✓ |  |  |  |  |  |  |  |
|  | [Min maximal matching (approximate)](measures/graph-theory-and-combinatorics/maximal_matching.html#cat_matching_maximal_min-approximate) | · |  |  |  |  |  |  |  |
| [Maximum-weight matching](measures/graph-theory-and-combinatorics/maximum_weight_matching.html) | [Max weight matching](measures/graph-theory-and-combinatorics/maximum_weight_matching.html#max_weight_matching) | ✓ |  |  | · |  | · | · | · |
|  | [Mwm](measures/graph-theory-and-combinatorics/maximum_weight_matching.html#st_mwm) | ✓ |  |  |  |  |  |  |  |
|  | [Mwm pairs](measures/graph-theory-and-combinatorics/maximum_weight_matching.html#st_mwm_pairs) | ✓ |  |  |  |  |  |  |  |
| [Minimum-weight matching](measures/graph-theory-and-combinatorics/minimum_weight_matching.html) | [Min weight full matching](measures/graph-theory-and-combinatorics/minimum_weight_matching.html#min_weight_full_matching) | ✓ |  |  |  |  |  |  |  |
|  | [Min weight matching](measures/graph-theory-and-combinatorics/minimum_weight_matching.html#min_weight_matching) | ✓ |  |  |  |  |  |  |  |

### Planarity

6 measures in 3 concepts.

| Concept | Variant | networkx | graphtool | rustworkx | jgrapht | boost |
|---|---|---|---|---|---|---|
| [Kuratowski subgraph and counterexample](measures/graph-theory-and-combinatorics/kuratowski_subgraph.html) | [Counterexample](measures/graph-theory-and-combinatorics/kuratowski_subgraph.html#st_counterexample) | ✓ |  |  |  |  |
|  | [Kuratowski](measures/graph-theory-and-combinatorics/kuratowski_subgraph.html#st_kuratowski) | ✓ |  |  |  |  |
| [Planar embedding](measures/graph-theory-and-combinatorics/planar_embedding.html) | [Embedding](measures/graph-theory-and-combinatorics/planar_embedding.html#st_embedding) | ✓ |  |  |  |  |
|  | [Embedding euler](measures/graph-theory-and-combinatorics/planar_embedding.html#st_embedding_euler) | ✓ |  |  |  |  |
| [Planarity test](measures/graph-theory-and-combinatorics/planarity_test.html) | [Planar](measures/graph-theory-and-combinatorics/planarity_test.html#st_planar) | ✓ | · | · |  | · |
|  | [Planarity testing, embedding and straight-line drawing](measures/graph-theory-and-combinatorics/planarity_test.html#planarity) |  | · |  | · | · |

### Similarity and link prediction

7 measures in 7 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | sknetwork | jgrapht | bct |
|---|---|---|---|---|---|---|---|---|---|
| [Dice similarity](measures/graph-theory-and-combinatorics/dice_similarity.html) | [Dice pairwise](measures/graph-theory-and-combinatorics/dice_similarity.html#cat_dice_pairwise) |  |  |  |  |  |  |  | · |
| [Edge neighborhood overlap](measures/graph-theory-and-combinatorics/edge_neighborhood_overlap.html) | [Edge nei overlap](measures/graph-theory-and-combinatorics/edge_neighborhood_overlap.html#cat_edge_nei_overlap) |  |  |  |  |  |  |  | · |
| [Generalized topological overlap](measures/graph-theory-and-combinatorics/topological_overlap.html) | [Gtom](measures/graph-theory-and-combinatorics/topological_overlap.html#cat_gtom) |  |  |  |  |  |  |  | · |
| [Link prediction scores](measures/graph-theory-and-combinatorics/link_prediction.html) | [Link prediction](measures/graph-theory-and-combinatorics/link_prediction.html#link_prediction) | ✓ | · | · | · | · | · | · |  |
| [Matching index](measures/graph-theory-and-combinatorics/matching_index.html) | [Matching ind](measures/graph-theory-and-combinatorics/matching_index.html#cat_ind_matching) |  |  |  |  |  |  |  | · |
| [Panther](measures/graph-theory-and-combinatorics/panther.html) | [Panther](measures/graph-theory-and-combinatorics/panther.html#panther) | ✓ |  |  |  |  |  |  |  |
| [SimRank](measures/graph-theory-and-combinatorics/simrank.html) | [Simrank](measures/graph-theory-and-combinatorics/simrank.html#simrank) | ✓ |  |  |  |  |  |  |  |

### Spanners, contraction and reduction

8 measures in 5 concepts.

| Concept | Variant | networkx | igraph | pyigraph | networkit | rustworkx | jgrapht | keyplayer |
|---|---|---|---|---|---|---|---|---|
| [Dedensify and compression](measures/graph-theory-and-combinatorics/dedensify.html) | [Dedensify](measures/graph-theory-and-combinatorics/dedensify.html#gb_dedensify) | ✓ |  |  |  |  |  |  |
|  | [Quotient internal](measures/graph-theory-and-combinatorics/dedensify.html#gb_quotient_internal) | ✓ |  |  |  |  |  |  |
|  | [Snap groups](measures/graph-theory-and-combinatorics/dedensify.html#gb_snap_groups) | ✓ |  |  |  |  |  |  |
| [Node boundary](measures/graph-theory-and-combinatorics/node_boundary.html) | [Node boundary](measures/graph-theory-and-combinatorics/node_boundary.html#gb_node_boundary) | ✓ |  |  |  |  |  |  |
| [Node contraction](measures/graph-theory-and-combinatorics/contracted_nodes.html) | [Contracted nodes](measures/graph-theory-and-combinatorics/contracted_nodes.html#nxs_contracted_nodes) | ✓ | · | · |  | · |  | · |
| [Pruned landmark labeling](measures/graph-theory-and-combinatorics/landmark_labeling.html) | [Pruned Landmark Labeling](measures/graph-theory-and-combinatorics/landmark_labeling.html#cat_labeling_landmark_pruned) |  |  |  | · |  |  |  |
| [Spanners](measures/graph-theory-and-combinatorics/spanners.html) | [Greedy Multiplicative Spanner](measures/graph-theory-and-combinatorics/spanners.html#cat_greedy_multiplicative_spanner) |  |  |  |  |  | · |  |
|  | [Spanner ok](measures/graph-theory-and-combinatorics/spanners.html#gb_spanner_ok) | ✓ |  |  |  |  |  |  |

### Tree decomposition

2 measures in 1 concepts.

| Concept | Variant | networkx |
|---|---|---|
| [Tree decomposition and treewidth](measures/graph-theory-and-combinatorics/tree_decomposition.html) | [Treewidth](measures/graph-theory-and-combinatorics/tree_decomposition.html#ap_treewidth) | ✓ |
|  | [Tw min degree](measures/graph-theory-and-combinatorics/tree_decomposition.html#ap_tw_min_degree) | ✓ |

### Triangles and local counts

5 measures in 3 concepts.

| Concept | Variant | networkx | igraph | pyigraph |
|---|---|---|---|---|
| [Convergence degree and field size](measures/graph-theory-and-combinatorics/convergence_degree.html) | [Convergence degree](measures/graph-theory-and-combinatorics/convergence_degree.html#cat_convergence_degree) |  |  | · |
|  | [Convergence field size](measures/graph-theory-and-combinatorics/convergence_degree.html#cat_convergence_field_size) |  |  | · |
| [Scan statistic](measures/graph-theory-and-combinatorics/scan_statistic.html) | [Local scan](measures/graph-theory-and-combinatorics/scan_statistic.html#cat_local_scan) |  | · |  |
|  | [Scan stat](measures/graph-theory-and-combinatorics/scan_statistic.html#cat_scan_stat) |  | · |  |
| [Triangle listing](measures/graph-theory-and-combinatorics/triangle_list.html) | [Triangle list](measures/graph-theory-and-combinatorics/triangle_list.html#nxs_triangle_list) | ✓ |  |  |

### Unclassified procedures

15 measures in 15 concepts.

| Concept | Variant | graphtool | networkit | bct | ucinet |
|---|---|---|---|---|---|
| [Congru](measures/graph-theory-and-combinatorics/congru.html) | [Congru](measures/graph-theory-and-combinatorics/congru.html#cat_congru) |  |  |  | · |
| [CPA](measures/graph-theory-and-combinatorics/cpa.html) | [Cpa](measures/graph-theory-and-combinatorics/cpa.html#cat_cpa) |  |  |  | · |
| [Dlbet](measures/graph-theory-and-combinatorics/dlbet.html) | [Dlbet](measures/graph-theory-and-combinatorics/dlbet.html#cat_dlbet) |  |  |  | · |
| [FACD](measures/graph-theory-and-combinatorics/facd.html) | [Facd](measures/graph-theory-and-combinatorics/facd.html#cat_facd) |  |  |  | · |
| [Makeup](measures/graph-theory-and-combinatorics/makeup.html) | [Makeup](measures/graph-theory-and-combinatorics/makeup.html#cat_makeup) |  |  |  | · |
| [OPP](measures/graph-theory-and-combinatorics/opp.html) | [Opp](measures/graph-theory-and-combinatorics/opp.html#cat_opp) |  |  |  | · |
| [PSI](measures/graph-theory-and-combinatorics/psi.html) | [Psi](measures/graph-theory-and-combinatorics/psi.html#cat_psi) |  |  |  | · |
| [Rowlas](measures/graph-theory-and-combinatorics/rowlas.html) | [Rowlas](measures/graph-theory-and-combinatorics/rowlas.html#cat_rowlas) |  |  |  | · |
| [RSH](measures/graph-theory-and-combinatorics/rsh.html) | [Rsh](measures/graph-theory-and-combinatorics/rsh.html#cat_rsh) |  |  |  | · |
| [Runtime parallelism context](measures/graph-theory-and-combinatorics/runtime_context.html) | [Openmp context](measures/graph-theory-and-combinatorics/runtime_context.html#cat_context_openmp) | · |  |  |  |
| [RWB](measures/graph-theory-and-combinatorics/rwb.html) | [Rwb](measures/graph-theory-and-combinatorics/rwb.html#cat_rwb) |  |  |  | · |
| [Score](measures/graph-theory-and-combinatorics/score.html) | [Score](measures/graph-theory-and-combinatorics/score.html#cat_score) |  |  | · |  |
| [Sfigality](measures/graph-theory-and-combinatorics/sfigality.html) | [Sfigality](measures/graph-theory-and-combinatorics/sfigality.html#cat_sfigality) |  | · |  |  |
| [SPSP](measures/graph-theory-and-combinatorics/spsp.html) | [SPSP](measures/graph-theory-and-combinatorics/spsp.html#cat_spsp) |  | · |  |  |
| [TCE](measures/graph-theory-and-combinatorics/tce.html) | [TCE](measures/graph-theory-and-combinatorics/tce.html#cat_tce) |  | · |  |  |

## Inference (QAP, null models)

7 measures in 7 concepts.

### QAP and permutation tests

7 measures in 7 concepts.

| Concept | Variant | sna | ucinet |
|---|---|---|---|
| [ANOVA density models](measures/inference-qap-null-models/anova_density.html) | [ANOVA density models (constant/variable homophily, structural blockmodel)](measures/inference-qap-null-models/anova_density.html#anova_density) |  | · |
| [Conditional uniform graph tests and null models](measures/inference-qap-null-models/cug_null_models.html) | [Conditional uniform graph tests and null models](measures/inference-qap-null-models/cug_null_models.html#cug_null_models) | · | · |
| [Group-level permutation tests](measures/inference-qap-null-models/node_permutation_tests.html) | [Group-level permutation tests](measures/inference-qap-null-models/node_permutation_tests.html#node_permutation_tests) |  | · |
| [Logistic MR-QAP](measures/inference-qap-null-models/logistic_qap.html) | [Logistic MR-QAP](measures/inference-qap-null-models/logistic_qap.html#lr_qap) | · | · |
| [MR-QAP regression](measures/inference-qap-null-models/qap_regression.html) | [MR-QAP regression (Y-permutation, double semi-partialling)](measures/inference-qap-null-models/qap_regression.html#qap_regression) | · | · |
| [Network autocorrelation](measures/inference-qap-null-models/network_autocorrelation.html) | [Network autocorrelation: lag/error model, Moran, Geary](measures/inference-qap-null-models/network_autocorrelation.html#network_autocorrelation) | · | · |
| [QAP correlation](measures/inference-qap-null-models/qap_correlation.html) | [QAP correlation (Y-permutation, exact and Monte Carlo)](measures/inference-qap-null-models/qap_correlation.html#qap_correlation) | · | · |

## Input and output

41 measures in 5 concepts.

### Binary and serialization formats

4 measures in 1 concepts.

| Concept | Variant | pyigraph | networkit |
|---|---|---|---|
| [Binary and serialization formats](measures/input-and-output/binary_io.html) | [GRAPHTOOLBINARY read and write](measures/input-and-output/binary_io.html#io_graphtoolbinary) |  | · |
|  | [NETWORKITBINARY read and write](measures/input-and-output/binary_io.html#io_networkitbinary) |  | · |
|  | [PICKLE read and write](measures/input-and-output/binary_io.html#io_pickle) | · |  |
|  | [THRILLGRAPHBINARY read and write](measures/input-and-output/binary_io.html#io_thrillgraphbinary) |  | · |

### Edge-list and adjacency-list formats

9 measures in 1 concepts.

| Concept | Variant | networkx | igraph | pyigraph | networkit | jgrapht |
|---|---|---|---|---|---|---|
| [Edge-list and adjacency-list text formats](measures/input-and-output/text_edge_list_io.html) | [ADJACENCY read and write](measures/input-and-output/text_edge_list_io.html#io_adjacency) |  |  | · |  |  |
|  | [CSV read and write](measures/input-and-output/text_edge_list_io.html#io_csv) |  |  |  |  | · |
|  | [EDGELIST read and write](measures/input-and-output/text_edge_list_io.html#io_edgelist) | · |  | · | · |  |
|  | [Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list](measures/input-and-output/text_edge_list_io.html#io_text_formats) |  | · |  |  |  |
|  | [KONECT read and write](measures/input-and-output/text_edge_list_io.html#io_konect) |  |  |  | · |  |
|  | [LGL read and write](measures/input-and-output/text_edge_list_io.html#io_lgl) |  |  | · |  |  |
|  | [METIS read and write](measures/input-and-output/text_edge_list_io.html#io_metis) |  |  |  | · |  |
|  | [NCOL read and write](measures/input-and-output/text_edge_list_io.html#io_ncol) |  |  | · |  |  |
|  | [SNAP read and write](measures/input-and-output/text_edge_list_io.html#io_snap) |  |  |  | · |  |

### Graph description formats

14 measures in 1 concepts.

| Concept | Variant | networkx | igraph | pyigraph | networkit | rustworkx | jgrapht | gephi |
|---|---|---|---|---|---|---|---|---|
| [Graph description and exchange formats](measures/input-and-output/graph_markup_io.html) | [DIMACS read and write](measures/input-and-output/graph_markup_io.html#io_dimacs) |  |  | · |  |  | · |  |
|  | [GEXF read and write](measures/input-and-output/graph_markup_io.html#io_gexf) | ✓ |  |  | · |  | · | · |
|  | [GML read and write](measures/input-and-output/graph_markup_io.html#io_gml) | ✓ | · | · | · |  | · |  |
|  | [GRAPH6 read and write](measures/input-and-output/graph_markup_io.html#io_graph6) | · |  |  |  |  | · |  |
|  | [GRAPHDB read and write](measures/input-and-output/graph_markup_io.html#io_graphdb) |  |  | · |  |  |  |  |
|  | [GraphML read and write](measures/input-and-output/graph_markup_io.html#io_graphml) | ✓ | · | · | · | · | · |  |
|  | [GRAPHVIZ read and write](measures/input-and-output/graph_markup_io.html#io_graphviz) |  |  | · | · |  | · |  |
|  | [LEDA read and write](measures/input-and-output/graph_markup_io.html#io_leda) | · |  | · |  |  |  |  |
|  | [LEMON read and write](measures/input-and-output/graph_markup_io.html#io_lemon) |  |  |  |  |  | · |  |
|  | [Node-link JSON read and write](measures/input-and-output/graph_markup_io.html#io_json) | ✓ |  |  |  |  | · |  |
|  | [NODELINKJSON read and write](measures/input-and-output/graph_markup_io.html#io_nodelinkjson) |  |  |  |  | · |  |  |
|  | [Pajek .net read and write](measures/input-and-output/graph_markup_io.html#io_pajek) | ✓ | · | · |  |  |  |  |
|  | [SVG read and write](measures/input-and-output/graph_markup_io.html#io_svg) |  |  | · |  |  |  |  |
|  | [TSPLIB read and write](measures/input-and-output/graph_markup_io.html#io_tsplib) |  |  |  |  |  | · |  |

### Matrix and spreadsheet formats

9 measures in 1 concepts.

| Concept | Variant | pyigraph | networkit | rustworkx | jgrapht | ucinet |
|---|---|---|---|---|---|---|
| [Matrix and spreadsheet formats](measures/input-and-output/matrix_file_io.html) | [Excel (xlsx) reader and writer](measures/input-and-output/matrix_file_io.html#io_xlsx) |  |  |  |  | · |
|  | [MATLAB read and write](measures/input-and-output/matrix_file_io.html#io_matlab) |  | · |  |  |  |
|  | [MATRIX read and write](measures/input-and-output/matrix_file_io.html#io_matrix) |  |  |  | · |  |
|  | [MATRIXMARKET read and write](measures/input-and-output/matrix_file_io.html#io_matrixmarket) |  |  | · |  |  |
|  | [MTX read and write](measures/input-and-output/matrix_file_io.html#io_mtx) |  | · |  |  |  |
|  | [Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA](measures/input-and-output/matrix_file_io.html#io_ucinet_multi) |  |  |  |  | · |
|  | [RB read and write](measures/input-and-output/matrix_file_io.html#io_rb) |  | · |  |  |  |
|  | [UCINET binary dataset reader (.##h / .##d)](measures/input-and-output/matrix_file_io.html#io_ucinet_binary) |  |  |  |  | · |
|  | [UCINET DL text read and write](measures/input-and-output/matrix_file_io.html#io_dl) | · |  |  |  | · |

### Partition and cover formats

5 measures in 1 concepts.

| Concept | Variant | networkit |
|---|---|---|
| [Partition and cover file formats](measures/input-and-output/partition_cover_io.html) | [BINARYEDGELISTPARTITION read and write](measures/input-and-output/partition_cover_io.html#io_binaryedgelistpartition) | · |
|  | [BINARYPARTITION read and write](measures/input-and-output/partition_cover_io.html#io_binarypartition) | · |
|  | [EDGELISTCOVER read and write](measures/input-and-output/partition_cover_io.html#io_edgelistcover) | · |
|  | [EDGELISTPARTITION read and write](measures/input-and-output/partition_cover_io.html#io_edgelistpartition) | · |
|  | [SNAPEDGELISTPARTITION read and write](measures/input-and-output/partition_cover_io.html#io_snapedgelistpartition) | · |

## Layout

52 measures in 14 concepts.

### Embeddings

13 measures in 5 concepts.

| Concept | Variant | pyigraph | networkit | sknetwork | graphlayouts | deepwalk |
|---|---|---|---|---|---|---|
| [Louvain embedding](measures/layout/louvain_embedding.html) | [Louvain Embedding](measures/layout/louvain_embedding.html#cat_embedding_louvain) |  |  | · |  |  |
| [Node2vec](measures/layout/node2vec.html) | [Node2 Vec](measures/layout/node2vec.html#cat_node2_vec) |  | · |  |  |  |
| [Spectral embedding and clustering](measures/layout/spectral_embedding.html) | [Spectral](measures/layout/spectral_embedding.html#cat_spectral) |  |  | · |  |  |
| [UMAP weights and layout](measures/layout/umap_weights.html) | [Layout umap](measures/layout/umap_weights.html#cat_layout_umap) |  |  |  | · |  |
|  | [Umap compute weights](measures/layout/umap_weights.html#cat_umap_weights) | · |  |  |  |  |
| [Walk corpora and skip-gram embeddings (DeepWalk)](measures/layout/walk_embeddings.html) | [Walk corpora and skip-gram embeddings (DeepWalk)](measures/layout/walk_embeddings.html#walk_embeddings) |  |  |  |  | · |
|  | [Adjlist input](measures/layout/walk_embeddings.html#cat_adjlist_input) |  |  |  |  | · |
|  | [Deepwalk](measures/layout/walk_embeddings.html#cat_deepwalk) |  |  |  |  | · |
|  | [Edgelist input](measures/layout/walk_embeddings.html#cat_edgelist_input) |  |  |  |  | · |
|  | [Mat input](measures/layout/walk_embeddings.html#cat_input_mat) |  |  |  |  | · |
|  | [Random walk corpus](measures/layout/walk_embeddings.html#cat_corpus_random_walk) |  |  |  |  | · |
|  | [Skip-gram embedding](measures/layout/walk_embeddings.html#cat_embedding_gram_skip) |  |  |  |  | · |
|  | [Word2vec output](measures/layout/walk_embeddings.html#cat_output_word2vec) |  |  |  |  | · |

### Layout algorithms

39 measures in 9 concepts.

| Concept | Variant | networkx | igraph | pyigraph | networkit | rustworkx | sknetwork | jgrapht | boost | graphlayouts |
|---|---|---|---|---|---|---|---|---|---|---|
| [Backbone, focus and centrality layouts](measures/layout/centrality_focus_layout.html) | [Backbone, focus and centrality (concentric) layouts](measures/layout/centrality_focus_layout.html#layout_focus_backbone) |  |  |  |  |  |  |  |  | · |
|  | [Layout backbone](measures/layout/centrality_focus_layout.html#cat_backbone_layout) |  |  |  |  |  |  |  |  | · |
|  | [Layout centrality](measures/layout/centrality_focus_layout.html#cat_layout) |  |  |  |  |  |  |  |  | · |
|  | [Layout centrality group](measures/layout/centrality_focus_layout.html#cat_group_layout) |  |  |  |  |  |  |  |  | · |
|  | [Layout focus](measures/layout/centrality_focus_layout.html#cat_focus_layout) |  |  |  |  |  |  |  |  | · |
|  | [Layout focus group](measures/layout/centrality_focus_layout.html#cat_focus_group_layout) |  |  |  |  |  |  |  |  | · |
| [Dynamic layout](measures/layout/dynamic_layout.html) | [Layout dynamic](measures/layout/dynamic_layout.html#cat_dynamic_layout) |  |  |  |  |  |  |  |  | · |
| [Force-directed layouts](measures/layout/force_directed_layout.html) | [Davidson-Harel layout](measures/layout/force_directed_layout.html#layout_dh) |  | · | · |  |  |  |  |  |  |
|  | [DrL (OpenOrd) layout](measures/layout/force_directed_layout.html#layout_drl) |  | · | · |  |  |  |  |  |  |
|  | [Fruchterman-Reingold layout](measures/layout/force_directed_layout.html#layout_fruchterman_reingold) | · | · | · |  | · | · |  | · |  |
|  | [GEM layout](measures/layout/force_directed_layout.html#layout_gem) |  | · |  |  |  |  |  |  |  |
|  | [Graphopt layout](measures/layout/force_directed_layout.html#layout_graphopt) |  | · | · |  |  |  |  |  |  |
|  | [Gursoy atun layout](measures/layout/force_directed_layout.html#cat_atun_gursoy_layout) |  |  |  |  |  |  |  | · |  |
|  | [Kamada-Kawai layout](measures/layout/force_directed_layout.html#layout_kamada_kawai) |  | · | · |  | · |  |  | · |  |
|  | [Large graph layout (LGL)](measures/layout/force_directed_layout.html#layout_lgl) |  | · | · |  |  |  |  |  |  |
|  | [Layout multilevel](measures/layout/force_directed_layout.html#cat_layout_multilevel) |  |  |  |  |  |  |  |  | · |
|  | [Spring](measures/layout/force_directed_layout.html#cat_spring) |  |  |  |  |  | · |  |  |  |
| [Grid, random, circle and sphere layouts](measures/layout/geometric_layout.html) | [Circle, tree and two-mode (barycenter) layouts](measures/layout/geometric_layout.html#layout_simple) | · | · | · |  | · |  |  | · |  |
|  | [Grid layout](measures/layout/geometric_layout.html#layout_grid) |  | · |  |  |  |  |  |  |  |
|  | [Random layout](measures/layout/geometric_layout.html#layout_random) |  | · |  |  | · |  |  | · |  |
|  | [Sphere layout](measures/layout/geometric_layout.html#layout_sphere) |  | · |  |  |  |  |  |  |  |
| [Layered and tree layouts](measures/layout/layered_layout.html) | [Barycenter Greedy Two Layered Bipartite Layout2 D](measures/layout/layered_layout.html#cat_barycenter_bipartite_d_greedy_layered_layout2_two) |  |  |  |  |  |  | · |  |  |
|  | [Layout tree unrooted](measures/layout/layered_layout.html#cat_layout_tree_unrooted) |  |  |  |  |  |  |  |  | · |
|  | [Median Greedy Two Layered Bipartite Layout2 D](measures/layout/layered_layout.html#cat_bipartite_d_greedy_layered_layout2_median_two) |  |  |  |  |  |  | · |  |  |
|  | [Sugiyama layered layout](measures/layout/layered_layout.html#layout_sugiyama) |  | · | · |  |  |  |  |  |  |
|  | [Two Layered Bipartite Layout2 D](measures/layout/layered_layout.html#cat_bipartite_d_layered_layout2_two) |  |  |  |  |  |  | · |  |  |
| [Metro-map layout](measures/layout/metromap_layout.html) | [Layout as metromap](measures/layout/metromap_layout.html#cat_as_layout_metromap) |  |  |  |  |  |  |  |  | · |
| [Pivot MDS layout](measures/layout/pivot_mds_layout.html) | [Layout pmds](measures/layout/pivot_mds_layout.html#cat_layout_pmds) |  |  |  |  |  |  |  |  | · |
|  | [Pivot MDS](measures/layout/pivot_mds_layout.html#cat_mds_pivot) |  |  |  | · |  |  |  |  |  |
| [Spectral and MDS layouts](measures/layout/spectral_mds_layout.html) | [Layout spectral](measures/layout/spectral_mds_layout.html#cat_layout_spectral) |  |  |  |  |  |  |  |  | · |
|  | [Multidimensional scaling layout](measures/layout/spectral_mds_layout.html#layout_mds) |  | · | · |  |  |  |  |  |  |
| [Stress-based layouts](measures/layout/stress_layout.html) | [Layout constrained stress](measures/layout/stress_layout.html#cat_constrained_layout_stress) |  |  |  |  |  |  |  |  | · |
|  | [Layout constrained stress3 D](measures/layout/stress_layout.html#cat_constrained_d_layout_stress3) |  |  |  |  |  |  |  |  | · |
|  | [Layout stress quality](measures/layout/stress_layout.html#layout_stress_quality) | ∅ |  |  |  |  |  |  |  |  |
|  | [Layout stress value](measures/layout/stress_layout.html#layout_stress_value) | ∅ |  |  |  |  |  |  |  |  |
|  | [Layout stress3 D](measures/layout/stress_layout.html#cat_d_layout_stress3) |  |  |  |  |  |  |  |  | · |
|  | [Maxent Stress](measures/layout/stress_layout.html#cat_maxent_stress) |  |  |  | · |  |  |  |  |  |
|  | [Sparse stress / pivot MDS layout](measures/layout/stress_layout.html#layout_sparse_stress) |  |  |  |  |  |  |  |  | · |
|  | [Stress-majorization layout (Kamada-Kawai energy)](measures/layout/stress_layout.html#layout_stress) | ✓ |  |  |  |  |  |  |  | · |

## Matrices and spectra

17 measures in 16 concepts.

### Graph matrices

11 measures in 10 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | sknetwork | boost | ucinet | centiserve | graspologic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Adjacency matrix](measures/matrices-and-spectra/adjacency_matrix.html) | [Adjacency](measures/matrices-and-spectra/adjacency_matrix.html#gm_adjacency) | ✓ | · | · | · | · | · |  |  |  |  |  |
| [Bethe Hessian](measures/matrices-and-spectra/bethe_hessian.html) | [Bethe hessian](measures/matrices-and-spectra/bethe_hessian.html#gm_bethe_hessian) | ✓ |  |  |  |  |  |  |  |  |  |  |
| [Class matrix](measures/matrices-and-spectra/class_matrix.html) | [Class matrix](measures/matrices-and-spectra/class_matrix.html#gm_class_matrix) | ✓ |  |  |  |  |  |  |  |  |  |  |
| [Graph matrix operators](measures/matrices-and-spectra/matrix_operators.html) | [Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence)](measures/matrices-and-spectra/matrix_operators.html#matrix_operators) |  |  |  | · |  |  |  |  | · |  |  |
| [Incidence matrix](measures/matrices-and-spectra/incidence_matrix.html) | [Incidence](measures/matrices-and-spectra/incidence_matrix.html#gm_incidence) | ✓ | · | · | · |  |  |  |  | · |  |  |
| [Laplacian matrix](measures/matrices-and-spectra/laplacian_matrix.html) | [Gm laplacian](measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian) | ✓ | · | · | · | · |  | · |  |  | · | ≠ |
|  | [Magnetic laplacian matrix](measures/matrices-and-spectra/laplacian_matrix.html#cat_laplacian_magnetic_matrix) | · |  |  |  |  |  |  |  |  |  |  |
| [Modularity matrix](measures/matrices-and-spectra/modularity_matrix.html) | [Gm modularity](measures/matrices-and-spectra/modularity_matrix.html#gm_modularity) | ✓ | · | · | · |  |  |  |  |  |  |  |
| [Sparse-matrix orderings and bandwidth](measures/matrices-and-spectra/matrix_bandwidth.html) | [Sparse-matrix orderings and bandwidth/wavefront](measures/matrices-and-spectra/matrix_bandwidth.html#matrix_bandwidth) |  |  |  |  |  |  |  | · |  |  |  |
| [Stochastic matrix](measures/matrices-and-spectra/stochastic_matrix.html) | [Stochastic matrix](measures/matrices-and-spectra/stochastic_matrix.html#cat_matrix_stochastic) |  | · |  |  |  |  |  |  |  |  |  |
| [Tournament matrix](measures/matrices-and-spectra/tournament_matrix.html) | [Tournament matrix](measures/matrices-and-spectra/tournament_matrix.html#cat_matrix_tournament) | · |  |  |  |  |  |  |  |  |  |  |

### Spectra

6 measures in 6 concepts.

| Concept | Variant | networkx | igraph | pyigraph | networkit | netrankr |
|---|---|---|---|---|---|---|
| [Eigenvectors of graph matrices](measures/matrices-and-spectra/eigenvectors_matrix.html) | [Eigenvectors of graph matrices](measures/matrices-and-spectra/eigenvectors_matrix.html#eigenvectors_matrix) |  |  |  | · |  |
| [Estrada index](measures/matrices-and-spectra/estrada_index.html) | [Estrada index](measures/matrices-and-spectra/estrada_index.html#estrada_index) | · |  |  |  |  |
| [Fiedler value and vector](measures/matrices-and-spectra/fiedler.html) | [Fiedler](measures/matrices-and-spectra/fiedler.html#gm_fiedler) | ≠ |  |  |  |  |
| [Graph spectrum](measures/matrices-and-spectra/graph_spectrum.html) | [Graph spectrum (eigenvalues of a graph matrix)](measures/matrices-and-spectra/graph_spectrum.html#graph_spectrum) | · | · | · |  |  |
| [Spectral gap](measures/matrices-and-spectra/spectral_gap.html) | [Spectral gap](measures/matrices-and-spectra/spectral_gap.html#cat_gap_spectral) |  |  |  |  | · |
| [Spectral ordering](measures/matrices-and-spectra/spectral_ordering.html) | [Spectral ordering](measures/matrices-and-spectra/spectral_ordering.html#cat_ordering_spectral) | · |  |  |  |  |

## Mixing and assortativity

22 measures in 13 concepts.

### Assortativity

9 measures in 4 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | bct | bctpy | ucinet | netseg |
|---|---|---|---|---|---|---|---|---|---|---|
| [Assortativity coefficient](measures/mixing-and-assortativity/assortativity_coefficient.html) | [Assort](measures/mixing-and-assortativity/assortativity_coefficient.html#assort) | ✓ |  |  |  |  |  | ≠ |  | · |
|  | [Assortativity degree](measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_degree) | ✓ | ∅ | ✓ |  |  | ≠ |  |  |  |
|  | [Assortativity nominal](measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_nominal) | ≠ | ∅ | ✓ |  |  |  |  | · |  |
|  | [Assortativity values](measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_values) | ✓ | ∅ | ✓ | · | · | · |  |  |  |
| [Average neighbor degree and degree connectivity](measures/mixing-and-assortativity/average_neighbor_degree.html) | [Avg deg conn](measures/mixing-and-assortativity/average_neighbor_degree.html#avg_deg_conn) | ≠ |  |  |  |  |  |  |  |  |
|  | [Avg nbr deg](measures/mixing-and-assortativity/average_neighbor_degree.html#avg_nbr_deg) | ≠ |  |  |  |  |  |  |  |  |
|  | [Knn](measures/mixing-and-assortativity/average_neighbor_degree.html#cat_knn) |  | · | · |  |  |  |  |  |  |
| [Degree and property correlation histograms](measures/mixing-and-assortativity/correlation_histograms.html) | [Degree and property correlation histograms](measures/mixing-and-assortativity/correlation_histograms.html#correlation_histograms) |  |  |  | · |  |  |  |  |  |
| [Local assortativity](measures/mixing-and-assortativity/local_assortativity.html) | [Local assortativity](measures/mixing-and-assortativity/local_assortativity.html#cat_assortativity_local) |  |  |  |  |  | · |  |  |  |

### Mixing matrices

3 measures in 1 concepts.

| Concept | Variant | networkx | ucinet |
|---|---|---|---|
| [Mixing matrices](measures/mixing-and-assortativity/mixing_matrix.html) | [Attribute mixing matrix](measures/mixing-and-assortativity/mixing_matrix.html#cat_attribute_matrix_mixing) | · |  |
|  | [Degree mixing matrix](measures/mixing-and-assortativity/mixing_matrix.html#cat_degree_matrix_mixing) | · |  |
|  | [Mixing](measures/mixing-and-assortativity/mixing_matrix.html#mixing) | ✓ | · |

### Rich club

3 measures in 1 concepts.

| Concept | Variant | networkx | bct | tnet |
|---|---|---|---|---|
| [Rich club](measures/mixing-and-assortativity/rich_club.html) | [Rich club](measures/mixing-and-assortativity/rich_club.html#rich_club) | ✓ | · |  |
|  | [Weighted richclub](measures/mixing-and-assortativity/rich_club.html#cat_richclub_weighted) |  |  | · |
|  | [Weighted richclub local](measures/mixing-and-assortativity/rich_club.html#cat_local_richclub_weighted) |  |  | · |

### Segregation and homophily indices

7 measures in 7 concepts.

| Concept | Variant | ucinet | egor | netseg |
|---|---|---|---|---|
| [Coleman homophily index](measures/mixing-and-assortativity/coleman_homophily.html) | [Coleman](measures/mixing-and-assortativity/coleman_homophily.html#cat_coleman) |  |  | · |
| [E-I index](measures/mixing-and-assortativity/ei_index.html) | [Ei index](measures/mixing-and-assortativity/ei_index.html#ei_index) | · | ≠ | · |
| [Freeman segregation index](measures/mixing-and-assortativity/freeman_segregation.html) | [Freeman's segregation index](measures/mixing-and-assortativity/freeman_segregation.html#seg_freeman) |  |  | · |
| [Gupta-Anderson-May mixing coefficient](measures/mixing-and-assortativity/gupta_anderson_may.html) | [Gupta-Anderson-May mixing coefficient](measures/mixing-and-assortativity/gupta_anderson_may.html#seg_gamix) |  |  | · |
| [Odds ratio of within-group ties](measures/mixing-and-assortativity/orwg.html) | [Odds ratio of within-group ties (ORWG)](measures/mixing-and-assortativity/orwg.html#seg_orwg) |  |  | · |
| [Segregation matrix index](measures/mixing-and-assortativity/segregation_matrix_index.html) | [Segregation matrix index (SMI)](measures/mixing-and-assortativity/segregation_matrix_index.html#seg_smi) |  |  | · |
| [Spectral segregation index](measures/mixing-and-assortativity/spectral_segregation_index.html) | [Spectral segregation index (SSI)](measures/mixing-and-assortativity/spectral_segregation_index.html#seg_ssi) |  |  | · |

## Paths and distances

65 measures in 39 concepts.

### Distance summaries

18 measures in 16 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | jgrapht | boost | bct | bctpy | gephi | ucinet | centiserve |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Barycenter](measures/paths-and-distances/barycenter.html) | [Barycenter](measures/paths-and-distances/barycenter.html#dm_barycenter) | ✓ |  |  |  |  |  |  |  |  |  |  |  | · |
| [Closeness vitality](measures/paths-and-distances/closeness_vitality.html) | [Closeness vitality](measures/paths-and-distances/closeness_vitality.html#dm_closeness_vitality) | ✓ |  |  |  |  |  |  |  |  |  |  |  | · |
| [Diameter](measures/paths-and-distances/diameter.html) | [Diameter](measures/paths-and-distances/diameter.html#diameter) | ✓ | ✓ | ✓ | · | ∅ |  | ≠ | ≠ | ≠ | ✓ | ✓ | · |  |
| [Distance histogram](measures/paths-and-distances/distance_histogram.html) | [Distance histogram](measures/paths-and-distances/distance_histogram.html#cat_distance_histogram) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Eccentricity](measures/paths-and-distances/eccentricity.html) | [Eccentricity](measures/paths-and-distances/eccentricity.html#eccentricity) | ✓ | ✓ | ✓ |  | ∅ |  | ≠ | ≠ | ≠ | ✓ | ✓ | · |  |
| [Graph center](measures/paths-and-distances/graph_center.html) | [Center](measures/paths-and-distances/graph_center.html#dm_center) | ✓ | · |  |  |  |  |  |  |  |  |  |  |  |
| [Graph periphery](measures/paths-and-distances/graph_periphery.html) | [Periphery](measures/paths-and-distances/graph_periphery.html#dm_periphery) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy routing and navigation](measures/paths-and-distances/greedy_routing.html) | [Hyperbolic greedy routing](measures/paths-and-distances/greedy_routing.html#cat_greedy_hyperbolic_routing) |  |  |  |  |  | · |  |  |  |  |  |  |  |
|  | [Hyperbolic greedy success rate](measures/paths-and-distances/greedy_routing.html#cat_greedy_hyperbolic_rate_success) |  |  |  |  |  | · |  |  |  |  |  |  |  |
|  | [Navigation](measures/paths-and-distances/greedy_routing.html#cat_navigation) |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Mean distance](measures/paths-and-distances/mean_distance.html) | [Mean distance](measures/paths-and-distances/mean_distance.html#mean_distance) | ✓ | ✓ | ✓ |  |  | · |  |  |  | ✓ | ✓ | · |  |
| [Mean first passage time](measures/paths-and-distances/mean_first_passage_time.html) | [Mean first passage time](measures/paths-and-distances/mean_first_passage_time.html#cat_first_mean_passage_time) |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Neighborhood function and effective diameter](measures/paths-and-distances/neighborhood_function.html) | [Neighborhood function, hop plot, effective diameter](measures/paths-and-distances/neighborhood_function.html#neighborhood_function) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Path transitivity](measures/paths-and-distances/path_transitivity.html) | [Path transitivity](measures/paths-and-distances/path_transitivity.html#cat_path_transitivity) |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Radius](measures/paths-and-distances/radius.html) | [Radius](measures/paths-and-distances/radius.html#radius) | · | ✓ | ✓ |  |  |  | ≠ | ≠ | ≠ | ✓ | ✓ |  |  |
| [Search information](measures/paths-and-distances/search_information.html) | [Search information](measures/paths-and-distances/search_information.html#cat_information_search) |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Social proximity](measures/paths-and-distances/social_proximity.html) | [Socialprox](measures/paths-and-distances/social_proximity.html#cat_socialprox) |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Wiener index](measures/paths-and-distances/wiener_index.html) | [Index](measures/paths-and-distances/wiener_index.html#dm_index) | ✓ |  |  |  |  |  |  |  | ≠ | ✓ |  |  |  |

### Efficiency and reachability

6 measures in 3 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | networkit | rustworkx | bct | bctpy | ucinet | netrankr |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Global and local efficiency](measures/paths-and-distances/global_efficiency.html) | [Global and local efficiency](measures/paths-and-distances/global_efficiency.html#efficiency_global) | · | · |  | · |  |  | · |  |  |  |
|  | [Swan efficiency](measures/paths-and-distances/global_efficiency.html#cat_efficiency_swan) |  |  |  |  |  |  |  |  |  | · |
| [Local efficiency](measures/paths-and-distances/local_efficiency.html) | [Local efficiency](measures/paths-and-distances/local_efficiency.html#dm_local_efficiency) | ✓ |  |  |  |  |  | ≠ | ≠ |  |  |
| [Reachability](measures/paths-and-distances/reachability.html) | [Reachability](measures/paths-and-distances/reachability.html#reachability) | ✓ | ✓ | ✓ |  |  | · |  |  | · |  |
|  | [Reachable Nodes](measures/paths-and-distances/reachability.html#cat_reachable) |  |  |  |  | · |  |  |  |  |  |
|  | [Reachdist](measures/paths-and-distances/reachability.html#cat_reachdist) |  |  |  |  |  |  | · |  |  |  |

### Geometry

3 measures in 3 concepts.

| Concept | Variant | ucinet | s2 | sf |
|---|---|---|---|---|
| [Edge lengths (geometry)](measures/paths-and-distances/edge_lengths.html) | [Edge lengths](measures/paths-and-distances/edge_lengths.html#edge_lengths) |  | ✓ | ✓ |
| [Group geometry](measures/paths-and-distances/group_geometry.html) | [Group geometry](measures/paths-and-distances/group_geometry.html#group_geometry) |  | ✓ | ✓ |
| [Proximity](measures/paths-and-distances/proximity.html) | [Proximity](measures/paths-and-distances/proximity.html#proximity) | · | ✓ | ✓ |

### Path enumeration and counting

11 measures in 8 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | jgrapht | boost | bct | ucinet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [All paths](measures/paths-and-distances/all_paths.html) | [All Directed Paths](measures/paths-and-distances/all_paths.html#cat_all_directed_path) |  |  |  |  |  |  |  | · |  |  |  |
|  | [Allpaths](measures/paths-and-distances/all_paths.html#cat_allpaths) |  |  |  |  |  |  |  |  |  |  | · |
|  | [Paths simple](measures/paths-and-distances/all_paths.html#paths_simple) | ✓ | · | · |  | · | · | · |  |  |  |  |
| [Bounded path and walk search](measures/paths-and-distances/bounded_path_search.html) | [Findpaths](measures/paths-and-distances/bounded_path_search.html#cat_findpaths) |  |  |  |  |  |  |  |  |  | · |  |
|  | [Findwalks](measures/paths-and-distances/bounded_path_search.html#cat_findwalks) |  |  |  |  |  |  |  |  |  | · |  |
| [Complex paths](measures/paths-and-distances/complex_paths.html) | [Complex Paths](measures/paths-and-distances/complex_paths.html#cat_complex_path) |  |  |  |  |  | · |  |  |  |  |  |
| [K-path census](measures/paths-and-distances/path_census.html) | [Kpath census](measures/paths-and-distances/path_census.html#cat_census_kpath) |  |  |  | · |  |  |  |  |  |  |  |
| [Longest simple path](measures/paths-and-distances/longest_simple_path.html) | [Longest simple path](measures/paths-and-distances/longest_simple_path.html#paths_longest_simple) |  |  |  |  |  |  | · |  |  |  |  |
| [Minimum and maximum cycle ratio](measures/paths-and-distances/cycle_ratio.html) | [Minimum/maximum cycle ratio and mean cycle](measures/paths-and-distances/cycle_ratio.html#cycle_ratio) |  |  |  |  |  |  |  | · | · |  |  |
| [Path counting in DAGs](measures/paths-and-distances/dag_path_count.html) | [Dag All Paths Counter](measures/paths-and-distances/dag_path_count.html#cat_all_counter_dag_path) |  |  |  |  |  |  |  | · |  |  |  |
| [Path counts](measures/paths-and-distances/path_counts.html) | [Paths count](measures/paths-and-distances/path_counts.html#paths_count) | ✓ |  |  |  | · |  |  |  |  |  |  |

### Resistance and spectral distances

4 measures in 2 concepts.

| Concept | Variant | networkx | networkit | netrankr |
|---|---|---|---|---|
| [Kemeny constant](measures/paths-and-distances/kemeny_constant.html) | [Kemeny](measures/paths-and-distances/kemeny_constant.html#cx_kemeny) | ✓ |  |  |
| [Resistance distance and effective resistance](measures/paths-and-distances/resistance_distance.html) | [Effective resistance](measures/paths-and-distances/resistance_distance.html#cx_effective_resistance) | ✓ |  |  |
|  | [Resistance](measures/paths-and-distances/resistance_distance.html#cx_resistance) | ✓ |  | ✓ |
|  | [Resistance-based and spectral edge/vertex scores](measures/paths-and-distances/resistance_distance.html#resistance_based) |  | · |  |

### Shortest paths

23 measures in 7 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | graphblas | bct | bctpy | gephi | ucinet | tnet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [All shortest paths](measures/paths-and-distances/all_shortest_paths.html) | [Paths all shortest](measures/paths-and-distances/all_shortest_paths.html#paths_all_shortest) | ✓ | · | · |  | · |  | · |  |  |  |  |  |  |  |  |  |
| [Geodesic distances](measures/paths-and-distances/geodesic_distances.html) | [Distances](measures/paths-and-distances/geodesic_distances.html#distances) | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | · |
|  | [Fw tree](measures/paths-and-distances/geodesic_distances.html#nxs_fw_tree) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Johnson lengths](measures/paths-and-distances/geodesic_distances.html#nxs_johnson_lengths) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Paths all pairs](measures/paths-and-distances/geodesic_distances.html#paths_all_pairs) | ✓ | · |  |  |  | · | · |  |  |  |  |  |  |  |  |  |
|  | [Paths floyd warshall](measures/paths-and-distances/geodesic_distances.html#paths_floyd_warshall) | ✓ |  |  |  |  |  | · |  | · | · |  |  |  |  |  |  |
|  | [Paths johnson](measures/paths-and-distances/geodesic_distances.html#paths_johnson) | ✓ |  |  |  |  |  |  |  | · | · |  |  |  |  |  |  |
| [K shortest paths](measures/paths-and-distances/k_shortest_paths.html) | [Paths k shortest](measures/paths-and-distances/k_shortest_paths.html#paths_k_shortest) | ✓ | · | · |  |  |  | · |  | · |  |  |  |  |  |  |  |
| [Many-to-many and hierarchy-based shortest paths](measures/paths-and-distances/hierarchical_shortest_paths.html) | [Many-to-many and hierarchy-based shortest paths](measures/paths-and-distances/hierarchical_shortest_paths.html#paths_hierarchy) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Negative cycle detection](measures/paths-and-distances/negative_cycle.html) | [Paths negative cycle](measures/paths-and-distances/negative_cycle.html#paths_negative_cycle) | ✓ |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Resource-constrained shortest path](measures/paths-and-distances/resource_constrained_shortest_path.html) | [R c shortest paths](measures/paths-and-distances/resource_constrained_shortest_path.html#cat_c_path_r_shortest) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional)](measures/paths-and-distances/shortest_paths.html) | [Astar](measures/paths-and-distances/shortest_paths.html#ord_astar) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Bellman ford](measures/paths-and-distances/shortest_paths.html#ord_bellman_ford) | ✓ |  |  |  | · |  | · |  | · | · |  |  |  |  |  |  |
|  | [Bidir bfs](measures/paths-and-distances/shortest_paths.html#ord_bidir_bfs) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Bidir dijkstra](measures/paths-and-distances/shortest_paths.html#ord_bidir_dijkstra) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Dijkstra](measures/paths-and-distances/shortest_paths.html#ord_dijkstra) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Paths astar](measures/paths-and-distances/shortest_paths.html#paths_astar) | ✓ |  | · |  | · | · | · |  | · | · |  |  |  |  |  |  |
|  | [Paths bidirectional](measures/paths-and-distances/shortest_paths.html#paths_bidirectional) | ✓ |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
|  | [Paths multi source](measures/paths-and-distances/shortest_paths.html#paths_multi_source) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Paths negative](measures/paths-and-distances/shortest_paths.html#paths_negative) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Paths predecessors](measures/paths-and-distances/shortest_paths.html#paths_predecessors) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [Paths sssp](measures/paths-and-distances/shortest_paths.html#paths_sssp) | ✓ | · | · |  | · | · | · | · | · | · |  |  |  |  |  |  |
|  | [Retrieve shortest path](measures/paths-and-distances/shortest_paths.html#cat_path_retrieve_shortest) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |

## Roles and positions

34 measures in 26 concepts.

### Blockmodels

6 measures in 6 concepts.

| Concept | Variant | sna | graphtool | ucinet | blockmodeling |
|---|---|---|---|---|---|
| [Block density](measures/roles-and-positions/block_density.html) | [Block density](measures/roles-and-positions/block_density.html#block_density) | ✓ |  | · | ✓ |
| [Blockmodel criterion function](measures/roles-and-positions/blockmodel_criterion.html) | [Crit Fun C](measures/roles-and-positions/blockmodel_criterion.html#cat_c_crit_fun) |  |  |  | · |
| [Blockmodel from a partition](measures/roles-and-positions/blockmodel_from_partition.html) | [Block (blockmodel from partition), Reduce](measures/roles-and-positions/blockmodel_from_partition.html#cat_block_blockmodel_from_partition_reduce) |  |  | · |  |
| [CONCOR](measures/roles-and-positions/concor.html) | [Concor](measures/roles-and-positions/concor.html#concor) |  |  | · |  |
| [Direct blockmodel search](measures/roles-and-positions/blockmodel_search.html) | [Direct blockmodel search (structural, regular, generalised block types)](measures/roles-and-positions/blockmodel_search.html#blockmodel_search) |  |  | · | · |
| [Nested blockmodel description length](measures/roles-and-positions/blockmodel_description_length.html) | [Minimize nested blockmodel dl](measures/roles-and-positions/blockmodel_description_length.html#cat_blockmodel_dl_minimize_nested) |  | · |  |  |

### Core-periphery

3 measures in 2 concepts.

| Concept | Variant | bct | ucinet | cpnet |
|---|---|---|---|---|
| [Core-periphery (continuous)](measures/roles-and-positions/core_periphery_continuous.html) | [Core periphery continuous](measures/roles-and-positions/core_periphery_continuous.html#core_periphery_continuous) |  | · | ✓ |
| [Core-periphery (discrete)](measures/roles-and-positions/core_periphery.html) | [Core periphery](measures/roles-and-positions/core_periphery.html#core_periphery) | · | · | ✓ |
|  | [Estevez-Nordlund variant](measures/roles-and-positions/core_periphery.html#core_periphery_en) |  | · |  |

### Equivalence and clustering

8 measures in 4 concepts.

| Concept | Variant | sna | ucinet | blockmodeling | nauty |
|---|---|---|---|---|---|
| [Automorphic equivalence](measures/roles-and-positions/automorphic_equivalence.html) | [Automorphic equivalence](measures/roles-and-positions/automorphic_equivalence.html#automorphic_equivalence) |  | · |  | ✓ |
| [Equivalence clustering](measures/roles-and-positions/equivalence_clustering.html) | [Equiv clust](measures/roles-and-positions/equivalence_clustering.html#cat_clust_equiv) | · |  |  |  |
|  | [Hiclus](measures/roles-and-positions/equivalence_clustering.html#cat_hiclus) |  | · |  |  |
| [Regular equivalence (REGE, CATREGE)](measures/roles-and-positions/regular_equivalence.html) | [Regular equivalence](measures/roles-and-positions/regular_equivalence.html#regular_equivalence) | ✓ | · | · |  |
|  | [Automorphic (Max Sim) and regular equivalence (REGE, CATREGE)](measures/roles-and-positions/regular_equivalence.html#cat_automorphic_catrege_equivalence_max_rege_regular_sim) |  | · |  |  |
| [Structural equivalence](measures/roles-and-positions/structural_equivalence.html) | [Structural equivalence](measures/roles-and-positions/structural_equivalence.html#structural_equivalence) | ✓ | · | ≠ |  |
|  | [Equivalence measures: matches, positive matches, overlaps, cross-products, coverage](measures/roles-and-positions/structural_equivalence.html#equivalence_extra) |  | · |  |  |
|  | [Structural equivalence: profile (correlation, Euclidean, etc ), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row](measures/roles-and-positions/structural_equivalence.html#cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural) |  | · |  |  |

### Module-based roles

5 measures in 4 concepts.

| Concept | Variant | bct |
|---|---|---|
| [Diversity coefficient](measures/roles-and-positions/diversity_coefficient.html) | [Diversity coef](measures/roles-and-positions/diversity_coefficient.html#cat_coef_diversity) | · |
| [Gateway coefficient](measures/roles-and-positions/gateway_coefficient.html) | [Gateway coef](measures/roles-and-positions/gateway_coefficient.html#cat_coef_gateway) | · |
| [Module degree z-score](measures/roles-and-positions/module_degree_zscore.html) | [Module degree zscore](measures/roles-and-positions/module_degree_zscore.html#cat_degree_module_zscore) | · |
| [Participation coefficient](measures/roles-and-positions/participation_coefficient.html) | [Participation coef](measures/roles-and-positions/participation_coefficient.html#cat_coef_participation) | · |
|  | [Participation coef sparse](measures/roles-and-positions/participation_coefficient.html#cat_coef_participation_sparse) | · |

### Scaling and clustering

4 measures in 3 concepts.

| Concept | Variant | sna | ucinet |
|---|---|---|---|
| [Cognitive social structures with accuracy](measures/roles-and-positions/css_accuracy.html) | [Cognitive social structures with accuracy measures](measures/roles-and-positions/css_accuracy.html#css_accuracy) | · | · |
| [Guttman scaling, K-means and quick clustering](measures/roles-and-positions/guttman_kmeans.html) | [Guttman scaling, K-means and quick clustering](measures/roles-and-positions/guttman_kmeans.html#guttman_kmeans) |  | · |
| [Multidimensional scaling](measures/roles-and-positions/multidimensional_scaling.html) | [Classical mds](measures/roles-and-positions/multidimensional_scaling.html#classical_mds) |  | · |
|  | [Non-metric MDS with stress-1](measures/roles-and-positions/multidimensional_scaling.html#mds_nonmetric) |  | · |

### Structural holes and brokerage

8 measures in 7 concepts.

| Concept | Variant | networkx | igraph | pyigraph | sna | ucinet | manynet |
|---|---|---|---|---|---|---|---|
| [Brokerage](measures/roles-and-positions/brokerage.html) | [Brokerage](measures/roles-and-positions/brokerage.html#brokerage) |  |  |  | ✓ | · |  |
| [Burt constraint](measures/roles-and-positions/burt_constraint.html) | [Constraint](measures/roles-and-positions/burt_constraint.html#constraint) | ≠ | ✓ | ✓ |  | · | ✓ |
| [Burt efficiency](measures/roles-and-positions/burt_efficiency.html) | [Efficiency](measures/roles-and-positions/burt_efficiency.html#efficiency) | ≠ |  |  |  | · | ≠ |
| [Effective size](measures/roles-and-positions/effective_size.html) | [Effective size](measures/roles-and-positions/effective_size.html#effective_size) | ≠ |  |  |  | · | ≠ |
| [Hierarchy](measures/roles-and-positions/hierarchy_krackhardt.html) | [Hierarchy](measures/roles-and-positions/hierarchy_krackhardt.html#hierarchy) |  | · |  | · | · |  |
| [Node redundancy](measures/roles-and-positions/node_redundancy.html) | [Node redundancy](measures/roles-and-positions/node_redundancy.html#node_redundancy) | ✓ |  |  |  |  |  |
| [Structural holes (Burt)](measures/roles-and-positions/structural_holes.html) | [Dyconst](measures/roles-and-positions/structural_holes.html#cat_dyconst) |  |  |  |  | · |  |
|  | [Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6 798), "corrected constraint" FA](measures/roles-and-positions/structural_holes.html#cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural) |  |  |  |  | · |  |

## Signed and multilayer

3 measures in 3 concepts.

### Multilayer networks

1 measures in 1 concepts.

| Concept | Variant | pymnet | multinet |
|---|---|---|---|
| [Multilayer networks](measures/signed-and-multilayer/multilayer.html) | [Multilayer networks (node-layers, supra-adjacency)](measures/signed-and-multilayer/multilayer.html#multilayer) | · | · |

### Signed networks

2 measures in 2 concepts.

| Concept | Variant | ucinet | signnet |
|---|---|---|---|
| [Positive-negative centrality](measures/signed-and-multilayer/pn_centrality.html) | [Positive-negative centrality (signed ties)](measures/signed-and-multilayer/pn_centrality.html#pn_centrality) | · | · |
| [Structural balance and frustration](measures/signed-and-multilayer/structural_balance.html) | [Structural balance, frustration index, signed blockmodels](measures/signed-and-multilayer/structural_balance.html#signed_balance) |  | · |

## Statistical fitting

505 measures in 80 concepts.

### Block model states

30 measures in 2 concepts.

| Concept | Variant | graphtool |
|---|---|---|
| [Block states for dynamics inference](measures/statistical-fitting/sbm_dynamics_state.html) | [CIsing Glauber Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_c_glauber_ising_state) | · |
|  | [Epidemics Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_epidemics_state) | · |
|  | [Ising Glauber Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_glauber_ising_state) | · |
|  | [Linear Normal Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_linear_normal_state) | · |
|  | [LVBlock State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_lv_state) | · |
|  | [Normal Glauber Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_glauber_normal_state) | · |
|  | [Potts Glauber Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_glauber_potts_state) | · |
|  | [Pseudo CIsing Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_c_ising_pseudo_state) | · |
|  | [Pseudo Ising Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_ising_pseudo_state) | · |
|  | [Pseudo Normal Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_normal_pseudo_state) | · |
|  | [Pseudo Potts Block State](measures/statistical-fitting/sbm_dynamics_state.html#cat_block_potts_pseudo_state) | · |
| [Stochastic block model states](measures/statistical-fitting/sbm_block_state.html) | [Draw Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_draw_state) | · |
|  | [EMBlock State](measures/statistical-fitting/sbm_block_state.html#cat_block_em_state) | · |
|  | [Latent Closure Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_closure_latent_state) | · |
|  | [Latent Mask Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_latent_mask_state) | · |
|  | [Latent Multigraph Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_latent_multigraph_state) | · |
|  | [Layered Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_layered_state) | · |
|  | [Layered Overlap Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_layered_overlap_state) | · |
|  | [Layered Weighted Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_layered_state_weighted) | · |
|  | [Layered Weighted Overlap Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_layered_overlap_state_weighted) | · |
|  | [Measured Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_measured_state) | · |
|  | [Measured Closure Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_closure_measured_state) | · |
|  | [Mixed Measured Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_measured_mixed_state) | · |
|  | [Nested Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_nested_state) | · |
|  | [Overlap Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_overlap_state) | · |
|  | [PPBlock State](measures/statistical-fitting/sbm_block_state.html#cat_block_pp_state) | · |
|  | [Ranked Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_ranked_state) | · |
|  | [Uncertain Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_state_uncertain) | · |
|  | [Weighted Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_state_weighted) | · |
|  | [Weighted Overlap Block State](measures/statistical-fitting/sbm_block_state.html#cat_block_overlap_state_weighted) | · |

### Dynamics states

25 measures in 6 concepts.

| Concept | Variant | graphtool |
|---|---|---|
| [Belief propagation states](measures/statistical-fitting/belief_propagation_state.html) | [Gen Potts BPState](measures/statistical-fitting/belief_propagation_state.html#cat_bp_gen_potts_state) | · |
|  | [Ising BPState](measures/statistical-fitting/belief_propagation_state.html#cat_bp_ising_state) | · |
|  | [Normal BPState](measures/statistical-fitting/belief_propagation_state.html#cat_bp_normal_state) | · |
| [Boolean and threshold dynamics states](measures/statistical-fitting/threshold_dynamics_state.html) | [Binary Threshold State](measures/statistical-fitting/threshold_dynamics_state.html#cat_binary_state_threshold) | · |
|  | [Boolean State](measures/statistical-fitting/threshold_dynamics_state.html#cat_boolean_state) | · |
|  | [Generalized Binary State](measures/statistical-fitting/threshold_dynamics_state.html#cat_binary_generalized_state) | · |
| [Continuous dynamics states (Kuramoto, linear, normal, Lotka-Volterra)](measures/statistical-fitting/continuous_dynamics_state.html) | [Kuramoto State](measures/statistical-fitting/continuous_dynamics_state.html#cat_kuramoto_state) | · |
|  | [Linear Normal State](measures/statistical-fitting/continuous_dynamics_state.html#cat_linear_normal_state) | · |
|  | [Linear State](measures/statistical-fitting/continuous_dynamics_state.html#cat_linear_state) | · |
|  | [LVState](measures/statistical-fitting/continuous_dynamics_state.html#cat_lv_state) | · |
|  | [Normal State](measures/statistical-fitting/continuous_dynamics_state.html#cat_normal_state) | · |
| [Epidemic dynamics states (SI, SIS, SIR, SIRS)](measures/statistical-fitting/epidemic_dynamics_state.html) | [SIRSState](measures/statistical-fitting/epidemic_dynamics_state.html#cat_sirs_state) | · |
|  | [SIRState](measures/statistical-fitting/epidemic_dynamics_state.html#cat_sir_state) | · |
|  | [SISState](measures/statistical-fitting/epidemic_dynamics_state.html#cat_sis_state) | · |
|  | [SIState](measures/statistical-fitting/epidemic_dynamics_state.html#cat_si_state) | · |
| [Ising and Potts dynamics states](measures/statistical-fitting/spin_dynamics_state.html) | [CIsing Glauber State](measures/statistical-fitting/spin_dynamics_state.html#cat_c_glauber_ising_state) | · |
|  | [Ising Glauber State](measures/statistical-fitting/spin_dynamics_state.html#cat_glauber_ising_state) | · |
|  | [Ising Metropolis State](measures/statistical-fitting/spin_dynamics_state.html#cat_ising_metropolis_state) | · |
|  | [Potts Glauber State](measures/statistical-fitting/spin_dynamics_state.html#cat_glauber_potts_state) | · |
|  | [Potts Metropolis State](measures/statistical-fitting/spin_dynamics_state.html#cat_metropolis_potts_state) | · |
|  | [Potts State](measures/statistical-fitting/spin_dynamics_state.html#cat_potts_state) | · |
| [Voter, Kirman and Axelrod dynamics states](measures/statistical-fitting/opinion_dynamics_state.html) | [Axelrod State](measures/statistical-fitting/opinion_dynamics_state.html#cat_axelrod_state) | · |
|  | [Kirman State](measures/statistical-fitting/opinion_dynamics_state.html#cat_kirman_state) | · |
|  | [Majority Voter State](measures/statistical-fitting/opinion_dynamics_state.html#cat_majority_state_voter) | · |
|  | [Voter State](measures/statistical-fitting/opinion_dynamics_state.html#cat_state_voter) | · |

### ERGM terms

118 measures in 14 concepts.

| Concept | Variant | ergm | rsiena |
|---|---|---|---|
| [Balance term](measures/statistical-fitting/ergm_balance.html) | [Balance](measures/statistical-fitting/ergm_balance.html#cat_balance) | · | · |
| [Bipartite terms](measures/statistical-fitting/ergm_bipartite_terms.html) | [B1concurrent](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1concurrent) | · |  |
|  | [B1cov](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1cov) | · |  |
|  | [B1degrange](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1degrange) | · |  |
|  | [B1degree](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1degree) | · |  |
|  | [B1dsp](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1dsp) | · |  |
|  | [B1dsp L](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1dsp_l) | · |  |
|  | [B1factor](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1factor) | · |  |
|  | [B1factordistinct](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1factordistinct) | · |  |
|  | [B1mindegree](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1mindegree) | · |  |
|  | [B1nodematch](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1nodematch) | · |  |
|  | [B1sociality](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1sociality) | · |  |
|  | [B1star](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1star) | · |  |
|  | [B1starmix](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1starmix) | · |  |
|  | [B1twostar](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1twostar) | · |  |
|  | [B2concurrent](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2concurrent) | · |  |
|  | [B2cov](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2cov) | · |  |
|  | [B2degrange](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2degrange) | · |  |
|  | [B2degree](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2degree) | · |  |
|  | [B2dsp](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2dsp) | · |  |
|  | [B2dsp L](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2dsp_l) | · |  |
|  | [B2factor](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2factor) | · |  |
|  | [B2factordistinct](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2factordistinct) | · |  |
|  | [B2mindegree](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2mindegree) | · |  |
|  | [B2nodematch](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2nodematch) | · |  |
|  | [B2sociality](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2sociality) | · |  |
|  | [B2star](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2star) | · |  |
|  | [B2starmix](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2starmix) | · |  |
|  | [B2twostar](measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2twostar) | · |  |
|  | [Coincidence](measures/statistical-fitting/ergm_bipartite_terms.html#cat_coincidence) | · |  |
|  | [Gwb1degree](measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb1degree) | · |  |
|  | [Gwb1dsp](measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb1dsp) | · |  |
|  | [Gwb1dsp L](measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb1dsp_l) | · |  |
|  | [Gwb2degree](measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb2degree) | · |  |
|  | [Gwb2dsp](measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb2dsp) | · |  |
|  | [Gwb2dsp L](measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb2dsp_l) | · |  |
| [Degree terms](measures/statistical-fitting/ergm_degree_terms.html) | [Concurrent](measures/statistical-fitting/ergm_degree_terms.html#cat_concurrent) | · |  |
|  | [Concurrentties](measures/statistical-fitting/ergm_degree_terms.html#cat_concurrentties) | · |  |
|  | [Degcor](measures/statistical-fitting/ergm_degree_terms.html#cat_degcor) | · |  |
|  | [Degcrossprod](measures/statistical-fitting/ergm_degree_terms.html#cat_degcrossprod) | · |  |
|  | [Degrange](measures/statistical-fitting/ergm_degree_terms.html#cat_degrange) | · |  |
|  | [Degree1 5](measures/statistical-fitting/ergm_degree_terms.html#cat_5_degree1) | · |  |
|  | [Degreedist](measures/statistical-fitting/ergm_degree_terms.html#cat_degreedist) | · |  |
|  | [Idegrange](measures/statistical-fitting/ergm_degree_terms.html#cat_idegrange) | · |  |
|  | [Idegree](measures/statistical-fitting/ergm_degree_terms.html#cat_idegree) | · |  |
|  | [Idegree1 5](measures/statistical-fitting/ergm_degree_terms.html#cat_5_idegree1) | · |  |
|  | [Odegrange](measures/statistical-fitting/ergm_degree_terms.html#cat_odegrange) | · |  |
|  | [Odegree](measures/statistical-fitting/ergm_degree_terms.html#cat_odegree) | · |  |
|  | [Odegree1 5](measures/statistical-fitting/ergm_degree_terms.html#cat_5_odegree1) | · |  |
| [Distance and difference terms](measures/statistical-fitting/ergm_distance_terms.html) | [Hamming](measures/statistical-fitting/ergm_distance_terms.html#cat_hamming) | · |  |
|  | [Mm](measures/statistical-fitting/ergm_distance_terms.html#cat_mm) | · |  |
|  | [Rlebdm](measures/statistical-fitting/ergm_distance_terms.html#cat_rlebdm) | · |  |
| [Edge count and density terms](measures/statistical-fitting/ergm_edge_terms.html) | [Edges](measures/statistical-fitting/ergm_edge_terms.html#cat_edge) | · |  |
|  | [Isolatededges](measures/statistical-fitting/ergm_edge_terms.html#cat_isolatededges) | · |  |
|  | [Meandeg](measures/statistical-fitting/ergm_edge_terms.html#cat_meandeg) | · |  |
| [Edge-age terms](measures/statistical-fitting/ergm_duration_terms.html) | [Degrange mean age](measures/statistical-fitting/ergm_duration_terms.html#cat_age_degrange_mean) | · |  |
|  | [Degree mean age](measures/statistical-fitting/ergm_duration_terms.html#cat_age_degree_mean) | · |  |
|  | [Edge ages](measures/statistical-fitting/ergm_duration_terms.html#cat_ages_edge) | · |  |
|  | [Edgecov ages](measures/statistical-fitting/ergm_duration_terms.html#cat_ages_edgecov) | · |  |
|  | [Edgecov mean age](measures/statistical-fitting/ergm_duration_terms.html#cat_age_edgecov_mean) | · |  |
|  | [Edges ageinterval](measures/statistical-fitting/ergm_duration_terms.html#cat_ageinterval_edge) | · |  |
|  | [Mean age](measures/statistical-fitting/ergm_duration_terms.html#cat_age_mean) | · |  |
|  | [Nodefactor mean age](measures/statistical-fitting/ergm_duration_terms.html#cat_age_mean_nodefactor) | · |  |
|  | [Nodemix mean age](measures/statistical-fitting/ergm_duration_terms.html#cat_age_mean_nodemix) | · |  |
| [Nodal and dyadic covariate terms](measures/statistical-fitting/ergm_covariate_terms.html) | [Absdiff](measures/statistical-fitting/ergm_covariate_terms.html#cat_absdiff) | · |  |
|  | [Absdiffcat](measures/statistical-fitting/ergm_covariate_terms.html#cat_absdiffcat) | · |  |
|  | [Attrcov](measures/statistical-fitting/ergm_covariate_terms.html#cat_attrcov) | · |  |
|  | [Dyadcov](measures/statistical-fitting/ergm_covariate_terms.html#cat_dyadcov) | · |  |
|  | [Edgecov](measures/statistical-fitting/ergm_covariate_terms.html#cat_edgecov) | · |  |
|  | [Nodecovar](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodecovar) | · |  |
|  | [Nodecovrange](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodecovrange) | · |  |
|  | [Nodefactordistinct](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodefactordistinct) | · |  |
|  | [Nodeicov](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeicov) | · |  |
|  | [Nodeicovar](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeicovar) | · |  |
|  | [Nodeicovrange](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeicovrange) | · |  |
|  | [Nodeifactor](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeifactor) | · |  |
|  | [Nodeifactordistinct](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeifactordistinct) | · |  |
|  | [Nodemix](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodemix) | · |  |
|  | [Nodeocov](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeocov) | · |  |
|  | [Nodeocovar](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeocovar) | · |  |
|  | [Nodeocovrange](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeocovrange) | · |  |
|  | [Nodeofactor](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeofactor) | · |  |
|  | [Nodeofactordistinct](measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeofactordistinct) | · |  |
|  | [Smalldiff](measures/statistical-fitting/ergm_covariate_terms.html#cat_smalldiff) | · |  |
| [Open triad term](measures/statistical-fitting/ergm_open_triad.html) | [Opentriad](measures/statistical-fitting/ergm_open_triad.html#cat_opentriad) | · |  |
| [Sender, receiver and sociality terms](measures/statistical-fitting/ergm_sender_receiver_terms.html) | [Receiver](measures/statistical-fitting/ergm_sender_receiver_terms.html#cat_receiver) | · |  |
|  | [Sender](measures/statistical-fitting/ergm_sender_receiver_terms.html#cat_sender) | · |  |
|  | [Sociality](measures/statistical-fitting/ergm_sender_receiver_terms.html#cat_sociality) | · |  |
| [Shared-partner terms](measures/statistical-fitting/ergm_shared_partner_terms.html) | [Ddsp](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_ddsp) | · |  |
|  | [Ddsp L](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_ddsp_l) | · |  |
|  | [Desp](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_desp) | · |  |
|  | [Desp L](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_desp_l) | · |  |
|  | [Dgwdsp](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwdsp) | · |  |
|  | [Dgwdsp L](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwdsp_l) | · |  |
|  | [Dgwesp](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwesp) | · |  |
|  | [Dgwesp L](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwesp_l) | · |  |
|  | [Dgwnsp](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwnsp) | · |  |
|  | [Dgwnsp L](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwnsp_l) | · |  |
|  | [Dnsp](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dnsp) | · |  |
|  | [Dnsp L](measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dnsp_l) | · |  |
| [Star and path terms](measures/statistical-fitting/ergm_star_path_terms.html) | [Altkstar](measures/statistical-fitting/ergm_star_path_terms.html#cat_altkstar) | · |  |
|  | [M2star](measures/statistical-fitting/ergm_star_path_terms.html#cat_m2star) | · |  |
|  | [Mutual L](measures/statistical-fitting/ergm_star_path_terms.html#cat_l_mutual) | · |  |
|  | [Threetrail](measures/statistical-fitting/ergm_star_path_terms.html#cat_threetrail) | · |  |
|  | [Twopath](measures/statistical-fitting/ergm_star_path_terms.html#cat_twopath) | · |  |
|  | [Twostar L](measures/statistical-fitting/ergm_star_path_terms.html#cat_l_twostar) | · |  |
| [Transitive and intransitive triple terms](measures/statistical-fitting/ergm_transitive.html) | [Intransitive](measures/statistical-fitting/ergm_transitive.html#cat_intransitive) | · |  |
|  | [Transitive](measures/statistical-fitting/ergm_transitive.html#cat_transitive) | · |  |
|  | [Transitiveties](measures/statistical-fitting/ergm_transitive.html#cat_transitiveties) | · |  |
|  | [Transitiveweights](measures/statistical-fitting/ergm_transitive.html#cat_transitiveweights) | · |  |
| [Triad percentage term](measures/statistical-fitting/ergm_triad_percent.html) | [Tripercent](measures/statistical-fitting/ergm_triad_percent.html#cat_tripercent) | · |  |
| [Triple, cycle and Simmelian terms](measures/statistical-fitting/ergm_triple_terms.html) | [Ctriple](measures/statistical-fitting/ergm_triple_terms.html#cat_ctriple) | · |  |
|  | [Cyclicalties](measures/statistical-fitting/ergm_triple_terms.html#cat_cyclicalties) | · |  |
|  | [Cyclicalweights](measures/statistical-fitting/ergm_triple_terms.html#cat_cyclicalweights) | · |  |
|  | [Localtriangle](measures/statistical-fitting/ergm_triple_terms.html#cat_localtriangle) | · |  |
|  | [Nearsimmelian](measures/statistical-fitting/ergm_triple_terms.html#cat_nearsimmelian) | · |  |
|  | [Simmelianties](measures/statistical-fitting/ergm_triple_terms.html#cat_simmelianties) | · |  |
|  | [Ttriple](measures/statistical-fitting/ergm_triple_terms.html#cat_ttriple) | · |  |

### Marginal and latent graph distributions

11 measures in 3 concepts.

| Concept | Variant | graphtool |
|---|---|---|
| [Block edge gradient](measures/statistical-fitting/block_edge_gradient.html) | [Get block edge gradient](measures/statistical-fitting/block_edge_gradient.html#cat_block_edge_gradient) | · |
| [Latent multigraph inference](measures/statistical-fitting/latent_multigraph.html) | [Em infer](measures/statistical-fitting/latent_multigraph.html#cat_em_infer) | · |
|  | [Latent multigraph](measures/statistical-fitting/latent_multigraph.html#cat_latent_multigraph) | · |
| [Marginal graph distribution (sample, probability, entropy)](measures/statistical-fitting/marginal_graph_distribution.html) | [Bethe entropy](measures/statistical-fitting/marginal_graph_distribution.html#cat_bethe_entropy) | · |
|  | [Marginal graph lprob](measures/statistical-fitting/marginal_graph_distribution.html#cat_lprob_marginal) | · |
|  | [Marginal graph sample](measures/statistical-fitting/marginal_graph_distribution.html#cat_marginal_sample) | · |
|  | [Marginal multigraph entropy](measures/statistical-fitting/marginal_graph_distribution.html#cat_entropy_marginal_multigraph) | · |
|  | [Marginal multigraph lprob](measures/statistical-fitting/marginal_graph_distribution.html#cat_lprob_marginal_multigraph) | · |
|  | [Marginal multigraph sample](measures/statistical-fitting/marginal_graph_distribution.html#cat_marginal_multigraph_sample) | · |
|  | [Mf entropy](measures/statistical-fitting/marginal_graph_distribution.html#cat_entropy_mf) | · |
|  | [Microstate entropy](measures/statistical-fitting/marginal_graph_distribution.html#cat_entropy_microstate) | · |

### Missing data and observation sampling

9 measures in 1 concepts.

| Concept | Variant | missSBM |
|---|---|---|
| [Observation sampling designs (missing data)](measures/statistical-fitting/observation_sampling.html) | [Block Dyad Sampler](measures/statistical-fitting/observation_sampling.html#cat_block_dyad_sampler) | · |
|  | [Block Node Sampler](measures/statistical-fitting/observation_sampling.html#cat_block_sampler) | · |
|  | [Degree Sampler](measures/statistical-fitting/observation_sampling.html#cat_degree_sampler) | · |
|  | [Double Standard Sampler](measures/statistical-fitting/observation_sampling.html#cat_double_sampler_standard) | · |
|  | [Dyad Sampler](measures/statistical-fitting/observation_sampling.html#cat_dyad_sampler) | · |
|  | [Node Sampler](measures/statistical-fitting/observation_sampling.html#cat_sampler) | · |
|  | [Simple Dyad Sampler](measures/statistical-fitting/observation_sampling.html#cat_dyad_sampler_simple) | · |
|  | [Simple Node Sampler](measures/statistical-fitting/observation_sampling.html#cat_sampler_simple) | · |
|  | [Snowball Sampler](measures/statistical-fitting/observation_sampling.html#cat_sampler_snowball) | · |

### Model fitting

32 measures in 28 concepts.

| Concept | Variant | igraph | pyigraph | sna | ergm | graphtool | sknetwork | bct | gephi | ucinet | latentnet | missSBM | goldfish | gergm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Actor-oriented event models (DyNAM)](measures/statistical-fitting/dynam.html) | [Actor-oriented event models (DyNAM)](measures/statistical-fitting/dynam.html#dynam) |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [AIC](measures/statistical-fitting/model_aic.html) | [Aic](measures/statistical-fitting/model_aic.html#cat_aic) |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Bayesian network accuracy model (BBNAM)](measures/statistical-fitting/bbnam.html) | [Bbnam](measures/statistical-fitting/bbnam.html#cat_bbnam) |  |  | · |  |  |  |  |  |  |  |  |  |  |
|  | [Bbnam bf](measures/statistical-fitting/bbnam.html#cat_bbnam_bf) |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Biased net models](measures/statistical-fitting/biased_net_model.html) | [Bn](measures/statistical-fitting/biased_net_model.html#cat_bn) |  |  | · |  |  |  |  |  |  |  |  |  |  |
|  | [Rgbn](measures/statistical-fitting/biased_net_model.html#cat_rgbn) |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Conditional edge prediction (GERGM)](measures/statistical-fitting/conditional_edge_prediction.html) | [Conditional edge prediction](measures/statistical-fitting/conditional_edge_prediction.html#cat_conditional_edge_prediction) |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Dirichlet regression on graphs](measures/statistical-fitting/dirichlet.html) | [Dirichlet](measures/statistical-fitting/dirichlet.html#cat_dirichlet) |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [ERGM change statistics](measures/statistical-fitting/ergm_change_sums.html) | [Ergm change sums](measures/statistical-fitting/ergm_change_sums.html#ergm_change_sums) |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |
| [ERGM Monte Carlo maximum likelihood](measures/statistical-fitting/ergm_mcmle.html) | [Ergm mcmle](measures/statistical-fitting/ergm_mcmle.html#ergm_mcmle) |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |
| [ERGM pseudolikelihood estimation](measures/statistical-fitting/ergm_mple.html) | [Ergm mple](measures/statistical-fitting/ergm_mple.html#ergm_mple) |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |
| [ERGM simulated mean statistics](measures/statistical-fitting/ergm_sim_mean.html) | [Ergm sim mean](measures/statistical-fitting/ergm_sim_mean.html#ergm_sim_mean) |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |
| [ERGM statistics](measures/statistical-fitting/ergm_statistics.html) | [Ergm statistics](measures/statistical-fitting/ergm_statistics.html#ergm_statistics) |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |
| [Generative network models (fit and evaluate)](measures/statistical-fitting/generative_model.html) | [Evaluate generative model](measures/statistical-fitting/generative_model.html#cat_evaluate_generative_model) |  |  |  |  |  |  | · |  |  |  |  |  |  |
|  | [Generative model](measures/statistical-fitting/generative_model.html#cat_generative_model) |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Hierarchical random graph](measures/statistical-fitting/hrg.html) | [Hierarchical random graph (fit, sample, predict)](measures/statistical-fitting/hrg.html#hrg) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hysteresis](measures/statistical-fitting/hysteresis.html) | [Hysteresis](measures/statistical-fitting/hysteresis.html#cat_hysteresis) |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Latent space log-likelihood](measures/statistical-fitting/latent_loglik.html) | [Latent loglik](measures/statistical-fitting/latent_loglik.html#latent_loglik) |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |
| [Latent space move delta](measures/statistical-fitting/latent_move_delta.html) | [Latent move delta](measures/statistical-fitting/latent_move_delta.html#latent_move_delta) |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |
| [MCMC annealing and equilibration](measures/statistical-fitting/mcmc_anneal_equilibrate.html) | [Mcmc anneal](measures/statistical-fitting/mcmc_anneal_equilibrate.html#cat_anneal_mcmc) |  |  |  |  | · |  |  |  |  |  |  |  |  |
|  | [Mcmc equilibrate](measures/statistical-fitting/mcmc_anneal_equilibrate.html#cat_equilibrate_mcmc) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Network canonical correlation](measures/statistical-fitting/canonical_correlation.html) | [Netcancor](measures/statistical-fitting/canonical_correlation.html#cat_netcancor) |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Network-based statistic](measures/statistical-fitting/bct_nbs.html) | [Nbs bct](measures/statistical-fitting/bct_nbs.html#cat_bct_nbs) |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Ordinal association](measures/statistical-fitting/ordinal_association.html) | [Ordinalassoc](measures/statistical-fitting/ordinal_association.html#cat_ordinalassoc) |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [p-star models](measures/statistical-fitting/pstar.html) | [Pstar](measures/statistical-fitting/pstar.html#cat_pstar) |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Power-law fit of a degree distribution](measures/statistical-fitting/power_law_fit.html) | [Power-law fit of a degree distribution](measures/statistical-fitting/power_law_fit.html#power_law_fit) | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [SBM description length](measures/statistical-fitting/sbm_description_length.html) | [Sbm description length](measures/statistical-fitting/sbm_description_length.html#sbm_description_length) |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |
| [SBM for partially observed networks](measures/statistical-fitting/sbm_missing.html) | [Stochastic block models for partially observed networks](measures/statistical-fitting/sbm_missing.html#sbm_missing) |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [SBM move delta](measures/statistical-fitting/sbm_move_delta.html) | [Sbm move delta](measures/statistical-fitting/sbm_move_delta.html#sbm_move_delta) |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |
| [Statistical inference clustering](measures/statistical-fitting/statistical_inference_clustering.html) | [Statistical Inference Clustering](measures/statistical-fitting/statistical_inference_clustering.html#cat_clustering_inference_statistical) |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Stochastic block model fit](measures/statistical-fitting/sbm_fit.html) | [Sbm fit](measures/statistical-fitting/sbm_fit.html#sbm_fit) |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |
| [Valued-network ERGM (GERGM)](measures/statistical-fitting/gergm.html) | [Valued-network ERGM (GERGM)](measures/statistical-fitting/gergm.html#gergm) |  |  |  |  |  |  |  |  |  |  |  |  | · |

### Prediction and classification

6 measures in 1 concepts.

| Concept | Variant | sknetwork |
|---|---|---|
| [Node classification](measures/statistical-fitting/node_classification.html) | [Diffusion Classifier](measures/statistical-fitting/node_classification.html#cat_classifier_diffusion) | · |
|  | [GNNClassifier](measures/statistical-fitting/node_classification.html#cat_classifier_gnn) | · |
|  | [NNClassifier](measures/statistical-fitting/node_classification.html#cat_classifier_nn) | · |
|  | [Page Rank Classifier](measures/statistical-fitting/node_classification.html#cat_classifier_page_rank) | · |
|  | [Propagation](measures/statistical-fitting/node_classification.html#cat_propagation) | · |
|  | [Rank Classifier](measures/statistical-fitting/node_classification.html#cat_classifier_rank) | · |

### SAOM effects

274 measures in 25 concepts.

| Concept | Variant | rsiena |
|---|---|---|
| [Activity effects](measures/statistical-fitting/saom_activity.html) | [Alt XOut Act](measures/statistical-fitting/saom_activity.html#cat_act_alt_out_x) | · |
|  | [Cross XOut Act](measures/statistical-fitting/saom_activity.html#cat_act_cross_out_x) | · |
|  | [Diff XOut Act](measures/statistical-fitting/saom_activity.html#cat_act_diff_out_x) | · |
|  | [Hom XOut Act](measures/statistical-fitting/saom_activity.html#cat_act_hom_out_x) | · |
|  | [Hom XOut Act2](measures/statistical-fitting/saom_activity.html#cat_act2_hom_out_x) | · |
|  | [In Act](measures/statistical-fitting/saom_activity.html#cat_act) | · |
|  | [In Act c](measures/statistical-fitting/saom_activity.html#cat_act_c) | · |
|  | [In Act ego](measures/statistical-fitting/saom_activity.html#cat_act_ego) | · |
|  | [In Act Sqrt](measures/statistical-fitting/saom_activity.html#cat_act_sqrt) | · |
|  | [In Act X](measures/statistical-fitting/saom_activity.html#cat_act_x) | · |
|  | [Out Act](measures/statistical-fitting/saom_activity.html#cat_act_out) | · |
|  | [Out Act c](measures/statistical-fitting/saom_activity.html#cat_act_c_out) | · |
|  | [Out Act ego](measures/statistical-fitting/saom_activity.html#cat_act_ego_out) | · |
|  | [Out Act More ego](measures/statistical-fitting/saom_activity.html#cat_act_ego_more_out) | · |
|  | [Out Act Sqrt](measures/statistical-fitting/saom_activity.html#cat_act_out_sqrt) | · |
|  | [Out Act Sqrt More ego](measures/statistical-fitting/saom_activity.html#cat_act_ego_more_out_sqrt) | · |
|  | [Out Act X](measures/statistical-fitting/saom_activity.html#cat_act_out_x) | · |
|  | [Prim Deg Act](measures/statistical-fitting/saom_activity.html#cat_act_deg_prim) | · |
|  | [Prim Deg Act Diff](measures/statistical-fitting/saom_activity.html#cat_act_deg_diff_prim) | · |
|  | [Prim Deg Act Diff Sqrt](measures/statistical-fitting/saom_activity.html#cat_act_deg_diff_prim_sqrt) | · |
|  | [Prim Deg Act Inv](measures/statistical-fitting/saom_activity.html#cat_act_deg_inv_prim) | · |
|  | [Prim Deg Act Log](measures/statistical-fitting/saom_activity.html#cat_act_deg_log_prim) | · |
|  | [Prim Deg Act Sqrt](measures/statistical-fitting/saom_activity.html#cat_act_deg_prim_sqrt) | · |
|  | [Same XOut Act](measures/statistical-fitting/saom_activity.html#cat_act_out_same_x) | · |
| [Alter average, total and extremum effects](measures/statistical-fitting/saom_alter_effects.html) | [Alt Higher Ego X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_ego_higher_x) | · |
|  | [Alt LThreshold X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_l_threshold_x) | · |
|  | [Alt RThreshold X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_r_threshold_x) | · |
|  | [Alt Sq X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_sq_x) | · |
|  | [Alt X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_x) | · |
|  | [Av Alt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_av) | · |
|  | [Av Alt Alt X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_av_x) | · |
|  | [Av Alt cc](measures/statistical-fitting/saom_alter_effects.html#cat_alt_av_cc) | · |
|  | [Av Alt Ego X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_av_ego_x) | · |
|  | [Av Alt gmm](measures/statistical-fitting/saom_alter_effects.html#cat_alt_av_gmm) | · |
|  | [Av Alt Same X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_av_same_x) | · |
|  | [Av Alt W](measures/statistical-fitting/saom_alter_effects.html#cat_alt_av_w) | · |
|  | [Ego Plus Alt Sq X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_ego_plus_sq_x) | · |
|  | [Ego Plus Alt X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_ego_plus_x) | · |
|  | [Ego Xalt X](measures/statistical-fitting/saom_alter_effects.html#cat_ego_x_xalt) | · |
|  | [Max Alt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_max) | · |
|  | [Max Alt gmm](measures/statistical-fitting/saom_alter_effects.html#cat_alt_gmm_max) | · |
|  | [Max XAlt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_max_x) | · |
|  | [Min Alt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_min) | · |
|  | [Min Alt gmm](measures/statistical-fitting/saom_alter_effects.html#cat_alt_gmm_min) | · |
|  | [Min XAlt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_min_x) | · |
|  | [Tot Alt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_tot) | · |
|  | [Tot Alt cc](measures/statistical-fitting/saom_alter_effects.html#cat_alt_cc_tot) | · |
|  | [Tot Alt Ego X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_ego_tot_x) | · |
|  | [Tot Alt gmm](measures/statistical-fitting/saom_alter_effects.html#cat_alt_gmm_tot) | · |
|  | [Tot Alt Same X](measures/statistical-fitting/saom_alter_effects.html#cat_alt_same_tot_x) | · |
|  | [Tot Alt W](measures/statistical-fitting/saom_alter_effects.html#cat_alt_tot_w) | · |
|  | [Tot XAlt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_tot_x) | · |
|  | [Var Alt](measures/statistical-fitting/saom_alter_effects.html#cat_alt_var) | · |
| [Compression effects](measures/statistical-fitting/saom_compression.html) | [Non PCompress](measures/statistical-fitting/saom_compression.html#cat_compress_non_p) | · |
|  | [Prim Compress](measures/statistical-fitting/saom_compression.html#cat_compress_prim) | · |
| [Covariate main and interaction effects](measures/statistical-fitting/saom_covariate_effects.html) | [Abs Diff X](measures/statistical-fitting/saom_covariate_effects.html#cat_abs_diff_x) | · |
|  | [Cy WWX](measures/statistical-fitting/saom_covariate_effects.html#cat_cy_wwx) | · |
|  | [Diff Sq X](measures/statistical-fitting/saom_covariate_effects.html#cat_diff_sq_x) | · |
|  | [Diff X](measures/statistical-fitting/saom_covariate_effects.html#cat_diff_x) | · |
|  | [Dyadic Cov](measures/statistical-fitting/saom_covariate_effects.html#cat_cov_dyadic) | · |
|  | [In WWX](measures/statistical-fitting/saom_covariate_effects.html#cat_wwx) | · |
|  | [Out WWX](measures/statistical-fitting/saom_covariate_effects.html#cat_out_wwx) | · |
|  | [Same X](measures/statistical-fitting/saom_covariate_effects.html#cat_same_x) | · |
|  | [Unequal X](measures/statistical-fitting/saom_covariate_effects.html#cat_unequal_x) | · |
|  | [WXX](measures/statistical-fitting/saom_covariate_effects.html#cat_wxx) | · |
|  | [X](measures/statistical-fitting/saom_covariate_effects.html#cat_x) | · |
|  | [XWX](measures/statistical-fitting/saom_covariate_effects.html#cat_xwx) | · |
|  | [XWX1](measures/statistical-fitting/saom_covariate_effects.html#cat_xwx1) | · |
|  | [XWX2](measures/statistical-fitting/saom_covariate_effects.html#cat_xwx2) | · |
|  | [XXW](measures/statistical-fitting/saom_covariate_effects.html#cat_xxw) | · |
| [Cycle effects](measures/statistical-fitting/saom_cycle_effects.html) | [Cycle3](measures/statistical-fitting/saom_cycle_effects.html#cat_cycle3) | · |
|  | [Cycle4](measures/statistical-fitting/saom_cycle_effects.html#cat_cycle4) | · |
|  | [Same In XCycle4](measures/statistical-fitting/saom_cycle_effects.html#cat_cycle4_same_x) | · |
| [Degree assortativity effects](measures/statistical-fitting/saom_assortativity.html) | [In In Ass](measures/statistical-fitting/saom_assortativity.html#cat_ass) | · |
|  | [In Out Ass](measures/statistical-fitting/saom_assortativity.html#cat_ass_out) | · |
| [Degree effects](measures/statistical-fitting/saom_degree_effects.html) | [Av Deg](measures/statistical-fitting/saom_degree_effects.html#cat_av_deg) | · |
|  | [Deg Abs Contr X](measures/statistical-fitting/saom_degree_effects.html#cat_abs_contr_deg_x) | · |
|  | [Deg Abs Diff X](measures/statistical-fitting/saom_degree_effects.html#cat_abs_deg_diff_x) | · |
|  | [Deg Neg Contr X](measures/statistical-fitting/saom_degree_effects.html#cat_contr_deg_neg_x) | · |
|  | [Deg Neg Diff X](measures/statistical-fitting/saom_degree_effects.html#cat_deg_diff_neg_x) | · |
|  | [Deg Pos Contr X](measures/statistical-fitting/saom_degree_effects.html#cat_contr_deg_pos_x) | · |
|  | [Deg Pos Diff X](measures/statistical-fitting/saom_degree_effects.html#cat_deg_diff_pos_x) | · |
|  | [In Is Degree](measures/statistical-fitting/saom_degree_effects.html#cat_degree_is) | · |
|  | [Indeg](measures/statistical-fitting/saom_degree_effects.html#cat_indeg) | · |
|  | [Indeg Av Group](measures/statistical-fitting/saom_degree_effects.html#cat_av_group_indeg) | · |
|  | [Indeg Tot Group](measures/statistical-fitting/saom_degree_effects.html#cat_group_indeg_tot) | · |
|  | [Outdeg](measures/statistical-fitting/saom_degree_effects.html#cat_outdeg) | · |
| [Dense triads effect](measures/statistical-fitting/saom_dense_triads.html) | [Beh Dense Triads](measures/statistical-fitting/saom_dense_triads.html#cat_beh_dense_triads) | · |
|  | [Dense Triads](measures/statistical-fitting/saom_dense_triads.html#cat_dense_triads) | · |
|  | [Sim Dense Triads](measures/statistical-fitting/saom_dense_triads.html#cat_dense_sim_triads) | · |
| [Distance-two effects](measures/statistical-fitting/saom_distance2.html) | [Alt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_dist2) | · |
|  | [Any In Exposure Dist2](measures/statistical-fitting/saom_distance2.html#cat_any_dist2_exposure) | · |
|  | [Av Alt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_av_dist2) | · |
|  | [Av In Alt Dist2 nc](measures/statistical-fitting/saom_distance2.html#cat_alt_av_dist2_nc) | · |
|  | [Av In Sim Dist2](measures/statistical-fitting/saom_distance2.html#cat_av_dist2_sim) | · |
|  | [Av TAlt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_av_dist2_t) | · |
|  | [Av TIn Alt Dist2 nc](measures/statistical-fitting/saom_distance2.html#cat_alt_av_dist2_nc_t) | · |
|  | [Av Tin Exposure Dist2](measures/statistical-fitting/saom_distance2.html#cat_av_dist2_exposure_tin) | · |
|  | [Av TXAlt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_av_dist2_tx) | · |
|  | [Av XAlt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_av_dist2_x) | · |
|  | [Nbr Dist2](measures/statistical-fitting/saom_distance2.html#cat_dist2_nbr) | · |
|  | [Nbr Dist2twice](measures/statistical-fitting/saom_distance2.html#cat_dist2twice_nbr) | · |
|  | [Same Ego Dist2](measures/statistical-fitting/saom_distance2.html#cat_dist2_ego_same) | · |
|  | [Sim Dist2](measures/statistical-fitting/saom_distance2.html#cat_dist2_sim) | · |
|  | [Sim Ego Dist2](measures/statistical-fitting/saom_distance2.html#cat_dist2_ego_sim) | · |
|  | [Tot AAlt Dist2](measures/statistical-fitting/saom_distance2.html#cat_a_alt_dist2_tot) | · |
|  | [Tot AIn Alt Dist2 nc](measures/statistical-fitting/saom_distance2.html#cat_a_alt_dist2_nc_tot) | · |
|  | [Tot AIn Exposure Dist2](measures/statistical-fitting/saom_distance2.html#cat_a_dist2_exposure_tot) | · |
|  | [Tot Alt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_dist2_tot) | · |
|  | [Tot AXAlt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_ax_dist2_tot) | · |
|  | [Tot Dist2](measures/statistical-fitting/saom_distance2.html#cat_dist2_tot) | · |
|  | [Tot In Alt Dist2 nc](measures/statistical-fitting/saom_distance2.html#cat_alt_dist2_nc_tot) | · |
|  | [Tot In Exposure Dist2](measures/statistical-fitting/saom_distance2.html#cat_dist2_exposure_tot) | · |
|  | [Tot In Sim Dist2](measures/statistical-fitting/saom_distance2.html#cat_dist2_sim_tot) | · |
|  | [Tot XAlt Dist2](measures/statistical-fitting/saom_distance2.html#cat_alt_dist2_tot_x) | · |
| [Ego effects](measures/statistical-fitting/saom_ego_effects.html) | [Av Group Ego X](measures/statistical-fitting/saom_ego_effects.html#cat_av_ego_group_x) | · |
|  | [Div In ego](measures/statistical-fitting/saom_ego_effects.html#cat_div_ego) | · |
|  | [Div Out ego](measures/statistical-fitting/saom_ego_effects.html#cat_div_ego_out) | · |
|  | [Ego Alter Combi](measures/statistical-fitting/saom_ego_effects.html#cat_alter_combi_ego) | · |
|  | [Ego Alter Covar Comb](measures/statistical-fitting/saom_ego_effects.html#cat_alter_comb_covar_ego) | · |
|  | [Ego Diff X](measures/statistical-fitting/saom_ego_effects.html#cat_diff_ego_x) | · |
|  | [Ego LThreshold X](measures/statistical-fitting/saom_ego_effects.html#cat_ego_l_threshold_x) | · |
|  | [Ego RThreshold X](measures/statistical-fitting/saom_ego_effects.html#cat_ego_r_threshold_x) | · |
|  | [Ego Sq X](measures/statistical-fitting/saom_ego_effects.html#cat_ego_sq_x) | · |
|  | [Ego X](measures/statistical-fitting/saom_ego_effects.html#cat_ego_x) | · |
|  | [Ego X gmm](measures/statistical-fitting/saom_ego_effects.html#cat_ego_gmm_x) | · |
|  | [Out More ego](measures/statistical-fitting/saom_ego_effects.html#cat_ego_more_out) | · |
|  | [Tot Group Ego X](measures/statistical-fitting/saom_ego_effects.html#cat_ego_group_tot_x) | · |
| [Exposure, infection and susceptibility effects](measures/statistical-fitting/saom_exposure_infection.html) | [Av Exposure](measures/statistical-fitting/saom_exposure_infection.html#cat_av_exposure) | · |
|  | [Infect Covar](measures/statistical-fitting/saom_exposure_infection.html#cat_covar_infect) | · |
|  | [Infect In](measures/statistical-fitting/saom_exposure_infection.html#cat_infect) | · |
|  | [Infect Out](measures/statistical-fitting/saom_exposure_infection.html#cat_infect_out) | · |
|  | [Suscept Av Covar](measures/statistical-fitting/saom_exposure_infection.html#cat_av_covar_suscept) | · |
|  | [Suscept Av In](measures/statistical-fitting/saom_exposure_infection.html#cat_av_suscept) | · |
|  | [Tot Exposure](measures/statistical-fitting/saom_exposure_infection.html#cat_exposure_tot) | · |
| [Geometrically weighted shared-partner effects](measures/statistical-fitting/saom_gwesp_gwdsp.html) | [Gwdsp FB](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_fb_gwdsp) | · |
|  | [Gwdsp FF](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_ff_gwdsp) | · |
|  | [Gwesp BB](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_bb_gwesp) | · |
|  | [Gwesp BF](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_bf_gwesp) | · |
|  | [Gwesp FB](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_fb_gwesp) | · |
|  | [Gwesp FF](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_ff_gwesp) | · |
|  | [Gwesp RR](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_gwesp_rr) | · |
|  | [Tot Gwdsp FBAlt](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_alt_fb_gwdsp_tot) | · |
|  | [Tot Gwdsp FBAlt nc](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_alt_fb_gwdsp_nc_tot) | · |
|  | [Tot Gwdsp FFAlt](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_alt_ff_gwdsp_tot) | · |
|  | [Tot Gwdsp FFAlt nc](measures/statistical-fitting/saom_gwesp_gwdsp.html#cat_alt_ff_gwdsp_nc_tot) | · |
| [Group effects](measures/statistical-fitting/saom_group_effects.html) | [Av Group](measures/statistical-fitting/saom_group_effects.html#cat_av_group) | · |
|  | [Tot Group](measures/statistical-fitting/saom_group_effects.html#cat_group_tot) | · |
| [Higher, lower and more-than effects](measures/statistical-fitting/saom_comparison_effects.html) | [Av Att Higher](measures/statistical-fitting/saom_comparison_effects.html#cat_att_av_higher) | · |
|  | [Av Att Lower](measures/statistical-fitting/saom_comparison_effects.html#cat_att_av_lower) | · |
|  | [Higher](measures/statistical-fitting/saom_comparison_effects.html#cat_higher) | · |
|  | [In2 Plus](measures/statistical-fitting/saom_comparison_effects.html#cat_in2_plus) | · |
|  | [In3 Plus](measures/statistical-fitting/saom_comparison_effects.html#cat_in3_plus) | · |
|  | [Jin](measures/statistical-fitting/saom_comparison_effects.html#cat_jin) | · |
|  | [Jout](measures/statistical-fitting/saom_comparison_effects.html#cat_jout) | · |
|  | [Out More](measures/statistical-fitting/saom_comparison_effects.html#cat_more_out) | · |
|  | [Out More2](measures/statistical-fitting/saom_comparison_effects.html#cat_more2_out) | · |
|  | [Out More3](measures/statistical-fitting/saom_comparison_effects.html#cat_more3_out) | · |
|  | [Out XMore](measures/statistical-fitting/saom_comparison_effects.html#cat_more_out_x) | · |
|  | [Tot Att Higher](measures/statistical-fitting/saom_comparison_effects.html#cat_att_higher_tot) | · |
|  | [Tot Att Lower](measures/statistical-fitting/saom_comparison_effects.html#cat_att_lower_tot) | · |
| [Isolate effects](measures/statistical-fitting/saom_isolate_effects.html) | [Anti In Iso](measures/statistical-fitting/saom_isolate_effects.html#cat_anti_iso) | · |
|  | [Anti In Iso2](measures/statistical-fitting/saom_isolate_effects.html#cat_anti_iso2) | · |
|  | [Isolate](measures/statistical-fitting/saom_isolate_effects.html#cat_isolate) | · |
|  | [Isolate Net](measures/statistical-fitting/saom_isolate_effects.html#cat_isolate_net) | · |
|  | [Out Iso](measures/statistical-fitting/saom_isolate_effects.html#cat_iso_out) | · |
|  | [Out Isolate](measures/statistical-fitting/saom_isolate_effects.html#cat_isolate_out) | · |
| [Popularity effects](measures/statistical-fitting/saom_popularity.html) | [Av Alt Pop](measures/statistical-fitting/saom_popularity.html#cat_alt_av_pop) | · |
|  | [Av In Sim Pop Alt](measures/statistical-fitting/saom_popularity.html#cat_alt_av_pop_sim) | · |
|  | [Av Sim Pop Ego](measures/statistical-fitting/saom_popularity.html#cat_av_ego_pop_sim) | · |
|  | [Diff XIn Pop](measures/statistical-fitting/saom_popularity.html#cat_diff_pop_x) | · |
|  | [In Pop](measures/statistical-fitting/saom_popularity.html#cat_pop) | · |
|  | [In Pop c](measures/statistical-fitting/saom_popularity.html#cat_c_pop) | · |
|  | [In Pop dya](measures/statistical-fitting/saom_popularity.html#cat_dya_pop) | · |
|  | [In Pop Sqrt](measures/statistical-fitting/saom_popularity.html#cat_pop_sqrt) | · |
|  | [In Pop X](measures/statistical-fitting/saom_popularity.html#cat_pop_x) | · |
|  | [Isolate Pop](measures/statistical-fitting/saom_popularity.html#cat_isolate_pop) | · |
|  | [Out Pop](measures/statistical-fitting/saom_popularity.html#cat_out_pop) | · |
|  | [Out Pop c](measures/statistical-fitting/saom_popularity.html#cat_c_out_pop) | · |
|  | [Out Pop More](measures/statistical-fitting/saom_popularity.html#cat_more_out_pop) | · |
|  | [Out Pop Sqrt](measures/statistical-fitting/saom_popularity.html#cat_out_pop_sqrt) | · |
|  | [Out Pop Sqrt More](measures/statistical-fitting/saom_popularity.html#cat_more_out_pop_sqrt) | · |
|  | [Out Pop Threshold](measures/statistical-fitting/saom_popularity.html#cat_out_pop_threshold) | · |
|  | [Out Pop X](measures/statistical-fitting/saom_popularity.html#cat_out_pop_x) | · |
|  | [Pop Alt](measures/statistical-fitting/saom_popularity.html#cat_alt_pop) | · |
|  | [Same XIn Pop](measures/statistical-fitting/saom_popularity.html#cat_pop_same_x) | · |
|  | [Shared Pop](measures/statistical-fitting/saom_popularity.html#cat_pop_shared) | · |
|  | [Tot Alt Pop](measures/statistical-fitting/saom_popularity.html#cat_alt_pop_tot) | · |
|  | [Tot In Sim Pop Alt](measures/statistical-fitting/saom_popularity.html#cat_alt_pop_sim_tot) | · |
| [Primary setting effect](measures/statistical-fitting/saom_primary_setting.html) | [Primary](measures/statistical-fitting/saom_primary_setting.html#cat_primary) | · |
| [Rate effects (inverse, log, covariate)](measures/statistical-fitting/saom_rate_effects.html) | [In Rate](measures/statistical-fitting/saom_rate_effects.html#cat_rate) | · |
|  | [In Rate Inv](measures/statistical-fitting/saom_rate_effects.html#cat_inv_rate) | · |
|  | [In Rate Log](measures/statistical-fitting/saom_rate_effects.html#cat_log_rate) | · |
|  | [Out Inv](measures/statistical-fitting/saom_rate_effects.html#cat_inv_out) | · |
|  | [Out Rate](measures/statistical-fitting/saom_rate_effects.html#cat_out_rate) | · |
|  | [Out Rate Inv](measures/statistical-fitting/saom_rate_effects.html#cat_inv_out_rate) | · |
|  | [Out Rate Log](measures/statistical-fitting/saom_rate_effects.html#cat_log_out_rate) | · |
|  | [Out Sq Inv](measures/statistical-fitting/saom_rate_effects.html#cat_inv_out_sq) | · |
|  | [Rate X](measures/statistical-fitting/saom_rate_effects.html#cat_rate_x) | · |
|  | [Recip Rate](measures/statistical-fitting/saom_rate_effects.html#cat_rate_recip) | · |
|  | [Recip Rate Inv](measures/statistical-fitting/saom_rate_effects.html#cat_inv_rate_recip) | · |
|  | [Recip Rate Log](measures/statistical-fitting/saom_rate_effects.html#cat_log_rate_recip) | · |
| [Reciprocity effects](measures/statistical-fitting/saom_reciprocity.html) | [Av Rec Alt](measures/statistical-fitting/saom_reciprocity.html#cat_alt_av_rec) | · |
|  | [Av Rec Alt Same X](measures/statistical-fitting/saom_reciprocity.html#cat_alt_av_rec_same_x) | · |
|  | [Av Sim Rec Pop](measures/statistical-fitting/saom_reciprocity.html#cat_av_pop_rec_sim) | · |
|  | [Av Sim Recip](measures/statistical-fitting/saom_reciprocity.html#cat_av_recip_sim) | · |
|  | [Av XRec Alt](measures/statistical-fitting/saom_reciprocity.html#cat_alt_av_rec_x) | · |
|  | [Diff XReci Act](measures/statistical-fitting/saom_reciprocity.html#cat_act_diff_reci_x) | · |
|  | [Ego Xalt XRecip](measures/statistical-fitting/saom_reciprocity.html#cat_ego_recip_x_xalt) | · |
|  | [Newrecip](measures/statistical-fitting/saom_reciprocity.html#cat_newrecip) | · |
|  | [Persistrecip](measures/statistical-fitting/saom_reciprocity.html#cat_persistrecip) | · |
|  | [Realrecip](measures/statistical-fitting/saom_reciprocity.html#cat_realrecip) | · |
|  | [Reci Act](measures/statistical-fitting/saom_reciprocity.html#cat_act_reci) | · |
|  | [Reci Act ego](measures/statistical-fitting/saom_reciprocity.html#cat_act_ego_reci) | · |
|  | [Reci Pop](measures/statistical-fitting/saom_reciprocity.html#cat_pop_reci) | · |
|  | [Reci Pop Sqrt](measures/statistical-fitting/saom_reciprocity.html#cat_pop_reci_sqrt) | · |
|  | [Recip](measures/statistical-fitting/saom_reciprocity.html#cat_recip) | · |
|  | [Recip Deg](measures/statistical-fitting/saom_reciprocity.html#cat_deg_recip) | · |
|  | [Same XReci Act](measures/statistical-fitting/saom_reciprocity.html#cat_act_reci_same_x) | · |
|  | [Same XRecip](measures/statistical-fitting/saom_reciprocity.html#cat_recip_same_x) | · |
|  | [Sim Recip X](measures/statistical-fitting/saom_reciprocity.html#cat_recip_sim_x) | · |
|  | [Tot Rec Alt](measures/statistical-fitting/saom_reciprocity.html#cat_alt_rec_tot) | · |
|  | [Tot Rec Alt Same X](measures/statistical-fitting/saom_reciprocity.html#cat_alt_rec_same_tot_x) | · |
|  | [Tot Sim Rec Pop](measures/statistical-fitting/saom_reciprocity.html#cat_pop_rec_sim_tot) | · |
|  | [Tot Sim Recip](measures/statistical-fitting/saom_reciprocity.html#cat_recip_sim_tot) | · |
|  | [Tot XRec Alt](measures/statistical-fitting/saom_reciprocity.html#cat_alt_rec_tot_x) | · |
|  | [XRecip](measures/statistical-fitting/saom_reciprocity.html#cat_recip_x) | · |
| [SAOM simulated mean statistics](measures/statistical-fitting/saom_simulated_mean.html) | [Saom sim mean](measures/statistical-fitting/saom_simulated_mean.html#saom_sim_mean) | ≠ |
| [Similarity effects](measures/statistical-fitting/saom_similarity.html) | [Av In Sim](measures/statistical-fitting/saom_similarity.html#cat_av_sim) | · |
|  | [Av Sim Alt X](measures/statistical-fitting/saom_similarity.html#cat_alt_av_sim_x) | · |
|  | [Av Sim Ego X](measures/statistical-fitting/saom_similarity.html#cat_av_ego_sim_x) | · |
|  | [Av Sim gmm](measures/statistical-fitting/saom_similarity.html#cat_av_gmm_sim) | · |
|  | [Av Sim Var Alt](measures/statistical-fitting/saom_similarity.html#cat_alt_av_sim_var) | · |
|  | [Av Sim W](measures/statistical-fitting/saom_similarity.html#cat_av_sim_w) | · |
|  | [Sim All Far](measures/statistical-fitting/saom_similarity.html#cat_all_far_sim) | · |
|  | [Sim All Near](measures/statistical-fitting/saom_similarity.html#cat_all_near_sim) | · |
|  | [Sim X](measures/statistical-fitting/saom_similarity.html#cat_sim_x) | · |
|  | [Sim X gmm](measures/statistical-fitting/saom_similarity.html#cat_gmm_sim_x) | · |
|  | [Tot In Sim](measures/statistical-fitting/saom_similarity.html#cat_sim_tot) | · |
|  | [Tot Sim Alt X](measures/statistical-fitting/saom_similarity.html#cat_alt_sim_tot_x) | · |
|  | [Tot Sim Ego X](measures/statistical-fitting/saom_similarity.html#cat_ego_sim_tot_x) | · |
|  | [Tot Sim W](measures/statistical-fitting/saom_similarity.html#cat_sim_tot_w) | · |
| [Structural equivalence effect](measures/statistical-fitting/saom_structural_equivalence.html) | [In Struct Eq](measures/statistical-fitting/saom_structural_equivalence.html#cat_eq_struct) | · |
| [Threshold and truncation effects](measures/statistical-fitting/saom_threshold_effects.html) | [Out Threshold](measures/statistical-fitting/saom_threshold_effects.html#cat_out_threshold) | · |
|  | [Out Threshold2](measures/statistical-fitting/saom_threshold_effects.html#cat_out_threshold2) | · |
|  | [Out Trunc](measures/statistical-fitting/saom_threshold_effects.html#cat_out_trunc) | · |
|  | [Out Trunc2](measures/statistical-fitting/saom_threshold_effects.html#cat_out_trunc2) | · |
|  | [Threshold](measures/statistical-fitting/saom_threshold_effects.html#cat_threshold) | · |
|  | [Threshold2](measures/statistical-fitting/saom_threshold_effects.html#cat_threshold2) | · |
|  | [Threshold3](measures/statistical-fitting/saom_threshold_effects.html#cat_threshold3) | · |
|  | [Threshold4](measures/statistical-fitting/saom_threshold_effects.html#cat_threshold4) | · |
| [Transitive triplets effects](measures/statistical-fitting/saom_transitive_triplets.html) | [Agreetrans](measures/statistical-fitting/saom_transitive_triplets.html#cat_agreetrans) | · |
|  | [Diff XTrans Rec Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_diff_rec_trans_trip_x) | · |
|  | [Diff XTrans Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_diff_trans_trip_x) | · |
|  | [Hom XTrans Rec Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_hom_rec_trans_trip_x) | · |
|  | [Hom XTrans Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_hom_trans_trip_x) | · |
|  | [Jump XTrans Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_jump_trans_trip_x) | · |
|  | [Realtrans](measures/statistical-fitting/saom_transitive_triplets.html#cat_realtrans) | · |
|  | [Same XTrans Rec Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_rec_same_trans_trip_x) | · |
|  | [Same XTrans Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_same_trans_trip_x) | · |
|  | [Sim XTrans Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_sim_trans_trip_x) | · |
|  | [Trans Med Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_med_trans_trip) | · |
|  | [Trans Rec Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_rec_trans_trip) | · |
|  | [Trans Rec Trip2](measures/statistical-fitting/saom_transitive_triplets.html#cat_rec_trans_trip2) | · |
|  | [Trans Ties](measures/statistical-fitting/saom_transitive_triplets.html#cat_ties_trans) | · |
|  | [Trans Trip](measures/statistical-fitting/saom_transitive_triplets.html#cat_trans_trip) | · |
|  | [Trans Trip EE](measures/statistical-fitting/saom_transitive_triplets.html#cat_ee_trans_trip) | · |
|  | [Trans Trip FE](measures/statistical-fitting/saom_transitive_triplets.html#cat_fe_trans_trip) | · |
|  | [Trans Trip FR](measures/statistical-fitting/saom_transitive_triplets.html#cat_fr_trans_trip) | · |
|  | [Trans Trip X](measures/statistical-fitting/saom_transitive_triplets.html#cat_trans_trip_x) | · |
|  | [Trans Trip1](measures/statistical-fitting/saom_transitive_triplets.html#cat_trans_trip1) | · |
|  | [Trans Trip2](measures/statistical-fitting/saom_transitive_triplets.html#cat_trans_trip2) | · |
| [Unspecified interaction effects](measures/statistical-fitting/saom_unspecified_interaction.html) | [Beh Unsp Int](measures/statistical-fitting/saom_unspecified_interaction.html#cat_beh_int_unsp) | · |
|  | [Unsp Int](measures/statistical-fitting/saom_unspecified_interaction.html#cat_int_unsp) | · |

## Temporal and events

20 measures in 14 concepts.

### Diffusion simulation

2 measures in 1 concepts.

| Concept | Variant | igraph | networkit |
|---|---|---|---|
| [Epidemic simulation (SIR, SEIR)](measures/temporal-and-events/epidemic_simulation.html) | [Epidemic Simulation SEIR](measures/temporal-and-events/epidemic_simulation.html#cat_epidemic_seir_simulation) |  | · |
|  | [Sir](measures/temporal-and-events/epidemic_simulation.html#cat_sir) | · |  |

### Relational event models

2 measures in 2 concepts.

| Concept | Variant | remstats | goldfish |
|---|---|---|---|
| [Relational event model fit](measures/temporal-and-events/rem_fit.html) | [Rem fit](measures/temporal-and-events/rem_fit.html#rem_fit) | ≠ | · |
| [Relational event statistics](measures/temporal-and-events/rem_statistic.html) | [Rem statistic](measures/temporal-and-events/rem_statistic.html#rem_statistic) | ✓ |  |

### Temporal descriptives

16 measures in 11 concepts.

| Concept | Variant | tsna | networkit | gephi |
|---|---|---|---|---|
| [Dynamic clustering coefficient](measures/temporal-and-events/dynamic_clustering.html) | [Dynamic Clustering Coefficient](measures/temporal-and-events/dynamic_clustering.html#cat_clustering_coefficient_dynamic) |  |  | · |
| [Edge formation and dissolution](measures/temporal-and-events/edge_formation_dissolution.html) | [T Edge Dissolution](measures/temporal-and-events/edge_formation_dissolution.html#cat_dissolution_edge_t) | · |  |  |
|  | [T Edge Formation](measures/temporal-and-events/edge_formation_dissolution.html#cat_edge_formation_t) | · |  |  |
| [Incremental maintenance on a changing graph](measures/temporal-and-events/dynamic_update.html) | [Incremental maintenance on a changing graph](measures/temporal-and-events/dynamic_update.html#dynamic_update) |  | · |  |
| [P-shift count](measures/temporal-and-events/p_shift_count.html) | [P Shift Count](measures/temporal-and-events/p_shift_count.html#cat_count_p_shift) | · |  |  |
| [Statistics over time (ergm, sna)](measures/temporal-and-events/temporal_statistic_series.html) | [T Ergm Stats](measures/temporal-and-events/temporal_statistic_series.html#cat_ergm_stats_t) | · |  |  |
|  | [T Sna Stats](measures/temporal-and-events/temporal_statistic_series.html#cat_sna_stats_t) | · |  |  |
| [Temporal degree](measures/temporal-and-events/temporal_degree.html) | [Dynamic Degree](measures/temporal-and-events/temporal_degree.html#cat_degree_dynamic) |  |  | · |
|  | [T Degree](measures/temporal-and-events/temporal_degree.html#cat_degree_t) | · |  |  |
| [Temporal edge density](measures/temporal-and-events/temporal_edge_density.html) | [T Edge Density](measures/temporal-and-events/temporal_edge_density.html#cat_density_edge_t) | · |  |  |
| [Temporal paths](measures/temporal-and-events/temporal_paths.html) | [Temporal paths](measures/temporal-and-events/temporal_paths.html#temporal_paths) | ✓ |  |  |
| [Temporal reach](measures/temporal-and-events/temporal_reach.html) | [Temporal reach](measures/temporal-and-events/temporal_reach.html#temporal_reach) | ✓ |  |  |
| [Time-projected network](measures/temporal-and-events/time_projected_network.html) | [Time Projected Network](measures/temporal-and-events/time_projected_network.html#cat_projected_time) | · |  |  |
| [Vertex, edge and tie duration](measures/temporal-and-events/activity_duration.html) | [Edge Duration](measures/temporal-and-events/activity_duration.html#cat_duration_edge) | · |  |  |
|  | [Tied Duration](measures/temporal-and-events/activity_duration.html#cat_duration_tied) | · |  |  |
|  | [Vertex Duration](measures/temporal-and-events/activity_duration.html#cat_duration) | · |  |  |

## Traversal, trees and DAGs

82 measures in 46 concepts.

### DAGs and topological order

28 measures in 16 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | rustworkx | sknetwork | jgrapht | boost | netrankr |
|---|---|---|---|---|---|---|---|---|---|---|
| [All topological orders](measures/traversal-trees-and-dags/all_topological_orders.html) | [All topological](measures/traversal-trees-and-dags/all_topological_orders.html#all_topological) | ✓ |  |  |  |  |  |  |  |  |
|  | [Topological sorts](measures/traversal-trees-and-dags/all_topological_orders.html#nxs_topological_sorts) | ✓ |  |  |  |  |  | · |  |  |
| [Antichains and antichain width](measures/traversal-trees-and-dags/antichains.html) | [Antichain width](measures/traversal-trees-and-dags/antichains.html#gb_antichain_width) | ✓ |  |  |  |  |  |  |  |  |
|  | [Antichains](measures/traversal-trees-and-dags/antichains.html#cat_antichains) | · |  |  |  |  |  |  |  |  |
| [Aperiodicity](measures/traversal-trees-and-dags/aperiodic.html) | [Gb aperiodic](measures/traversal-trees-and-dags/aperiodic.html#gb_aperiodic) | ✓ |  |  |  |  |  |  |  |  |
|  | [Gm aperiodic](measures/traversal-trees-and-dags/aperiodic.html#gm_aperiodic) | ✓ |  |  |  |  |  |  |  |  |
| [CD index](measures/traversal-trees-and-dags/cd_index.html) | [CD index](measures/traversal-trees-and-dags/cd_index.html#nxs_cd_index) | ≠ |  |  |  |  |  |  |  |  |
| [Chain decomposition](measures/traversal-trees-and-dags/chain_decomposition.html) | [Chain count](measures/traversal-trees-and-dags/chain_decomposition.html#gb_chain_count) | ✓ |  |  |  |  |  |  |  |  |
|  | [Chain decomposition](measures/traversal-trees-and-dags/chain_decomposition.html#cat_chain_decomposition) |  |  |  |  | · |  |  |  |  |
| [Colliders](measures/traversal-trees-and-dags/colliders.html) | [Colliders](measures/traversal-trees-and-dags/colliders.html#nxs_colliders) | ✓ |  |  |  |  |  |  |  |  |
| [DAG reachability](measures/traversal-trees-and-dags/dag_reachability.html) | [Dag reachability](measures/traversal-trees-and-dags/dag_reachability.html#nxs_dag_reachability) | ✓ |  |  |  |  |  |  |  |  |
| [DAG test](measures/traversal-trees-and-dags/is_dag.html) | [Is dag](measures/traversal-trees-and-dags/is_dag.html#is_dag) | ✓ | · | · | · | ✓ | · |  |  |  |
| [Lexicographic topological sort](measures/traversal-trees-and-dags/lexicographic_topological_sort.html) | [Lex topo](measures/traversal-trees-and-dags/lexicographic_topological_sort.html#gb_lex_topo) | ✓ |  |  |  |  |  |  |  |  |
|  | [Lexicographic](measures/traversal-trees-and-dags/lexicographic_topological_sort.html#lexicographic) | ✓ |  |  |  |  |  |  |  |  |
| [Longest path in a DAG](measures/traversal-trees-and-dags/dag_longest_path.html) | [Dag longest path](measures/traversal-trees-and-dags/dag_longest_path.html#cat_dag_longest_path) |  |  |  |  | · |  |  |  |  |
|  | [Dag longest path length](measures/traversal-trees-and-dags/dag_longest_path.html#cat_dag_length_longest_path) |  |  |  |  | · |  |  |  |  |
|  | [Dag weighted longest path](measures/traversal-trees-and-dags/dag_longest_path.html#cat_dag_longest_path_weighted) |  |  |  |  | · |  |  |  |  |
|  | [Dag weighted longest path length](measures/traversal-trees-and-dags/dag_longest_path.html#cat_dag_length_longest_path_weighted) |  |  |  |  | · |  |  |  |  |
|  | [Longest length](measures/traversal-trees-and-dags/dag_longest_path.html#longest_length) | ✓ |  |  |  |  |  |  |  |  |
|  | [Longest path](measures/traversal-trees-and-dags/dag_longest_path.html#longest_path) | ✓ |  |  |  |  |  |  |  |  |
|  | [Longest path len](measures/traversal-trees-and-dags/dag_longest_path.html#gb_longest_path_len) | ✓ |  |  |  |  |  |  |  |  |
| [Lowest common ancestor in DAGs](measures/traversal-trees-and-dags/dag_lca.html) | [Dag lca](measures/traversal-trees-and-dags/dag_lca.html#dag_lca) | ≠ |  |  |  |  |  |  |  |  |
| [Moral graph](measures/traversal-trees-and-dags/moral_graph.html) | [Moral edges](measures/traversal-trees-and-dags/moral_graph.html#gb_moral_edges) | ✓ |  |  |  |  |  |  |  |  |
| [Topological generations](measures/traversal-trees-and-dags/topological_generations.html) | [Generations](measures/traversal-trees-and-dags/topological_generations.html#generations) | ✓ |  |  |  |  |  |  |  |  |
|  | [Topo levels](measures/traversal-trees-and-dags/topological_generations.html#gb_topo_levels) | ✓ |  |  |  |  |  |  |  |  |
| [Topological sort](measures/traversal-trees-and-dags/topological_sort.html) | [Topological sort](measures/traversal-trees-and-dags/topological_sort.html#topological_sort) | ✓ | · | · | · | · |  |  | · |  |
| [Transitive closure](measures/traversal-trees-and-dags/transitive_closure.html) | [Closure](measures/traversal-trees-and-dags/transitive_closure.html#closure) | ✓ | · |  | · |  |  | · | · |  |
| [Transitive reduction](measures/traversal-trees-and-dags/transitive_reduction.html) | [Reduction](measures/traversal-trees-and-dags/transitive_reduction.html#reduction) | ✓ |  |  |  | · |  | · | · | · |

### Spanning trees and branchings

17 measures in 9 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | jgrapht | boost |
|---|---|---|---|---|---|---|---|---|---|
| [Capacitated minimum spanning tree](measures/traversal-trees-and-dags/capacitated_spanning_tree.html) | [Ahuja Orlin Sharma Capacitated Minimum Spanning Tree](measures/traversal-trees-and-dags/capacitated_spanning_tree.html#cat_ahuja_capacitated_minimum_orlin_sharma_spanning_tree) |  |  |  |  |  |  | · |  |
|  | [Esau Williams Capacitated Minimum Spanning Tree](measures/traversal-trees-and-dags/capacitated_spanning_tree.html#cat_capacitated_esau_minimum_spanning_tree_williams) |  |  |  |  |  |  | · |  |
| [Common spanning trees of two graphs](measures/traversal-trees-and-dags/common_spanning_trees.html) | [Two graphs common spanning trees](measures/traversal-trees-and-dags/common_spanning_trees.html#cat_common_spanning_tree_two) |  |  |  |  |  |  |  | · |
| [Maximum branching](measures/traversal-trees-and-dags/maximum_branching.html) | [Branching](measures/traversal-trees-and-dags/maximum_branching.html#branching) | ✓ |  |  |  |  |  |  |  |
|  | [Branching weight](measures/traversal-trees-and-dags/maximum_branching.html#gb_branching_weight) | ✓ |  |  |  |  |  |  |  |
|  | [Dag to branching](measures/traversal-trees-and-dags/maximum_branching.html#cat_branching_dag_to) | · |  |  |  |  |  |  |  |
|  | [Greedy branching](measures/traversal-trees-and-dags/maximum_branching.html#nxs_greedy_branching) | ✓ |  |  |  |  |  |  |  |
| [Minimum spanning tree](measures/traversal-trees-and-dags/minimum_spanning_tree.html) | [Mst weight](measures/traversal-trees-and-dags/minimum_spanning_tree.html#gb_mst_weight) | ✓ |  |  |  |  |  |  |  |
|  | [Spanning tree](measures/traversal-trees-and-dags/minimum_spanning_tree.html#spanning_tree) | ✓ | · | · | · | · | · | · | · |
|  | [Spanning weight](measures/traversal-trees-and-dags/minimum_spanning_tree.html#spanning_weight) | ✓ |  |  |  | ✓ | ✓ | ✓ | ✓ |
| [Number of spanning trees](measures/traversal-trees-and-dags/spanning_tree_count.html) | [Spanning trees](measures/traversal-trees-and-dags/spanning_tree_count.html#gb_spanning_trees) | ✓ |  |  |  |  |  |  |  |
| [Partition spanning tree](measures/traversal-trees-and-dags/partition_spanning_tree.html) | [Partition spanning tree](measures/traversal-trees-and-dags/partition_spanning_tree.html#cat_partition_spanning_tree) | · |  |  |  |  |  |  |  |
| [Random spanning tree](measures/traversal-trees-and-dags/random_spanning_tree.html) | [Random spanning tree](measures/traversal-trees-and-dags/random_spanning_tree.html#random_spanning_tree) | · | · |  | · |  |  |  | · |
|  | [Random Maximum Spanning Forest](measures/traversal-trees-and-dags/random_spanning_tree.html#cat_forest_maximum_random_spanning) |  |  |  |  | · |  |  |  |
|  | [Rst edge freq](measures/traversal-trees-and-dags/random_spanning_tree.html#rst_edge_freq) | ✓ |  |  |  |  |  |  |  |
| [Steiner tree](measures/traversal-trees-and-dags/steiner_tree.html) | [Steiner tree](measures/traversal-trees-and-dags/steiner_tree.html#steiner_tree) | · |  |  |  |  | · | · |  |
| [Union maximum spanning forest](measures/traversal-trees-and-dags/maximum_spanning_forest.html) | [Union Maximum Spanning Forest](measures/traversal-trees-and-dags/maximum_spanning_forest.html#cat_forest_maximum_spanning_union) |  |  |  |  | · |  |  |  |

### Traversal and orderings

16 measures in 5 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost |
|---|---|---|---|---|---|---|---|---|---|---|
| [Breadth-first search](measures/traversal-trees-and-dags/breadth_first_search.html) | [Beam](measures/traversal-trees-and-dags/breadth_first_search.html#trav_beam) | ✓ |  |  |  |  |  |  |  |  |
|  | [Bfs edges](measures/traversal-trees-and-dags/breadth_first_search.html#trav_bfs_edges) | ✓ | · | · | · | · | · | · | · | · |
|  | [Bfs iterator](measures/traversal-trees-and-dags/breadth_first_search.html#cat_bfs_iterator) |  |  |  | · |  |  |  |  |  |
|  | [Bfs labeled](measures/traversal-trees-and-dags/breadth_first_search.html#trav_bfs_labeled) | ✓ |  |  |  |  |  |  |  |  |
|  | [Bfs layers](measures/traversal-trees-and-dags/breadth_first_search.html#trav_bfs_layers) | ✓ |  |  |  |  | · |  |  |  |
|  | [Edge bfs](measures/traversal-trees-and-dags/breadth_first_search.html#trav_edge_bfs) | ✓ |  |  |  |  |  |  |  |  |
|  | [Random BFS](measures/traversal-trees-and-dags/breadth_first_search.html#cat_bfs_random) |  |  |  |  | · |  |  |  |  |
|  | [Reverse BFS](measures/traversal-trees-and-dags/breadth_first_search.html#cat_bfs_reverse) |  |  |  |  | · |  |  |  |  |
| [Depth-first search](measures/traversal-trees-and-dags/depth_first_search.html) | [Dfs events](measures/traversal-trees-and-dags/depth_first_search.html#trav_dfs_events) | ✓ |  |  |  |  |  |  | · |  |
|  | [Dfs iterator](measures/traversal-trees-and-dags/depth_first_search.html#cat_dfs_iterator) |  |  |  | · |  |  |  |  |  |
|  | [Edge dfs](measures/traversal-trees-and-dags/depth_first_search.html#trav_edge_dfs) | ✓ | · | · | · |  | · |  |  | · |
| [Random walks](measures/traversal-trees-and-dags/random_walks.html) | [Random walk generation and sampling](measures/traversal-trees-and-dags/random_walks.html#random_walk_sampling) |  |  |  |  |  |  |  | · | · |
|  | [Random walks](measures/traversal-trees-and-dags/random_walks.html#random_walk) | · | · | · |  |  | · |  |  |  |
| [Vertex orderings (max cardinality, degeneracy)](measures/traversal-trees-and-dags/vertex_orderings.html) | [Vertex orderings (max cardinality, degeneracy)](measures/traversal-trees-and-dags/vertex_orderings.html#vertex_orderings) |  |  |  |  |  |  |  | · | · |
|  | [Maximum cardinality search](measures/traversal-trees-and-dags/vertex_orderings.html#cat_cardinality_maximum_search) |  |  | · |  |  |  |  |  |  |
| [Walk counts](measures/traversal-trees-and-dags/walk_counts.html) | [Walks](measures/traversal-trees-and-dags/walk_counts.html#gb_walks) | ✓ |  |  |  | · |  |  |  |  |

### Tree structure and enumeration

21 measures in 16 concepts.

| Concept | Variant | networkx | igraph | pyigraph | graphtool | rustworkx | sknetwork | jgrapht |
|---|---|---|---|---|---|---|---|---|
| [Binomial tree](measures/traversal-trees-and-dags/binomial_tree.html) | [Binomial tree](measures/traversal-trees-and-dags/binomial_tree.html#cat_binomial_tree) | · |  |  |  | · |  |  |
| [Consensus tree](measures/traversal-trees-and-dags/consensus_tree.html) | [Consensus tree](measures/traversal-trees-and-dags/consensus_tree.html#cat_consensus_tree) |  | · |  |  |  |  |  |
| [Heavy path decomposition](measures/traversal-trees-and-dags/heavy_path_decomposition.html) | [Heavy Path Decomposition](measures/traversal-trees-and-dags/heavy_path_decomposition.html#cat_decomposition_heavy_path) |  |  |  |  |  |  | · |
| [Hierarchy tree](measures/traversal-trees-and-dags/hierarchy_tree.html) | [Get hierarchy tree](measures/traversal-trees-and-dags/hierarchy_tree.html#cat_hierarchy_tree) |  |  |  | · |  |  |  |
| [Join trees](measures/traversal-trees-and-dags/join_trees.html) | [Join trees](measures/traversal-trees-and-dags/join_trees.html#cat_join_tree) | · |  |  |  |  |  |  |
| [Lowest common ancestor in trees](measures/traversal-trees-and-dags/tree_lca.html) | [Tree lca](measures/traversal-trees-and-dags/tree_lca.html#tree_lca) | ✓ |  |  |  |  |  | · |
|  | [Nxs tree lca](measures/traversal-trees-and-dags/tree_lca.html#nxs_tree_lca) | ✓ |  |  |  |  |  |  |
| [Number of nonisomorphic trees](measures/traversal-trees-and-dags/nonisomorphic_trees.html) | [Number of nonisomorphic trees](measures/traversal-trees-and-dags/nonisomorphic_trees.html#cat_nonisomorphic_tree) | · |  |  |  |  |  |  |
| [Predecessor tree](measures/traversal-trees-and-dags/predecessor_tree.html) | [Predecessor tree](measures/traversal-trees-and-dags/predecessor_tree.html#cat_predecessor_tree) |  |  |  | · |  |  |  |
| [Prufer sequences](measures/traversal-trees-and-dags/prufer_sequence.html) | [From prufer](measures/traversal-trees-and-dags/prufer_sequence.html#nxs_from_prufer) | ✓ | · | · |  |  |  | · |
|  | [Prufer](measures/traversal-trees-and-dags/prufer_sequence.html#nxs_prufer) | ✓ |  | · |  |  |  |  |
| [Random power-law trees](measures/traversal-trees-and-dags/random_powerlaw_tree.html) | [Random powerlaw tree](measures/traversal-trees-and-dags/random_powerlaw_tree.html#cat_powerlaw_random_tree) | · |  |  |  |  |  |  |
|  | [Random powerlaw tree sequence](measures/traversal-trees-and-dags/random_powerlaw_tree.html#cat_powerlaw_random_sequence_tree) | · |  |  |  |  |  |  |
| [Random rooted forests](measures/traversal-trees-and-dags/random_rooted_forest.html) | [Random labeled rooted forest](measures/traversal-trees-and-dags/random_rooted_forest.html#cat_forest_labeled_random_rooted) | · |  |  |  |  |  |  |
|  | [Random unlabeled rooted forest](measures/traversal-trees-and-dags/random_rooted_forest.html#cat_forest_random_rooted_unlabeled) | · |  |  |  |  |  |  |
| [Tree broadcast time and center](measures/traversal-trees-and-dags/tree_broadcast.html) | [Broadcast time](measures/traversal-trees-and-dags/tree_broadcast.html#gb_broadcast_time) | ✓ |  |  |  |  |  |  |
|  | [Tree broadcast center](measures/traversal-trees-and-dags/tree_broadcast.html#cat_broadcast_center_tree) | · |  |  |  |  |  |  |
| [Tree centroid](measures/traversal-trees-and-dags/tree_centroid.html) | [Tree centroid](measures/traversal-trees-and-dags/tree_centroid.html#nxs_tree_centroid) | ✓ |  |  |  |  |  |  |
| [Tree sampling divergence](measures/traversal-trees-and-dags/tree_sampling_divergence.html) | [Tree sampling divergence](measures/traversal-trees-and-dags/tree_sampling_divergence.html#cat_divergence_sampling_tree) |  |  |  |  |  | · |  |
| [Tree, forest and arborescence tests](measures/traversal-trees-and-dags/forest_tests.html) | [Forest flags](measures/traversal-trees-and-dags/forest_tests.html#nxs_forest_flags) | ✓ | · | · |  |  |  |  |
| [Unfold tree](measures/traversal-trees-and-dags/tree_unfold.html) | [Unfold tree](measures/traversal-trees-and-dags/tree_unfold.html#cat_tree_unfold) |  | · | · |  |  |  |  |

## Two-mode and bipartite

14 measures in 10 concepts.

### Bipartite structure

11 measures in 9 concepts.

| Concept | Variant | networkx | networkit | ucinet | tnet |
|---|---|---|---|---|---|
| [Bipartite degree and neighbor indices](measures/two-mode-and-bipartite/bipartite_degree_indices.html) | [Total Neighbors Index](measures/two-mode-and-bipartite/bipartite_degree_indices.html#cat_neighbors_total) |  | · |  |  |
|  | [UDegree Index](measures/two-mode-and-bipartite/bipartite_degree_indices.html#cat_degree_u) |  | · |  |  |
|  | [VDegree Index](measures/two-mode-and-bipartite/bipartite_degree_indices.html#cat_degree_v) |  | · |  |  |
| [Bipartite modularity](measures/two-mode-and-bipartite/bipartite_modularity.html) | [Bipartite modularity](measures/two-mode-and-bipartite/bipartite_modularity.html#bipartite_modularity) | ✓ |  |  |  |
| [BiRank](measures/two-mode-and-bipartite/birank.html) | [Birank](measures/two-mode-and-bipartite/birank.html#birank) | ✓ |  |  |  |
| [Butterflies](measures/two-mode-and-bipartite/butterflies.html) | [Butterflies](measures/two-mode-and-bipartite/butterflies.html#butterflies) | ✓ |  |  |  |
| [Latapy clustering](measures/two-mode-and-bipartite/latapy_clustering.html) | [Latapy clustering](measures/two-mode-and-bipartite/latapy_clustering.html#latapy_clustering) | ✓ |  |  |  |
| [Robins-Alexander clustering](measures/two-mode-and-bipartite/robins_alexander.html) | [Robins alexander](measures/two-mode-and-bipartite/robins_alexander.html#robins_alexander) | ✓ |  |  |  |
| [Spectral bipartivity](measures/two-mode-and-bipartite/spectral_bipartivity.html) | [Spectral bipartivity](measures/two-mode-and-bipartite/spectral_bipartivity.html#spectral_bipartivity) | ✓ |  |  |  |
| [Two-mode clustering coefficients (six-cycle)](measures/two-mode-and-bipartite/twomode_clustering.html) | [Two-mode clustering coefficients (six-cycle)](measures/two-mode-and-bipartite/twomode_clustering.html#twomode_cc) |  |  |  | · |
| [Two-mode core-periphery and bi-cliques](measures/two-mode-and-bipartite/twomode_core_biclique.html) | [Two-mode core-periphery, bi-cliques, two-mode equivalence](measures/two-mode-and-bipartite/twomode_core_biclique.html#twomode_core_biclique) |  |  | · |  |

### Projection

3 measures in 1 concepts.

| Concept | Variant | networkx | igraph | pyigraph | ergm | graphtool | ucinet | tnet |
|---|---|---|---|---|---|---|---|---|
| [Bipartite projection](measures/two-mode-and-bipartite/bipartite_projection.html) | [Project](measures/two-mode-and-bipartite/bipartite_projection.html#project) | ∅ | ∅ | · | · |  | · | ✓ |
|  | [Projection](measures/two-mode-and-bipartite/bipartite_projection.html#projection) | ✓ |  |  |  | · |  |  |
|  | [Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine)](measures/two-mode-and-bipartite/bipartite_projection.html#projection_weights) |  |  |  |  |  | · | · |
{% endraw %}
