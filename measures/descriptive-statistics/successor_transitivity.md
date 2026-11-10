---
title: "Successor transitivity"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Successor transitivity {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `successor_transitivity`. 1 measure.

## Definition {#concept-definition}

Successor transitivity. Entries grouped here: Successor transitivity.

*Definition not yet written.*

## Successor transitivity {#nxo_successor_transitivity}

Measure id: `nxo_successor_transitivity`. Original family: Descriptive statistics.

**Definition.** Successor transitivity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxo_successor_transitivity</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.transitivity(nx.DiGraph(G)) (triangles over successors)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
