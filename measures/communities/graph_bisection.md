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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `greedy_node_swap_bipartition` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Kernighan lin {#cnx_kernighan_lin}

Measure id: `cnx_kernighan_lin`. Original family: Communities.

**Definition.** Kernighan lin.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `kernighan_lin_bisection` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_kernighan_lin` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.community.kernighan_lin_bisection(G_sorted, (first half, rest), max_iter = 10, weight = 'weight' if weighted)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Spectral Partitioner {#cat_partitioner_spectral}

Measure id: `cat_partitioner_spectral`. Original family: Communities.

**Definition.** Spectral Partitioner.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `SpectralPartitioner` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
