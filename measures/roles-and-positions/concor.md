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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target</td></tr><tr><td>\(M^{(0)}\)</td><td>matrix of correlations between the tie profiles (rows) of the nodes</td></tr><tr><td>\(M^{(t+1)}=\mathrm{corr}(M^{(t)})\)</td><td>the matrix of Pearson correlations between the columns of the previous matrix</td></tr></tbody></table></div>

## Definition {#concept-definition}

CONCOR blocks: repeated splits of the nodes by iterated correlation of their correlation matrix, numbered from 1.

*Definition partly written:* Documented only (UCINET), never run; the stopping rule, the treatment of the diagonal and the handling of several relations in its implementation are not recorded in the sources.

<div class="formula-block"><p class="formula-name"><strong>CONCOR (Breiger, Boorman and Arabie 1975)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[M^{(t+1)}_{ij}=\frac{\sum_k\bigl(M^{(t)}_{ki}-\bar M^{(t)}_i\bigr)\bigl(M^{(t)}_{kj}-\bar M^{(t)}_j\bigr)}{\sqrt{\sum_k\bigl(M^{(t)}_{ki}-\bar M^{(t)}_i\bigr)^2\sum_k\bigl(M^{(t)}_{kj}-\bar M^{(t)}_j\bigr)^2}}\]</div><p class="formula-where">Iterated correlation converges to a matrix of entries \(\pm1\); the nodes are split into two blocks by the sign pattern, and each block is split again by repeating the procedure on its submatrix. A column with zero variance makes the correlation 0/0.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#concor">Concor</a></td><td><code>concor</code></td><td>1</td><td>Blocks obtained by repeated splitting by iterated correlation, numbered from 1; the formula above is the iteration step.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With fewer than three nodes a correlation between profiles over the remaining entries is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A node with no ties (and a profile of constant entries) has zero variance: its correlations are 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Entries that are exactly 0 after convergence have no sign: which side they belong to is not fixed by the definition.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[breiger1975algorithm](../../references.html#breiger1975algorithm), [burt1976positions](../../references.html#burt1976positions), [lorrain1971structural](../../references.html#lorrain1971structural), [wasserman1994social](../../references.html#wasserman1994social)

## Concor {#concor}

Measure id: `concor`. Original family: Roles and positions.

**Definition.** CONCOR blocks: repeated splits of the nodes by iterated correlation of their correlation matrix, numbered from 1.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-concor-ucinet">details</a></td><td><code>CONCOR, hierarchical clustering, blockmodels, optimization; ccsplit</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-concor-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [breiger1975algorithm](../../references.html#breiger1975algorithm), [burt1976positions](../../references.html#burt1976positions), [lorrain1971structural](../../references.html#lorrain1971structural), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
