---
title: "Average clustering"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Average clustering

Family: Descriptive statistics. Identifier: `average_clustering`.

## Definition

Mean local clustering coefficient over the nodes.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `average_clustering` |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `transitivity_avglocal_undirected` |  |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees |  |  |
| [JGraphT](../tools/jgrapht.html) | ≠ checked, differs by convention |  |  |
| [Boost Graph Library](../tools/boost.html) | ≠ checked, differs by convention |  |  |
| [GraphBLAS algorithms](../tools/graphblas.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../tools/bct.html) | ≠ checked, differs by convention |  |  |
| [bctpy](../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../tools/gephi.html) | ≠ checked, differs by convention |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `average_clustering` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-12 | `igraph::transitivity(simplify(as_undirected(g)), type = 'average', isolates = 'NaN')` |  |
| `average_clustering` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-12 | `python-igraph: [su.transitivity_avglocal_undirected(mode="nan")]` |  |
| `average_clustering` | Gephi toolkit | any | differs |  | multi\_edges, self\_loops | abs 0, rel 1e-12 | `Gephi toolkit 0.11.3: ClusteringCoefficient.getAverageClusteringCoefficient() (setDirected(false))` | Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the simple-graph definition, which this reference and the definition oracle follow; parallel edges do not change them (checked on multi\_loops\_und and multi\_loops\_dir). |
| `average_clustering_onnela` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.average_clustering(G, weight = 'weight')` |  |
| `average_clustering_onnela` | bctpy | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `mean(bct.clustering_coef_wu(W / max(W)))` |  |
| `average_clustering_zero` | NetworkX | any | agrees |  |  | abs 0, rel 1e-12 | `nx.average_clustering(nx.Graph of the network, self-loops removed)` |  |
| `average_clustering_zero` | igraph (R) | any | no-value-on-some-inputs | (no value) null\_graph | defaults | abs 0, rel 1e-12 | `igraph::transitivity(simplify(as_undirected(g)), type = 'average', isolates = 'zero')` | The null graph has no nodes to average over; igraph returns 0, the reference reports undefined. |
| `average_clustering_zero` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-12 | `python-igraph: [su.transitivity_avglocal_undirected(mode="zero")]` |  |
| `average_clustering_zero` | NetworKit | any | agrees |  |  | abs 0, rel 1e-12 | `mean of nk.centrality.LocalClusteringCoefficient(G simple)` |  |
| `average_clustering_zero` | JGraphT | any | differs |  | direction, multi\_edges, self\_loops, ties | abs 0, rel 1e-12 | `JGraphT 1.5.2: new ClusteringCoefficient<>(g).getAverageClusteringCoefficient() on a pseudograph` | JGraphT's local clustering on a directed graph counts ordered pairs of neighbours (denominator k(k-1) per arc direction), while the reference, like NetworkX and igraph, treats the neighbourhood as undirected; on a pseudograph JGraphT also counts loops and parallel edges, while the reference uses simple neighbour sets. Values agree whenever every arc is reciprocated (complete5\_dir). |
| `average_clustering_zero` | Boost Graph Library | any | differs | (no value) directed | direction, multi\_edges, self\_loops | abs 0, rel 1e-12 | `Boost Graph Library mean_clustering_coefficient` | BGL's clustering\_coefficient counts parallel edges and loops as extra neighbours; the reference uses simple neighbour sets. BGL's mean\_clustering\_coefficient is defined for undirected graphs only; the driver does not call it on directed input. |
| `average_clustering_zero` | GraphBLAS algorithms | any | agrees |  |  | abs 0, rel 1e-12 | `nx.average_clustering(G simple without loops, backend = 'graphblas')` |  |
| `average_clustering_zero` | BCT (Octave) | any | differs |  | direction | abs 0, rel 1e-12 | `Brain Connectivity Toolbox 2019-03-03 in Octave: mean(clustering_coef_bu / _bd), on the binary adjacency matrix without loops or parallel edges` | BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle types over the total degree; the reference takes the undirected neighbourhood. Undirected simple networks agree. |
| `average_clustering_zero` | bctpy | any | agrees |  |  | abs 0, rel 1e-12 | `mean(bct.clustering_coef_bu(A binary, no diagonal))` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F021](../findings.html#f021) | Gephi toolkit | convention | Average clustering leaves out nodes of degree below 2 |

## References

[barrat2004architecture](../references.html#barrat2004architecture), [chiba1985arboricity](../references.html#chiba1985arboricity), [dial1969algorithm](../references.html#dial1969algorithm), [dijkstra1959note](../references.html#dijkstra1959note), [garlaschelli2004patterns](../references.html#garlaschelli2004patterns), [hage1995eccentricity](../references.html#hage1995eccentricity), [hopcroft1973algorithm](../references.html#hopcroft1973algorithm), [kaiser2008mean](../references.html#kaiser2008mean)

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [rubinov2010complex](../references.html#rubinov2010complex), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
