---
title: "Vertex coloring"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Vertex coloring {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Coloring. Concept id: `vertex_coloring`. 2 measures.

## Definition {#concept-definition}

A greedy colouring: the colour of every node, from 0, by one of seven node-order strategies.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Coloring](#st_coloring) | `st_coloring` | 1 |
| [Greedy color](#greedy_color) | `greedy_color` | 8 |

## References {#concept-references}

[brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [matula1983smallest](../../references.html#matula1983smallest), [welsh1967upper](../../references.html#welsh1967upper)

## Coloring {#st_coloring}

Measure id: `st_coloring`. Original family: Graph theory and combinatorics.

**Definition.** Coloring.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_coloring` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `colours per node from greedy_color(G, 'largest_first'), (G, 'largest_first', interchange=True), (G, 'DSATUR'), equitable_color(G, D + 1), equitable_color(G, D + 3) on the simple undirected graph` |  |
| `st_coloring_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's colourings` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Greedy color {#greedy_color}

Measure id: `greedy_color`. Original family: Graph theory and combinatorics.

**Definition.** A greedy colouring: the colour of every node, from 0, by one of seven node-order strategies.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and ties): NetworkX visits the neighbours of a node in the order its edges were added, and starts each component from the first node of its Python set (not the... [details](#why-greedy_color-networkx) | `color; equitable_color; greedy_color; strategy_connected_sequential; strategy_connected_sequential_bfs; strategy_connected_sequential_dfs; strategy_independent_set; strategy_largest_first; strategy_random_sequential; strategy_saturation_largest_first; strategy_smallest_last` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-greedy_color-igraph) | `greedy_vertex_coloring` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-greedy_color-pyigraph) | `vertex_coloring_greedy` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-greedy_color-graphtool) | `sequential_vertex_coloring` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-greedy_color-networkit) | `SpectralColoring` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-greedy_color-rustworkx) | `graph_greedy_color` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-greedy_color-jgrapht) | `BrownBacktrackColoring; ChordalGraphColoring; GreedyColoring; LargestDegreeFirstColoring; RandomGreedyColoring; SaturationDegreeColoring; SmallestDegreeLastColoring` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-greedy_color-boost) | `edge_coloring; sequential_vertex_coloring; smallest_last_ordering` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-greedy_color-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults and ties) on inputs tagged disconnected and unsorted\_edges. NetworkX visits the neighbours of a node in the order its edges were added, and starts each component from the first node of its Python set (not the smallest when the component's nodes are large numbers); the reference visits neighbours in increasing node order and starts from the smallest node (the order used by the definition oracle). The two agree on connected graphs with a sorted edge list. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 2 comparisons differ and 130 agree.
- <a id="why-greedy_color-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: greedy\_vertex\_coloring.
- <a id="why-greedy_color-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: vertex\_coloring\_greedy.
- <a id="why-greedy_color-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: sequential\_vertex\_coloring.
- <a id="why-greedy_color-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: SpectralColoring.
- <a id="why-greedy_color-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: graph\_greedy\_color.
- <a id="why-greedy_color-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BrownBacktrackColoring; ChordalGraphColoring; GreedyColoring; LargestDegreeFirstColoring; RandomGreedyColoring; SaturationDegreeColoring; SmallestDegreeLastColoring.
- <a id="why-greedy_color-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: edge\_coloring; sequential\_vertex\_coloring; smallest\_last\_ordering.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `color_connected_sequential_bfs` | NetworkX | undirected | differs | disconnected, unsorted\_edges | defaults, ties | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'connected_sequential_bfs')` | NetworkX visits the neighbours of a node in the order its edges were added, and starts each component from the first node of its Python set (not the smallest when the component's nodes are large numbers); the reference visits neighbours in increasing node order and starts from the smallest node (the order used by the definition oracle). The two agree on connected graphs with a sorted edge list. |
| `color_connected_sequential_dfs` | NetworkX | undirected | differs | disconnected, unsorted\_edges | defaults, ties | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'connected_sequential_dfs')` | NetworkX visits the neighbours of a node in the order its edges were added, and starts each component from the first node of its Python set (not the smallest when the component's nodes are large numbers); the reference visits neighbours in increasing node order and starts from the smallest node (the order used by the definition oracle). The two agree on connected graphs with a sorted edge list. |
| `color_independent_set_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same two tests on nx.greedy_color(G, strategy = 'independent_set') of the loop-free simple graph` |  |
| `color_largest_first` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'largest_first')` |  |
| `color_saturation_largest_first` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.greedy_color(G, strategy = 'saturation_largest_first')` |  |
| `color_smallest_last_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same two tests on nx.greedy_color(G, strategy = 'smallest_last') of the loop-free simple graph` |  |

**References:** [brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [matula1983smallest](../../references.html#matula1983smallest), [welsh1967upper](../../references.html#welsh1967upper)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
