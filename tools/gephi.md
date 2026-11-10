---
title: "Gephi toolkit"
layout: default
parent: Tools
---

{% raw %}
# Gephi toolkit

| Field | Value |
|---|---|
| Identifier | `gephi` |
| Language | Java |
| Version tested | 0.11.3 |
| License | GPL-3.0 / CDDL-1.0 (dual) |
| Homepage | <https://gephi.org> |
| Role | checked |
| Citation | [bastian2009gephi](../references.html#bastian2009gephi) |

## How it was run

Statistics classes in the published toolkit jar driven through the public Java API.

Capabilities listed by documentation of Gephi toolkit 0.11.3 javadoc (published class list of org.gephi.statistics.plugin).

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 8 |
| checked, differs by convention (≠) | 9 |
| checked, defect (✗) | 1 |
| reported in docs (·) | 6 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention |  |
| Centrality | [Closeness](../measures/closeness.html) | ≠ checked, differs by convention |  |
| Centrality | [Eigenvector](../measures/eigenvector.html) | ≠ checked, differs by convention | `EigenvectorCentrality` |
| Centrality | [Harmonic](../measures/harmonic.html) | ≠ checked, differs by convention |  |
| Centrality | [Hits](../measures/hits.html) | ≠ checked, differs by convention | `Hits` |
| Centrality | [Pagerank](../measures/pagerank.html) | ✗ checked, defect | `PageRank` |
| Centrality | [Strength](../measures/strength.html) | ✓ checked, agrees | `WeightedDegree` |
| Communities | [Louvain quality](../measures/louvain_quality.html) | ≠ checked, differs by convention |  |
| Communities | [Modularity](../measures/modularity.html) | · reported in docs | `Modularity` |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ≠ checked, differs by convention | `ClusteringCoefficient` |
| Descriptive statistics | [Components](../measures/components.html) | ✓ checked, agrees | `ConnectedComponents` |
| Descriptive statistics | [Degree](../measures/degree.html) | ✓ checked, agrees | `Degree` |
| Descriptive statistics | [Density](../measures/density.html) | ✓ checked, agrees | `GraphDensity` |
| Descriptive statistics | [Triangles](../measures/nxo_triangles.html) | ≠ checked, differs by convention |  |
| Generators and rewiring | [Dynamic Clustering Coefficient](../measures/cat_clustering_coefficient_dynamic.html) | · reported in docs | `DynamicClusteringCoefficient` |
| Generators and rewiring | [Statistical Inference Clustering](../measures/cat_clustering_inference_statistical.html) | · reported in docs | `StatisticalInferenceClustering` |
| Input and output | [GEXF read and write](../measures/io_gexf.html) | · reported in docs |  |
| Paths and distances | [Diameter](../measures/diameter.html) | ✓ checked, agrees |  |
| Paths and distances | [Distances](../measures/distances.html) | · reported in docs | `GraphDistance` |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ✓ checked, agrees |  |
| Paths and distances | [Mean distance](../measures/mean_distance.html) | ✓ checked, agrees |  |
| Paths and distances | [Radius](../measures/radius.html) | ✓ checked, agrees |  |
| Temporal and events | [Dynamic Degree](../measures/cat_degree_dynamic.html) | · reported in docs | `DynamicDegree` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F014](../findings.html#f014) | defect | Eigenvector centrality is not converged |
| [F015](../findings.html#f015) | defect | Louvain with setRandom(false) is not reproducible |
| [F016](../findings.html#f016) | defect | Louvain sometimes does not return |
| [F017](../findings.html#f017) | defect | PageRank loses probability mass at self-loops |
| [F018](../findings.html#f018) | convention | Closeness is reached/sum of distances; 0 for a node reaching nobody |
| [F019](../findings.html#f019) | convention | HITS uses unit Euclidean scaling and ignores self-loops |
| [F020](../findings.html#f020) | convention | Degree counts a self-loop twice |
| [F021](../findings.html#f021) | convention | Average clustering leaves out nodes of degree below 2 |
| [F022](../findings.html#f022) | convention | Louvain resolution acts as the reciprocal of gamma |
{% endraw %}
