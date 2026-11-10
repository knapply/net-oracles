---
title: "Power-law cluster graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Power-law cluster graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Growth and attachment models. Concept id: `powerlaw_cluster`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(m\)</td><td>edges per new node</td></tr><tr><td>\(p\)</td><td>probability of a triad-formation step</td></tr></tbody></table></div>

## Definition {#concept-definition}

Power-law cluster graph. Entries grouped here: Powerlaw cluster graph.

*Definition partly written:* The model is written from the paper; the tool function was recorded by name only.

<div class="formula-block"><p class="formula-name"><strong>Power-law cluster model (Holme and Kim 2002)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\text{first edge by preferential attachment; each further edge: with probability }p\text{ to a random neighbour of the last target, otherwise preferential attachment}\]</div><p class="formula-where">Adding triad formation to linear attachment raises clustering while keeping the power-law degree tail. A generator returns a random sample, so a result is reproducible only for a fixed seed and random generator; tools use different generators.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_cluster_powerlaw">Powerlaw cluster graph</a></td><td><code>cat_cluster_powerlaw</code></td><td>1</td><td>The Holme-Kim model above.</td></tr></tbody></table></div>

## Powerlaw cluster graph {#cat_cluster_powerlaw}

Measure id: `cat_cluster_powerlaw`. Original family: Generators and rewiring.

**Definition.** Powerlaw cluster graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_cluster_powerlaw-networkx">details</a></td><td><code>powerlaw_cluster_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_cluster_powerlaw-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: powerlaw\_cluster\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
