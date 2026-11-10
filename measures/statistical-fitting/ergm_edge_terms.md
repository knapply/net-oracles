---
title: "Edge count and density terms"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge count and density terms {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: ERGM terms. Concept id: `ergm_edge_terms`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr></tbody></table></div>

## Definition {#concept-definition}

Edge count and density terms. Entries grouped here: Edges; Isolatededges; Meandeg.

*Definition partly written:* Only the edge count is written; mean degree and isolated-edges terms are named in the sources but their definitions were not checked against a primary paper.

<div class="formula-block"><p class="formula-name"><strong>Edge count (Frank and Strauss 1986; Morris et al. 2008)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\text{edges}(y)=\sum_{i&lt;j}y_{ij}\ \text{(undirected)},\qquad \sum_{i\ne j}y_{ij}\ \text{(directed)}\]</div><p class="formula-where">Its coefficient is the baseline log-odds of a tie.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_edge">Edges</a></td><td><code>cat_edge</code></td><td>1</td><td>The edge count above.</td></tr></tbody></table></div>

## Edges {#cat_edge}

Measure id: `cat_edge`. Original family: Graph theory and combinatorics.

**Definition.** Edges.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_edge-ergm">details</a></td><td><code>edges</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_edge-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: edges.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Isolatededges {#cat_isolatededges}

Measure id: `cat_isolatededges`. Original family: Graph theory and combinatorics.

**Definition.** Isolatededges.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_isolatededges-ergm">details</a></td><td><code>isolatededges</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_isolatededges-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: isolatededges.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Meandeg {#cat_meandeg}

Measure id: `cat_meandeg`. Original family: Graph theory and combinatorics.

**Definition.** Meandeg.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_meandeg-ergm">details</a></td><td><code>meandeg</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_meandeg-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: meandeg.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
