---
title: "Shortest paths (Dijkstra, Bellman-Ford, A*, bidirectional)"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional) {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Shortest paths. Concept id: `shortest_paths`. 12 measures.

## Definition {#concept-definition}

Shortest-path lengths from one node by Delta-stepping; infinity for unreached nodes.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Astar](#ord_astar) | `ord_astar` | 1 |
| [Bellman ford](#ord_bellman_ford) | `ord_bellman_ford` | 5 |
| [Bidir bfs](#ord_bidir_bfs) | `ord_bidir_bfs` | 1 |
| [Bidir dijkstra](#ord_bidir_dijkstra) | `ord_bidir_dijkstra` | 1 |
| [Dijkstra](#ord_dijkstra) | `ord_dijkstra` | 1 |
| [Paths astar](#paths_astar) | `paths_astar` | 7 |
| [Paths bidirectional](#paths_bidirectional) | `paths_bidirectional` | 2 |
| [Paths multi source](#paths_multi_source) | `paths_multi_source` | 1 |
| [Paths negative](#paths_negative) | `paths_negative` | 1 |
| [Paths predecessors](#paths_predecessors) | `paths_predecessors` | 1 |
| [Paths sssp](#paths_sssp) | `paths_sssp` | 9 |
| [Retrieve shortest path](#cat_path_retrieve_shortest) | `cat_path_retrieve_shortest` | 1 |

## Astar {#ord_astar}

Measure id: `ord_astar`. Original family: Traversal, trees and DAGs.

**Definition.** Astar.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_astar` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.astar_path(M, 0, n - 1)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Bellman ford {#ord_bellman_ford}

Measure id: `ord_bellman_ford`. Original family: Traversal, trees and DAGs.

**Definition.** Bellman ford.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `bellman_ford_path; bellman_ford_path_length; bellman_ford_predecessor_and_distance; single_source_bellman_ford; single_source_bellman_ford_path; single_source_bellman_ford_path_length` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-ord_bellman_ford-graphtool) | `bellman_ford_search` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-ord_bellman_ford-rustworkx) | `bellman_ford_shortest_path_lengths; bellman_ford_shortest_paths; digraph_bellman_ford_shortest_path_lengths; digraph_bellman_ford_shortest_paths; graph_bellman_ford_shortest_path_lengths; graph_bellman_ford_shortest_paths` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-ord_bellman_ford-jgrapht) | `BellmanFordShortestPath` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-ord_bellman_ford-boost) | `bellman_ford_shortest_paths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ord_bellman_ford-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: bellman\_ford\_search.
- <a id="why-ord_bellman_ford-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: bellman\_ford\_shortest\_path\_lengths; bellman\_ford\_shortest\_paths; digraph\_bellman\_ford\_shortest\_path\_lengths; digraph\_bellman\_ford\_shortest\_paths; graph\_bellman\_ford\_shortest\_path\_lengths; graph\_bellman\_ford\_shortest\_paths.
- <a id="why-ord_bellman_ford-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BellmanFordShortestPath.
- <a id="why-ord_bellman_ford-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: bellman\_ford\_shortest\_paths.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bellman_ford` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bellman_ford_predecessor_and_distance(M, 0)` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F004](../../findings.html#f004) | NetworkX | defect | goldberg\_radzik raises NetworkXUnbounded for any negative self-loop |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Bidir bfs {#ord_bidir_bfs}

Measure id: `ord_bidir_bfs`. Original family: Traversal, trees and DAGs.

**Definition.** Bidir bfs.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bidir_bfs` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bidirectional_shortest_path(M, 0, n - 1)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Bidir dijkstra {#ord_bidir_dijkstra}

Measure id: `ord_bidir_dijkstra`. Original family: Traversal, trees and DAGs.

**Definition.** Bidir dijkstra.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bidir_dijkstra` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.bidirectional_dijkstra(M, 0, n - 1): path, then length` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Dijkstra {#ord_dijkstra}

Measure id: `ord_dijkstra`. Original family: Traversal, trees and DAGs.

**Definition.** Dijkstra.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ord_bfs_preds` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.dijkstra_predecessor_and_distance(M, 0, weight = None)[0]` |  |
| `ord_dijkstra_preds` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.dijkstra_predecessor_and_distance(M, 0)[0]` |  |
| `ord_dijkstra_unit` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.single_source_dijkstra(M, 0, weight = None): (node, distance, parent) in dict order` |  |
| `ord_dijkstra_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.single_source_dijkstra(M, 0)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Paths astar {#paths_astar}

Measure id: `paths_astar`. Original family: Paths and distances.

**Definition.** Paths astar.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `astar_path; astar_path_length` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_astar-pyigraph) | `get_shortest_path_astar` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_astar-graphtool) | `astar_iterator; astar_search` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_astar-networkit) | `AStar` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_astar-rustworkx) | `astar_shortest_path; digraph_astar_shortest_path; graph_astar_shortest_path` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_astar-jgrapht) | `AStarShortestPath; BidirectionalAStarShortestPath` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_astar-boost) | `astar_search` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_astar-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: get\_shortest\_path\_astar.
- <a id="why-paths_astar-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: astar\_iterator; astar\_search.
- <a id="why-paths_astar-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AStar.
- <a id="why-paths_astar-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: astar\_shortest\_path; digraph\_astar\_shortest\_path; graph\_astar\_shortest\_path.
- <a id="why-paths_astar-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: AStarShortestPath; BidirectionalAStarShortestPath.
- <a id="why-paths_astar-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: astar\_search.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_astar_exact` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.astar_path_length(G, s, t, heuristic = lambda u, v: d(u, t)) for every pair` |  |
| `paths_astar_half` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.astar_path_length(G, s, t, heuristic = lambda u, v: 0.5 d(u, t), weight = 'weight') for every pair` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Paths bidirectional {#paths_bidirectional}

Measure id: `paths_bidirectional`. Original family: Paths and distances.

**Definition.** Paths bidirectional.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `bidirectional_shortest_path` |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_bidirectional-networkit) | `BidirectionalBFS` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_bidirectional-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: BidirectionalBFS.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_bidirectional_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.bidirectional_shortest_path(G, s, t)) - 1 for every pair (no path: unreachable)` |  |
| `paths_bidirectional_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.bidirectional_dijkstra(G, s, t, weight = 'weight')[0] for every pair` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)

## Paths multi source {#paths_multi_source}

Measure id: `paths_multi_source`. Original family: Paths and distances.

**Definition.** Paths multi source.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_multi_source_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.multi_source_dijkstra_path_length(G, {0, n - 1}, weight = None)` |  |
| `paths_multi_source_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.multi_source_dijkstra_path_length(G, {0, n - 1}, weight = 'weight')` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Paths negative {#paths_negative}

Measure id: `paths_negative`. Original family: Paths and distances.

**Definition.** Paths negative.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `goldberg_radzik` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_bellman_ford_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_bellman_ford_path_length(G, 0, weight = 'len')` |  |
| `paths_bellman_ford_shift` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_bellman_ford_path_length(G, 0, weight = 'len'); NetworkXUnbounded is a negative cycle` |  |
| `paths_goldberg_radzik_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.goldberg_radzik(G, 0, weight = 'len')[1]` |  |
| `paths_goldberg_radzik_shift` | NetworkX | any | differs | loops | defaults, self\_loops | abs 1e-12, rel 1e-12 | `nx.goldberg_radzik(G, 0, weight = 'len')[1]; NetworkXUnbounded is a negative cycle` | NetworkX raises NetworkXUnbounded for any negative self-loop, reachable from the source or not (checked with nx.goldberg\_radzik and bellman\_ford\_predecessor\_and\_distance); the reference and the definition oracle report the unreachable node and no negative cycle. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Paths predecessors {#paths_predecessors}

Measure id: `paths_predecessors`. Original family: Paths and distances.

**Definition.** Paths predecessors.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `predecessor` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_predecessors_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.predecessor(G, 0)` |  |
| `paths_predecessors_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.dijkstra_predecessor_and_distance(G, 0, weight = 'weight')[0]` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Paths sssp {#paths_sssp}

Measure id: `paths_sssp`. Original family: Paths and distances.

**Definition.** Shortest-path lengths from one node by Delta-stepping; infinity for unreached nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `bidirectional_dijkstra; dijkstra_path; dijkstra_path_length; dijkstra_predecessor_and_distance; multi_source_dijkstra; multi_source_dijkstra_path; multi_source_dijkstra_path_length; shortest_path; shortest_path_length; single_source_all_shortest_paths; single_source_dijkstra; single_source_dijkstra_path` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-igraph) | `shortest_paths` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-pyigraph) | `get_shortest_path; get_shortest_paths` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-graphtool) | `all_predecessors; dijkstra_iterator; dijkstra_search; random_shortest_path; shortest_distance; shortest_path` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-networkit) | `BidirectionalDijkstra; Dijkstra; DynDijkstra; MultiTargetBFS; MultiTargetDijkstra; SSSP` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-rustworkx) | `digraph_dijkstra_search; digraph_dijkstra_shortest_path_lengths; digraph_dijkstra_shortest_paths; digraph_single_source_all_shortest_paths; dijkstra_search; dijkstra_shortest_path_lengths; dijkstra_shortest_paths; graph_dijkstra_search; graph_dijkstra_shortest_path_lengths; graph_dijkstra_shortest_paths; graph_single_source_all_shortest_paths; single_source_all_shortest_paths` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-sknetwork) | `get_shortest_path` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-jgrapht) | `BFSShortestPath; BidirectionalDijkstraShortestPath; ClosestFirstIterator; ContractionHierarchyBidirectionalDijkstra; DeltaSteppingShortestPath; DijkstraManyToManyShortestPaths; DijkstraShortestPath; IntVertexDijkstraShortestPath; MartinShortestPath` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_sssp-boost) | `dag_shortest_paths; dijkstra_shortest_paths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_sssp-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: shortest\_paths.
- <a id="why-paths_sssp-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: get\_shortest\_path; get\_shortest\_paths.
- <a id="why-paths_sssp-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: all\_predecessors; dijkstra\_iterator; dijkstra\_search; random\_shortest\_path; shortest\_distance; shortest\_path.
- <a id="why-paths_sssp-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: BidirectionalDijkstra; Dijkstra; DynDijkstra; MultiTargetBFS; MultiTargetDijkstra; SSSP.
- <a id="why-paths_sssp-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_dijkstra\_search; digraph\_dijkstra\_shortest\_path\_lengths; digraph\_dijkstra\_shortest\_paths; digraph\_single\_source\_all\_shortest\_paths; dijkstra\_search; dijkstra\_shortest\_path\_lengths; dijkstra\_shortest\_paths; graph\_dijkstra\_search; graph\_dijkstra\_shortest\_path\_lengths; graph\_dijkstra\_shortest\_paths; graph\_single\_source\_all\_shortest\_paths; single\_source\_all\_shortest\_paths.
- <a id="why-paths_sssp-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: get\_shortest\_path.
- <a id="why-paths_sssp-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BFSShortestPath; BidirectionalDijkstraShortestPath; ClosestFirstIterator; ContractionHierarchyBidirectionalDijkstra; DeltaSteppingShortestPath; DijkstraManyToManyShortestPaths; DijkstraShortestPath; IntVertexDijkstraShortestPath; MartinShortestPath.
- <a id="why-paths_sssp-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: dag\_shortest\_paths; dijkstra\_shortest\_paths.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_sssp_cutoff_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.single_source_shortest_path_length(G, s, cutoff = 2) for every s` |  |
| `paths_sssp_cutoff_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_dijkstra_path_length(G, s, cutoff = 2.5, weight = 'weight') for every s` |  |
| `paths_sssp_strength` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_dijkstra_path_length(G, s, weight = lambda u, v, d: min(1 / w)) for every s` |  |
| `paths_sssp_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.single_source_shortest_path_length(G, s) for every s` |  |
| `paths_sssp_unweighted_all` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.single_source_shortest_path_length(G.to_undirected(), s) for every s` |  |
| `paths_sssp_unweighted_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.single_target_shortest_path_length(G, s) for every s` |  |
| `paths_sssp_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.single_source_dijkstra_path_length(G, s, weight = 'weight') for every s` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Retrieve shortest path {#cat_path_retrieve_shortest}

Measure id: `cat_path_retrieve_shortest`. Original family: Paths and distances.

**Definition.** Retrieve shortest path.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_path_retrieve_shortest-bct) | `retrieve_shortest_path` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_path_retrieve_shortest-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: retrieve\_shortest\_path.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
