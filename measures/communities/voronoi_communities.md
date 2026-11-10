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

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Community voronoi](#cat_community_voronoi) | `cat_community_voronoi` | 1 |
| [Voronoi](#voronoi) | `voronoi` | 1 |
| [Voronoi cells](#cat_cells_voronoi) | `cat_cells_voronoi` | 2 |

## Community voronoi {#cat_community_voronoi}

Measure id: `cat_community_voronoi`. Original family: Communities.

**Definition.** Community voronoi.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_community_voronoi-pyigraph) | `community_voronoi` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_community_voronoi-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_voronoi.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Voronoi {#voronoi}

Measure id: `voronoi`. Original family: Communities.

**Definition.** Voronoi.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, self-loops and ties): igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance. [details](#why-voronoi-igraph) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-voronoi-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (direction, multi-edges, self-loops and ties) on inputs tagged directed and undirected. igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance; where they differ the reference value's modularity is the higher. igraph's result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 14 comparisons differ and 11 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `voronoi_modularity` | igraph (R) | any | differs | directed, undirected, (no value) loops, (no value) multi\_edges | direction, multi\_edges, self\_loops, ties | abs 1e-14, rel 1e-12 | `set.seed(1); modularity of cluster_voronoi(g, weights = NULL, lengths = NULL, mode = 'out') (igraph 2.3: its internal community_voronoi_impl(g, mode = 'out', radius = -1))` | igraph chooses the radius with Brent's method, a local search, while the reference tries every distinct distance; where they differ the reference value's modularity is the higher. igraph's result also depends on the random number generator (the seed is fixed at 1). Listed for inspection, not expected to match igraph requires a simple network, and on cycle7\_dir its radius search stops with "optimizer did not converge" |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Voronoi cells {#cat_cells_voronoi}

Measure id: `cat_cells_voronoi`. Original family: Graph theory and combinatorics.

**Definition.** Voronoi cells.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_cells_voronoi-networkx) | `voronoi_cells` | API listing |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_cells_voronoi-igraph) | `voronoi_cells` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_cells_voronoi-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: voronoi\_cells.
- <a id="why-cat_cells_voronoi-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: voronoi\_cells.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
