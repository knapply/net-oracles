---
title: "Betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Betweenness

Family: Centrality. Identifier: `betweenness`.

## Definition

Shortest-path betweenness of every node (Brandes 2001).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `betweenness_centrality` |  |
| [igraph (R)](../tools/igraph.html) | ≠ checked, differs by convention | `betweenness` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `betweenness` |  |
| [sna](../tools/sna.html) | ≠ checked, differs by convention | `betweenness` |  |
| [RSiena](../tools/rsiena.html) | · reported in docs | `between` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `betweenness` | API listing |
| [NetworKit](../tools/networkit.html) | ∅ checked, no value on some inputs | `Betweenness` |  |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees | `betweenness_centrality; digraph_betweenness_centrality; graph_betweenness_centrality` |  |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `Betweenness` | API listing |
| [JGraphT](../tools/jgrapht.html) | ≠ checked, differs by convention | `BetweennessCentrality` |  |
| [Boost Graph Library](../tools/boost.html) | ≠ checked, differs by convention | `brandes_betweenness_centrality` |  |
| [BCT (Octave)](../tools/bct.html) | ≠ checked, differs by convention | `betweenness_bin; betweenness_wei` |  |
| [bctpy](../tools/bctpy.html) | ≠ checked, differs by convention |  |  |
| [Gephi toolkit](../tools/gephi.html) | ≠ checked, differs by convention |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Betweenness: Freeman nodes, edges, normalized (percent), distance-weighted betweenness (6.798 fixes), flow betweenness, Newman random-walk betweenness, induced ; betw` | published documentation |
| [tnet](../tools/tnet.html) | ✓ checked, agrees | `betweenness_w` |  |
| [netrankr](../tools/netrankr.html) | ≠ checked, differs by convention | `aggregate_positions` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F033](../findings.html#f033) | NetworkX | convention | Weighted betweenness counts one shortest path per neighbour pair with parallel edges |
| [F045](../findings.html#f045) | JGraphT | convention | Normalized betweenness divides by (n-1)(n-2) in undirected graphs |
| [F046](../findings.html#f046) | Boost Graph Library | convention | relative\_betweenness\_centrality is twice the standard value on directed graphs |
| [F055](../findings.html#f055) | BCT (Octave) | convention | Betweenness counts ordered pairs on undirected networks |
| [F060](../findings.html#f060) | NetworKit | convention | Undirected betweenness scores both orderings of a pair |
| [F076](../findings.html#f076) | influenceR | convention | influenceR betweenness counts both orderings of an undirected pair and reads directed graphs as undirected |
| [F079](../findings.html#f079) | netrankr | convention | depend\_sp and depend\_curflow count both orderings of an unordered pair |
| [F089](../findings.html#f089) | GAP Benchmark Suite | convention | The BC verifier uses a float-epsilon tolerance against its own float accumulation |
| [F090](../findings.html#f090) | graph-tool | convention | Betweenness normalization can differ by a factor 2 from the Freeman convention |

## References

[brandes2001faster](../references.html#brandes2001faster)

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [opsahl2010node](../references.html#opsahl2010node), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [ripley2026manual](../references.html#ripley2026manual), [rubinov2010complex](../references.html#rubinov2010complex), [schoch2018centrality](../references.html#schoch2018centrality), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
