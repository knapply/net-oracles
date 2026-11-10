---
title: "Krackhardt graph-theoretic dimensions"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Krackhardt graph-theoretic dimensions {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Efficiency, compactness and hierarchy. Concept id: `krackhardt_dimensions`. 1 measure.

## Definition {#concept-definition}

Krackhardt graph-theoretic dimensions. Entries grouped here: Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness).

## Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness) {#krackhardt_dimensions}

Measure id: `krackhardt_dimensions`. Original family: Descriptive statistics.

**Definition.** Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-krackhardt_dimensions-sna) | `connectedness; lubness` | documentation |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-krackhardt_dimensions-ucinet) | `Fragmentation, Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-krackhardt_dimensions-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: connectedness; lubness.
- <a id="why-krackhardt_dimensions-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
