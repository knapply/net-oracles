---
title: "LFR benchmark generator"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# LFR benchmark generator {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Growth and attachment models. Concept id: `lfr_benchmark`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(\tau_1,\tau_2\)</td><td>exponents of the power laws for degrees and community sizes</td></tr><tr><td>\(\mu\)</td><td>mixing parameter</td></tr></tbody></table></div>

## Definition {#concept-definition}

LFR benchmark generator. Entries grouped here: LFRGenerator.

*Definition partly written:* Only the main parameters of the benchmark are written; the construction of the degree and community-size sequences is not given here.

<div class="formula-block"><p class="formula-name"><strong>LFR benchmark (Lancichinetti, Fortunato and Radicchi 2008)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\text{each node has a fraction }1-\mu\text{ of its edges inside its community and }\mu\text{ outside; }P(k)\propto k^{-\tau_1},\ P(s)\propto s^{-\tau_2}\]</div><p class="formula-where">Degrees and community sizes follow power laws; \(\mu\) controls how well communities are separated. A generator returns a random sample, so a result is reproducible only for a fixed seed and random generator; tools use different generators.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_generator_lfr">LFRGenerator</a></td><td><code>cat_generator_lfr</code></td><td>1</td><td>The LFR benchmark with the parameters above.</td></tr></tbody></table></div>

## LFRGenerator {#cat_generator_lfr}

Measure id: `cat_generator_lfr`. Original family: Generators and rewiring.

**Definition.** LFRGenerator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_generator_lfr-networkit">details</a></td><td><code>LFRGenerator</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generator_lfr-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LFRGenerator.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
