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

*Definition not yet written.*

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [boyd2010computing](../../references.html#boyd2010computing), [comrey1962minimum](../../references.html#comrey1962minimum), [nocedal2006numerical](../../references.html#nocedal2006numerical)

## Core periphery continuous {#core_periphery_continuous}

Measure id: `core_periphery_continuous`. Original family: Roles and positions.

**Definition.** Continuous core-periphery fit: a coreness score per node by MINRES or by correlation with the pattern c\_i c\_j.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-core_periphery_continuous-ucinet">details</a></td><td><code>contcp</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/cpnet.html">cpnet</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_periphery_continuous-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>core_periphery_minres_vs_cpnet</code></td><td>cpnet</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>smallest residual sum of squares sum (a_ij - c_i c_j)^2 over the coreness vectors of cpnet.MINRES, Rombach and Rossa (those installed)</code></td><td></td></tr></tbody></table></div>

**References:** [borgatti1999models](../../references.html#borgatti1999models), [boyd2010computing](../../references.html#boyd2010computing), [comrey1962minimum](../../references.html#comrey1962minimum), [nocedal2006numerical](../../references.html#nocedal2006numerical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [tool_cpnet](../../references.html#tool_cpnet)
{% endraw %}
