---
title: "Local bridges"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Local bridges {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `local_bridges`. 1 measure.

## Definition {#concept-definition}

Local bridges. Entries grouped here: Local bridges.

*Definition not yet written.*

## Local bridges {#local_bridges}

Measure id: `local_bridges`. Original family: Components and connectivity.

**Definition.** Local bridges.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_local_bridges</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.local_bridges(G, with_span = True), mapped to the fixture's edges</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
