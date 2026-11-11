---
title: "Onion decomposition"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Onion decomposition {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cores, trusses and cohesive blocks. Concept id: `onion_decomposition`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>simple undirected graph (direction ignored, parallel edges merged, loops dropped) with node set \(V\), \(n=|V|\)</td></tr><tr><td>\(\deg_R(v)\)</td><td>degree within the remaining graph \(R\)</td></tr><tr><td>\(\ell(v)\)</td><td>onion layer of \(v\), starting at 1</td></tr></tbody></table></div>

## Definition {#concept-definition}

Onion layer of every node, from 1: the round of the core peeling in which it is removed.

<div class="formula-block"><p class="formula-name"><strong>Onion decomposition (Hebert-Dufresne et al. 2016)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\text{repeat: }k\leftarrow\max\bigl(k,\min_{u\in R}\deg_R(u)\bigr);\ L=\{v\in R:\deg_R(v)\le k\};\ \ell(v)=\text{round index for }v\in L;\ R\leftarrow R\setminus L\]</div><p class="formula-where">A refinement of the core decomposition that records, for each node, the round in which it is peeled when all nodes of degree at most the current core number \(k\) are removed simultaneously. The core number of a node is the value of \(k\) at its removal; layers are ordered from 1.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#onion">Onion</a></td><td><code>onion</code></td><td>1</td><td>The onion layer \(\ell(v)\) of every node of the simple undirected graph (loops dropped).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No nodes: no layers.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All nodes have degree 0 and are removed in round 1.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Layer 1.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Dropped (simple graph).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Merged.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Direction ignored.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">All nodes removed together in round 1 (all degrees \(n-1\) equal \(k\)).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Leaves have degree 1 and are removed first (layer 1); the centre then has degree 0 and is removed in layer 2.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (star8).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Nodes with equal degree are removed in the same round: the layers do not depend on an order among ties.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Star</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (star8). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

## Onion {#onion}

Measure id: `onion`. Original family: Cohesion and subgroups.

**Definition.** Onion layer of every node, from 1: the round of the core peeling in which it is removed.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>onion_layers</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.onion_layers(G), G the simple undirected graph without loops</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/cores.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/cores.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
