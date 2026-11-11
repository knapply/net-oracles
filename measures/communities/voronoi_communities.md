---
title: "Voronoi communities"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Voronoi communities {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `voronoi_communities`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(g_1..g_k\)</td><td>generator nodes</td></tr><tr><td>\(d(v,g)\)</td><td>distance to a generator (in a possibly transformed length)</td></tr><tr><td>\(r\)</td><td>radius parameter of the length transformation</td></tr></tbody></table></div>

## Definition {#concept-definition}

Voronoi communities. Entries grouped here: Community voronoi; Voronoi; Voronoi cells.

*Definition partly written:* cat\_community\_voronoi (python-igraph) and cat\_cells\_voronoi (igraph, NetworkX) are documented only and were never run; their generator choice and tie handling are not recorded in the sources. The checked entry's radius selection is described under its variant.

<div class="formula-block"><p class="formula-name"><strong>Voronoi cells (Deritei et al. 2014)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{cell}(g)=\{v: d(v,g)&lt;d(v,g')\ \forall g'\ne g\}\]</div><p class="formula-where">Each node belongs to the nearest generator; nodes equidistant to several generators are ties that need a rule (split among cells or assigned to one). Generators are chosen by local relative density (a strongly dependent heuristic); the radius or length parameter is chosen to maximize modularity.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_community_voronoi">Community voronoi</a></td><td><code>cat_community_voronoi</code></td><td>1</td><td>Documented for python-igraph as Voronoi communities; not recorded in detail.</td></tr><tr><td><a href="#voronoi">Voronoi</a></td><td><code>voronoi</code></td><td>1</td><td>Voronoi communities: generators chosen by local relative density, cells by nearest generator, radius chosen to maximize modularity (the reference tries every distinct distance; a tool may use a local optimizer).</td></tr><tr><td><a href="#cat_cells_voronoi">Voronoi cells</a></td><td><code>cat_cells_voronoi</code></td><td>2</td><td>Documented for igraph and NetworkX as Voronoi cells of given generators; not recorded in detail.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/igraph.html">igraph (R)</a></th><th><a href="../../tools/pyigraph.html">igraph (Python)</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One cell.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Nodes unreachable from any generator belong to no cell.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equidistant nodes are assigned by a tie rule.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">Distances along arcs may leave nodes unassigned.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Irrelevant to distances.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><a class="st st-w st-nov" href="#why-voronoi-igraph" title="igraph chooses the radius with Brent&#x27;s method, a local search, while the reference tries every distinct distance; where they differ the reference value&#x27;s modularity is the higher. igraph&#x27;s result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match igraph requires a simple network, and on cycle7_dir its radius search stops with &quot;optimizer did not converge&quot;">no value</a></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Irrelevant with unit lengths.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><a class="st st-w st-nov" href="#why-voronoi-igraph" title="igraph chooses the radius with Brent&#x27;s method, a local search, while the reference tries every distinct distance; where they differ the reference value&#x27;s modularity is the higher. igraph&#x27;s result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match igraph requires a simple network, and on cycle7_dir its radius search stops with &quot;optimizer did not converge&quot;">no value</a></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Lengths replace edge counts.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li><strong>igraph (R)</strong>: no value. igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance; where they differ the reference value's modularity is the higher. igraph's result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match igraph requires a simple network, and on cycle7_dir its radius search stops with "optimizer did not converge" <em>(conventions.json voronoi / voronoi_modularity)</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>igraph (R)</strong>: no value. igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance; where they differ the reference value's modularity is the higher. igraph's result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match igraph requires a simple network, and on cycle7_dir its radius search stops with "optimizer did not converge" <em>(conventions.json voronoi / voronoi_modularity)</em></li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Community voronoi {#cat_community_voronoi}

Measure id: `cat_community_voronoi`. Original family: Communities.

**Definition.** Community voronoi.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_community_voronoi-pyigraph">details</a></td><td><code>community_voronoi</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_community_voronoi-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_voronoi.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Voronoi {#voronoi}

Measure id: `voronoi`. Original family: Communities.

**Definition.** Voronoi.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (direction, multi-edges, self-loops and ties): igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance. <a href="#why-voronoi-igraph">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-voronoi-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (direction, multi-edges, self-loops and ties) on inputs tagged directed and undirected. igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance; where they differ the reference value's modularity is the higher. igraph's result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 14 comparisons differ and 11 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>voronoi_modularity</code></td><td>igraph (R)</td><td>any</td><td>differs</td><td>directed, undirected, (no value) loops, (no value) multi_edges</td><td>direction, multi_edges, self_loops, ties</td><td>abs 1e-14, rel 1e-12</td><td><code>set.seed(1); modularity of cluster_voronoi(g, weights = NULL, lengths = NULL, mode = 'out') (igraph 2.3: its internal community_voronoi_impl(g, mode = 'out', radius = -1))</code></td><td>igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance; where they differ the reference value's modularity is the higher. igraph's result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match igraph requires a simple network, and on cycle7_dir its radius search stops with "optimizer did not converge"</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/communities.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/communities.yaml); [harness/golden/igraph/](https://github.com/knapply/net-oracles/tree/main/harness/golden/igraph/)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Voronoi cells {#cat_cells_voronoi}

Measure id: `cat_cells_voronoi`. Original family: Graph theory and combinatorics.

**Definition.** Voronoi cells.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_cells_voronoi-networkx">details</a></td><td><code>voronoi_cells</code></td><td>API listing</td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_cells_voronoi-igraph">details</a></td><td><code>voronoi_cells</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_cells_voronoi-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: voronoi\_cells.
- <a id="why-cat_cells_voronoi-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: voronoi\_cells.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
