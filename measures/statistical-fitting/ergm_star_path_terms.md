---
title: "Star and path terms"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Star and path terms {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: ERGM terms. Concept id: `ergm_star_path_terms`. 6 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr></tbody></table></div>

## Definition {#concept-definition}

Star and path terms. Entries grouped here: Altkstar; M2star; Mutual L; Threetrail; Twopath; Twostar L.

*Definition partly written:* Only twopath and the alternating k-star are written; M2star, three-trail and the L-suffixed forms are named only.

<div class="formula-block"><p class="formula-name"><strong>Two-path (Morris et al. 2008)</strong> <span class="applies">applies to: directed, simple</span></p><div class="formula">\[\text{twopath}(y)=\sum_{(i,j,h)}y_{ij}y_{jh}\quad(i,j,h\text{ distinct})\]</div><p class="formula-where">Ordered pairs of consecutive ties through a middle node.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Alternating k-star (Snijders et al. 2006)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\text{altkstar}_\lambda=\sum_{k=2}^{n-1}(-1)^{k}\frac{S_k}{\lambda^{k-2}}\]</div><p class="formula-where">Weights the \(k\)-star counts \(S_k\) alternately; for \(\lambda&gt;1\) it is a curved-exponential-family form of the degree distribution (related to gwdegree).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_altkstar">Altkstar</a></td><td><code>cat_altkstar</code></td><td>1</td><td>Alternating k-star statistic with decay \(\lambda\).</td></tr><tr><td><a href="#cat_twopath">Twopath</a></td><td><code>cat_twopath</code></td><td>1</td><td>Directed two-path count above.</td></tr></tbody></table></div>

## Altkstar {#cat_altkstar}

Measure id: `cat_altkstar`. Original family: Graph theory and combinatorics.

**Definition.** Altkstar.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_altkstar-ergm">details</a></td><td><code>altkstar</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_altkstar-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: altkstar.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## M2star {#cat_m2star}

Measure id: `cat_m2star`. Original family: Graph theory and combinatorics.

**Definition.** M2star.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_m2star-ergm">details</a></td><td><code>m2star</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_m2star-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: m2star.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Mutual L {#cat_l_mutual}

Measure id: `cat_l_mutual`. Original family: Graph theory and combinatorics.

**Definition.** Mutual L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_l_mutual-ergm">details</a></td><td><code>mutualL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_l_mutual-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: mutualL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Threetrail {#cat_threetrail}

Measure id: `cat_threetrail`. Original family: Graph theory and combinatorics.

**Definition.** Threetrail.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_threetrail-ergm">details</a></td><td><code>threetrail</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_threetrail-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: threetrail.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Twopath {#cat_twopath}

Measure id: `cat_twopath`. Original family: Paths and distances.

**Definition.** Twopath.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_twopath-ergm">details</a></td><td><code>twopath</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_twopath-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: twopath.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Twostar L {#cat_l_twostar}

Measure id: `cat_l_twostar`. Original family: Graph theory and combinatorics.

**Definition.** Twostar L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_l_twostar-ergm">details</a></td><td><code>twostarL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_l_twostar-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: twostarL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
