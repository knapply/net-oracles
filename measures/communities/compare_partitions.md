---
title: "Compare partitions"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Compare partitions {#concept-top}

Family: [Communities](index.html). Subfamily: Partition comparison and operations. Concept id: `compare_partitions`. 6 measures.

## Definition {#concept-definition}

Compare partitions. Entries grouped here: Compare partitions; Mutual information; Partition distance; Reduced mutual information; Same Community Index; Variation information.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Compare partitions](#compare_partitions) | `compare_partitions` | 4 |
| [Mutual information](#cat_information_mutual) | `cat_information_mutual` | 1 |
| [Partition distance](#cat_distance_partition) | `cat_distance_partition` | 1 |
| [Reduced mutual information](#cat_information_mutual_reduced) | `cat_information_mutual_reduced` | 1 |
| [Same Community Index](#cat_community_same) | `cat_community_same` | 1 |
| [Variation information](#cat_information_variation) | `cat_information_variation` | 1 |

## Compare partitions {#compare_partitions}

Measure id: `compare_partitions`. Original family: Communities.

**Definition.** Compare partitions.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0. [details](#why-compare_partitions-igraph) | `compare; split_join_distance` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-compare_partitions-pyigraph) | `compare_communities; split_join_distance` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-compare_partitions-networkit) | `AdjustedRandIndex; AdjustedRandMeasure; GraphStructuralRandMeasure; JaccardMeasure; NMIDistance; NodeStructuralRandMeasure; OverlappingNMIDistance; compareCommunities` | API listing |
| [cdlib](../../tools/cdlib.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): For partitions of one element cdlib (through scikit-learn) returns 1.0. [details](#why-compare_partitions-cdlib) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-compare_partitions-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults) on inputs tagged two\_nodes. on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0; the reference reports 1, the value for every other pair of identical partitions (as scikit-learn's adjusted\_rand\_score() does), and igraph NaN. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (compare\_nmi) on inputs tagged null\_graph: Two partitions of no nodes: the reference reports undefined, igraph a value. No value (compare\_rand) on the fixtures single\_node: igraph raises an error for fewer than two nodes; the reference reports NaN. No value (compare\_split\_join) on inputs tagged null\_graph: Two partitions of no nodes: the reference reports undefined, igraph a value. No value (compare\_vi) on inputs tagged null\_graph: Two partitions of no nodes: the reference reports undefined, igraph a value. 1 comparisons differ and 137 agree. Finding F036 (convention): Adjusted Rand index is NaN on all-singleton partitions. Findings: [F036](../../findings.html#f036).
- <a id="why-compare_partitions-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: compare\_communities; split\_join\_distance.
- <a id="why-compare_partitions-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AdjustedRandIndex; AdjustedRandMeasure; GraphStructuralRandMeasure; JaccardMeasure; NMIDistance; NodeStructuralRandMeasure; OverlappingNMIDistance; compareCommunities.
- <a id="why-compare_partitions-cdlib"></a>**[cdlib](../../tools/cdlib.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> cdlib 0.4.1 was run and its value differs from the reference value by convention (defaults) on the fixtures single\_node. For partitions of one element cdlib (through scikit-learn) returns 1.0; the adjusted Rand index is 0/0 there, and the reference, like igraph, reports it undefined. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 1 comparisons differ and 139 agree. Finding F037 (convention): Adjusted Rand index is 1 on degenerate partitions. Findings: [F037](../../findings.html#f037).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `compare_adjusted_rand` | igraph (R) | any | differs | two\_nodes, (no value) null\_graph, (no value) one\_node | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'adjusted.rand')` | on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0; the reference reports 1, the value for every other pair of identical partitions (as scikit-learn's adjusted\_rand\_score() does), and igraph NaN igraph raises an error for fewer than two nodes; the reference reports NaN. |
| `compare_adjusted_rand` | cdlib | any | differs |  | defaults | abs 1e-14, rel 1e-12 | `cdlib.evaluation.adjusted_rand_index(blocks, stripes)` | For partitions of one element cdlib (through scikit-learn) returns 1.0; the adjusted Rand index is 0/0 there, and the reference, like igraph, reports it undefined. |
| `compare_ami` | cdlib | any | agrees |  |  | abs 1e-12, rel 1e-09 | `cdlib.evaluation.adjusted_mutual_information(blocks, stripes)` |  |
| `compare_nmi` | igraph (R) | any | no-value-on-some-inputs | (no value) null\_graph | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'nmi')` | Two partitions of no nodes: the reference reports undefined, igraph a value. |
| `compare_nmi` | cdlib | any | agrees |  |  | abs 1e-14, rel 1e-12 | `cdlib.evaluation.normalized_mutual_information(blocks, stripes)` |  |
| `compare_rand` | igraph (R) | any | no-value-on-some-inputs |  | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'rand')` | igraph raises an error for fewer than two nodes; the reference reports NaN. |
| `compare_rand` | cdlib | any | agrees |  |  | abs 1e-14, rel 1e-12 | `cdlib.evaluation.rand_index(blocks, stripes)` |  |
| `compare_split_join` | igraph (R) | any | no-value-on-some-inputs | (no value) null\_graph | defaults | abs 0, rel 0 | `sum(split_join_distance(a, b))` | Two partitions of no nodes: the reference reports undefined, igraph a value. |
| `compare_vi` | igraph (R) | any | no-value-on-some-inputs | (no value) null\_graph | defaults | abs 1e-14, rel 1e-12 | `compare(a, b, method = 'vi')` | Two partitions of no nodes: the reference reports undefined, igraph a value. |
| `compare_vi` | cdlib | any | agrees |  |  | abs 1e-14, rel 1e-12 | `cdlib.evaluation.variation_of_information(blocks, stripes)` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F036](../../findings.html#f036) | igraph (R) | convention | Adjusted Rand index is NaN on all-singleton partitions |
| [F037](../../findings.html#f037) | cdlib | convention | Adjusted Rand index is 1 on degenerate partitions |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_cdlib](../../references.html#tool_cdlib)

## Mutual information {#cat_information_mutual}

Measure id: `cat_information_mutual`. Original family: Generators and rewiring.

**Definition.** Mutual information.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_information_mutual-graphtool) | `mutual_information` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_information_mutual-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: mutual\_information.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Partition distance {#cat_distance_partition}

Measure id: `cat_distance_partition`. Original family: Communities.

**Definition.** Partition distance.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_distance_partition-bct) | `partition_distance` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_distance_partition-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: partition\_distance.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)

## Reduced mutual information {#cat_information_mutual_reduced}

Measure id: `cat_information_mutual_reduced`. Original family: Generators and rewiring.

**Definition.** Reduced mutual information.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_information_mutual_reduced-graphtool) | `reduced_mutual_information` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_information_mutual_reduced-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: reduced\_mutual\_information.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Same Community Index {#cat_community_same}

Measure id: `cat_community_same`. Original family: Communities.

**Definition.** Same Community Index.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_community_same-networkit) | `SameCommunityIndex` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_community_same-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SameCommunityIndex.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Variation information {#cat_information_variation}

Measure id: `cat_information_variation`. Original family: Generators and rewiring.

**Definition.** Variation information.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_information_variation-graphtool) | `variation_information` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_information_variation-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: variation\_information.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
