---
title: "Multilayer networks"
layout: default
parent: "Signed and multilayer"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Multilayer networks {#concept-top}

Family: [Signed and multilayer](index.html). Subfamily: Multilayer networks. Concept id: `multilayer`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(L\)</td><td>set of layers (aspects), \(L=L_1\times\cdots\times L_d\)</td></tr><tr><td>\(V_M\subseteq V\times L\)</td><td>node-layers: a node \(v\) present in layer \(\alpha\)</td></tr><tr><td>\(A^{(\alpha)}\)</td><td>adjacency matrix of the intra-layer edges of layer \(\alpha\)</td></tr><tr><td>\(C^{(\alpha\beta)}\)</td><td>coupling matrix of the inter-layer edges between layers \(\alpha\) and \(\beta\)</td></tr><tr><td>\(\mathcal A\)</td><td>supra-adjacency matrix, of size \(n\,|L|\times n\,|L|\) when every node is present in every layer</td></tr></tbody></table></div>

## Definition {#concept-definition}

Multilayer networks. Entries grouped here: Multilayer networks (node-layers, supra-adjacency).

<div class="formula-block"><p class="formula-name"><strong>Multilayer network (Kivela et al. 2014)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[M=(V_M,E_M,V,L),\qquad E_M\subseteq V_M\times V_M\]</div><p class="formula-where">Node-layers \(V_M\) joined by edges \(E_M\); edges within one layer are intra-layer, edges between layers are inter-layer. A multiplex network is the case in which the inter-layer edges join only the copies of the same node.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Supra-adjacency matrix (De Domenico et al. 2013)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathcal A=\begin{pmatrix}A^{(1)}&amp;C^{(12)}&amp;\cdots\\C^{(21)}&amp;A^{(2)}&amp;\cdots\\\vdots&amp;\vdots&amp;\ddots\end{pmatrix},\qquad C^{(\alpha\beta)}=\omega\,I\ \text{for multiplex coupling}\]</div><p class="formula-where">Block matrix of the layers on the diagonal and the couplings off the diagonal; the scalar \(\omega\) is the coupling weight of a multiplex network and is not fixed by the definition.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#multilayer">Multilayer networks (node-layers, supra-adjacency)</a></td><td><code>multilayer</code></td><td>2</td><td>The structure and its supra-adjacency matrix; the coupling weight and which inter-layer edges exist are parameters of the model, not of the definition.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/pymnet.html">pymnet</a></th><th><a href="../../tools/multinet.html">multinet</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">With no node-layers \(\mathcal A\) is the 0\(\times\)0 matrix; the definition allows it.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A node-layer with no intra- or inter-layer edge gives a zero row and column of \(\mathcal A\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">The coupling weight \(\omega\) is a free real parameter; the definition imposes no range, and measures built on \(\mathcal A\) may need \(\omega\ge 0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Multilayer networks (node-layers, supra-adjacency) {#multilayer}

Measure id: `multilayer`. Original family: Signed and multilayer.

**Definition.** Multilayer networks (node-layers, supra-adjacency).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pymnet.html">pymnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: pymnet is documented-only in this survey; listed in its documentation. <a href="#why-multilayer-pymnet">details</a></td><td></td><td>documentation</td></tr><tr><td><a href="../../tools/multinet.html">multinet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: multinet is documented-only in this survey; listed in its documentation. <a href="#why-multilayer-multinet">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-multilayer-pymnet"></a>**[pymnet](../../tools/pymnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. pymnet (version not recorded) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: its documentation.
- <a id="why-multilayer-multinet"></a>**[multinet](../../tools/multinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. multinet (version not recorded) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: its documentation.

**Tools cited:** [magnani2021analysis](../../references.html#magnani2021analysis), [nurmi2024pymnet](../../references.html#nurmi2024pymnet)
{% endraw %}
