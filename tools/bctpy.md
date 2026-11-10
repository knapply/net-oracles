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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention |  |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Density](../measures/density.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Directed clustering](../measures/nxo_directed_clustering.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ✓ checked, agrees |  |
| Mixing and assortativity | [Assort](../measures/assort.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Diameter](../measures/diameter.html) | ✓ checked, agrees |  |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees |  |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ✓ checked, agrees |  |
| Paths and distances | [Index](../measures/dm_index.html) | ✓ checked, agrees |  |
| Paths and distances | [Local efficiency](../measures/dm_local_efficiency.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Mean distance](../measures/mean_distance.html) | ✓ checked, agrees |  |
| Paths and distances | [Radius](../measures/radius.html) | ✓ checked, agrees |  |
{% endraw %}
