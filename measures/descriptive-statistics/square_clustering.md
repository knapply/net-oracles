---
title: "Square clustering"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Square clustering {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `square_clustering`. 2 measures.

## Definition {#concept-definition}

Square clustering of every node: the share of possible squares through it that exist.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Square clustering](#square_clustering) | `square_clustering` | 2 |
| [Local Square Clustering Coefficient](#cat_clustering_coefficient_local_square) | `cat_clustering_coefficient_local_square` | 1 |

## References {#concept-references}

[hagberg2008exploring](../../references.html#hagberg2008exploring), [lind2005cycles](../../references.html#lind2005cycles), [zhang2008clustering](../../references.html#zhang2008clustering), [zlatic2012networks](../../references.html#zlatic2012networks)

## Square clustering {#square_clustering}

Measure id: `square_clustering`. Original family: Descriptive statistics.

**Definition.** Square clustering of every node: the share of possible squares through it that exist.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `square_clustering` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `square_clustering` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.square_clustering(G)` |  |
| `square_clustering` | GraphBLAS algorithms | any | differs | multi\_edges, (no value) directed | direction, multi\_edges, weights | abs 1e-12, rel 1e-12 | `nx.square_clustering(G simple, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. graphblas-algorithms' square\_clustering fails on a DiGraph (KeyError 'degrees+'). |

**References:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [lind2005cycles](../../references.html#lind2005cycles), [zhang2008clustering](../../references.html#zhang2008clustering), [zlatic2012networks](../../references.html#zlatic2012networks)

**Tools cited:** [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Local Square Clustering Coefficient {#cat_clustering_coefficient_local_square}

Measure id: `cat_clustering_coefficient_local_square`. Original family: Generators and rewiring.

**Definition.** Local Square Clustering Coefficient.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `LocalSquareClusteringCoefficient` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
