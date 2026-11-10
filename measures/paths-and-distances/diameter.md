---
title: "Diameter"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Diameter {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `diameter`. 1 measure.

## Definition {#concept-definition}

Longest shortest-path distance.

## References {#concept-references}

[barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

## Diameter {#diameter}

Measure id: `diameter`. Original family: Paths and distances.

**Definition.** Longest shortest-path distance.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `diameter; harmonic_diameter` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `diameter; get_diameter` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `diameter; get_diameter` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-diameter-graphtool) | `pseudo_diameter` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `Diameter; DiameterAlgo; EffectiveDiameter` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (unreachable pairs): JGraphT's GraphMeasurer returns Infinity when some node cannot reach another. [details](#why-diameter-jgrapht) |  |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (unreachable pairs): BGL's radius\_and\_diameter gives DBL\_MAX when some node cannot reach another. [details](#why-diameter-boost) |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): charpath gives NaN where no node reaches another (empty and one-node networks). [details](#why-diameter-bct) | `charpath` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-diameter-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-diameter-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: pseudo\_diameter.
- <a id="why-diameter-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (unreachable pairs) on the fixtures empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, two\_triangles\_isolate, weighted\_dir. JGraphT's GraphMeasurer returns Infinity when some node cannot reach another; the reference reports the longest finite shortest path (unconnected: true). Fixtures listed are not (strongly) connected. Relation to the reference value: Unreachable pairs: Infinity / DBL\_MAX when any pair is unreachable; the reference returns the longest finite shortest path. Mapping: the reference value computed with the tool's convention (infinity when some pair is not joined) agrees with the tool within abs 0, rel 0 on all 8 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 8 comparisons differ and 20 agree.
- <a id="why-diameter-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Boost Graph Library 1.90 was run and its value differs from the reference value by convention (unreachable pairs) on the fixtures empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, two\_triangles\_isolate, weighted\_dir. BGL's radius\_and\_diameter gives DBL\_MAX when some node cannot reach another; the reference reports the longest finite shortest path (unconnected: true). Listed fixtures are not (strongly) connected. Relation to the reference value: Unreachable pairs: Infinity / DBL\_MAX when any pair is unreachable; the reference returns the longest finite shortest path. Mapping: the reference value computed with the tool's convention (infinity when some pair is not joined) agrees with the tool within abs 0, rel 0 on all 8 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 8 comparisons differ and 20 agree.
- <a id="why-diameter-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (defaults) on the fixtures empty, single\_node. charpath gives NaN where no node reaches another (empty and one-node networks); the reference returns 0. Relation to the reference value: Unreachable pairs, isolated nodes: charpath takes the longest finite distance (direction followed on directed input), NaN for a node reaching nobody, and a radius that ignores such nodes; NaN diameter for a network without edges. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 2 comparisons differ and 26 agree.
- <a id="why-diameter-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `diameter` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `largest value of nx.all_pairs_shortest_path_length (nx.diameter where NetworkX defines it, which the oracle checks)` |  |
| `diameter` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::diameter(g, directed = TRUE, unconnected = TRUE, weights = NA)` |  |
| `diameter` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [gu.diameter(directed=True, unconn=True)]` |  |
| `diameter` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nk.distance.Diameter(G simple, algo = DiameterAlgo.EXACT)` |  |
| `diameter` | JGraphT | any | differs |  |  | abs 0, rel 0 | `JGraphT 1.5.2: new GraphMeasurer<>(g).getDiameter() on a pseudograph` | JGraphT's GraphMeasurer returns Infinity when some node cannot reach another; the reference reports the longest finite shortest path. Fixtures listed are not (strongly) connected. |
| `diameter` | Boost Graph Library | any | differs |  |  | abs 0, rel 0 | `Boost Graph Library radius_and_diameter().second` | BGL's radius\_and\_diameter gives DBL\_MAX when some node cannot reach another; the reference reports the longest finite shortest path. Listed fixtures are not (strongly) connected. |
| `diameter` | BCT (Octave) | any | differs |  | defaults | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: charpath(distance_bin(A), 0, 0) diameter, on the binary adjacency matrix without loops or parallel edges` | charpath gives NaN where no node reaches another (empty and one-node networks); the reference returns 0. |
| `diameter` | bctpy | any | no-value-on-some-inputs |  | defaults | abs 0, rel 0 | `bct.charpath(D, include_infinite = False)[4]` | bctpy's charpath() keeps unreachable pairs in the eccentricities and the diameter (reported as 1e20) even with include\_infinite = False, which only drops them from the characteristic path length; the reference ignores unreachable pairs. |
| `diameter` | Gephi toolkit | any | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: GraphDistance.getDiameter() (setDirected as the network)` |  |
| `diameter_all` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::diameter(g, directed = FALSE, unconnected = TRUE, weights = NA)` |  |
| `diameter_all` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: [gu.diameter(directed=False, unconn=True)]` |  |
| `diameter_all` | Gephi toolkit | directed | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: GraphDistance.getDiameter() (setDirected(false))` |  |
| `diameter_connected` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::diameter(g, directed = TRUE, unconnected = FALSE, weights = NA)` |  |
| `diameter_connected` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [gu.diameter(directed=True, unconn=False)]` |  |
| `diameter_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `largest finite length of nx.all_pairs_shortest_path_length(G.reverse())` |  |
| `diameter_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `largest value of nx.all_pairs_dijkstra_path_length` |  |
| `diameter_weighted` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-12 | `igraph::diameter(g, directed = TRUE, unconnected = TRUE, weights = E(g)$weight)` |  |
| `diameter_weighted` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-12 | `python-igraph: [g.diameter(directed=True, unconn=True, weights=w)]` |  |
| `diameter_weighted` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `nk.distance.Diameter(G_weighted simple (shortest parallel edge), algo = DiameterAlgo.EXACT)` |  |
| `diameter_weighted` | bctpy | any | no-value-on-some-inputs |  | defaults | abs 0, rel 1e-12 | `bct.charpath(distance_wei(L), include_infinite = False)[4]` | bctpy's charpath() keeps unreachable pairs in the eccentricities and the diameter (reported as 1e20) even with include\_infinite = False, which only drops them from the characteristic path length; the reference ignores unreachable pairs. |
| `diameter_weighted_strength` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `largest finite length of nx.all_pairs_dijkstra_path_length with length 1 / weight` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F067](../../findings.html#f067) | NetworKit | defect | Exact diameter on a weighted graph returns whole numbers; weighted Laplacian differs by 5% to 10% |

**References:** [barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
