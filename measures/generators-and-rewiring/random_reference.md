---
title: "Random reference graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random reference graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Rewiring and randomization. Concept id: `random_reference`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(E\)</td><td>edge set</td></tr><tr><td>\(\deg_E(v)\)</td><td>degree of node \(v\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Random reference graph. Entries grouped here: Random reference.

*Definition partly written:* Only the degree-preserving rewiring is written (Maslov and Sneppen 2002, as used by Sporns and Zwi 2004); the number of rewiring rounds and the lattice-reference variant are not written.

<div class="formula-block"><p class="formula-name"><strong>Random reference by degree-preserving rewiring (Maslov and Sneppen 2002; Sporns and Zwi 2004)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\text{repeat the double edge swap }\{(a,b),(c,d)\}\to\{(a,d),(c,b)\}\ \text{ about }\text{niter}\cdot|E|\ \text{times}\]</div><p class="formula-where">The graph is randomized while all degrees stay fixed. A generator returns a random sample, so a result is reproducible only for a fixed seed and random generator; tools use different generators.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_random_reference">Random reference</a></td><td><code>cat_random_reference</code></td><td>1</td><td>Rewiring above, in rounds proportional to the number of edges; the round count is a parameter.</td></tr></tbody></table></div>

## Random reference {#cat_random_reference}

Measure id: `cat_random_reference`. Original family: Graph theory and combinatorics.

**Definition.** Random reference.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_random_reference-networkx">details</a></td><td><code>random_reference</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_random_reference-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: random\_reference.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
