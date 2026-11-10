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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Eigenvector](../measures/eigenvector.html) | ≠ checked, differs by convention |  |
| Centrality | [Hits](../measures/hits.html) | ≠ checked, differs by convention |  |
| Centrality | [Katz](../measures/katz.html) | ≠ checked, differs by convention |  |
| Centrality | [Pagerank](../measures/pagerank.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Directed clustering](../measures/nxo_directed_clustering.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Node reciprocity](../measures/nxo_node_reciprocity.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Square clustering](../measures/square_clustering.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Triangles](../measures/nxo_triangles.html) | ✓ checked, agrees |  |
| Graph theory and combinatorics | [Generalized degree](../measures/generalized_degree.html) | ✓ checked, agrees |  |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F086](../findings.html#f086) | defect | Katz loses beta at nodes without in-links |
{% endraw %}
