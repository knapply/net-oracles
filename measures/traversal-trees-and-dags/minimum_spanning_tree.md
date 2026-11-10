---
title: "Minimum spanning tree"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum spanning tree {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Spanning trees and branchings. Concept id: `minimum_spanning_tree`. 3 measures.

## Definition {#concept-definition}

Minimum or maximum spanning forest of an undirected network, as input edge positions and total weight.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Mst weight](#gb_mst_weight) | `gb_mst_weight` | 1 |
| [Spanning tree](#spanning_tree) | `spanning_tree` | 8 |
| [Spanning weight](#spanning_weight) | `spanning_weight` | 5 |

## References {#concept-references}

[boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

## Mst weight {#gb_mst_weight}

Measure id: `gb_mst_weight`. Original family: Traversal, trees and DAGs.

**Definition.** Mst weight.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_mst_weight` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `sum of weights over nx.minimum_spanning_edges(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Spanning tree {#spanning_tree}

Measure id: `spanning_tree`. Original family: Traversal, trees and DAGs.

**Definition.** Minimum or maximum spanning forest of an undirected network, as input edge positions and total weight.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `maximum_spanning_edges; maximum_spanning_tree; minimum_spanning_edges; minimum_spanning_tree` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spanning_tree-igraph) | `mst` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spanning_tree-pyigraph) | `spanning_tree` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spanning_tree-graphtool) | `min_spanning_tree` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spanning_tree-networkit) | `KruskalMSF; PrimMSF; SpanningForest` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spanning_tree-rustworkx) | `minimum_spanning_edges; minimum_spanning_tree` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spanning_tree-jgrapht) | `BoruvkaMinimumSpanningTree; KruskalMinimumSpanningTree; PrimMinimumSpanningTree` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spanning_tree-boost) | `kruskal_minimum_spanning_tree; prim_minimum_spanning_tree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-spanning_tree-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: mst.
- <a id="why-spanning_tree-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: spanning\_tree.
- <a id="why-spanning_tree-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: min\_spanning\_tree.
- <a id="why-spanning_tree-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: KruskalMSF; PrimMSF; SpanningForest.
- <a id="why-spanning_tree-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: minimum\_spanning\_edges; minimum\_spanning\_tree.
- <a id="why-spanning_tree-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BoruvkaMinimumSpanningTree; KruskalMinimumSpanningTree; PrimMinimumSpanningTree.
- <a id="why-spanning_tree-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: kruskal\_minimum\_spanning\_tree; prim\_minimum\_spanning\_tree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `tree_maxst_edges_kruskal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.maximum_spanning_edges(M, algorithm = 'kruskal', keys = True) as (u, v, weight)` |  |
| `tree_mst_edges_boruvka` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_edges(M, algorithm = 'kruskal', keys = True)` |  |
| `tree_mst_edges_kruskal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_edges(M, algorithm = 'kruskal', keys = True) as (u, v, weight); the reference is given the edges in M.edges() order` |  |
| `tree_mst_edges_prim` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_edges(M, algorithm = 'kruskal', keys = True): every algorithm of the reference returns Kruskal's forest` |  |

**References:** [boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Spanning weight {#spanning_weight}

Measure id: `spanning_weight`. Original family: Traversal, trees and DAGs.

**Definition.** Minimum or maximum spanning forest of an undirected network, as input edge positions and total weight.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `tree_maxst_weight_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_spanning_tree(M, weight = 'weight').size(weight = 'weight')` |  |
| `tree_mst_weight` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.minimum_spanning_tree(M).size(weight = 'weight') on the multigraph` |  |
| `tree_mst_weight` | NetworKit | undirected | agrees |  |  | abs 0, rel 0 | `nk.graph.KruskalMSF(G with unit weights).getTotalWeight()` |  |
| `tree_mst_weight` | rustworkx | undirected | agrees |  |  | abs 0, rel 0 | `rx.minimum_spanning_edges(G, weight_fn = 1)` |  |
| `tree_mst_weight` | JGraphT | undirected | agrees |  |  | abs 0, rel 0 | `JGraphT 1.5.2: new KruskalMinimumSpanningTree<>(g).getSpanningTree().getWeight() on a pseudograph` |  |
| `tree_mst_weight` | Boost Graph Library | undirected | agrees |  |  | abs 0, rel 0 | `Boost Graph Library kruskal_minimum_spanning_tree (unit weights: tree edge count)` |  |
| `tree_mst_weight_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_spanning_tree(M, weight = 'weight').size(weight = 'weight')` |  |
| `tree_mst_weight_weighted` | NetworKit | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nk.graph.KruskalMSF(G_weighted).getTotalWeight()` |  |
| `tree_mst_weight_weighted` | rustworkx | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `rx.minimum_spanning_edges(G, weight_fn = float)` |  |
| `tree_mst_weight_weighted` | JGraphT | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `JGraphT 1.5.2: new KruskalMinimumSpanningTree<>(g_weighted).getSpanningTree().getWeight() on a pseudograph` |  |
| `tree_mst_weight_weighted` | Boost Graph Library | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `Boost Graph Library kruskal_minimum_spanning_tree` |  |

**References:** [boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
