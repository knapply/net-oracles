---
title: "Modularity maximization (Louvain, Leiden, greedy, spectral, exact)"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Modularity maximization (Louvain, Leiden, greedy, spectral, exact) {#concept-top}

Family: [Communities](index.html). Subfamily: Modularity-based detection. Concept id: `modularity_maximization`. 13 measures.

## Definition {#concept-definition}

A partition of maximum modularity found exactly by Russian doll search.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Fast greedy](#fast_greedy) | `fast_greedy` | 4 |
| [Greedy modularity](#cnx_greedy_modularity) | `cnx_greedy_modularity` | 2 |
| [Leading eigen](#leading_eigen) | `leading_eigen` | 3 |
| [Leiden](#leiden) | `leiden` | 6 |
| [Leiden seeded](#cnx_leiden_seeded) | `cnx_leiden_seeded` | 1 |
| [Louvain Hierarchy](#cat_hierarchy_louvain) | `cat_hierarchy_louvain` | 1 |
| [Louvain Iteration](#cat_iteration_louvain) | `cat_iteration_louvain` | 1 |
| [Louvain modularity](#louvain_modularity) | `louvain_modularity` | 7 |
| [Louvain quality](#louvain_quality) | `louvain_quality` | 3 |
| [Louvain seeded](#cnx_louvain_seeded) | `cnx_louvain_seeded` | 1 |
| [Naive greedy](#cnx_naive_greedy) | `cnx_naive_greedy` | 1 |
| [Naive greedy nx](#cnx_naive_greedy_nx) | `cnx_naive_greedy_nx` | 1 |
| [Optimal modularity](#optimal_modularity) | `optimal_modularity` | 2 |

## References {#concept-references}

[clauset2004finding](../../references.html#clauset2004finding), [newman2006modularity](../../references.html#newman2006modularity), [wu2000thick](../../references.html#wu2000thick), [traag2019louvain](../../references.html#traag2019louvain), [blondel2008fast](../../references.html#blondel2008fast), [dugue2015directed](../../references.html#dugue2015directed), [leicht2008community](../../references.html#leicht2008community), [newman2004analysis](../../references.html#newman2004analysis), [newman2004finding](../../references.html#newman2004finding), [reichardt2006statistical](../../references.html#reichardt2006statistical), [brandes2008modularity](../../references.html#brandes2008modularity)

## Fast greedy {#fast_greedy}

Measure id: `fast_greedy`. Original family: Communities.

**Definition.** Greedy modularity communities by repeated best mergers (Clauset, Newman and Moore); returns the best level, its modularity and the mergers.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `greedy_modularity_communities; naive_greedy_modularity_communities` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, self-loops, ties and weights): Exactly tied mergers on the greedy path are common (modularity gains are sums of small fractions): igraph breaks them by its own order and may reach... [details](#why-fast_greedy-igraph) | `cluster_fast_greedy` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-fast_greedy-pyigraph) | `community_fastgreedy` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-fast_greedy-ucinet) | `Community detection (6.7xx): FastGreedy, LabelProp, LocalGreedy (6.809), Louvain-type, Moca, Girvan-Newman, factor-analysis clustering, polish partitions, Initi; FastGreedy` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-fast_greedy-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (direction, multi-edges, self-loops, ties and weights) on inputs tagged directed and undirected. fast\_greedy: Exactly tied mergers on the greedy path are common (modularity gains are sums of small fractions): igraph breaks them by its own order and may reach a different dendrogram and best level. On networks without community structure (complete6, star8, two nodes and one edge) every merger along the reference value's path raises modularity and the path ends in one group (modularity 0), while igraph reports a partition of negative modularity. The definition oracle checks the reference. fast\_greedy\_weighted: Tied mergers as for fast\_greedy; and self-loops, which igraph drops (one node with a loop: igraph -1, the reference 0). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 15 comparisons differ and 12 agree.
- <a id="why-fast_greedy-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_fastgreedy.
- <a id="why-fast_greedy-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `fast_greedy` | NetworkX | undirected | no-value-on-some-inputs |  | ties | abs 1e-14, rel 1e-12 | `modularity of nx.community.greedy_modularity_communities(multigraph)` | NetworkX breaks ties between equally good mergers by the order of its floating-point heap, the reference by node order; on these fixtures the oracle verified in exact arithmetic that every merger NetworkX made was a best merger, so the two partitions differ only by tie-breaking |
| `fast_greedy` | igraph (R) | undirected | differs | directed, undirected, (no value) loops | direction, multi\_edges, self\_loops, ties, weights | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_fast_greedy(simplify(g, edge.attr.comb = 'sum'), weights = multiplicity)` | Exactly tied mergers on the greedy path are common (modularity gains are sums of small fractions): igraph breaks them by its own order and may reach a different dendrogram and best level. On networks without community structure (complete6, star8, two nodes and one edge) every merger along the reference value's path raises modularity and the path ends in one group (modularity 0), while igraph reports a partition of negative modularity. The definition oracle checks the reference. cluster\_fast\_greedy() needs a graph without multiple edges, so parallel edges are collapsed into weights, and the self-loops dropped with them count toward degree and modularity in the reference (as in NetworkX) but not in the simplified igraph graph; the listed fixtures have tied mergers on the greedy path (verified in exact arithmetic), which igraph breaks by its own order and so reaches a different partition. On complete6 and star8, which have no community structure, every merger along the reference value's path raises modularity and the path ends in one group (modularity 0), while igraph reports a partition of negative modularity (the oracle script skips these fixtures; on other graphs the tag declarations apply) |
| `fast_greedy_membership` | NetworkX | undirected | differs | directed, undirected | direction, ties | abs 0, rel 0 | `membership of nx.community.greedy_modularity_communities(multigraph)` | Exactly tied mergers: NetworkX's greedy\_modularity\_communities breaks ties by its heap and dict order, the reference by group number. as for fast\_greedy (the oracle script skips these fixtures; on other graphs the tag declarations apply) |
| `fast_greedy_resolution` | NetworkX | undirected | no-value-on-some-inputs |  | ties | abs 1e-14, rel 1e-12 | `modularity of nx.community.greedy_modularity_communities(G, resolution = 0.5)` | tie-breaking between equally good mergers, verified in exact arithmetic as for fast\_greedy |
| `fast_greedy_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `modularity of nx.community.greedy_modularity_communities(G, weight = 'weight')` |  |
| `fast_greedy_weighted` | igraph (R) | undirected | differs | directed, undirected | direction, self\_loops, ties, weights | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_fast_greedy(g, weights = E(g)$weight)` | Tied mergers as for fast\_greedy; and self-loops, which igraph drops (one node with a loop: igraph -1, the reference 0). the weighted greedy path has tied mergers on these fixtures (verified in exact arithmetic), which igraph breaks by its own order (the oracle script skips these fixtures; on other graphs the tag declarations apply) |

**References:** [clauset2004finding](../../references.html#clauset2004finding)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Greedy modularity {#cnx_greedy_modularity}

Measure id: `cnx_greedy_modularity`. Original family: Communities.

**Definition.** Greedy modularity.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cnx_greedy_modularity-jgrapht) | `GreedyModularityAlgorithm` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cnx_greedy_modularity-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GreedyModularityAlgorithm.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_greedy_modularity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.greedy_modularity_communities(G) on the simple undirected graph` |  |
| `nx_greedy_modularity_res` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.greedy_modularity_communities(G, resolution = 0.6) on the simple undirected graph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Leading eigen {#leading_eigen}

Measure id: `leading_eigen`. Original family: Communities.

**Definition.** Leading eigenvector communities by repeated modularity-matrix splits (Newman); returns the membership, its modularity and the number of splits.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, multi-edges, self-loops and ties): On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero... [details](#why-leading_eigen-igraph) | `cluster_leading_eigen` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-leading_eigen-pyigraph) | `community_leading_eigenvector` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-leading_eigen-ucinet) | `NCD` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-leading_eigen-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults, multi-edges, self-loops and ties) on inputs tagged disconnected and symmetric\_nodes and the fixtures mid\_plc\_und\_5000, mid\_plc\_und\_real\_3000. leading\_eigen: On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero components for isolated nodes), and the definition oracle declines; igraph's ARPACK vector and the reference value's then split differently. On the two size-tier power-law networks the modularities differ by 5e-7 (0.356872 against 0.356871): the division is decided by the signs of eigenvector entries, and the entries below the solvers' stopping tolerances are assigned differently (about one low-degree node). leading\_eigen\_membership: igraph puts each isolated node in a group of its own; the reference leaves isolated nodes, whose eigenvector components are zero, on the non-positive side of each division. Isolated nodes add nothing to modularity, so the modularity of the two partitions is the same (checked by leading\_eigen). With symmetric positions the leading eigenvector of a division can be repeated or have zero components, which the two place differently. leading\_eigen\_weighted: On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero components for isolated nodes), and the definition oracle declines; igraph's ARPACK vector and the reference value's then split differently. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12; abs 0, rel 0 (0 means exact equality). 14 comparisons differ and 46 agree. Finding F011 (convention): Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance. Findings: [F011](../../findings.html#f011).
- <a id="why-leading_eigen-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_leading\_eigenvector.
- <a id="why-leading_eigen-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `leading_eigen` | igraph (R) | undirected | differs | disconnected, (no value) edge\_case, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_leading_eigen(g) with the weight attribute removed` | On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero components for isolated nodes), and the definition oracle declines; igraph's ARPACK vector and the reference value's then split differently. On the two sized power-law networks the modularities differ by 5e-7 (0.356872 against 0.356871): the division is decided by the signs of eigenvector entries, and the entries below the solvers' stopping tolerances are assigned differently (about one low-degree node). kite and two\_triangles\_isolate have a degenerate leading eigenvalue (see the definition oracle), so the division is not unique; igraph's ARPACK-based routine is not run on multigraphs, networks with self-loops, or trivial networks, where its conventions for loops and its convergence are not those documented here |
| `leading_eigen_membership` | igraph (R) | undirected | differs | disconnected, symmetric\_nodes, (no value) edge\_case, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops, ties | abs 0, rel 0 | `igraph::membership(cluster_leading_eigen(g)) with the weight attribute removed` | igraph puts each isolated node in a group of its own; the reference leaves isolated nodes, whose eigenvector components are zero, on the non-positive side of each division. Isolated nodes add nothing to modularity, so the modularity of the two partitions is the same (checked by leading\_eigen). With symmetric positions the leading eigenvector of a division can be repeated or have zero components, which the two place differently. as for leading\_eigen (the oracle script skips these fixtures; on other graphs the tag declarations apply) |
| `leading_eigen_weighted` | igraph (R) | undirected | differs | disconnected | defaults | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_leading_eigen(g, weights = E(g)$weight)` | On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero components for isolated nodes), and the definition oracle declines; igraph's ARPACK vector and the reference value's then split differently. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F011](../../findings.html#f011) | igraph (R) | convention | Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance |

**References:** [newman2006modularity](../../references.html#newman2006modularity), [wu2000thick](../../references.html#wu2000thick)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph)

## Leiden {#leiden}

Measure id: `leiden`. Original family: Communities.

**Definition.** Leiden communities of an undirected network: local moving, refinement into connected groups and aggregation.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `leiden_communities; leiden_partitions` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `cluster_leiden` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-leiden-pyigraph) | `community_leiden` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-leiden-networkit) | `ParallelLeiden` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-leiden-sknetwork) | `Leiden` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-leiden-ucinet) | `localgreedy` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-leiden-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_leiden.
- <a id="why-leiden-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ParallelLeiden.
- <a id="why-leiden-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Leiden.
- <a id="why-leiden-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `leiden_cpm_quality` | igraph (R) | undirected | agrees |  |  | abs 0.015, rel 0 | `mean over set.seed(1..20) of the CPM quality (1/2m) sum_ij (A_ij - 0.1) delta of cluster_leiden(g, objective_function = 'CPM', resolution = 0.1, n_iterations = -1, weights = NA)` |  |
| `leiden_quality` | NetworkX | undirected | differs | edge\_case, loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0.03, rel 0 | `mean over seeds of modularity(G, leiden_communities(simple graph, metric = 'modularity', seed = s))` | NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0) |
| `leiden_quality` | igraph (R) | undirected | no-value-on-some-inputs |  |  | abs 0.03, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_leiden(g, objective_function = 'modularity', n_iterations = -1, weights = NA))` | igraph's cluster\_leiden() raises an error for a single node. |

**References:** [traag2019louvain](../../references.html#traag2019louvain)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)

## Leiden seeded {#cnx_leiden_seeded}

Measure id: `cnx_leiden_seeded`. Original family: Communities.

**Definition.** Leiden seeded.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_leiden_seeded` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `per node: community index under nx.community.leiden_communities(simple graph, seed=random.Random(7)) with metric 'cpm' and 'modularity' (NetworkX 3.7); -1 without edges` |  |
| `nx_leiden_seeded_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's communities` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Louvain Hierarchy {#cat_hierarchy_louvain}

Measure id: `cat_hierarchy_louvain`. Original family: Communities.

**Definition.** Louvain Hierarchy.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_hierarchy_louvain-sknetwork) | `LouvainHierarchy` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_hierarchy_louvain-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: LouvainHierarchy.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)

## Louvain Iteration {#cat_iteration_louvain}

Measure id: `cat_iteration_louvain`. Original family: Communities.

**Definition.** Louvain Iteration.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_iteration_louvain-sknetwork) | `LouvainIteration` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_iteration_louvain-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: LouvainIteration.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)

## Louvain modularity {#louvain_modularity}

Measure id: `louvain_modularity`. Original family: Communities.

**Definition.** Louvain communities of an undirected network by greedy modularity moves and aggregation.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): NetworkX returns 0 for a network without edges. [details](#why-louvain_modularity-networkx) | `louvain_communities; louvain_partitions` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-louvain_modularity-igraph) | `cluster_louvain` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-louvain_modularity-pyigraph) | `community_multilevel` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-louvain_modularity-networkit) | `LouvainMapEquation; PLM` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-louvain_modularity-sknetwork) | `Louvain` | API listing |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-louvain_modularity-bct) | `community_louvain; modularity_finetune_dir; modularity_finetune_und; modularity_finetune_und_sign; modularity_louvain_dir; modularity_louvain_und; modularity_louvain_und_sign; modularity_probtune_und_sign` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-louvain_modularity-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-louvain_modularity-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults) on inputs tagged edge\_case and edgeless. louvain\_modularity and louvain\_modularity\_resolution: NetworkX returns 0 for a network without edges; this reference returns NaN. louvain\_modularity\_weighted: Without edges modularity is 0 / 0; NetworkX returns 0, the reference NaN. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 2 comparisons differ and 63 agree.
- <a id="why-louvain_modularity-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: cluster\_louvain.
- <a id="why-louvain_modularity-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_multilevel.
- <a id="why-louvain_modularity-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LouvainMapEquation; PLM.
- <a id="why-louvain_modularity-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Louvain.
- <a id="why-louvain_modularity-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: community\_louvain; modularity\_finetune\_dir; modularity\_finetune\_und; modularity\_finetune\_und\_sign; modularity\_louvain\_dir; modularity\_louvain\_und; modularity\_louvain\_und\_sign; modularity\_probtune\_und\_sign.
- <a id="why-louvain_modularity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `louvain_modularity` | NetworkX | undirected | differs | edge\_case | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, reference partition, weight = None)` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_modularity_resolution` | NetworkX | undirected | differs | edge\_case | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, reference partition, resolution = 0.5)` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_modularity_weighted` | NetworkX | undirected | differs | edgeless | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, reference partition, weight = 'weight')` | Without edges modularity is 0 / 0; NetworkX returns 0, the reference NaN. |

**References:** [blondel2008fast](../../references.html#blondel2008fast), [dugue2015directed](../../references.html#dugue2015directed), [leicht2008community](../../references.html#leicht2008community), [newman2004analysis](../../references.html#newman2004analysis), [newman2004finding](../../references.html#newman2004finding), [newman2006modularity](../../references.html#newman2006modularity), [reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2019louvain](../../references.html#traag2019louvain)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)

## Louvain quality {#louvain_quality}

Measure id: `louvain_quality`. Original family: Communities.

**Definition.** Louvain communities of an undirected network by greedy modularity moves and aggregation.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and ties): NetworkX returns 0 for a network without edges. [details](#why-louvain_quality-networkx) |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and ties): Two different randomized procedures: the mean modularity over 20 seeds agrees within the tolerance on the corpus, but on small graphs the spread... [details](#why-louvain_quality-igraph) |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept). [details](#why-louvain_quality-gephi) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-louvain_quality-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults, direction and ties) on inputs tagged directed, edge\_case, edgeless and undirected. louvain\_quality and louvain\_quality\_resolution: NetworkX returns 0 for a network without edges; this reference returns NaN. louvain\_quality\_weighted: Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0.02, rel 0; abs 0.01, rel 0; abs 0.005, rel 0 (0 means exact equality). 2 comparisons differ and 63 agree.
- <a id="why-louvain_quality-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults, direction and ties) on inputs tagged directed and undirected. louvain\_quality: Two different randomized procedures: the mean modularity over 20 seeds agrees within the tolerance on the corpus, but on small graphs the spread between runs exceeds it (0.219 against 0.187 on 7 nodes); the comparison is statistical, not per run. louvain\_quality\_resolution and louvain\_quality\_weighted: Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0.02, rel 0; abs 0.01, rel 0; abs 0.005, rel 0 (0 means exact equality). 1 comparisons differ and 73 agree.
- <a id="why-louvain_quality-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (multi-edges and self-loops) on the fixtures multi\_loops\_und. With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept); the reference value and the definition oracle count a loop as degree 2, the standard modularity of a multigraph. Relation to the reference value: Self-loops: a loop enters the neighbourhood; removing loops gives the simple-graph value. Meaning: reciprocal of gamma; modularity reported at gamma = 1; runs not reproducible, sometimes non-terminating. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0.02, rel 0 (0 means exact equality). 1 comparisons differ and 23 agree. Finding F015 (defect): Louvain with setRandom(false) is not reproducible. Finding F016 (defect): Louvain sometimes does not return. Finding F022 (convention): Louvain resolution acts as the reciprocal of gamma. Findings: [F015](../../findings.html#f015), [F016](../../findings.html#f016), [F022](../../findings.html#f022).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `louvain_quality` | NetworkX | undirected | differs | edge\_case | defaults | abs 0.02, rel 0 | `mean over seeds 1..20 of modularity(G, louvain_communities(G, weight = None, seed = s))` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_quality` | igraph (R) | undirected | differs | directed, undirected | direction, ties | abs 0.02, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_louvain(g, weights = NA))` | Two different randomized procedures: the mean modularity over 20 seeds agrees within the tolerance on the corpus, but on small graphs the spread between runs exceeds it (0.219 against 0.187 on 7 nodes); the comparison is statistical, not per run. |
| `louvain_quality` | Gephi toolkit | undirected | differs |  | multi\_edges, self\_loops | abs 0.02, rel 0 | `Gephi toolkit 0.11.3: mean over 20 runs, on the main thread of a fresh JVM, of Modularity (setRandom(false), setUseWeight(false), setResolution(1.0)).getModularity(); an unseeded draw, fixed by the run order (see louvain_quality_weighted)` | With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept); the reference and the definition oracle count a loop as degree 2, the standard modularity of a multigraph. |
| `louvain_quality_resolution` | NetworkX | undirected | differs | edge\_case | defaults | abs 0.01, rel 0 | `mean over seeds 1..20 of modularity(G, louvain_communities(G, weight = None, resolution = 0.5, seed = s), resolution = 0.5)` | NetworkX returns 0 for a network without edges; this reference returns NaN. |
| `louvain_quality_resolution` | igraph (R) | undirected | differs | directed, undirected | defaults, direction, ties | abs 0.01, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_louvain(g, weights = NA, resolution = 0.5), resolution = 0.5)` | Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). |
| `louvain_quality_weighted` | NetworkX | undirected | differs | directed, edgeless, undirected | defaults, direction, ties | abs 0.005, rel 0 | `mean over seeds 1..20 of modularity(G, louvain_communities(G, weight = 'weight', seed = s), weight = 'weight')` | Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). |
| `louvain_quality_weighted` | igraph (R) | undirected | differs | directed, undirected | defaults, direction, ties | abs 0.005, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_louvain(g, weights = E(g)$weight), weights = E(g)$weight)` | Two different randomized procedures: the mean modularity over the seeds agrees within the tolerance on the corpus but not on every graph; the comparison is statistical, not per run (and without edges modularity is 0 / 0: the reference NaN, the tools 0). |
| `louvain_quality_weighted` | Gephi toolkit | undirected | agrees |  |  | abs 0.005, rel 0 | `Gephi toolkit 0.11.3: mean over 20 runs, on the main thread of a fresh JVM, of Modularity (setRandom(false), setUseWeight(true), setResolution(1.0)).getModularity()` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F015](../../findings.html#f015) | Gephi toolkit | defect | Louvain with setRandom(false) is not reproducible |
| [F016](../../findings.html#f016) | Gephi toolkit | defect | Louvain sometimes does not return |
| [F022](../../findings.html#f022) | Gephi toolkit | convention | Louvain resolution acts as the reciprocal of gamma |

**References:** [blondel2008fast](../../references.html#blondel2008fast), [dugue2015directed](../../references.html#dugue2015directed), [leicht2008community](../../references.html#leicht2008community), [newman2004analysis](../../references.html#newman2004analysis), [newman2004finding](../../references.html#newman2004finding), [newman2006modularity](../../references.html#newman2006modularity), [reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2019louvain](../../references.html#traag2019louvain)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Louvain seeded {#cnx_louvain_seeded}

Measure id: `cnx_louvain_seeded`. Original family: Communities.

**Definition.** Louvain seeded.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_louvain_seeded` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `per node: community index under nx.community.louvain_communities(simple graph, seed=random.Random(7)); -1 for a graph without edges` |  |
| `nx_louvain_seeded_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's communities` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Naive greedy {#cnx_naive_greedy}

Measure id: `cnx_naive_greedy`. Original family: Communities.

**Definition.** Naive greedy.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction and ties): Exactly tied merges: NetworkX compares whole-partition modularities summed in set order, so rounding decides. [details](#why-cnx_naive_greedy-networkx) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cnx_naive_greedy-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (direction and ties) on inputs tagged directed and undirected. Exactly tied merges: NetworkX compares whole-partition modularities summed in set order, so rounding decides; the reference compares gains and takes the first pair. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 2 comparisons differ and 26 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_naive_greedy_modularity` | NetworkX | any | differs | directed, undirected | direction, ties | abs 0, rel 0 | `nx.community.naive_greedy_modularity_communities(G) on the simple undirected graph` | Exactly tied merges: NetworkX compares whole-partition modularities summed in set order, so rounding decides; the reference compares gains and takes the first pair. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Naive greedy nx {#cnx_naive_greedy_nx}

Measure id: `cnx_naive_greedy_nx`. Original family: Communities.

**Definition.** Naive greedy nx.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_naive_greedy_exact` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.naive_greedy_modularity_communities(G) on the simple undirected graph: community index per node in NetworkX's order; -1 without edges` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Optimal modularity {#optimal_modularity}

Measure id: `optimal_modularity`. Original family: Communities.

**Definition.** A partition of maximum modularity found exactly by Russian doll search.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `cluster_optimal` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-optimal_modularity-pyigraph) | `community_optimal_modularity` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-optimal_modularity-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_optimal\_modularity.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `optimal_modularity` | igraph (R) | any | no-value-on-some-inputs |  | direction | abs 1e-14, rel 1e-12 | `modularity(cluster_optimal(g, weights = NULL))` | the exact search is not run on these larger fixtures (see the note above), and GLPK would take too long on several of them |
| `optimal_modularity_weighted` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `modularity(cluster_optimal(g, weights = E(g)$weight))` | as for optimal\_modularity |

**References:** [brandes2008modularity](../../references.html#brandes2008modularity)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
