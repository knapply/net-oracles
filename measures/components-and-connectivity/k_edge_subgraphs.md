---
title: "K-edge subgraphs"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-edge subgraphs {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `k_edge_subgraphs`. 1 measure.

## Definition {#concept-definition}

K-edge subgraphs. Entries grouped here: K edge subgraphs.

*Definition not yet written.*

## K edge subgraphs {#gb_k_edge_subgraphs}

Measure id: `gb_k_edge_subgraphs`. Original family: Traversal, trees and DAGs.

**Definition.** K edge subgraphs.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>k_edge_subgraphs</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_k_edge_subgraphs</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>nx.k_edge_subgraphs(G, 2)</code></td><td>NetworkX's k_edge_subgraphs rejects multigraphs.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
