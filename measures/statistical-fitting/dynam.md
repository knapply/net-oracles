---
title: "Actor-oriented event models (DyNAM)"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Actor-oriented event models (DyNAM) {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `dynam`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(\lambda_i\)</td><td>rate at which actor \(i\) acts</td></tr><tr><td>\(s_{ij}\)</td><td>statistic vector of the choice of \(j\) by \(i\)</td></tr><tr><td>\(\alpha,\beta\)</td><td>rate and choice coefficients</td></tr></tbody></table></div>

## Definition {#concept-definition}

Actor-oriented event models (DyNAM). Entries grouped here: Actor-oriented event models (DyNAM).

*Definition partly written:* The rate and choice structure is written from the DyNAM paper; the tool's options (effects, estimation) were not recorded.

<div class="formula-block"><p class="formula-name"><strong>Dynamic network actor model (Stadtfeld and Block 2017)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\lambda_i=\exp(\alpha^{\top}r_i),\qquad \Pr(j\mid i)=\frac{\exp(\beta^{\top}s_{ij})}{\sum_{h\ne i}\exp(\beta^{\top}s_{ih})}\]</div><p class="formula-where">Each event is a pair of an actor who acts (chosen by the rate) and the target they choose (multinomial logit); likelihood is the product over observed events.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#dynam">Actor-oriented event models (DyNAM)</a></td><td><code>dynam</code></td><td>1</td><td>Rate and choice sub-models of the formula; estimation by maximum likelihood.</td></tr></tbody></table></div>

## Actor-oriented event models (DyNAM) {#dynam}

Measure id: `dynam`. Original family: Statistical fitting.

**Definition.** Actor-oriented event models (DyNAM).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/goldfish.html">goldfish</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: goldfish is documented-only in this survey; listed in its documentation. <a href="#why-dynam-goldfish">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dynam-goldfish"></a>**[goldfish](../../tools/goldfish.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. goldfish (1.6.12) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: R package goldfish: exported functions and help titles.

**Tools cited:** [tool_goldfish](../../references.html#tool_goldfish)
{% endraw %}
