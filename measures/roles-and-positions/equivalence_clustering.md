---
title: "Equivalence clustering"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Equivalence clustering {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Equivalence and clustering. Concept id: `equivalence_clustering`. 2 measures.

## Definition {#concept-definition}

Equivalence clustering. Entries grouped here: Equiv clust; Hiclus.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Equiv clust](#cat_clust_equiv) | `cat_clust_equiv` | 1 |
| [Hiclus](#cat_hiclus) | `cat_hiclus` | 1 |

## Equiv clust {#cat_clust_equiv}

Measure id: `cat_clust_equiv`. Original family: Graph theory and combinatorics.

**Definition.** Equiv clust.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clust_equiv-sna) | `equiv.clust` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clust_equiv-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: equiv.clust.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)

## Hiclus {#cat_hiclus}

Measure id: `cat_hiclus`. Original family: Graph theory and combinatorics.

**Definition.** Hiclus.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-cat_hiclus-ucinet) | `hiclus` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_hiclus-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
