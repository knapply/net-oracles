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

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | ✓ checked, agrees | `betweenness_w` |
| Centrality | Degree and strength | [Alpha-tuned degree and closeness](../measures/centrality/weighted_degree_alpha.html) | [Opsahl alpha-tuned degree and closeness](../measures/centrality/weighted_degree_alpha.html#opsahl_alpha) | · reported in docs |  |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | · reported in docs | `degree_tm; degree_w` |
| Centrality | Degree and strength | [Strength (weighted degree)](../measures/centrality/strength.html) | [Strength](../measures/centrality/strength.html#strength) | ✓ checked, agrees |  |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | · reported in docs | `closeness_w` |
| Data transforms | Matrix and tie transformations | [Dichotomize](../measures/data-transforms/dichotomize.html) | [Dichotomise](../measures/data-transforms/dichotomize.html#cat_dichotomise) | · reported in docs | `dichotomise_tm; dichotomise_w` |
| Data transforms | Matrix and tie transformations | [Symmetrize](../measures/data-transforms/symmetrize.html) | [Symmetrise](../measures/data-transforms/symmetrize.html#cat_symmetrise) | · reported in docs | `symmetrise_w` |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | ✓ checked, agrees | `clustering_local_tm; clustering_local_w; clustering_tm; clustering_w` |
| Generators and rewiring | Growth and attachment models | [Growth (tnet)](../measures/generators-and-rewiring/growth_tnet.html) | [Growth](../measures/generators-and-rewiring/growth_tnet.html#cat_growth) | · reported in docs | `growth_l` |
| Generators and rewiring | Rewiring and randomization | [Reinforcement](../measures/generators-and-rewiring/reinforcement.html) | [Reinforcement](../measures/generators-and-rewiring/reinforcement.html#cat_reinforcement) | · reported in docs | `reinforcement_tm` |
| Generators and rewiring | Rewiring and randomization | [Weighted reshuffling](../measures/generators-and-rewiring/weighted_reshuffling.html) | [Rg](../measures/generators-and-rewiring/weighted_reshuffling.html#cat_rg) | · reported in docs | `rg_tm; rg_w` |
| Generators and rewiring | Rewiring and randomization | [Weighted reshuffling](../measures/generators-and-rewiring/weighted_reshuffling.html) | [Rg reshuffling](../measures/generators-and-rewiring/weighted_reshuffling.html#cat_reshuffling_rg) | · reported in docs | `rg_reshuffling_l; rg_reshuffling_tm; rg_reshuffling_w` |
| Mixing and assortativity | Rich club | [Rich club](../measures/mixing-and-assortativity/rich_club.html) | [Weighted richclub](../measures/mixing-and-assortativity/rich_club.html#cat_richclub_weighted) | · reported in docs | `weighted_richclub_tm; weighted_richclub_w` |
| Mixing and assortativity | Rich club | [Rich club](../measures/mixing-and-assortativity/rich_club.html) | [Weighted richclub local](../measures/mixing-and-assortativity/rich_club.html#cat_local_richclub_weighted) | · reported in docs | `weighted_richclub_local_w` |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | · reported in docs | `distance_tm; distance_w` |
| Two-mode and bipartite | Bipartite structure | [Two-mode clustering coefficients (six-cycle)](../measures/two-mode-and-bipartite/twomode_clustering.html) | [Two-mode clustering coefficients (six-cycle)](../measures/two-mode-and-bipartite/twomode_clustering.html#twomode_cc) | · reported in docs |  |
| Two-mode and bipartite | Projection | [Bipartite projection](../measures/two-mode-and-bipartite/bipartite_projection.html) | [Project](../measures/two-mode-and-bipartite/bipartite_projection.html#project) | ✓ checked, agrees | `projecting_tm` |
| Two-mode and bipartite | Projection | [Bipartite projection](../measures/two-mode-and-bipartite/bipartite_projection.html) | [Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine)](../measures/two-mode-and-bipartite/bipartite_projection.html#projection_weights) | · reported in docs |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F078](../findings.html#f078) | defect | Weighted distance and closeness with the alpha exponent differ from the definition |
{% endraw %}
