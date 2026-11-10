---
title: "Dichotomize"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Dichotomize {#concept-top}

Family: [Data transforms](index.html). Subfamily: Matrix and tie transformations. Concept id: `dichotomize`. 2 measures.

## Definition {#concept-definition}

Dichotomize. Entries grouped here: Dichotomise; Dichotomize.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_dichotomise">Dichotomise</a></td><td><code>cat_dichotomise</code></td><td>1</td></tr><tr><td><a href="#cat_dichotomize">Dichotomize</a></td><td><code>cat_dichotomize</code></td><td>1</td></tr></tbody></table></div>

## Dichotomise {#cat_dichotomise}

Measure id: `cat_dichotomise`. Original family: Data transforms.

**Definition.** Dichotomise.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tnet.html">tnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dichotomise-tnet">details</a></td><td><code>dichotomise_tm; dichotomise_w</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dichotomise-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: dichotomise\_tm; dichotomise\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)

## Dichotomize {#cat_dichotomize}

Measure id: `cat_dichotomize`. Original family: Data transforms.

**Definition.** Dichotomize.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_dichotomize-ucinet">details</a></td><td><code>Dichotomize</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dichotomize-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
