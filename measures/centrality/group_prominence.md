---
title: "Prominent group"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Prominent group {#concept-top}

Family: [Centrality](index.html). Subfamily: Group centrality. Concept id: `group_prominence`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(k\)</td><td>group size</td></tr><tr><td>\(C_B(S)\)</td><td>group betweenness of \(S\) (see group betweenness)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Prominent group. Entries grouped here: Prominent group.

<div class="formula-block"><p class="formula-name"><strong>Prominent group</strong> <span class="applies">applies to: group</span></p><div class="formula">\[S^*=\arg\max_{|S|=k}C_B(S)\]</div><p class="formula-where">The group of \(k\) nodes with the largest group betweenness. Exact search checks all \(\binom nk\) groups; greedy search adds the node with the largest gain one at a time and is not guaranteed to find the maximum.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#nxo_prominent">Prominent group</a></td><td><code>nxo_prominent</code></td><td>1</td><td>Prominent-group search with exact or greedy strategy and optional options (endpoints, weights).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">\(k=0\): empty group, value 0. \(k\ge n-1\): fewer than two non-members.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Several groups can share the maximum; which one is returned is not fixed.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Group betweenness counts only pairs with a path.</td><td><span class="st st-w st-conv" title="the reference searches the value without endpoints; the definition oracle checks it.">differs</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Inherits group betweenness.</td><td><span class="st st-w st-nov" title="NetworkX takes the smallest weight of parallel edges; the reference reads the first (the backend leaves multigraphs to NetworkX).">no value</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: differs. the reference searches the value without endpoints; the definition oracle checks it. <em>(conventions.json nxo_prominent / nxo_prominent_group)</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX takes the smallest weight of parallel edges; the reference reads the first (the backend leaves multigraphs to NetworkX). <em>(conventions.json nxo_prominent / nxo_prominent_group_options)</em></li></ul></details></div>

## Prominent group {#nxo_prominent}

Measure id: `nxo_prominent`. Original family: Graph theory and combinatorics.

**Definition.** Prominent group.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>prominent_group</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxo_prominent_greedy</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.prominent_group(G, 3, greedy = True)</code></td><td></td></tr><tr><td><code>nxo_prominent_group</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>disconnected</td><td>defaults, direction</td><td>abs 0, rel 0</td><td><code>nx.prominent_group(G, 2), value then group</code></td><td>the reference searches the value without endpoints; the definition oracle checks it.</td></tr><tr><td><code>nxo_prominent_group_options</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges, weights</td><td>abs 0, rel 0</td><td><code>nx.prominent_group(G, 3, weight = 'weight', endpoints = True, normalized = False)</code></td><td>NetworkX takes the smallest weight of parallel edges; the reference reads the first (the backend leaves multigraphs to NetworkX).</td></tr><tr><td><code>nxo_prominent_value</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>disconnected</td><td>defaults, direction</td><td>abs 0, rel 0</td><td><code>nx.prominent_group(G, 2)[0]</code></td><td>the reference searches the value without endpoints; the definition oracle checks it.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/nx_order.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/nx_order.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f002">F002</a></td><td>NetworkX</td><td>defect</td><td>prominent_group misses the best group on disconnected graphs</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
