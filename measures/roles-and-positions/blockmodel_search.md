---
title: "Direct blockmodel search"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Direct blockmodel search {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Blockmodels. Concept id: `blockmodel_search`. 1 measure.

## Definition {#concept-definition}

Direct blockmodel search. Entries grouped here: Direct blockmodel search (structural, regular, generalised block types).

## Direct blockmodel search (structural, regular, generalised block types) {#blockmodel_search}

Measure id: `blockmodel_search`. Original family: Roles and positions.

**Definition.** Direct blockmodel search (structural, regular, generalised block types).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-blockmodel_search-ucinet) |  | published documentation |
| [blockmodeling](../../tools/blockmodeling.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-blockmodel_search-blockmodeling) | `optParC; optRandomParC` | documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-blockmodel_search-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-blockmodel_search-blockmodeling"></a>**[blockmodeling](../../tools/blockmodeling.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. blockmodeling 1.1.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package blockmodeling: exported functions and help titles); API names: optParC; optRandomParC.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [ziberna2007generalized](../../references.html#ziberna2007generalized)
{% endraw %}
