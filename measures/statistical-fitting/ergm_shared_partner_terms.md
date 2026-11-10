---
title: "Shared-partner terms"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Shared-partner terms {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: ERGM terms. Concept id: `ergm_shared_partner_terms`. 12 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr></tbody></table></div>

## Definition {#concept-definition}

Shared-partner terms. Entries grouped here: Ddsp; Ddsp L; Desp; Desp L; Dgwdsp; Dgwdsp L; and 6 more.

*Definition partly written:* The geometrically weighted forms are written. The edgewise, dyadwise and non-edgewise shared-partner counts (esp, dsp, nsp) and the directed (d-prefixed) and L-suffixed forms are named in the sources only; variants are not given.

<div class="formula-block"><p class="formula-name"><strong>Geometrically weighted terms (Hunter 2007)</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\text{gwesp}_\alpha=e^{\alpha}\sum_{k=1}^{n-2}\bigl\{1-(1-e^{-\alpha})^{k}\bigr\}\,\mathrm{ESP}_k,\qquad \text{gwdsp}_\alpha=e^{\alpha}\sum_{k=1}^{n-2}\bigl\{1-(1-e^{-\alpha})^{k}\bigr\}\,\mathrm{DSP}_k,\qquad \text{gwdegree}_\alpha=e^{\alpha}\sum_{k=1}^{n-1}\bigl\{1-(1-e^{-\alpha})^{k}\bigr\}\,D_k\]</div><p class="formula-where">\(\mathrm{ESP}_k\): number of tied pairs with exactly \(k\) shared partners; \(\mathrm{DSP}_k\): number of node pairs (tied or not) with \(k\) shared partners; \(D_k\): number of nodes of degree \(k\). With the decay \(\alpha\) fixed they are ordinary statistics; with \(\alpha\) estimated the model is a curved exponential family. Software truncates the counts at a cutoff; a cutoff above \(n\) loses nothing. In directed networks the direction of the shared-partner two-path (and of the degree) has to be chosen, giving gwidegree and gwodegree for in- and out-degrees.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_ddsp">Ddsp</a></td><td><code>cat_ddsp</code></td><td>1</td></tr><tr><td><a href="#cat_ddsp_l">Ddsp L</a></td><td><code>cat_ddsp_l</code></td><td>1</td></tr><tr><td><a href="#cat_desp">Desp</a></td><td><code>cat_desp</code></td><td>1</td></tr><tr><td><a href="#cat_desp_l">Desp L</a></td><td><code>cat_desp_l</code></td><td>1</td></tr><tr><td><a href="#cat_dgwdsp">Dgwdsp</a></td><td><code>cat_dgwdsp</code></td><td>1</td></tr><tr><td><a href="#cat_dgwdsp_l">Dgwdsp L</a></td><td><code>cat_dgwdsp_l</code></td><td>1</td></tr><tr><td><a href="#cat_dgwesp">Dgwesp</a></td><td><code>cat_dgwesp</code></td><td>1</td></tr><tr><td><a href="#cat_dgwesp_l">Dgwesp L</a></td><td><code>cat_dgwesp_l</code></td><td>1</td></tr><tr><td><a href="#cat_dgwnsp">Dgwnsp</a></td><td><code>cat_dgwnsp</code></td><td>1</td></tr><tr><td><a href="#cat_dgwnsp_l">Dgwnsp L</a></td><td><code>cat_dgwnsp_l</code></td><td>1</td></tr><tr><td><a href="#cat_dnsp">Dnsp</a></td><td><code>cat_dnsp</code></td><td>1</td></tr><tr><td><a href="#cat_dnsp_l">Dnsp L</a></td><td><code>cat_dnsp_l</code></td><td>1</td></tr></tbody></table></div>

## Ddsp {#cat_ddsp}

Measure id: `cat_ddsp`. Original family: Graph theory and combinatorics.

**Definition.** Ddsp.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_ddsp-ergm">details</a></td><td><code>ddsp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_ddsp-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: ddsp.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Ddsp L {#cat_ddsp_l}

Measure id: `cat_ddsp_l`. Original family: Graph theory and combinatorics.

**Definition.** Ddsp L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_ddsp_l-ergm">details</a></td><td><code>ddspL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_ddsp_l-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: ddspL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Desp {#cat_desp}

Measure id: `cat_desp`. Original family: Graph theory and combinatorics.

**Definition.** Desp.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_desp-ergm">details</a></td><td><code>desp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_desp-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: desp.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Desp L {#cat_desp_l}

Measure id: `cat_desp_l`. Original family: Graph theory and combinatorics.

**Definition.** Desp L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_desp_l-ergm">details</a></td><td><code>despL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_desp_l-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: despL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dgwdsp {#cat_dgwdsp}

Measure id: `cat_dgwdsp`. Original family: Graph theory and combinatorics.

**Definition.** Dgwdsp.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dgwdsp-ergm">details</a></td><td><code>dgwdsp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dgwdsp-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dgwdsp.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dgwdsp L {#cat_dgwdsp_l}

Measure id: `cat_dgwdsp_l`. Original family: Graph theory and combinatorics.

**Definition.** Dgwdsp L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dgwdsp_l-ergm">details</a></td><td><code>dgwdspL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dgwdsp_l-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dgwdspL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dgwesp {#cat_dgwesp}

Measure id: `cat_dgwesp`. Original family: Graph theory and combinatorics.

**Definition.** Dgwesp.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dgwesp-ergm">details</a></td><td><code>dgwesp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dgwesp-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dgwesp.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dgwesp L {#cat_dgwesp_l}

Measure id: `cat_dgwesp_l`. Original family: Graph theory and combinatorics.

**Definition.** Dgwesp L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dgwesp_l-ergm">details</a></td><td><code>dgwespL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dgwesp_l-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dgwespL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dgwnsp {#cat_dgwnsp}

Measure id: `cat_dgwnsp`. Original family: Graph theory and combinatorics.

**Definition.** Dgwnsp.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dgwnsp-ergm">details</a></td><td><code>dgwnsp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dgwnsp-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dgwnsp.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dgwnsp L {#cat_dgwnsp_l}

Measure id: `cat_dgwnsp_l`. Original family: Graph theory and combinatorics.

**Definition.** Dgwnsp L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dgwnsp_l-ergm">details</a></td><td><code>dgwnspL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dgwnsp_l-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dgwnspL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dnsp {#cat_dnsp}

Measure id: `cat_dnsp`. Original family: Graph theory and combinatorics.

**Definition.** Dnsp.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dnsp-ergm">details</a></td><td><code>dnsp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dnsp-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dnsp.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)

## Dnsp L {#cat_dnsp_l}

Measure id: `cat_dnsp_l`. Original family: Graph theory and combinatorics.

**Definition.** Dnsp L.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dnsp_l-ergm">details</a></td><td><code>dnspL</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dnsp_l-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: dnspL.

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
