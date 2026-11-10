---
title: "MR-QAP regression"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# MR-QAP regression {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `qap_regression`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>vectorized dependent matrix</td></tr><tr><td>\(x_1,\dots,x_p\)</td><td>vectorized independent matrices</td></tr><tr><td>\(\beta\)</td><td>coefficients</td></tr><tr><td>\(\pi\)</td><td>node permutation, applied to rows and columns of a matrix together</td></tr><tr><td>\(\tilde x_k\)</td><td>residual of \(x_k\) after regression on the other independent matrices</td></tr></tbody></table></div>

## Definition {#concept-definition}

MR-QAP regression. Entries grouped here: MR-QAP regression (Y-permutation, double semi-partialling).

<div class="formula-block"><p class="formula-name"><strong>Multiple regression on dyads (Krackhardt 1988)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[y=\beta_0+\sum_{k=1}^p\beta_kx_k+\varepsilon,\qquad \hat\beta=(Z^{\top}Z)^{-1}Z^{\top}y,\ \ Z=[\mathbf 1,x_1,\dots,x_p]\]</div><p class="formula-where">Ordinary least squares on the off-diagonal dyads; the usual standard errors are not valid because dyads are dependent, so inference uses permutations. Defined when \(Z^{\top}Z\) is invertible (no exact collinearity).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Y-permutation test (Krackhardt 1988)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[p_k=\Pr_\pi\bigl(|\hat\beta_k(y^{\pi})|\ge|\hat\beta_k(y)|\bigr)\]</div><p class="formula-where">The dependent matrix is permuted (rows and columns together) and the model refit; \(p_k\) is the share of permutations with an equal or larger coefficient.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Double semi-partialling (Dekker, Krackhardt and Snijders 2007)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[p_k=\Pr_\pi\bigl(|\hat\beta_k(y,\ \tilde x_k^{\pi})|\ge|\hat\beta_k(y,\tilde x_k)|\bigr)\]</div><p class="formula-where">Only the residual \(\tilde x_k\) of the tested matrix is permuted, which is less sensitive to collinearity among the independent matrices than permuting \(y\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#qap_regression">MR-QAP regression (Y-permutation, double semi-partialling)</a></td><td><code>qap_regression</code></td><td>2</td><td>Coefficients from the least-squares formula; the p-values come from permuting the dependent matrix (Y-permutation) or the partialled independent matrix (double semi-partialling). Monte Carlo draws depend on the random seed.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Diagonal entries are excluded from the dyad vectors.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">A constant dependent or independent matrix gives a singular or null design: \(\hat\beta\) is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">There are \(n!\) permutations, so for small \(n\) the p-values take few distinct values.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details></div>

## MR-QAP regression (Y-permutation, double semi-partialling) {#qap_regression}

Measure id: `qap_regression`. Original family: Inference (QAP, null models).

**Definition.** MR-QAP regression (Y-permutation, double semi-partialling).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-qap_regression-sna">details</a></td><td><code>netlm</code></td><td>documentation</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-qap_regression-ucinet">details</a></td><td><code>Logistic regression with 2-tailed tests (6.751), OLS regression, univariate statistics, correlation, ANOVA/density-by-group (blocks), contingency tables with od; logistic; regress</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-qap_regression-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: netlm.
- <a id="why-qap_regression-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
