---
title: "tnet"
layout: default
parent: Tools
---

{% raw %}
# tnet

| Field | Value |
|---|---|
| Identifier | `tnet` |
| Language | R |
| Version tested | 3.0.16 |
| License | GPL-3.0-only |
| Homepage | <https://cran.r-project.org/package=tnet> |
| Role | checked |
| Citation | [opsahl2010node](../references.html#opsahl2010node) |

## How it was run

Called from R on edge lists.

Capabilities listed by introspection of R package tnet: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 4 |
| reported in docs (·) | 14 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ✓ checked, agrees | `betweenness_w` |
| Centrality | [Closeness](../measures/closeness.html) | · reported in docs | `closeness_w` |
| Centrality | [Opsahl alpha-tuned degree and closeness](../measures/opsahl_alpha.html) | · reported in docs |  |
| Centrality | [Strength](../measures/strength.html) | ✓ checked, agrees |  |
| Data transforms | [Dichotomise](../measures/cat_dichotomise.html) | · reported in docs | `dichotomise_tm; dichotomise_w` |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ✓ checked, agrees | `clustering_local_tm; clustering_local_w; clustering_tm; clustering_w` |
| Descriptive statistics | [Degree](../measures/degree.html) | · reported in docs | `degree_tm; degree_w` |
| Graph theory and combinatorics | [Growth](../measures/cat_growth.html) | · reported in docs | `growth_l` |
| Graph theory and combinatorics | [Rg](../measures/cat_rg.html) | · reported in docs | `rg_tm; rg_w` |
| Graph theory and combinatorics | [Rg reshuffling](../measures/cat_reshuffling_rg.html) | · reported in docs | `rg_reshuffling_l; rg_reshuffling_tm; rg_reshuffling_w` |
| Graph theory and combinatorics | [Symmetrise](../measures/cat_symmetrise.html) | · reported in docs | `symmetrise_w` |
| Graph theory and combinatorics | [Weighted richclub](../measures/cat_richclub_weighted.html) | · reported in docs | `weighted_richclub_tm; weighted_richclub_w` |
| Graph theory and combinatorics | [Weighted richclub local](../measures/cat_local_richclub_weighted.html) | · reported in docs | `weighted_richclub_local_w` |
| Layout | [Reinforcement](../measures/cat_reinforcement.html) | · reported in docs | `reinforcement_tm` |
| Paths and distances | [Distances](../measures/distances.html) | · reported in docs | `distance_tm; distance_w` |
| Two-mode and bipartite | [Project](../measures/project.html) | ✓ checked, agrees | `projecting_tm` |
| Two-mode and bipartite | [Two-mode clustering coefficients (six-cycle)](../measures/twomode_cc.html) | · reported in docs |  |
| Two-mode and bipartite | [Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine)](../measures/projection_weights.html) | · reported in docs |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F078](../findings.html#f078) | defect | Weighted distance and closeness with the alpha exponent differ from the definition |
{% endraw %}
