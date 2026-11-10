---
title: "Partition quality (coverage, performance)"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Partition quality (coverage, performance) {#concept-top}

Family: [Communities](index.html). Subfamily: Partition and cover quality. Concept id: `partition_quality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(m_{\mathrm{in}}\)</td><td>number of edges inside communities</td></tr><tr><td>\(m_{\mathrm{out}}\)</td><td>number of non-edges between communities (pairs in different communities without an edge)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Partition quality (coverage, performance). Entries grouped here: Partition quality (coverage, performance).

*Definition partly written:* Documented only (NetworKit, NetworkX), never run. The formulas are the usual coverage and performance of a partition, stated from the NetworkX documentation; the original papers are not in the bibliography, so no citation is given.

<div class="formula-block"><p class="formula-name"><strong>Coverage</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\mathrm{cov}=\frac{m_{\mathrm{in}}}{m}\]</div><p class="formula-where">Fraction of edges that are intra-community; defined for \(m&gt;0\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Performance</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\mathrm{perf}=\frac{m_{\mathrm{in}}+m_{\mathrm{out}}}{\binom n2}\]</div><p class="formula-where">Fraction of node pairs that are correctly classified: intra-community edges plus inter-community non-edges over all pairs; defined for \(n\ge2\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#partition_quality">Partition quality (coverage, performance)</a></td><td><code>partition_quality</code></td><td>2</td><td>The coverage and the performance of a partition.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/networkit.html">NetworKit</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Coverage 0/0: not defined; performance 1 for \(n\ge2\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Performance: \(\binom12=0\): not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Not between distinct nodes: excluded in the simple reading.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Merged in the simple reading.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Stated for undirected graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">One community gives coverage 1 and performance 1.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">A partition must cover every node exactly once.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details></div>

## Partition quality (coverage, performance) {#partition_quality}

Measure id: `partition_quality`. Original family: Communities.

**Definition.** Partition quality (coverage, performance).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-partition_quality-networkx">details</a></td><td><code>partition_quality</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-partition_quality-networkit">details</a></td><td><code>Coverage</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-partition_quality-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: partition\_quality.
- <a id="why-partition_quality-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: Coverage.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
