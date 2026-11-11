---
title: "Dedensify and compression"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Dedensify and compression {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `dedensify`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\theta\)</td><td>degree threshold for 'high-degree' nodes</td></tr><tr><td>\(P(S)\)</td><td>set of high-degree neighbours shared by a group \(S\) of low-degree nodes</td></tr><tr><td>\(\mathcal B\)</td><td>a partition into blocks</td></tr><tr><td>\(E(B)\)</td><td>edges with both ends in block \(B\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Dedensify and compression. Entries grouped here: Dedensify; Quotient internal; Snap groups.

<div class="formula-block"><p class="formula-name"><strong>Dedensification (Maccioni and Abadi 2016)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\text{replace the edges between }S\text{ and }P(S)\text{ by a compressor node}\ \text{iff}\ |S|\,|P(S)|&gt;|S|+|P(S)|\]</div><p class="formula-where">Low-degree nodes that point to the same set of high-degree nodes are grouped; a compressor node replaces the \(|S||P|\) edges by \(|S|+|P|\) edges when that saves edges.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Edges inside blocks (quotient graph)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{nedges}(B)=\bigl|\{uv\in E:\ u,v\in B\}\bigr|\]</div><p class="formula-where">Number of edges with both ends in block \(B\) of the quotient graph.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Attribute-relation aggregation (Tian, Hankins and Patel 2008)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[u\sim v\Rightarrow a(u)=a(v)\ \wedge\ \forall B':\ (N(u)\cap B'\ne\emptyset\iff N(v)\cap B'\neq\emptyset)\]</div><p class="formula-where">The coarsest partition whose blocks agree on the node attributes and whose members have neighbours in the same blocks (the SNAP summary); it refines the attribute classes until stable.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gb_dedensify">Dedensify</a></td><td><code>gb_dedensify</code></td><td>1</td><td>The number of compressor nodes (groups) created for a degree threshold.</td></tr><tr><td><a href="#gb_quotient_internal">Quotient internal</a></td><td><code>gb_quotient_internal</code></td><td>1</td><td>The number of edges inside each block of a quotient graph.</td></tr><tr><td><a href="#gb_snap_groups">Snap groups</a></td><td><code>gb_snap_groups</code></td><td>1</td><td>The number of groups of the coarsest attribute-compatible refinement, here with degree parity as the attribute.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No groups.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No edges to compress; one block per attribute class.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop lies inside its node's block.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges count in \(\mathrm{nedges}\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Dedensification groups nodes by their out-neighbours.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">The threshold \(\theta\) decides which nodes are high-degree; \(\theta\ge\) the maximum degree leaves nothing to compress.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Dedensify {#gb_dedensify}

Measure id: `gb_dedensify`. Original family: Traversal, trees and DAGs.

**Definition.** Dedensify.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>dedensify</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_dedensify</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.dedensify(M, 2)[1])</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/traversal_b.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/traversal_b.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Quotient internal {#gb_quotient_internal}

Measure id: `gb_quotient_internal`. Original family: Traversal, trees and DAGs.

**Definition.** Quotient internal.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_quotient_internal</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nedges of each block of nx.quotient_graph(M, parts)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/traversal_b.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/traversal_b.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Snap groups {#gb_snap_groups}

Measure id: `gb_snap_groups`. Original family: Traversal, trees and DAGs.

**Definition.** Snap groups.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>snap_aggregation</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_snap_groups</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.snap_aggregation(M, node_attributes=('parity',)).number_of_nodes()</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/traversal_b.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/traversal_b.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
