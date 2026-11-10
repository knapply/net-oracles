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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 4 |
| <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | 14 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `betweenness_w` |  |
| Centrality | Degree and strength | [Alpha-tuned degree and closeness](../measures/centrality/weighted_degree_alpha.html) | [Opsahl alpha-tuned degree and closeness](../measures/centrality/weighted_degree_alpha.html#opsahl_alpha) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> |  | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](../measures/centrality/weighted_degree_alpha.html#why-opsahl_alpha-tnet) |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `degree_tm; degree_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/centrality/degree.html#why-degree-tnet) |
| Centrality | Degree and strength | [Strength (weighted degree)](../measures/centrality/strength.html) | [Strength](../measures/centrality/strength.html#strength) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `closeness_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/centrality/closeness.html#why-closeness-tnet) |
| Data transforms | Matrix and tie transformations | [Dichotomize](../measures/data-transforms/dichotomize.html) | [Dichotomise](../measures/data-transforms/dichotomize.html#cat_dichotomise) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `dichotomise_tm; dichotomise_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/data-transforms/dichotomize.html#why-cat_dichotomise-tnet) |
| Data transforms | Matrix and tie transformations | [Symmetrize](../measures/data-transforms/symmetrize.html) | [Symmetrise](../measures/data-transforms/symmetrize.html#cat_symmetrise) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `symmetrise_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/data-transforms/symmetrize.html#why-cat_symmetrise-tnet) |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `clustering_local_tm; clustering_local_w; clustering_tm; clustering_w` |  |
| Generators and rewiring | Growth and attachment models | [Growth (tnet)](../measures/generators-and-rewiring/growth_tnet.html) | [Growth](../measures/generators-and-rewiring/growth_tnet.html#cat_growth) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `growth_l` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/generators-and-rewiring/growth_tnet.html#why-cat_growth-tnet) |
| Generators and rewiring | Rewiring and randomization | [Reinforcement](../measures/generators-and-rewiring/reinforcement.html) | [Reinforcement](../measures/generators-and-rewiring/reinforcement.html#cat_reinforcement) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `reinforcement_tm` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/generators-and-rewiring/reinforcement.html#why-cat_reinforcement-tnet) |
| Generators and rewiring | Rewiring and randomization | [Weighted reshuffling](../measures/generators-and-rewiring/weighted_reshuffling.html) | [Rg](../measures/generators-and-rewiring/weighted_reshuffling.html#cat_rg) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `rg_tm; rg_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/generators-and-rewiring/weighted_reshuffling.html#why-cat_rg-tnet) |
| Generators and rewiring | Rewiring and randomization | [Weighted reshuffling](../measures/generators-and-rewiring/weighted_reshuffling.html) | [Rg reshuffling](../measures/generators-and-rewiring/weighted_reshuffling.html#cat_reshuffling_rg) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `rg_reshuffling_l; rg_reshuffling_tm; rg_reshuffling_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/generators-and-rewiring/weighted_reshuffling.html#why-cat_reshuffling_rg-tnet) |
| Mixing and assortativity | Rich club | [Rich club](../measures/mixing-and-assortativity/rich_club.html) | [Weighted richclub](../measures/mixing-and-assortativity/rich_club.html#cat_richclub_weighted) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `weighted_richclub_tm; weighted_richclub_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/mixing-and-assortativity/rich_club.html#why-cat_richclub_weighted-tnet) |
| Mixing and assortativity | Rich club | [Rich club](../measures/mixing-and-assortativity/rich_club.html) | [Weighted richclub local](../measures/mixing-and-assortativity/rich_club.html#cat_local_richclub_weighted) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `weighted_richclub_local_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/mixing-and-assortativity/rich_club.html#why-cat_local_richclub_weighted-tnet) |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `distance_tm; distance_w` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/paths-and-distances/geodesic_distances.html#why-distances-tnet) |
| Two-mode and bipartite | Bipartite structure | [Two-mode clustering coefficients (six-cycle)](../measures/two-mode-and-bipartite/twomode_clustering.html) | [Two-mode clustering coefficients (six-cycle)](../measures/two-mode-and-bipartite/twomode_clustering.html#twomode_cc) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> |  | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](../measures/two-mode-and-bipartite/twomode_clustering.html#why-twomode_cc-tnet) |
| Two-mode and bipartite | Projection | [Bipartite projection](../measures/two-mode-and-bipartite/bipartite_projection.html) | [Project](../measures/two-mode-and-bipartite/bipartite_projection.html#project) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `projecting_tm` |  |
| Two-mode and bipartite | Projection | [Bipartite projection](../measures/two-mode-and-bipartite/bipartite_projection.html) | [Two-mode projection weights (covariance, correlation, Jaccard, Bonacich, cosine)](../measures/two-mode-and-bipartite/bipartite_projection.html#projection_weights) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> |  | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](../measures/two-mode-and-bipartite/bipartite_projection.html#why-projection_weights-tnet) |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F078](../findings.html#f078) | defect | Weighted distance and closeness with the alpha exponent differ from the definition |
{% endraw %}
