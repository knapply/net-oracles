---
title: "Coreness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Coreness

Family: Cohesion and subgroups. Identifier: `coreness`.

## Definition

Coreness.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `core_number; k_core; k_corona; k_crust; k_shell; onion_layers` |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `coreness` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `coreness; k_core` |  |
| [sna](../tools/sna.html) | · reported in docs | `kcores` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `kcore_decomposition` | API listing |
| [NetworKit](../tools/networkit.html) | ∅ checked, no value on some inputs | `CoreDecomposition` |  |
| [rustworkx](../tools/rustworkx.html) | ≠ checked, differs by convention | `core_number; digraph_core_number; graph_core_number` |  |
| [scikit-network](../tools/sknetwork.html) | ≠ checked, differs by convention | `get_core_decomposition` |  |
| [JGraphT](../tools/jgrapht.html) | ✓ checked, agrees | `Coreness` |  |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `core_numbers` | API listing |
| [BCT (Octave)](../tools/bct.html) | ≠ checked, differs by convention | `kcore_bd; kcore_bu; kcoreness_centrality_bd; kcoreness_centrality_bu` |  |
| [bctpy](../tools/bctpy.html) | ≠ checked, differs by convention |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Cohesion: k-cores, lambda sets, bicomponents, cut points, n-cliques, n-clans, k-plexes, cliques, factions; kcorelev` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F054](../findings.html#f054) | JGraphT | limitation | Coreness and clique finders refuse non-simple input |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [rubinov2010complex](../references.html#rubinov2010complex), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
