---
title: "Diffusion centrality and diffusion degree"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Diffusion centrality and diffusion degree {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `diffusion_centrality`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(A\)</td><td>adjacency matrix: \(A_{uv}\) is the number of edges from \(u\) to \(v\), or their total weight for a weighted graph</td></tr><tr><td>\(q\)</td><td>probability that a node passes information to a neighbour</td></tr><tr><td>\(T\)</td><td>number of rounds</td></tr><tr><td>\(\lambda_v\)</td><td>propagation probability of node \(v\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Diffusion centrality and diffusion degree. Entries grouped here: Diffusion; Diffusion degree; Diffusion efficiency.

*Definition partly written:* The diffusion-efficiency entry and the second tool's function of the same name are described by name and documentation summary only.

<div class="formula-block"><p class="formula-name"><strong>Diffusion centrality (Banerjee et al. 2013)</strong> <span class="applies">applies to: any, weighted</span></p><div class="formula">\[\mathrm{DC}(v)=\Bigl[\sum_{t=1}^{T}(qA)^{t}\,\mathbf 1\Bigr]_v\]</div><p class="formula-where">Expected number of information receivers from \(v\) after \(T\) rounds in which each tie transmits with probability \(q\); the tool takes \(P=qA\) as input and \(T\) defaults to the network size.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Diffusion degree (Pal et al. 2014)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\mathrm{DD}(v)=\lambda_v k^{\mathrm{out}}(v)+\sum_{u\in N^{\mathrm{out}}(v)}\lambda_u k^{\mathrm{out}}(u)\]</div><p class="formula-where">As described in the documentation: the contribution of the node itself plus that of its neighbours, each a propagation probability times degree; \(\lambda\) defaults to 1.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_diffusion">Diffusion</a></td><td><code>cat_diffusion</code></td><td>2</td><td>Diffusion centrality of one tool (formula one); another tool's function of the same name is a heat-diffusion computation and is a different quantity.</td></tr><tr><td><a href="#cat_degree_diffusion">Diffusion degree</a></td><td><code>cat_degree_diffusion</code></td><td>1</td><td>Diffusion degree, second formula.</td></tr><tr><td><a href="#cat_diffusion_efficiency">Diffusion efficiency</a></td><td><code>cat_diffusion_efficiency</code></td><td>1</td><td>Pairwise diffusion efficiency, the inverse of mean first-passage time of a random walk (Goni et al. 2014); a different quantity grouped here by the catalogue.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sknetwork.html">scikit-network</a></th><th><a href="../../tools/bct.html">BCT (Octave)</a></th><th><a href="../../tools/keyplayer.html">keyplayer</a></th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Diffusion centrality 0 without edges; diffusion degree 0 with \(\lambda\)-weighted degree 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All scores 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is a diagonal entry of \(A\) and feeds back into the sum.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">\(A\) counts parallel edges.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(T\) a positive integer, \(q\in[0,1]\); the series is finite so it converges for any \(q\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Diffusion {#cat_diffusion}

Measure id: `cat_diffusion`. Original family: Centrality.

**Definition.** Diffusion.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_diffusion-sknetwork">details</a></td><td><code>Diffusion; diffusion</code></td><td>API listing</td></tr><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_diffusion-keyplayer">details</a></td><td><code>diffusion</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_diffusion-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Diffusion; diffusion.
- <a id="why-cat_diffusion-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. keyplayer 1.0.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package keyplayer: exported functions and help titles); API names: diffusion.

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer), [tool_sknetwork](../../references.html#tool_sknetwork)

## Diffusion degree {#cat_degree_diffusion}

Measure id: `cat_degree_diffusion`. Original family: Centrality.

**Definition.** Diffusion degree.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_degree_diffusion-centiserve">details</a></td><td><code>diffusion.degree</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_diffusion-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: diffusion.degree.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Diffusion efficiency {#cat_diffusion_efficiency}

Measure id: `cat_diffusion_efficiency`. Original family: Centrality.

**Definition.** Diffusion efficiency.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_diffusion_efficiency-bct">details</a></td><td><code>diffusion_efficiency</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_diffusion_efficiency-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: diffusion\_efficiency.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
