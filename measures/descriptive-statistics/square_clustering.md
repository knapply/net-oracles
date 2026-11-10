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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `square_clustering` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](#why-square_clustering-graphblas) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-square_clustering-graphblas"></a>**[GraphBLAS algorithms](../../tools/graphblas.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> GraphBLAS algorithms graphblas-algorithms 2023.10.0 (python-graphblas 2025.2.0, SuiteSparse:GraphBLAS 9.4.5.0) was run and its value differs from the reference value by convention (direction, multi-edges and weights) on inputs tagged multi\_edges. graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 1 comparisons differ and 18 agree.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clustering_coefficient_local_square-networkit) | `LocalSquareClusteringCoefficient` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clustering_coefficient_local_square-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LocalSquareClusteringCoefficient.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
