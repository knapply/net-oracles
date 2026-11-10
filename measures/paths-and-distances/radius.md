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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `radius` | API listing |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `radius` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `radius` |  |
| [JGraphT](../../tools/jgrapht.html) | ≠ checked, differs by convention |  |  |
| [Boost Graph Library](../../tools/boost.html) | ≠ checked, differs by convention |  |  |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention |  |  |
| [bctpy](../../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../../tools/gephi.html) | ✓ checked, agrees |  |  |

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
