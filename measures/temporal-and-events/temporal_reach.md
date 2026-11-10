---
title: "Temporal reach"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Temporal reach {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Temporal descriptives. Concept id: `temporal_reach`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\((u,v,t)\)</td><td>a contact: an edge from source \(u\) to target \(v\) (or between \(u\) and \(v\) if undirected) active at time \(t\)</td></tr><tr><td>\(t_0,t_1\)</td><td>start and end of the observation window; only contacts with \(t_0\le t\le t_1\) are used</td></tr><tr><td>\(A(s,v)\)</td><td>earliest arrival time at \(v\) over time-respecting paths from \(s\); \(\infty\) if there is none</td></tr></tbody></table></div>

## Definition {#concept-definition}

Temporal reach. Entries grouped here: Temporal reach.

<div class="formula-block"><p class="formula-name"><strong>Time-respecting path and earliest arrival (Kempe et al. 2002; Holme and Saramaki 2012)</strong> <span class="applies">applies to: any, directed, undirected</span></p><div class="formula">\[A(s,v)=\min\Bigl\{t_k:\ (s{=}v_0,v_1,t_1),\dots,(v_{k-1},v_k{=}v,t_k)\text{ contacts},\ t_0\le t_1\le\dots\le t_k\le t_1^{\mathrm{end}}\Bigr\},\qquad A(s,s)=t_0\]</div><p class="formula-where">A path may wait at a node and may use several contacts with the same time (traversal time 0, non-strict ordering \(t_i\le t_{i+1}\)). \(t_1^{\mathrm{end}}\) is the end of the window. Unreachable nodes have \(A=\infty\). Strict ordering \(t_i&lt;t_{i+1}\) would give a different value on simultaneous contacts.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Forward reachable set size</strong> <span class="applies">applies to: any</span></p><div class="formula">\[R(s)=\bigl|\{v\ne s:\ A(s,v)&lt;\infty\}\bigr|\]</div><p class="formula-where">The number of other nodes reachable from \(s\) by a time-respecting path in the window; subtracting the source removes the trivial path to itself.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#temporal_reach">Temporal reach</a></td><td><code>temporal_reach</code></td><td>1</td><td>Count of nodes with finite earliest arrival time from the source, excluding the source.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/tsna.html">tsna / networkDynamic</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(R(s)=0\): no other node.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(R(s)=0\) for every node.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">An isolate reaches nobody and is reached by nobody: 0.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse).">agrees</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">Counts only nodes reachable along source to target.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">For undirected contacts both orientations are usable; for directed contacts only source to target.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Contacts with equal times can be chained when the ordering is non-strict, as in the formula above.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Repeated contacts only add candidate times; the minimum in \(A\) is unchanged by duplicates of the same time.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>tsna / networkDynamic</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>tsna / networkDynamic</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Isolated nodes</summary><ul><li><strong>tsna / networkDynamic</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty, single_node, two_triangles_isolate, gnp_und_sparse). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li><strong>tsna / networkDynamic</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>tsna / networkDynamic</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>tsna / networkDynamic</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>tsna / networkDynamic</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## Temporal reach {#temporal_reach}

Measure id: `temporal_reach`. Original family: Temporal and events.

**Definition.** Temporal reach.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tsna.html">tsna / networkDynamic</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>forward.reachable; tReach</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>temporal_reach_out_instantaneous</code></td><td>tsna / networkDynamic</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sum(is.finite(tPath(nd, v, 'fwd', 'earliest.arrive', ...)$tdist)) - 1</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [handcock2008statnet](../../references.html#handcock2008statnet)
{% endraw %}
