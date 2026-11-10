---
title: "Radiality and integration"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Radiality and integration {#concept-top}

Family: [Centrality](index.html). Subfamily: Distance-based. Concept id: `radiality`. 2 measures.

## Definition {#concept-definition}

Radiality and integration. Entries grouped here: Radiality; Valente-Foreman integration and radiality.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Radiality](#cat_radiality) | `cat_radiality` | 1 |
| [Valente-Foreman integration and radiality](#valente_foreman) | `valente_foreman` | 1 |

## Radiality {#cat_radiality}

Measure id: `cat_radiality`. Original family: Centrality.

**Definition.** Radiality.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_radiality-centiserve) | `radiality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_radiality-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: radiality.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Valente-Foreman integration and radiality {#valente_foreman}

Measure id: `valente_foreman`. Original family: Centrality.

**Definition.** Valente-Foreman integration and radiality.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-valente_foreman-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-valente_foreman-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
