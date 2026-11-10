---
title: "Random spanning tree"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random spanning tree {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Spanning trees and branchings. Concept id: `random_spanning_tree`. 3 measures.

## Definition {#concept-definition}

A random spanning tree of a connected undirected network by Wilson's algorithm, as input edge positions.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Random spanning tree](#random_spanning_tree) | `random_spanning_tree` | 4 |
| [Random Maximum Spanning Forest](#cat_forest_maximum_random_spanning) | `cat_forest_maximum_random_spanning` | 1 |
| [Rst edge freq](#rst_edge_freq) | `rst_edge_freq` | 1 |

## References {#concept-references}

[wilson1996generating](../../references.html#wilson1996generating)

## Random spanning tree {#random_spanning_tree}

Measure id: `random_spanning_tree`. Original family: Traversal, trees and DAGs.

**Definition.** Random spanning tree.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `random_spanning_tree` | API listing |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `sample_spanning_tree` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `random_spanning_tree` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `random_spanning_tree` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost)

## Random Maximum Spanning Forest {#cat_forest_maximum_random_spanning}

Measure id: `cat_forest_maximum_random_spanning`. Original family: Traversal, trees and DAGs.

**Definition.** Random Maximum Spanning Forest.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `RandomMaximumSpanningForest` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Rst edge freq {#rst_edge_freq}

Measure id: `rst_edge_freq`. Original family: Traversal, trees and DAGs.

**Definition.** A random spanning tree of a connected undirected network by Wilson's algorithm, as input edge positions.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `rst_edge_freq_nx` | NetworkX | undirected | agrees |  |  | abs 0.06, rel 0 | `fraction of 2000 draws of nx.random_spanning_tree(G, weight = None, seed = k) containing each edge` |  |
| `rst_edge_freq_nx_weighted` | NetworkX | undirected | agrees |  |  | abs 0.06, rel 0 | `fraction of 2000 draws of nx.random_spanning_tree(G, weight = 'weight', seed = k) containing each edge` |  |

**References:** [wilson1996generating](../../references.html#wilson1996generating)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
