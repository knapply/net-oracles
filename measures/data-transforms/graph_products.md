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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(H=(V_H,E_H)\)</td><td>second graph, with the same edge conventions as \(G\)</td></tr><tr><td>\((u,x)\)</td><td>node of a product, \(u\in V\), \(x\in V_H\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Graph products. Entries grouped here: Graph products.

*Definition partly written:* The sources list one collective entry of documented tools; the four products are defined, but which of them each tool computes is not recorded.

<div class="formula-block"><p class="formula-name"><strong>Cartesian product</strong> <span class="applies">applies to: any</span></p><div class="formula">\[(u,x)(v,y)\in E\iff (u=v\ \wedge\ xy\in E_H)\ \vee\ (uv\in E\ \wedge\ x=y)\]</div><p class="formula-where">One factor moves while the other stays.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Tensor (direct, categorical) product</strong> <span class="applies">applies to: any</span></p><div class="formula">\[(u,x)(v,y)\in E\iff uv\in E\ \wedge\ xy\in E_H\]</div><p class="formula-where">Both factors move at once.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Strong product</strong> <span class="applies">applies to: any</span></p><div class="formula">\[E_{\boxtimes}=E_{\square}\cup E_{\times}\]</div><p class="formula-where">The union of the Cartesian and the tensor product edge sets.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Lexicographic product (composition)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[(u,x)(v,y)\in E\iff uv\in E\ \vee\ (u=v\ \wedge\ xy\in E_H)\]</div><p class="formula-where">The first factor decides unless it stays; not commutative.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#op_graph_product">Graph products</a></td><td><code>op_graph_product</code></td><td>2</td><td>Collective entry for the graph products of documented tools: Cartesian, tensor, strong and lexicographic products have the formulas above; which products a tool offers is not recorded.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/rustworkx.html">rustworkx</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">A product with a null graph has no nodes.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The product of an edgeless factor is edgeless for the tensor product, and a union of copies of the other factor for the Cartesian product.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop in a factor adds edges between a node's copies and others, by the formulas; loop-free input gives a loop-free product except where the formula places loops (the tensor product of two looped nodes).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">For digraphs the pairs are ordered in each coordinate.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

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
