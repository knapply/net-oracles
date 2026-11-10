---
title: "AIC"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# AIC {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `model_aic`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(k\)</td><td>number of free parameters</td></tr><tr><td>\(\hat\ell\)</td><td>maximized log-likelihood</td></tr></tbody></table></div>

## Definition {#concept-definition}

AIC. Entries grouped here: Aic.

*Definition partly written:* The standard formula is given without a citation because the primary paper is not in the bibliography and could not be verified.

<div class="formula-block"><p class="formula-name"><strong>Akaike information criterion</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{AIC}=2k-2\hat\ell\]</div><p class="formula-where">Lower is better; defined for models with a likelihood.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_aic">Aic</a></td><td><code>cat_aic</code></td><td>1</td><td>AIC of a fitted model; the UCINET function is documented by name only.</td></tr></tbody></table></div>

## Aic {#cat_aic}

Measure id: `cat_aic`. Original family: Graph theory and combinatorics.

**Definition.** Aic.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_aic-ucinet">details</a></td><td><code>aic</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_aic-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
