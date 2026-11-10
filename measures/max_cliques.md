---
title: "Max cliques"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Max cliques

Family: Cohesion and subgroups. Identifier: `max_cliques`.

## Definition

Every maximal clique with at least min\_size members, in lexicographic order.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `enumerate_all_cliques; find_cliques; find_cliques_recursive` |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `clique_size_counts; cliques; largest_cliques; max_cliques` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `cliques; largest_cliques; maximal_cliques` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `max_cliques` | API listing |
| [NetworKit](../tools/networkit.html) | ∅ checked, no value on some inputs | `MaximalCliques` |  |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `count_cliques` | API listing |
| [JGraphT](../tools/jgrapht.html) | ✓ checked, agrees | `BronKerboschCliqueFinder; DegeneracyBronKerboschCliqueFinder; PivotBronKerboschCliqueFinder` |  |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `bron_kerbosch_all_cliques` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs | `cliqueoverlap; cliques` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `max_cliques` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cliques(nx.Graph(G)) (undirected simple projection; find_cliques rejects directed graphs and ignores loops)` |  |
| `max_cliques` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::max_cliques(g) (ignores directions, loops, and parallel edges)` |  |
| `max_cliques` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [tuple(sorted(c)) for c in g.maximal_cliques(min=0)]` |  |
| `max_cliques` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nk.clique.MaximalCliques(G simple undirected).getCliques()` |  |
| `max_cliques` | JGraphT | any | no-value-on-some-inputs | (no value) directed, (no value) loops, (no value) multi\_edges | direction, multi\_edges, self\_loops | abs 0, rel 0 | `JGraphT 1.5.2: new BronKerboschCliqueFinder<>(g) on a pseudograph` | BronKerboschCliqueFinder throws 'Graph must be simple' on loops or parallel edges; on directed input it does not error but returns a collection that is not the maximal cliques of the underlying graph (pair 0-&gt;1 gives two singletons, cycle7\_dir six cliques instead of seven edges), so it is not compared. |
| `max_cliques_min3` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[c for c in nx.find_cliques(nx.Graph(G)) if len(c) >= 3]` |  |
| `max_cliques_min3` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::max_cliques(g, min = 3)` |  |
| `max_cliques_min3` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [tuple(sorted(c)) for c in g.maximal_cliques(min=3)]` |  |
| `max_cliques_min3` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nk.clique.MaximalCliques(G simple undirected).getCliques(), size >= 3` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F066](../findings.html#f066) | NetworKit | convention | MaximalCliques omits a node without edges |

## References

[bron1973algorithm](../references.html#bron1973algorithm), [eppstein2010listing](../references.html#eppstein2010listing), [matula1983smallest](../references.html#matula1983smallest), [tomita2006worst](../references.html#tomita2006worst)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
