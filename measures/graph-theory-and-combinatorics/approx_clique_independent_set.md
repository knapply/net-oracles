---
title: "Approximate clique and independent set (Ramsey, clique removal)"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Approximate clique and independent set (Ramsey, clique removal) {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `approx_clique_independent_set`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\omega(G),\ \alpha(G)\)</td><td>clique number and independence number</td></tr><tr><td>\((C,I)\)</td><td>a clique and an independent set returned together</td></tr></tbody></table></div>

## Definition {#concept-definition}

Ramsey-based clique removal: a large independent set and the disjoint cliques removed.

<div class="formula-block"><p class="formula-name"><strong>Ramsey procedure (Boppana and Halldorsson 1992)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{Ram}(G)=\bigl(\text{larger clique of }C_1\cup\{v\},C_2;\ \text{larger independent set of }I_1,\ I_2\cup\{v\}\bigr),\ (C_1,I_1)=\mathrm{Ram}(G[N(v)]),\ (C_2,I_2)=\mathrm{Ram}(G[V\setminus N[v]])\]</div><p class="formula-where">Pick a node \(v\), recurse on its neighbours and on its non-neighbours, and combine; Ramsey's theorem guarantees a clique or an independent set of size \(\Omega(\log n)\); and \(\mathrm{Ram}(\emptyset)=(\emptyset,\emptyset)\). The choice of \(v\) is arbitrary and changes the output.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Clique removal</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\text{repeat: }(C,I)=\mathrm{Ram}(G);\ \text{record }C;\ G\leftarrow G-C;\qquad \text{output the largest }I\text{ seen}\]</div><p class="formula-where">Removes disjoint cliques one at a time and returns a large independent set together with the cliques removed; approximation factor \(O(n/\log^2n)\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Greedy clique size bound</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\text{start from a node of largest degree; keep adding the candidate of largest degree among common neighbours}\]</div><p class="formula-where">A lower bound on \(\omega(G)\) that is exact only when the start node lies in a largest clique.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ap_clique_removal">Clique removal</a></td><td><code>ap_clique_removal</code></td><td>1</td><td>The size of the independent set and the number of cliques removed by clique removal.</td></tr><tr><td><a href="#ap_large_clique_size">Large clique size</a></td><td><code>ap_large_clique_size</code></td><td>1</td><td>The size of the clique found by the greedy bound.</td></tr><tr><td><a href="#ap_nx_ramsey">Nx ramsey</a></td><td><code>ap_nx_ramsey</code></td><td>1</td><td>The Ramsey procedure's clique and independent set, each set sorted with its size first.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">\(\mathrm{Ram}(\emptyset)=(\emptyset,\emptyset)\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The whole node set is an independent set, and any single node a clique.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">The whole node set is a clique, and a single node an independent set.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">The arbitrary node \(v\) (and equal-degree candidates) decide which clique and which independent set result: the guarantee is about size, not identity.</td><td><a class="st st-w st-conv" href="#why-ap_clique_removal-networkx" title="NetworkX&#x27;s ramsey_R2 recurses on subgraphs whose nodes come in Python set order, so its arbitrary node, and the cliques and independent sets it finds, differ from the reference value&#x27;s, which takes the first node in node order; any graph with a choice can differ. ap_clique_removal_valid checks the reference value&#x27;s sets, and the convention check ap_clique_removal__networkx reproduces NetworkX through the reference value&#x27;s set-order kernel.">differs</a></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Undirected notion.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: differs. NetworkX's ramsey_R2 recurses on subgraphs whose nodes come in Python set order, so its arbitrary node, and the cliques and independent sets it finds, differ from the reference value's, which takes the first node in node order; any graph with a choice can differ. ap_clique_removal_valid checks the reference value's sets, and the convention check ap_clique_removal__networkx reproduces NetworkX through the reference value's set-order kernel. <em>(conventions.json ap_clique_removal / ap_clique_removal)</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [haynes1998fundamentals](../../references.html#haynes1998fundamentals), [lekkerkerker1962representation](../../references.html#lekkerkerker1962representation), [moon1968topics](../../references.html#moon1968topics)

## Clique removal {#ap_clique_removal}

Measure id: `ap_clique_removal`. Original family: Graph theory and combinatorics.

**Definition.** Ramsey-based clique removal: a large independent set and the disjoint cliques removed.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (direction and ties): NetworkX's ramsey_R2 recurses on subgraphs whose nodes come in Python set order, so its arbitrary node, and the cliques and independent sets it... <a href="#why-ap_clique_removal-networkx">details</a></td><td><code>clique_removal</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ap_clique_removal-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (direction and ties) on inputs tagged directed and undirected. NetworkX's ramsey\_R2 recurses on subgraphs whose nodes come in Python set order, so its arbitrary node, and the cliques and independent sets it finds, differ from the reference value's, which takes the first node in node order; any graph with a choice can differ. ap\_clique\_removal\_valid checks the reference value's sets, and the convention check ap\_clique\_removal\_\_networkx reproduces NetworkX through the reference value's set-order kernel. Mapping: the reference value computed with NetworkX's set order (the order its Ramsey routine visits nodes) agrees with the tool within abs 0, rel 0 on all 12 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 12 comparisons differ and 16 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ap_clique_removal</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>directed, undirected</td><td>direction, ties</td><td>abs 0, rel 0</td><td><code>nx.approximation.clique_removal(G_sorted): (size of the independent set, number of cliques)</code></td><td>NetworkX's ramsey_R2 recurses on subgraphs whose nodes come in Python set order, so its arbitrary node, and the cliques and independent sets it finds, differ from the reference value's, which takes the first node in node order; any graph with a choice can differ. ap_clique_removal_valid checks the reference value's sets, and the convention check ap_clique_removal__networkx reproduces NetworkX through the reference value's set-order kernel.</td></tr></tbody></table></div>

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [haynes1998fundamentals](../../references.html#haynes1998fundamentals), [lekkerkerker1962representation](../../references.html#lekkerkerker1962representation), [moon1968topics](../../references.html#moon1968topics)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Large clique size {#ap_large_clique_size}

Measure id: `ap_large_clique_size`. Original family: Graph theory and combinatorics.

**Definition.** Large clique size.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (direction and ties): NetworkX picks the candidate of largest degree from a Python set, so ties go to a different node than the reference value's first in node order, on... <a href="#why-ap_large_clique_size-networkx">details</a></td><td><code>large_clique_size</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ap_large_clique_size-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (direction and ties) on inputs tagged directed and undirected. NetworkX picks the candidate of largest degree from a Python set, so ties go to a different node than the reference value's first in node order, on any graph with tied degrees. Mapping: the reference value computed with NetworkX's set order (the order its Ramsey routine visits nodes) agrees with the tool within abs 0, rel 0 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 27 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ap_large_clique_size</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>directed, undirected</td><td>direction, ties</td><td>abs 0, rel 0</td><td><code>nx.approximation.large_clique_size(G_sorted)</code></td><td>NetworkX picks the candidate of largest degree from a Python set, so ties go to a different node than the reference value's first in node order, on any graph with tied degrees.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nx ramsey {#ap_nx_ramsey}

Measure id: `ap_nx_ramsey`. Original family: Graph theory and combinatorics.

**Definition.** Nx ramsey.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>ramsey_R2</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ap_nx_ramsey</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>ramsey_R2, clique_removal, max_clique, maximum_independent_set, large_clique_size on G_sorted: each set sorted with its size first</code></td><td></td></tr><tr><td><code>ap_nx_ramsey_valid</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>the same checks on NetworkX's results</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
