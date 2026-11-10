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

## Definition {#concept-definition}

Voronoi communities. Entries grouped here: Community voronoi; Voronoi; Voronoi cells.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_community_voronoi">Community voronoi</a></td><td><code>cat_community_voronoi</code></td><td>1</td></tr><tr><td><a href="#voronoi">Voronoi</a></td><td><code>voronoi</code></td><td>1</td></tr><tr><td><a href="#cat_cells_voronoi">Voronoi cells</a></td><td><code>cat_cells_voronoi</code></td><td>2</td></tr></tbody></table></div>

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
