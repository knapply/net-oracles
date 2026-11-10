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

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#wl_hash">Wl hash</a></td><td><code>wl_hash</code></td><td>3</td></tr><tr><td><a href="#wl_subgraph">Wl subgraph</a></td><td><code>wl_subgraph</code></td><td>1</td></tr></tbody></table></div>

## Wl hash {#wl_hash}

Measure id: `wl_hash`. Original family: Graph theory and combinatorics.

**Definition.** Wl hash.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>weisfeiler_lehman_graph_hash; weisfeiler_lehman_subgraph_hashes</code></td><td></td></tr><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-wl_hash-sknetwork">details</a></td><td><code>color_weisfeiler_lehman; weisfeiler_lehman_coloring</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-wl_hash-jgrapht">details</a></td><td><code>ColorRefinementAlgorithm</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-wl_hash-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: color\_weisfeiler\_lehman; weisfeiler\_lehman\_coloring.
- <a id="why-wl_hash-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ColorRefinementAlgorithm.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>wl_hash</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_graph_hash(G)</code></td><td></td></tr><tr><td><code>wl_hash_both_labels</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_graph_hash(G, edge_attr = 'label', node_attr = 'label', digest_size = 32)</code></td><td>edge labels need a network without parallel edges (a NetworkX Graph has one label per pair)</td></tr><tr><td><code>wl_hash_edge_labels</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_graph_hash(G, edge_attr = 'label')</code></td><td>edge labels need a network without parallel edges (a NetworkX Graph has one label per pair)</td></tr><tr><td><code>wl_hash_iter1</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_graph_hash(G, iterations = 1)</code></td><td></td></tr><tr><td><code>wl_hash_iter5_digest8</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_graph_hash(G, iterations = 5, digest_size = 8)</code></td><td></td></tr><tr><td><code>wl_hash_node_labels</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_graph_hash(G, node_attr = 'label')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_sknetwork](../../references.html#tool_sknetwork)

## Wl subgraph {#wl_subgraph}

Measure id: `wl_subgraph`. Original family: Graph theory and combinatorics.

**Definition.** Wl subgraph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>wl_subgraph</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_subgraph_hashes(G)</code></td><td></td></tr><tr><td><code>wl_subgraph_edge_labels</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_subgraph_hashes(G, edge_attr = 'label')</code></td><td>edge labels need a network without parallel edges (a NetworkX Graph has one label per pair)</td></tr><tr><td><code>wl_subgraph_initial</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_subgraph_hashes(G, iterations = 2, include_initial_labels = True)</code></td><td></td></tr><tr><td><code>wl_subgraph_node_labels</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.weisfeiler_lehman_subgraph_hashes(G, node_attr = 'label', include_initial_labels = True)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
