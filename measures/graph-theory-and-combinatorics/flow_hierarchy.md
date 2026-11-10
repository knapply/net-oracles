---
title: "Flow hierarchy"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Flow hierarchy {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `flow_hierarchy`. 1 measure.

## Definition {#concept-definition}

Flow hierarchy. Entries grouped here: Flow hierarchy.

*Definition not yet written.*

## Flow hierarchy {#nxo_flow_hierarchy}

Measure id: `nxo_flow_hierarchy`. Original family: Graph theory and combinatorics.

**Definition.** Flow hierarchy.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>flow_hierarchy</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxo_flow_hierarchy</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.flow_hierarchy(G)</code></td><td></td></tr><tr><td><code>nxo_flow_hierarchy_weighted</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.flow_hierarchy(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
