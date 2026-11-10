---
title: "Betweenness"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Betweenness {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `betweenness`. 5 measures.

## Definition {#concept-definition}

Shortest-path betweenness of every node (Brandes 2001).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Betweenness](#betweenness) | `betweenness` | 17 |
| [Approximate betweenness (sampling)](#betweenness_approx) | `betweenness_approx` | 3 |
| [Betweenness simple](#betweenness_simple) | `betweenness_simple` | 2 |
| [Betweenness subset](#cx_betweenness_subset) | `cx_betweenness_subset` | 1 |
| [Twomode / betweenness](#twomode-betweenness) | `twomode:betweenness` | 3 |

## References {#concept-references}

[brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation), [borgatti1997network](../../references.html#borgatti1997network), [borgatti2011analyzing](../../references.html#borgatti2011analyzing), [breiger1974duality](../../references.html#breiger1974duality), [everett2013dual](../../references.html#everett2013dual), [newman2001scientific](../../references.html#newman2001scientific), [wasserman1994social](../../references.html#wasserman1994social)

## Betweenness {#betweenness}

Measure id: `betweenness`. Original family: Centrality.

**Definition.** Shortest-path betweenness of every node (Brandes 2001).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges, normalization, ties and weights): NetworkX traverses neighbor sets, so parallel edges count as a single shortest path. [details](#why-betweenness-networkx) | `betweenness_centrality` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and normalization): With fewer than three nodes the normalizing constant (n-1)(n-2) is zero. [details](#why-betweenness-igraph) | `betweenness` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `betweenness` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges): sna works on adjacency matrices, so parallel edges collapse to one. [details](#why-betweenness-sna) | `betweenness` |  |
| [RSiena](../../tools/rsiena.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-betweenness-rsiena) | `between` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-betweenness-graphtool) | `betweenness` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `Betweenness` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `betweenness_centrality; digraph_betweenness_centrality; graph_betweenness_centrality` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-betweenness-sknetwork) | `Betweenness` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction and normalization): JGraphT normalizes the undirected betweenness by (n-1)(n-2) rather than (n-1)(n-2)/2: every nonzero value on all 16 undirected networks with at... [details](#why-betweenness-jgrapht) | `BetweennessCentrality` |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and normalization): relative\_betweenness\_centrality gives exactly twice the reference value's normalized value on every directed network (checked on all six directed... [details](#why-betweenness-boost) | `brandes_betweenness_centrality` |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, normalization, self-loops, ties and weights): BCT's betweenness\_bin counts ordered pairs, so an undirected network's value is exactly twice the reference value's (checked on every undirected... [details](#why-betweenness-bct) | `betweenness_bin; betweenness_wei` |  |
| [bctpy](../../tools/bctpy.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and ties): BCT works on a connection matrix, so parallel edges collapse to one tie (one shortest path per pair of neighbours). [details](#why-betweenness-bctpy) |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and normalization): With fewer than three nodes the normalizing constant is zero. [details](#why-betweenness-gephi) |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-betweenness-ucinet) | `Betweenness: Freeman nodes, edges, normalized (percent), distance-weighted betweenness (6.798 fixes), flow betweenness, Newman random-walk betweenness, induced ; betw` | published documentation |
| [tnet](../../tools/tnet.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `betweenness_w` |  |
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges, self-loops, ties and weights): netrankr reads the simple undirected graph (parallel edges collapsed, loops dropped), while the reference counts parallel edges as distinct shortest... [details](#why-betweenness-netrankr) | `aggregate_positions` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-betweenness-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges, normalization, ties and weights) on inputs tagged integer\_weights and multi\_edges. betweenness: NetworkX traverses neighbor sets, so parallel edges count as a single shortest path. igraph and this reference count each parallel edge as a distinct path. betweenness\_normalized: NetworkX counts parallel edges as a single shortest path. betweenness\_weighted: NetworkX counts one shortest path per neighbour pair, so parallel edges of equal weight do not multiply the path count; the reference, igraph and NetworKit count each edge as a path (checked: 0-&gt;1 twice, 1-&gt;2, 0-&gt;3, 3-&gt;2, all weights 1, gives 2/3 and 1/3 for nodes 1 and 3 in the reference, 1/2 and 1/2 in NetworkX). betweenness\_weighted\_strength: Reciprocals of whole-number weights often give path lengths that tie exactly (1/3 + 1/6 = 1/2) but differ in the last bit of floating point. NetworkX compares lengths exactly and drops one of the tied paths; this reference (like igraph) compares with a relative tolerance and agrees with the exact-arithmetic definition oracle. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-09, rel 1e-09 on all 2 comparisons where the difference occurs. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-12, rel 1e-09 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 1e-09, rel 1e-09; abs 1e-12, rel 1e-09 (0 means exact equality). 13 comparisons differ and 81 agree. Finding F033 (convention): Weighted betweenness counts one shortest path per neighbour pair with parallel edges. Findings: [F033](../../findings.html#f033).
- <a id="why-betweenness-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults and normalization) on inputs tagged edge\_case. With fewer than three nodes the normalizing constant (n-1)(n-2) is zero. igraph returns NaN; this reference, like NetworkX, returns 0, since no node can lie between two others. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 2 comparisons differ and 108 agree.
- <a id="why-betweenness-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (multi-edges) on inputs tagged multi\_edges. sna works on adjacency matrices, so parallel edges collapse to one. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-09, rel 1e-09 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 1e-09, rel 1e-09 (0 means exact equality). 4 comparisons differ and 32 agree.
- <a id="why-betweenness-rsiena"></a>**[RSiena](../../tools/rsiena.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. RSiena 1.6.6 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (RSiena exported functions and help titles; effects from getEffects()); API names: between.
- <a id="why-betweenness-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: betweenness.
- <a id="why-betweenness-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Betweenness.
- <a id="why-betweenness-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (direction and normalization) on inputs tagged undirected. JGraphT normalizes the undirected betweenness by (n-1)(n-2) rather than (n-1)(n-2)/2: every nonzero value on all 16 undirected networks with at least three nodes is exactly half the reference value's (raw betweenness agrees). Relation to the reference value: Normalizing constant, undirected: raw / ((n-1)(n-2)); the standard value (and the reference value's) is raw / ((n-1)(n-2)/2), so JGraphT is exactly half. Mapping: the reference value computed with the tool's convention (normalized by (n-1)(n-2) whatever the direction) agrees with the tool within abs 1e-12, rel 1e-09 on all 16 comparisons where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 16 comparisons differ and 47 agree. Finding F045 (convention): Normalized betweenness divides by (n-1)(n-2) in undirected graphs. Findings: [F045](../../findings.html#f045).
- <a id="why-betweenness-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Boost Graph Library 1.90 was run and its value differs from the reference value by convention (defaults, direction and normalization) on the fixtures cycle7\_dir, gnp\_dir\_dense, gnp\_dir\_sparse, multi\_loops\_dir, pair, real\_weights\_dir, single\_node, weighted\_dir. relative\_betweenness\_centrality gives exactly twice the reference value's normalized value on every directed network (checked on all six directed networks with at least three nodes), and 0/0 = NaN where n &lt; 3 (pair, single\_node); undirected networks agree. Relation to the reference value: Normalizing constant, directed: relative\_betweenness\_centrality is exactly twice the standard value on directed networks; undirected agrees. N &lt; 3: 0/0 = NaN where the reference (and NetworkX) return 0. Mapping: the reference value computed with the tool's convention (normalized by (n-1)(n-2)/2 whatever the direction) agrees with the tool within abs 1e-12, rel 1e-09 on all 6 comparisons where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 8 comparisons differ and 55 agree. Finding F046 (convention): relative\_betweenness\_centrality is twice the standard value on directed graphs. Findings: [F046](../../findings.html#f046).
- <a id="why-betweenness-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (direction, multi-edges, normalization, self-loops, ties and weights) on inputs tagged undirected and the fixtures multi\_loops\_dir. betweenness: BCT's betweenness\_bin counts ordered pairs, so an undirected network's value is exactly twice the reference value's (checked on every undirected network with a nonzero value); a BCT call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge (multi\_loops\_dir). betweenness\_weighted: BCT's betweenness\_wei counts ordered pairs, so an undirected network's value is exactly twice the reference value's (all five weighted undirected networks with a nonzero value). Relation to the reference value: Pair counting, undirected: counts ordered pairs, so exactly twice the reference value's and NetworkX's value on every undirected network. Mapping: the reference value computed with the tool's convention (both orderings of an undirected pair) on the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-09, rel 1e-09 on all 17 comparisons where the difference occurs. Mapping: the reference value computed with the tool's convention (both orderings of an undirected pair) agrees with the tool within abs 1e-09, rel 1e-09 on all 5 comparisons where the difference occurs. Tolerance before mapping: abs 1e-09, rel 1e-09 (0 means exact equality). 22 comparisons differ and 13 agree. Finding F055 (convention): Betweenness counts ordered pairs on undirected networks. Findings: [F055](../../findings.html#f055).
- <a id="why-betweenness-bctpy"></a>**[bctpy](../../tools/bctpy.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> bctpy 0.6.1 was run and its value differs from the reference value by convention (multi-edges and ties) on inputs tagged multi\_edges. betweenness: BCT works on a connection matrix, so parallel edges collapse to one tie (one shortest path per pair of neighbours); the reference counts each edge. betweenness\_weighted: BCT works on a connection matrix, so parallel edges collapse to one tie (the shortest one); the reference counts each edge. Relation to the reference value: Pair counting, undirected: counts ordered pairs, so exactly twice the reference value's and NetworkX's value on every undirected network. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-09, rel 1e-09 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 1e-09, rel 1e-09 (0 means exact equality). 2 comparisons differ and 33 agree.
- <a id="why-betweenness-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (defaults and normalization) on inputs tagged edge\_case. With fewer than three nodes the normalizing constant is zero. Gephi returns NaN (0/0); this reference, like NetworkX, returns 0, since no node can lie between two others. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 2 comparisons differ and 54 agree.
- <a id="why-betweenness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-betweenness-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> netrankr 2.0.0 was run and its value differs from the reference value by convention (defaults, direction, multi-edges, self-loops, ties and weights) on inputs tagged loops and multi\_edges. netrankr reads the simple undirected graph (parallel edges collapsed, loops dropped), while the reference counts parallel edges as distinct shortest paths. The oracle halves netrankr's sum over ordered pairs. Relation to the reference value: Pair counting: `depend_sp` and `depend_curflow` summed over a node count both orderings of an unordered pair, twice the reference value's; the oracle halves it. Parallel edges and loops are dropped (simple undirected reading). Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 1e-09, rel 1e-09 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 1e-09, rel 1e-09 (0 means exact equality). 1 comparisons differ and 17 agree. Finding F079 (convention): depend\_sp and depend\_curflow count both orderings of an unordered pair. Findings: [F079](../../findings.html#f079).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `betweenness` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(G, normalized = False)` | NetworkX traverses neighbor sets, so parallel edges count as a single shortest path. igraph and this reference count each parallel edge as a distinct path. |
| `betweenness` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(g, weights = NA, normalized = FALSE)` |  |
| `betweenness` | igraph (Python) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `python-igraph: gu.betweenness(directed=d)` |  |
| `betweenness` | sna | any | differs | multi\_edges | multi\_edges | abs 1e-09, rel 1e-09 | `sna::betweenness(m, gmode, cmode = 'directed' \| 'undirected')` | sna works on adjacency matrices, so parallel edges collapse to one. |
| `betweenness` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `nk.centrality.Betweenness(G, normalized = False)` |  |
| `betweenness` | rustworkx | any | agrees |  |  | abs 1e-09, rel 1e-09 | `rx.betweenness_centrality(G, normalized = False) on a multigraph` |  |
| `betweenness` | JGraphT | any | agrees |  |  | abs 1e-09, rel 1e-09 | `JGraphT 1.5.2: new BetweennessCentrality<>(g, false) on a pseudograph` |  |
| `betweenness` | Boost Graph Library | any | agrees |  |  | abs 1e-09, rel 1e-09 | `Boost Graph Library brandes_betweenness_centrality(g)` |  |
| `betweenness` | BCT (Octave) | any | differs | undirected | direction, multi\_edges, normalization, self\_loops, ties | abs 1e-09, rel 1e-09 | `Brain Connectivity Toolbox 2019-03-03 in Octave: betweenness_bin, on the binary adjacency matrix without loops or parallel edges` | BCT's betweenness\_bin counts ordered pairs, so an undirected network's value is exactly twice the reference value's (checked on every undirected network with a nonzero value); a BCT call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge (multi\_loops\_dir). |
| `betweenness` | bctpy | any | differs | multi\_edges | multi\_edges, ties | abs 1e-09, rel 1e-09 | `bct.betweenness_bin(A binary, no diagonal)` | BCT works on a connection matrix, so parallel edges collapse to one tie (one shortest path per pair of neighbours); the reference counts each edge. |
| `betweenness` | Gephi toolkit | any | agrees |  |  | abs 1e-09, rel 1e-09 | `Gephi toolkit 0.11.3: GraphDistance (setNormalized(false); setDirected as the network), node column 'betweenesscentrality'` |  |
| `betweenness` | netrankr | any | differs | loops, multi\_edges, (no value) directed | defaults, direction, multi\_edges, self\_loops, ties, weights | abs 1e-09, rel 1e-09 | `aggregate_positions(indirect_relations(g, 'depend_sp'), 'sum')` | netrankr reads the simple undirected graph (parallel edges collapsed, loops dropped), while the reference counts parallel edges as distinct shortest paths. The oracle halves netrankr's sum over ordered pairs. netrankr reads the network as undirected, unweighted and simple (the oracle writes nothing for a directed fixture) and has no value for a single node. |
| `betweenness_documented` | UCINET | any | documented |  | multi\_edges, self\_loops | abs 0, rel 0 | `Documented behaviour (not run)` | Betweenness is read from the adjacency matrix: parallel edges count once and the diagonal is ignored (matrix reading). |
| `betweenness_normalized` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, normalized = True)` | NetworkX counts parallel edges as a single shortest path. |
| `betweenness_normalized` | igraph (R) | any | differs | edge\_case | defaults, normalization | abs 1e-12, rel 1e-09 | `igraph::betweenness(g, weights = NA, normalized = TRUE)` | With fewer than three nodes the normalizing constant (n-1)(n-2) is zero. igraph returns NaN; this reference, like NetworkX, returns 0, since no node can lie between two others. |
| `betweenness_normalized` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-09 | `nk.centrality.Betweenness(G, normalized = True)` |  |
| `betweenness_normalized` | rustworkx | any | agrees |  |  | abs 1e-12, rel 1e-09 | `rx.betweenness_centrality(G, normalized = True) on a multigraph` |  |
| `betweenness_normalized` | JGraphT | any | differs | undirected | direction, normalization | abs 1e-12, rel 1e-09 | `JGraphT 1.5.2: new BetweennessCentrality<>(g, true) on a pseudograph` | JGraphT normalizes the undirected betweenness by (n-1)(n-2) rather than (n-1)(n-2)/2: every nonzero value on all 16 undirected networks with at least three nodes is exactly half the reference value's (raw betweenness agrees). |
| `betweenness_normalized` | Boost Graph Library | any | differs |  | defaults, direction, normalization | abs 1e-12, rel 1e-09 | `Boost Graph Library brandes_betweenness_centrality + relative_betweenness_centrality` | relative\_betweenness\_centrality gives exactly twice the reference value's normalized value on every directed network (checked on all six directed networks with at least three nodes), and 0/0 = NaN where n &lt; 3 (pair, single\_node); undirected networks agree. |
| `betweenness_normalized` | Gephi toolkit | any | differs | edge\_case | defaults, normalization | abs 1e-12, rel 1e-09 | `Gephi toolkit 0.11.3: GraphDistance (setNormalized(true)), node column 'betweenesscentrality'` | With fewer than three nodes the normalizing constant is zero. Gephi returns NaN (0/0); this reference, like NetworkX, returns 0, since no node can lie between two others. |
| `betweenness_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization, weights | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(G, weight = 'weight', normalized = False)` | NetworkX counts one shortest path per neighbour pair, so parallel edges of equal weight do not multiply the path count; the reference, igraph and NetworKit count each edge as a path (checked: 0-&gt;1 twice, 1-&gt;2, 0-&gt;3, 3-&gt;2, all weights 1, gives 2/3 and 1/3 for nodes 1 and 3 in the reference, 1/2 and 1/2 in NetworkX). |
| `betweenness_weighted` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(g, weights = E(g)$weight, normalized = FALSE)` |  |
| `betweenness_weighted` | igraph (Python) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `python-igraph: g.betweenness(directed=d, weights=w)` |  |
| `betweenness_weighted` | NetworKit | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nk.centrality.Betweenness(G_weighted, normalized = False)` |  |
| `betweenness_weighted` | JGraphT | any | agrees |  |  | abs 1e-09, rel 1e-09 | `JGraphT 1.5.2: new BetweennessCentrality<>(g_weighted, false) on a pseudograph` |  |
| `betweenness_weighted` | Boost Graph Library | any | agrees |  |  | abs 1e-09, rel 1e-09 | `Boost Graph Library brandes_betweenness_centrality(g, weight_map)` |  |
| `betweenness_weighted` | BCT (Octave) | any | differs | undirected | direction, normalization, ties, weights | abs 1e-09, rel 1e-09 | `Brain Connectivity Toolbox 2019-03-03 in Octave: betweenness_wei (weights as lengths), on the binary adjacency matrix without loops or parallel edges` | BCT's betweenness\_wei counts ordered pairs, so an undirected network's value is exactly twice the reference value's (all five weighted undirected networks with a nonzero value). |
| `betweenness_weighted` | bctpy | any | differs | multi\_edges | multi\_edges, ties | abs 1e-09, rel 1e-09 | `bct.betweenness_wei(L), L = shortest parallel edge as length` | BCT works on a connection matrix, so parallel edges collapse to one tie (the shortest one); the reference counts each edge. |
| `betweenness_weighted_strength` | NetworkX | any | differs | integer\_weights | ties, weights | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(G, weight = 1/w, normalized = False)` | Reciprocals of whole-number weights often give path lengths that tie exactly (1/3 + 1/6 = 1/2) but differ in the last bit of floating point. NetworkX compares lengths exactly and drops one of the tied paths; this reference (like igraph) compares with a relative tolerance and agrees with the exact-arithmetic definition oracle. |
| `betweenness_weighted_strength` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(g, weights = 1 / E(g)$weight, normalized = FALSE)` |  |
| `betweenness_weighted_strength` | igraph (Python) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `python-igraph: g.betweenness( directed=d, weights=[1 / x for x in g.es["weight"]])` |  |
| `betweenness_weighted_strength` | tnet | any | differs | isolates, multi\_edges | defaults, multi\_edges, normalization, ties, weights | abs 1e-09, rel 1e-09 | `tnet::betweenness_w(net, directed, alpha = 1)` | tnet reports NaN for a node without ties (its strength is 0 and the measure divides by it); the reference reports 0 betweenness. tnet also takes parallel edges as one tie of their summed weight (tnet rejects repeated pairs, so the oracle script sums them), which shortens its paths; the reference keeps the parallel edges apart, as the definition oracle, NetworkX and igraph do, and the four agree on the multigraph. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F033](../../findings.html#f033) | NetworkX | convention | Weighted betweenness counts one shortest path per neighbour pair with parallel edges |
| [F045](../../findings.html#f045) | JGraphT | convention | Normalized betweenness divides by (n-1)(n-2) in undirected graphs |
| [F046](../../findings.html#f046) | Boost Graph Library | convention | relative\_betweenness\_centrality is twice the standard value on directed graphs |
| [F055](../../findings.html#f055) | BCT (Octave) | convention | Betweenness counts ordered pairs on undirected networks |
| [F060](../../findings.html#f060) | NetworKit | convention | Undirected betweenness scores both orderings of a pair |
| [F076](../../findings.html#f076) | influenceR | convention | influenceR betweenness counts both orderings of an undirected pair and reads directed graphs as undirected |
| [F079](../../findings.html#f079) | netrankr | convention | depend\_sp and depend\_curflow count both orderings of an unordered pair |
| [F089](../../findings.html#f089) | GAP Benchmark Suite | convention | The BC verifier uses a float-epsilon tolerance against its own float accumulation |
| [F090](../../findings.html#f090) | graph-tool | convention | Betweenness normalization can differ by a factor 2 from the Freeman convention |

**References:** [brandes2001faster](../../references.html#brandes2001faster)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [opsahl2010node](../../references.html#opsahl2010node), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [ripley2026manual](../../references.html#ripley2026manual), [rubinov2010complex](../../references.html#rubinov2010complex), [schoch2018centrality](../../references.html#schoch2018centrality), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Approximate betweenness (sampling) {#betweenness_approx}

Measure id: `betweenness_approx`. Original family: Centrality.

**Definition.** Approximate betweenness (sampling).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-betweenness_approx-networkit) | `ApproxBetweenness; ApproxGroupBetweenness; DynApproxBetweenness; EstimateBetweenness; KadabraBetweenness` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-betweenness_approx-jgrapht) | `ApBetweennessCentrality` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-betweenness_approx-boost) | `betweenness_centrality_clustering` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-betweenness_approx-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ApproxBetweenness; ApproxGroupBetweenness; DynApproxBetweenness; EstimateBetweenness; KadabraBetweenness.
- <a id="why-betweenness_approx-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ApBetweennessCentrality.
- <a id="why-betweenness_approx-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: betweenness\_centrality\_clustering.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)

## Betweenness simple {#betweenness_simple}

Measure id: `betweenness_simple`. Original family: Centrality.

**Definition.** Betweenness simple.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `betweenness_networkx` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(MultiGraph/MultiDiGraph, normalized = False)` |  |
| `betweenness_networkx` | sna | any | agrees |  |  | abs 1e-09, rel 1e-09 | `sna::betweenness(m, gmode, cmode = 'directed' \| 'undirected')` |  |
| `betweenness_networkx_weighted` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(MultiGraph/MultiDiGraph, weight = 'weight', normalized = False), which uses the lightest parallel edge` |  |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Betweenness subset {#cx_betweenness_subset}

Measure id: `cx_betweenness_subset`. Original family: Centrality.

**Definition.** Betweenness of nodes and edges for chosen sources and targets (Brandes 2008), which includes betweenness from a sample of sources.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges): NetworkX counts a pair of adjacent nodes once however many parallel edges join them. [details](#why-cx_betweenness_subset-networkx) | `betweenness_centrality_subset; edge_betweenness_centrality_subset` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cx_betweenness_subset-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges) on inputs tagged multi\_edges. cx\_bc\_all\_distinct and cx\_bc\_all\_distinct\_weighted: NetworkX counts a pair of adjacent nodes once however many parallel edges join them; this variant counts each parallel edge as a distinct shortest path (igraph). cx\_ebc\_all\_distinct: NetworkX counts parallel edges as one path and shares the pair's value equally among them; this variant gives each parallel edge its own value (igraph). Mapping: the reference value computed with the tool's convention (a pair joined by parallel edges is one shortest path) agrees with the tool within abs 1e-12, rel 1e-09 on all 2 comparisons where the difference occurs. Mapping: the reference value computed with the tool's convention (the pair's credit shared equally among its parallel edges) agrees with the tool within abs 1e-12, rel 1e-09 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 4 comparisons differ and 276 agree. Finding F024 (defect): edge\_betweenness\_centrality\_subset deviates from its documented formula. Findings: [F024](../../findings.html#f024).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_bc_all_distinct` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, normalized = False)` | NetworkX counts a pair of adjacent nodes once however many parallel edges join them; this variant counts each parallel edge as a distinct shortest path (igraph). |
| `cx_bc_all_distinct_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, normalized = False, weight = 'weight')` | NetworkX counts a pair of adjacent nodes once however many parallel edges join them; this variant counts each parallel edge as a distinct shortest path (igraph). |
| `cx_bc_sampled` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, seed = 3)` |  |
| `cx_bc_sampled_endpoints` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, endpoints = True, seed = 3)` |  |
| `cx_bc_sampled_raw` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, normalized = False, seed = 3)` |  |
| `cx_bc_sampled_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality(G, k = 7, weight = 'weight', seed = 3)` |  |
| `cx_bc_subset_nx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality_subset(G, even, thirds, normalized = False)` |  |
| `cx_bc_subset_nx_normalized` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality_subset(G, even, thirds, normalized = True)` |  |
| `cx_bc_subset_nx_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.betweenness_centrality_subset(G, even, thirds, weight = 'weight')` |  |
| `cx_ebc_all_distinct` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality(G, normalized = False)` | NetworkX counts parallel edges as one path and shares the pair's value equally among them; this variant gives each parallel edge its own value (igraph). |
| `cx_ebc_sampled` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality(G, k = 7, seed = 3)` |  |
| `cx_ebc_subset_nx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality_subset(G, even, thirds, normalized = False)` |  |
| `cx_ebc_subset_nx_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality_subset(G, even, thirds, weight = 'weight')` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F024](../../findings.html#f024) | NetworkX | defect | edge\_betweenness\_centrality\_subset deviates from its documented formula |

**References:** [brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Twomode / betweenness {#twomode-betweenness}

Measure id: `twomode:betweenness`. Original family: Two-mode and bipartite.

**Definition.** Betweenness of every node in a two-mode network, optionally divided by the largest possible value (Borgatti and Everett 1997).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-twomode-betweenness-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-twomode-betweenness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_betweenness` | NetworkX | any | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-09 | `nx.bipartite.betweenness_centrality(G, first_mode_nodes)` | one-mode fixture (no node types) |
| `twomode_betweenness_raw` | NetworkX | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(G, normalized = False)` | one-mode fixture (no node types) |
| `twomode_betweenness_raw` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(simplify(as.undirected(g)))` | one-mode fixture (no node types) |

**References:** [borgatti1997network](../../references.html#borgatti1997network), [borgatti2011analyzing](../../references.html#borgatti2011analyzing), [breiger1974duality](../../references.html#breiger1974duality), [everett2013dual](../../references.html#everett2013dual), [newman2001scientific](../../references.html#newman2001scientific), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
