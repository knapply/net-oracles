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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `average_clustering` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `transitivity_avglocal_undirected` |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, self-loops and ties): JGraphT's local clustering on a directed graph counts ordered pairs of neighbours (denominator k(k-1) per arc direction), while the reference, like... [details](#why-average_clustering-jgrapht) |  |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and self-loops): BGL's clustering\_coefficient counts parallel edges and loops as extra neighbours. [details](#why-average_clustering-boost) |  |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle... [details](#why-average_clustering-bct) |  |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the... [details](#why-average_clustering-gephi) |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-average_clustering-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-average_clustering-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (direction, multi-edges, self-loops and ties) on the fixtures gnp\_dir\_dense, gnp\_dir\_sparse, multi\_loops\_dir, multi\_loops\_und, real\_weights\_dir, weighted\_dir. JGraphT's local clustering on a directed graph counts ordered pairs of neighbours (denominator k(k-1) per arc direction), while the reference, like NetworkX and igraph, treats the neighbourhood as undirected; on a pseudograph JGraphT also counts loops and parallel edges, while the reference uses simple neighbour sets. Values agree whenever every arc is reciprocated (complete5\_dir). Relation to the reference value: Directed input, loops, parallel edges: counts ordered neighbour pairs on a directed graph (half the undirected-neighbourhood value), counts loops and parallel edges in a pseudograph. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-12 (0 means exact equality). 6 comparisons differ and 22 agree.
- <a id="why-average_clustering-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Boost Graph Library 1.90 was run and its value differs from the reference value by convention (direction, multi-edges and self-loops) on the fixtures multi\_loops\_und. BGL's clustering\_coefficient counts parallel edges and loops as extra neighbours; the reference uses simple neighbour sets. Relation to the reference value: Loops, parallel edges: counts them as extra neighbours; directed input not supported by the API. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-12 (0 means exact equality). 1 comparisons differ and 18 agree.
- <a id="why-average_clustering-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (direction) on the fixtures gnp\_dir\_dense, gnp\_dir\_sparse, multi\_loops\_dir, real\_weights\_dir, weighted\_dir. BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle types over the total degree; the reference takes the undirected neighbourhood. Undirected simple networks agree. Relation to the reference value: Directed input: clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients (triangle types weighed over the total degree), not the undirected-neighbourhood value; undirected simple networks agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-12 (0 means exact equality). 5 comparisons differ and 23 agree.
- <a id="why-average_clustering-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (multi-edges and self-loops) on the fixtures multi\_loops\_dir, multi\_loops\_und. Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the simple-graph definition, which this reference and the definition oracle follow; parallel edges do not change them (checked on multi\_loops\_und and multi\_loops\_dir). Relation to the reference value: Nodes of degree below 2: left out of the average (local value 0). Self-loops: a loop enters the neighbourhood; removing loops gives the simple-graph value. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-12 (0 means exact equality). 2 comparisons differ and 26 agree. Finding F021 (convention): Average clustering leaves out nodes of degree below 2. Findings: [F021](../../findings.html#f021).
- <a id="why-average_clustering-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `clustering` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `transitivity_local_undirected` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-clustering-graphtool) | `local_clustering` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `ClusteringCoefficient; LocalClusteringCoefficient; clustering` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-clustering-sknetwork) | `get_clustering_coefficient` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, self-loops and ties): JGraphT's local clustering on a directed graph counts ordered pairs of neighbours (denominator k(k-1) per arc direction), while the reference, like... [details](#why-clustering-jgrapht) | `ClusteringCoefficient` |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and self-loops): BGL's clustering\_coefficient counts parallel edges and loops as extra neighbours. [details](#why-clustering-boost) | `clustering_coefficient` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle... [details](#why-clustering-bct) | `clustering_coef_bd; clustering_coef_bu; clustering_coef_wd; clustering_coef_wu; clustering_coef_wu_sign` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the... [details](#why-clustering-gephi) | `ClusteringCoefficient` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-clustering-ucinet) | `Clustering coefficient (ClusteringCoefficient, nordcp, fagiolocc, oldcc CLI)` | published documentation |
| [tnet](../../tools/tnet.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `clustering_local_tm; clustering_local_w; clustering_tm; clustering_w` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-clustering-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: local\_clustering.
- <a id="why-clustering-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: get\_clustering\_coefficient.
- <a id="why-clustering-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (direction, multi-edges, self-loops and ties) on the fixtures gnp\_dir\_dense, gnp\_dir\_sparse, multi\_loops\_dir, multi\_loops\_und, real\_weights\_dir, weighted\_dir. JGraphT's local clustering on a directed graph counts ordered pairs of neighbours (denominator k(k-1) per arc direction), while the reference, like NetworkX and igraph, treats the neighbourhood as undirected; on a pseudograph JGraphT also counts loops and parallel edges, while the reference uses simple neighbour sets. Values agree whenever every arc is reciprocated (complete5\_dir). Relation to the reference value: Directed input, loops, parallel edges: counts ordered neighbour pairs on a directed graph (half the undirected-neighbourhood value), counts loops and parallel edges in a pseudograph. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 6 comparisons differ and 22 agree. Finding F051 (convention): Local clustering counts ordered neighbour pairs on directed input; counts loops and parallel edges in pseudographs. Findings: [F051](../../findings.html#f051).
- <a id="why-clustering-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Boost Graph Library 1.90 was run and its value differs from the reference value by convention (direction, multi-edges and self-loops) on the fixtures multi\_loops\_und. BGL's clustering\_coefficient counts parallel edges and loops as extra neighbours; the reference uses simple neighbour sets. Relation to the reference value: Loops, parallel edges: counts them as extra neighbours; directed input not supported by the API. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 1 comparisons differ and 18 agree. Finding F052 (convention): Clustering counts loops and parallel edges as extra neighbours. Findings: [F052](../../findings.html#f052).
- <a id="why-clustering-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (direction) on the fixtures gnp\_dir\_dense, gnp\_dir\_sparse, multi\_loops\_dir, real\_weights\_dir, weighted\_dir. BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle types over the total degree; the reference takes the undirected neighbourhood. Undirected simple networks agree. Relation to the reference value: Directed input: clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients (triangle types weighed over the total degree), not the undirected-neighbourhood value; undirected simple networks agree. Mapping: the reference value computed with Fagiolo's directed clustering (NetworkX's clustering of a DiGraph) agrees with the tool within abs 0, rel 1e-14 on all 5 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 5 comparisons differ and 23 agree. Finding F056 (convention): clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients. Findings: [F056](../../findings.html#f056).
- <a id="why-clustering-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (multi-edges and self-loops) on the fixtures multi\_loops\_dir, multi\_loops\_und. Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the simple-graph definition, which this reference and the definition oracle follow; parallel edges do not change them (checked on multi\_loops\_und and multi\_loops\_dir). Relation to the reference value: Self-loops: a loop enters the neighbourhood; removing loops gives the simple-graph value. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 2 comparisons differ and 26 agree.
- <a id="why-clustering-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](#why-nxo_directed_clustering-graphblas) |  |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxo_directed_clustering-graphblas"></a>**[GraphBLAS algorithms](../../tools/graphblas.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> GraphBLAS algorithms graphblas-algorithms 2023.10.0 (python-graphblas 2025.2.0, SuiteSparse:GraphBLAS 9.4.5.0) was run and its value differs from the reference value by convention (direction, multi-edges and weights) on inputs tagged multi\_edges. graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12; abs 1e-12, rel 1e-10 (0 means exact equality). 1 comparisons differ and 10 agree.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clustering_extended-graphtool) | `extended_clustering` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clustering_extended-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: extended\_clustering.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
