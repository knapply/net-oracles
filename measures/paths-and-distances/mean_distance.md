---
title: "Mean distance"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Mean distance {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `mean_distance`. 1 measure.

## Definition {#concept-definition}

Mean shortest-path distance over ordered pairs of distinct nodes joined by a path.

## References {#concept-references}

[barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

## Mean distance {#mean_distance}

Measure id: `mean_distance`. Original family: Paths and distances.

**Definition.** Mean shortest-path distance over ordered pairs of distinct nodes joined by a path.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `average_shortest_path_length` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `mean_distance` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `average_path_length; path_length_hist` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-mean_distance-rustworkx) | `digraph_unweighted_average_shortest_path_length; graph_unweighted_average_shortest_path_length; unweighted_average_shortest_path_length` | API listing |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-mean_distance-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-mean_distance-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_unweighted\_average\_shortest\_path\_length; graph\_unweighted\_average\_shortest\_path\_length; unweighted\_average\_shortest\_path\_length.
- <a id="why-mean_distance-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `mean_distance` | NetworkX | any | no-value-on-some-inputs |  | defaults | abs 0, rel 1e-14 | `mean of nx.all_pairs_shortest_path_length over distinct pairs (equal to nx.average_shortest_path_length where NetworkX defines it, which the oracle checks)` | No pair of distinct nodes is joined by a path, so the mean is 0 / 0 (NetworkX's average\_shortest\_path\_length returns 0 for one node and raises for the empty graph); not compared. |
| `mean_distance` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::mean_distance(g, directed = TRUE, unconnected = TRUE, weights = NA)` |  |
| `mean_distance` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-14 | `python-igraph: [gu.average_path_length(directed=True, unconn=True)]` |  |
| `mean_distance` | bctpy | any | agrees |  |  | abs 0, rel 1e-14 | `bct.charpath(D, include_diagonal = False, include_infinite = False)[0]` |  |
| `mean_distance` | Gephi toolkit | any | agrees |  |  | abs 0, rel 1e-14 | `Gephi toolkit 0.11.3: GraphDistance.getPathLength() (setDirected as the network)` |  |
| `mean_distance_all` | igraph (R) | directed | agrees |  |  | abs 0, rel 1e-14 | `igraph::mean_distance(g, directed = FALSE, unconnected = TRUE, weights = NA)` |  |
| `mean_distance_all` | igraph (Python) | directed | agrees |  |  | abs 0, rel 1e-14 | `python-igraph: [gu.average_path_length(directed=False, unconn=True)]` |  |
| `mean_distance_all` | Gephi toolkit | directed | agrees |  |  | abs 0, rel 1e-14 | `Gephi toolkit 0.11.3: GraphDistance.getPathLength() (setDirected(false))` |  |
| `mean_distance_connected` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::mean_distance(g, directed = TRUE, unconnected = FALSE, weights = NA)` |  |
| `mean_distance_connected` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-14 | `python-igraph: [gu.average_path_length(directed=True, unconn=False)]` |  |
| `mean_distance_in` | NetworkX | directed | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `mean of the finite lengths of nx.all_pairs_shortest_path_length(G.reverse())` | a network without nodes has no mean distance (the oracle writes nothing). |
| `mean_distance_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `mean of nx.all_pairs_dijkstra_path_length over distinct pairs` |  |
| `mean_distance_weighted` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-12 | `igraph::mean_distance(g, directed = TRUE, unconnected = TRUE, weights = E(g)$weight)` |  |
| `mean_distance_weighted` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-12 | `python-igraph: [g.average_path_length(directed=True, unconn=True, weights=w)]` |  |
| `mean_distance_weighted` | bctpy | any | agrees |  |  | abs 0, rel 1e-12 | `bct.charpath(distance_wei(L), include_infinite = False)[0]` |  |
| `mean_distance_weighted_strength` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `mean of the finite lengths of nx.all_pairs_dijkstra_path_length with length 1 / weight` |  |

**References:** [barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
