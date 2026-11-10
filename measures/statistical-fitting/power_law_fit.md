---
title: "Power-law fit of a degree distribution"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Power-law fit of a degree distribution {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `power_law_fit`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(x_i\)</td><td>observed values (degrees) with \(x_i\ge x_{\min}\)</td></tr><tr><td>\(n\)</td><td>number of observations in the tail</td></tr><tr><td>\(\alpha\)</td><td>power-law exponent</td></tr><tr><td>\(x_{\min}\)</td><td>lower cutoff of the power law</td></tr></tbody></table></div>

## Definition {#concept-definition}

Power-law fit of a degree distribution. Entries grouped here: Power-law fit of a degree distribution.

*Definition partly written:* The maximum likelihood exponent and the minimum-\\(x\\) rule of Clauset et al. are written; the tool options (implementation of the discrete case, whether the Kolmogorov-Smirnov scan is used) were not recorded.

<div class="formula-block"><p class="formula-name"><strong>Continuous maximum likelihood exponent (Clauset, Shalizi and Newman 2009)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\hat\alpha=1+n\Bigl[\sum_{i=1}^{n}\ln\frac{x_i}{x_{\min}}\Bigr]^{-1}\]</div><p class="formula-where">For \(p(x)\propto x^{-\alpha}\), \(x\ge x_{\min}\). Defined if not all \(x_i\) equal \(x_{\min}\) (otherwise the sum is 0).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Discrete approximation</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\hat\alpha\simeq1+n\Bigl[\sum_{i=1}^{n}\ln\frac{x_i}{x_{\min}-\tfrac12}\Bigr]^{-1}\]</div><p class="formula-where">Approximation for integer data with \(x_{\min}\gtrsim6\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Choice of the cutoff</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\hat x_{\min}=\arg\min_{x_{\min}}\ \max_{x\ge x_{\min}}\bigl|S(x)-P(x;\hat\alpha,x_{\min})\bigr|\]</div><p class="formula-where">The cutoff minimizing the Kolmogorov-Smirnov distance between the empirical distribution \(S\) of the tail and the fitted power law \(P\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#power_law_fit">Power-law fit of a degree distribution</a></td><td><code>power_law_fit</code></td><td>2</td><td>Exponent and cutoff of a power law fitted to the degree distribution by the formulas above (continuous or discrete).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/igraph.html">igraph (R)</a></th><th><a href="../../tools/pyigraph.html">igraph (Python)</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All degrees are 0; no positive observations exist and the fit is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">All degrees are equal: the tail has no spread and the exponent is not defined (the sum of logs is 0 for \(x_{\min}\) equal to the degree).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Power-law fit of a degree distribution {#power_law_fit}

Measure id: `power_law_fit`. Original family: Statistical fitting.

**Definition.** Power-law fit of a degree distribution.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-power_law_fit-igraph">details</a></td><td><code>fit_power_law</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-power_law_fit-pyigraph">details</a></td><td><code>power_law_fit</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-power_law_fit-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: fit\_power\_law.
- <a id="why-power_law_fit-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: power\_law\_fit.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
