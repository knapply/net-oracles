---
title: "Local clustering coefficient"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Local clustering coefficient {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `local_clustering`. 4 measures.

## Definition {#concept-definition}

Mean local clustering coefficient over the nodes.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Average clustering](#average_clustering) | `average_clustering` | 11 |
| [Clustering](#clustering) | `clustering` | 14 |
| [Directed clustering](#nxo_directed_clustering) | `nxo_directed_clustering` | 3 |
| [Extended clustering](#cat_clustering_extended) | `cat_clustering_extended` | 1 |

## References {#concept-references}

[barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

## Average clustering {#average_clustering}

Measure id: `average_clustering`. Original family: Descriptive statistics.

**Definition.** Mean local clustering coefficient over the nodes.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `average_clustering` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `transitivity_avglocal_undirected` |  |
| [NetworKit](../../tools/networkit.html) | ✓ checked, agrees |  |  |
| [JGraphT](../../tools/jgrapht.html) | ≠ checked, differs by convention |  |  |
| [Boost Graph Library](../../tools/boost.html) | ≠ checked, differs by convention |  |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention |  |  |
| [bctpy](../../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../../tools/gephi.html) | ≠ checked, differs by convention |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F021](../../findings.html#f021) | Gephi toolkit | convention | Average clustering leaves out nodes of degree below 2 |

**References:** [barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)

## Clustering {#clustering}

Measure id: `clustering`. Original family: Descriptive statistics.

**Definition.** Local clustering coefficient of every node: the share of pairs of its neighbours that are tied.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `clustering` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `transitivity_local_undirected` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `local_clustering` | API listing |
| [NetworKit](../../tools/networkit.html) | ✓ checked, agrees | `ClusteringCoefficient; LocalClusteringCoefficient; clustering` |  |
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `get_clustering_coefficient` | API listing |
| [JGraphT](../../tools/jgrapht.html) | ≠ checked, differs by convention | `ClusteringCoefficient` |  |
| [Boost Graph Library](../../tools/boost.html) | ≠ checked, differs by convention | `clustering_coefficient` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention | `clustering_coef_bd; clustering_coef_bu; clustering_coef_wd; clustering_coef_wu; clustering_coef_wu_sign` |  |
| [bctpy](../../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../../tools/gephi.html) | ≠ checked, differs by convention | `ClusteringCoefficient` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Clustering coefficient (ClusteringCoefficient, nordcp, fagiolocc, oldcc CLI)` | published documentation |
| [tnet](../../tools/tnet.html) | ✓ checked, agrees | `clustering_local_tm; clustering_local_w; clustering_tm; clustering_w` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `clustering` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::transitivity(simplify(as_undirected(g)), type = 'local', isolates = 'NaN')` |  |
| `clustering` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-14 | `python-igraph: su.transitivity_local_undirected(mode="nan")` |  |
| `clustering` | NetworKit | any | agrees |  |  | abs 0, rel 1e-14 | `nk.centrality.LocalClusteringCoefficient(G simple, turbo = False), NaN below degree 2` |  |
| `clustering_barrat` | igraph (R) | undirected | differs | loops | defaults, self\_loops, ties, weights | abs 1e-14, rel 1e-12 | `igraph::transitivity(g, type = 'barrat', weights = E(g)$weight, isolates = 'NaN')` | Self-loops: a node whose only tie is a loop has no pair of distinct neighbours, so the reference reports it undefined; igraph counts the loop in the strength and degree and reports a number (2 for one loop of weight 1). |
| `clustering_barrat` | igraph (Python) | undirected | differs | loops | defaults, self\_loops, ties | abs 1e-14, rel 1e-12 | `python-igraph: g.transitivity_local_undirected(mode="nan", weights=w)` | Self-loops: a node whose only tie is a loop has no pair of distinct neighbours, so the reference reports it undefined; python-igraph reports 0. |
| `clustering_barrat` | tnet | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `tnet::clustering_local_w(net, measure = 'am')` |  |
| `clustering_onnela` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.clustering(G, weight = 'weight')` |  |
| `clustering_onnela` | bctpy | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `bct.clustering_coef_wu(W / max(W))` |  |
| `clustering_zero` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.clustering(nx.Graph of the network, self-loops removed)` |  |
| `clustering_zero` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::transitivity(simplify(as_undirected(g)), type = 'local', isolates = 'zero')` |  |
| `clustering_zero` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-14 | `python-igraph: su.transitivity_local_undirected(mode="zero")` |  |
| `clustering_zero` | NetworKit | any | agrees |  |  | abs 0, rel 1e-14 | `nk.centrality.LocalClusteringCoefficient(G simple, turbo = False)` |  |
| `clustering_zero` | JGraphT | any | differs |  | direction, multi\_edges, self\_loops, ties | abs 0, rel 1e-14 | `JGraphT 1.5.2: new ClusteringCoefficient<>(g).getScores() on a pseudograph` | JGraphT's local clustering on a directed graph counts ordered pairs of neighbours (denominator k(k-1) per arc direction), while the reference, like NetworkX and igraph, treats the neighbourhood as undirected; on a pseudograph JGraphT also counts loops and parallel edges, while the reference uses simple neighbour sets. Values agree whenever every arc is reciprocated (complete5\_dir). |
| `clustering_zero` | Boost Graph Library | any | differs | (no value) directed | direction, multi\_edges, self\_loops | abs 0, rel 1e-14 | `Boost Graph Library clustering_coefficient(g, v)` | BGL's clustering\_coefficient counts parallel edges and loops as extra neighbours; the reference uses simple neighbour sets. BGL's clustering\_coefficient, mean\_clustering\_coefficient and articulation\_points are defined for undirected graphs only; the driver does not call them on directed input. |
| `clustering_zero` | GraphBLAS algorithms | any | differs | multi\_edges | direction, multi\_edges, weights | abs 0, rel 1e-14 | `nx.clustering(G simple without loops, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |
| `clustering_zero` | BCT (Octave) | any | differs |  | direction | abs 0, rel 1e-14 | `Brain Connectivity Toolbox 2019-03-03 in Octave: clustering_coef_bu / clustering_coef_bd, on the binary adjacency matrix without loops or parallel edges` | BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle types over the total degree; the reference takes the undirected neighbourhood. Undirected simple networks agree. |
| `clustering_zero` | bctpy | any | agrees |  |  | abs 0, rel 1e-14 | `bct.clustering_coef_bu(A binary, no diagonal)` |  |
| `clustering_zero` | Gephi toolkit | any | differs |  | multi\_edges, self\_loops | abs 0, rel 1e-14 | `Gephi toolkit 0.11.3: ClusteringCoefficient (setDirected(false)), node column 'clustering'` | Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the simple-graph definition, which this reference and the definition oracle follow; parallel edges do not change them (checked on multi\_loops\_und and multi\_loops\_dir). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F051](../../findings.html#f051) | JGraphT | convention | Local clustering counts ordered neighbour pairs on directed input; counts loops and parallel edges in pseudographs |
| [F052](../../findings.html#f052) | Boost Graph Library | convention | Clustering counts loops and parallel edges as extra neighbours |
| [F056](../../findings.html#f056) | BCT (Octave) | convention | clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients |

**References:** [barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [opsahl2010node](../../references.html#opsahl2010node), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)

## Directed clustering {#nxo_directed_clustering}

Measure id: `nxo_directed_clustering`. Original family: Descriptive statistics.

**Definition.** Directed clustering.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | ≠ checked, differs by convention |  |  |
| [bctpy](../../tools/bctpy.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_directed_clustering` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.clustering(nx.DiGraph(G))` |  |
| `nxo_directed_clustering` | GraphBLAS algorithms | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-14, rel 1e-12 | `nx.clustering(DiGraph, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |
| `nxo_directed_clustering` | bctpy | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `bct.clustering_coef_bd(A binary, no diagonal)` |  |
| `nxo_directed_clustering_weighted` | NetworkX | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-12, rel 1e-10 | `nx.clustering(nx.DiGraph(G), weight = 'weight')` | nx.DiGraph(G) keeps the last of a pair's parallel arcs (and its weight); the reference keeps the first. |
| `nxo_directed_clustering_weighted` | GraphBLAS algorithms | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-12, rel 1e-10 | `nx.clustering(DiGraph, weight = 'weight', backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |
| `nxo_directed_clustering_weighted` | bctpy | directed | agrees |  |  | abs 1e-12, rel 1e-10 | `bct.clustering_coef_wd(W / max(W))` |  |

**Tools cited:** [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)

## Extended clustering {#cat_clustering_extended}

Measure id: `cat_clustering_extended`. Original family: Generators and rewiring.

**Definition.** Extended clustering.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `extended_clustering` | API listing |

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
