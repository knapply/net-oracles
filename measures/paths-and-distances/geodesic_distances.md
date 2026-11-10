---
title: "Geodesic distances"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Geodesic distances {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Shortest paths. Concept id: `geodesic_distances`. 6 measures.

## Definition {#concept-definition}

Geodesic distances. Entries grouped here: Distances; Fw tree; Johnson lengths; Paths all pairs; Paths floyd warshall; Paths johnson.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Distances](#distances) | `distances` | 15 |
| [Fw tree](#nxs_fw_tree) | `nxs_fw_tree` | 1 |
| [Johnson lengths](#nxs_johnson_lengths) | `nxs_johnson_lengths` | 1 |
| [Paths all pairs](#paths_all_pairs) | `paths_all_pairs` | 4 |
| [Paths floyd warshall](#paths_floyd_warshall) | `paths_floyd_warshall` | 4 |
| [Paths johnson](#paths_johnson) | `paths_johnson` | 3 |

## Distances {#distances}

Measure id: `distances`. Original family: Paths and distances.

**Definition.** Distances.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `distances` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `distances` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `geodist` |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `GraphDistance` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `get_distances` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `geodesic_distance` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `distance_bin; distance_wei; distance_wei_floyd` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-distances-gephi) | `GraphDistance` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-distances-ucinet) | `Distance: geodesics (parallel routine 6.745), reachability, diameter, mean distance, compactness, breadth; floyd; geo` | published documentation |
| [tnet](../../tools/tnet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-distances-tnet) | `distance_tm; distance_w` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-distances-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Gephi toolkit 0.11.3 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Gephi toolkit 0.11.3 javadoc (published class list of org.gephi.statistics.plugin)); API names: GraphDistance.
- <a id="why-distances-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-distances-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: distance\_tm; distance\_w.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `distances` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.all_pairs_shortest_path_length(G)` |  |
| `distances` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::distances(g, mode = 'out', weights = NA)` |  |
| `distances` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: flat(gu.distances(mode="out"))` |  |
| `distances` | sna | any | agrees |  |  | abs 0, rel 0 | `sna::geodist(m without its diagonal)$gdist` |  |
| `distances` | NetworKit | any | agrees |  |  | abs 0, rel 0 | `nk.distance.APSP(G).getDistances()` |  |
| `distances` | rustworkx | any | agrees |  |  | abs 0, rel 0 | `rx.digraph_distance_matrix(G, null_value = inf) (graph_distance_matrix when undirected)` |  |
| `distances` | scikit-network | any | no-value-on-some-inputs |  | defaults | abs 0, rel 0 | `sknetwork.path.get_distances(A simple, source = s) for each s` | scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `distances` | JGraphT | any | agrees |  |  | abs 0, rel 0 | `JGraphT 1.5.2: DijkstraShortestPath(g).getPathWeight(i, j) on a pseudograph` |  |
| `distances` | Boost Graph Library | any | agrees |  |  | abs 0, rel 0 | `Boost Graph Library floyd_warshall_all_pairs_shortest_paths (unit weights)` |  |
| `distances` | GraphBLAS algorithms | any | agrees |  |  | abs 0, rel 0 | `nx.single_source_shortest_path_length(G simple, s, backend = 'graphblas') for each s` |  |
| `distances` | BCT (Octave) | any | agrees |  |  | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: distance_bin, on the binary adjacency matrix without loops or parallel edges` |  |
| `distances` | bctpy | any | agrees |  |  | abs 0, rel 0 | `bct.distance_bin(A binary)` |  |
| `distances_all` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.all_pairs_shortest_path_length(G.to_undirected())` |  |
| `distances_all` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::distances(g, mode = 'all', weights = NA)` |  |
| `distances_all` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: flat(gu.distances(mode="all"))` |  |
| `distances_all` | NetworKit | directed | agrees |  |  | abs 0, rel 0 | `nk.distance.APSP(undirected G).getDistances()` |  |
| `distances_all` | rustworkx | directed | agrees |  |  | abs 0, rel 0 | `rx.graph_distance_matrix(undirected G, null_value = inf)` |  |
| `distances_all` | scikit-network | directed | no-value-on-some-inputs |  | defaults | abs 0, rel 0 | `sknetwork.path.get_distances(A simple symmetrized, source = s) for each s` | scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `distances_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.all_pairs_shortest_path_length(G.reverse())` |  |
| `distances_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::distances(g, mode = 'in', weights = NA)` |  |
| `distances_in` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: flat(gu.distances(mode="in"))` |  |
| `distances_weighted` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.all_pairs_dijkstra_path_length(G, weight = 'weight')` |  |
| `distances_weighted` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::distances(g, mode = 'out', weights = E(g)$weight)` |  |
| `distances_weighted` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: flat(g.distances(mode="out", weights=w))` |  |
| `distances_weighted` | NetworKit | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nk.distance.APSP(G_weighted).getDistances()` |  |
| `distances_weighted` | rustworkx | any | agrees |  |  | abs 1e-14, rel 1e-12 | `rx.floyd_warshall_numpy(G, weight_fn = float)` |  |
| `distances_weighted` | JGraphT | any | agrees |  |  | abs 1e-14, rel 1e-12 | `JGraphT 1.5.2: DijkstraShortestPath(g_weighted).getPathWeight(i, j) on a pseudograph` |  |
| `distances_weighted` | Boost Graph Library | any | agrees |  |  | abs 1e-14, rel 1e-12 | `Boost Graph Library floyd_warshall_all_pairs_shortest_paths(weight_map)` |  |
| `distances_weighted` | bctpy | any | agrees |  |  | abs 1e-14, rel 1e-12 | `bct.distance_wei(L)[0]` |  |
| `distances_weighted_strength` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::distances(g, mode = 'out', weights = 1 / E(g)$weight)` |  |
| `distances_weighted_strength` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: flat(g.distances( mode="out", weights=[1 / x for x in g.es["weight"]]))` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F078](../../findings.html#f078) | tnet | defect | Weighted distance and closeness with the alpha exponent differ from the definition |

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [opsahl2010node](../../references.html#opsahl2010node), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Fw tree {#nxs_fw_tree}

Measure id: `nxs_fw_tree`. Original family: Graph theory and combinatorics.

**Definition.** Fw tree.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_fw_tree_dist` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall_tree(G): finite distances, sorted` |  |
| `nxs_fw_tree_dist_negative` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall_tree(DAG): finite distances, sorted` |  |
| `nxs_fw_tree_pred` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.floyd_warshall_tree(G): predecessor entries, sorted` |  |
| `nxs_fw_tree_pred_negative` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.floyd_warshall_tree(DAG): predecessor entries, sorted` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Johnson lengths {#nxs_johnson_lengths}

Measure id: `nxs_johnson_lengths`. Original family: Paths and distances.

**Definition.** Johnson lengths.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_johnson_lengths` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `the same from nx.single_source_bellman_ford_path_length on the graph with a zero-length source arc to every node` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Paths all pairs {#paths_all_pairs}

Measure id: `paths_all_pairs`. Original family: Paths and distances.

**Definition.** Paths all pairs.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `all_pairs_all_shortest_paths; all_pairs_bellman_ford_path; all_pairs_bellman_ford_path_length; all_pairs_dijkstra; all_pairs_dijkstra_path; all_pairs_dijkstra_path_length; all_pairs_lowest_common_ancestor; all_pairs_node_connectivity; all_pairs_shortest_path; all_pairs_shortest_path_length; floyd_warshall_numpy` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_all_pairs-igraph) | `distance_table` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_all_pairs-networkit) | `APSP; DynAPSP` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_all_pairs-rustworkx) | `all_pairs_all_simple_paths; all_pairs_bellman_ford_path_lengths; all_pairs_bellman_ford_shortest_paths; all_pairs_dijkstra_path_lengths; all_pairs_dijkstra_shortest_paths; digraph_all_pairs_all_simple_paths; digraph_all_pairs_bellman_ford_path_lengths; digraph_all_pairs_bellman_ford_shortest_paths; digraph_all_pairs_dijkstra_path_lengths; digraph_all_pairs_dijkstra_shortest_paths; digraph_distance_matrix; digraph_floyd_warshall_numpy` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_all_pairs-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: distance\_table.
- <a id="why-paths_all_pairs-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: APSP; DynAPSP.
- <a id="why-paths_all_pairs-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: all\_pairs\_all\_simple\_paths; all\_pairs\_bellman\_ford\_path\_lengths; all\_pairs\_bellman\_ford\_shortest\_paths; all\_pairs\_dijkstra\_path\_lengths; all\_pairs\_dijkstra\_shortest\_paths; digraph\_all\_pairs\_all\_simple\_paths; digraph\_all\_pairs\_bellman\_ford\_path\_lengths; digraph\_all\_pairs\_bellman\_ford\_shortest\_paths; digraph\_all\_pairs\_dijkstra\_path\_lengths; digraph\_all\_pairs\_dijkstra\_shortest\_paths; digraph\_distance\_matrix; digraph\_floyd\_warshall\_numpy.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_all_pairs_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `dict(nx.all_pairs_shortest_path_length(G))` |  |
| `paths_all_pairs_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `dict(nx.all_pairs_dijkstra_path_length(G, weight = 'weight'))` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Paths floyd warshall {#paths_floyd_warshall}

Measure id: `paths_floyd_warshall`. Original family: Paths and distances.

**Definition.** Paths floyd warshall.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `floyd_warshall; floyd_warshall_predecessor_and_distance; floyd_warshall_tree` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_floyd_warshall-rustworkx) | `digraph_floyd_warshall; digraph_floyd_warshall_successor_and_distance; floyd_warshall; floyd_warshall_successor_and_distance; graph_floyd_warshall; graph_floyd_warshall_successor_and_distance` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_floyd_warshall-jgrapht) | `FloydWarshallShortestPaths` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_floyd_warshall-boost) | `floyd_warshall_all_pairs_shortest_paths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_floyd_warshall-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_floyd\_warshall; digraph\_floyd\_warshall\_successor\_and\_distance; floyd\_warshall; floyd\_warshall\_successor\_and\_distance; graph\_floyd\_warshall; graph\_floyd\_warshall\_successor\_and\_distance.
- <a id="why-paths_floyd_warshall-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: FloydWarshallShortestPaths.
- <a id="why-paths_floyd_warshall-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: floyd\_warshall\_all\_pairs\_shortest\_paths.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_floyd_warshall_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall(G, weight = 'len')` |  |
| `paths_floyd_warshall_shift` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall(G, weight = 'len'); NetworkXUnbounded is a negative cycle` |  |
| `paths_floyd_warshall_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.floyd_warshall(G, weight = 'weight')` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Paths johnson {#paths_johnson}

Measure id: `paths_johnson`. Original family: Paths and distances.

**Definition.** Paths johnson.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `johnson` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_johnson-jgrapht) | `JohnsonShortestPaths` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_johnson-boost) | `johnson_all_pairs_shortest_paths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_johnson-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: JohnsonShortestPaths.
- <a id="why-paths_johnson-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: johnson\_all\_pairs\_shortest\_paths.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_johnson_potential` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.johnson(G, weight = 'len'), each path's length summed in order` |  |
| `paths_johnson_shift` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.johnson(G, weight = 'len'); NetworkXUnbounded is a negative cycle` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
