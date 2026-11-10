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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-random_spanning_tree-networkx) | `random_spanning_tree` | API listing |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-random_spanning_tree-igraph) | `sample_spanning_tree` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-random_spanning_tree-graphtool) | `random_spanning_tree` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-random_spanning_tree-boost) | `random_spanning_tree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-random_spanning_tree-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: random\_spanning\_tree.
- <a id="why-random_spanning_tree-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: sample\_spanning\_tree.
- <a id="why-random_spanning_tree-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: random\_spanning\_tree.
- <a id="why-random_spanning_tree-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: random\_spanning\_tree.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost)

## Random Maximum Spanning Forest {#cat_forest_maximum_random_spanning}

Measure id: `cat_forest_maximum_random_spanning`. Original family: Traversal, trees and DAGs.

**Definition.** Random Maximum Spanning Forest.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_forest_maximum_random_spanning-networkit) | `RandomMaximumSpanningForest` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_forest_maximum_random_spanning-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: RandomMaximumSpanningForest.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Rst edge freq {#rst_edge_freq}

Measure id: `rst_edge_freq`. Original family: Traversal, trees and DAGs.

**Definition.** A random spanning tree of a connected undirected network by Wilson's algorithm, as input edge positions.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `rst_edge_freq_nx` | NetworkX | undirected | agrees |  |  | abs 0.06, rel 0 | `fraction of 2000 draws of nx.random_spanning_tree(G, weight = None, seed = k) containing each edge` |  |
| `rst_edge_freq_nx_weighted` | NetworkX | undirected | agrees |  |  | abs 0.06, rel 0 | `fraction of 2000 draws of nx.random_spanning_tree(G, weight = 'weight', seed = k) containing each edge` |  |

**References:** [wilson1996generating](../../references.html#wilson1996generating)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
