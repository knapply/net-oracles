---
title: "Iterative proportional fitting"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Iterative proportional fitting {#concept-top}

Family: [Data transforms](index.html). Subfamily: Sparsification and backbones. Concept id: `ipf`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(X^{(0)}\)</td><td>seed matrix with non-negative entries</td></tr><tr><td>\(r_u,\ c_v\)</td><td>target row and column sums</td></tr></tbody></table></div>

## Definition {#concept-definition}

Iterative proportional fitting. Entries grouped here: Ipf.

*Definition partly written:* The scaling steps are written in their standard form without a cited source; convergence conditions and stopping rules of the documented entry are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Iterative proportional fitting</strong> <span class="applies">applies to: weighted</span></p><div class="formula">\[x^{(2t+1)}_{uv}=x^{(2t)}_{uv}\,\frac{r_u}{\sum_{v'}x^{(2t)}_{uv'}},\qquad x^{(2t+2)}_{uv}=x^{(2t+1)}_{uv}\,\frac{c_v}{\sum_{u'}x^{(2t+1)}_{u'v}}\]</div><p class="formula-where">Alternately rescale rows to the targets \(r\) and columns to \(c\) until both hold; it converges to a matrix with those margins when one exists (equal totals, compatible zero pattern), and is not defined for a zero row with a positive target.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_ipf">Ipf</a></td><td><code>cat_ipf</code></td><td>1</td><td>Alternate row and column rescaling to given margins; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">A zero entry stays 0 under multiplicative scaling, so the zero pattern of the seed is kept.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">An all-zero seed row with positive target has no rescaling: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Ipf {#cat_ipf}

Measure id: `cat_ipf`. Original family: Graph theory and combinatorics.

**Definition.** Ipf.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_ipf-ucinet">details</a></td><td><code>ipf</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_ipf-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
