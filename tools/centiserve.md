---
title: "centiserve"
layout: default
parent: Tools
---

{% raw %}
# centiserve

| Field | Value |
|---|---|
| Identifier | `centiserve` |
| Language | R |
| Version tested | 1.0.0 |
| License | see package DESCRIPTION |
| Homepage | <https://cran.r-project.org/package=centiserve> |
| Role | checked |
| Citation | [jalili2015centiserver](../references.html#jalili2015centiserver) |

## How it was run

Called from R on igraph objects.

Capabilities listed by introspection of R package centiserve: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 3 |
| reported in docs (·) | 31 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Communicability betweenness](../measures/centrality/communicability_betweenness.html) | [Communicability betweenness](../measures/centrality/communicability_betweenness.html#cx_communicability_betweenness) | ✓ checked, agrees | `communibet` |
| Centrality | Betweenness, load and flow | [K-path centrality](../measures/centrality/k_path_centrality.html) | [Geokpath](../measures/centrality/k_path_centrality.html#cat_geokpath) | · reported in docs | `geokpath` |
| Centrality | Distance-based | [Average distance centrality](../measures/centrality/average_distance_centrality.html) | [Averagedis](../measures/centrality/average_distance_centrality.html#cat_averagedis) | · reported in docs | `averagedis` |
| Centrality | Distance-based | [Average distance centrality](../measures/centrality/average_distance_centrality.html) | [Pairwisedis](../measures/centrality/average_distance_centrality.html#cat_pairwisedis) | · reported in docs | `pairwisedis` |
| Centrality | Distance-based | [Bottleneck centrality](../measures/centrality/bottleneck_centrality.html) | [Bottleneck](../measures/centrality/bottleneck_centrality.html#cat_bottleneck) | · reported in docs | `bottleneck` |
| Centrality | Distance-based | [Centroid centrality](../measures/centrality/centroid_centrality.html) | [Centroid](../measures/centrality/centroid_centrality.html#cat_centroid) | · reported in docs | `centroid` |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | · reported in docs | `closeness.freeman` |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness latora](../measures/centrality/closeness.html#cat_closeness_latora) | · reported in docs | `closeness.latora` |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness residual](../measures/centrality/closeness.html#cat_closeness_residual) | · reported in docs | `closeness.residual` |
| Centrality | Distance-based | [Decay centrality](../measures/centrality/decay_centrality.html) | [Decay](../measures/centrality/decay_centrality.html#cat_decay) | · reported in docs | `decay` |
| Centrality | Distance-based | [Harmonic centrality](../measures/centrality/harmonic_centrality.html) | [Harmonic](../measures/centrality/harmonic_centrality.html#harmonic) | ✓ checked, agrees |  |
| Centrality | Distance-based | [Radiality and integration](../measures/centrality/radiality.html) | [Radiality](../measures/centrality/radiality.html#cat_radiality) | · reported in docs | `radiality` |
| Centrality | Local and structural scores | [Community-based centrality](../measures/centrality/community_centrality.html) | [Communitycent](../measures/centrality/community_centrality.html#cat_communitycent) | · reported in docs | `communitycent` |
| Centrality | Local and structural scores | [Cross-clique centrality](../measures/centrality/cross_clique_centrality.html) | [Crossclique](../measures/centrality/cross_clique_centrality.html#cat_crossclique) | · reported in docs | `crossclique` |
| Centrality | Local and structural scores | [Diffusion centrality and diffusion degree](../measures/centrality/diffusion_centrality.html) | [Diffusion degree](../measures/centrality/diffusion_centrality.html#cat_degree_diffusion) | · reported in docs | `diffusion.degree` |
| Centrality | Local and structural scores | [Edge percolated component](../measures/centrality/epc.html) | [Epc](../measures/centrality/epc.html#cat_epc) | · reported in docs | `epc` |
| Centrality | Local and structural scores | [Entropy centrality](../measures/centrality/entropy_centrality.html) | [Entropy](../measures/centrality/entropy_centrality.html#cat_entropy) | · reported in docs | `entropy` |
| Centrality | Local and structural scores | [Leverage centrality](../measures/centrality/leverage_centrality.html) | [Leverage](../measures/centrality/leverage_centrality.html#cat_leverage) | · reported in docs | `leverage` |
| Centrality | Local and structural scores | [Lin centrality](../measures/centrality/lin_centrality.html) | [Lincent](../measures/centrality/lin_centrality.html#cat_lincent) | · reported in docs | `lincent` |
| Centrality | Local and structural scores | [Lobby index](../measures/centrality/lobby_index.html) | [Lobby](../measures/centrality/lobby_index.html#cat_lobby) | · reported in docs | `lobby` |
| Centrality | Local and structural scores | [MNC and DMNC](../measures/centrality/mnc_dmnc.html) | [Dmnc](../measures/centrality/mnc_dmnc.html#cat_dmnc) | · reported in docs | `dmnc` |
| Centrality | Local and structural scores | [MNC and DMNC](../measures/centrality/mnc_dmnc.html) | [Mnc](../measures/centrality/mnc_dmnc.html#cat_mnc) | · reported in docs | `mnc` |
| Centrality | Local and structural scores | [Semi-local centrality](../measures/centrality/semilocal_centrality.html) | [Semilocal](../measures/centrality/semilocal_centrality.html#cat_semilocal) | · reported in docs | `semilocal` |
| Centrality | Local and structural scores | [Topological coefficient](../measures/centrality/topological_coefficient.html) | [Topocoefficient](../measures/centrality/topological_coefficient.html#cat_topocoefficient) | · reported in docs | `topocoefficient` |
| Centrality | Resistance and information | [Information centrality (current-flow closeness)](../measures/centrality/information_centrality.html) | [Current flow closeness](../measures/centrality/information_centrality.html#cx_current_flow_closeness) | · reported in docs | `closeness.currentflow` |
| Centrality | Spectral and walk-based | [ClusterRank](../measures/centrality/clusterrank.html) | [Clusterrank](../measures/centrality/clusterrank.html#cat_clusterrank) | · reported in docs | `clusterrank` |
| Centrality | Spectral and walk-based | [Hubbell centrality](../measures/centrality/hubbell_centrality.html) | [Hubbell](../measures/centrality/hubbell_centrality.html#cat_hubbell) | · reported in docs | `hubbell` |
| Centrality | Spectral and walk-based | [Katz centrality](../measures/centrality/katz_centrality.html) | [Katz](../measures/centrality/katz_centrality.html#katz) | ✓ checked, agrees | `katzcent` |
| Centrality | Spectral and walk-based | [LeaderRank](../measures/centrality/leaderrank.html) | [Leaderrank](../measures/centrality/leaderrank.html#cat_leaderrank) | · reported in docs | `leaderrank` |
| Centrality | Spectral and walk-based | [Markov centrality](../measures/centrality/markov_centrality.html) | [Markovcent](../measures/centrality/markov_centrality.html#cat_markovcent) | · reported in docs | `markovcent` |
| Centrality | Spectral and walk-based | [SALSA](../measures/centrality/salsa.html) | [Salsa](../measures/centrality/salsa.html#cat_salsa) | · reported in docs | `salsa` |
| Matrices and spectra | Graph matrices | [Laplacian matrix](../measures/matrices-and-spectra/laplacian_matrix.html) | [Gm laplacian](../measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian) | · reported in docs | `laplacian` |
| Paths and distances | Distance summaries | [Barycenter](../measures/paths-and-distances/barycenter.html) | [Barycenter](../measures/paths-and-distances/barycenter.html#dm_barycenter) | · reported in docs | `barycenter` |
| Paths and distances | Distance summaries | [Closeness vitality](../measures/paths-and-distances/closeness_vitality.html) | [Closeness vitality](../measures/paths-and-distances/closeness_vitality.html#dm_closeness_vitality) | · reported in docs | `closeness.vitality` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F013](../findings.html#f013) | defect | communibet() cannot find an installed expm |
| [F077](../findings.html#f077) | convention | Flow closeness is larger by a factor near n - 1; closeness vitality is twice the standard value on undirected networks |
{% endraw %}
