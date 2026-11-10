---
title: "Symmetrize"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Symmetrize {#concept-top}

Family: [Data transforms](index.html). Subfamily: Matrix and tie transformations. Concept id: `symmetrize`. 2 measures.

## Definition {#concept-definition}

Symmetrize. Entries grouped here: Full symmetrize method set and dichotomize by density; Symmetrise.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Full symmetrize method set and dichotomize by density](#symmetrize_methods) | `symmetrize_methods` | 3 |
| [Symmetrise](#cat_symmetrise) | `cat_symmetrise` | 1 |

## Full symmetrize method set and dichotomize by density {#symmetrize_methods}

Measure id: `symmetrize_methods`. Original family: Data transforms.

**Definition.** Full symmetrize method set and dichotomize by density.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-symmetrize_methods-sna) | `symmetrize` | API listing |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-symmetrize_methods-ergm) | `Symmetrize` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-symmetrize_methods-ucinet) | `Symmetrize` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-symmetrize_methods-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: symmetrize.
- <a id="why-symmetrize_methods-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: Symmetrize.
- <a id="why-symmetrize_methods-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [hunter2008ergm](../../references.html#hunter2008ergm)

## Symmetrise {#cat_symmetrise}

Measure id: `cat_symmetrise`. Original family: Graph theory and combinatorics.

**Definition.** Symmetrise.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [tnet](../../tools/tnet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_symmetrise-tnet) | `symmetrise_w` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_symmetrise-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: symmetrise\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)
{% endraw %}
