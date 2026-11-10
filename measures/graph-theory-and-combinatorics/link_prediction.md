---
title: "Link prediction scores"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Link prediction scores {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Similarity and link prediction. Concept id: `link_prediction`. 1 measure.

## Definition {#concept-definition}

Link prediction score of each listed pair of nodes: common neighbors, Jaccard, Adamic-Adar and the other neighborhood indices.

## References {#concept-references}

[adamic2003friends](../../references.html#adamic2003friends), [ahmad2020missing](../../references.html#ahmad2020missing), [barabasi1999emergence](../../references.html#barabasi1999emergence), [hagberg2008exploring](../../references.html#hagberg2008exploring), [liben2007link](../../references.html#liben2007link), [soundarajan2012using](../../references.html#soundarajan2012using), [zhou2009predicting](../../references.html#zhou2009predicting)

## Link prediction {#link_prediction}

Measure id: `link_prediction`. Original family: Graph theory and combinatorics.

**Definition.** Link prediction score of each listed pair of nodes: common neighbors, Jaccard, Adamic-Adar and the other neighborhood indices.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `adamic_adar_index; cn_soundarajan_hopcroft; common_neighbor_centrality; jaccard_coefficient; preferential_attachment; ra_index_soundarajan_hopcroft; resource_allocation_index; within_inter_cluster` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `similarity` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `similarity_dice; similarity_inverse_log_weighted; similarity_jaccard` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `similarity; vertex_similarity` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `AdamicAdarDistance; AdamicAdarIndex; AlgebraicDistanceIndex; CommonNeighborsIndex; JaccardDistance; JaccardIndex; LinkThresholder; MissingLinksFinder; NeighborhoodDistanceIndex; NeighborsMeasureIndex; PreferentialAttachmentIndex; ResourceAllocationIndex` | API listing |
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `NNLinker` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `AdamicAdarIndexLinkPrediction; CommonNeighborsLinkPrediction; HubDepressedIndexLinkPrediction; HubPromotedIndexLinkPrediction; JaccardCoefficientLinkPrediction; LeichtHolmeNewmanIndexLinkPrediction; PreferentialAttachmentLinkPrediction; ResourceAllocationIndexLinkPrediction; SaltonIndexLinkPrediction; SorensenIndexLinkPrediction; SørensenIndexLinkPrediction` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `lp_adamic_adar_all` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.adamic_adar_index(G, all pairs u < v)` |  |
| `lp_adamic_adar_non_edges` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.adamic_adar_index(G, nx.non_edges(G))` |  |
| `lp_cn_sh_all` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.cn_soundarajan_hopcroft(G, all pairs u < v, community = 'community')` |  |
| `lp_cn_sh_non_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.cn_soundarajan_hopcroft(G, nx.non_edges(G), community = 'community')` |  |
| `lp_cnc_all` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.common_neighbor_centrality(G, all pairs u < v, alpha = 0.8)` |  |
| `lp_cnc_all_alpha_095` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.common_neighbor_centrality(G, all pairs u < v, alpha = 0.95)` |  |
| `lp_cnc_non_edges` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.common_neighbor_centrality(G, nx.non_edges(G), alpha = 0.8)` |  |
| `lp_cnc_non_edges_alpha_030` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.common_neighbor_centrality(G, nx.non_edges(G), alpha = 0.3)` |  |
| `lp_common_neighbors_all` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.common_neighbors(G, u, v)) for every pair u < v` |  |
| `lp_common_neighbors_non_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.common_neighbors(G, u, v)) for each pair of nx.non_edges(G)` |  |
| `lp_jaccard_all` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.jaccard_coefficient(G, all pairs u < v)` |  |
| `lp_jaccard_non_edges` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.jaccard_coefficient(G, nx.non_edges(G))` |  |
| `lp_preferential_attachment_all` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.preferential_attachment(G, all pairs u < v)` |  |
| `lp_preferential_attachment_non_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.preferential_attachment(G, nx.non_edges(G))` |  |
| `lp_ra_sh_all` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.ra_index_soundarajan_hopcroft(G, all pairs u < v, community = 'community')` |  |
| `lp_ra_sh_non_edges` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.ra_index_soundarajan_hopcroft(G, nx.non_edges(G), community = 'community')` |  |
| `lp_resource_allocation_all` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.resource_allocation_index(G, all pairs u < v)` |  |
| `lp_resource_allocation_non_edges` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.resource_allocation_index(G, nx.non_edges(G))` |  |
| `lp_wic_all` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.within_inter_cluster(G, all pairs u < v, delta = 0.001, community = 'community')` |  |
| `lp_wic_all_delta_002` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.within_inter_cluster(G, all pairs u < v, delta = 0.02, community = 'community')` |  |
| `lp_wic_non_edges` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.within_inter_cluster(G, nx.non_edges(G), delta = 0.001, community = 'community')` |  |
| `lp_wic_non_edges_delta_05` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.within_inter_cluster(G, nx.non_edges(G), delta = 0.5, community = 'community')` |  |

**References:** [adamic2003friends](../../references.html#adamic2003friends), [ahmad2020missing](../../references.html#ahmad2020missing), [barabasi1999emergence](../../references.html#barabasi1999emergence), [hagberg2008exploring](../../references.html#hagberg2008exploring), [liben2007link](../../references.html#liben2007link), [soundarajan2012using](../../references.html#soundarajan2012using), [zhou2009predicting](../../references.html#zhou2009predicting)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
