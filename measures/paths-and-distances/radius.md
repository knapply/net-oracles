---
title: "Radius"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Radius {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `radius`. 1 measure.

## Definition {#concept-definition}

The smallest eccentricity (NaN for a network without nodes).

## References {#concept-references}

[barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

## Radius {#radius}

Measure id: `radius`. Original family: Paths and distances.

**Definition.** The smallest eccentricity (NaN for a network without nodes).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-radius-networkx) | `radius` | API listing |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `radius` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `radius` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): JGraphT's GraphMeasurer follows edge direction and returns Infinity for a node that cannot reach every other node. [details](#why-radius-jgrapht) |  |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): BGL's all\_eccentricities and radius\_and\_diameter follow edge direction and give DBL\_MAX for a node that cannot reach every other node. [details](#why-radius-boost) |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and direction): charpath's radius is the minimum eccentricity over nodes that reach at least one other, so isolated nodes are ignored (the reference counts them as... [details](#why-radius-bct) |  |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-radius-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: radius.
- <a id="why-radius-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (direction) on the fixtures cycle7\_dir, empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, real\_weights\_dir, two\_triangles\_isolate, weighted\_dir. JGraphT's GraphMeasurer follows edge direction and returns Infinity for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) and over reachable nodes. Fixtures listed are directed or not connected. Relation to the reference value: Direction, unreachable: follow edge direction (the reference value's mode here ignores it); Infinity / DBL\_MAX when some node is unreachable. Mapping: the reference value computed with the tool's convention (infinity when some node cannot be reached, following arcs) agrees with the tool within abs 0, rel 0 on all 9 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 9 comparisons differ and 19 agree.
- <a id="why-radius-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Boost Graph Library 1.90 was run and its value differs from the reference value by convention (direction) on the fixtures cycle7\_dir, empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, real\_weights\_dir, two\_triangles\_isolate, weighted\_dir. BGL's all\_eccentricities and radius\_and\_diameter follow edge direction and give DBL\_MAX for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) over reachable nodes. Listed fixtures are directed or not connected. Relation to the reference value: Direction, unreachable: follow edge direction (the reference value's mode here ignores it); Infinity / DBL\_MAX when some node is unreachable. Mapping: the reference value computed with the tool's convention (infinity when some node cannot be reached, following arcs) agrees with the tool within abs 0, rel 0 on all 9 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 9 comparisons differ and 19 agree.
- <a id="why-radius-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (defaults and direction) on the fixtures cycle7\_dir, empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_und, real\_weights\_dir, single\_node, two\_triangles\_isolate, weighted\_dir. charpath's radius is the minimum eccentricity over nodes that reach at least one other, so isolated nodes are ignored (the reference counts them as 0), NaN when no node reaches another; it follows edge direction on directed networks. Relation to the reference value: Unreachable pairs, isolated nodes: charpath takes the longest finite distance (direction followed on directed input), NaN for a node reaching nobody, and a radius that ignores such nodes; NaN diameter for a network without edges. Mapping: the reference value computed with the tool's convention (largest finite distance along arcs, undefined for a node reaching none) agrees with the tool within abs 0, rel 0 on all 9 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 9 comparisons differ and 19 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `radius` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::radius(g without weights, mode = 'all')` |  |
| `radius` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [gu.radius(mode="all")]` |  |
| `radius` | JGraphT | any | differs |  | direction | abs 0, rel 0 | `JGraphT 1.5.2: new GraphMeasurer<>(g).getRadius() on a pseudograph` | JGraphT's GraphMeasurer follows edge direction and returns Infinity for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) and over reachable nodes. Fixtures listed are directed or not connected. |
| `radius` | Boost Graph Library | any | differs |  | direction | abs 0, rel 0 | `Boost Graph Library radius_and_diameter().first` | BGL's all\_eccentricities and radius\_and\_diameter follow edge direction and give DBL\_MAX for a node that cannot reach every other node; the reference value's eccentricity and radius here are in mode 'all' (direction ignored) over reachable nodes. Listed fixtures are directed or not connected. |
| `radius` | BCT (Octave) | any | differs |  | defaults, direction | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: charpath radius, on the binary adjacency matrix without loops or parallel edges` | charpath's radius is the minimum eccentricity over nodes that reach at least one other, so isolated nodes are ignored (the reference counts them as 0), NaN when no node reaches another; it follows edge direction on directed networks. |
| `radius` | bctpy | any | no-value-on-some-inputs | (no value) directed | defaults, direction | abs 0, rel 0 | `bct.charpath(D, include_infinite = False)[3]` | bctpy's charpath() keeps unreachable pairs in the eccentricities (reported as 1e20) even with include\_infinite = False, which only drops them from the characteristic path length; the reference ignores unreachable pairs. The radius is the smallest of those eccentricities. Directed fixtures are not passed (mode 'all'). |
| `radius` | Gephi toolkit | any | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: GraphDistance.getRadius() (setDirected(false))` |  |

**References:** [barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
