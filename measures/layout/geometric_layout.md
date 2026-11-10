---
title: "Grid, random, circle and sphere layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Grid, random, circle and sphere layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `geometric_layout`. 4 measures.

## Definition {#concept-definition}

Grid, random, circle and sphere layouts. Entries grouped here: Circle, tree and two-mode (barycenter) layouts; Grid layout; Random layout; Sphere layout.

*Definition not yet written.* Documented by name only; the sources record the tool function and no definition, and no primary paper was checked.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#layout_simple">Circle, tree and two-mode (barycenter) layouts</a></td><td><code>layout_simple</code></td><td>5</td></tr><tr><td><a href="#layout_grid">Grid layout</a></td><td><code>layout_grid</code></td><td>1</td></tr><tr><td><a href="#layout_random">Random layout</a></td><td><code>layout_random</code></td><td>3</td></tr><tr><td><a href="#layout_sphere">Sphere layout</a></td><td><code>layout_sphere</code></td><td>1</td></tr></tbody></table></div>

## Circle, tree and two-mode (barycenter) layouts {#layout_simple}

Measure id: `layout_simple`. Original family: Layout.

**Definition.** Circle, tree and two-mode (barycenter) layouts.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-layout_simple-networkx">details</a></td><td></td><td>documentation</td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-layout_simple-igraph">details</a></td><td><code>layout_as_bipartite; layout_as_star; layout_as_tree; layout_in_circle</code></td><td>documentation</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_simple-pyigraph">details</a></td><td><code>layout_reingold_tilford; layout_reingold_tilford_circular</code></td><td>API listing</td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_simple-rustworkx">details</a></td><td><code>bipartite_layout; circular_layout; digraph_bipartite_layout; digraph_circular_layout; digraph_shell_layout; digraph_spiral_layout; graph_bipartite_layout; graph_circular_layout; graph_shell_layout; graph_spiral_layout; shell_layout; spiral_layout</code></td><td>API listing</td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_simple-boost">details</a></td><td><code>circle_layout</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_simple-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (networkx public API (algorithms, generators, linalg, readwrite)).
- <a id="why-layout_simple-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package igraph: exported functions and help titles); API names: layout\_as\_bipartite; layout\_as\_star; layout\_as\_tree; layout\_in\_circle.
- <a id="why-layout_simple-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: layout\_reingold\_tilford; layout\_reingold\_tilford\_circular.
- <a id="why-layout_simple-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: bipartite\_layout; circular\_layout; digraph\_bipartite\_layout; digraph\_circular\_layout; digraph\_shell\_layout; digraph\_spiral\_layout; graph\_bipartite\_layout; graph\_circular\_layout; graph\_shell\_layout; graph\_spiral\_layout; shell\_layout; spiral\_layout.
- <a id="why-layout_simple-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: circle\_layout.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Grid layout {#layout_grid}

Measure id: `layout_grid`. Original family: Layout.

**Definition.** Grid layout.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_grid-igraph">details</a></td><td><code>layout_on_grid</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_grid-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: layout\_on\_grid.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Random layout {#layout_random}

Measure id: `layout_random`. Original family: Layout.

**Definition.** Random layout.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_random-igraph">details</a></td><td><code>layout_randomly</code></td><td>API listing</td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_random-rustworkx">details</a></td><td><code>digraph_random_layout; graph_random_layout; random_layout</code></td><td>API listing</td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_random-boost">details</a></td><td><code>random_graph_layout</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_random-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: layout\_randomly.
- <a id="why-layout_random-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_random\_layout; graph\_random\_layout; random\_layout.
- <a id="why-layout_random-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: random\_graph\_layout.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Sphere layout {#layout_sphere}

Measure id: `layout_sphere`. Original family: Layout.

**Definition.** Sphere layout.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-layout_sphere-igraph">details</a></td><td><code>layout_on_sphere</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_sphere-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: layout\_on\_sphere.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
