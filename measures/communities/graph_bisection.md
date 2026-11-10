---
title: "Graph bisection"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph bisection {#concept-top}

Family: [Communities](index.html). Subfamily: Graph bisection and partitioning. Concept id: `graph_bisection`. 3 measures.

## Definition {#concept-definition}

Graph bisection. Entries grouped here: Greedy node swap bipartition (community); Kernighan lin; Spectral Partitioner.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Greedy node swap bipartition (community)](#cat_bipartition_greedy_swap-community) | `cat_bipartition_greedy_swap@community` | 1 |
| [Kernighan lin](#cnx_kernighan_lin) | `cnx_kernighan_lin` | 1 |
| [Spectral Partitioner](#cat_partitioner_spectral) | `cat_partitioner_spectral` | 1 |

## Greedy node swap bipartition (community) {#cat_bipartition_greedy_swap-community}

Measure id: `cat_bipartition_greedy_swap@community`. Original family: Generators and rewiring.

**Definition.** Greedy node swap bipartition (community).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_bipartition_greedy_swap-community-networkx) | `greedy_node_swap_bipartition` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartition_greedy_swap-community-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: greedy\_node\_swap\_bipartition.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Kernighan lin {#cnx_kernighan_lin}

Measure id: `cnx_kernighan_lin`. Original family: Communities.

**Definition.** Kernighan lin.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `kernighan_lin_bisection` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_kernighan_lin` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.community.kernighan_lin_bisection(G_sorted, (first half, rest), max_iter = 10, weight = 'weight' if weighted)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Spectral Partitioner {#cat_partitioner_spectral}

Measure id: `cat_partitioner_spectral`. Original family: Communities.

**Definition.** Spectral Partitioner.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_partitioner_spectral-networkit) | `SpectralPartitioner` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_partitioner_spectral-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SpectralPartitioner.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
