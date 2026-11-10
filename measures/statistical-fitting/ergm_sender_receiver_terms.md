---
title: "Sender, receiver and sociality terms"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Sender, receiver and sociality terms {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: ERGM terms. Concept id: `ergm_sender_receiver_terms`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr></tbody></table></div>

## Definition {#concept-definition}

Sender, receiver and sociality terms. Entries grouped here: Receiver; Sender; Sociality.

*Definition partly written:* The node-wise definitions are written; which node is the baseline is a tool convention not stated in the sources.

<div class="formula-block"><p class="formula-name"><strong>Sender, receiver and sociality (Morris et al. 2008)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\text{sender}_v=\sum_jy_{vj},\qquad \text{receiver}_v=\sum_iy_{iv},\qquad \text{sociality}_v=\sum_jy_{vj}\ (\text{undirected})\]</div><p class="formula-where">One statistic per node: its out-degree, in-degree or degree. One node serves as the baseline and is dropped, otherwise the statistics add up to the edge count.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_receiver">Receiver</a></td><td><code>cat_receiver</code></td><td>1</td><td>In-degree of each non-baseline node.</td></tr><tr><td><a href="#cat_sender">Sender</a></td><td><code>cat_sender</code></td><td>1</td><td>Out-degree of each non-baseline node.</td></tr><tr><td><a href="#cat_sociality">Sociality</a></td><td><code>cat_sociality</code></td><td>1</td><td>Degree of each non-baseline node in an undirected network.</td></tr></tbody></table></div>

## Receiver {#cat_receiver}

Measure id: `cat_receiver`. Original family: Graph theory and combinatorics.

**Definition.** Receiver.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_receiver-ergm">details</a></td><td><code>receiver</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_receiver-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: receiver.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Sender {#cat_sender}

Measure id: `cat_sender`. Original family: Graph theory and combinatorics.

**Definition.** Sender.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_sender-ergm">details</a></td><td><code>sender</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sender-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: sender.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Sociality {#cat_sociality}

Measure id: `cat_sociality`. Original family: Graph theory and combinatorics.

**Definition.** Sociality.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_sociality-ergm">details</a></td><td><code>sociality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sociality-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: sociality.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
