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

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Algebraic Distance Sparsifier](#cat_algebraic_distance_sparsifier) | `cat_algebraic_distance_sparsifier` | 1 |
| [Degree Multiscale Sparsifier](#cat_degree_multiscale_sparsifier) | `cat_degree_multiscale_sparsifier` | 1 |
| [Forest Fire Sparsifier](#cat_fire_forest_sparsifier) | `cat_fire_forest_sparsifier` | 1 |
| [Global Threshold Filter](#cat_filter_global_threshold) | `cat_filter_global_threshold` | 1 |
| [Jaccard Similarity Sparsifier](#cat_jaccard_similarity_sparsifier) | `cat_jaccard_similarity_sparsifier` | 1 |
| [Local Degree Sparsifier](#cat_degree_local_sparsifier) | `cat_degree_local_sparsifier` | 1 |
| [Local Similarity Sparsifier](#cat_local_similarity_sparsifier) | `cat_local_similarity_sparsifier` | 1 |
| [Local sparsification (L-Spar)](#local_sparsification) | `local_sparsification` | 1 |
| [Multiscale Sparsifier](#cat_multiscale_sparsifier) | `cat_multiscale_sparsifier` | 1 |
| [Quadrilateral Simmelian Sparsifier](#cat_quadrilateral_simmelian_sparsifier) | `cat_quadrilateral_simmelian_sparsifier` | 1 |
| [Random Edge Sparsifier](#cat_edge_random_sparsifier) | `cat_edge_random_sparsifier` | 1 |
| [SCANSparsifier](#cat_scan_sparsifier) | `cat_scan_sparsifier` | 1 |
| [Simmelian Multiscale Sparsifier](#cat_multiscale_simmelian_sparsifier) | `cat_multiscale_simmelian_sparsifier` | 1 |
| [Simmelian Sparsifier Non Parametric](#cat_non_parametric_simmelian_sparsifier) | `cat_non_parametric_simmelian_sparsifier` | 1 |
| [Simmelian Sparsifier Parametric](#cat_parametric_simmelian_sparsifier) | `cat_parametric_simmelian_sparsifier` | 1 |
| [Triangle Sparsifier](#cat_sparsifier_triangle) | `cat_sparsifier_triangle` | 1 |

## Algebraic Distance Sparsifier {#cat_algebraic_distance_sparsifier}

Measure id: `cat_algebraic_distance_sparsifier`. Original family: Paths and distances.

**Definition.** Algebraic Distance Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_algebraic_distance_sparsifier-networkit) | `AlgebraicDistanceSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_algebraic_distance_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AlgebraicDistanceSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Degree Multiscale Sparsifier {#cat_degree_multiscale_sparsifier}

Measure id: `cat_degree_multiscale_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Degree Multiscale Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degree_multiscale_sparsifier-networkit) | `DegreeMultiscaleSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_multiscale_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: DegreeMultiscaleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Forest Fire Sparsifier {#cat_fire_forest_sparsifier}

Measure id: `cat_fire_forest_sparsifier`. Original family: Generators and rewiring.

**Definition.** Forest Fire Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_fire_forest_sparsifier-networkit) | `ForestFireSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_fire_forest_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ForestFireSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Global Threshold Filter {#cat_filter_global_threshold}

Measure id: `cat_filter_global_threshold`. Original family: Graph theory and combinatorics.

**Definition.** Global Threshold Filter.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_filter_global_threshold-networkit) | `GlobalThresholdFilter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_filter_global_threshold-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: GlobalThresholdFilter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Jaccard Similarity Sparsifier {#cat_jaccard_similarity_sparsifier}

Measure id: `cat_jaccard_similarity_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Jaccard Similarity Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_jaccard_similarity_sparsifier-networkit) | `JaccardSimilaritySparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_jaccard_similarity_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: JaccardSimilaritySparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Local Degree Sparsifier {#cat_degree_local_sparsifier}

Measure id: `cat_degree_local_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Local Degree Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degree_local_sparsifier-networkit) | `LocalDegreeSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_local_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LocalDegreeSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Local Similarity Sparsifier {#cat_local_similarity_sparsifier}

Measure id: `cat_local_similarity_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Local Similarity Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_local_similarity_sparsifier-networkit) | `LocalSimilaritySparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_local_similarity_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LocalSimilaritySparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Local sparsification (L-Spar) {#local_sparsification}

Measure id: `local_sparsification`. Original family: Data transforms.

**Definition.** Local sparsification (L-Spar).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-local_sparsification-ucinet) | `Local sparsification (6.831); lspar` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-local_sparsification-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Multiscale Sparsifier {#cat_multiscale_sparsifier}

Measure id: `cat_multiscale_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Multiscale Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_multiscale_sparsifier-networkit) | `MultiscaleSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_multiscale_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: MultiscaleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Quadrilateral Simmelian Sparsifier {#cat_quadrilateral_simmelian_sparsifier}

Measure id: `cat_quadrilateral_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Quadrilateral Simmelian Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_quadrilateral_simmelian_sparsifier-networkit) | `QuadrilateralSimmelianSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_quadrilateral_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: QuadrilateralSimmelianSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Random Edge Sparsifier {#cat_edge_random_sparsifier}

Measure id: `cat_edge_random_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Random Edge Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_edge_random_sparsifier-networkit) | `RandomEdgeSparsifier; RandomNodeEdgeSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_edge_random_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: RandomEdgeSparsifier; RandomNodeEdgeSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## SCANSparsifier {#cat_scan_sparsifier}

Measure id: `cat_scan_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** SCANSparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_scan_sparsifier-networkit) | `SCANSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_scan_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SCANSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Simmelian Multiscale Sparsifier {#cat_multiscale_simmelian_sparsifier}

Measure id: `cat_multiscale_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Simmelian Multiscale Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_multiscale_simmelian_sparsifier-networkit) | `SimmelianMultiscaleSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_multiscale_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SimmelianMultiscaleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Simmelian Sparsifier Non Parametric {#cat_non_parametric_simmelian_sparsifier}

Measure id: `cat_non_parametric_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Simmelian Sparsifier Non Parametric.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_non_parametric_simmelian_sparsifier-networkit) | `SimmelianSparsifierNonParametric` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_non_parametric_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SimmelianSparsifierNonParametric.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Simmelian Sparsifier Parametric {#cat_parametric_simmelian_sparsifier}

Measure id: `cat_parametric_simmelian_sparsifier`. Original family: Graph theory and combinatorics.

**Definition.** Simmelian Sparsifier Parametric.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_parametric_simmelian_sparsifier-networkit) | `SimmelianSparsifierParametric` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_parametric_simmelian_sparsifier-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SimmelianSparsifierParametric.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Triangle Sparsifier {#cat_sparsifier_triangle}

Measure id: `cat_sparsifier_triangle`. Original family: Graph theory and combinatorics.

**Definition.** Triangle Sparsifier.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_sparsifier_triangle-networkit) | `TriangleSparsifier` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sparsifier_triangle-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: TriangleSparsifier.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
