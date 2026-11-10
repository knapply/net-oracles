---
title: "Statistical backbone extraction"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Statistical backbone extraction {#concept-top}

Family: [Data transforms](index.html). Subfamily: Sparsification and backbones. Concept id: `statistical_backbone`. 12 measures.

## Definition {#concept-definition}

Statistical backbone extraction. Entries grouped here: Backbone; Backbone extraction (SDSM/BiCM, FDSM, fixed-row/column/fill); Bicm; Disparity; Fastball; Fdsm; and 6 more.

*Definition not yet written.* The sources list thirteen backbone-extraction procedures (SDSM, FDSM, BiCM, fixed row/column/fill, disparity filter, LANS, MLF, fastball) as documented-only entries by name; none of the original papers is among the checked sources, so no formula is written.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_backbone">Backbone</a></td><td><code>cat_backbone</code></td><td>1</td></tr><tr><td><a href="#backbone_extraction">Backbone extraction (SDSM/BiCM, FDSM, fixed-row/column/fill)</a></td><td><code>backbone_extraction</code></td><td>1</td></tr><tr><td><a href="#cat_bicm">Bicm</a></td><td><code>cat_bicm</code></td><td>1</td></tr><tr><td><a href="#cat_disparity">Disparity</a></td><td><code>cat_disparity</code></td><td>1</td></tr><tr><td><a href="#cat_fastball">Fastball</a></td><td><code>cat_fastball</code></td><td>1</td></tr><tr><td><a href="#cat_fdsm">Fdsm</a></td><td><code>cat_fdsm</code></td><td>1</td></tr><tr><td><a href="#cat_fixedcol">Fixedcol</a></td><td><code>cat_fixedcol</code></td><td>1</td></tr><tr><td><a href="#cat_fixedfill">Fixedfill</a></td><td><code>cat_fixedfill</code></td><td>1</td></tr><tr><td><a href="#cat_fixedrow">Fixedrow</a></td><td><code>cat_fixedrow</code></td><td>1</td></tr><tr><td><a href="#cat_lans">Lans</a></td><td><code>cat_lans</code></td><td>1</td></tr><tr><td><a href="#cat_mlf">Mlf</a></td><td><code>cat_mlf</code></td><td>1</td></tr><tr><td><a href="#cat_sdsm">Sdsm</a></td><td><code>cat_sdsm</code></td><td>1</td></tr></tbody></table></div>

## Backbone {#cat_backbone}

Measure id: `cat_backbone`. Original family: Graph theory and combinatorics.

**Definition.** Backbone.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_backbone-bct">details</a></td><td><code>backbone_wu</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_backbone-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: backbone\_wu.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)

## Backbone extraction (SDSM/BiCM, FDSM, fixed-row/column/fill) {#backbone_extraction}

Measure id: `backbone_extraction`. Original family: Two-mode and bipartite.

**Definition.** Backbone extraction (SDSM/BiCM, FDSM, fixed-row/column/fill).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-backbone_extraction-backbone">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-backbone_extraction-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Bicm {#cat_bicm}

Measure id: `cat_bicm`. Original family: Graph theory and combinatorics.

**Definition.** Bicm.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_bicm-backbone">details</a></td><td><code>bicm</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bicm-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Disparity {#cat_disparity}

Measure id: `cat_disparity`. Original family: Graph theory and combinatorics.

**Definition.** Disparity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_disparity-backbone">details</a></td><td><code>disparity</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_disparity-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Fastball {#cat_fastball}

Measure id: `cat_fastball`. Original family: Graph theory and combinatorics.

**Definition.** Fastball.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_fastball-backbone">details</a></td><td><code>fastball</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_fastball-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Fdsm {#cat_fdsm}

Measure id: `cat_fdsm`. Original family: Graph theory and combinatorics.

**Definition.** Fdsm.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_fdsm-backbone">details</a></td><td><code>fdsm</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_fdsm-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Fixedcol {#cat_fixedcol}

Measure id: `cat_fixedcol`. Original family: Graph theory and combinatorics.

**Definition.** Fixedcol.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_fixedcol-backbone">details</a></td><td><code>fixedcol</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_fixedcol-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Fixedfill {#cat_fixedfill}

Measure id: `cat_fixedfill`. Original family: Graph theory and combinatorics.

**Definition.** Fixedfill.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_fixedfill-backbone">details</a></td><td><code>fixedfill</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_fixedfill-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Fixedrow {#cat_fixedrow}

Measure id: `cat_fixedrow`. Original family: Graph theory and combinatorics.

**Definition.** Fixedrow.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_fixedrow-backbone">details</a></td><td><code>fixedrow</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_fixedrow-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Lans {#cat_lans}

Measure id: `cat_lans`. Original family: Graph theory and combinatorics.

**Definition.** Lans.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_lans-backbone">details</a></td><td><code>lans</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_lans-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Mlf {#cat_mlf}

Measure id: `cat_mlf`. Original family: Graph theory and combinatorics.

**Definition.** Mlf.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_mlf-backbone">details</a></td><td><code>mlf</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mlf-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)

## Sdsm {#cat_sdsm}

Measure id: `cat_sdsm`. Original family: Graph theory and combinatorics.

**Definition.** Sdsm.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/backbone.html">backbone</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: backbone is documented-only in this survey; listed in its documentation. <a href="#why-cat_sdsm-backbone">details</a></td><td><code>sdsm</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sdsm-backbone"></a>**[backbone](../../tools/backbone.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. backbone (3.0.4) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of backbone 3.0.4: help topics.

**Tools cited:** [tool_backbone](../../references.html#tool_backbone)
{% endraw %}
