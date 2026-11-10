---
title: "Closeness"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Closeness {#concept-top}

Family: [Centrality](index.html). Subfamily: Distance-based. Concept id: `closeness`. 8 measures.

## Definition {#concept-definition}

Closeness of every node: the inverse of its mean distance to the nodes it reaches, with the unreachable-node rule of the chosen tool.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Closeness](#closeness) | `closeness` | 15 |
| [Approximate, top-k and group closeness](#closeness_approx) | `closeness_approx` | 1 |
| [Closeness latora](#cat_closeness_latora) | `cat_closeness_latora` | 1 |
| [Closeness residual](#cat_closeness_residual) | `cat_closeness_residual` | 1 |
| [Incremental closeness centrality](#cat_closeness_incremental) | `cat_closeness_incremental` | 1 |
| [Newman weighted closeness centrality](#cat_closeness_newman_weighted) | `cat_closeness_newman_weighted` | 1 |
| [Swan closeness](#cat_closeness_swan) | `cat_closeness_swan` | 1 |
| [Twomode / closeness](#twomode-closeness) | `twomode:closeness` | 3 |

## References {#concept-references}

[boldi2014axioms](../../references.html#boldi2014axioms), [freeman1978centrality](../../references.html#freeman1978centrality), [marchiori2000harmony](../../references.html#marchiori2000harmony), [rochat2009closeness](../../references.html#rochat2009closeness), [sabidussi1966centrality](../../references.html#sabidussi1966centrality), [staudt2016networkit](../../references.html#staudt2016networkit), [then2014more](../../references.html#then2014more), [wasserman1994social](../../references.html#wasserman1994social), [borgatti1997network](../../references.html#borgatti1997network), [borgatti2011analyzing](../../references.html#borgatti2011analyzing), [breiger1974duality](../../references.html#breiger1974duality), [everett2013dual](../../references.html#everett2013dual), [newman2001scientific](../../references.html#newman2001scientific)

## Closeness {#closeness}

Measure id: `closeness`. Original family: Centrality.

**Definition.** Closeness of every node: the inverse of its mean distance to the nodes it reaches, with the unreachable-node rule of the chosen tool.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `closeness_centrality` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `closeness` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `closeness` |  |
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `closeness` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-closeness-graphtool) | `closeness` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `Closeness` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `closeness_centrality; digraph_closeness_centrality; graph_closeness_centrality` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): Closeness() sets the score of every node that does not reach all others to 0 (ranking/closeness.py). [details](#why-closeness-sknetwork) | `Closeness` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): JGraphT's closeness is exactly 0 for a node that does not reach every other node, and Infinity for the lone node of a one-node network (checked on... [details](#why-closeness-jgrapht) | `ClosenessCentrality` |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): BGL's closeness is 1 / (sum of distances) with DBL\_MAX standing in for an unreachable distance, so a node that cannot reach every other node gets... [details](#why-closeness-boost) | `closeness_centrality` |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and normalization): Gephi gives 0 to a node that reaches no other node. [details](#why-closeness-gephi) |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-closeness-ucinet) | `Closeness: Freeman (inverse of total distance), unreachable set to max observed + 1 (default), n, or ignored; InClose/OutClose; reciprocal-distance variant` | published documentation |
| [tnet](../../tools/tnet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-closeness-tnet) | `closeness_w` | API listing |
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and weights): netrankr takes 1 over the sum of the finite and infinite distances, so a node that does not reach every other node gets 0 (an isolated node too). [details](#why-closeness-netrankr) |  |  |
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-closeness-centiserve) | `closeness.freeman` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-closeness-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: closeness.
- <a id="why-closeness-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> scikit-network 0.33.0 was run and its value differs from the reference value by convention (defaults) on the fixtures gnp\_dir\_sparse, multi\_loops\_dir, pair, weighted\_dir. Closeness() sets the score of every node that does not reach all others to 0 (ranking/closeness.py); the reference ignores unreachable nodes and leaves a node that reaches none undefined. Mapping: the reference value computed with the tool's convention (0 for a node that does not reach every other node, as sna) agrees with the tool within abs 1e-14, rel 1e-12 on all 4 comparisons where the difference occurs. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 4 comparisons differ and 19 agree.
- <a id="why-closeness-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> JGraphT 1.5.2 was run and its value differs from the reference value by convention (defaults) on the fixtures empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, single\_node, two\_triangles\_isolate, weighted\_dir. JGraphT's closeness is exactly 0 for a node that does not reach every other node, and Infinity for the lone node of a one-node network (checked on all 1534 node values of the corpus); the reference uses the reachable nodes only (unreachable: ignore) and marks a node reaching no other as undefined. Fixtures listed are those with such nodes. Relation to the reference value: Nodes not reaching everyone: value is exactly 0 for a node that cannot reach every other node (not the reachable-only sum the reference uses); Infinity for the single node of a one-node network. Mapping: the reference value computed with the tool's convention (0 for a node that does not reach every other node, as sna) agrees with the tool within abs 1e-14, rel 1e-12 on all 22 comparisons where the difference occurs. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 23 comparisons differ and 49 agree. Finding F047 (convention): Closeness is 0 for a node that cannot reach every other node. Findings: [F047](../../findings.html#f047).
- <a id="why-closeness-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Boost Graph Library 1.90 was run and its value differs from the reference value by convention (defaults) on the fixtures empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, single\_node, two\_triangles\_isolate, weighted\_dir. BGL's closeness is 1 / (sum of distances) with DBL\_MAX standing in for an unreachable distance, so a node that cannot reach every other node gets about 5.6e-309 (effectively 0), and the lone node of a one-node network gets Infinity (1/0); the reference uses the reachable nodes only (unreachable: ignore) and marks a node reaching no other as undefined. Listed fixtures contain such nodes. Relation to the reference value: Nodes not reaching everyone: 1 / sum of distances with DBL\_MAX for an unreachable distance, giving about 5.6e-309 (zero in effect); Infinity on one node. Normalization: 1 / sum of distances, i.e. the reference value's unnormalized closeness; times (n-1) gives the normalized one. Mapping: the reference value computed with the tool's convention (0 for a node that does not reach every other node, as sna) agrees with the tool within abs 1e-14, rel 1e-12 on all 8 comparisons where the difference occurs. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 9 comparisons differ and 19 agree. Finding F048 (convention): Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair. Findings: [F048](../../findings.html#f048).
- <a id="why-closeness-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (defaults, direction and normalization) on the fixtures empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_und, pair, single\_node, two\_triangles\_isolate, weighted\_dir. closeness\_all: Gephi gives 0 to a node that reaches no other node; the reference leaves closeness undefined there (reported -1). closeness\_normalized: Gephi's closeness is (nodes reached) / (sum of distances to them), the reference value's unreachable: ignore reading, but it gives 0 to a node that reaches no other node (isolated, or a sink in a directed network); the reference leaves closeness undefined there (reported -1). setNormalized does not change it. Relation to the reference value: Nodes reaching nobody: (reached) / (sum of distances), 0 for a node that reaches nobody (the reference: undefined); setNormalized has no effect. Mapping: the reference value computed with the tool's convention (nodes reached / sum of distances, and 0 for a node that reaches no other node) agrees with the tool within abs 1e-14, rel 1e-12 on all 9 comparisons where the difference occurs. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 9 comparisons differ and 28 agree. Finding F018 (convention): Closeness is reached/sum of distances; 0 for a node reaching nobody. Findings: [F018](../../findings.html#f018).
- <a id="why-closeness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-closeness-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: closeness\_w.
- <a id="why-closeness-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> netrankr 2.0.0 was run and its value differs from the reference value by convention (defaults, direction and weights) on inputs tagged disconnected. netrankr takes 1 over the sum of the finite and infinite distances, so a node that does not reach every other node gets 0 (an isolated node too); the reference (and igraph) sum over the nodes reached, and leave a node that reaches none undefined. Relation to the reference value: Nodes without reachable nodes: empty distance sum inverts to 0 where the reference value and igraph give NaN. Mapping: the reference value computed with the tool's convention (0 for a node that does not reach every other node, as sna) agrees with the tool within abs 1e-14, rel 1e-12 on all 3 comparisons where the difference occurs. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 3 comparisons differ and 15 agree. Finding F081 (convention): Empty distance sum inverts to 0. Findings: [F081](../../findings.html#f081).
- <a id="why-closeness-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: closeness.freeman.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F018](../../findings.html#f018) | Gephi toolkit | convention | Closeness is reached/sum of distances; 0 for a node reaching nobody |
| [F043](../../findings.html#f043) | sna | convention | Closeness and centralization normalizations differ from other tools |
| [F047](../../findings.html#f047) | JGraphT | convention | Closeness is 0 for a node that cannot reach every other node |
| [F048](../../findings.html#f048) | Boost Graph Library | convention | Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair |
| [F061](../../findings.html#f061) | NetworKit | convention | Closeness returns (n-1)/sum of distances whatever normalized says |
| [F081](../../findings.html#f081) | netrankr | convention | Empty distance sum inverts to 0 |

**References:** [boldi2014axioms](../../references.html#boldi2014axioms), [freeman1978centrality](../../references.html#freeman1978centrality), [marchiori2000harmony](../../references.html#marchiori2000harmony), [rochat2009closeness](../../references.html#rochat2009closeness), [sabidussi1966centrality](../../references.html#sabidussi1966centrality), [staudt2016networkit](../../references.html#staudt2016networkit), [then2014more](../../references.html#then2014more), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver), [michail2020jgrapht](../../references.html#michail2020jgrapht), [opsahl2010node](../../references.html#opsahl2010node), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [schoch2018centrality](../../references.html#schoch2018centrality), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Approximate, top-k and group closeness {#closeness_approx}

Measure id: `closeness_approx`. Original family: Centrality.

**Definition.** Approximate, top-k and group closeness.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-closeness_approx-networkit) | `ApproxCloseness; DynTopHarmonicCloseness; GroupClosenessGrowShrink; GroupClosenessLocalSearch; GroupClosenessLocalSwaps; GroupHarmonicCloseness; TopCloseness` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-closeness_approx-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ApproxCloseness; DynTopHarmonicCloseness; GroupClosenessGrowShrink; GroupClosenessLocalSearch; GroupClosenessLocalSwaps; GroupHarmonicCloseness; TopCloseness.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Closeness latora {#cat_closeness_latora}

Measure id: `cat_closeness_latora`. Original family: Centrality.

**Definition.** Closeness latora.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_closeness_latora-centiserve) | `closeness.latora` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_closeness_latora-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: closeness.latora.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Closeness residual {#cat_closeness_residual}

Measure id: `cat_closeness_residual`. Original family: Centrality.

**Definition.** Closeness residual.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_closeness_residual-centiserve) | `closeness.residual` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_closeness_residual-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: closeness.residual.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Incremental closeness centrality {#cat_closeness_incremental}

Measure id: `cat_closeness_incremental`. Original family: Centrality.

**Definition.** Incremental closeness centrality.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_closeness_incremental-networkx) | `incremental_closeness_centrality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_closeness_incremental-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: incremental\_closeness\_centrality.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Newman weighted closeness centrality {#cat_closeness_newman_weighted}

Measure id: `cat_closeness_newman_weighted`. Original family: Centrality.

**Definition.** Newman weighted closeness centrality.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_closeness_newman_weighted-rustworkx) | `digraph_newman_weighted_closeness_centrality; graph_newman_weighted_closeness_centrality; newman_weighted_closeness_centrality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_closeness_newman_weighted-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_newman\_weighted\_closeness\_centrality; graph\_newman\_weighted\_closeness\_centrality; newman\_weighted\_closeness\_centrality.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Swan closeness {#cat_closeness_swan}

Measure id: `cat_closeness_swan`. Original family: Centrality.

**Definition.** Swan closeness.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_closeness_swan-netrankr) | `swan_closeness` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_closeness_swan-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: swan\_closeness.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Twomode / closeness {#twomode-closeness}

Measure id: `twomode:closeness`. Original family: Two-mode and bipartite.

**Definition.** Closeness of every node in a two-mode network, normalized by the bounds of Borgatti and Everett (1997).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): One node, or a node that reaches nobody: no other node to be close to. [details](#why-twomode-closeness-networkx) |  |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-twomode-closeness-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-twomode-closeness-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults) on inputs tagged isolates and one\_node. One node, or a node that reaches nobody: no other node to be close to; the reference reports undefined, NetworkX 0. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 1e-12 (0 means exact equality). No value (twomode\_closeness) on the fixtures complete5\_dir, complete6, cycle7\_dir, empty, florentine, gnp\_dir\_dense, gnp\_dir\_sparse, gnp\_und\_dense, gnp\_und\_sparse, karate, kite, les\_miserables, multi\_loops\_dir, multi\_loops\_und, pair, path10, real\_weights\_dir, real\_weights\_und, single\_node, southern\_women, star8, two\_triangles\_isolate, uniform\_weights, weighted\_dir, weighted\_und: one-mode fixture (no node types). 1 comparisons differ and 7 agree.
- <a id="why-twomode-closeness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_closeness` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `nx.bipartite.closeness_centrality(G, first_mode_nodes, normalized = True)` | one-mode fixture (no node types) |
| `twomode_closeness_ignore` | NetworkX | any | differs | isolates, one\_node, (no value) onemode | defaults | abs 0, rel 1e-12 | `nx.bipartite.closeness_centrality(G, first_mode_nodes, normalized = False)` | One node, or a node that reaches nobody: no other node to be close to; the reference reports undefined, NetworkX 0. one-mode fixture (no node types) |
| `twomode_closeness_raw` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `igraph::closeness(simplify(as.undirected(g)), normalized = FALSE)` | one-mode fixture (no node types) |

**References:** [borgatti1997network](../../references.html#borgatti1997network), [borgatti2011analyzing](../../references.html#borgatti2011analyzing), [breiger1974duality](../../references.html#breiger1974duality), [everett2013dual](../../references.html#everett2013dual), [newman2001scientific](../../references.html#newman2001scientific), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
