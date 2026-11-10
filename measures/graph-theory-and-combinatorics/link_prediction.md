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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `adamic_adar_index; cn_soundarajan_hopcroft; common_neighbor_centrality; jaccard_coefficient; preferential_attachment; ra_index_soundarajan_hopcroft; resource_allocation_index; within_inter_cluster` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-link_prediction-igraph) | `similarity` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-link_prediction-pyigraph) | `similarity_dice; similarity_inverse_log_weighted; similarity_jaccard` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-link_prediction-graphtool) | `similarity; vertex_similarity` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-link_prediction-networkit) | `AdamicAdarDistance; AdamicAdarIndex; AlgebraicDistanceIndex; CommonNeighborsIndex; JaccardDistance; JaccardIndex; LinkThresholder; MissingLinksFinder; NeighborhoodDistanceIndex; NeighborsMeasureIndex; PreferentialAttachmentIndex; ResourceAllocationIndex` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-link_prediction-sknetwork) | `NNLinker` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-link_prediction-jgrapht) | `AdamicAdarIndexLinkPrediction; CommonNeighborsLinkPrediction; HubDepressedIndexLinkPrediction; HubPromotedIndexLinkPrediction; JaccardCoefficientLinkPrediction; LeichtHolmeNewmanIndexLinkPrediction; PreferentialAttachmentLinkPrediction; ResourceAllocationIndexLinkPrediction; SaltonIndexLinkPrediction; SorensenIndexLinkPrediction; SørensenIndexLinkPrediction` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-link_prediction-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: similarity.
- <a id="why-link_prediction-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: similarity\_dice; similarity\_inverse\_log\_weighted; similarity\_jaccard.
- <a id="why-link_prediction-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: similarity; vertex\_similarity.
- <a id="why-link_prediction-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AdamicAdarDistance; AdamicAdarIndex; AlgebraicDistanceIndex; CommonNeighborsIndex; JaccardDistance; JaccardIndex; LinkThresholder; MissingLinksFinder; NeighborhoodDistanceIndex; NeighborsMeasureIndex; PreferentialAttachmentIndex; ResourceAllocationIndex.
- <a id="why-link_prediction-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: NNLinker.
- <a id="why-link_prediction-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: AdamicAdarIndexLinkPrediction; CommonNeighborsLinkPrediction; HubDepressedIndexLinkPrediction; HubPromotedIndexLinkPrediction; JaccardCoefficientLinkPrediction; LeichtHolmeNewmanIndexLinkPrediction; PreferentialAttachmentLinkPrediction; ResourceAllocationIndexLinkPrediction; SaltonIndexLinkPrediction; SorensenIndexLinkPrediction; SørensenIndexLinkPrediction.

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
