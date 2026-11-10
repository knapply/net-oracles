---
title: "Automorphic equivalence"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Automorphic equivalence {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Equivalence and clustering. Concept id: `automorphic_equivalence`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target</td></tr><tr><td>\(\varphi\)</td><td>a permutation of \(V\)</td></tr><tr><td>\(a_{ij}\)</td><td>number of ties from \(i\) to \(j\) (multiplicity respected)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Orbits of the automorphism group of the binary ties: nodes that map to each other under some automorphism share a label.

<div class="formula-block"><p class="formula-name"><strong>Automorphic equivalence</strong> <span class="applies">applies to: any</span></p><div class="formula">\[i\simeq j\iff\exists\,\varphi\in\mathrm{Aut}(G):\varphi(i)=j,\qquad \mathrm{Aut}(G)=\{\varphi: a_{\varphi(u)\varphi(v)}=a_{uv}\ \forall u,v\}\]</div><p class="formula-where">Two nodes are equivalent when some automorphism (tie-preserving permutation) maps one to the other; the classes are the orbits of the automorphism group. Orbit computation by canonical labelling is due to McKay and Piperno 2014. Every orbit is a union of structural-equivalence classes and lies inside a regular-equivalence class.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#automorphic_equivalence">Automorphic equivalence</a></td><td><code>automorphic_equivalence</code></td><td>2</td><td>The orbit label of each node under the automorphism group of the binary (or multiplicity-valued) ties.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/nauty.html">nauty</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No nodes: no orbits.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All nodes are interchangeable: one orbit.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One orbit of one node.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">All isolates map to each other: they share one orbit.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is preserved by an automorphism: nodes with and without loops are in different orbits.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Multiplicities are part of the structure: \(a_{\varphi(u)\varphi(v)}=a_{uv}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-nov" title="nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented.">no value</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">For directed graphs \(a_{ij}\) is not symmetric, so fewer permutations are automorphisms.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Every permutation is an automorphism: one orbit.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Two orbits: the centre and the leaves.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>nauty</strong>: no value. nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented. <em>(conventions.json automorphic_equivalence / automorphic_equivalence)</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[mckay2014practical](../../references.html#mckay2014practical)

## Automorphic equivalence {#automorphic_equivalence}

Measure id: `automorphic_equivalence`. Original family: Roles and positions.

**Definition.** Orbits of the automorphism group of the binary ties: nodes that map to each other under some automorphism share a label.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-automorphic_equivalence-ucinet">details</a></td><td><code>orbits</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/nauty.html">nauty</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-automorphic_equivalence-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>automorphic_equivalence</code></td><td>nauty</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>pynauty.autgrp(Graph).orbits (nauty 2.8.8): orbit of the automorphism group</code></td><td>nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented.</td></tr></tbody></table></div>

**References:** [mckay2014practical](../../references.html#mckay2014practical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [mckay2014practical](../../references.html#mckay2014practical)
{% endraw %}
