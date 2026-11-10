---
title: "Edge cover"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge cover {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Covers and dominating sets. Concept id: `edge_cover`. 2 measures.

## Definition {#concept-definition}

Edge cover. Entries grouped here: Edge cover; St edge cover.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#edge_cover">Edge cover</a></td><td><code>edge_cover</code></td><td>1</td></tr><tr><td><a href="#st_edge_cover">St edge cover</a></td><td><code>st_edge_cover</code></td><td>1</td></tr></tbody></table></div>

## Edge cover {#edge_cover}

Measure id: `edge_cover`. Original family: Graph theory and combinatorics.

**Definition.** Edge cover.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-edge_cover-networkx">details</a></td><td><code>is_cover; is_edge_cover; min_edge_cover</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-edge_cover-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_cover; is\_edge\_cover; min\_edge\_cover.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## St edge cover {#st_edge_cover}

Measure id: `st_edge_cover`. Original family: Graph theory and combinatorics.

**Definition.** St edge cover.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>st_edge_cover</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.min_edge_cover(G)) counting each edge once, -1 with an isolated node</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
