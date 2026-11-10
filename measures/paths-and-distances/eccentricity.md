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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `eccentricity` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `eccentricity` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `eccentricity` |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `Eccentricity` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): JGraphT's GraphMeasurer follows edge direction and returns Infinity for a node that cannot reach every other node. [details](#why-eccentricity-jgrapht) |  |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): BGL's all\_eccentricities and radius\_and\_diameter follow edge direction and give DBL\_MAX for a node that cannot reach every other node. [details](#why-eccentricity-boost) | `eccentricity` |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and direction): charpath(distance\_bin(A), 0, 0) takes the longest finite distance and gives NaN to a node that reaches nobody. [details](#why-eccentricity-bct) |  |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-eccentricity-ucinet) | `Eccentricity, Radiality, Integration, Delta/fragmentation (fragcent CLI 6.746), DW fragmentation and reach` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-eccentricity-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (direction) on the fixtures cycle7\_dir, empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, real\_weights\_dir, two\_triangles\_isolate, weighted\_dir. eccentricity: JGraphT's GraphMeasurer follows edge direction and returns Infinity for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) and over reachable nodes. Fixtures listed are directed or not connected. eccentricity\_out: JGraphT's GraphMeasurer returns Infinity for a node that cannot reach every other node along arcs; the reference returns the longest finite distance. The listed fixtures are the directed ones that are not strongly connected (agreement on the other four). Relation to the reference value: Direction, unreachable: follow edge direction (the reference value's mode here ignores it); Infinity / DBL\_MAX when some node is unreachable. Mapping: the reference value computed with the tool's convention (infinity when some node cannot be reached, following arcs) agrees with the tool within abs 0, rel 0 on all 15 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 15 comparisons differ and 22 agree. Finding F049 (convention): Eccentricity, radius and diameter follow edge direction and return Infinity when a node is unreachable. Findings: [F049](../../findings.html#f049).
- <a id="why-eccentricity-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Boost Graph Library 1.90 was run and its value differs from the reference value by convention (direction) on the fixtures cycle7\_dir, empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, real\_weights\_dir, two\_triangles\_isolate, weighted\_dir. eccentricity: BGL's all\_eccentricities and radius\_and\_diameter follow edge direction and give DBL\_MAX for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) over reachable nodes. Listed fixtures are directed or not connected. eccentricity\_out: BGL's all\_eccentricities gives DBL\_MAX for a node that cannot reach every other node along arcs; the reference returns the longest finite distance. The listed fixtures are the directed ones that are not strongly connected (agreement on the other four). Relation to the reference value: Direction, unreachable: follow edge direction (the reference value's mode here ignores it); Infinity / DBL\_MAX when some node is unreachable. Mapping: the reference value computed with the tool's convention (infinity when some node cannot be reached, following arcs) agrees with the tool within abs 0, rel 0 on all 15 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 15 comparisons differ and 22 agree. Finding F050 (convention): Eccentricity, radius and diameter return DBL\_MAX when a node is unreachable. Findings: [F050](../../findings.html#f050).
- <a id="why-eccentricity-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (defaults and direction) on the fixtures cycle7\_dir, empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, real\_weights\_dir, single\_node, two\_triangles\_isolate, weighted\_dir. charpath(distance\_bin(A), 0, 0) takes the longest finite distance and gives NaN to a node that reaches nobody; on directed networks it follows edge direction (the reference value's mode here ignores it). Relation to the reference value: Unreachable pairs, isolated nodes: charpath takes the longest finite distance (direction followed on directed input), NaN for a node reaching nobody, and a radius that ignores such nodes; NaN diameter for a network without edges. Mapping: the reference value computed with the tool's convention (largest finite distance along arcs, undefined for a node reaching none) agrees with the tool within abs 0, rel 0 on all 11 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 11 comparisons differ and 17 agree. Finding F057 (convention): charpath takes the longest finite distance; NaN for a node reaching nobody. Findings: [F057](../../findings.html#f057).
- <a id="why-eccentricity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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
