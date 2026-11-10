---
title: "Density"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Density {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Density and degree distribution. Concept id: `density`. 2 measures.

## Definition {#concept-definition}

Density. Entries grouped here: Density; Twomode / density.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Density](#density) | `density` | 11 |
| [Twomode / density](#twomode-density) | `twomode:density` | 2 |

## Density {#density}

Measure id: `density`. Original family: Descriptive statistics.

**Definition.** Density.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): NetworkX returns 0 for a graph with one node, where there are no possible edges. [details](#why-density-networkx) | `density` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `edge_density` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `density` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): sna works on adjacency matrices, so parallel edges collapse to one and self-loops are ignored. [details](#why-density-sna) | `gden` |  |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges, self-loops and ties): A network object holds each tie once and no loops (multiple = FALSE, loops = FALSE), so the edge count drops parallel edges and loops that this... [details](#why-density-ergm) | `density` |  |
| [RSiena](../../tools/rsiena.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-density-rsiena) | `density` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): The density of a one-node network is undefined (0/0): BCT returns NaN and the reference its undefined marker -1. [details](#why-density-bct) | `density_dir; density_und` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `GraphDensity` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-density-ucinet) | `Density (overall; also average degree in CLI, 6.790); density` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-density-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults) on inputs tagged edge\_case. density: NetworkX returns 0 for a graph with one node, where there are no possible edges; igraph, sna, and this reference report the density as undefined. density\_simple: NetworkX returns 0 for a graph with one node. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 2 comparisons differ and 86 agree.
- <a id="why-density-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (multi-edges and self-loops) on inputs tagged loops and multi\_edges. sna works on adjacency matrices, so parallel edges collapse to one and self-loops are ignored; the reference value's density of the simplified network (density\_simple) matches it. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0, rel 1e-14 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 5 comparisons differ and 83 agree.
- <a id="why-density-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> ergm (statnet) 4.12.0 was run and its value differs from the reference value by convention (multi-edges, self-loops and ties) on inputs tagged loops and multi\_edges. A network object holds each tie once and no loops (multiple = FALSE, loops = FALSE), so the edge count drops parallel edges and loops that this reference's edge count keeps. Relation to the reference value: Loops, parallel edges: a network object holds each tie once and no loops, so the edge count is lower than the reference value's on multigraphs. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0, rel 1e-14 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). No value (density\_simple) on the fixtures single\_node: ergm gives no density for a network of one node. 2 comparisons differ and 52 agree. Finding F070 (convention): A network object holds each tie once and no loops. Findings: [F070](../../findings.html#f070).
- <a id="why-density-rsiena"></a>**[RSiena](../../tools/rsiena.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. RSiena 1.6.6 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (RSiena exported functions and help titles; effects from getEffects()); API names: density.
- <a id="why-density-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (defaults) on the fixtures single\_node. The density of a one-node network is undefined (0/0): BCT returns NaN and the reference its undefined marker -1. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 1 comparisons differ and 27 agree.
- <a id="why-density-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `density` | NetworkX | any | differs | edge\_case | defaults | abs 0, rel 1e-14 | `nx.density(MultiGraph/MultiDiGraph)` | NetworkX returns 0 for a graph with one node, where there are no possible edges; igraph, sna, and this reference report the density as undefined. |
| `density` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::edge_density(g, loops = FALSE)` |  |
| `density` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-14 | `python-igraph: [g.density(loops=False)]` |  |
| `density` | sna | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 1e-14 | `sna::gden(m, mode = 'digraph' \| 'graph', diag = FALSE)` | sna works on adjacency matrices, so parallel edges collapse to one and self-loops are ignored; the reference value's density of the simplified network (density\_simple) matches it. |
| `density` | ergm (statnet) | any | differs | loops, multi\_edges | multi\_edges, self\_loops, ties | abs 0, rel 1e-14 | `summary(nw ~ edges) / possible pairs` | A network object holds each tie once and no loops (multiple = FALSE, loops = FALSE), so the edge count drops parallel edges and loops that this reference's edge count keeps. ergm gives no density for a network of one node. |
| `density` | Gephi toolkit | any | agrees |  |  | abs 0, rel 1e-14 | `Gephi toolkit 0.11.3: GraphDensity.getDensity() (setDirected as the network)` |  |
| `density_loops` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `igraph::edge_density(g, loops = TRUE)` |  |
| `density_loops` | igraph (Python) | any | agrees |  |  | abs 0, rel 1e-14 | `python-igraph: [g.density(loops=True)]` |  |
| `density_simple` | NetworkX | any | differs | edge\_case | defaults | abs 0, rel 1e-14 | `nx.density(nx.Graph/DiGraph without self-loops)` | NetworkX returns 0 for a graph with one node. |
| `density_simple` | sna | any | agrees |  |  | abs 0, rel 1e-14 | `sna::gden(m, mode = 'digraph' \| 'graph', diag = FALSE)` |  |
| `density_simple` | ergm (statnet) | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `summary(nw ~ edges) / possible pairs` | ergm gives no density for a network of one node. |
| `density_simple` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nk.graphtools.density(G simple)` |  |
| `density_simple` | BCT (Octave) | any | differs |  | defaults | abs 0, rel 1e-14 | `Brain Connectivity Toolbox 2019-03-03 in Octave: density_und / density_dir, on the binary adjacency matrix without loops or parallel edges` | The density of a one-node network is undefined (0/0): BCT returns NaN and the reference its undefined marker -1. |
| `density_simple` | bctpy | any | no-value-on-some-inputs |  | normalization | abs 0, rel 1e-14 | `bct.density_und(A binary) (density_dir when directed)` | density\_und() divides by n (n - 1) / 2 = 0 for one node (ZeroDivisionError). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F070](../../findings.html#f070) | ergm (statnet) | convention | A network object holds each tie once and no loops |

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [ripley2026manual](../../references.html#ripley2026manual), [rubinov2010complex](../../references.html#rubinov2010complex), [staudt2016networkit](../../references.html#staudt2016networkit)

## Twomode / density {#twomode-density}

Measure id: `twomode:density`. Original family: Two-mode and bipartite.

**Definition.** Twomode / density.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-twomode-density-ucinet) | `2-mode eigenvector, SVD, matching 2-mode, bipartite/density` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-twomode-density-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_density` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nx.bipartite.density(G, first_mode_nodes)` | one-mode fixture (no node types) |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
