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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `density` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `edge_density` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `density` |  |
| [sna](../../tools/sna.html) | ≠ checked, differs by convention | `gden` |  |
| [ergm (statnet)](../../tools/ergm.html) | ≠ checked, differs by convention | `density` |  |
| [RSiena](../../tools/rsiena.html) | · reported in docs | `density` | API listing |
| [NetworKit](../../tools/networkit.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention | `density_dir; density_und` |  |
| [bctpy](../../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../../tools/gephi.html) | ✓ checked, agrees | `GraphDensity` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Density (overall; also average degree in CLI, 6.790); density` | published documentation |

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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `2-mode eigenvector, SVD, matching 2-mode, bipartite/density` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_density` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nx.bipartite.density(G, first_mode_nodes)` | one-mode fixture (no node types) |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
