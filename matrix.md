---
title: Capability matrix
layout: default
nav_order: 2
---

{% raw %}
# Capability matrix

✓ checked, agrees; ≠ checked, differs by a documented convention; ✗ checked, defect found; ∅ checked, no value on the compared inputs; · reported in the tool's documentation (not run); blank: not known to implement it.

Columns are tool identifiers (see [Tools](tools/)). Rows link to the measure pages.

## Centrality

92 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | rsiena | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | graphblas | bct | bctpy | gephi | ucinet | tnet | netrankr | keyplayer | centiserve |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Approximate betweenness (sampling)](measures/betweenness_approx.html) |  |  |  |  |  |  |  | · |  |  | · | · |  |  |  |  |  |  |  |  |  |
| [Approximate, top-k and group closeness](measures/closeness_approx.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Betweenness](measures/betweenness.html) | ≠ | ≠ | ✓ | ≠ |  | · | · | ∅ | ✓ | · | ≠ | ≠ |  | ≠ | ≠ | ≠ | · | ✓ | ≠ |  |  |
| [Betweenness simple](measures/betweenness_simple.html) | ✓ |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Betweenness subset](measures/cx_betweenness_subset.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Bonacich](measures/bonacich.html) |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Centralization](measures/cat_centralization.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Closeness](measures/closeness.html) | ✓ | ✓ | ✓ | ✓ |  |  | · | ✓ | ✓ | ≠ | ≠ | ≠ |  |  |  | ≠ | · | · | ≠ |  | · |
| [Closeness latora](measures/cat_closeness_latora.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Closeness residual](measures/cat_closeness_residual.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Communicability](measures/cx_communicability.html) | ✓ | · |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  | ≠ |  |  |
| [Communicability betweenness](measures/cx_communicability_betweenness.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |
| [Communitycent](measures/cat_communitycent.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Concent](measures/cat_concent.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Cover Hub Dominance](measures/cat_cover_dominance_hub.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Current flow approx](measures/cx_current_flow_approx.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Current flow closeness](measures/cx_current_flow_closeness.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  | · |
| [Current flow subset](measures/cx_current_flow_subset.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cx current flow](measures/cx_current_flow.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |
| [Cx laplacian](measures/cx_laplacian.html) | ✓ |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Decay](measures/cat_decay.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Degree simple](measures/degree_simple.html) |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diffusion](measures/cat_diffusion.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  | · |  |
| [Diffusion Classifier](measures/cat_classifier_diffusion.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Diffusion degree](measures/cat_degree_diffusion.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Diffusion efficiency](measures/cat_diffusion_efficiency.html) |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Dispersion](measures/cx_dispersion.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edge betweenness](measures/edge_betweenness.html) | ≠ | ✓ | · |  |  |  |  | ✓ | ✓ |  | · |  |  | · |  |  | · |  |  |  |  |
| [Edge load](measures/cx_edge_load.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edge percolation](measures/cat_edge_percolation.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Eigenvector](measures/eigenvector.html) | ∅ | ∅ | ≠ | ≠ |  |  | · | · | ✓ |  | · |  | ≠ | · |  | ≠ | · |  |  |  |  |
| [Flow betweenness](measures/flow_betweenness.html) |  |  |  | ≠ |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Google](measures/nxp_google.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Graphcent](measures/cat_graphcent.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Group / betweenness](measures/group-betweenness.html) | ≠ |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Group / closeness](measures/group-closeness.html) | ✓ |  |  |  |  |  |  | ✓ | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Group / degree](measures/group-degree.html) | ✓ |  |  |  |  |  |  | ✓ | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Group out degree centrality](measures/cat_degree_group_out.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Harmonic](measures/harmonic.html) | ✓ | ✓ | ✓ | ≠ |  |  |  | ✓ |  |  | ✓ |  |  |  |  | ≠ | · |  | ✓ |  | ✓ |
| [Hits](measures/hits.html) | ✓ | ∅ | ≠ |  |  |  | · |  | ∅ | ≠ |  |  | ≠ |  |  | ≠ | · |  |  |  |  |
| [Hub Dominance](measures/cat_dominance_hub.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hubbell](measures/cat_hubbell.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Incremental closeness centrality](measures/cat_closeness_incremental.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Induced centrality](measures/induced_centrality.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Information centrality](measures/information_centrality.html) | ✓ |  |  | ≠ |  |  |  |  |  |  |  |  |  |  |  |  | · |  | ✓ |  |  |
| [Katz](measures/katz.html) | ✓ | ∅ |  |  |  |  | · | · | ∅ | · | · |  | ≠ |  |  |  | · |  |  |  | ✓ |
| [KPath Centrality](measures/cat_k_path.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kpp\_optimum / distance\_fragmentation](measures/kpp_optimum-distance_fragmentation.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |
| [Kpp\_optimum / distance\_reach](measures/kpp_optimum-distance_reach.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |
| [Kpp\_optimum / fragmentation](measures/kpp_optimum-fragmentation.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Kpp\_optimum / m\_reach](measures/kpp_optimum-m_reach.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |
| [Kpp\_single / distance\_fragmentation](measures/kpp_single-distance_fragmentation.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ≠ |  |
| [Kpp\_single / distance\_reach](measures/kpp_single-distance_reach.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ≠ |  |
| [Kpp\_single / fragmentation](measures/kpp_single-fragmentation.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Kpp\_single / m\_reach](measures/kpp_single-m_reach.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |
| [Leverage](measures/cat_leverage.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Lincent](measures/cat_lincent.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Load](measures/cx_load.html) | ✓ |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Loadcent](measures/cat_loadcent.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Lobby](measures/cat_lobby.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Local and approximate PageRank](measures/local_pagerank.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Markovcent](measures/cat_markovcent.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Mreach closeness](measures/cat_closeness_mreach.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Neighborhood inclusion, positional dominance, rank intervals](measures/partial_ranking.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Net\_centrality\_table() (raw and normalised columns)](measures/centrality_table.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Newman weighted closeness centrality](measures/cat_closeness_newman_weighted.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nxp eigenvector](measures/nxp_eigenvector.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nxp hits](measures/nxp_hits.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nxp katz](measures/nxp_katz.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nxp pagerank](measures/nxp_pagerank.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Opsahl alpha-tuned degree and closeness](measures/opsahl_alpha.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Page Rank Classifier](measures/cat_classifier_page_rank.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Pagerank](measures/pagerank.html) | ≠ | ∅ | ✓ |  |  |  | · | ∅ | ≠ | ≠ | ✓ | · | ≠ |  |  | ✗ | · |  |  |  |  |
| [Partition Hub Dominance](measures/cat_dominance_hub_partition.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Percolation](measures/cx_percolation.html) | ✓ |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Permanence Centrality](measures/cat_permanence.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Radiality](measures/cat_radiality.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Reach](measures/reach.html) | ✓ | ✓ |  | · |  |  |  |  | · |  |  |  |  |  |  |  | · |  |  |  |  |
| [Reaching](measures/cx_reaching.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Resistance](measures/cx_resistance.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |
| [Resistance-based and spectral edge/vertex scores](measures/resistance_based.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Salsa](measures/cat_salsa.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Second order](measures/cx_second_order.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Strength](measures/strength.html) | ✓ | ∅ | ✓ |  |  |  |  | ∅ |  |  |  |  |  |  |  | ✓ | · | ✓ |  |  |  |
| [Subgraph centrality and stress centrality](measures/subgraph_stress_centrality.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Swan closeness](measures/cat_closeness_swan.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Theoretical maximum of centralization](measures/centralization_tmax.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tripercent](measures/cat_tripercent.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trophic](measures/cx_trophic.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Valente-Foreman integration and radiality](measures/valente_foreman.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Voterank](measures/cx_voterank.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Walks ppr](measures/walks_ppr.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Cohesion and subgroups

44 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | rsiena | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | bct | bctpy | ucinet | centiserve |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [All cliques](measures/all_cliques.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [All triads](measures/cat_all_triads.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Beh Dense Triads](measures/cat_beh_dense_triads.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Clique census](measures/cat_census_clique.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Clique co-membership and overlap matrices](measures/clique_overlap.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Clique Detect](measures/cat_clique_detect.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Clique number](measures/clique_number.html) | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  |  | ✓ |  |  |  |  |  |
| [Clique State](measures/cat_clique_state.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Cocitation and bibliographic coupling](measures/cocitation.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cohesive blocks](measures/cat_blocks_cohesive.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Core subset](measures/core_subset.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Coreness](measures/coreness.html) | ≠ | ✓ | ✓ | · |  |  | · | ∅ | ≠ | ≠ | ✓ | · | ≠ | ≠ | · |  |
| [Count max cliques](measures/cat_clique_count_max.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Crossclique](measures/cat_crossclique.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Cut quality (conductance, expansion, boundary)](measures/cut_quality.html) | · |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Dense Triads](measures/cat_dense_triads.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Factions](measures/cat_factions.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Factions errors](measures/factions_errors.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Generate triadic closure](measures/cat_closure_generate_triadic.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Graphlet basis and projection](measures/graphlets.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is clique](measures/cat_clique_is.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [K plexes](measures/k_plexes.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [K truss](measures/k_truss.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Lambda connectivity](measures/lambda_connectivity.html) | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Lambda sets](measures/lambda_sets.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Largest weighted cliques](measures/cat_clique_largest_weighted.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Liststriads](measures/cat_liststriads.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Max cliques](measures/max_cliques.html) | ✓ | ✓ | ✓ |  |  |  | · | ∅ |  | · | ✓ | · |  |  | · |  |
| [Max weight clique](measures/max_weight_clique.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Max weight clique nodes](measures/max_weight_clique_nodes.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mixed Triad Census](measures/cat_census_mixed_triad.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Motif census](measures/motif_census.html) |  | · | · |  |  |  | · |  |  |  |  |  | · |  |  |  |
| [N clans](measures/n_clans.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [N cliques](measures/n_cliques.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Node clique number](measures/node_clique_number.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nx cliques order](measures/nx_cliques_order.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Onion](measures/onion.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Opentriad](measures/cat_opentriad.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Sim Dense Triads](measures/cat_dense_sim_triads.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Simmelian ties](measures/simmelian.html) |  |  |  | · | · |  |  |  |  |  |  |  |  |  | · |  |
| [Triad type](measures/cat_triad_type.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Triads by type](measures/cat_triads_type.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Truss](measures/truss.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Weighted cliques](measures/cat_clique_weighted.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Communities

66 measures.

| Measure | networkx | igraph | pyigraph | graphtool | networkit | sknetwork | jgrapht | bct | gephi | ucinet | cdlib | infomap | graspologic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Allpaths](measures/cat_allpaths.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Bipartite Partitioning](measures/cat_bipartite_partitioning.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Block (blockmodel from partition), Reduce](measures/cat_block_blockmodel_from_partition_reduce.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Clique communities](measures/cat_clique_community.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Cnx current flow](measures/cnx_current_flow.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cnx edge betweenness](measures/cnx_edge_betweenness.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cnx girvan newman](measures/cnx_girvan_newman.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cnx label propagation](measures/cnx_label_propagation.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Community voronoi](measures/cat_community_voronoi.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Compare partitions](measures/compare_partitions.html) |  | ≠ | · |  | · |  |  |  |  |  | ≠ |  |  |
| [Dag All Paths Counter](measures/cat_all_counter_dag_path.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Fast greedy](measures/fast_greedy.html) | ∅ | ≠ | · |  |  |  |  |  |  | · |  |  |  |
| [Fluid communities](measures/fluid_communities.html) | ✓ | ✓ | · |  |  |  |  |  |  |  |  |  |  |
| [Girvan newman](measures/girvan_newman.html) | ✓ | ✓ | · |  |  |  | · |  |  | · |  |  |  |
| [Girvan newman cut](measures/girvan_newman_cut.html) |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy modularity](measures/cnx_greedy_modularity.html) | ✓ |  |  |  |  |  | · |  |  |  |  |  |  |
| [Infomap](measures/infomap.html) |  | ∅ | · |  |  |  |  |  |  |  |  | ✓ |  |
| [Intrapartition Density](measures/cat_density_intrapartition.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Is partition (community)](measures/cat_is_partition-community.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Isolated Interpartition Conductance](measures/cat_conductance_interpartition_isolated.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Isolated Interpartition Expansion](measures/cat_expansion_interpartition_isolated.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [K clique](measures/cnx_k_clique.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [K Core Community Detection](measures/cat_community_core_detection_k.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Kernighan lin](measures/cnx_kernighan_lin.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Label propagation](measures/label_propagation.html) | ≠ | ∅ | · |  | · | · | · |  |  | · |  |  |  |
| [Label spreading](measures/nxo_label_spreading.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Leading eigen](measures/leading_eigen.html) |  | ✓ | · |  |  |  |  |  |  | · |  |  |  |
| [Leiden](measures/leiden.html) | ✓ | ∅ | · |  | · | · |  |  |  | · |  |  |  |
| [Leiden seeded](measures/cnx_leiden_seeded.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Link communities](measures/cat_community_link.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Local Partition Coverage](measures/cat_coverage_local_partition.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [LocalGreedy, Moca, partition polishing, initial partitions](measures/ucinet_community_extras.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Louvain Hierarchy](measures/cat_hierarchy_louvain.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Louvain Iteration](measures/cat_iteration_louvain.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Louvain modularity](measures/louvain_modularity.html) | ≠ | · | · |  | · | · |  | · |  | · |  |  |  |
| [Louvain quality](measures/louvain_quality.html) | ≠ | ≠ |  |  |  |  |  |  | ≠ |  |  |  |  |
| [Louvain seeded](measures/cnx_louvain_seeded.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Lukes](measures/cnx_lukes.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Modularity](measures/modularity.html) | ≠ | ✓ | ✓ | · | ∅ | ≠ | · | · | · |  | ≠ |  | ≠ |
| [Modularity nx](measures/cnx_modularity_nx.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Modularity State](measures/cat_modularity_state.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Naive greedy](measures/cnx_naive_greedy.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Naive greedy nx](measures/cnx_naive_greedy_nx.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nested partition overlap](measures/cat_nested_overlap_partition.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Nested partition overlap center](measures/cat_center_nested_overlap_partition.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Optimal modularity](measures/optimal_modularity.html) |  | ✓ | · |  |  |  |  |  |  |  |  |  |  |
| [Overlapping](measures/cnx_overlapping.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Partition Centroid State](measures/cat_centroid_partition_state.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Partition counts](measures/cnx_partition_counts.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Partition distance](measures/cat_distance_partition.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Partition entropy](measures/cat_entropy_partition.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Partition Fragmentation](measures/cat_fragmentation_partition.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Partition Mode State](measures/cat_mode_partition_state.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Partition overlap](measures/cat_overlap_partition.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Partition overlap center](measures/cat_center_overlap_partition.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Partition quality (coverage, performance)](measures/partition_quality.html) | · |  |  |  | · |  |  |  |  |  |  |  |  |
| [Partition spanning tree](measures/cat_partition_spanning_tree.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Randomized partitioning (approximate)](measures/cat_partitioning_randomized-approximate.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same Community Index](measures/cat_community_same.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Seeded labels](measures/cnx_seeded_labels.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Set Conductance](measures/cat_conductance_set.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Spectral modularity bipartition (community)](measures/cat_bipartition_modularity_spectral-community.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Spectral Partitioner](measures/cat_partitioner_spectral.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Spinglass](measures/spinglass.html) |  | ✓ | · |  |  |  |  |  |  |  |  |  |  |
| [Voronoi](measures/voronoi.html) |  | ≠ |  |  |  |  |  |  |  |  |  |  |  |
| [Walktrap](measures/walktrap.html) |  | ≠ | · |  |  |  |  |  |  |  |  |  |  |

## Components and connectivity

53 measures.

| Measure | networkx | igraph | pyigraph | sna | graphtool | networkit | rustworkx | jgrapht | boost | bct | ucinet | netrankr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [All node cuts (connectivity)](measures/cat_all_cut-connectivity.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [All pairs node](measures/all_pairs_node.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Attracting](measures/attracting.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Attracting flags](measures/attracting_flags.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Average node](measures/average_node.html) | ✓ |  |  |  | · |  |  |  |  |  |  |  |
| [Bicomponents](measures/bicomponents.html) | ✓ | ✓ | · | · | · | ∅ | · | · | · |  | · |  |
| [Biconnected](measures/nxo_biconnected.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Bridge components (connectivity)](measures/cat_bridge_component-connectivity.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Bridges](measures/bridges.html) | ✓ | ∅ | · |  |  |  | ✓ |  |  |  |  |  |
| [Capacity Scaling Minimum Cost Flow](measures/cat_capacity_cost_flow_minimum_scaling.html) |  |  |  |  |  |  |  | · |  |  |  |  |
| [Cohesive blocking (Moody-White)](measures/cohesive_blocking.html) |  | · |  |  |  |  |  |  |  |  |  |  |
| [Condensation](measures/condensation.html) | ✓ |  |  |  | · |  | · |  | · |  |  |  |
| [Connectivity](measures/connectivity.html) | ✓ | · | · |  |  |  |  |  | · |  | · |  |
| [Count components](measures/cat_component_count.html) |  | · |  |  |  |  |  |  |  |  |  |  |
| [Cut measures](measures/cut_measures.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Cut points](measures/cut_points.html) | ✓ | ∅ | ✓ | ✓ |  |  | ✓ |  | ✓ |  | · |  |
| [Disjoint paths](measures/disjoint_paths.html) | ✓ | · |  |  |  |  |  | · |  |  |  |  |
| [Dominator](measures/cat_dominator.html) |  |  | · |  |  |  |  |  |  |  |  |  |
| [Edge cut](measures/edge_cut.html) | ✓ |  |  |  |  | · |  |  |  |  |  |  |
| [Experienceflows](measures/cat_experienceflows.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Find minimal d separator](measures/cat_d_find_minimal_separator.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Flow coef](measures/cat_coef_flow.html) |  |  |  |  |  |  |  |  |  | · |  |  |
| [Flowsim](measures/cat_flowsim.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Fragmentation](measures/fragmentation.html) |  | ∅ |  |  |  |  |  |  |  |  | · |  |
| [Gomory hu](measures/gomory_hu.html) | ✓ |  | · |  |  |  |  | · |  |  |  |  |
| [Gomory hu values](measures/gomory_hu_values.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Gusfield Equivalent Flow Tree](measures/cat_equivalent_flow_gusfield_tree.html) |  |  |  |  |  |  |  | · |  |  |  |  |
| [Is attracting component](measures/cat_attracting_component_is.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Is kl connected](measures/cat_connected_is_kl.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Is locally k edge connected (connectivity)](measures/cat_connected_edge_is_k_locally-connectivity.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Is minimal d separator](measures/cat_d_is_minimal_separator.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Is semi connected](measures/cat_connected_is_semi.html) |  |  |  |  |  |  | · |  |  |  |  |  |
| [K components](measures/k_components.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [K edge components](measures/k_edge_components.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [KConnectivity Flow Algorithm](measures/cat_connectivity_flow_k.html) |  |  |  |  |  |  |  | · |  |  |  |  |
| [Local bridges](measures/local_bridges.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Local connectivity](measures/local_connectivity.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Max flow](measures/max_flow.html) | ✓ | · | · | · | · | · |  |  | · |  |  |  |
| [Max flow min cost](measures/max_flow_min_cost.html) | ✓ |  |  |  |  |  |  |  | · |  |  |  |
| [Min cut](measures/min_cut.html) | ✓ | · | · |  | · |  | · | · | · |  |  |  |
| [Min node cut](measures/min_node_cut.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Node cut](measures/node_cut.html) | ✓ | · | · |  |  |  |  |  |  |  |  |  |
| [Norm Cut State](measures/cat_cut_norm_state.html) |  |  |  |  | · |  |  |  |  |  |  |  |
| [Number attracting components](measures/cat_attracting_component.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Padberg Rao Odd Minimum Cutset](measures/cat_cutset_minimum_odd_padberg_rao.html) |  |  |  |  |  |  |  | · |  |  |  |  |
| [Parallel Connected Components](measures/cat_component_connected_parallel.html) |  |  |  |  |  | · |  |  |  |  |  |  |
| [Semiconnected](measures/semiconnected.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [St edge cut](measures/st_edge_cut.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [St Mincuts](measures/cat_mincuts_st.html) |  | · |  |  |  |  |  |  |  |  |  |  |
| [St node cut](measures/st_node_cut.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Strong partition](measures/strong_partition.html) |  |  |  |  |  |  |  | ✓ | ✓ |  |  |  |
| [Swan connectivity](measures/cat_connectivity_swan.html) |  |  |  |  |  |  |  |  |  |  |  | · |
| [Tree Dynamic Connectivity](measures/cat_connectivity_dynamic_tree.html) |  |  |  |  |  |  |  | · |  |  |  |  |

## Data transforms

19 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | graphtool | networkit | rustworkx | jgrapht | ucinet | tnet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Attribute to matrix (same, difference, sender, receiver)](measures/attribute_matrix.html) |  |  |  |  |  |  |  |  |  | · |  |
| [Dichotomise](measures/cat_dichotomise.html) |  |  |  |  |  |  |  |  |  |  | · |
| [Dichotomize](measures/cat_dichotomize.html) |  |  |  |  |  |  |  |  |  | · |  |
| [Full symmetrize method set and dichotomize by density](measures/symmetrize_methods.html) |  |  |  | · | · |  |  |  |  | · |  |
| [Graph complement](measures/graph_complement.html) |  |  |  |  |  |  |  |  | · |  |  |
| [Graph complement](measures/op_complement.html) | · | · | · |  |  |  |  | · |  |  |  |
| [Graph products](measures/op_graph_product.html) | · |  |  |  |  |  |  | · |  |  |  |
| [Graph sym difference](measures/cat_difference_sym.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Line graph](measures/line_graph.html) | ✓ | · | · |  |  | · |  | · | · |  |  |
| [Local sparsification (L-Spar)](measures/local_sparsification.html) |  |  |  |  |  |  |  |  |  | · |  |
| [Multiplex coding of several relations into one matrix](measures/multiplex_coding.html) |  |  |  |  |  |  |  |  |  | · |  |
| [Normalize ties (row, column, matrix; sum, mean, max, z, Euclidean, IPF)](measures/normalize_ties.html) |  |  |  |  |  |  |  |  |  | · |  |
| [Op compose](measures/op_compose.html) | · | · | · |  |  |  |  |  |  |  |  |
| [Op difference](measures/op_difference.html) | ✓ | · | · |  |  | · | · |  |  |  |  |
| [Op intersection](measures/op_intersection.html) | ✓ | · | · |  |  | · |  |  |  |  |  |
| [Op union](measures/op_union.html) | ✓ | · | · |  |  | · |  | · |  |  |  |
| [Power](measures/cat_power.html) | · |  |  |  |  |  |  |  |  |  |  |
| [Reverse](measures/cat_reverse.html) | · |  |  |  |  |  |  |  |  |  |  |
| [Tucker congruence, factor rotation, iterative proportional fitting, state transitions](measures/matrix_utils.html) |  |  |  |  |  |  |  |  |  | · |  |

## Descriptive statistics

38 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | tsna | rsiena | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | graphblas | bct | bctpy | gephi | ucinet | tnet | netrankr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Average clustering](measures/average_clustering.html) | ✓ | ∅ | ✓ |  |  |  |  |  | ✓ |  |  | ≠ | ≠ | ✓ | ≠ | ✓ | ≠ | · |  |  |
| [Centralization / betweenness](measures/centralization-betweenness.html) |  | ✓ |  | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Centralization / closeness](measures/centralization-closeness.html) |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Centralization / degree](measures/centralization-degree.html) |  | ∅ |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Centralization eigenvector](measures/centralization_eigenvector.html) |  | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Clustering](measures/clustering.html) | ✓ | ∅ | ✓ |  |  |  |  | · | ✓ |  | · | ≠ | ≠ | ✓ | ≠ | ✓ | ≠ | · | ✓ |  |
| [Compactness](measures/compactness.html) | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Components](measures/components.html) | ✓ | ∅ | ✓ | · |  |  |  | · | ✓ | ✓ | ✓ | · | · |  | · |  | ✓ | · |  |  |
| [Degree](measures/degree.html) | ✓ | ∅ | ✓ | ≠ | · |  |  |  | ✓ | · |  |  | · |  | ≠ |  | ✓ | · | · |  |
| [Degree distribution and its summary statistics](measures/degree_distribution.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Density](measures/density.html) | ≠ | ∅ | ✓ | ≠ | ≠ |  | · |  | ✓ |  |  |  |  |  | ≠ | ✓ | ✓ | · |  |  |
| [Directed clustering](measures/nxo_directed_clustering.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  | ≠ |  | ✓ |  |  |  |  |
| [Dyad census (mutual, asymmetric, null)](measures/dyad_census.html) |  | · | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Effective resistance](measures/cx_effective_resistance.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego size](measures/ego_size.html) | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Generate knn](measures/cat_generate_knn.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Intransitive](measures/cat_intransitive.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kemeny](measures/cx_kemeny.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Knn](measures/cat_knn.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)](measures/krackhardt_dimensions.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Node reciprocity](measures/nxo_node_reciprocity.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  | · |  |  |
| [Normalized reciprocity and transitivity, DKS transitivity, cyclicity](measures/ucinet_cohesion_variants.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Reciprocity](measures/reciprocity.html) | ✓ | ∅ | ✓ | ≠ | ✓ |  |  | · |  |  |  |  |  | ✓ |  |  |  | · |  |  |
| [Resource efficiency](measures/cat_efficiency_resource.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Rout efficiency](measures/cat_efficiency_rout.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Small world observed](measures/small_world_observed.html) | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Square clustering](measures/square_clustering.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  | ≠ |  |  |  |  |  |  |
| [Successor transitivity](measures/nxo_successor_transitivity.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Swan efficiency](measures/cat_efficiency_swan.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [T Edge Density](measures/cat_density_edge_t.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Transitive](measures/cat_transitive.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Transitiveties](measures/cat_transitiveties.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Transitiveweights](measures/cat_transitiveweights.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Transitivity](measures/transitivity.html) | ✓ | ∅ | ✓ | · | ✓ |  |  | · | ✓ | ✓ |  | ≠ |  | ✓ | ≠ | ✓ |  | · |  |  |
| [Triad census](measures/triad_census.html) | ✓ | ∅ | ≠ | ≠ | ✓ |  | · |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Triangles](measures/nxo_triangles.html) | ✓ | · | · |  | · |  |  |  |  |  | · |  |  | ✓ |  |  | ≠ |  |  |  |
| [Trust transitivity](measures/cat_transitivity_trust.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Weak and strong transitivity; directed and weighted clustering conventions](measures/sna_transitivity.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Ego networks

1 measures.

| Measure | ucinet | egor |
|---|---|---|
| [Ego composition: alter shares, Blau and Shannon heterogeneity, IQV](measures/ego_composition.html) | · | · |

## Generators and rewiring

142 measures.

| Measure | networkx | igraph | pyigraph | sna | tsna | graphtool | networkit | rustworkx | jgrapht | boost | bct | gephi | ucinet | netrankr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Barbell graph](measures/cat_barbell.html) | · |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Bipartite degree-sequence realization](measures/gen_realize_bipartite.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Caveman graph](measures/cat_caveman.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chordal cycle graph](measures/cat_chordal_cycle.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chordal ring generator](measures/gen_chordal_ring.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chung-Lu (expected degree) generator](measures/gen_chung_lu.html) | · | · | · |  |  |  | · |  |  |  |  |  |  |  |
| [Circulant graph generator](measures/gen_circulant.html) | · | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Circular ladder graph](measures/cat_circular_ladder.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Citation-type growth generators](measures/gen_citation.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Clique, regular and bow-tie generators; all graphs of size n](measures/misc_generators.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Clustering Generator](measures/cat_clustering_generator.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Complete multipartite graph generator](measures/gen_complete_multipartite.html) | · | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Configuration model](measures/gen_configuration.html) | · | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Connected caveman graph](measures/cat_caveman_connected.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Contingency graph](measures/cat_contingency.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Correlated and bipartite random graph generators](measures/gen_correlated_bipartite.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cut Clustering](measures/cat_clustering_cut.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [De Bruijn graph generator](measures/gen_de_bruijn.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Degree sequence tree](measures/cat_degree_sequence_tree.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deterministic generators](measures/deterministic_generators.html) | ✓ | · | · |  |  | · |  | · | · |  |  |  | · |  |
| [Deterministic realisation of a degree sequence](measures/gen_degree_realization.html) | · | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Directed joint degree graph](measures/cat_degree_directed_joint.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dominance graph](measures/cat_dominance.html) |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Dorogovtsev goltsev mendes graph](measures/cat_dorogovtsev_goltsev_mendes.html) | · |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Dorogovtsev-Goltsev-Mendes graph](measures/dorogovtsev_goltsev_mendes_graph.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Duplication divergence graph](measures/cat_divergence_duplication.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dynamic Clustering Coefficient](measures/cat_clustering_coefficient_dynamic.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Dynamic Path Generator](measures/cat_dynamic_generator_path.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Dynamic Pub Web Generator](measures/cat_dynamic_generator_pub_web.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Extended clustering](measures/cat_clustering_extended.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Forest fire generator](measures/gen_forest_fire.html) |  | · | · |  |  |  | · |  |  |  |  |  |  |  |
| [Forest Fire Sparsifier](measures/cat_fire_forest_sparsifier.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Full bipartite graph](measures/cat_bipartite_full.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Full graph](measures/cat_full.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Full join](measures/cat_full_join.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Full multipartite](measures/cat_full_multipartite.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [G(n, m) random graph](measures/gen_gnm.html) | · | · |  | · |  |  |  | · | · |  |  |  |  |  |
| [G(n, p) random graph](measures/gen_gnp.html) | · | · | · | · |  |  | · | · | · | · |  |  | · |  |
| [Generalized petersen graph](measures/cat_generalized_petersen.html) | · |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Generalized Petersen graph generator](measures/gen_generalized_petersen.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Geometric soft configuration graph](measures/cat_configuration_geometric_soft.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gn graph](measures/cat_gn.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gnc graph](measures/cat_gnc.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gnm](measures/cat_gnm.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gnp](measures/cat_gnp.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gnr graph](measures/cat_gnr.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Graph atlas](measures/cat_atlas.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Graph atlas g](measures/cat_atlas_g.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy node swap bipartition (community)](measures/cat_bipartition_greedy_swap-community.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Grid communities](measures/cat_community_grid.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Growing random graph generator](measures/gen_growing.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Havel Hakimi Generator](measures/cat_generator_hakimi_havel.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Heavy hex graph](measures/cat_heavy_hex.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Heavy square graph](measures/cat_heavy_square.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Hexagonal lattice graph](measures/cat_hexagonal_lattice.html) | · |  | · |  |  |  |  | · |  |  |  |  |  |  |
| [Hkn harary graph](measures/cat_harary_hkn.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hnm harary graph](measures/cat_harary_hnm.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hyperbolic greedy routing](measures/cat_greedy_hyperbolic_routing.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Hyperbolic greedy success rate](measures/cat_greedy_hyperbolic_rate_success.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Hyperbolic index](measures/cat_hyperbolic.html) |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Hyperbolic random graph generator](measures/gen_hyperbolic.html) |  |  |  |  |  |  | · | · |  |  |  |  |  |  |
| [Interval graph](measures/cat_interval.html) | · |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Inverse line graph](measures/cat_inverse_line.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is complete](measures/cat_complete_is.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Joint degree graph](measures/cat_degree_joint.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kautz graph generator](measures/gen_kautz.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Kneser graph](measures/cat_kneser.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [KSpanning Tree Clustering](measures/cat_clustering_k_spanning_tree.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Latent-space generators (dot product, sphere, islands)](measures/gen_latent_space.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Lattice generator](measures/gen_lattice.html) | · | · | · |  |  | · |  | · | · |  |  |  |  |  |
| [Lattice-preserving rewiring](measures/rewire_lattice.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [LCF notation graph generator](measures/gen_lcf.html) | · |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [LFRGenerator](measures/cat_generator_lfr.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Linearized Chord Diagram Graph Generator](measures/cat_chord_diagram_generator_linearized.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Local Square Clustering Coefficient](measures/cat_clustering_coefficient_local_square.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Lollipop graph](measures/cat_lollipop.html) | · |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Make connected](measures/cat_connected_make.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Make max clique graph](measures/cat_clique_make_max.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Makeringlattice CIJ](measures/cat_cij_makeringlattice.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Margulis gabber galil graph](measures/cat_gabber_galil_margulis.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Maybe regular expander graph](measures/cat_expander_maybe_regular.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mesh graph](measures/cat_mesh.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Mesh graph generator](measures/cat_generator_mesh.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Mocnik Generator](measures/cat_generator_mocnik.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Mocnik Generator Basic](measures/cat_basic_generator_mocnik.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Mutual information](measures/cat_information_mutual.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Mycielski graph](measures/cat_mycielski.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Navigable small world graph](measures/cat_navigable_small_world.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Navigable small-world generator](measures/gen_navigable_small_world.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Nearest Neighbor Graph](measures/cat_nearest_neighbor.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Paley graph](measures/cat_paley.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Partial duplication graph](measures/cat_duplication_partial.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Plod generator](measures/cat_generator_plod.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Powerlaw cluster graph](measures/cat_cluster_powerlaw.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Powerlaw Degree Sequence](measures/cat_degree_powerlaw_sequence.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Preference (types) random graph generator](measures/gen_preference.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Preferential attachment generator](measures/gen_preferential.html) | · | · | · |  |  | · | · | · | · |  |  |  |  |  |
| [Preferential attachment graph (bipartite)](measures/cat_attachment_preferential-bipartite.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pub Web Generator](measures/cat_generator_pub_web.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [R-MAT generator](measures/gen_rmat.html) |  |  |  |  |  |  | · |  |  | · |  |  |  |  |
| [Random bipartite graph generator](measures/gen_random_bipartite.html) |  | · | · |  |  |  |  | · | · |  |  |  |  |  |
| [Random clustered graph](measures/cat_clustered_random.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random edge addition and removal](measures/random_edge_edit.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Random geometric graph generator](measures/gen_geometric.html) | · | · | · |  |  | · |  | · |  |  |  |  |  |  |
| [Random internet as graph](measures/cat_as_internet_random.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random intersection graph generator](measures/gen_intersection.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random k-out graph generator](measures/gen_k_out.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random kernel graph](measures/cat_kernel_random.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random lobster graph](measures/cat_lobster_random.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random regular expander graph](measures/cat_expander_random_regular.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random regular graph generator](measures/gen_regular.html) | · | · | · |  |  |  |  | · | · |  |  |  | · |  |
| [Random shell graph](measures/cat_random_shell.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random tree generator](measures/gen_random_tree.html) | · | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Reduced mutual information](measures/cat_information_mutual_reduced.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Regular Ring Lattice Generator](measures/cat_generator_lattice_regular_ring.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Relaxed caveman graph](measures/cat_caveman_relaxed.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Rgnmix](measures/cat_rgnmix.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Rich club](measures/rich_club.html) | ✓ |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Ring of cliques](measures/cat_clique_ring.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sample seq](measures/cat_sample_seq.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sbm random graph](measures/cat_random_sbm.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Search information](measures/cat_information_search.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Small world](measures/small_world.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Small-world generator](measures/gen_small_world.html) | · | · | · | · |  |  | · |  | · | · |  |  | · |  |
| [Spectral ordering](measures/cat_ordering_spectral.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ssca graph generator](measures/cat_generator_ssca.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Static fitness and static power-law generators](measures/gen_static_fitness.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Statistical Inference Clustering](measures/cat_clustering_inference_statistical.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Stochastic block model generator](measures/gen_sbm.html) | · | · | · |  |  | · | · | · | · |  |  |  | · |  |
| [Stochastic graph](measures/cat_stochastic.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sudoku graph](measures/cat_sudoku.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Swap contract](measures/swap_contract.html) | ✓ | · | · | · |  | · | · |  |  |  | · |  |  |  |
| [T Edge Formation](measures/cat_edge_formation_t.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Tadpole graph](measures/cat_tadpole.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trait-based (Callaway) growth generator](measures/gen_traits.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tree Game](measures/cat_game_tree.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Triangular lattice graph](measures/cat_lattice_triangular.html) | · |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Turan graph generator](measures/gen_turan.html) | · | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Variation information](measures/cat_information_variation.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Visibility graph](measures/cat_visibility.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Windmill graph](measures/cat_windmill.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Windmill graph generator](measures/gen_windmill.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |

## Graph theory and combinatorics

748 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | tsna | rsiena | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | graphblas | bct | ucinet | tnet | netrankr | keyplayer | centiserve | blockmodeling | nauty | backbone | missSBM | gergm | deepwalk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Abs Diff X](measures/cat_abs_diff_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Absdiff](measures/cat_absdiff.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Absdiffcat](measures/cat_absdiffcat.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Adjlist input](measures/cat_adjlist_input.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Agreement](measures/cat_agreement.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Agreement weighted](measures/cat_agreement_weighted.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Agreetrans](measures/cat_agreetrans.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ahuja Orlin Sharma Cyclic Exchange Local Augmentation](measures/cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Aic](measures/cat_aic.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Allgraphs](measures/cat_allgraphs.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Alpha](measures/cat_alpha.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Alt Dist2](measures/cat_alt_dist2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Alt LThreshold X](measures/cat_alt_l_threshold_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Alt RThreshold X](measures/cat_alt_r_threshold_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Alt Sq X](measures/cat_alt_sq_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Alt X](measures/cat_alt_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Alt XOut Act](measures/cat_act_alt_out_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Altkstar](measures/cat_altkstar.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Anti In Iso](measures/cat_anti_iso.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Anti In Iso2](measures/cat_anti_iso2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Antichains](measures/cat_antichains.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Any In Exposure Dist2](measures/cat_any_dist2_exposure.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ap dominating set](measures/ap_dominating_set.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ap local connectivity](measures/ap_local_connectivity.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ap vertex cover](measures/ap_vertex_cover.html) | ✓ |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Approx rank expected](measures/cat_approx_expected_rank.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Approx rank relative](measures/cat_approx_rank_relative.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Approximate and b-matching](measures/matching_approx.html) |  |  |  |  |  |  |  |  | · |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Asteroidal](measures/st_asteroidal.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [At free](measures/st_at_free.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Attrcov](measures/cat_attrcov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Automorphism group, count and canonical form](measures/automorphisms.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt](measures/cat_alt_av.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt Alt X](measures/cat_alt_av_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt cc](measures/cat_alt_av_cc.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt Dist2](measures/cat_alt_av_dist2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt gmm](measures/cat_alt_av_gmm.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt Pop](measures/cat_alt_av_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt Same X](measures/cat_alt_av_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Alt W](measures/cat_alt_av_w.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Att Higher](measures/cat_att_av_higher.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Att Lower](measures/cat_att_av_lower.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Deg](measures/cat_av_deg.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Exposure](measures/cat_av_exposure.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Group](measures/cat_av_group.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av In Alt Dist2 nc](measures/cat_alt_av_dist2_nc.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av In Sim](measures/cat_av_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av In Sim Dist2](measures/cat_av_dist2_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av In Sim Pop Alt](measures/cat_alt_av_pop_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Rec Alt](measures/cat_alt_av_rec.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Rec Alt Same X](measures/cat_alt_av_rec_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim Alt X](measures/cat_alt_av_sim_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim gmm](measures/cat_av_gmm_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim Rec Pop](measures/cat_av_pop_rec_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim Recip](measures/cat_av_recip_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim Var Alt](measures/cat_alt_av_sim_var.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim W](measures/cat_av_sim_w.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av TAlt Dist2](measures/cat_alt_av_dist2_t.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av TIn Alt Dist2 nc](measures/cat_alt_av_dist2_nc_t.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Tin Exposure Dist2](measures/cat_av_dist2_exposure_tin.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av TXAlt Dist2](measures/cat_alt_av_dist2_tx.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av XAlt Dist2](measures/cat_alt_av_dist2_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av XRec Alt](measures/cat_alt_av_rec_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Averagedis](measures/cat_averagedis.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Axelrod State](measures/cat_axelrod_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1concurrent](measures/cat_b1concurrent.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1cov](measures/cat_b1cov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1degrange](measures/cat_b1degrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1degree](measures/cat_b1degree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1dsp](measures/cat_b1dsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1dsp L](measures/cat_b1dsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1factor](measures/cat_b1factor.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1factordistinct](measures/cat_b1factordistinct.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1mindegree](measures/cat_b1mindegree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1nodematch](measures/cat_b1nodematch.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1sociality](measures/cat_b1sociality.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1star](measures/cat_b1star.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1starmix](measures/cat_b1starmix.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B1twostar](measures/cat_b1twostar.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2concurrent](measures/cat_b2concurrent.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2cov](measures/cat_b2cov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2degrange](measures/cat_b2degrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2degree](measures/cat_b2degree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2dsp](measures/cat_b2dsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2dsp L](measures/cat_b2dsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2factor](measures/cat_b2factor.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2factordistinct](measures/cat_b2factordistinct.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2mindegree](measures/cat_b2mindegree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2nodematch](measures/cat_b2nodematch.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2sociality](measures/cat_b2sociality.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2star](measures/cat_b2star.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2starmix](measures/cat_b2starmix.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [B2twostar](measures/cat_b2twostar.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Backbone](measures/cat_backbone.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Basis](measures/basis.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Bbnam](measures/cat_bbnam.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Bbnam bf](measures/cat_bbnam_bf.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Beh Unsp Int](measures/cat_beh_int_unsp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Bicm](measures/cat_bicm.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Binary Threshold State](measures/cat_binary_state_threshold.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Block Dyad Sampler](measures/cat_block_dyad_sampler.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Block Node Sampler](measures/cat_block_sampler.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Bn](measures/cat_bn.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Boolean State](measures/cat_boolean_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Bottleneck](measures/cat_bottleneck.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Break cycles](measures/cat_break_cycle.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [BTERReplicator](measures/cat_bter_replicator.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [CD index](measures/nxs_cd_index.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cds](measures/st_cds.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Central point dominance](measures/cat_central_dominance_point.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Centralgraph](measures/cat_centralgraph.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Centroid](measures/cat_centroid.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Check matching](measures/check_matching.html) | ✓ | · |  |  |  |  |  |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chinese Postman](measures/cat_chinese_postman.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chordal order](measures/st_chordal_order.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chordal-graph tests and algorithms](measures/chordal.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chordless cycles](measures/chordless_cycles.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chromatic polynomial](measures/cat_chromatic_polynomial.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [CIsing Glauber Block State](measures/cat_block_c_glauber_ising_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [CIsing Glauber State](measures/cat_c_glauber_ising_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Clique removal](measures/ap_clique_removal.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Clusterrank](measures/cat_clusterrank.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Colliders](measures/nxs_colliders.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Coloring](measures/st_coloring.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Combined SCD](measures/cat_combined_scd.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Combining similar relations](measures/cat_combining_relations_similar.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Comparable pairs](measures/cat_comparable_pairs.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Compare ranks](measures/cat_compare_ranks.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Concurrent](measures/cat_concurrent.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Concurrentties](measures/cat_concurrentties.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Congru](measures/cat_congru.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Consensus](measures/cat_consensus.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Contracted nodes](measures/nxs_contracted_nodes.html) | ✓ | · | · |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Convergence degree](measures/cat_convergence_degree.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Convergence field size](measures/cat_convergence_field_size.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Convex hull](measures/cat_convex_hull.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Could be iso](measures/could_be_iso.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Counterexample](measures/st_counterexample.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cover F1 Similarity](measures/cat_cover_f1_similarity.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cpa](measures/cat_cpa.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Crit Fun C](measures/cat_c_crit_fun.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Cross XOut Act](measures/cat_act_cross_out_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ctriple](measures/cat_ctriple.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cy WWX](measures/cat_cy_wwx.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cycle basis](measures/cycle_basis.html) | ≠ |  |  |  |  |  |  |  |  | · |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cycle3](measures/cat_cycle3.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cycle4](measures/cat_cycle4.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cyclicalties](measures/cat_cyclicalties.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cyclicalweights](measures/cat_cyclicalweights.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Cycprob](measures/cat_cycprob.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Dag reachability](measures/nxs_dag_reachability.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dasgupta cost](measures/cat_cost_dasgupta.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dasgupta score](measures/cat_dasgupta.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ddsp](measures/cat_ddsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ddsp L](measures/cat_ddsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deg Abs Contr X](measures/cat_abs_contr_deg_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deg Abs Diff X](measures/cat_abs_deg_diff_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deg Neg Contr X](measures/cat_contr_deg_neg_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deg Neg Diff X](measures/cat_deg_diff_neg_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deg Pos Contr X](measures/cat_contr_deg_pos_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deg Pos Diff X](measures/cat_deg_diff_pos_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degcor](measures/cat_degcor.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degcrossprod](measures/cat_degcrossprod.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degrange](measures/cat_degrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degrange mean age](measures/cat_age_degrange_mean.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degree mean age](measures/cat_age_degree_mean.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degree Multiscale Sparsifier](measures/cat_degree_multiscale_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degree Sampler](measures/cat_degree_sampler.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Degree sequence test](measures/nxs_degree_sequence_test.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degree1 5](measures/cat_5_degree1.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degreedist](measures/cat_degreedist.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Degseq](measures/cat_degseq.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Densest](measures/ap_densest.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Desp](measures/cat_desp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Desp L](measures/cat_desp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dgwdsp](measures/cat_dgwdsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dgwdsp L](measures/cat_dgwdsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dgwesp](measures/cat_dgwesp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dgwesp L](measures/cat_dgwesp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dgwnsp](measures/cat_dgwnsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dgwnsp L](measures/cat_dgwnsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Di Graph Matcher](measures/cat_di_matcher.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dice pairwise](measures/cat_dice_pairwise.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Diff Sq X](measures/cat_diff_sq_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diff X](measures/cat_diff_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diff XIn Pop](measures/cat_diff_pop_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diff XOut Act](measures/cat_act_diff_out_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diff XReci Act](measures/cat_act_diff_reci_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diff XTrans Rec Trip](measures/cat_diff_rec_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diff XTrans Trip](measures/cat_diff_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dirichlet](measures/cat_dirichlet.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Disparity](measures/cat_disparity.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Dist 2pow](measures/cat_2pow_dist.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Dist dpow](measures/cat_dist_dpow.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Dist inv](measures/cat_dist_inv.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Dist powd](measures/cat_dist_powd.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Diversity](measures/cat_diversity.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Diversity coef](measures/cat_coef_diversity.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Dlbet](measures/cat_dlbet.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Dmnc](measures/cat_dmnc.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Dnsp](measures/cat_dnsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dnsp L](measures/cat_dnsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dominating](measures/st_dominating.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dominating sets](measures/dominating_set.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Double Standard Sampler](measures/cat_double_sampler_standard.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Draw Block State](measures/cat_block_draw_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dyad Sampler](measures/cat_dyad_sampler.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Dyadcov](measures/cat_dyadcov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dyadic Cov](measures/cat_cov_dyadic.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dyconst](measures/cat_dyconst.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Edge ages](measures/cat_ages_edge.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edge average](measures/cat_average_edge.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edge cover](measures/edge_cover.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edge Duration](measures/cat_duration_edge.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edge nei overlap](measures/cat_edge_nei_overlap.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Edgecov](measures/cat_edgecov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edgecov ages](measures/cat_ages_edgecov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edgecov mean age](measures/cat_age_edgecov_mean.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edgelist input](measures/cat_edgelist_input.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Edges](measures/cat_edge.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Edges ageinterval](measures/cat_ageinterval_edge.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Em infer](measures/cat_em_infer.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Embedding](measures/st_embedding.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Embedding euler](measures/st_embedding_euler.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [EMBlock State](measures/cat_block_em_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Entropy](measures/cat_entropy.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Epc](measures/cat_epc.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Epidemic Simulation SEIR](measures/cat_epidemic_seir_simulation.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Epidemics Block State](measures/cat_block_epidemics_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Equiv clust](measures/cat_clust_equiv.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Establishment](measures/cat_establishment.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Euler](measures/nxs_euler.html) | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Euler circuit](measures/nxs_euler_circuit.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Exact rank prob](measures/cat_exact_prob_rank.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Facd](measures/cat_facd.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Farthest points](measures/cat_farthest_points.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Farthest vertices](measures/cat_farthest.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Fastball](measures/cat_fastball.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Fdsm](measures/cat_fdsm.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Feedback arc and vertex sets](measures/feedback_sets.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Fill](measures/st_fill.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Find cycle](measures/find_cycle.html) | ✓ | · |  |  |  |  |  |  |  | · | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Fixedcol](measures/cat_fixedcol.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Fixedfill](measures/cat_fixedfill.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Fixedrow](measures/cat_fixedrow.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Flow hierarchy](measures/nxo_flow_hierarchy.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Forest flags](measures/nxs_forest_flags.html) | ✓ | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [From prufer](measures/nxs_from_prufer.html) | ✓ | · | · |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Fw tree](measures/nxs_fw_tree.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gateway coef](measures/cat_coef_gateway.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [GCE](measures/cat_gce.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gen Potts BPState](measures/cat_bp_gen_potts_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Generalized Binary State](measures/cat_binary_generalized_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Generalized degree](measures/generalized_degree.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Generate fc](measures/cat_fc_generate.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Generic edge match](measures/cat_edge_generic_match.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Generic multiedge match](measures/cat_generic_match_multiedge.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Generic node match](measures/cat_generic_match.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Get block edge gradient](measures/cat_block_edge_gradient.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Get rankings](measures/cat_rankings.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Gilschmidt](measures/cat_gilschmidt.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Girth](measures/girth.html) | ✓ | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Global Threshold Filter](measures/cat_filter_global_threshold.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gon Heuristic](measures/cat_gon_heuristic.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Graph edit distance](measures/ged.html) | ✓ |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Graph Matcher](measures/cat_matcher.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy branching](measures/nxs_greedy_branching.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy color](measures/greedy_color.html) | ≠ | · | · |  |  |  |  | · | · | · |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy edge color](measures/cat_color_edge_greedy.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy Multiplicative Spanner](measures/cat_greedy_multiplicative_spanner.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Greedy source expansion (community)](measures/cat_expansion_greedy_source-community.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Groupden](measures/cat_groupden.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Growth](measures/cat_growth.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Gtom](measures/cat_gtom.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Gwb1degree](measures/cat_gwb1degree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwb1dsp](measures/cat_gwb1dsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwb1dsp L](measures/cat_gwb1dsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwb2degree](measures/cat_gwb2degree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwb2dsp](measures/cat_gwb2dsp.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwb2dsp L](measures/cat_gwb2dsp_l.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwdsp FB](measures/cat_fb_gwdsp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwdsp FF](measures/cat_ff_gwdsp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwesp BB](measures/cat_bb_gwesp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwesp BF](measures/cat_bf_gwesp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwesp FB](measures/cat_fb_gwesp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwesp FF](measures/cat_ff_gwesp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gwesp RR](measures/cat_gwesp_rr.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hamming](measures/cat_hamming.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hampath](measures/st_hampath.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hdist](measures/cat_hdist.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hiclus](measures/cat_hiclus.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Higher](measures/cat_higher.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hom XOut Act](measures/cat_act_hom_out_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hom XOut Act2](measures/cat_act2_hom_out_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hom XTrans Rec Trip](measures/cat_hom_rec_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hom XTrans Trip](measures/cat_hom_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Hysteresis](measures/cat_hysteresis.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |
| [Idegrange](measures/cat_idegrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Idegree](measures/cat_idegree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Idegree1 5](measures/cat_5_idegree1.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Implicit family](measures/implicit_family.html) | ∅ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Act](measures/cat_act.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Act c](measures/cat_act_c.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Act Sqrt](measures/cat_act_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Act X](measures/cat_act_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In In Ass](measures/cat_ass.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Is Degree](measures/cat_degree_is.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Out Ass](measures/cat_ass_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Pop](measures/cat_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Pop c](measures/cat_c_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Pop dya](measures/cat_dya_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Pop Sqrt](measures/cat_pop_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Pop X](measures/cat_pop_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Rate](measures/cat_rate.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Rate Inv](measures/cat_inv_rate.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Rate Log](measures/cat_log_rate.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In Struct Eq](measures/cat_eq_struct.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In WWX](measures/cat_wwx.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In2 Plus](measures/cat_in2_plus.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [In3 Plus](measures/cat_in3_plus.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Incomparable pairs](measures/cat_incomparable_pairs.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Indeg](measures/cat_indeg.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Indeg Av Group](measures/cat_av_group_indeg.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Indeg Tot Group](measures/cat_group_indeg_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Index builder](measures/cat_builder.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Infect Covar](measures/cat_covar_infect.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Infect In](measures/cat_infect.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Infect Out](measures/cat_infect_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Intersection](measures/st_intersection.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ipf](measures/cat_ipf.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Is bigraphical](measures/cat_bigraphical_is.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is degseq](measures/cat_degseq_is.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is graphical](measures/cat_graphical_is.html) |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is hierarchical](measures/cat_hierarchical_is.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is independent vertex set](measures/cat_independent_is_set.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is isolate](measures/cat_is_isolate.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is ivs](measures/cat_is_ivs.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is k regular](measures/cat_is_k_regular.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is preserved](measures/cat_is_preserved.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Is regular expander](measures/cat_expander_is_regular.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is simple path](measures/nxs_is_simple_path.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Is strongly regular](measures/cat_is_regular_strongly.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ising BPState](measures/cat_bp_ising_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ising Glauber Block State](measures/cat_block_glauber_ising_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ising Glauber State](measures/cat_glauber_ising_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ising Metropolis State](measures/cat_ising_metropolis_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [ISMAGS](measures/cat_ismags.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Isolate](measures/cat_isolate.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Isolate Net](measures/cat_isolate_net.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Isolate Pop](measures/cat_isolate_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Isolatededges](measures/cat_isolatededges.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Jaccard Similarity Sparsifier](measures/cat_jaccard_similarity_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Jdegree](measures/cat_jdegree.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Jin](measures/cat_jin.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Jout](measures/cat_jout.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Jump XTrans Trip](measures/cat_jump_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Junction](measures/st_junction.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [K edge augmentation (connectivity)](measures/cat_augmentation_edge_k-connectivity.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [KCenters](measures/cat_centers_k.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kcycle census](measures/cat_census_kcycle.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kfactor](measures/st_kfactor.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kfactor edges](measures/st_kfactor_edges.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kirman State](measures/cat_kirman_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kl](measures/st_kl.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kosaraju](measures/nxo_kosaraju.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kpset](measures/cat_kpset.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Kuramoto State](measures/cat_kuramoto_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kuratowski](measures/st_kuratowski.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Lans](measures/cat_lans.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Large clique size](measures/ap_large_clique_size.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Leaderrank](measures/cat_leaderrank.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [LFM](measures/cat_lfm.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [LFMLocal](measures/cat_lfm_local.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Linear Normal Block State](measures/cat_block_linear_normal_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Linear Normal State](measures/cat_linear_normal_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Linear State](measures/cat_linear_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Link prediction](measures/link_prediction.html) | ✓ | · | · |  |  |  |  | · | · |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Local Degree Sparsifier](measures/cat_degree_local_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Local scan](measures/cat_local_scan.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Local Similarity Sparsifier](measures/cat_local_similarity_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Local Tightness Expansion](measures/cat_expansion_local_tightness.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Localtriangle](measures/cat_localtriangle.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Loop and multi-edge detection](measures/multi_loop_detection.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [LVBlock State](measures/cat_block_lv_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [LVState](measures/cat_lv_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [M2star](measures/cat_m2star.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Majority Voter State](measures/cat_majority_state_voter.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Majorization gap](measures/cat_gap_majorization.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Makebowtie](measures/cat_makebowtie.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Makeeven CIJ](measures/cat_cij_makeeven.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Makefractal CIJ](measures/cat_cij_makefractal.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Makerand CIJ](measures/cat_cij_makerand.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Makerand CIJdegreesfixed](measures/cat_ci_jdegreesfixed_makerand.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Maketoeplitz CIJ](measures/cat_cij_maketoeplitz.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Makeup](measures/cat_makeup.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Marginal graph lprob](measures/cat_lprob_marginal.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Marginal graph sample](measures/cat_marginal_sample.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Marginal multigraph entropy](measures/cat_entropy_marginal_multigraph.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Marginal multigraph lprob](measures/cat_lprob_marginal_multigraph.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Marginal multigraph sample](measures/cat_marginal_multigraph_sample.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mat input](measures/cat_input_mat.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Match vertices](measures/cat_match.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Matching ind](measures/cat_ind_matching.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Max Alt](measures/cat_alt_max.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Max Alt gmm](measures/cat_alt_gmm_max.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Max weight matching](measures/max_weight_matching.html) | ✓ |  |  |  |  |  |  | · |  | · |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Max XAlt](measures/cat_alt_max_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Maxcohesion](measures/cat_maxcohesion.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Maximal matching](measures/maximal_matching.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Maximum bisimulation](measures/cat_bisimulation_maximum.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mean age](measures/cat_age_mean.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Meandeg](measures/cat_meandeg.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Measured Block State](measures/cat_block_measured_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Measured Closure Block State](measures/cat_block_closure_measured_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Metric closure (approximate)](measures/cat_closure_metric-approximate.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mf entropy](measures/cat_entropy_mf.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Microstate entropy](measures/cat_entropy_microstate.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min Alt](measures/cat_alt_min.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min Alt gmm](measures/cat_alt_gmm_min.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min basis](measures/min_basis.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min basis weights](measures/min_basis_weights.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min maximal matching (approximate)](measures/cat_matching_maximal_min-approximate.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min weight matching](measures/min_weight_matching.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min XAlt](measures/cat_alt_min_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mis](measures/mis.html) | ✓ | · | · |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Misra gries edge color](measures/cat_color_edge_gries_misra.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mixed Measured Block State](measures/cat_block_measured_mixed_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mlf](measures/cat_mlf.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Mm](measures/cat_mm.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mnc](measures/cat_mnc.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Mode Cluster State](measures/cat_cluster_mode_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Module degree zscore](measures/cat_degree_module_zscore.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Multi Di Graph Matcher](measures/cat_di_matcher_multi.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Multi Graph Matcher](measures/cat_matcher_multi.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Multiscale Sparsifier](measures/cat_multiscale_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mutual L](measures/cat_l_mutual.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mwm](measures/st_mwm.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mwm pairs](measures/st_mwm_pairs.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mycielskian](measures/cat_mycielskian.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Navigation](measures/cat_navigation.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Nbr Dist2](measures/cat_dist2_nbr.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nbr Dist2twice](measures/cat_dist2twice_nbr.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nbs bct](measures/cat_bct_nbs.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Nearsimmelian](measures/cat_nearsimmelian.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Neighborhood inclusion](measures/cat_inclusion_neighborhood.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Nested Block State](measures/cat_block_nested_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Netcancor](measures/cat_netcancor.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Newrecip](measures/cat_newrecip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Node connectivity](measures/ap_node_connectivity.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Node Sampler](measures/cat_sampler.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Nodecovar](measures/cat_nodecovar.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodecovrange](measures/cat_nodecovrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodefactor mean age](measures/cat_age_mean_nodefactor.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodefactordistinct](measures/cat_nodefactordistinct.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeicov](measures/cat_nodeicov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeicovar](measures/cat_nodeicovar.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeicovrange](measures/cat_nodeicovrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeifactor](measures/cat_nodeifactor.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeifactordistinct](measures/cat_nodeifactordistinct.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodemix](measures/cat_nodemix.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodemix mean age](measures/cat_age_mean_nodemix.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeocov](measures/cat_nodeocov.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeocovar](measures/cat_nodeocovar.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeocovrange](measures/cat_nodeocovrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeofactor](measures/cat_nodeofactor.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nodeofactordistinct](measures/cat_nodeofactordistinct.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Non PCompress](measures/cat_compress_non_p.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Non randomness](measures/cat_non_randomness.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Normal BPState](measures/cat_bp_normal_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Normal Glauber Block State](measures/cat_block_glauber_normal_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Normal State](measures/cat_normal_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Numerical edge match](measures/cat_edge_match_numerical.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Numerical multiedge match](measures/cat_match_multiedge_numerical.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Numerical node match](measures/cat_match_numerical.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Numties](measures/cat_numties.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Nx anneal](measures/ap_nx_anneal.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nx ramsey](measures/ap_nx_ramsey.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nx random](measures/ap_nx_random.html) | ✓ |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nxs cycle basis](measures/nxs_cycle_basis.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nxs find cycle](measures/nxs_find_cycle.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nxs tree lca](measures/nxs_tree_lca.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Odegrange](measures/cat_odegrange.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Odegree](measures/cat_odegree.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Odegree1 5](measures/cat_5_odegree1.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [One exchange (approximate)](measures/cat_exchange_one-approximate.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Openmp context](measures/cat_context_openmp.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Opp](measures/cat_opp.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Ordinalassoc](measures/cat_ordinalassoc.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Out Act](measures/cat_act_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Act c](measures/cat_act_c_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Act Sqrt](measures/cat_act_out_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Act X](measures/cat_act_out_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Inv](measures/cat_inv_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Iso](measures/cat_iso_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Isolate](measures/cat_isolate_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out More](measures/cat_more_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out More2](measures/cat_more2_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out More3](measures/cat_more3_out.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Pop](measures/cat_out_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Pop c](measures/cat_c_out_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Pop More](measures/cat_more_out_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Pop Sqrt](measures/cat_out_pop_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Pop Sqrt More](measures/cat_more_out_pop_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Pop Threshold](measures/cat_out_pop_threshold.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Pop X](measures/cat_out_pop_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Rate](measures/cat_out_rate.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Rate Inv](measures/cat_inv_out_rate.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Rate Log](measures/cat_log_out_rate.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Sq Inv](measures/cat_inv_out_sq.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Threshold](measures/cat_out_threshold.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Threshold2](measures/cat_out_threshold2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Trunc](measures/cat_out_trunc.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Trunc2](measures/cat_out_trunc2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out WWX](measures/cat_out_wwx.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out XMore](measures/cat_more_out_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Outdeg](measures/cat_outdeg.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Overlap Block State](measures/cat_block_overlap_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [P Shift Count](measures/cat_count_p_shift.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pa](measures/cat_pa.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pa age](measures/cat_age_pa.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pairwisedis](measures/cat_pairwisedis.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Panther](measures/panther.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paris](measures/cat_paris.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Participation coef](measures/cat_coef_participation.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Participation coef sparse](measures/cat_coef_participation_sparse.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Perfect](measures/st_perfect.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Perfect-graph (Berge) tests](measures/perfect_graph.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Persistrecip](measures/cat_persistrecip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pivot MDS](measures/cat_mds_pivot.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Planar](measures/st_planar.html) | ✓ |  |  |  |  |  |  | · |  | · |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Planarity testing, embedding and straight-line drawing](measures/planarity.html) |  |  |  |  |  |  |  | · |  |  |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Plod iterator](measures/cat_iterator_plod.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Polish](measures/cat_polish.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Polynomials](measures/st_polynomials.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pop Alt](measures/cat_alt_pop.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Potts Glauber Block State](measures/cat_block_glauber_potts_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Potts Glauber State](measures/cat_glauber_potts_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Potts Metropolis State](measures/cat_metropolis_potts_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Potts State](measures/cat_potts_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [PPBlock State](measures/cat_block_pp_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prestige](measures/cat_prestige.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prim Compress](measures/cat_compress_prim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prim Deg Act](measures/cat_act_deg_prim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prim Deg Act Diff](measures/cat_act_deg_diff_prim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prim Deg Act Diff Sqrt](measures/cat_act_deg_diff_prim_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prim Deg Act Inv](measures/cat_act_deg_inv_prim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prim Deg Act Log](measures/cat_act_deg_log_prim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prim Deg Act Sqrt](measures/cat_act_deg_prim_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Primary](measures/cat_primary.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prominent group](measures/nxo_prominent.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Propagation](measures/cat_propagation.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Prufer](measures/nxs_prufer.html) | ✓ |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pruned Landmark Labeling](measures/cat_labeling_landmark_pruned.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pseudo CIsing Block State](measures/cat_block_c_ising_pseudo_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pseudo Ising Block State](measures/cat_block_ising_pseudo_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pseudo Normal Block State](measures/cat_block_normal_pseudo_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Pseudo Potts Block State](measures/cat_block_potts_pseudo_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Psi](measures/cat_psi.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Pstar](measures/cat_pstar.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Quadrilateral Simmelian Sparsifier](measures/cat_quadrilateral_simmelian_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random cograph](measures/cat_cograph_random.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random Edge Sparsifier](measures/cat_edge_random_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random k lift](measures/cat_k_lift_random.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random reference](measures/cat_random_reference.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random tournament](measures/cat_random_tournament.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Random walk corpus](measures/cat_corpus_random_walk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Randomize](measures/cat_randomize.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Rank intervals](measures/cat_intervals_rank.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Ranked Block State](measures/cat_block_ranked_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Rate X](measures/cat_rate_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Realrecip](measures/cat_realrecip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Realtrans](measures/cat_realtrans.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Receiver](measures/cat_receiver.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Reci Act](measures/cat_act_reci.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Reci Pop](measures/cat_pop_reci.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Reci Pop Sqrt](measures/cat_pop_reci_sqrt.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Recip](measures/cat_recip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Recip Deg](measures/cat_deg_recip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Recip Rate](measures/cat_rate_recip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Recip Rate Inv](measures/cat_inv_rate_recip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Recip Rate Log](measures/cat_log_rate_recip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Recursive cycles](measures/nxs_recursive_cycles.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Regular](measures/st_regular.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Rentian scaling](measures/cat_rentian_scaling.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Rg](measures/cat_rg.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Rg reshuffling](measures/cat_reshuffling_rg.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Rgbn](measures/cat_rgbn.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Rguman](measures/cat_rguman.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Rlebdm](measures/cat_rlebdm.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Rowlas](measures/cat_rowlas.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Rsh](measures/cat_rsh.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Rwb](measures/cat_rwb.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [S metric](measures/cat_metric_s.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same In XCycle4](measures/cat_cycle4_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same X](measures/cat_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same XIn Pop](measures/cat_pop_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same XOut Act](measures/cat_act_out_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same XReci Act](measures/cat_act_reci_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same XRecip](measures/cat_recip_same_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same XTrans Rec Trip](measures/cat_rec_same_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Same XTrans Trip](measures/cat_same_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Scan stat](measures/cat_scan_stat.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [SCANSparsifier](measures/cat_scan_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [SCDGround Truth Comparison](measures/cat_comparison_ground_scd_truth.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Score](measures/cat_score.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Score sequence](measures/cat_sequence.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sdmat](measures/cat_sdmat.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sdsm](measures/cat_sdsm.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Semilocal](measures/cat_semilocal.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Sender](measures/cat_sender.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sfigality](measures/cat_sfigality.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Shared Pop](measures/cat_pop_shared.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim All Far](measures/cat_all_far_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim All Near](measures/cat_all_near_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim Dist2](measures/cat_dist2_sim.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim Recip X](measures/cat_recip_sim_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim X](measures/cat_sim_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim X gmm](measures/cat_gmm_sim_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim XTrans Trip](measures/cat_sim_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Simmelian Multiscale Sparsifier](measures/cat_multiscale_simmelian_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Simmelian Sparsifier Non Parametric](measures/cat_non_parametric_simmelian_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Simmelian Sparsifier Parametric](measures/cat_parametric_simmelian_sparsifier.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Simmelianties](measures/cat_simmelianties.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Simple cycles](measures/simple_cycles.html) | ✓ | · | · |  |  |  |  | · |  | · |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Simple Dyad Sampler](measures/cat_dyad_sampler_simple.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Simple Node Sampler](measures/cat_sampler_simple.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Simrank](measures/simrank.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sir](measures/cat_sir.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [SIRSState](measures/cat_sirs_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [SIRState](measures/cat_sir_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [SISState](measures/cat_sis_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [SIState](measures/cat_si_state.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Smalldiff](measures/cat_smalldiff.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Snowball Sampler](measures/cat_sampler_snowball.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Sociality](measures/cat_sociality.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Socialprox](measures/cat_socialprox.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [SPSP](measures/cat_spsp.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [St chordal](measures/st_chordal.html) | ✓ | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [St edge cover](measures/st_edge_cover.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [St tsp](measures/st_tsp.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Structdist](measures/cat_structdist.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Structure statistics](measures/cat_statistics_structure.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Suscept Av Covar](measures/cat_av_covar_suscept.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Suscept Av In](measures/cat_av_suscept.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Swan combinatory](measures/cat_combinatory_swan.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Symmetrise](measures/cat_symmetrise.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [T Degree](measures/cat_degree_t.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [T Edge Dissolution](measures/cat_dissolution_edge_t.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [TCE](measures/cat_tce.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Threetrail](measures/cat_threetrail.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Threshold](measures/cat_threshold.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Threshold graphs](measures/threshold_graph.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Threshold2](measures/cat_threshold2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Threshold3](measures/cat_threshold3.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Threshold4](measures/cat_threshold4.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tied Duration](measures/cat_duration_tied.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Topocoefficient](measures/cat_topocoefficient.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Topological sorts](measures/nxs_topological_sorts.html) | ✓ |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot AAlt Dist2](measures/cat_a_alt_dist2_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot AIn Alt Dist2 nc](measures/cat_a_alt_dist2_nc_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot AIn Exposure Dist2](measures/cat_a_dist2_exposure_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Alt](measures/cat_alt_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Alt cc](measures/cat_alt_cc_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Alt Dist2](measures/cat_alt_dist2_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Alt gmm](measures/cat_alt_gmm_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Alt Pop](measures/cat_alt_pop_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Alt Same X](measures/cat_alt_same_tot_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Alt W](measures/cat_alt_tot_w.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Att Higher](measures/cat_att_higher_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Att Lower](measures/cat_att_lower_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot AXAlt Dist2](measures/cat_alt_ax_dist2_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Dist2](measures/cat_dist2_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Exposure](measures/cat_exposure_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Group](measures/cat_group_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Gwdsp FBAlt](measures/cat_alt_fb_gwdsp_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Gwdsp FBAlt nc](measures/cat_alt_fb_gwdsp_nc_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Gwdsp FFAlt](measures/cat_alt_ff_gwdsp_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Gwdsp FFAlt nc](measures/cat_alt_ff_gwdsp_nc_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot In Alt Dist2 nc](measures/cat_alt_dist2_nc_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot In Exposure Dist2](measures/cat_dist2_exposure_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot In Sim](measures/cat_sim_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot In Sim Dist2](measures/cat_dist2_sim_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot In Sim Pop Alt](measures/cat_alt_pop_sim_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Rec Alt](measures/cat_alt_rec_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Rec Alt Same X](measures/cat_alt_rec_same_tot_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Sim Alt X](measures/cat_alt_sim_tot_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Sim Rec Pop](measures/cat_pop_rec_sim_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Sim Recip](measures/cat_recip_sim_tot.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Sim W](measures/cat_sim_tot_w.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot XAlt](measures/cat_alt_tot_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot XAlt Dist2](measures/cat_alt_dist2_tot_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot XRec Alt](measures/cat_alt_rec_tot_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Total Neighbors Index](measures/cat_neighbors_total.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tournament](measures/st_tournament.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Med Trip](measures/cat_med_trans_trip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Rec Trip](measures/cat_rec_trans_trip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Rec Trip2](measures/cat_rec_trans_trip2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Ties](measures/cat_ties_trans.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Trip](measures/cat_trans_trip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Trip EE](measures/cat_ee_trans_trip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Trip FE](measures/cat_fe_trans_trip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Trip FR](measures/cat_fr_trans_trip.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Trip X](measures/cat_trans_trip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Trip1](measures/cat_trans_trip1.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Trans Trip2](measures/cat_trans_trip2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Traveling salesman (exact and heuristic)](measures/tsp.html) | · |  |  |  |  |  |  |  | · |  |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tree centroid](measures/nxs_tree_centroid.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tree iso](measures/tree_iso.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Treewidth](measures/ap_treewidth.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Triads](measures/st_triads.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Triangle list](measures/nxs_triangle_list.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Triangle Sparsifier](measures/cat_sparsifier_triangle.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Triangulation](measures/cat_triangulation.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tsp tour](measures/cat_tour_tsp.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ttriple](measures/cat_ttriple.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tw min degree](measures/ap_tw_min_degree.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Twostar L](measures/cat_l_twostar.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [UDegree Index](measures/cat_degree_u.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Umap compute weights](measures/cat_umap_weights.html) |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Uncertain Block State](measures/cat_block_state_uncertain.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Unequal X](measures/cat_unequal_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Unsp Int](measures/cat_int_unsp.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Var Alt](measures/cat_alt_var.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [VDegree Index](measures/cat_degree_v.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Vertex Duration](measures/cat_duration.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Vf2pp](measures/vf2pp.html) | ✓ | · | · |  |  |  |  | · |  | · | · | · | · |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |
| [Voronoi cells](measures/cat_cells_voronoi.html) | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Voter State](measures/cat_state_voter.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Walks attenuated](measures/cat_attenuated_walk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Walks exp](measures/cat_exp_walk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Walks exp even](measures/cat_even_exp_walk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Walks exp odd](measures/cat_exp_odd_walk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Walks limit prop](measures/cat_limit_prop_walk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Walks uptok](measures/cat_uptok_walk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Weighted Block State](measures/cat_block_state_weighted.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Weighted Overlap Block State](measures/cat_block_overlap_state_weighted.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Weighted richclub](measures/cat_richclub_weighted.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Weighted richclub local](measures/cat_local_richclub_weighted.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Wl hash](measures/wl_hash.html) | ✓ |  |  |  |  |  |  |  |  |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Wl subgraph](measures/wl_subgraph.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Word2vec output](measures/cat_output_word2vec.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [WXX](measures/cat_wxx.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [X](measures/cat_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [XRecip](measures/cat_recip_x.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [XWX](measures/cat_xwx.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [XWX1](measures/cat_xwx1.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [XWX2](measures/cat_xwx2.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [XXW](measures/cat_xxw.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Inference (QAP, null models)

14 measures.

| Measure | sna | graphtool | jgrapht | ucinet | netrankr |
|---|---|---|---|---|---|
| [ANOVA density models (constant/variable homophily, structural blockmodel)](measures/anova_density.html) |  |  |  | · |  |
| [Conditional uniform graph tests and null models](measures/cug_null_models.html) | · |  |  | · |  |
| [Goldberg Maximum Density Subgraph Algorithm](measures/cat_density_goldberg_maximum_subgraph.html) |  |  | · |  |  |
| [Goldberg Maximum Density Subgraph Algorithm Base](measures/cat_base_density_goldberg_maximum_subgraph.html) |  |  | · |  |  |
| [Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight](measures/cat_density_edge_goldberg_maximum_per_subgraph_weight.html) |  |  | · |  |  |
| [Goldberg Maximum Density Subgraph Algorithm Node Weights](measures/cat_density_goldberg_maximum_subgraph_weights.html) |  |  | · |  |  |
| [Group-level permutation tests](measures/node_permutation_tests.html) |  |  |  | · |  |
| [Logistic MR-QAP](measures/lr_qap.html) | · |  |  | · |  |
| [Mcmc anneal](measures/cat_anneal_mcmc.html) |  | · |  |  |  |
| [Mcmc equilibrate](measures/cat_equilibrate_mcmc.html) |  | · |  |  |  |
| [Mcmc rank prob](measures/cat_mcmc_prob_rank.html) |  |  |  |  | · |
| [MR-QAP regression (Y-permutation, double semi-partialling)](measures/qap_regression.html) | · |  |  | · |  |
| [Network autocorrelation: lag/error model, Moran, Geary](measures/network_autocorrelation.html) | · |  |  | · |  |
| [QAP correlation (Y-permutation, exact and Monte Carlo)](measures/qap_correlation.html) | · |  |  | · |  |

## Input and output

41 measures.

| Measure | networkx | igraph | pyigraph | networkit | rustworkx | jgrapht | gephi | ucinet |
|---|---|---|---|---|---|---|---|---|
| [ADJACENCY read and write](measures/io_adjacency.html) |  |  | · |  |  |  |  |  |
| [BINARYEDGELISTPARTITION read and write](measures/io_binaryedgelistpartition.html) |  |  |  | · |  |  |  |  |
| [BINARYPARTITION read and write](measures/io_binarypartition.html) |  |  |  | · |  |  |  |  |
| [CSV read and write](measures/io_csv.html) |  |  |  |  |  | · |  |  |
| [DIMACS read and write](measures/io_dimacs.html) |  |  | · |  |  | · |  |  |
| [EDGELIST read and write](measures/io_edgelist.html) | · |  | · | · |  |  |  |  |
| [EDGELISTCOVER read and write](measures/io_edgelistcover.html) |  |  |  | · |  |  |  |  |
| [EDGELISTPARTITION read and write](measures/io_edgelistpartition.html) |  |  |  | · |  |  |  |  |
| [Excel (xlsx) reader and writer](measures/io_xlsx.html) |  |  |  |  |  |  |  | · |
| [Extra file formats: ncol, lgl, dimacs, graphdb, adjacency list](measures/io_text_formats.html) |  | · |  |  |  |  |  |  |
| [GEXF read and write](measures/io_gexf.html) | ✓ |  |  | · |  | · | · |  |
| [GML read and write](measures/io_gml.html) | ✓ | · | · | · |  | · |  |  |
| [GRAPH6 read and write](measures/io_graph6.html) | · |  |  |  |  | · |  |  |
| [GRAPHDB read and write](measures/io_graphdb.html) |  |  | · |  |  |  |  |  |
| [GraphML read and write](measures/io_graphml.html) | ✓ | · | · | · | · | · |  |  |
| [GRAPHTOOLBINARY read and write](measures/io_graphtoolbinary.html) |  |  |  | · |  |  |  |  |
| [GRAPHVIZ read and write](measures/io_graphviz.html) |  |  | · | · |  | · |  |  |
| [KONECT read and write](measures/io_konect.html) |  |  |  | · |  |  |  |  |
| [LEDA read and write](measures/io_leda.html) | · |  | · |  |  |  |  |  |
| [LEMON read and write](measures/io_lemon.html) |  |  |  |  |  | · |  |  |
| [LGL read and write](measures/io_lgl.html) |  |  | · |  |  |  |  |  |
| [MATLAB read and write](measures/io_matlab.html) |  |  |  | · |  |  |  |  |
| [MATRIX read and write](measures/io_matrix.html) |  |  |  |  |  | · |  |  |
| [MATRIXMARKET read and write](measures/io_matrixmarket.html) |  |  |  |  | · |  |  |  |
| [METIS read and write](measures/io_metis.html) |  |  |  | · |  |  |  |  |
| [MTX read and write](measures/io_mtx.html) |  |  |  | · |  |  |  |  |
| [Multi-matrix DL, edgelist23, nodelist, ranklist, pilesort, VNA](measures/io_ucinet_multi.html) |  |  |  |  |  |  |  | · |
| [NCOL read and write](measures/io_ncol.html) |  |  | · |  |  |  |  |  |
| [NETWORKITBINARY read and write](measures/io_networkitbinary.html) |  |  |  | · |  |  |  |  |
| [Node-link JSON read and write](measures/io_json.html) | ✓ |  |  |  |  | · |  |  |
| [NODELINKJSON read and write](measures/io_nodelinkjson.html) |  |  |  |  | · |  |  |  |
| [Pajek .net read and write](measures/io_pajek.html) | ✓ | · | · |  |  |  |  |  |
| [PICKLE read and write](measures/io_pickle.html) |  |  | · |  |  |  |  |  |
| [RB read and write](measures/io_rb.html) |  |  |  | · |  |  |  |  |
| [SNAP read and write](measures/io_snap.html) |  |  |  | · |  |  |  |  |
| [SNAPEDGELISTPARTITION read and write](measures/io_snapedgelistpartition.html) |  |  |  | · |  |  |  |  |
| [SVG read and write](measures/io_svg.html) |  |  | · |  |  |  |  |  |
| [THRILLGRAPHBINARY read and write](measures/io_thrillgraphbinary.html) |  |  |  | · |  |  |  |  |
| [TSPLIB read and write](measures/io_tsplib.html) |  |  |  |  |  | · |  |  |
| [UCINET binary dataset reader (.##h / .##d)](measures/io_ucinet_binary.html) |  |  |  |  |  |  |  | · |
| [UCINET DL text read and write](measures/io_dl.html) |  |  | · |  |  |  |  | · |

## Layout

44 measures.

| Measure | networkx | igraph | pyigraph | sna | networkit | rustworkx | sknetwork | jgrapht | boost | tnet | graphlayouts | deepwalk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Backbone, focus and centrality (concentric) layouts](measures/layout_focus_backbone.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Barycenter Greedy Two Layered Bipartite Layout2 D](measures/cat_barycenter_bipartite_d_greedy_layered_layout2_two.html) |  |  |  |  |  |  |  | · |  |  |  |  |
| [Circle, tree and two-mode (barycenter) layouts](measures/layout_simple.html) | · | · | · |  |  | · |  |  | · |  |  |  |
| [Davidson-Harel layout](measures/layout_dh.html) |  | · | · |  |  |  |  |  |  |  |  |  |
| [DrL (OpenOrd) layout](measures/layout_drl.html) |  | · | · |  |  |  |  |  |  |  |  |  |
| [Fruchterman-Reingold layout](measures/layout_fruchterman_reingold.html) | · | · | · |  |  | · | · |  | · |  |  |  |
| [GEM layout](measures/layout_gem.html) |  | · |  |  |  |  |  |  |  |  |  |  |
| [Graphopt layout](measures/layout_graphopt.html) |  | · | · |  |  |  |  |  |  |  |  |  |
| [Grid layout](measures/layout_grid.html) |  | · |  |  |  |  |  |  |  |  |  |  |
| [Gursoy atun layout](measures/cat_atun_gursoy_layout.html) |  |  |  |  |  |  |  |  | · |  |  |  |
| [Kamada-Kawai layout](measures/layout_kamada_kawai.html) |  | · | · |  |  | · |  |  | · |  |  |  |
| [Large graph layout (LGL)](measures/layout_lgl.html) |  | · | · |  |  |  |  |  |  |  |  |  |
| [Layout as metromap](measures/cat_as_layout_metromap.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout backbone](measures/cat_backbone_layout.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout centrality](measures/cat_layout.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout centrality group](measures/cat_group_layout.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout constrained stress](measures/cat_constrained_layout_stress.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout constrained stress3 D](measures/cat_constrained_d_layout_stress3.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout dynamic](measures/cat_dynamic_layout.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout focus](measures/cat_focus_layout.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout focus group](measures/cat_focus_group_layout.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout multilevel](measures/cat_layout_multilevel.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout pmds](measures/cat_layout_pmds.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout spectral](measures/cat_layout_spectral.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout stress quality](measures/layout_stress_quality.html) | ∅ |  |  |  |  |  |  |  |  |  |  |  |
| [Layout stress value](measures/layout_stress_value.html) | ∅ |  |  |  |  |  |  |  |  |  |  |  |
| [Layout stress3 D](measures/cat_d_layout_stress3.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout tree unrooted](measures/cat_layout_tree_unrooted.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Layout umap](measures/cat_layout_umap.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Louvain Embedding](measures/cat_embedding_louvain.html) |  |  |  |  |  |  | · |  |  |  |  |  |
| [Maxent Stress](measures/cat_maxent_stress.html) |  |  |  |  | · |  |  |  |  |  |  |  |
| [Median Greedy Two Layered Bipartite Layout2 D](measures/cat_bipartite_d_greedy_layered_layout2_median_two.html) |  |  |  |  |  |  |  | · |  |  |  |  |
| [Multidimensional scaling layout](measures/layout_mds.html) |  | · | · |  |  |  |  |  |  |  |  |  |
| [Node2 Vec](measures/cat_node2_vec.html) |  |  |  |  | · |  |  |  |  |  |  |  |
| [Random layout](measures/layout_random.html) |  | · |  |  |  | · |  |  | · |  |  |  |
| [Reinforcement](measures/cat_reinforcement.html) |  |  |  |  |  |  |  |  |  | · |  |  |
| [Skip-gram embedding](measures/cat_embedding_gram_skip.html) |  |  |  |  |  |  |  |  |  |  |  | · |
| [Sparse stress / pivot MDS layout](measures/layout_sparse_stress.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Sphere layout](measures/layout_sphere.html) |  | · |  |  |  |  |  |  |  |  |  |  |
| [Spring](measures/cat_spring.html) |  |  |  |  |  |  | · |  |  |  |  |  |
| [Stress-majorization layout (Kamada-Kawai energy)](measures/layout_stress.html) | ✓ |  |  |  |  |  |  |  |  |  | · |  |
| [Stresscent](measures/cat_stresscent.html) |  |  |  | · |  |  |  |  |  |  |  |  |
| [Sugiyama layered layout](measures/layout_sugiyama.html) |  | · | · |  |  |  |  |  |  |  |  |  |
| [Two Layered Bipartite Layout2 D](measures/cat_bipartite_d_layered_layout2_two.html) |  |  |  |  |  |  |  | · |  |  |  |  |

## Matrices and spectra

22 measures.

| Measure | networkx | igraph | pyigraph | graphtool | networkit | rustworkx | sknetwork | boost | ucinet | netrankr | centiserve | graspologic | deepwalk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Adjacency](measures/gm_adjacency.html) | ✓ | · | · | · | · | · |  |  |  |  |  |  |  |
| [Bethe entropy](measures/cat_bethe_entropy.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Bethe hessian](measures/gm_bethe_hessian.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Class matrix](measures/gm_class_matrix.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Eigentrust](measures/cat_eigentrust.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Eigenvectors of graph matrices](measures/eigenvectors_matrix.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Estrada index](measures/estrada_index.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Fiedler](measures/gm_fiedler.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gm aperiodic](measures/gm_aperiodic.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Gm laplacian](measures/gm_laplacian.html) | ✓ | · | · | · | · |  | · |  |  |  | · | ≠ |  |
| [Gm modularity](measures/gm_modularity.html) | ✓ | · | · | · |  |  |  |  |  |  |  |  |  |
| [Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence)](measures/matrix_operators.html) |  |  |  | · |  |  |  |  | · |  |  |  |  |
| [Graph spectrum (eigenvalues of a graph matrix)](measures/graph_spectrum.html) | · | · | · |  |  |  |  |  |  |  |  |  |  |
| [Incidence](measures/gm_incidence.html) | ✓ | · | · | · |  |  |  |  | · |  |  |  |  |
| [Magnetic laplacian matrix](measures/cat_laplacian_magnetic_matrix.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sparse-matrix orderings and bandwidth/wavefront](measures/matrix_bandwidth.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Spectral](measures/cat_spectral.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Spectral gap](measures/cat_gap_spectral.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Spectral graph forge](measures/cat_forge_spectral.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Stochastic matrix](measures/cat_matrix_stochastic.html) |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Tournament matrix](measures/cat_matrix_tournament.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Walk corpora and skip-gram embeddings (DeepWalk)](measures/walk_embeddings.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |

## Mixing and assortativity

22 measures.

| Measure | networkx | igraph | pyigraph | graphtool | networkit | sknetwork | bct | bctpy | ucinet | egor | netseg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Assort](measures/assort.html) | ✓ |  |  |  |  |  |  | ≠ |  |  | · |
| [Assortativity degree](measures/assortativity_degree.html) | ✓ | ∅ | ✓ |  |  |  | ≠ |  |  |  |  |
| [Assortativity nominal](measures/assortativity_nominal.html) | ≠ | ∅ | ✓ |  |  |  |  |  | · |  |  |
| [Assortativity values](measures/assortativity_values.html) | ✓ | ∅ | ✓ | · | · |  | · |  |  |  |  |
| [Attribute mixing matrix](measures/cat_attribute_matrix_mixing.html) | · |  |  |  |  |  |  |  |  |  |  |
| [Avg deg conn](measures/avg_deg_conn.html) | ≠ |  |  |  |  |  |  |  |  |  |  |
| [Avg nbr deg](measures/avg_nbr_deg.html) | ≠ |  |  |  |  |  |  |  |  |  |  |
| [Coleman](measures/cat_coleman.html) |  |  |  |  |  |  |  |  |  |  | · |
| [Degree and property correlation histograms](measures/correlation_histograms.html) |  |  |  | · |  |  |  |  |  |  |  |
| [Degree mixing matrix](measures/cat_degree_matrix_mixing.html) | · |  |  |  |  |  |  |  |  |  |  |
| [Ei index](measures/ei_index.html) |  |  |  |  |  |  |  |  | · | ≠ | · |
| [Freeman's segregation index](measures/seg_freeman.html) |  |  |  |  |  |  |  |  |  |  | · |
| [GNNClassifier](measures/cat_classifier_gnn.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Gupta-Anderson-May mixing coefficient](measures/seg_gamix.html) |  |  |  |  |  |  |  |  |  |  | · |
| [Local assortativity](measures/cat_assortativity_local.html) |  |  |  |  |  |  | · |  |  |  |  |
| [Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed)](measures/cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected.html) |  |  |  |  |  |  |  |  | · |  |  |
| [Mixing](measures/mixing.html) | ✓ |  |  |  |  |  |  |  | · |  |  |
| [NNClassifier](measures/cat_classifier_nn.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Odds ratio of within-group ties (ORWG)](measures/seg_orwg.html) |  |  |  |  |  |  |  |  |  |  | · |
| [Rank Classifier](measures/cat_classifier_rank.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Segregation matrix index (SMI)](measures/seg_smi.html) |  |  |  |  |  |  |  |  |  |  | · |
| [Spectral segregation index (SSI)](measures/seg_ssi.html) |  |  |  |  |  |  |  |  |  |  | · |

## Paths and distances

62 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | graphblas | bct | bctpy | gephi | ucinet | tnet | keyplayer | centiserve | s2 | sf | deepwalk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Algebraic Distance Sparsifier](measures/cat_algebraic_distance_sparsifier.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [All Directed Paths](measures/cat_all_directed_path.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Barycenter](measures/dm_barycenter.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Bfs iterator](measures/cat_bfs_iterator.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Center](measures/dm_center.html) | ✓ | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Closeness vitality](measures/dm_closeness_vitality.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Complex Paths](measures/cat_complex_path.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dag longest path](measures/cat_dag_longest_path.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dag longest path length](measures/cat_dag_length_longest_path.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dag weighted longest path](measures/cat_dag_longest_path_weighted.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dag weighted longest path length](measures/cat_dag_length_longest_path_weighted.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Deepwalk](measures/cat_deepwalk.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Diameter](measures/diameter.html) | ✓ | ✓ | ✓ |  |  | · | ∅ |  |  | ≠ | ≠ |  | ≠ | ✓ | ✓ | · |  |  |  |  |  |  |
| [Distance histogram](measures/cat_distance_histogram.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Distances](measures/distances.html) | ✓ | ✓ | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | · |  |  |  |  |  |
| [Eccentricity](measures/eccentricity.html) | ✓ | ✓ | ✓ |  |  |  | ∅ |  |  | ≠ | ≠ |  | ≠ | ✓ | ✓ | · |  |  |  |  |  |  |
| [Edge lengths](measures/edge_lengths.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |
| [Findpaths](measures/cat_findpaths.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Findwalks](measures/cat_findwalks.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Ged Walk](measures/cat_ged_walk.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Geokpath](measures/cat_geokpath.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Global and local efficiency](measures/efficiency_global.html) | · | · |  | · |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Group geometry](measures/group_geometry.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |
| [Heavy Path Decomposition](measures/cat_decomposition_heavy_path.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Index](measures/dm_index.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  | ≠ | ✓ |  |  |  |  |  |  |  |  |
| [Is distance regular](measures/cat_distance_is_regular.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Johnson lengths](measures/nxs_johnson_lengths.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Kpath census](measures/cat_census_kpath.html) |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Local efficiency](measures/dm_local_efficiency.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  | ≠ | ≠ |  |  |  |  |  |  |  |  |
| [Longest simple path](measures/paths_longest_simple.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Many-to-many and hierarchy-based shortest paths](measures/paths_hierarchy.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Mean distance](measures/mean_distance.html) | ✓ | ✓ | ✓ |  |  |  |  | · |  |  |  |  |  | ✓ | ✓ | · |  |  |  |  |  |  |
| [Minimum/maximum cycle ratio and mean cycle](measures/cycle_ratio.html) |  |  |  |  |  |  |  |  |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Mreach degree](measures/cat_degree_mreach.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Neighborhood function, hop plot, effective diameter](measures/neighborhood_function.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Path transitivity](measures/cat_path_transitivity.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Paths all pairs](measures/paths_all_pairs.html) | ✓ | · |  |  |  |  | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths all shortest](measures/paths_all_shortest.html) | ✓ | · | · |  |  | · |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths astar](measures/paths_astar.html) | ✓ |  | · |  |  | · | · | · |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Paths bidirectional](measures/paths_bidirectional.html) | ✓ |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths count](measures/paths_count.html) | ✓ |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths floyd warshall](measures/paths_floyd_warshall.html) | ✓ |  |  |  |  |  |  | · |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Paths johnson](measures/paths_johnson.html) | ✓ |  |  |  |  |  |  |  |  | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Paths k shortest](measures/paths_k_shortest.html) | ✓ | · | · |  |  |  |  | · |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths multi source](measures/paths_multi_source.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths negative](measures/paths_negative.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths negative cycle](measures/paths_negative_cycle.html) | ✓ |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths predecessors](measures/paths_predecessors.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths simple](measures/paths_simple.html) | ✓ | · | · |  |  | · | · | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Paths sssp](measures/paths_sssp.html) | ✓ | · | · |  |  | · | · | · | · | · | · |  |  |  |  |  |  |  |  |  |  |  |
| [Periphery](measures/dm_periphery.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Proximity](measures/proximity.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  | ✓ | ✓ |  |
| [R c shortest paths](measures/cat_c_path_r_shortest.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Radius](measures/radius.html) | · | ✓ | ✓ |  |  |  |  |  |  | ≠ | ≠ |  | ≠ | ✓ | ✓ |  |  |  |  |  |  |  |
| [Random BFS](measures/cat_bfs_random.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Reachability](measures/reachability.html) | ✓ | ✓ | ✓ |  |  |  |  | · |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Reachable Nodes](measures/cat_reachable.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Reachdist](measures/cat_reachdist.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Retrieve shortest path](measures/cat_path_retrieve_shortest.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Reverse BFS](measures/cat_bfs_reverse.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Structural equivalence: profile (correlation, Euclidean, etc ), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row](measures/cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural.html) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |
| [Twopath](measures/cat_twopath.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Roles and positions

64 measures.

| Measure | networkx | igraph | pyigraph | sna | rsiena | graphtool | networkit | rustworkx | jgrapht | boost | bct | ucinet | netrankr | blockmodeling | manynet | cpnet | nauty |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Alt Higher Ego X](measures/cat_alt_ego_higher_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Automorphic (Max Sim) and regular equivalence (REGE, CATREGE)](measures/cat_automorphic_catrege_equivalence_max_rege_regular_sim.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Automorphic equivalence](measures/automorphic_equivalence.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  | ✓ |
| [Av Alt Ego X](measures/cat_alt_av_ego_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Group Ego X](measures/cat_av_ego_group_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim Ego X](measures/cat_av_ego_sim_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Av Sim Pop Ego](measures/cat_av_ego_pop_sim.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Block density](measures/block_density.html) |  |  |  | ✓ |  |  |  |  |  |  |  | · |  | ✓ |  |  |  |
| [Bridging centrality](measures/bridging_centrality.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Bridging coefficient](measures/bridging_coefficient.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Brokerage](measures/brokerage.html) |  |  |  | ✓ |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Categorical edge match](measures/cat_categorical_edge_match.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Categorical multiedge match](measures/cat_categorical_match_multiedge.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Categorical node match](measures/cat_categorical_match.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Chain decomposition](measures/cat_chain_decomposition.html) |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Classical mds](measures/classical_mds.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Cognitive social structures with accuracy measures](measures/css_accuracy.html) |  |  |  | · |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Concor](measures/concor.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Constraint](measures/constraint.html) | ≠ | ✓ | ✓ |  |  |  |  |  |  |  |  | · |  |  | ✓ |  |  |
| [Core Decomposition Sequence](measures/cat_core_decomposition_sequence.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| [Core periphery](measures/core_periphery.html) |  |  |  |  |  |  |  |  |  |  | · | · |  |  |  | ✓ |  |
| [Core periphery continuous](measures/core_periphery_continuous.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  | ✓ |  |
| [Direct blockmodel search (structural, regular, generalised block types)](measures/blockmodel_search.html) |  |  |  |  |  |  |  |  |  |  |  | · |  | · |  |  |  |
| [Div In ego](measures/cat_div_ego.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Div Out ego](measures/cat_div_ego_out.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Dulmage Mendelsohn Decomposition](measures/cat_decomposition_dulmage_mendelsohn.html) |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Effective size](measures/effective_size.html) | ≠ |  |  |  |  |  |  |  |  |  |  | · |  |  | ≠ |  |  |
| [Efficiency](measures/efficiency.html) | ≠ |  |  |  |  |  |  |  |  |  |  | · |  |  | ≠ |  |  |
| [Ego Alter Combi](measures/cat_alter_combi_ego.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego Alter Covar Comb](measures/cat_alter_comb_covar_ego.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego Diff X](measures/cat_diff_ego_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego LThreshold X](measures/cat_ego_l_threshold_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego Plus Alt Sq X](measures/cat_alt_ego_plus_sq_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego Plus Alt X](measures/cat_alt_ego_plus_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego RThreshold X](measures/cat_ego_r_threshold_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego Sq X](measures/cat_ego_sq_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego X](measures/cat_ego_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego X gmm](measures/cat_ego_gmm_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego Xalt X](measures/cat_ego_x_xalt.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego Xalt XRecip](measures/cat_ego_recip_x_xalt.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Egotize (6 750), Ego network extraction with tab "Ego"](measures/cat_6_750_ego_egotize_extraction_tab_with.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Equivalence measures: matches, positive matches, overlaps, cross-products, coverage](measures/equivalence_extra.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Estevez-Nordlund variant](measures/core_periphery_en.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Guttman scaling, K-means and quick clustering](measures/guttman_kmeans.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Hierarchy](measures/hierarchy.html) |  | · |  | · |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [In Act ego](measures/cat_act_ego.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Makeegonets](measures/cat_makeegonets.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Mcgregor common subgraphs](measures/cat_common_mcgregor_subgraphs.html) |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Minimize nested blockmodel dl](measures/cat_blockmodel_dl_minimize_nested.html) |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| [Non-metric MDS with stress-1](measures/mds_nonmetric.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Out Act ego](measures/cat_act_ego_out.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Act More ego](measures/cat_act_ego_more_out.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out Act Sqrt More ego](measures/cat_act_ego_more_out_sqrt.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Out More ego](measures/cat_ego_more_out.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Positional dominance](measures/cat_dominance_positional.html) |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| [Reci Act ego](measures/cat_act_ego_reci.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Regular equivalence](measures/regular_equivalence.html) |  |  |  | ✓ |  |  |  |  |  |  |  | · |  | · |  |  |  |
| [Same Ego Dist2](measures/cat_dist2_ego_same.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Sim Ego Dist2](measures/cat_dist2_ego_sim.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Structural equivalence](measures/structural_equivalence.html) |  |  |  | ✓ |  |  |  |  |  |  |  | · |  | ≠ |  |  |  |
| [Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6 798), "corrected constraint" FA](measures/cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| [Tot Alt Ego X](measures/cat_alt_ego_tot_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Group Ego X](measures/cat_ego_group_tot_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tot Sim Ego X](measures/cat_ego_sim_tot_x.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |

## Signed and multilayer

8 measures.

| Measure | ergm | rsiena | graphtool | ucinet | signnet | pymnet | multinet |
|---|---|---|---|---|---|---|---|
| [Balance](measures/cat_balance.html) | · | · |  |  |  |  |  |
| [Layered Block State](measures/cat_block_layered_state.html) |  |  | · |  |  |  |  |
| [Layered Overlap Block State](measures/cat_block_layered_overlap_state.html) |  |  | · |  |  |  |  |
| [Layered Weighted Block State](measures/cat_block_layered_state_weighted.html) |  |  | · |  |  |  |  |
| [Layered Weighted Overlap Block State](measures/cat_block_layered_overlap_state_weighted.html) |  |  | · |  |  |  |  |
| [Multilayer networks (node-layers, supra-adjacency)](measures/multilayer.html) |  |  |  |  |  | · | · |
| [Positive-negative centrality (signed ties)](measures/pn_centrality.html) |  |  |  | · | · |  |  |
| [Structural balance, frustration index, signed blockmodels](measures/signed_balance.html) |  |  |  |  | · |  |  |

## Statistical fitting

24 measures.

| Measure | networkx | igraph | pyigraph | ergm | rsiena | graphtool | bct | latentnet | missSBM | goldfish | gergm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Actor-oriented event models (DyNAM)](measures/dynam.html) |  |  |  |  |  |  |  |  |  | · |  |
| [Conditional edge prediction](measures/cat_conditional_edge_prediction.html) |  |  |  |  |  |  |  |  |  |  | · |
| [Constant potts model (community)](measures/cat_constant_model_potts-community.html) | · |  |  |  |  |  |  |  |  |  |  |
| [Ergm change sums](measures/ergm_change_sums.html) |  |  |  | ✓ |  |  |  |  |  |  |  |
| [Ergm mcmle](measures/ergm_mcmle.html) |  |  |  | ✓ |  |  |  |  |  |  |  |
| [Ergm mple](measures/ergm_mple.html) |  |  |  | ✓ |  |  |  |  |  |  |  |
| [Ergm sim mean](measures/ergm_sim_mean.html) |  |  |  | ✓ |  |  |  |  |  |  |  |
| [Ergm statistics](measures/ergm_statistics.html) |  |  |  | ✓ |  |  |  |  |  |  |  |
| [Evaluate generative model](measures/cat_evaluate_generative_model.html) |  |  |  |  |  |  | · |  |  |  |  |
| [Generative model](measures/cat_generative_model.html) |  |  |  |  |  |  | · |  |  |  |  |
| [Hierarchical random graph (fit, sample, predict)](measures/hrg.html) |  | · |  |  |  |  |  |  |  |  |  |
| [Latent Closure Block State](measures/cat_block_closure_latent_state.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Latent loglik](measures/latent_loglik.html) |  |  |  |  |  |  |  | ✓ |  |  |  |
| [Latent Mask Block State](measures/cat_block_latent_mask_state.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Latent move delta](measures/latent_move_delta.html) |  |  |  |  |  |  |  | ✓ |  |  |  |
| [Latent multigraph](measures/cat_latent_multigraph.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Latent Multigraph Block State](measures/cat_block_latent_multigraph_state.html) |  |  |  |  |  | · |  |  |  |  |  |
| [Power-law fit of a degree distribution](measures/power_law_fit.html) |  | · | · |  |  |  |  |  |  |  |  |
| [Saom sim mean](measures/saom_sim_mean.html) |  |  |  |  | ≠ |  |  |  |  |  |  |
| [Sbm description length](measures/sbm_description_length.html) |  |  |  |  |  | ✓ |  |  |  |  |  |
| [Sbm fit](measures/sbm_fit.html) |  |  |  |  |  | ✓ |  |  |  |  |  |
| [Sbm move delta](measures/sbm_move_delta.html) |  |  |  |  |  | ✓ |  |  |  |  |  |
| [Stochastic block models for partially observed networks](measures/sbm_missing.html) |  |  |  |  |  |  |  |  | · |  |  |
| [Valued-network ERGM (GERGM)](measures/gergm.html) |  |  |  |  |  |  |  |  |  |  | · |

## Temporal and events

12 measures.

| Measure | networkx | tsna | networkit | bct | gephi | remstats | goldfish |
|---|---|---|---|---|---|---|---|
| [Dynamic Degree](measures/cat_degree_dynamic.html) |  |  |  |  | · |  |  |
| [Incremental maintenance on a changing graph](measures/dynamic_update.html) |  |  | · |  |  |  |  |
| [Mean first passage time](measures/cat_first_mean_passage_time.html) |  |  |  | · |  |  |  |
| [Rem fit](measures/rem_fit.html) |  |  |  |  |  | ≠ | · |
| [Rem statistic](measures/rem_statistic.html) |  |  |  |  |  | ✓ |  |
| [T Ergm Stats](measures/cat_ergm_stats_t.html) |  | · |  |  |  |  |  |
| [T Sna Stats](measures/cat_sna_stats_t.html) |  | · |  |  |  |  |  |
| [Temporal paths](measures/temporal_paths.html) |  | ✓ |  |  |  |  |  |
| [Temporal reach](measures/temporal_reach.html) |  | ✓ |  |  |  |  |  |
| [Time Projected Network](measures/cat_projected_time.html) |  | · |  |  |  |  |  |
| [Time Respecting Di Graph Matcher](measures/cat_di_matcher_respecting_time.html) | · |  |  |  |  |  |  |
| [Time Respecting Graph Matcher](measures/cat_matcher_respecting_time.html) | · |  |  |  |  |  |  |

## Traversal, trees and DAGs

84 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | graphtool | networkit | rustworkx | sknetwork | jgrapht | boost | netrankr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Ahuja Orlin Sharma Capacitated Minimum Spanning Tree](measures/cat_ahuja_capacitated_minimum_orlin_sharma_spanning_tree.html) |  |  |  |  |  |  |  |  |  | · |  |  |
| [All topological](measures/all_topological.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Antichain width](measures/gb_antichain_width.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Astar](measures/ord_astar.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Beam](measures/trav_beam.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Bellman ford](measures/ord_bellman_ford.html) | ✓ |  |  |  |  | · |  | · |  | · | · |  |
| [Bfs edges](measures/trav_bfs_edges.html) | ✓ | · | · |  |  | · | · | · | · | · | · |  |
| [Bfs labeled](measures/trav_bfs_labeled.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Bfs layers](measures/trav_bfs_layers.html) | ✓ |  |  |  |  |  |  | · |  |  |  |  |
| [Bidir bfs](measures/ord_bidir_bfs.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Bidir dijkstra](measures/ord_bidir_dijkstra.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Binomial tree](measures/cat_binomial_tree.html) | · |  |  |  |  |  |  | · |  |  |  |  |
| [Branching](measures/branching.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Branching weight](measures/gb_branching_weight.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Broadcast time](measures/gb_broadcast_time.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Chain count](measures/gb_chain_count.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Closure](measures/closure.html) | ✓ | · |  |  |  | · |  |  |  | · | · |  |
| [Consensus tree](measures/cat_consensus_tree.html) |  | · |  |  |  |  |  |  |  |  |  |  |
| [Cycle count](measures/gb_cycle_count.html) | ✓ |  |  |  | ✓ |  |  |  |  |  |  |  |
| [D separated](measures/gb_d_separated.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Dag lca](measures/dag_lca.html) | ≠ |  |  |  |  |  |  |  |  |  |  |  |
| [Dag to branching](measures/cat_branching_dag_to.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Dedensify](measures/gb_dedensify.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Dfs events](measures/trav_dfs_events.html) | ✓ |  |  |  |  |  |  |  |  | · |  |  |
| [Dfs iterator](measures/cat_dfs_iterator.html) |  |  |  |  |  | · |  |  |  |  |  |  |
| [Dijkstra](measures/ord_dijkstra.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Edge bfs](measures/trav_edge_bfs.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Edge dfs](measures/trav_edge_dfs.html) | ✓ | · | · |  |  | · |  | · |  |  | · |  |
| [Esau Williams Capacitated Minimum Spanning Tree](measures/cat_capacitated_esau_minimum_spanning_tree_williams.html) |  |  |  |  |  |  |  |  |  | · |  |  |
| [Eulerian circuits and paths](measures/eulerian.html) |  |  |  |  |  |  |  |  |  | · |  |  |
| [Frontiers](measures/frontiers.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Gb aperiodic](measures/gb_aperiodic.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Gb disjoint paths](measures/gb_disjoint_paths.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Generations](measures/generations.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Get hierarchy tree](measures/cat_hierarchy_tree.html) |  |  |  |  |  | · |  |  |  |  |  |  |
| [Idom](measures/idom.html) | ✓ | · |  |  |  | · |  | · |  |  | · |  |
| [Is dag](measures/is_dag.html) | ✓ | · | · |  |  | · |  | ✓ | · |  |  |  |
| [Is eulerian](measures/gb_is_eulerian.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Isolates](measures/gb_isolates.html) | ✓ |  |  | · | · |  |  | · |  |  |  |  |
| [Join trees](measures/cat_join_tree.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [K edge subgraphs](measures/gb_k_edge_subgraphs.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Lex topo](measures/gb_lex_topo.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Lexicographic](measures/lexicographic.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Longest length](measures/longest_length.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Longest path](measures/longest_path.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Longest path len](measures/gb_longest_path_len.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Maxflow](measures/gb_maxflow.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Maximum cardinality search](measures/cat_cardinality_maximum_search.html) |  |  | · |  |  |  |  |  |  |  |  |  |
| [Mcb weight](measures/gb_mcb_weight.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Mincost](measures/gb_mincost.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Moral edges](measures/gb_moral_edges.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Mst weight](measures/gb_mst_weight.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Node boundary](measures/gb_node_boundary.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Number of nonisomorphic trees](measures/cat_nonisomorphic_tree.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Palmer Hamiltonian Cycle](measures/cat_cycle_hamiltonian_palmer.html) |  |  |  |  |  |  |  |  |  | · |  |  |
| [Predecessor tree](measures/cat_predecessor_tree.html) |  |  |  |  |  | · |  |  |  |  |  |  |
| [Quotient internal](measures/gb_quotient_internal.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Random labeled rooted forest](measures/cat_forest_labeled_random_rooted.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Random Maximum Spanning Forest](measures/cat_forest_maximum_random_spanning.html) |  |  |  |  |  |  | · |  |  |  |  |  |
| [Random powerlaw tree](measures/cat_powerlaw_random_tree.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Random powerlaw tree sequence](measures/cat_powerlaw_random_sequence_tree.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Random spanning tree](measures/random_spanning_tree.html) | · | · |  |  |  | · |  |  |  |  | · |  |
| [Random unlabeled rooted forest](measures/cat_forest_random_rooted_unlabeled.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Random walk generation and sampling](measures/random_walk_sampling.html) |  |  |  |  |  |  |  |  |  | · | · |  |
| [Random walks](measures/random_walk.html) | · | · | · |  |  |  |  | · |  |  |  |  |
| [Reduction](measures/reduction.html) | ✓ |  |  |  |  |  |  | · |  | · | · | · |
| [Rst edge freq](measures/rst_edge_freq.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Snap groups](measures/gb_snap_groups.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Spanner ok](measures/gb_spanner_ok.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Spanning tree](measures/spanning_tree.html) | ✓ | · | · |  |  | · | · | · |  | · | · |  |
| [Spanning trees](measures/gb_spanning_trees.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Spanning weight](measures/spanning_weight.html) | ✓ |  |  |  |  |  | ✓ | ✓ |  | ✓ | ✓ |  |
| [Steiner tree](measures/steiner_tree.html) | · |  |  |  |  |  |  | · |  | · |  |  |
| [Stoer wagner](measures/gb_stoer_wagner.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Topo levels](measures/gb_topo_levels.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| [Topological sort](measures/topological_sort.html) | ✓ | · | · |  |  | · |  | · |  |  | · |  |
| [Tree broadcast center](measures/cat_broadcast_center_tree.html) | · |  |  |  |  |  |  |  |  |  |  |  |
| [Tree lca](measures/tree_lca.html) | ✓ |  |  |  |  |  |  |  |  | · |  |  |
| [Tree sampling divergence](measures/cat_divergence_sampling_tree.html) |  |  |  |  |  |  |  |  | · |  |  |  |
| [Two graphs common spanning trees](measures/cat_common_spanning_tree_two.html) |  |  |  |  |  |  |  |  |  |  | · |  |
| [Unfold tree](measures/cat_tree_unfold.html) |  | · | · |  |  |  |  |  |  |  |  |  |
| [Union Maximum Spanning Forest](measures/cat_forest_maximum_spanning_union.html) |  |  |  |  |  |  | · |  |  |  |  |  |
| [Vertex orderings (max cardinality, degeneracy)](measures/vertex_orderings.html) |  |  |  |  |  |  |  |  |  | · | · |  |
| [Walks](measures/gb_walks.html) | ✓ |  |  |  |  |  | · |  |  |  |  |  |

## Two-mode and bipartite

35 measures.

| Measure | networkx | igraph | pyigraph | sna | ergm | graphtool | rustworkx | sknetwork | jgrapht | boost | ucinet | tnet | egor | backbone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [Backbone extraction (SDSM/BiCM, FDSM, fixed-row/column/fill)](measures/backbone_extraction.html) |  |  |  |  |  |  |  |  |  |  |  |  |  | · |
| [Bipartite](measures/cat_bipartite.html) |  | · |  |  |  |  |  |  |  | · |  |  |  |  |
| [Bipartite color](measures/bipartite_color.html) | ✓ | · | · |  |  | · | · | · |  | · |  |  |  |  |
| [Bipartite edge color](measures/cat_bipartite_color_edge.html) |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| [Bipartite modularity](measures/bipartite_modularity.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Birank](measures/birank.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Butterflies](measures/butterflies.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Coincidence](measures/cat_coincidence.html) |  |  |  |  | · |  |  |  |  |  |  |  |  |  |
| [Ego members](measures/ego_members.html) | ✓ | ✓ |  | · |  |  |  |  |  |  |  |  |  |  |
| [Ego\_summary / betweenness](measures/ego_summary-betweenness.html) | ✓ | ✓ |  |  |  |  |  |  |  |  | · |  |  |  |
| [Ego\_summary / components](measures/ego_summary-components.html) | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| [Ego\_summary / density](measures/ego_summary-density.html) | ✓ | ✓ |  |  |  |  |  |  |  |  | · |  | ✓ |  |
| [Ego\_summary / ties](measures/ego_summary-ties.html) | ✓ | ✓ |  |  |  |  |  |  |  |  | · |  |  |  |
| [Hopcroft karp](measures/hopcroft_karp.html) | ✓ | · | · |  |  |  |  |  | · | · |  |  |  |  |
| [Is bipartite node set (bipartite)](measures/cat_bipartite_is_set-bipartite.html) | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Latapy clustering](measures/latapy_clustering.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Maximal extendability](measures/maximal_extendability.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Min weight full matching](measures/min_weight_full_matching.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Node redundancy](measures/node_redundancy.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nx eppstein](measures/nx_eppstein.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nx eppstein size](measures/nx_eppstein_size.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Nx hk mates](measures/nx_hk_mates.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Project](measures/project.html) | ∅ | ∅ | · |  | · |  |  |  |  |  | · | ✓ |  |  |
| [Projection](measures/projection.html) | ✓ |  |  |  |  | · |  |  |  |  |  |  |  |  |
| [Robins alexander](measures/robins_alexander.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Spectral bipartivity](measures/spectral_bipartivity.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Two-mode clustering coefficients (six-cycle)](measures/twomode_cc.html) |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| [Two-mode core-periphery, bi-cliques, two-mode equivalence](measures/twomode_core_biclique.html) |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine)](measures/projection_weights.html) |  |  |  |  |  |  |  |  |  |  | · | · |  |  |
| [Twomode / betweenness](measures/twomode-betweenness.html) | ∅ | ∅ |  |  |  |  |  |  |  |  | · |  |  |  |
| [Twomode / closeness](measures/twomode-closeness.html) | ≠ | ∅ |  |  |  |  |  |  |  |  | · |  |  |  |
| [Twomode / degree](measures/twomode-degree.html) | ∅ | ∅ |  |  |  |  |  |  |  |  | · |  |  |  |
| [Twomode / density](measures/twomode-density.html) | ∅ |  |  |  |  |  |  |  |  |  | · |  |  |  |
| [Twomode / eigenvector](measures/twomode-eigenvector.html) |  | ✓ |  |  |  |  |  |  |  |  | · |  |  |  |
| [Vertex cover](measures/vertex_cover.html) | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
{% endraw %}
