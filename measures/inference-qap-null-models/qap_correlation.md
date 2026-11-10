---
title: "QAP correlation"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# QAP correlation {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `qap_correlation`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(X,Y\)</td><td>two \(n\times n\) matrices over the same node set</td></tr><tr><td>\(x,y\)</td><td>their vectorized off-diagonal entries (for undirected data the upper triangle only)</td></tr><tr><td>\(\pi\)</td><td>a permutation of the nodes; \(Y^{\pi}\) has rows and columns permuted by \(\pi\) simultaneously</td></tr><tr><td>\(r(X,Y)\)</td><td>Pearson correlation of \(x\) and \(y\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

QAP correlation. Entries grouped here: QAP correlation (Y-permutation, exact and Monte Carlo).

<div class="formula-block"><p class="formula-name"><strong>Matrix correlation (Hubert and Schultz 1976)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[r(X,Y)=\frac{\sum_{(i,j)}(x_{ij}-\bar x)(y_{ij}-\bar y)}{\sqrt{\sum_{(i,j)}(x_{ij}-\bar x)^2\sum_{(i,j)}(y_{ij}-\bar y)^2}},\quad i\ne j\]</div><p class="formula-where">The product-moment correlation over dyads, diagonal excluded. Defined when both matrices are non-constant (otherwise a variance is 0).</p></div>

<div class="formula-block"><p class="formula-name"><strong>QAP permutation p-value (Hubert and Schultz 1976; Krackhardt 1987)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[p_{\ge}=\frac{\#\{\pi:\ r(X,Y^{\pi})\ge r(X,Y)\}}{n!},\qquad p_{\le}=\frac{\#\{\pi:\ r(X,Y^{\pi})\le r(X,Y)\}}{n!}\]</div><p class="formula-where">The reference distribution is all \(n!\) simultaneous row-and-column permutations of one matrix, which keeps the dependence among dyads of the same node. For large \(n\) it is estimated from a random sample of \(B\) permutations, so the p-value then depends on the random generator and seed.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#qap_correlation">QAP correlation (Y-permutation, exact and Monte Carlo)</a></td><td><code>qap_correlation</code></td><td>2</td><td>Observed correlation and permutation p-values (Y-permutation); exact enumeration or Monte Carlo sampling of permutations changes only how the p-value is computed.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The diagonal is not part of the dyad vectors; loops do not enter \(r\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">For directed data all \(n(n-1)\) off-diagonal entries are used; for undirected data the \(n(n-1)/2\) upper-triangle entries.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With \(n\le2\) there are at most two permutations, so the permutation p-value can take only a few values; with a single dyad the correlation is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">A constant matrix (for example an empty one) has zero variance: the correlation is not defined (0/0).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Permutations giving a correlation equal to the observed one count in both tails \(p_{\ge}\) and \(p_{\le}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

## QAP correlation (Y-permutation, exact and Monte Carlo) {#qap_correlation}

Measure id: `qap_correlation`. Original family: Inference (QAP, null models).

**Definition.** QAP correlation (Y-permutation, exact and Monte Carlo).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-qap_correlation-sna">details</a></td><td><code>gcor; gcov; gscor; gscov; qaptest</code></td><td>documentation</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-qap_correlation-ucinet">details</a></td><td><code>QAP; QAP correlation (2-tailed default since 6.839), QAP regression (MR-QAP rewritten 6.829; seed fix 6.805; "count in dyad" effect 6.833; FAQ on how coefficients ar; corr; corrmat; rectqap</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-qap_correlation-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: gcor; gcov; gscor; gscov; qaptest.
- <a id="why-qap_correlation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
