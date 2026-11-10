---
title: "Eccentricity"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Eccentricity {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `eccentricity`. 1 measure.

## Definition {#concept-definition}

Each node's largest distance to the nodes it reaches.

## References {#concept-references}

[barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

## Eccentricity {#eccentricity}

Measure id: `eccentricity`. Original family: Paths and distances.

**Definition.** Each node's largest distance to the nodes it reaches.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `eccentricity` |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `eccentricity` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `eccentricity` |  |
| [NetworKit](../../tools/networkit.html) | ∅ checked, no value on some inputs | `Eccentricity` |  |
| [JGraphT](../../tools/jgrapht.html) | ≠ checked, differs by convention |  |  |
| [Boost Graph Library](../../tools/boost.html) | ≠ checked, differs by convention | `eccentricity` |  |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention |  |  |
| [bctpy](../../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../../tools/gephi.html) | ✓ checked, agrees |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Eccentricity, Radiality, Integration, Delta/fragmentation (fragcent CLI 6.746), DW fragmentation and reach` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `eccentricity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.eccentricity(G.to_undirected()) on connected networks; elsewhere the largest value of nx.single_source_shortest_path_length` |  |
| `eccentricity` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::eccentricity(g without weights, mode = 'all')` |  |
| `eccentricity` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: gu.eccentricity(mode="all")` |  |
| `eccentricity` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nk.distance.Eccentricity.getValue(G simple, v)` |  |
| `eccentricity` | JGraphT | any | differs |  | direction | abs 0, rel 0 | `JGraphT 1.5.2: new GraphMeasurer<>(g).getVertexEccentricityMap() on a pseudograph` | JGraphT's GraphMeasurer follows edge direction and returns Infinity for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) and over reachable nodes. Fixtures listed are directed or not connected. |
| `eccentricity` | Boost Graph Library | any | differs |  | direction | abs 0, rel 0 | `Boost Graph Library all_eccentricities` | BGL's all\_eccentricities and radius\_and\_diameter follow edge direction and give DBL\_MAX for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) over reachable nodes. Listed fixtures are directed or not connected. |
| `eccentricity` | BCT (Octave) | any | differs |  | defaults, direction | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: charpath eccentricity, on the binary adjacency matrix without loops or parallel edges` | charpath(distance\_bin(A), 0, 0) takes the longest finite distance and gives NaN to a node that reaches nobody; on directed networks it follows edge direction (the reference value's mode here ignores it). |
| `eccentricity` | bctpy | any | no-value-on-some-inputs | (no value) directed | defaults, direction | abs 0, rel 0 | `bct.charpath(D, include_infinite = False)[2]` | bctpy's charpath() keeps unreachable pairs in the eccentricities (reported as 1e20) even with include\_infinite = False, which only drops them from the characteristic path length; the reference ignores unreachable pairs. Directed fixtures are not passed: this variant (mode 'all') reads them as undirected, which charpath() does not do. |
| `eccentricity` | Gephi toolkit | any | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: GraphDistance (setDirected(false)), node column 'eccentricity'` |  |
| `eccentricity_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `largest value of nx.single_source_shortest_path_length(G.reverse(), v)` |  |
| `eccentricity_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.eccentricity(G) on strongly connected networks; elsewhere the largest value of nx.single_source_shortest_path_length` |  |
| `eccentricity_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::eccentricity(g without weights, mode = 'out')` |  |
| `eccentricity_out` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: gu.eccentricity(mode="out")` |  |
| `eccentricity_out` | JGraphT | directed | differs |  | direction | abs 0, rel 0 | `JGraphT 1.5.2: new GraphMeasurer<>(g).getVertexEccentricityMap() on a pseudograph` | JGraphT's GraphMeasurer returns Infinity for a node that cannot reach every other node along arcs; the reference returns the longest finite distance. The listed fixtures are the directed ones that are not strongly connected (agreement on the other four). |
| `eccentricity_out` | Boost Graph Library | directed | differs |  | direction | abs 0, rel 0 | `Boost Graph Library all_eccentricities over floyd_warshall_all_pairs_shortest_paths` | BGL's all\_eccentricities gives DBL\_MAX for a node that cannot reach every other node along arcs; the reference returns the longest finite distance. The listed fixtures are the directed ones that are not strongly connected (agreement on the other four). |
| `eccentricity_out` | Gephi toolkit | directed | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: GraphDistance (setDirected(true)), node column 'eccentricity'` |  |
| `eccentricity_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.eccentricity(G, weight = 'weight') on (strongly) connected networks; elsewhere the largest value of nx.single_source_dijkstra_path_length` |  |
| `eccentricity_weighted_strength` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `largest value of nx.single_source_dijkstra_path_length with length 1 / weight` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F049](../../findings.html#f049) | JGraphT | convention | Eccentricity, radius and diameter follow edge direction and return Infinity when a node is unreachable |
| [F050](../../findings.html#f050) | Boost Graph Library | convention | Eccentricity, radius and diameter return DBL\_MAX when a node is unreachable |
| [F057](../../findings.html#f057) | BCT (Octave) | convention | charpath takes the longest finite distance; NaN for a node reaching nobody |

**References:** [barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
