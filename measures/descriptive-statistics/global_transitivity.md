---
title: "Global transitivity"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Global transitivity {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `global_transitivity`. 2 measures.

## Definition {#concept-definition}

Transitivity of the simple undirected reading of the network: closed triples over connected triples.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Transitivity](#transitivity) | `transitivity` | 13 |
| [Weak and strong transitivity; directed and weighted clustering conventions](#sna_transitivity) | `sna_transitivity` | 1 |

## References {#concept-references}

[barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

## Transitivity {#transitivity}

Measure id: `transitivity`. Original family: Descriptive statistics.

**Definition.** Transitivity of the simple undirected reading of the network: closed triples over connected triples.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `transitivity` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `transitivity` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `transitivity_undirected` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-transitivity-sna) | `gt; gtrans` | API listing |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `kstar` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-transitivity-graphtool) | `global_clustering` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `digraph_transitivity; graph_transitivity; transitivity` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and self-loops): JGraphT counts loops and parallel edges as extra neighbours/triangles in a pseudograph. [details](#why-transitivity-jgrapht) |  |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle... [details](#why-transitivity-bct) | `transitivity_bd; transitivity_bu; transitivity_wd; transitivity_wu` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-transitivity-ucinet) | `Transitivity, normalized transitivity (6.831), Dekker-Krackhardt-Snijders transitivity (6.840), cyclicity (6.834, cyclicity); transitivity` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-transitivity-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: gt; gtrans.
- <a id="why-transitivity-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: global\_clustering.
- <a id="why-transitivity-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (direction, multi-edges and self-loops) on the fixtures multi\_loops\_und. JGraphT counts loops and parallel edges as extra neighbours/triangles in a pseudograph; the reference uses simple neighbour sets. Relation to the reference value: Directed input: refuses ("Graph must be undirected"); NaN when no connected triple. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 1 comparisons differ and 18 agree. Finding F053 (limitation): Transitivity refuses directed input. Findings: [F053](../../findings.html#f053).
- <a id="why-transitivity-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (direction) on the fixtures gnp\_dir\_dense, gnp\_dir\_sparse, multi\_loops\_dir, real\_weights\_dir, weighted\_dir. BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle types over the total degree; the reference takes the undirected neighbourhood. Undirected simple networks agree. Relation to the reference value: Directed input: clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients (triangle types weighed over the total degree), not the undirected-neighbourhood value; undirected simple networks agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-14 (0 means exact equality). 5 comparisons differ and 23 agree.
- <a id="why-transitivity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F053](../../findings.html#f053) | JGraphT | limitation | Transitivity refuses directed input |

**References:** [barrat2004architecture](../../references.html#barrat2004architecture), [chiba1985arboricity](../../references.html#chiba1985arboricity), [dial1969algorithm](../../references.html#dial1969algorithm), [dijkstra1959note](../../references.html#dijkstra1959note), [garlaschelli2004patterns](../../references.html#garlaschelli2004patterns), [hage1995eccentricity](../../references.html#hage1995eccentricity), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kaiser2008mean](../../references.html#kaiser2008mean)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Weak and strong transitivity; directed and weighted clustering conventions {#sna_transitivity}

Measure id: `sna_transitivity`. Original family: Descriptive statistics.

**Definition.** Weak and strong transitivity; directed and weighted clustering conventions.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-sna_transitivity-sna) |  | documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-sna_transitivity-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles).

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
