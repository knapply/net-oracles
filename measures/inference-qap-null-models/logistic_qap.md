---
title: "Logistic MR-QAP"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Logistic MR-QAP {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `logistic_qap`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>vectorized dependent matrix</td></tr><tr><td>\(x_1,\dots,x_p\)</td><td>vectorized independent matrices</td></tr><tr><td>\(\beta\)</td><td>coefficients</td></tr><tr><td>\(\pi\)</td><td>node permutation, applied to rows and columns of a matrix together</td></tr><tr><td>\(p_{ij}\)</td><td>modelled probability of a tie from \(i\) to \(j\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Logistic MR-QAP. Entries grouped here: Logistic MR-QAP.

*Definition partly written:* The logistic likelihood is the standard one; no primary paper for logistic MR-QAP was checked, so the permutation scheme is stated only by analogy with MR-QAP and has no citation of its own.

<div class="formula-block"><p class="formula-name"><strong>Logistic model of the dyads (as in logistic regression)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\operatorname{logit}p_{ij}=\beta_0+\sum_{k=1}^p\beta_kx_{k,ij},\qquad \ell(\beta)=\sum_{i\ne j}\bigl[y_{ij}\log p_{ij}+(1-y_{ij})\log(1-p_{ij})\bigr]\]</div><p class="formula-where">For a binary dependent matrix; the maximum likelihood estimate does not exist when the tie indicator is perfectly separated by the independent matrices. Significance is judged against node permutations, as for MR-QAP.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#lr_qap">Logistic MR-QAP</a></td><td><code>lr_qap</code></td><td>2</td><td>Binary-dependent version of the MR-QAP regression: logistic likelihood above, permutation p-values.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">A dependent matrix with no ties (or all ties) has no finite maximum likelihood estimate: the likelihood is monotone.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Logistic MR-QAP {#lr_qap}

Measure id: `lr_qap`. Original family: Inference (QAP, null models).

**Definition.** Logistic MR-QAP.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-lr_qap-sna">details</a></td><td><code>netlogit</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-lr_qap-ucinet">details</a></td><td><code>LR-QAP (logistic, 6.763 help file, 6.839 three times faster)</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-lr_qap-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: netlogit.
- <a id="why-lr_qap-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
