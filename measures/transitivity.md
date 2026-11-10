---
title: "Transitivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Transitivity

Family: Descriptive statistics. Identifier: `transitivity`.

## Definition

Transitivity of the simple undirected reading of the network: closed triples over connected triples.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `transitivity` |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `transitivity` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `transitivity_undirected` |  |
| [sna](../tools/sna.html) | · reported in docs | `gt; gtrans` | API listing |
| [ergm (statnet)](../tools/ergm.html) | ✓ checked, agrees | `kstar` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `global_clustering` | API listing |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees |  |  |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees | `digraph_transitivity; graph_transitivity; transitivity` |  |
| [JGraphT](../tools/jgrapht.html) | ≠ checked, differs by convention |  |  |
| [GraphBLAS algorithms](../tools/graphblas.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../tools/bct.html) | ≠ checked, differs by convention | `transitivity_bd; transitivity_bu; transitivity_wd; transitivity_wu` |  |
| [bctpy](../tools/bctpy.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Transitivity, normalized transitivity (6.831), Dekker-Krackhardt-Snijders transitivity (6.840), cyclicity (6.834, cyclicity); transitivity` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `transitivity` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `igraph::transitivity(simplify(as_undirected(g)), type = 'global')` | Without connected triples the ratio is 0 / 0; not compared. |
| `transitivity` | igraph (Python) | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `python-igraph: (None if sum(k * (k - 1) for k in su.degree()) == 0 else [su.transitivity_undirected(mode="nan")])` | Without connected triples the ratio is 0 / 0; not compared. |
| `transitivity` | ergm (statnet) | any | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `3 * summary(nw ~ triangle) / summary(nw ~ kstar(2))` | The statistic is computed for undirected networks with at least three nodes only. |
| `transitivity` | NetworKit | any | no-value-on-some-inputs | (no value) no\_two\_paths |  | abs 0, rel 1e-14 | `nk.globals.ClusteringCoefficient.exactGlobal(G simple)` |  |
| `transitivity` | JGraphT | any | differs | (no value) directed | direction, multi\_edges, self\_loops | abs 0, rel 1e-14 | `JGraphT 1.5.2: new ClusteringCoefficient<>(g).getGlobalClusteringCoefficient() on a pseudograph` | JGraphT counts loops and parallel edges as extra neighbours/triangles in a pseudograph; the reference uses simple neighbour sets. ClusteringCoefficient.getGlobalClusteringCoefficient throws 'Graph must be undirected' on a directed graph. |
| `transitivity` | BCT (Octave) | any | differs |  | direction | abs 0, rel 1e-14 | `Brain Connectivity Toolbox 2019-03-03 in Octave: transitivity_bu / transitivity_bd, on the binary adjacency matrix without loops or parallel edges` | BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle types over the total degree; the reference takes the undirected neighbourhood. Undirected simple networks agree. |
| `transitivity_networkx` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.transitivity(nx.Graph of the network, self-loops removed)` |  |
| `transitivity_networkx` | ergm (statnet) | any | no-value-on-some-inputs |  | direction | abs 0, rel 1e-14 | `3 * summary(nw ~ triangle) / summary(nw ~ kstar(2)), 0 without 2-stars` | The statistic is computed for undirected networks with at least three nodes only. |
| `transitivity_networkx` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nk.globals.ClusteringCoefficient.exactGlobal(G simple)` |  |
| `transitivity_networkx` | rustworkx | any | agrees |  |  | abs 0, rel 1e-14 | `rx.transitivity(G simple)` |  |
| `transitivity_networkx` | GraphBLAS algorithms | any | agrees |  |  | abs 0, rel 1e-14 | `nx.transitivity(G simple without loops, backend = 'graphblas')` |  |
| `transitivity_networkx` | bctpy | any | no-value-on-some-inputs |  | defaults, normalization | abs 0, rel 1e-14 | `bct.transitivity_bu(A binary, no diagonal)` | No connected triples: transitivity\_bu() divides 0 by 0 and returns NaN, where this variant (NetworkX's convention) is 0. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F053](../findings.html#f053) | JGraphT | limitation | Transitivity refuses directed input |

## References

[barrat2004architecture](../references.html#barrat2004architecture), [chiba1985arboricity](../references.html#chiba1985arboricity), [dial1969algorithm](../references.html#dial1969algorithm), [dijkstra1959note](../references.html#dijkstra1959note), [garlaschelli2004patterns](../references.html#garlaschelli2004patterns), [hage1995eccentricity](../references.html#hage1995eccentricity), [hopcroft1973algorithm](../references.html#hopcroft1973algorithm), [kaiser2008mean](../references.html#kaiser2008mean)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring), [hunter2008ergm](../references.html#hunter2008ergm), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [rubinov2010complex](../references.html#rubinov2010complex), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
