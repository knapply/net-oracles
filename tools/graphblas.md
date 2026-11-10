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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 8 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 6 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Centrality | Spectral and walk-based | [Eigenvector centrality](../measures/centrality/eigenvector_centrality.html) | [Eigenvector](../measures/centrality/eigenvector_centrality.html#eigenvector) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction, multi-edges, ties and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](../measures/centrality/eigenvector_centrality.html#why-eigenvector-graphblas) |
| Centrality | Spectral and walk-based | [HITS hubs and authorities](../measures/centrality/hits.html) | [Hits](../measures/centrality/hits.html#hits) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults, direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](../measures/centrality/hits.html#why-hits-graphblas) |
| Centrality | Spectral and walk-based | [Katz centrality](../measures/centrality/katz_centrality.html) | [Katz](../measures/centrality/katz_centrality.html#katz) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction and multi-edges): graphblas-algorithms' katz\_centrality drops the beta term for nodes that have no in-links (they get no entry in the sparse result, read as 0), so... [details](../measures/centrality/katz_centrality.html#why-katz-graphblas) |
| Centrality | Spectral and walk-based | [PageRank](../measures/centrality/pagerank.html) | [Pagerank](../measures/centrality/pagerank.html#pagerank) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults, direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](../measures/centrality/pagerank.html#why-pagerank-graphblas) |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Transitivity](../measures/descriptive-statistics/global_transitivity.html#transitivity) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Directed clustering](../measures/descriptive-statistics/local_clustering.html#nxo_directed_clustering) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](../measures/descriptive-statistics/local_clustering.html#why-nxo_directed_clustering-graphblas) |
| Descriptive statistics | Clustering and transitivity | [Square clustering](../measures/descriptive-statistics/square_clustering.html) | [Square clustering](../measures/descriptive-statistics/square_clustering.html#square_clustering) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](../measures/descriptive-statistics/square_clustering.html#why-square_clustering-graphblas) |
| Descriptive statistics | Clustering and transitivity | [Triangle count](../measures/descriptive-statistics/triangle_count.html) | [Triangles](../measures/descriptive-statistics/triangle_count.html#nxo_triangles) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Reciprocity, dyad and triad census | [Reciprocity](../measures/descriptive-statistics/reciprocity.html) | [Node reciprocity](../measures/descriptive-statistics/reciprocity.html#nxo_node_reciprocity) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Descriptive statistics | Reciprocity, dyad and triad census | [Reciprocity](../measures/descriptive-statistics/reciprocity.html) | [Reciprocity](../measures/descriptive-statistics/reciprocity.html#reciprocity) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Graph theory and combinatorics | Degree sequences and predicates | [Generalized degree](../measures/graph-theory-and-combinatorics/generalized_degree.html) | [Generalized degree](../measures/graph-theory-and-combinatorics/generalized_degree.html#generalized_degree) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F086](../findings.html#f086) | defect | Katz loses beta at nodes without in-links |
{% endraw %}
