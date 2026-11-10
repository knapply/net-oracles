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

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#compare_partitions">Compare partitions</a></td><td><code>compare_partitions</code></td><td>4</td></tr><tr><td><a href="#cat_information_mutual">Mutual information</a></td><td><code>cat_information_mutual</code></td><td>1</td></tr><tr><td><a href="#cat_distance_partition">Partition distance</a></td><td><code>cat_distance_partition</code></td><td>1</td></tr><tr><td><a href="#cat_information_mutual_reduced">Reduced mutual information</a></td><td><code>cat_information_mutual_reduced</code></td><td>1</td></tr><tr><td><a href="#cat_community_same">Same Community Index</a></td><td><code>cat_community_same</code></td><td>1</td></tr><tr><td><a href="#cat_information_variation">Variation information</a></td><td><code>cat_information_variation</code></td><td>1</td></tr></tbody></table></div>

## Compare partitions {#compare_partitions}

Measure id: `compare_partitions`. Original family: Communities.

**Definition.** Compare partitions.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults): on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0. <a href="#why-compare_partitions-igraph">details</a></td><td><code>compare; split_join_distance</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-compare_partitions-pyigraph">details</a></td><td><code>compare_communities; split_join_distance</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-compare_partitions-networkit">details</a></td><td><code>AdjustedRandIndex; AdjustedRandMeasure; GraphStructuralRandMeasure; JaccardMeasure; NMIDistance; NodeStructuralRandMeasure; OverlappingNMIDistance; compareCommunities</code></td><td>API listing</td></tr><tr><td><a href="../../tools/cdlib.html">cdlib</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults): For partitions of one element cdlib (through scikit-learn) returns 1.0. <a href="#why-compare_partitions-cdlib">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-compare_partitions-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults) on inputs tagged two\_nodes. on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0; the reference reports 1, the value for every other pair of identical partitions (as scikit-learn's adjusted\_rand\_score() does), and igraph NaN. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (compare\_nmi) on inputs tagged null\_graph: Two partitions of no nodes: the reference reports undefined, igraph a value. No value (compare\_rand) on the fixtures single\_node: igraph raises an error for fewer than two nodes; the reference reports NaN. No value (compare\_split\_join) on inputs tagged null\_graph: Two partitions of no nodes: the reference reports undefined, igraph a value. No value (compare\_vi) on inputs tagged null\_graph: Two partitions of no nodes: the reference reports undefined, igraph a value. 1 comparisons differ and 137 agree. Finding F036 (convention): Adjusted Rand index is NaN on all-singleton partitions. Findings: [F036](../../findings.html#f036).
- <a id="why-compare_partitions-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: compare\_communities; split\_join\_distance.
- <a id="why-compare_partitions-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AdjustedRandIndex; AdjustedRandMeasure; GraphStructuralRandMeasure; JaccardMeasure; NMIDistance; NodeStructuralRandMeasure; OverlappingNMIDistance; compareCommunities.
- <a id="why-compare_partitions-cdlib"></a>**[cdlib](../../tools/cdlib.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> cdlib 0.4.1 was run and its value differs from the reference value by convention (defaults) on the fixtures single\_node. For partitions of one element cdlib (through scikit-learn) returns 1.0; the adjusted Rand index is 0/0 there, and the reference, like igraph, reports it undefined. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 1 comparisons differ and 139 agree. Finding F037 (convention): Adjusted Rand index is 1 on degenerate partitions. Findings: [F037](../../findings.html#f037).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>compare_adjusted_rand</code></td><td>igraph (R)</td><td>any</td><td>differs</td><td>two_nodes, (no value) null_graph, (no value) one_node</td><td>defaults</td><td>abs 1e-14, rel 1e-12</td><td><code>compare(a, b, method = 'adjusted.rand')</code></td><td>on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0; the reference reports 1, the value for every other pair of identical partitions (as scikit-learn's adjusted_rand_score() does), and igraph NaN igraph raises an error for fewer than two nodes; the reference reports NaN.</td></tr><tr><td><code>compare_adjusted_rand</code></td><td>cdlib</td><td>any</td><td>differs</td><td></td><td>defaults</td><td>abs 1e-14, rel 1e-12</td><td><code>cdlib.evaluation.adjusted_rand_index(blocks, stripes)</code></td><td>For partitions of one element cdlib (through scikit-learn) returns 1.0; the adjusted Rand index is 0/0 there, and the reference, like igraph, reports it undefined.</td></tr><tr><td><code>compare_ami</code></td><td>cdlib</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>cdlib.evaluation.adjusted_mutual_information(blocks, stripes)</code></td><td></td></tr><tr><td><code>compare_nmi</code></td><td>igraph (R)</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) null_graph</td><td>defaults</td><td>abs 1e-14, rel 1e-12</td><td><code>compare(a, b, method = 'nmi')</code></td><td>Two partitions of no nodes: the reference reports undefined, igraph a value.</td></tr><tr><td><code>compare_nmi</code></td><td>cdlib</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>cdlib.evaluation.normalized_mutual_information(blocks, stripes)</code></td><td></td></tr><tr><td><code>compare_rand</code></td><td>igraph (R)</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td>defaults</td><td>abs 1e-14, rel 1e-12</td><td><code>compare(a, b, method = 'rand')</code></td><td>igraph raises an error for fewer than two nodes; the reference reports NaN.</td></tr><tr><td><code>compare_rand</code></td><td>cdlib</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>cdlib.evaluation.rand_index(blocks, stripes)</code></td><td></td></tr><tr><td><code>compare_split_join</code></td><td>igraph (R)</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) null_graph</td><td>defaults</td><td>abs 0, rel 0</td><td><code>sum(split_join_distance(a, b))</code></td><td>Two partitions of no nodes: the reference reports undefined, igraph a value.</td></tr><tr><td><code>compare_vi</code></td><td>igraph (R)</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) null_graph</td><td>defaults</td><td>abs 1e-14, rel 1e-12</td><td><code>compare(a, b, method = 'vi')</code></td><td>Two partitions of no nodes: the reference reports undefined, igraph a value.</td></tr><tr><td><code>compare_vi</code></td><td>cdlib</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>cdlib.evaluation.variation_of_information(blocks, stripes)</code></td><td></td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f036">F036</a></td><td>igraph (R)</td><td>convention</td><td>Adjusted Rand index is NaN on all-singleton partitions</td></tr><tr><td><a href="../../findings.html#f037">F037</a></td><td>cdlib</td><td>convention</td><td>Adjusted Rand index is 1 on degenerate partitions</td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_cdlib](../../references.html#tool_cdlib)

## Mutual information {#cat_information_mutual}

Measure id: `cat_information_mutual`. Original family: Generators and rewiring.

**Definition.** Mutual information.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_information_mutual-graphtool">details</a></td><td><code>mutual_information</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_information_mutual-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: mutual\_information.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Partition distance {#cat_distance_partition}

Measure id: `cat_distance_partition`. Original family: Communities.

**Definition.** Partition distance.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_distance_partition-bct">details</a></td><td><code>partition_distance</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_distance_partition-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: partition\_distance.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)

## Reduced mutual information {#cat_information_mutual_reduced}

Measure id: `cat_information_mutual_reduced`. Original family: Generators and rewiring.

**Definition.** Reduced mutual information.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_information_mutual_reduced-graphtool">details</a></td><td><code>reduced_mutual_information</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_information_mutual_reduced-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: reduced\_mutual\_information.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Same Community Index {#cat_community_same}

Measure id: `cat_community_same`. Original family: Communities.

**Definition.** Same Community Index.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_community_same-networkit">details</a></td><td><code>SameCommunityIndex</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_community_same-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SameCommunityIndex.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Variation information {#cat_information_variation}

Measure id: `cat_information_variation`. Original family: Generators and rewiring.

**Definition.** Variation information.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_information_variation-graphtool">details</a></td><td><code>variation_information</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_information_variation-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: variation\_information.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
