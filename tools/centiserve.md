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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Closeness](../measures/closeness.html) | · reported in docs | `closeness.freeman` |
| Centrality | [Closeness latora](../measures/cat_closeness_latora.html) | · reported in docs | `closeness.latora` |
| Centrality | [Closeness residual](../measures/cat_closeness_residual.html) | · reported in docs | `closeness.residual` |
| Centrality | [Communicability betweenness](../measures/cx_communicability_betweenness.html) | ✓ checked, agrees | `communibet` |
| Centrality | [Communitycent](../measures/cat_communitycent.html) | · reported in docs | `communitycent` |
| Centrality | [Current flow closeness](../measures/cx_current_flow_closeness.html) | · reported in docs | `closeness.currentflow` |
| Centrality | [Decay](../measures/cat_decay.html) | · reported in docs | `decay` |
| Centrality | [Diffusion degree](../measures/cat_degree_diffusion.html) | · reported in docs | `diffusion.degree` |
| Centrality | [Harmonic](../measures/harmonic.html) | ✓ checked, agrees |  |
| Centrality | [Hubbell](../measures/cat_hubbell.html) | · reported in docs | `hubbell` |
| Centrality | [Katz](../measures/katz.html) | ✓ checked, agrees | `katzcent` |
| Centrality | [Leverage](../measures/cat_leverage.html) | · reported in docs | `leverage` |
| Centrality | [Lincent](../measures/cat_lincent.html) | · reported in docs | `lincent` |
| Centrality | [Lobby](../measures/cat_lobby.html) | · reported in docs | `lobby` |
| Centrality | [Markovcent](../measures/cat_markovcent.html) | · reported in docs | `markovcent` |
| Centrality | [Radiality](../measures/cat_radiality.html) | · reported in docs | `radiality` |
| Centrality | [Salsa](../measures/cat_salsa.html) | · reported in docs | `salsa` |
| Cohesion and subgroups | [Crossclique](../measures/cat_crossclique.html) | · reported in docs | `crossclique` |
| Graph theory and combinatorics | [Averagedis](../measures/cat_averagedis.html) | · reported in docs | `averagedis` |
| Graph theory and combinatorics | [Bottleneck](../measures/cat_bottleneck.html) | · reported in docs | `bottleneck` |
| Graph theory and combinatorics | [Centroid](../measures/cat_centroid.html) | · reported in docs | `centroid` |
| Graph theory and combinatorics | [Clusterrank](../measures/cat_clusterrank.html) | · reported in docs | `clusterrank` |
| Graph theory and combinatorics | [Dmnc](../measures/cat_dmnc.html) | · reported in docs | `dmnc` |
| Graph theory and combinatorics | [Entropy](../measures/cat_entropy.html) | · reported in docs | `entropy` |
| Graph theory and combinatorics | [Epc](../measures/cat_epc.html) | · reported in docs | `epc` |
| Graph theory and combinatorics | [Leaderrank](../measures/cat_leaderrank.html) | · reported in docs | `leaderrank` |
| Graph theory and combinatorics | [Mnc](../measures/cat_mnc.html) | · reported in docs | `mnc` |
| Graph theory and combinatorics | [Pairwisedis](../measures/cat_pairwisedis.html) | · reported in docs | `pairwisedis` |
| Graph theory and combinatorics | [Semilocal](../measures/cat_semilocal.html) | · reported in docs | `semilocal` |
| Graph theory and combinatorics | [Topocoefficient](../measures/cat_topocoefficient.html) | · reported in docs | `topocoefficient` |
| Matrices and spectra | [Gm laplacian](../measures/gm_laplacian.html) | · reported in docs | `laplacian` |
| Paths and distances | [Barycenter](../measures/dm_barycenter.html) | · reported in docs | `barycenter` |
| Paths and distances | [Closeness vitality](../measures/dm_closeness_vitality.html) | · reported in docs | `closeness.vitality` |
| Paths and distances | [Geokpath](../measures/cat_geokpath.html) | · reported in docs | `geokpath` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F013](../findings.html#f013) | defect | communibet() cannot find an installed expm |
| [F077](../findings.html#f077) | convention | Flow closeness is larger by a factor near n - 1; closeness vitality is twice the standard value on undirected networks |
{% endraw %}
