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

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_generate_knn">Generate knn</a></td><td><code>cat_generate_knn</code></td><td>1</td></tr><tr><td><a href="#cat_nearest_neighbor">Nearest Neighbor Graph</a></td><td><code>cat_nearest_neighbor</code></td><td>1</td></tr></tbody></table></div>

## Generate knn {#cat_generate_knn}

Measure id: `cat_generate_knn`. Original family: Descriptive statistics.

**Definition.** Generate knn.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_generate_knn-graphtool">details</a></td><td><code>generate_knn</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generate_knn-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: generate\_knn.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Nearest Neighbor Graph {#cat_nearest_neighbor}

Measure id: `cat_nearest_neighbor`. Original family: Generators and rewiring.

**Definition.** Nearest Neighbor Graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_nearest_neighbor-pyigraph">details</a></td><td><code>Nearest_Neighbor_Graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_nearest_neighbor-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Nearest\_Neighbor\_Graph.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
