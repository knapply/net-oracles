---
title: "Congruence, rotation, IPF and state transitions"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Congruence, rotation, IPF and state transitions {#concept-top}

Family: [Data transforms](index.html). Subfamily: Matrix and tie transformations. Concept id: `matrix_utils`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(x,y\)</td><td>two vectors (for example columns of two factor matrices)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Congruence, rotation, IPF and state transitions. Entries grouped here: Tucker congruence, factor rotation, iterative proportional fitting, state transitions.

*Definition partly written:* One entry of a documented tool bundles four utilities; only the congruence coefficient is defined here, from its standard form without a cited source. Factor rotation, iterative proportional fitting (see ipf) and state transitions are not specified in the sources.

<div class="formula-block"><p class="formula-name"><strong>Tucker congruence coefficient</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\varphi(x,y)=\frac{x^{\top}y}{\sqrt{(x^{\top}x)(y^{\top}y)}}\]</div><p class="formula-where">Cosine of the angle between \(x\) and \(y\) without centring; not defined when either vector is zero.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#matrix_utils">Tucker congruence, factor rotation, iterative proportional fitting, state transitions</a></td><td><code>matrix_utils</code></td><td>1</td><td>Collective entry (congruence, factor rotation, iterative proportional fitting, state transitions); only the congruence coefficient is defined above.</td></tr></tbody></table></div>

## Tucker congruence, factor rotation, iterative proportional fitting, state transitions {#matrix_utils}

Measure id: `matrix_utils`. Original family: Data transforms.

**Definition.** Tucker congruence, factor rotation, iterative proportional fitting, state transitions.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-matrix_utils-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-matrix_utils-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
