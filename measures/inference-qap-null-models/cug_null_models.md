---
title: "Conditional uniform graph tests and null models"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Conditional uniform graph tests and null models {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `cug_null_models`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(g\)</td><td>the observed graph</td></tr><tr><td>\(T\)</td><td>a graph-level statistic (density, centralization, ...)</td></tr><tr><td>\(U(n),U(n,m),U(n,M,A,N)\)</td><td>uniform distributions over graphs of order \(n\), of order \(n\) with \(m\) edges, and of order \(n\) with a given dyad census (\(M\) mutual, \(A\) asymmetric, \(N\) null dyads)</td></tr><tr><td>\(B\)</td><td>number of simulated graphs</td></tr></tbody></table></div>

## Definition {#concept-definition}

Conditional uniform graph tests and null models. Entries grouped here: Conditional uniform graph tests and null models.

<div class="formula-block"><p class="formula-name"><strong>Conditional uniform graph test (Anderson, Butts and Carley 1999)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[p_{\ge}=\Pr_{G\sim U(\cdot)}\bigl(T(G)\ge T(g)\bigr),\qquad p_{\le}=\Pr_{G\sim U(\cdot)}\bigl(T(G)\le T(g)\bigr)\]</div><p class="formula-where">The observed statistic is compared with its distribution among graphs drawn uniformly from the class fixed by the conditioning: size only, size and number of edges, or size and dyad census. For classes too large to enumerate the probabilities are estimated from \(B\) random draws, so the value depends on the random generator and seed.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Uniform distribution on graphs with given order and size</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[U(n,m):\ \ \Pr(G)=\binom{n(n-1)/2}{m}^{-1}\ (\text{undirected, simple})\]</div><p class="formula-where">Each simple undirected graph with \(m\) edges is equally likely; the number of such graphs is the binomial coefficient.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cug_null_models">Conditional uniform graph tests and null models</a></td><td><code>cug_null_models</code></td><td>2</td><td>Choice of the conditioning class (size, edges, dyad census) and of the tail decides the null distribution; the statistic \(T\) is any graph-level index.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The class \(U(n,0)\) contains one graph; the distribution of \(T\) is a point mass and \(p_{\ge}=p_{\le}=1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">The class \(U(n,m)\) with \(m\) the maximum contains one graph: both p-values are 1.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">For tiny \(n\) the classes can be enumerated, giving exact p-values instead of Monte Carlo ones.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Draws with a statistic equal to the observed one count in both tails.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

## Conditional uniform graph tests and null models {#cug_null_models}

Measure id: `cug_null_models`. Original family: Inference (QAP, null models).

**Definition.** Conditional uniform graph tests and null models.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-cug_null_models-sna">details</a></td><td><code>cug.test; cugtest</code></td><td>documentation</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cug_null_models-ucinet">details</a></td><td><code>Conditional uniform graph tests, TERGM/ERGM are not UCINET</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cug_null_models-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: cug.test; cugtest.
- <a id="why-cug_null_models-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
