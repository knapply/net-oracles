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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 8 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 9 |
| <a class="st st-t st-defect" href="../method.html#state-checked-defect"><span class="g" aria-hidden="true">✗</span>checked, defect</a> | 1 |
| <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | 6 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults and normalization): With fewer than three nodes the normalizing constant is zero. [details](../measures/centrality/betweenness.html#why-betweenness-gephi) |
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `Degree` |  |
| Centrality | Degree and strength | [Strength (weighted degree)](../measures/centrality/strength.html) | [Strength](../measures/centrality/strength.html#strength) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `WeightedDegree` |  |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults, direction and normalization): Gephi gives 0 to a node that reaches no other node. [details](../measures/centrality/closeness.html#why-closeness-gephi) |
| Centrality | Distance-based | [Harmonic centrality](../measures/centrality/harmonic_centrality.html) | [Harmonic](../measures/centrality/harmonic_centrality.html#harmonic) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (normalization): Gephi divides the sum of 1/d by the number of nodes the node reaches (0 if none), the reference by n - 1 (the standard normalization). [details](../measures/centrality/harmonic_centrality.html#why-harmonic-gephi) |
| Centrality | Spectral and walk-based | [Eigenvector centrality](../measures/centrality/eigenvector_centrality.html) | [Eigenvector](../measures/centrality/eigenvector_centrality.html#eigenvector) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | `EigenvectorCentrality` | Differs by convention (defaults, direction, multi-edges, normalization, self-loops, ties and weights): Gephi runs a fixed number of power-iteration steps (setNumRuns, here 10^6) without a convergence test, and its result is not the converged... [details](../measures/centrality/eigenvector_centrality.html#why-eigenvector-gephi) |
| Centrality | Spectral and walk-based | [HITS hubs and authorities](../measures/centrality/hits.html) | [Hits](../measures/centrality/hits.html#hits) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | `Hits` | Differs by convention (defaults, direction, normalization and self-loops): Gephi scales the hub and authority vectors to unit Euclidean length. [details](../measures/centrality/hits.html#why-hits-gephi) |
| Centrality | Spectral and walk-based | [PageRank](../measures/centrality/pagerank.html) | [Pagerank](../measures/centrality/pagerank.html#pagerank) | <a class="st st-t st-defect" href="../method.html#state-checked-defect"><span class="g" aria-hidden="true">✗</span>checked, defect</a> | `PageRank` | Defect: PageRank loses probability mass at self-loops; scores do not sum to 1 (finding F017). [details](../measures/centrality/pagerank.html#why-pagerank-gephi) |
| Communities | Modularity-based detection | [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](../measures/communities/modularity_maximization.html) | [Louvain quality](../measures/communities/modularity_maximization.html#louvain_quality) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (multi-edges and self-loops): With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept). [details](../measures/communities/modularity_maximization.html#why-louvain_quality-gephi) |
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `Modularity` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/communities/modularity.html#why-modularity-gephi) |
| Components and connectivity | Connected components | [Connected components](../measures/components-and-connectivity/connected_components.html) | [Components](../measures/components-and-connectivity/connected_components.html#components) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `ConnectedComponents` |  |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Average clustering](../measures/descriptive-statistics/local_clustering.html#average_clustering) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (multi-edges and self-loops): Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the... [details](../measures/descriptive-statistics/local_clustering.html#why-average_clustering-gephi) |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | `ClusteringCoefficient` | Differs by convention (multi-edges and self-loops): Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the... [details](../measures/descriptive-statistics/local_clustering.html#why-clustering-gephi) |
| Descriptive statistics | Clustering and transitivity | [Triangle count](../measures/descriptive-statistics/triangle_count.html) | [Triangles](../measures/descriptive-statistics/triangle_count.html#nxo_triangles) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (multi-edges and self-loops): Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the... [details](../measures/descriptive-statistics/triangle_count.html#why-nxo_triangles-gephi) |
| Descriptive statistics | Density and degree distribution | [Density](../measures/descriptive-statistics/density.html) | [Density](../measures/descriptive-statistics/density.html#density) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `GraphDensity` |  |
| Input and output | Graph description formats | [Graph description and exchange formats](../measures/input-and-output/graph_markup_io.html) | [GEXF read and write](../measures/input-and-output/graph_markup_io.html#io_gexf) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> |  | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](../measures/input-and-output/graph_markup_io.html#why-io_gexf-gephi) |
| Paths and distances | Distance summaries | [Diameter](../measures/paths-and-distances/diameter.html) | [Diameter](../measures/paths-and-distances/diameter.html#diameter) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Distance summaries | [Eccentricity](../measures/paths-and-distances/eccentricity.html) | [Eccentricity](../measures/paths-and-distances/eccentricity.html#eccentricity) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Distance summaries | [Mean distance](../measures/paths-and-distances/mean_distance.html) | [Mean distance](../measures/paths-and-distances/mean_distance.html#mean_distance) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Distance summaries | [Radius](../measures/paths-and-distances/radius.html) | [Radius](../measures/paths-and-distances/radius.html#radius) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `GraphDistance` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/paths-and-distances/geodesic_distances.html#why-distances-gephi) |
| Statistical fitting | Model fitting | [Statistical inference clustering](../measures/statistical-fitting/statistical_inference_clustering.html) | [Statistical Inference Clustering](../measures/statistical-fitting/statistical_inference_clustering.html#cat_clustering_inference_statistical) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `StatisticalInferenceClustering` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/statistical-fitting/statistical_inference_clustering.html#why-cat_clustering_inference_statistical-gephi) |
| Temporal and events | Temporal descriptives | [Dynamic clustering coefficient](../measures/temporal-and-events/dynamic_clustering.html) | [Dynamic Clustering Coefficient](../measures/temporal-and-events/dynamic_clustering.html#cat_clustering_coefficient_dynamic) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `DynamicClusteringCoefficient` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/dynamic_clustering.html#why-cat_clustering_coefficient_dynamic-gephi) |
| Temporal and events | Temporal descriptives | [Temporal degree](../measures/temporal-and-events/temporal_degree.html) | [Dynamic Degree](../measures/temporal-and-events/temporal_degree.html#cat_degree_dynamic) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `DynamicDegree` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/temporal_degree.html#why-cat_degree_dynamic-gephi) |

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
