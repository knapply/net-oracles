---
title: "Conditional uniform graph tests and null models"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Conditional uniform graph tests and null models {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `cug_null_models`. 1 measure.

## Definition {#concept-definition}

Conditional uniform graph tests and null models. Entries grouped here: Conditional uniform graph tests and null models.

*Definition not yet written.*

## Conditional uniform graph tests and null models {#cug_null_models}

Measure id: `cug_null_models`. Original family: Inference (QAP, null models).

**Definition.** Conditional uniform graph tests and null models.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-cug_null_models-sna">details</a></td><td><code>cug.test; cugtest</code></td><td>documentation</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cug_null_models-ucinet">details</a></td><td><code>Conditional uniform graph tests, TERGM/ERGM are not UCINET</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cug_null_models-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: cug.test; cugtest.
- <a id="why-cug_null_models-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
