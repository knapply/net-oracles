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

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs | `contcp` | published documentation |
| [cpnet](../../tools/cpnet.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `core_periphery_minres_vs_cpnet` | cpnet | any | agrees |  |  | abs 1e-09, rel 1e-09 | `smallest residual sum of squares sum (a_ij - c_i c_j)^2 over the coreness vectors of cpnet.MINRES, Rombach and Rossa (those installed)` |  |

**References:** [borgatti1999models](../../references.html#borgatti1999models), [boyd2010computing](../../references.html#boyd2010computing), [comrey1962minimum](../../references.html#comrey1962minimum), [nocedal2006numerical](../../references.html#nocedal2006numerical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [tool_cpnet](../../references.html#tool_cpnet)
{% endraw %}
