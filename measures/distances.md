---
title: "Distances"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Distances

Family: Paths and distances. Identifier: `distances`.

## Definition

Distances.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `distances` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `distances` |  |
| [sna](../tools/sna.html) | ✓ checked, agrees | `geodist` |  |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees | `GraphDistance` |  |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees |  |  |
| [scikit-network](../tools/sknetwork.html) | ✓ checked, agrees | `get_distances` |  |
| [JGraphT](../tools/jgrapht.html) | ✓ checked, agrees |  |  |
| [Boost Graph Library](../tools/boost.html) | ✓ checked, agrees | `geodesic_distance` |  |
| [GraphBLAS algorithms](../tools/graphblas.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../tools/bct.html) | ✓ checked, agrees | `distance_bin; distance_wei; distance_wei_floyd` |  |
| [bctpy](../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../tools/gephi.html) | · reported in docs | `GraphDistance` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Distance: geodesics (parallel routine 6.745), reachability, diameter, mean distance, compactness, breadth; floyd; geo` | published documentation |
| [tnet](../tools/tnet.html) | · reported in docs | `distance_tm; distance_w` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F078](../findings.html#f078) | tnet | defect | Weighted distance and closeness with the alpha exponent differ from the definition |

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [opsahl2010node](../references.html#opsahl2010node), [rubinov2010complex](../references.html#rubinov2010complex), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
