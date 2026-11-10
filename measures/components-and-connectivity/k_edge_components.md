---
title: "K-edge-connected components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-edge-connected components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `k_edge_components`. 1 measure.

## Definition {#concept-definition}

K-edge-connected components. Entries grouped here: K edge components.

*Definition not yet written.*

## K edge components {#k_edge_components}

Measure id: `k_edge_components`. Original family: Components and connectivity.

**Definition.** K edge components.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>k_edge_components</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_k_edge_components_2</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_edge_components(G, k = 2)</code></td><td></td></tr><tr><td><code>conn_k_edge_components_3</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_edge_components(G, k = 3)</code></td><td></td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f028">F028</a></td><td>NetworkX</td><td>limitation</td><td>k_edge_components hits the recursion limit near n = 1000</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
