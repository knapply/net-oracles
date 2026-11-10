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

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | ≠ checked, differs by convention |  |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | ✓ checked, agrees | `Degree` |
| Centrality | Degree and strength | [Strength (weighted degree)](../measures/centrality/strength.html) | [Strength](../measures/centrality/strength.html#strength) | ✓ checked, agrees | `WeightedDegree` |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | ≠ checked, differs by convention |  |
| Centrality | Distance-based | [Harmonic centrality](../measures/centrality/harmonic_centrality.html) | [Harmonic](../measures/centrality/harmonic_centrality.html#harmonic) | ≠ checked, differs by convention |  |
| Centrality | Spectral and walk-based | [Eigenvector centrality](../measures/centrality/eigenvector_centrality.html) | [Eigenvector](../measures/centrality/eigenvector_centrality.html#eigenvector) | ≠ checked, differs by convention | `EigenvectorCentrality` |
| Centrality | Spectral and walk-based | [HITS hubs and authorities](../measures/centrality/hits.html) | [Hits](../measures/centrality/hits.html#hits) | ≠ checked, differs by convention | `Hits` |
| Centrality | Spectral and walk-based | [PageRank](../measures/centrality/pagerank.html) | [Pagerank](../measures/centrality/pagerank.html#pagerank) | ✗ checked, defect | `PageRank` |
| Communities | Modularity-based detection | [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](../measures/communities/modularity_maximization.html) | [Louvain quality](../measures/communities/modularity_maximization.html#louvain_quality) | ≠ checked, differs by convention |  |
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | · reported in docs | `Modularity` |
| Components and connectivity | Connected components | [Connected components](../measures/components-and-connectivity/connected_components.html) | [Components](../measures/components-and-connectivity/connected_components.html#components) | ✓ checked, agrees | `ConnectedComponents` |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | ≠ checked, differs by convention |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | ≠ checked, differs by convention | `ClusteringCoefficient` |
| Descriptive statistics | Clustering and transitivity | [Triangle count](../measures/descriptive-statistics/triangle_count.html) | [Triangles](../measures/descriptive-statistics/triangle_count.html#nxo_triangles) | ≠ checked, differs by convention |  |
| Descriptive statistics | Density and degree distribution | [Density](../measures/descriptive-statistics/density.html) | [Density](../measures/descriptive-statistics/density.html#density) | ✓ checked, agrees | `GraphDensity` |
| Input and output | Graph description formats | [Graph description and exchange formats](../measures/input-and-output/graph_markup_io.html) | [GEXF read and write](../measures/input-and-output/graph_markup_io.html#io_gexf) | · reported in docs |  |
| Paths and distances | Distance summaries | [Diameter](../measures/paths-and-distances/diameter.html) | [Diameter](../measures/paths-and-distances/diameter.html#diameter) | ✓ checked, agrees |  |
| Paths and distances | Distance summaries | [Eccentricity](../measures/paths-and-distances/eccentricity.html) | [Eccentricity](../measures/paths-and-distances/eccentricity.html#eccentricity) | ✓ checked, agrees |  |
| Paths and distances | Distance summaries | [Mean distance](../measures/paths-and-distances/mean_distance.html) | [Mean distance](../measures/paths-and-distances/mean_distance.html#mean_distance) | ✓ checked, agrees |  |
| Paths and distances | Distance summaries | [Radius](../measures/paths-and-distances/radius.html) | [Radius](../measures/paths-and-distances/radius.html#radius) | ✓ checked, agrees |  |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | · reported in docs | `GraphDistance` |
| Statistical fitting | Model fitting | [Statistical inference clustering](../measures/statistical-fitting/statistical_inference_clustering.html) | [Statistical Inference Clustering](../measures/statistical-fitting/statistical_inference_clustering.html#cat_clustering_inference_statistical) | · reported in docs | `StatisticalInferenceClustering` |
| Temporal and events | Temporal descriptives | [Dynamic clustering coefficient](../measures/temporal-and-events/dynamic_clustering.html) | [Dynamic Clustering Coefficient](../measures/temporal-and-events/dynamic_clustering.html#cat_clustering_coefficient_dynamic) | · reported in docs | `DynamicClusteringCoefficient` |
| Temporal and events | Temporal descriptives | [Temporal degree](../measures/temporal-and-events/temporal_degree.html) | [Dynamic Degree](../measures/temporal-and-events/temporal_degree.html#cat_degree_dynamic) | · reported in docs | `DynamicDegree` |

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
