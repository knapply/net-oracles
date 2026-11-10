---
title: "Imputation of missing node-level data"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Imputation of missing node-level data {#concept-top}

Family: [Data transforms](index.html). Subfamily: Missing data. Concept id: `impute_missing`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(X=(x_{uv})\)</td><td>relation with missing entries</td></tr><tr><td>\(U\)</td><td>nodes whose whole row is missing</td></tr></tbody></table></div>

## Definition {#concept-definition}

Imputation of missing node-level data. Entries grouped here: Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed).

*Definition partly written:* The rule is written from the name of the documented entry; no source or tool behaviour beyond the name is recorded.

<div class="formula-block"><p class="formula-name"><strong>Row imputation from the column</strong> <span class="applies">applies to: any</span></p><div class="formula">\[x_{u\cdot}:=x_{\cdot u}^{\top}\quad(u\in U)\]</div><p class="formula-where">For an undirected (symmetric) relation a missing row is replaced by the same node's column; for a directed relation the entries are taken from the opposite-direction relation as the entry says.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected">Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed)</a></td><td><code>cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected</code></td><td>1</td><td>Node-level imputation of missing rows from the column or the opposite-direction relation; documented only.</td></tr></tbody></table></div>

## Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed) {#cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected}

Measure id: `cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected`. Original family: Mixing and assortativity.

**Definition.** Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected-ucinet">details</a></td><td><code>Missing: impute node-level missing row from column (undirected) or from the opposite-direction relation (directed)</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_column_directed_direction_from_impute_level_missing_opposite_or_relation_row_undirected-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
