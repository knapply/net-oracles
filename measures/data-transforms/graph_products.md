---
title: "Graph products"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph products {#concept-top}

Family: [Data transforms](index.html). Subfamily: Graph operators. Concept id: `graph_products`. 1 measure.

## Definition {#concept-definition}

Graph products. Entries grouped here: Graph products.

*Definition not yet written.*

## Graph products {#op_graph_product}

Measure id: `op_graph_product`. Original family: Data transforms.

**Definition.** Graph products.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-op_graph_product-networkx">details</a></td><td><code>cartesian_product; corona_product; lexicographic_product; modular_product; rooted_product; strong_product; tensor_product</code></td><td>API listing</td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-op_graph_product-rustworkx">details</a></td><td><code>cartesian_product; digraph_cartesian_product; digraph_tensor_product; graph_cartesian_product; graph_tensor_product; tensor_product</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-op_graph_product-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: cartesian\_product; corona\_product; lexicographic\_product; modular\_product; rooted\_product; strong\_product; tensor\_product.
- <a id="why-op_graph_product-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: cartesian\_product; digraph\_cartesian\_product; digraph\_tensor\_product; graph\_cartesian\_product; graph\_tensor\_product; tensor\_product.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
