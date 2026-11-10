---
title: "K-path centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-path centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `k_path_centrality`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(k\)</td><td>maximum number of steps (path length limit)</td></tr><tr><td>\(W_k(s)\)</td><td>random self-avoiding walk of at most \(k\) steps from \(s\): each step moves to a neighbour not yet visited, chosen uniformly; it stops after \(k\) steps or when none is left</td></tr><tr><td>\(d(s,t)\)</td><td>length of a shortest path from \(s\) to \(t\): number of edges, or the total of the edge lengths for a weighted graph; \(\infty\) if \(t\) cannot be reached from \(s\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

K-path centrality. Entries grouped here: Geokpath; KPath Centrality.

*Definition partly written:* The exact weighting of the walk in the first formula follows the paper's message-passing model; edge cases of the sampling estimator are not stated.

<div class="formula-block"><p class="formula-name"><strong>K-path centrality (Alahakoon et al. 2011)</strong> <span class="applies">applies to: undirected, raw</span></p><div class="formula">\[\mathrm{KPC}_k(v)=\sum_{s\ne v}\Pr\bigl[v\in W_k(s)\bigr]\]</div><p class="formula-where">Expected number of messages, one per source, that reach \(v\) when messages follow random self-avoiding walks of at most \(k\) steps.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Geodesic k-path centrality (Borgatti and Everett 2006)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[C_{\mathrm{gk}}(v)=\bigl|\{u\ne v:\ d(v,u)\le k\}\bigr|\]</div><p class="formula-where">Number of nodes reached from \(v\) by a shortest path of at most \(k\) edges.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_geokpath">Geokpath</a></td><td><code>cat_geokpath</code></td><td>1</td><td>The second formula: nodes within geodesic distance \(k\) (default \(k=3\) in the documentation of the tool).</td></tr><tr><td><a href="#cat_k_path">KPath Centrality</a></td><td><code>cat_k_path</code></td><td>1</td><td>Estimates the first quantity by sampling walks; the number of steps and the sampling precision are parameters, so values are random and compared as distributions.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkit.html">NetworKit</a></th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Both quantities are 0: no other source or no other node.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Both 0: no walk reaches an isolate and an isolate reaches nobody.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Walks and geodesics stay inside a component.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(k\) must be a positive integer; \(k\ge n-1\) makes the geodesic version count every reachable node.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Geokpath {#cat_geokpath}

Measure id: `cat_geokpath`. Original family: Paths and distances.

**Definition.** Geokpath.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_geokpath-centiserve">details</a></td><td><code>geokpath</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_geokpath-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: geokpath.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## KPath Centrality {#cat_k_path}

Measure id: `cat_k_path`. Original family: Centrality.

**Definition.** KPath Centrality.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_k_path-networkit">details</a></td><td><code>KPathCentrality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_k_path-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: KPathCentrality.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
