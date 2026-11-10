---
title: "Graph sparsification (score-based edge filtering)"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph sparsification (score-based edge filtering) {#concept-top}

Family: [Data transforms](index.html). Subfamily: Sparsification and backbones. Concept id: `graph_sparsification`. 16 measures.

## Definition {#concept-definition}

Graph sparsification (score-based edge filtering). Entries grouped here: Algebraic Distance Sparsifier; Degree Multiscale Sparsifier; Forest Fire Sparsifier; Global Threshold Filter; Jaccard Similarity Sparsifier; Local Degree Sparsifier; and 10 more.

*Definition not yet written.* The sources list sixteen score-based edge-filtering procedures and L-Spar (Local Degree, Forest Fire, SCAN, Simmelian, Jaccard, algebraic distance, global threshold and others) as documented-only entries by name; none of the original papers is among the checked sources, so no formula is written.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_algebraic_distance_sparsifier">Algebraic Distance Sparsifier</a></td><td><code>cat_algebraic_distance_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_degree_multiscale_sparsifier">Degree Multiscale Sparsifier</a></td><td><code>cat_degree_multiscale_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_fire_forest_sparsifier">Forest Fire Sparsifier</a></td><td><code>cat_fire_forest_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_filter_global_threshold">Global Threshold Filter</a></td><td><code>cat_filter_global_threshold</code></td><td>1</td></tr><tr><td><a href="#cat_jaccard_similarity_sparsifier">Jaccard Similarity Sparsifier</a></td><td><code>cat_jaccard_similarity_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_degree_local_sparsifier">Local Degree Sparsifier</a></td><td><code>cat_degree_local_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_local_similarity_sparsifier">Local Similarity Sparsifier</a></td><td><code>cat_local_similarity_sparsifier</code></td><td>1</td></tr><tr><td><a href="#local_sparsification">Local sparsification (L-Spar)</a></td><td><code>local_sparsification</code></td><td>1</td></tr><tr><td><a href="#cat_multiscale_sparsifier">Multiscale Sparsifier</a></td><td><code>cat_multiscale_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_quadrilateral_simmelian_sparsifier">Quadrilateral Simmelian Sparsifier</a></td><td><code>cat_quadrilateral_simmelian_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_edge_random_sparsifier">Random Edge Sparsifier</a></td><td><code>cat_edge_random_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_scan_sparsifier">SCANSparsifier</a></td><td><code>cat_scan_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_multiscale_simmelian_sparsifier">Simmelian Multiscale Sparsifier</a></td><td><code>cat_multiscale_simmelian_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_non_parametric_simmelian_sparsifier">Simmelian Sparsifier Non Parametric</a></td><td><code>cat_non_parametric_simmelian_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_parametric_simmelian_sparsifier">Simmelian Sparsifier Parametric</a></td><td><code>cat_parametric_simmelian_sparsifier</code></td><td>1</td></tr><tr><td><a href="#cat_sparsifier_triangle">Triangle Sparsifier</a></td><td><code>cat_sparsifier_triangle</code></td><td>1</td></tr></tbody></table></div>

## Algebraic Distance Sparsifier {#cat_algebraic_distance_sparsifier}

Measure id: `cat_algebraic_distance_sparsifier`. Original family: Paths and distances.

**Definition.** Algebraic Distance Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_algebraic_distance_sparsifier-networkit">details</a></td><td><code>AlgebraicDistanceSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_algebraic_distance_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AlgebraicDistanceSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Degree Multiscale Sparsifier {#cat_degree_multiscale_sparsifier}

Measure id: `cat_degree_multiscale_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Degree Multiscale Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_degree_multiscale_sparsifier-networkit">details</a></td><td><code>DegreeMultiscaleSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_multiscale_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: DegreeMultiscaleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Forest Fire Sparsifier {#cat_fire_forest_sparsifier}

Measure id: `cat_fire_forest_sparsifier`. Original family: Generators and rewiring.

**Definition.** Forest Fire Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_fire_forest_sparsifier-networkit">details</a></td><td><code>ForestFireSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_fire_forest_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ForestFireSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Global Threshold Filter {#cat_filter_global_threshold}

Measure id: `cat_filter_global_threshold`. Original family: Graph theory and combinatorics.

**Definition.** Global Threshold Filter.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_filter_global_threshold-networkit">details</a></td><td><code>GlobalThresholdFilter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_filter_global_threshold-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: GlobalThresholdFilter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Jaccard Similarity Sparsifier {#cat_jaccard_similarity_sparsifier}

Measure id: `cat_jaccard_similarity_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Jaccard Similarity Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_jaccard_similarity_sparsifier-networkit">details</a></td><td><code>JaccardSimilaritySparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_jaccard_similarity_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: JaccardSimilaritySparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Local Degree Sparsifier {#cat_degree_local_sparsifier}

Measure id: `cat_degree_local_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Local Degree Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_degree_local_sparsifier-networkit">details</a></td><td><code>LocalDegreeSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_local_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LocalDegreeSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Local Similarity Sparsifier {#cat_local_similarity_sparsifier}

Measure id: `cat_local_similarity_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Local Similarity Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_local_similarity_sparsifier-networkit">details</a></td><td><code>LocalSimilaritySparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_local_similarity_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LocalSimilaritySparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Local sparsification (L-Spar) {#local_sparsification}

Measure id: `local_sparsification`. Original family: Data transforms.

**Definition.** Local sparsification (L-Spar).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-local_sparsification-ucinet">details</a></td><td><code>Local sparsification (6.831); lspar</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-local_sparsification-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Multiscale Sparsifier {#cat_multiscale_sparsifier}

Measure id: `cat_multiscale_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Multiscale Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_multiscale_sparsifier-networkit">details</a></td><td><code>MultiscaleSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_multiscale_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: MultiscaleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Quadrilateral Simmelian Sparsifier {#cat_quadrilateral_simmelian_sparsifier}

Measure id: `cat_quadrilateral_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Quadrilateral Simmelian Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_quadrilateral_simmelian_sparsifier-networkit">details</a></td><td><code>QuadrilateralSimmelianSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_quadrilateral_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: QuadrilateralSimmelianSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Random Edge Sparsifier {#cat_edge_random_sparsifier}

Measure id: `cat_edge_random_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Random Edge Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_edge_random_sparsifier-networkit">details</a></td><td><code>RandomEdgeSparsifier; RandomNodeEdgeSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_edge_random_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: RandomEdgeSparsifier; RandomNodeEdgeSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## SCANSparsifier {#cat_scan_sparsifier}

Measure id: `cat_scan_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** SCANSparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_scan_sparsifier-networkit">details</a></td><td><code>SCANSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_scan_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SCANSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Simmelian Multiscale Sparsifier {#cat_multiscale_simmelian_sparsifier}

Measure id: `cat_multiscale_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Simmelian Multiscale Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_multiscale_simmelian_sparsifier-networkit">details</a></td><td><code>SimmelianMultiscaleSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_multiscale_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SimmelianMultiscaleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Simmelian Sparsifier Non Parametric {#cat_non_parametric_simmelian_sparsifier}

Measure id: `cat_non_parametric_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Simmelian Sparsifier Non Parametric.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_non_parametric_simmelian_sparsifier-networkit">details</a></td><td><code>SimmelianSparsifierNonParametric</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_non_parametric_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SimmelianSparsifierNonParametric.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Simmelian Sparsifier Parametric {#cat_parametric_simmelian_sparsifier}

Measure id: `cat_parametric_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Simmelian Sparsifier Parametric.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_parametric_simmelian_sparsifier-networkit">details</a></td><td><code>SimmelianSparsifierParametric</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_parametric_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SimmelianSparsifierParametric.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Triangle Sparsifier {#cat_sparsifier_triangle}

Measure id: `cat_sparsifier_triangle`. Original family: Graph theory and combinatorics.

**Definition.** Triangle Sparsifier.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_sparsifier_triangle-networkit">details</a></td><td><code>TriangleSparsifier</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sparsifier_triangle-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: TriangleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
