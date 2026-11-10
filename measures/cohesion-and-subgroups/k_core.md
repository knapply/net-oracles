---
title: "K-core decomposition"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-core decomposition {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cores, trusses and cohesive blocks. Concept id: `k_core`. 3 measures.

## Definition {#concept-definition}

K-core decomposition. Entries grouped here: Core Decomposition Sequence; Core subset; Coreness.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Core Decomposition Sequence](#cat_core_decomposition_sequence) | `cat_core_decomposition_sequence` | 1 |
| [Core subset](#core_subset) | `core_subset` | 1 |
| [Coreness](#coreness) | `coreness` | 13 |

## Core Decomposition Sequence {#cat_core_decomposition_sequence}

Measure id: `cat_core_decomposition_sequence`. Original family: Roles and positions.

**Definition.** Core Decomposition Sequence.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_core_decomposition_sequence-networkit) | `coreDecompositionSequence` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_core_decomposition_sequence-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: coreDecompositionSequence.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Core subset {#core_subset}

Measure id: `core_subset`. Original family: Cohesion and subgroups.

**Definition.** Core subset.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops. [details](#why-core_subset-networkx) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_subset-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and self-loops) on inputs tagged loops and multi\_edges. nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0, rel 0 on all 4 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 13 comparisons differ and 295 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `core_corona_k1` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_corona(G, k = 1) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_corona_k2` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_corona(G, k = 2) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_crust` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_crust(G) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_crust_k1` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_crust(G, k = 1) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_k2` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_core(G, k = 2) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_shell` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_shell(G) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_shell_k1` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_shell(G, k = 1) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Coreness {#coreness}

Measure id: `coreness`. Original family: Cohesion and subgroups.

**Definition.** Coreness.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and self-loops): nx.core\_number rejects self-loops and multigraphs, so it is run on the simple graph without loops. [details](#why-coreness-networkx) | `core_number; k_core; k_corona; k_crust; k_shell; onion_layers` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `coreness` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `coreness; k_core` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-coreness-sna) | `kcores` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-coreness-graphtool) | `kcore_decomposition` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `CoreDecomposition` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, normalization and self-loops): rx.core\_number() counts distinct neighbours and drops self-loops: given the fixture's multigraph it counts parallel edges once and ignores loops,... [details](#why-coreness-rustworkx) | `core_number; digraph_core_number; graph_core_number` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction and multi-edges): get\_core\_decomposition() peels by the row (out-) neighbours of the sparse matrix (topology/core.pyx), and a sparse matrix holds one entry per pair,... [details](#why-coreness-sknetwork) | `get_core_decomposition` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `Coreness` |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-coreness-boost) | `core_numbers` | API listing |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, self-loops and ties): A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops,... [details](#why-coreness-bct) | `kcore_bd; kcore_bu; kcoreness_centrality_bd; kcoreness_centrality_bu` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and ties): kcoreness\_centrality\_bu() takes a binary undirected matrix: a directed fixture enters symmetrized, so a reciprocated pair is one tie, and parallel... [details](#why-coreness-bctpy) |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-coreness-ucinet) | `Cohesion: k-cores, lambda sets, bicomponents, cut points, n-cliques, n-clans, k-plexes, cliques, factions; kcorelev` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-coreness-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (direction, multi-edges and self-loops) on inputs tagged loops and multi\_edges. nx.core\_number rejects self-loops and multigraphs, so it is run on the simple graph without loops. igraph and this reference count each parallel edge and count a loop in a node's degree (2 in undirected networks, 1 in and 1 out in directed networks). Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0, rel 0 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 5 comparisons differ and 39 agree.
- <a id="why-coreness-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: kcores.
- <a id="why-coreness-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: kcore\_decomposition.
- <a id="why-coreness-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> rustworkx 0.18.1 was run and its value differs from the reference value by convention (direction, multi-edges, normalization and self-loops) on inputs tagged directed, loops and multi\_edges. rx.core\_number() counts distinct neighbours and drops self-loops: given the fixture's multigraph it counts parallel edges once and ignores loops, and it reads a directed graph's in- and out-neighbours as one neighbourhood; the reference value's mode 'all' counts in- plus out- degree with every edge, a loop twice (igraph's convention). Mapping: the reference value computed with the binary undirected reading (as the adjacency-matrix reading, and a directed network symmetrized) agrees with the tool within abs 0, rel 0 on all 6 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 19 comparisons differ and 34 agree.
- <a id="why-coreness-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> scikit-network 0.33.0 was run and its value differs from the reference value by convention (direction and multi-edges) on inputs tagged directed and multi\_edges. get\_core\_decomposition() peels by the row (out-) neighbours of the sparse matrix (topology/core.pyx), and a sparse matrix holds one entry per pair, so parallel edges count once; the reference value's mode 'all' counts in- plus out-degree with every edge. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 9 comparisons differ and 19 agree.
- <a id="why-coreness-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: core\_numbers.
- <a id="why-coreness-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (direction, multi-edges, self-loops and ties) on the fixtures multi\_loops\_und. A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge. Relation to the reference value: Loops, parallel edges: a binary adjacency matrix carries neither; degrees, coreness, local efficiency differ on the two multigraph fixtures. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0, rel 0 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 18 agree.
- <a id="why-coreness-bctpy"></a>**[bctpy](../../tools/bctpy.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> bctpy 0.6.1 was run and its value differs from the reference value by convention (direction, multi-edges and ties) on inputs tagged directed and multi\_edges. kcoreness\_centrality\_bu() takes a binary undirected matrix: a directed fixture enters symmetrized, so a reciprocated pair is one tie, and parallel edges collapse; the reference value's mode 'all' counts in- plus out-degree with every edge (igraph's convention). Relation to the reference value: Loops, parallel edges: a binary adjacency matrix carries neither; degrees, coreness, local efficiency differ on the two multigraph fixtures. Mapping: the reference value computed with the binary undirected reading (as the adjacency-matrix reading, and a directed network symmetrized) agrees with the tool within abs 0, rel 0 on all 6 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 6 comparisons differ and 22 agree.
- <a id="why-coreness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `coreness_all` | NetworkX | any | differs | loops, multi\_edges | direction, multi\_edges, self\_loops | abs 0, rel 0 | `nx.core_number(nx.Graph(G) \| nx.DiGraph(G)) after removing self-loops` | nx.core\_number rejects self-loops and multigraphs, so it is run on the simple graph without loops. igraph and this reference count each parallel edge and count a loop in a node's degree (2 in undirected networks, 1 in and 1 out in directed networks). |
| `coreness_all` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::coreness(g, mode = 'all')` |  |
| `coreness_all` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: g.coreness(mode="all")` |  |
| `coreness_all` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nk.centrality.CoreDecomposition(G simple undirected)` |  |
| `coreness_all` | rustworkx | any | differs | directed, loops, multi\_edges | direction, multi\_edges, normalization, self\_loops | abs 0, rel 0 | `rx.core_number(G simple undirected)` | rx.core\_number() counts distinct neighbours and drops self-loops: given the fixture's multigraph it counts parallel edges once and ignores loops, and it reads a directed graph's in- and out-neighbours as one neighbourhood; the reference value's mode 'all' counts in- plus out- degree with every edge, a loop twice (igraph's convention). |
| `coreness_all` | scikit-network | any | differs | directed, multi\_edges | direction, multi\_edges | abs 0, rel 0 | `sknetwork.topology.get_core_decomposition(A simple symmetrized)` | get\_core\_decomposition() peels by the row (out-) neighbours of the sparse matrix (topology/core.pyx), and a sparse matrix holds one entry per pair, so parallel edges count once; the reference value's mode 'all' counts in- plus out-degree with every edge. |
| `coreness_all` | JGraphT | any | no-value-on-some-inputs | (no value) directed, (no value) loops, (no value) multi\_edges | direction, multi\_edges, self\_loops | abs 0, rel 0 | `JGraphT 1.5.2: new Coreness<>(g).getScores() on a pseudograph` | Coreness throws 'Graph must be undirected' on a directed graph and 'Graph must be simple' on loops or parallel edges. |
| `coreness_all` | BCT (Octave) | any | differs | (no value) directed | direction, multi\_edges, self\_loops, ties | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: kcoreness_centrality_bu, on the binary adjacency matrix without loops or parallel edges` | A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge. kcoreness\_centrality\_bu is defined for undirected matrices only. |
| `coreness_all` | bctpy | any | differs | directed, multi\_edges | direction, multi\_edges, ties | abs 0, rel 0 | `bct.kcoreness_centrality_bu(A binary)[0]` | kcoreness\_centrality\_bu() takes a binary undirected matrix: a directed fixture enters symmetrized, so a reciprocated pair is one tie, and parallel edges collapse; the reference value's mode 'all' counts in- plus out-degree with every edge (igraph's convention). |
| `coreness_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::coreness(g, mode = 'in')` |  |
| `coreness_in` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: g.coreness(mode="in")` |  |
| `coreness_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::coreness(g, mode = 'out')` |  |
| `coreness_out` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: g.coreness(mode="out")` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F054](../../findings.html#f054) | JGraphT | limitation | Coreness and clique finders refuse non-simple input |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
