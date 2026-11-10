---
title: "Multidimensional scaling"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Multidimensional scaling {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Scaling and clustering. Concept id: `multidimensional_scaling`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(D=(d_{ij})\)</td><td>matrix of dissimilarities between \(n\) objects</td></tr><tr><td>\(J=I-\tfrac1n\mathbf 1\mathbf 1^{\mathsf T}\)</td><td>centering matrix</td></tr><tr><td>\(B=-\tfrac12JD^{(2)}J\)</td><td>double-centred matrix of squared dissimilarities</td></tr><tr><td>\(X\)</td><td>configuration of \(n\) points in \(p\) dimensions, with distances \(\hat d_{ij}\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Multidimensional scaling. Entries grouped here: Classical mds; Non-metric MDS with stress-1.

*Note:* Both measures are documented only (UCINET) and were never run; the formulas are those of the original papers, not a record of UCINET's options.

<div class="formula-block"><p class="formula-name"><strong>Classical scaling (Torgerson 1952)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[X=E_p\,\Lambda_p^{1/2},\qquad B=E\Lambda E^{\mathsf T}\]</div><p class="formula-where">The first \(p\) eigenvectors scaled by the square roots of the \(p\) largest positive eigenvalues of \(B\). The configuration is unique up to rotation, reflection and sign, and is not determined when leading eigenvalues coincide.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Kruskal stress-1 (Kruskal 1964)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[S_1=\sqrt{\frac{\sum_{i&lt;j}(\hat d_{ij}-f(d_{ij}))^2}{\sum_{i&lt;j}\hat d_{ij}^2}}\]</div><p class="formula-where">Non-metric scaling chooses \(X\) to minimize stress, where \(f\) is a monotone transformation of the dissimilarities; iterative, so the result depends on the start and may be a local minimum.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#classical_mds">Classical mds</a></td><td><code>classical_mds</code></td><td>1</td><td>Classical (Torgerson) scaling: eigendecomposition of the double-centred squared distance matrix.</td></tr><tr><td><a href="#mds_nonmetric">Non-metric MDS with stress-1</a></td><td><code>mds_nonmetric</code></td><td>1</td><td>Non-metric scaling that minimizes Kruskal's stress-1 over configurations and monotone transformations.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With fewer than \(p+1\) points the configuration has fewer than \(p\) dimensions of positive eigenvalue.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Repeated eigenvalues leave the configuration determined only up to a rotation within the eigenspace; sign of each axis is arbitrary.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">Negative eigenvalues of \(B\) (non-Euclidean dissimilarities) cannot be represented and are dropped.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Classical mds {#classical_mds}

Measure id: `classical_mds`. Original family: Roles and positions.

**Definition.** Classical mds.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-classical_mds-ucinet">details</a></td><td><code>MDS (metric, classic, non-metric), Guttman scaling (6.831), correspondence analysis, factor analysis; classicmds</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-classical_mds-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Non-metric MDS with stress-1 {#mds_nonmetric}

Measure id: `mds_nonmetric`. Original family: Roles and positions.

**Definition.** Non-metric MDS with stress-1.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-mds_nonmetric-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-mds_nonmetric-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
