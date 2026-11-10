---
title: "Densest subgraph"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Densest subgraph {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `densest_subgraph`. 5 measures.

## Definition {#concept-definition}

Densest subgraph of a simple undirected network by Greedy++ peeling, as the best density and its nodes.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Densest](#ap_densest) | `ap_densest` | 1 |
| [Goldberg Maximum Density Subgraph Algorithm](#cat_density_goldberg_maximum_subgraph) | `cat_density_goldberg_maximum_subgraph` | 1 |
| [Goldberg Maximum Density Subgraph Algorithm Base](#cat_base_density_goldberg_maximum_subgraph) | `cat_base_density_goldberg_maximum_subgraph` | 1 |
| [Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight](#cat_density_edge_goldberg_maximum_per_subgraph_weight) | `cat_density_edge_goldberg_maximum_per_subgraph_weight` | 1 |
| [Goldberg Maximum Density Subgraph Algorithm Node Weights](#cat_density_goldberg_maximum_subgraph_weights) | `cat_density_goldberg_maximum_subgraph_weights` | 1 |

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Densest {#ap_densest}

Measure id: `ap_densest`. Original family: Graph theory and combinatorics.

**Definition.** Densest subgraph of a simple undirected network by Greedy++ peeling, as the best density and its nodes.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `densest_subgraph` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_densest` | NetworkX | any | agrees |  |  | abs 0, rel 1e-15 | `nx.approximation.densest_subgraph(G_sorted, 2, method = 'greedy++'): (density, size)` |  |

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Goldberg Maximum Density Subgraph Algorithm {#cat_density_goldberg_maximum_subgraph}

Measure id: `cat_density_goldberg_maximum_subgraph`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithm` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Goldberg Maximum Density Subgraph Algorithm Base {#cat_base_density_goldberg_maximum_subgraph}

Measure id: `cat_base_density_goldberg_maximum_subgraph`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm Base.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithmBase` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight {#cat_density_edge_goldberg_maximum_per_subgraph_weight}

Measure id: `cat_density_edge_goldberg_maximum_per_subgraph_weight`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithmNodeWeightPerEdgeWeight` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Goldberg Maximum Density Subgraph Algorithm Node Weights {#cat_density_goldberg_maximum_subgraph_weights}

Measure id: `cat_density_goldberg_maximum_subgraph_weights`. Original family: Inference (QAP, null models).

**Definition.** Goldberg Maximum Density Subgraph Algorithm Node Weights.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithmNodeWeights` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
