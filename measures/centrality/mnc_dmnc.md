---
title: "MNC and DMNC"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# MNC and DMNC {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `mnc_dmnc`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(N(v)\)</td><td>set of neighbours of \(v\) (nodes joined to \(v\) by an edge, \(v\) itself excluded)</td></tr><tr><td>\(G[N(v)]\)</td><td>subgraph induced by the neighbours of \(v\) (without \(v\))</td></tr><tr><td>\(MC(v)\)</td><td>largest connected component of \(G[N(v)]\)</td></tr><tr><td>\(\varepsilon\in[1,2]\)</td><td>exponent of the density</td></tr></tbody></table></div>

## Definition {#concept-definition}

MNC and DMNC. Entries grouped here: Dmnc; Mnc.

<div class="formula-block"><p class="formula-name"><strong>Maximum neighbourhood component (Lin et al. 2008)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{MNC}(v)=|V(MC(v))|\]</div><p class="formula-where">Number of nodes of the largest connected component among the neighbours of \(v\). For directed graphs the neighbours are chosen by mode (in, out, all).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Density of MNC</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{DMNC}(v)=\frac{|E(MC(v))|}{|V(MC(v))|^{\varepsilon}}\]</div><p class="formula-where">Edges of that component divided by its number of nodes to the power \(\varepsilon\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_dmnc">Dmnc</a></td><td><code>cat_dmnc</code></td><td>1</td><td>DMNC, second formula.</td></tr><tr><td><a href="#cat_mnc">Mnc</a></td><td><code>cat_mnc</code></td><td>1</td><td>MNC, first formula.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">\(N(v)=\emptyset\): MNC 0; DMNC is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">MNC 0; DMNC 0/0 (empty component).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop makes \(v\) its own neighbour; the definition excludes \(v\) from \(N(v)\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Edges inside the component: parallel edges would count more than once in \(|E|\) unless the graph is simple.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\varepsilon\) between 1 and 2.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Dmnc {#cat_dmnc}

Measure id: `cat_dmnc`. Original family: Graph theory and combinatorics.

**Definition.** Dmnc.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dmnc-centiserve">details</a></td><td><code>dmnc</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dmnc-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: dmnc.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Mnc {#cat_mnc}

Measure id: `cat_mnc`. Original family: Graph theory and combinatorics.

**Definition.** Mnc.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_mnc-centiserve">details</a></td><td><code>mnc</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mnc-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: mnc.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
