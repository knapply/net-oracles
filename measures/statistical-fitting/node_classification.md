---
title: "Node classification"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Node classification {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Prediction and classification. Concept id: `node_classification`. 6 measures.

## Definition {#concept-definition}

Node classification. Entries grouped here: Diffusion Classifier; GNNClassifier; NNClassifier; Page Rank Classifier; Propagation; Rank Classifier.

*Definition not yet written.* Documented by name only; the sources record the tool function or effect name and no definition, and no primary paper was checked.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_classifier_diffusion">Diffusion Classifier</a></td><td><code>cat_classifier_diffusion</code></td><td>1</td></tr><tr><td><a href="#cat_classifier_gnn">GNNClassifier</a></td><td><code>cat_classifier_gnn</code></td><td>1</td></tr><tr><td><a href="#cat_classifier_nn">NNClassifier</a></td><td><code>cat_classifier_nn</code></td><td>1</td></tr><tr><td><a href="#cat_classifier_page_rank">Page Rank Classifier</a></td><td><code>cat_classifier_page_rank</code></td><td>1</td></tr><tr><td><a href="#cat_propagation">Propagation</a></td><td><code>cat_propagation</code></td><td>1</td></tr><tr><td><a href="#cat_classifier_rank">Rank Classifier</a></td><td><code>cat_classifier_rank</code></td><td>1</td></tr></tbody></table></div>

## Diffusion Classifier {#cat_classifier_diffusion}

Measure id: `cat_classifier_diffusion`. Original family: Centrality.

**Definition.** Diffusion Classifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_classifier_diffusion-sknetwork">details</a></td><td><code>DiffusionClassifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_classifier_diffusion-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: DiffusionClassifier.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)

## GNNClassifier {#cat_classifier_gnn}

Measure id: `cat_classifier_gnn`. Original family: Mixing and assortativity.

**Definition.** GNNClassifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_classifier_gnn-sknetwork">details</a></td><td><code>GNNClassifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_classifier_gnn-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: GNNClassifier.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)

## NNClassifier {#cat_classifier_nn}

Measure id: `cat_classifier_nn`. Original family: Mixing and assortativity.

**Definition.** NNClassifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_classifier_nn-sknetwork">details</a></td><td><code>NNClassifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_classifier_nn-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: NNClassifier.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)

## Page Rank Classifier {#cat_classifier_page_rank}

Measure id: `cat_classifier_page_rank`. Original family: Centrality.

**Definition.** Page Rank Classifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_classifier_page_rank-sknetwork">details</a></td><td><code>PageRankClassifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_classifier_page_rank-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: PageRankClassifier.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)

## Propagation {#cat_propagation}

Measure id: `cat_propagation`. Original family: Graph theory and combinatorics.

**Definition.** Propagation.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_propagation-sknetwork">details</a></td><td><code>Propagation</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_propagation-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Propagation.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)

## Rank Classifier {#cat_classifier_rank}

Measure id: `cat_classifier_rank`. Original family: Mixing and assortativity.

**Definition.** Rank Classifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_classifier_rank-sknetwork">details</a></td><td><code>RankClassifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_classifier_rank-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: RankClassifier.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
