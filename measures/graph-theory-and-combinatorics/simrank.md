---
title: "SimRank"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SimRank {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Similarity and link prediction. Concept id: `simrank`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(I(v)\)</td><td>in-neighbours of \(v\)</td></tr><tr><td>\(C\)</td><td>decay constant in \((0,1)\)</td></tr><tr><td>\(s(u,v)\)</td><td>SimRank similarity</td></tr></tbody></table></div>

## Definition {#concept-definition}

SimRank similarity of every pair of nodes: two nodes are similar when their in-neighbors are (Jeh and Widom 2002).

<div class="formula-block"><p class="formula-name"><strong>SimRank (Jeh and Widom 2002)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[s(u,u)=1,\qquad s(u,v)=\frac{C}{|I(u)|\,|I(v)|}\sum_{a\in I(u)}\sum_{b\in I(v)}s(a,b)\ \ (u\ne v),\quad s(u,v)=0\ \text{if }I(u)=\emptyset\text{ or }I(v)=\emptyset\]</div><p class="formula-where">Two nodes are similar when their in-neighbours are similar; defined by a fixed-point equation, computed by iteration (Jacobi) from \(s=I\) until the change falls below a tolerance or an iteration cap is reached, so values depend on the stopping rule.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#simrank">Simrank</a></td><td><code>simrank</code></td><td>1</td><td>The similarity of every pair of nodes, for a decay constant \(C\) (default 0.8 in common use) and a stopping rule.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No pairs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(s=1\) for the node with itself.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">No in-neighbours: \(s(u,v)=0\) for all \(v\ne u\).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse).">agrees</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">The identity matrix.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">In-neighbour sets ignore multiplicity (the sum over \(I(u)\) is over a set).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(C\notin(0,1)\): the iteration need not converge or the values leave \([0,1]\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">In-neighbours of a digraph; for undirected input all neighbours.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Isolated nodes</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

## Simrank {#simrank}

Measure id: `simrank`. Original family: Graph theory and combinatorics.

**Definition.** SimRank similarity of every pair of nodes: two nodes are similar when their in-neighbors are (Jeh and Widom 2002).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>simrank_similarity</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>simrank</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.simrank_similarity(G) on the simple Graph or DiGraph, every pair</code></td><td></td></tr><tr><td><code>simrank_converged</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-11, rel 1e-09</td><td><code>nx.similarity._simrank_similarity_python(G, tolerance = 1e-13)</code></td><td></td></tr><tr><td><code>simrank_pairwise</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.similarity._simrank_similarity_python(G)</code></td><td></td></tr><tr><td><code>simrank_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.simrank_similarity(M) on the weighted multigraph (to_numpy_array adds the weights of parallel edges)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/similarity.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/similarity.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
