---
title: "Network autocorrelation"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Network autocorrelation {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `network_autocorrelation`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>vector of node outcomes</td></tr><tr><td>\(W\)</td><td>\(n\times n\) weight matrix of the network (row-normalized in the usual formulation)</td></tr><tr><td>\(\rho,\lambda\)</td><td>autocorrelation parameters</td></tr><tr><td>\(X,\beta\)</td><td>covariates and coefficients</td></tr></tbody></table></div>

## Definition {#concept-definition}

Network autocorrelation. Entries grouped here: Network autocorrelation: lag/error model, Moran, Geary.

*Definition partly written:* The lag and error models are written (Anselin 1988). The Moran and Geary indices that the sources also list are named only; their formulas are not written here.

<div class="formula-block"><p class="formula-name"><strong>Network effects (lag) model (Anselin 1988)</strong> <span class="applies">applies to: any, weighted</span></p><div class="formula">\[y=\rho Wy+X\beta+\varepsilon,\qquad \varepsilon\sim N(0,\sigma^2I)\]</div><p class="formula-where">The outcome of a node depends on the weighted outcomes of its neighbours. The reduced form \(y=(I-\rho W)^{-1}(X\beta+\varepsilon)\) requires \(I-\rho W\) to be invertible, i.e. \(1/\rho\) is not an eigenvalue of \(W\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Network disturbances (error) model (Anselin 1988)</strong> <span class="applies">applies to: any, weighted</span></p><div class="formula">\[y=X\beta+u,\qquad u=\lambda Wu+\varepsilon\]</div><p class="formula-where">The dependence sits in the error term instead of the outcome.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#network_autocorrelation">Network autocorrelation: lag/error model, Moran, Geary</a></td><td><code>network_autocorrelation</code></td><td>2</td><td>Lag or error model estimated by maximum likelihood; the Moran and Geary indices are not covered.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">The model is defined only for \(\rho\) (or \(\lambda\)) with \(I-\rho W\) non-singular; for a row-normalized \(W\) this holds for \(|\rho|&lt;1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A node with no ties has a zero row in \(W\); row normalization is then 0/0 and a convention is needed.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details></div>

## Network autocorrelation: lag/error model, Moran, Geary {#network_autocorrelation}

Measure id: `network_autocorrelation`. Original family: Inference (QAP, null models).

**Definition.** Network autocorrelation: lag/error model, Moran, Geary.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-network_autocorrelation-sna">details</a></td><td><code>lnam; nacf</code></td><td>documentation</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-network_autocorrelation-ucinet">details</a></td><td><code>Geary; Network autocorrelation (continuous, 6.753): Moran, Geary; lautocorr</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-network_autocorrelation-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: lnam; nacf.
- <a id="why-network_autocorrelation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
