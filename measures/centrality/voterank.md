---
title: "VoteRank"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# VoteRank {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `voterank`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(\bar k\)</td><td>mean degree of the graph</td></tr><tr><td>\(a_v\)</td><td>voting ability of \(v\), initially 1</td></tr><tr><td>\(s_v\)</td><td>score of \(v\): total voting ability of its neighbours</td></tr></tbody></table></div>

## Definition {#concept-definition}

VoteRank: up to a given number of influential spreaders, chosen one at a time by voting, in the order chosen.

<div class="formula-block"><p class="formula-name"><strong>VoteRank (Zhang et al. 2016)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[s_v=\sum_{u\in N(v)}a_u;\ \ \text{select }v^*=\arg\max_{v\notin S}s_v;\ \ a_{v^*}\leftarrow 0;\ \ a_u\leftarrow\max\bigl(a_u-\tfrac1{\bar k},0\bigr)\ \ (u\in N(v^*))\]</div><p class="formula-where">Up to \(r\) spreaders are chosen one at a time; the output is the sequence of chosen nodes. Ties between equal scores are resolved by the implementation's order (the definition does not fix it).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_voterank">Voterank</a></td><td><code>cx_voterank</code></td><td>1</td><td>The sequence of up to \(r\) nodes chosen by the voting rounds above.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">The one node has score 0; whether it is chosen depends on the stopping rule (a score of 0 ends the selection).</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All scores 0: nothing is chosen.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Score 0: never chosen while others have votes.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal top scores need a tie-break; the definition leaves it open, so the order of chosen nodes can differ between implementations.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(r\ge 1\); \(\bar k=0\) (no edges) makes the decrement \(1/\bar k\) undefined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Isolated nodes</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

## Voterank {#cx_voterank}

Measure id: `cx_voterank`. Original family: Centrality.

**Definition.** VoteRank: up to a given number of influential spreaders, chosen one at a time by voting, in the order chosen.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>voterank</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_voterank</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.voterank(G)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/centrality_extra.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/centrality_extra.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
