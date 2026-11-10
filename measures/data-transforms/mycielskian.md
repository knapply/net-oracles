---
title: "Mycielskian"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Mycielskian {#concept-top}

Family: [Data transforms](index.html). Subfamily: Graph operators. Concept id: `mycielskian`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(v_i,u_i,w\)</td><td>the original node \(v_i\), its copy \(u_i\) and the new apex node \(w\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Mycielskian. Entries grouped here: Mycielski graph; Mycielskian.

*Definition partly written:* The construction is given from its standard description without a cited primary source (Mycielski 1955 is not among the checked bibliography); the two documented entries are not specified further in the sources.

<div class="formula-block"><p class="formula-name"><strong>Mycielskian \(M(G)\)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[V(M(G))=\{v_i\}\cup\{u_i\}\cup\{w\},\quad E=\{v_iv_j,\ v_iu_j,\ u_iv_j:\ v_iv_j\in E(G)\}\cup\{u_iw\}_{i}\]</div><p class="formula-where">Adds a copy \(u_i\) of each node joined to the neighbours of \(v_i\), and an apex \(w\) joined to all copies: \(2n+1\) nodes and \(3m+n\) edges, triangle-free when \(G\) is, and one more colour needed than for \(G\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_mycielski">Mycielski graph</a></td><td><code>cat_mycielski</code></td><td>1</td><td>Mycielski graph as listed by one documented tool; same construction.</td></tr><tr><td><a href="#cat_mycielskian">Mycielskian</a></td><td><code>cat_mycielskian</code></td><td>1</td><td>Mycielskian of a graph as listed by another documented tool; same construction, possibly iterated.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">The construction gives the single node \(w\) (\(2\cdot0+1\) nodes).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One node gives \(M(K_1)=K_2\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">\(M(K_2)=C_5\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Two nodes</summary><ul><li>No tool entries.</li></ul></details></div>

## Mycielski graph {#cat_mycielski}

Measure id: `cat_mycielski`. Original family: Generators and rewiring.

**Definition.** Mycielski graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_mycielski-networkx">details</a></td><td><code>mycielski_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mycielski-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: mycielski\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Mycielskian {#cat_mycielskian}

Measure id: `cat_mycielskian`. Original family: Graph theory and combinatorics.

**Definition.** Mycielskian.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_mycielskian-networkx">details</a></td><td><code>mycielskian</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mycielskian-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: mycielskian.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
