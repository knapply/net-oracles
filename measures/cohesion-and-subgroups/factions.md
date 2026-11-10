---
title: "Factions"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Factions {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `factions`. 2 measures.

## Definition {#concept-definition}

Factions: a partition into k groups that best fits the ideal pattern of ties inside groups only, by tabu search from random starts.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Factions](#cat_factions) | `cat_factions` | 1 |
| [Factions errors](#factions_errors) | `factions_errors` | 1 |

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [doreian2005generalized](../../references.html#doreian2005generalized), [glover1989tabu](../../references.html#glover1989tabu), [hanneman2005introduction](../../references.html#hanneman2005introduction)

## Factions {#cat_factions}

Measure id: `cat_factions`. Original family: Cohesion and subgroups.

**Definition.** Factions.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-cat_factions-ucinet) | `factions` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_factions-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Factions errors {#factions_errors}

Measure id: `factions_errors`. Original family: Cohesion and subgroups.

**Definition.** Factions: a partition into k groups that best fits the ideal pattern of ties inside groups only, by tabu search from random starts.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-factions_errors-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-factions_errors-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [borgatti1999models](../../references.html#borgatti1999models), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [doreian2005generalized](../../references.html#doreian2005generalized), [glover1989tabu](../../references.html#glover1989tabu), [hanneman2005introduction](../../references.html#hanneman2005introduction)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
