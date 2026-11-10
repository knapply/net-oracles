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
| checked, agrees (✓) | 11 |
| checked, differs by convention (≠) | 4 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | ≠ checked, differs by convention |  |
| Cohesion and subgroups | Cores, trusses and cohesive blocks | [K-core decomposition](../measures/cohesion-and-subgroups/k_core.html) | [Coreness](../measures/cohesion-and-subgroups/k_core.html#coreness) | ≠ checked, differs by convention |  |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Transitivity](../measures/descriptive-statistics/global_transitivity.html#transitivity) | ✓ checked, agrees |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | ✓ checked, agrees |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | ✓ checked, agrees |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Directed clustering](../measures/descriptive-statistics/local_clustering.html#nxo_directed_clustering) | ✓ checked, agrees |  |
| Descriptive statistics | Density and degree distribution | [Density](../measures/descriptive-statistics/density.html) | [Density](../measures/descriptive-statistics/density.html#density) | ✓ checked, agrees |  |
| Mixing and assortativity | Assortativity | [Assortativity coefficient](../measures/mixing-and-assortativity/assortativity_coefficient.html) | [Assort](../measures/mixing-and-assortativity/assortativity_coefficient.html#assort) | ≠ checked, differs by convention |  |
| Paths and distances | Distance summaries | [Diameter](../measures/paths-and-distances/diameter.html) | [Diameter](../measures/paths-and-distances/diameter.html#diameter) | ✓ checked, agrees |  |
| Paths and distances | Distance summaries | [Eccentricity](../measures/paths-and-distances/eccentricity.html) | [Eccentricity](../measures/paths-and-distances/eccentricity.html#eccentricity) | ✓ checked, agrees |  |
| Paths and distances | Distance summaries | [Mean distance](../measures/paths-and-distances/mean_distance.html) | [Mean distance](../measures/paths-and-distances/mean_distance.html#mean_distance) | ✓ checked, agrees |  |
| Paths and distances | Distance summaries | [Radius](../measures/paths-and-distances/radius.html) | [Radius](../measures/paths-and-distances/radius.html#radius) | ✓ checked, agrees |  |
| Paths and distances | Distance summaries | [Wiener index](../measures/paths-and-distances/wiener_index.html) | [Index](../measures/paths-and-distances/wiener_index.html#dm_index) | ✓ checked, agrees |  |
| Paths and distances | Efficiency and reachability | [Local efficiency](../measures/paths-and-distances/local_efficiency.html) | [Local efficiency](../measures/paths-and-distances/local_efficiency.html#dm_local_efficiency) | ≠ checked, differs by convention |  |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | ✓ checked, agrees |  |
{% endraw %}
