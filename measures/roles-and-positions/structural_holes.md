---
title: "Structural holes (Burt)"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Structural holes (Burt) {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `structural_holes`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(p_{ij}\)</td><td>share of the tie volume of \(i\) invested in \(j\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Structural holes (Burt). Entries grouped here: Dyconst; Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6 798), "corrected constraint" FA.

*Definition partly written:* Both measures are documented only (UCINET) and never run: dyadic constraint (Dyconst) and the Structural holes suite (effective size, efficiency, constraint, hierarchy, dyadic redundancy, 'corrected constraint'). Their implementation options are not recorded; the formulas of Burt's own indices are under Burt constraint, effective size and efficiency.

<div class="formula-block"><p class="formula-name"><strong>Dyadic constraint (Burt 1992)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[c_{ij}=\Bigl(p_{ij}+\sum_{q\ne i,j}p_{iq}p_{qj}\Bigr)^2\]</div><p class="formula-where">Constraint on \(i\) from the single contact \(j\); its sum over contacts is the aggregate constraint. Not defined for a node without ties (the shares \(p\) have a 0 denominator).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_dyconst">Dyconst</a></td><td><code>cat_dyconst</code></td><td>1</td><td>The dyadic constraint \(c_{ij}\) for each ordered pair, as in the formula above.</td></tr><tr><td><a href="#cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural">Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6 798), "corrected constraint" FA</a></td><td><code>cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural</code></td><td>1</td><td>The UCINET structural holes suite: effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint, and a 'corrected constraint'; documented only and not recorded in detail.</td></tr></tbody></table></div>

## Dyconst {#cat_dyconst}

Measure id: `cat_dyconst`. Original family: Graph theory and combinatorics.

**Definition.** Dyconst.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_dyconst-ucinet">details</a></td><td><code>dyconst</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dyconst-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6 798), "corrected constraint" FA {#cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural}

Measure id: `cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural`. Original family: Roles and positions.

**Definition.** Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6 798), "corrected constraint" FA.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural-ucinet">details</a></td><td><code>Structural holes (Burt): effective size, efficiency, constraint, hierarchy, dyadic redundancy and constraint (dyadicconstraint 6.798), "corrected constraint" FA</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_6_798_burt_constraint_corrected_dyadic_dyadicconstraint_effective_efficiency_fa_hierarchy_holes_redundancy_size_structural-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
