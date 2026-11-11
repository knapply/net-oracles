---
title: "Dispersion"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Dispersion {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `dispersion`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(C_{uv}\)</td><td>common neighbours of \(u\) and \(v\)</td></tr><tr><td>\(d_v(s,t)\)</td><td>1 if \(s\ne t\) are not adjacent and have no common neighbour in the ego network of \(u\) with \(u\) and \(v\) removed; 0 otherwise</td></tr></tbody></table></div>

## Definition {#concept-definition}

Dispersion of the tie between each given pair of nodes (Backstrom and Kleinberg), one value per pair.

<div class="formula-block"><p class="formula-name"><strong>Dispersion of the tie (Backstrom and Kleinberg 2014)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{disp}(u,v)=\sum_{s,t\in C_{uv}}d_v(s,t)\]</div><p class="formula-where">Counts pairs of common neighbours of \(u\) and \(v\) that are not themselves closely connected. The paper also defines normalized and recursive forms; the plain count is the base definition.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_dispersion">Dispersion</a></td><td><code>cx_dispersion</code></td><td>1</td><td>The count above for given pairs of nodes, with optional normalization and embeddedness-based variants as parameters of the tool.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">No common neighbours: dispersion 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop makes a node its own neighbour; the pair test \(d_v(s,t)\) is then not symmetric in \(s\) and \(t\) unless \(s,t\) are required to differ from \(u,v\).</td><td><a class="st st-w st-conv" href="#why-cx_dispersion-networkx" title="On directed networks, and at nodes with self-loops, NetworkX&#x27;s pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; On undirected networks without self-loops the test is symmetric and the values agree.">differs</a></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">The definition is for undirected graphs; with directed edges the symmetric pair test is not defined.</td><td><a class="st st-w st-conv" href="#why-cx_dispersion-networkx" title="On directed networks, and at nodes with self-loops, NetworkX&#x27;s pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; On undirected networks without self-loops the test is symmetric and the values agree.">differs</a></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Dispersion 0: every pair of common neighbours is adjacent.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: differs. On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; On undirected networks without self-loops the test is symmetric and the values agree. <em>(conventions.json cx_dispersion / cx_dispersion)</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: differs. On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; On undirected networks without self-loops the test is symmetric and the values agree. <em>(conventions.json cx_dispersion / cx_dispersion)</em></li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

## Dispersion {#cx_dispersion}

Measure id: `cx_dispersion`. Original family: Centrality.

**Definition.** Dispersion of the tie between each given pair of nodes (Backstrom and Kleinberg), one value per pair.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (direction, self-loops and ties): On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair... <a href="#why-cx_dispersion-networkx">details</a></td><td><code>dispersion</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cx_dispersion-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (direction, self-loops and ties) on inputs tagged directed and loops. On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 15 comparisons differ and 69 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_dispersion</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>directed, loops</td><td>direction, self_loops, ties</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.dispersion(G)[u][v] for every ordered pair of adjacent nodes</code></td><td>On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree.</td></tr><tr><td><code>cx_dispersion_params</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>directed, loops</td><td>direction, self_loops, ties</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.dispersion(G, alpha = 2, b = 1, c = 0.5)</code></td><td>On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree.</td></tr><tr><td><code>cx_dispersion_raw</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>directed, loops</td><td>direction, self_loops, ties</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.dispersion(G, normalized = False)</code></td><td>On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/centrality_extra.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/centrality_extra.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
