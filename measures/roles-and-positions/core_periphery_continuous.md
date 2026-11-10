---
title: "Core-periphery (continuous)"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Core-periphery (continuous) {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Core-periphery. Concept id: `core_periphery_continuous`. 1 measure.

## Definition {#concept-definition}

Continuous core-periphery fit: a coreness score per node by MINRES or by correlation with the pattern c\_i c\_j.

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [boyd2010computing](../../references.html#boyd2010computing), [comrey1962minimum](../../references.html#comrey1962minimum), [nocedal2006numerical](../../references.html#nocedal2006numerical)

## Core periphery continuous {#core_periphery_continuous}

Measure id: `core_periphery_continuous`. Original family: Roles and positions.

**Definition.** Continuous core-periphery fit: a coreness score per node by MINRES or by correlation with the pattern c\_i c\_j.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-core_periphery_continuous-ucinet) | `contcp` | published documentation |
| [cpnet](../../tools/cpnet.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_periphery_continuous-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `core_periphery_minres_vs_cpnet` | cpnet | any | agrees |  |  | abs 1e-09, rel 1e-09 | `smallest residual sum of squares sum (a_ij - c_i c_j)^2 over the coreness vectors of cpnet.MINRES, Rombach and Rossa (those installed)` |  |

**References:** [borgatti1999models](../../references.html#borgatti1999models), [boyd2010computing](../../references.html#boyd2010computing), [comrey1962minimum](../../references.html#comrey1962minimum), [nocedal2006numerical](../../references.html#nocedal2006numerical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [tool_cpnet](../../references.html#tool_cpnet)
{% endraw %}
