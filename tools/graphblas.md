---
title: "GraphBLAS algorithms"
layout: default
parent: Tools
---

{% raw %}

# GraphBLAS algorithms

| Field | Value |
|---|---|
| Identifier | `graphblas` |
| Language | Python / C |
| Version tested | graphblas-algorithms 2023.10.0 (python-graphblas 2025.2.0, SuiteSparse:GraphBLAS 9.4.5.0) |
| License | Apache-2.0 |
| Homepage | <https://github.com/python-graphblas/graphblas-algorithms> |
| Role | checked |
| Citation | [davis2019algorithm](../references.html#davis2019algorithm) |

## How it was run

Imported in CPython (graphblas-algorithms over python-graphblas and SuiteSparse:GraphBLAS) as a NetworkX backend.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 8 |
| checked, differs by convention (≠) | 6 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Spectral and walk-based | [Eigenvector centrality](../measures/centrality/eigenvector_centrality.html) | [Eigenvector](../measures/centrality/eigenvector_centrality.html#eigenvector) | ≠ checked, differs by convention |  |
| Centrality | Spectral and walk-based | [HITS hubs and authorities](../measures/centrality/hits.html) | [Hits](../measures/centrality/hits.html#hits) | ≠ checked, differs by convention |  |
| Centrality | Spectral and walk-based | [Katz centrality](../measures/centrality/katz_centrality.html) | [Katz](../measures/centrality/katz_centrality.html#katz) | ≠ checked, differs by convention |  |
| Centrality | Spectral and walk-based | [PageRank](../measures/centrality/pagerank.html) | [Pagerank](../measures/centrality/pagerank.html#pagerank) | ≠ checked, differs by convention |  |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Transitivity](../measures/descriptive-statistics/global_transitivity.html#transitivity) | ✓ checked, agrees |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | ✓ checked, agrees |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | ✓ checked, agrees |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Directed clustering](../measures/descriptive-statistics/local_clustering.html#nxo_directed_clustering) | ≠ checked, differs by convention |  |
| Descriptive statistics | Clustering and transitivity | [Square clustering](../measures/descriptive-statistics/square_clustering.html) | [Square clustering](../measures/descriptive-statistics/square_clustering.html#square_clustering) | ≠ checked, differs by convention |  |
| Descriptive statistics | Clustering and transitivity | [Triangle count](../measures/descriptive-statistics/triangle_count.html) | [Triangles](../measures/descriptive-statistics/triangle_count.html#nxo_triangles) | ✓ checked, agrees |  |
| Descriptive statistics | Reciprocity, dyad and triad census | [Reciprocity](../measures/descriptive-statistics/reciprocity.html) | [Node reciprocity](../measures/descriptive-statistics/reciprocity.html#nxo_node_reciprocity) | ✓ checked, agrees |  |
| Descriptive statistics | Reciprocity, dyad and triad census | [Reciprocity](../measures/descriptive-statistics/reciprocity.html) | [Reciprocity](../measures/descriptive-statistics/reciprocity.html#reciprocity) | ✓ checked, agrees |  |
| Graph theory and combinatorics | Degree sequences and predicates | [Generalized degree](../measures/graph-theory-and-combinatorics/generalized_degree.html) | [Generalized degree](../measures/graph-theory-and-combinatorics/generalized_degree.html#generalized_degree) | ✓ checked, agrees |  |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | ✓ checked, agrees |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F086](../findings.html#f086) | defect | Katz loses beta at nodes without in-links |
{% endraw %}
