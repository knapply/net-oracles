---
title: "Normalize ties"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Normalize ties {#concept-top}

Family: [Data transforms](index.html). Subfamily: Matrix and tie transformations. Concept id: `normalize_ties`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(X=(x_{uv})\)</td><td>valued matrix</td></tr><tr><td>\(S\)</td><td>the set of entries normalized together: a row, a column, or the whole matrix</td></tr><tr><td>\(\bar x_S,\ s_S\)</td><td>mean and standard deviation of the entries of \(S\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Normalize ties. Entries grouped here: Normalize ties (row, column, matrix; sum, mean, max, z, Euclidean, IPF).

*Definition partly written:* Formulas are written from the method names in the documented entry without a cited source; the standard-deviation convention of the z-score (population or sample) and the treatment of a zero normalizer are not stated in the sources. Iterative proportional fitting is on the concept ipf.

<div class="formula-block"><p class="formula-name"><strong>Sum</strong> <span class="applies">applies to: weighted</span></p><div class="formula">\[x'_{uv}=\frac{x_{uv}}{\sum_{S}x}\]</div><p class="formula-where">Entries of \(S\) sum to 1; not defined when the sum is 0.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Mean</strong> <span class="applies">applies to: weighted</span></p><div class="formula">\[x'_{uv}=\frac{x_{uv}}{\bar x_S}\]</div><p class="formula-where">Entries have mean 1; not defined when the mean is 0.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Maximum</strong> <span class="applies">applies to: weighted</span></p><div class="formula">\[x'_{uv}=\frac{x_{uv}}{\max_Sx}\]</div><p class="formula-where">The largest entry becomes 1; not defined when the maximum is 0.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Z-score</strong> <span class="applies">applies to: weighted</span></p><div class="formula">\[x'_{uv}=\frac{x_{uv}-\bar x_S}{s_S}\]</div><p class="formula-where">Mean 0 and standard deviation 1; \(s_S\) uses \(n\) or \(n-1\) in the denominator by convention, and is 0 for a constant set.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Euclidean</strong> <span class="applies">applies to: weighted</span></p><div class="formula">\[x'_{uv}=\frac{x_{uv}}{\sqrt{\sum_{S}x^2}}\]</div><p class="formula-where">Unit Euclidean length of \(S\); not defined for an all-zero \(S\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#normalize_ties">Normalize ties (row, column, matrix; sum, mean, max, z, Euclidean, IPF)</a></td><td><code>normalize_ties</code></td><td>1</td><td>Collective entry: the five scalings above applied by row, by column, or by matrix; iterative proportional fitting is a sixth method (concept ipf).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">An all-zero row, column or matrix makes the sum, mean, maximum and Euclidean normalizers 0, so the result is 0/0: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">A single entry has \(s_S=0\) (or \(n-1=0\)): the z-score is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">Negative entries are allowed by the formulas; the sum can then be 0 or negative, and normalization by sum no longer gives proportions.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Normalize ties (row, column, matrix; sum, mean, max, z, Euclidean, IPF) {#normalize_ties}

Measure id: `normalize_ties`. Original family: Data transforms.

**Definition.** Normalize ties (row, column, matrix; sum, mean, max, z, Euclidean, IPF).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-normalize_ties-ucinet">details</a></td><td><code>Recode, Diagonal (set/ignore), Normalize (row, column, matrix; sum, mean, max, z, Euclidean, IPF)</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-normalize_ties-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
