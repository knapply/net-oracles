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

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Dichotomise](#cat_dichotomise) | `cat_dichotomise` | 1 |
| [Dichotomize](#cat_dichotomize) | `cat_dichotomize` | 1 |

## Dichotomise {#cat_dichotomise}

Measure id: `cat_dichotomise`. Original family: Data transforms.

**Definition.** Dichotomise.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [tnet](../../tools/tnet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_dichotomise-tnet) | `dichotomise_tm; dichotomise_w` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dichotomise-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: dichotomise\_tm; dichotomise\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)

## Dichotomize {#cat_dichotomize}

Measure id: `cat_dichotomize`. Original family: Data transforms.

**Definition.** Dichotomize.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-cat_dichotomize-ucinet) | `Dichotomize` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dichotomize-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
