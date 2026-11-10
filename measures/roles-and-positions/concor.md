---
title: "CONCOR"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# CONCOR {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Blockmodels. Concept id: `concor`. 1 measure.

## Definition {#concept-definition}

CONCOR blocks: repeated splits of the nodes by iterated correlation of their correlation matrix, numbered from 1.

## References {#concept-references}

[breiger1975algorithm](../../references.html#breiger1975algorithm), [burt1976positions](../../references.html#burt1976positions), [lorrain1971structural](../../references.html#lorrain1971structural), [wasserman1994social](../../references.html#wasserman1994social)

## Concor {#concor}

Measure id: `concor`. Original family: Roles and positions.

**Definition.** CONCOR blocks: repeated splits of the nodes by iterated correlation of their correlation matrix, numbered from 1.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-concor-ucinet) | `CONCOR, hierarchical clustering, blockmodels, optimization; ccsplit` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-concor-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [breiger1975algorithm](../../references.html#breiger1975algorithm), [burt1976positions](../../references.html#burt1976positions), [lorrain1971structural](../../references.html#lorrain1971structural), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
