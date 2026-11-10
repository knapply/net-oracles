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

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_factions">Factions</a></td><td><code>cat_factions</code></td><td>1</td></tr><tr><td><a href="#factions_errors">Factions errors</a></td><td><code>factions_errors</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [doreian2005generalized](../../references.html#doreian2005generalized), [glover1989tabu](../../references.html#glover1989tabu), [hanneman2005introduction](../../references.html#hanneman2005introduction)

## Factions {#cat_factions}

Measure id: `cat_factions`. Original family: Cohesion and subgroups.

**Definition.** Factions.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_factions-ucinet">details</a></td><td><code>factions</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_factions-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Factions errors {#factions_errors}

Measure id: `factions_errors`. Original family: Cohesion and subgroups.

**Definition.** Factions: a partition into k groups that best fits the ideal pattern of ties inside groups only, by tabu search from random starts.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-factions_errors-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-factions_errors-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [borgatti1999models](../../references.html#borgatti1999models), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [doreian2005generalized](../../references.html#doreian2005generalized), [glover1989tabu](../../references.html#glover1989tabu), [hanneman2005introduction](../../references.html#hanneman2005introduction)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
