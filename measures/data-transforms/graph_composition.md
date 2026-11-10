---
title: "Graph composition"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph composition {#concept-top}

Family: [Data transforms](index.html). Subfamily: Graph operators. Concept id: `graph_composition`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(H=(V_H,E_H)\)</td><td>second graph, with the same edge conventions as \(G\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Graph composition. Entries grouped here: Op compose.

*Definition partly written:* Tools use the word 'compose' for at least two different operations (relational composition of edge sets, and the lexicographic product also called composition); the sources do not say which operation each documented entry performs, and a third reading (union with attribute override) is not defined in the sources checked. The relational form is given without a cited source.

<div class="formula-block"><p class="formula-name"><strong>Composition (lexicographic product) G[H] (Harary 1969)</strong> <span class="applies">applies to: simple</span></p><div class="formula">\[V(G[H])=V\times V_H,\qquad (u,x)(v,y)\in E\iff uv\in E\ \text{or}\ (u=v\ \text{and}\ xy\in E_H)\]</div><p class="formula-where">Replace every node of \(G\) by a copy of \(H\); all edges between the copies of adjacent nodes of \(G\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Relational composition of edge sets</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[E(G\circ H)=\{(u,w):\ \exists v,\ (u,v)\in E,\ (v,w)\in E_H\}\]</div><p class="formula-where">Path of length 2 whose first edge is in \(G\) and second in \(H\), on a common node set; the order of the operands matters.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#op_compose">Op compose</a></td><td><code>op_compose</code></td><td>3</td><td>Either of the two operations above, depending on the tool; the entries of documented-only tools are not specified further in the sources.</td></tr></tbody></table></div>

## Op compose {#op_compose}

Measure id: `op_compose`. Original family: Data transforms.

**Definition.** Op compose.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-op_compose-networkx">details</a></td><td><code>compose; compose_all</code></td><td>API listing</td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-op_compose-igraph">details</a></td><td><code>compose</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-op_compose-pyigraph">details</a></td><td><code>compose</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-op_compose-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: compose; compose\_all.
- <a id="why-op_compose-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: compose.
- <a id="why-op_compose-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: compose.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
