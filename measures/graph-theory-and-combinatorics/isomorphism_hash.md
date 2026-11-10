---
title: "Weisfeiler-Lehman graph and subgraph hash"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Weisfeiler-Lehman graph and subgraph hash {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `isomorphism_hash`. 2 measures.

## Definition {#concept-definition}

Weisfeiler-Lehman graph and subgraph hash. Entries grouped here: Wl hash; Wl subgraph.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Wl hash](#wl_hash) | `wl_hash` | 3 |
| [Wl subgraph](#wl_subgraph) | `wl_subgraph` | 1 |

## Wl hash {#wl_hash}

Measure id: `wl_hash`. Original family: Graph theory and combinatorics.

**Definition.** Wl hash.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `weisfeiler_lehman_graph_hash; weisfeiler_lehman_subgraph_hashes` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-wl_hash-sknetwork) | `color_weisfeiler_lehman; weisfeiler_lehman_coloring` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-wl_hash-jgrapht) | `ColorRefinementAlgorithm` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-wl_hash-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: color\_weisfeiler\_lehman; weisfeiler\_lehman\_coloring.
- <a id="why-wl_hash-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ColorRefinementAlgorithm.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `wl_hash` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G)` |  |
| `wl_hash_both_labels` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, edge_attr = 'label', node_attr = 'label', digest_size = 32)` | edge labels need a network without parallel edges (a NetworkX Graph has one label per pair) |
| `wl_hash_edge_labels` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, edge_attr = 'label')` | edge labels need a network without parallel edges (a NetworkX Graph has one label per pair) |
| `wl_hash_iter1` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, iterations = 1)` |  |
| `wl_hash_iter5_digest8` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, iterations = 5, digest_size = 8)` |  |
| `wl_hash_node_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, node_attr = 'label')` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_sknetwork](../../references.html#tool_sknetwork)

## Wl subgraph {#wl_subgraph}

Measure id: `wl_subgraph`. Original family: Graph theory and combinatorics.

**Definition.** Wl subgraph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `wl_subgraph` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G)` |  |
| `wl_subgraph_edge_labels` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G, edge_attr = 'label')` | edge labels need a network without parallel edges (a NetworkX Graph has one label per pair) |
| `wl_subgraph_initial` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G, iterations = 2, include_initial_labels = True)` |  |
| `wl_subgraph_node_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G, node_attr = 'label', include_initial_labels = True)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
