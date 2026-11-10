---
title: "K-nearest-neighbor graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-nearest-neighbor graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Small-world, lattice and geometric models. Concept id: `knn_graph`. 2 measures.

## Definition {#concept-definition}

K-nearest-neighbor graph. Entries grouped here: Generate knn; Nearest Neighbor Graph.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Generate knn](#cat_generate_knn) | `cat_generate_knn` | 1 |
| [Nearest Neighbor Graph](#cat_nearest_neighbor) | `cat_nearest_neighbor` | 1 |

## Generate knn {#cat_generate_knn}

Measure id: `cat_generate_knn`. Original family: Descriptive statistics.

**Definition.** Generate knn.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_generate_knn-graphtool) | `generate_knn` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generate_knn-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: generate\_knn.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Nearest Neighbor Graph {#cat_nearest_neighbor}

Measure id: `cat_nearest_neighbor`. Original family: Generators and rewiring.

**Definition.** Nearest Neighbor Graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_nearest_neighbor-pyigraph) | `Nearest_Neighbor_Graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_nearest_neighbor-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Nearest\_Neighbor\_Graph.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
