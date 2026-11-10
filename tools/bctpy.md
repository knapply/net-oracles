---
title: "bctpy"
layout: default
parent: Tools
---

{% raw %}

# bctpy

| Field | Value |
|---|---|
| Identifier | `bctpy` |
| Language | Python |
| Version tested | 0.6.1 |
| License | GPL-3.0-or-later |
| Homepage | <https://pypi.org/project/bctpy/> |
| Role | checked |
| Citation | [rubinov2010complex](../references.html#rubinov2010complex) |

## How it was run

Imported in CPython; functions called on NumPy adjacency matrices.

## Coverage

| State | Measures |
|---|---|
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 11 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 4 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (multi-edges and ties): BCT works on a connection matrix, so parallel edges collapse to one tie (one shortest path per pair of neighbours). [details](../measures/centrality/betweenness.html#why-betweenness-bctpy) |
| Cohesion and subgroups | Cores, trusses and cohesive blocks | [K-core decomposition](../measures/cohesion-and-subgroups/k_core.html) | [Coreness](../measures/cohesion-and-subgroups/k_core.html#coreness) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction, multi-edges and ties): kcoreness\_centrality\_bu() takes a binary undirected matrix: a directed fixture enters symmetrized, so a reciprocated pair is one tie, and parallel... [details](../measures/cohesion-and-subgroups/k_core.html#why-coreness-bctpy) |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Transitivity](../measures/descriptive-statistics/global_transitivity.html#transitivity) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Directed clustering](../measures/descriptive-statistics/local_clustering.html#nxo_directed_clustering) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Density and degree distribution | [Density](../measures/descriptive-statistics/density.html) | [Density](../measures/descriptive-statistics/density.html#density) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Mixing and assortativity | Assortativity | [Assortativity coefficient](../measures/mixing-and-assortativity/assortativity_coefficient.html) | [Assort](../measures/mixing-and-assortativity/assortativity_coefficient.html#assort) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction and multi-edges): BCT works on the binary matrix, so parallel edges collapse and degrees count distinct neighbours. [details](../measures/mixing-and-assortativity/assortativity_coefficient.html#why-assort-bctpy) |
| Paths and distances | Distance summaries | [Diameter](../measures/paths-and-distances/diameter.html) | [Diameter](../measures/paths-and-distances/diameter.html#diameter) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Distance summaries | [Eccentricity](../measures/paths-and-distances/eccentricity.html) | [Eccentricity](../measures/paths-and-distances/eccentricity.html#eccentricity) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Distance summaries | [Mean distance](../measures/paths-and-distances/mean_distance.html) | [Mean distance](../measures/paths-and-distances/mean_distance.html#mean_distance) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Distance summaries | [Radius](../measures/paths-and-distances/radius.html) | [Radius](../measures/paths-and-distances/radius.html#radius) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Distance summaries | [Wiener index](../measures/paths-and-distances/wiener_index.html) | [Index](../measures/paths-and-distances/wiener_index.html#dm_index) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Efficiency and reachability | [Local efficiency](../measures/paths-and-distances/local_efficiency.html) | [Local efficiency](../measures/paths-and-distances/local_efficiency.html#dm_local_efficiency) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (self-loops): This variant follows NetworkX in counting a self-loop as making a node its own neighbour. [details](../measures/paths-and-distances/local_efficiency.html#why-dm_local_efficiency-bctpy) |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
{% endraw %}
