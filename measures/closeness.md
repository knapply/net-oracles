---
title: "Closeness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Closeness

Family: Centrality. Identifier: `closeness`.

## Definition

Closeness of every node: the inverse of its mean distance to the nodes it reaches, with the unreachable-node rule of the chosen tool.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `closeness_centrality` |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `closeness` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `closeness` |  |
| [sna](../tools/sna.html) | ✓ checked, agrees | `closeness` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `closeness` | API listing |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees | `Closeness` |  |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees | `closeness_centrality; digraph_closeness_centrality; graph_closeness_centrality` |  |
| [scikit-network](../tools/sknetwork.html) | ≠ checked, differs by convention | `Closeness` |  |
| [JGraphT](../tools/jgrapht.html) | ≠ checked, differs by convention | `ClosenessCentrality` |  |
| [Boost Graph Library](../tools/boost.html) | ≠ checked, differs by convention | `closeness_centrality` |  |
| [Gephi toolkit](../tools/gephi.html) | ≠ checked, differs by convention |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Closeness: Freeman (inverse of total distance), unreachable set to max observed + 1 (default), n, or ignored; InClose/OutClose; reciprocal-distance variant` | published documentation |
| [tnet](../tools/tnet.html) | · reported in docs | `closeness_w` | API listing |
| [netrankr](../tools/netrankr.html) | ≠ checked, differs by convention |  |  |
| [centiserve](../tools/centiserve.html) | · reported in docs | `closeness.freeman` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `closeness` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::closeness(g, mode = 'out', weights = NA, normalized = FALSE)` |  |
| `closeness` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.closeness(mode="out", weights=None, normalized=False)` |  |
| `closeness` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(G, True, ClosenessVariant.STANDARD) divided by n - 1 (NetworKit 11 returns the normalized value whatever the flag says)` |  |
| `closeness` | JGraphT | any | differs |  | defaults | abs 1e-14, rel 1e-12 | `JGraphT 1.5.2: new ClosenessCentrality<>(g, false, false) on a pseudograph` | JGraphT's closeness is exactly 0 for a node that does not reach every other node, and Infinity for the lone node of a one-node network (checked on all 1534 node values of the corpus); the reference uses the reachable nodes only and marks a node reaching no other as undefined. Fixtures listed are those with such nodes. |
| `closeness` | Boost Graph Library | any | differs |  | defaults | abs 1e-14, rel 1e-12 | `Boost Graph Library all_closeness_centralities over Floyd-Warshall distances: 1 / (sum of distances)` | BGL's closeness is 1 / (sum of distances) with DBL\_MAX standing in for an unreachable distance, so a node that cannot reach every other node gets about 5.6e-309 (effectively 0), and the lone node of a one-node network gets Infinity (1/0); the reference uses the reachable nodes only and marks a node reaching no other as undefined. Listed fixtures contain such nodes. |
| `closeness` | netrankr | any | differs | disconnected, (no value) directed | defaults, direction, weights | abs 1e-14, rel 1e-12 | `aggregate_positions(indirect_relations(g, 'dist_sp'), 'invsum') on the undirected simple reading` | netrankr takes 1 over the sum of the finite and infinite distances, so a node that does not reach every other node gets 0 (an isolated node too); the reference (and igraph) sum over the nodes reached, and leave a node that reaches none undefined. netrankr reads the network as undirected, unweighted and simple (the oracle writes nothing for a directed fixture) and has no value for a single node. |
| `closeness_all` | igraph (R) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::closeness(g, mode = 'all', weights = NA, normalized = TRUE)` |  |
| `closeness_all` | igraph (Python) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.closeness(mode="all", weights=None, normalized=True)` |  |
| `closeness_all` | NetworKit | directed | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(undirected G, True, ClosenessVariant.STANDARD)` |  |
| `closeness_all` | Gephi toolkit | directed | differs |  | defaults | abs 1e-14, rel 1e-12 | `Gephi toolkit 0.11.3: GraphDistance (setNormalized(true), setDirected(false)), node column 'closnesscentrality'` | Gephi gives 0 to a node that reaches no other node; the reference leaves closeness undefined there (reported -1). |
| `closeness_documented` | UCINET | any | documented |  | normalization, defaults | abs 0, rel 0 | `Documented behaviour (not run)` | Closeness (Freeman) as described in the help: normalized closeness is (n - 1) divided by the sum of distances; unreachable distances are set to the largest observed distance plus 1. |
| `closeness_in` | igraph (R) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::closeness(g, mode = 'in', weights = NA, normalized = TRUE)` |  |
| `closeness_in` | igraph (Python) | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.closeness(mode="in", weights=None, normalized=True)` |  |
| `closeness_in` | NetworKit | directed | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(reversed G, True, ClosenessVariant.STANDARD)` |  |
| `closeness_in` | JGraphT | directed | differs |  | defaults | abs 1e-14, rel 1e-12 | `JGraphT 1.5.2: new ClosenessCentrality<>(g, true, true) on a pseudograph` | JGraphT's closeness is exactly 0 for a node that does not reach every other node, and Infinity for the lone node of a one-node network (checked on all 1534 node values of the corpus); the reference uses the reachable nodes only and marks a node reaching no other as undefined. Fixtures listed are those with such nodes. |
| `closeness_normalized` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::closeness(g, mode = 'out', weights = NA, normalized = TRUE)` |  |
| `closeness_normalized` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.closeness(mode="out", weights=None, normalized=True)` |  |
| `closeness_normalized` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(G, True, ClosenessVariant.STANDARD)` |  |
| `closeness_normalized` | scikit-network | any | differs |  | defaults | abs 1e-14, rel 1e-12 | `sknetwork.ranking.Closeness(method = 'exact').fit_predict(A simple)` | Closeness() requires a connected graph ('The graph is expected to be connected') or rejects an empty matrix. |
| `closeness_normalized` | JGraphT | any | differs |  | defaults | abs 1e-14, rel 1e-12 | `JGraphT 1.5.2: new ClosenessCentrality<>(g, false, true) on a pseudograph` | JGraphT's closeness is exactly 0 for a node that does not reach every other node, and Infinity for the lone node of a one-node network (checked on all 1534 node values of the corpus); the reference uses the reachable nodes only and marks a node reaching no other as undefined. Fixtures listed are those with such nodes. |
| `closeness_normalized` | Gephi toolkit | any | differs |  | defaults, direction, normalization | abs 1e-14, rel 1e-12 | `Gephi toolkit 0.11.3: GraphDistance, node column 'closnesscentrality' (identical with setNormalized(true) or (false))` | Gephi's closeness is (nodes reached) / (sum of distances to them), the reference value's unreachable: ignore reading, but it gives 0 to a node that reaches no other node (isolated, or a sink in a directed network); the reference leaves closeness undefined there (reported -1). setNormalized does not change it. |
| `closeness_sna` | sna | any | agrees |  |  | abs 1e-14, rel 1e-12 | `sna::closeness(m, gmode, cmode = 'directed' \| 'undirected')` |  |
| `closeness_weighted` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::closeness(g, mode = 'out', weights = E(g)$weight, normalized = TRUE)` |  |
| `closeness_weighted` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.closeness(mode="out", weights=w, normalized=True)` |  |
| `closeness_weighted` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(G_weighted, True, ClosenessVariant.STANDARD)` |  |
| `closeness_weighted` | JGraphT | any | differs |  | defaults | abs 1e-14, rel 1e-12 | `JGraphT 1.5.2: new ClosenessCentrality<>(g_weighted, false, true) on a pseudograph` | JGraphT's closeness is exactly 0 for a node that does not reach every other node, and Infinity for the lone node of a one-node network (checked on all 1534 node values of the corpus); the reference uses the reachable nodes only and marks a node reaching no other as undefined. Fixtures listed are those with such nodes. |
| `closeness_weighted_strength` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::closeness(g, mode = 'out', weights = 1 / E(g)$weight, normalized = TRUE)` |  |
| `closeness_weighted_strength` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: g.closeness( mode="out", weights=[1 / x for x in g.es["weight"]], normalized=True)` |  |
| `closeness_wf` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.closeness_centrality(G) (wf_improved = True, the default)` |  |
| `closeness_wf` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(reversed G, True, ClosenessVariant.GENERALIZED)` |  |
| `closeness_wf` | rustworkx | any | agrees |  |  | abs 1e-14, rel 1e-12 | `rx.closeness_centrality(G, wf_improved = True)` |  |
| `closeness_wf_weighted` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.closeness_centrality(G, distance = 'weight')` |  |
| `closeness_wf_weighted` | NetworKit | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(reversed G_weighted, True, ClosenessVariant.GENERALIZED)` |  |
| `proximity_prestige` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.closeness_centrality(G) (paths to the node, wf_improved = True)` |  |
| `proximity_prestige` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(reversed G, True, ClosenessVariant.GENERALIZED)` |  |
| `proximity_prestige` | rustworkx | any | agrees |  |  | abs 1e-14, rel 1e-12 | `rx.closeness_centrality(G, wf_improved = True)` |  |
| `proximity_prestige_weighted` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.closeness_centrality(G, distance = 'weight')` |  |
| `proximity_prestige_weighted` | NetworKit | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nk.centrality.Closeness(reversed G_weighted, True, ClosenessVariant.GENERALIZED)` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F018](../findings.html#f018) | Gephi toolkit | convention | Closeness is reached/sum of distances; 0 for a node reaching nobody |
| [F043](../findings.html#f043) | sna | convention | Closeness and centralization normalizations differ from other tools |
| [F047](../findings.html#f047) | JGraphT | convention | Closeness is 0 for a node that cannot reach every other node |
| [F048](../findings.html#f048) | Boost Graph Library | convention | Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair |
| [F061](../findings.html#f061) | NetworKit | convention | Closeness returns (n-1)/sum of distances whatever normalized says |
| [F081](../findings.html#f081) | netrankr | convention | Empty distance sum inverts to 0 |

## References

[boldi2014axioms](../references.html#boldi2014axioms), [freeman1978centrality](../references.html#freeman1978centrality), [marchiori2000harmony](../references.html#marchiori2000harmony), [rochat2009closeness](../references.html#rochat2009closeness), [sabidussi1966centrality](../references.html#sabidussi1966centrality), [staudt2016networkit](../references.html#staudt2016networkit), [then2014more](../references.html#then2014more), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [jalili2015centiserver](../references.html#jalili2015centiserver), [michail2020jgrapht](../references.html#michail2020jgrapht), [opsahl2010node](../references.html#opsahl2010node), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [schoch2018centrality](../references.html#schoch2018centrality), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
