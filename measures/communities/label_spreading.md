---
title: "Label spreading"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Label spreading {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `label_spreading`. 1 measure.

## Definition {#concept-definition}

NetworkX's label spreading (harmonic function or local and global consistency): best class of every node and whether it ties.

*Definition not yet written.*

## Label spreading {#nxo_label_spreading}

Measure id: `nxo_label_spreading`. Original family: Communities.

**Definition.** NetworkX's label spreading (harmonic function or local and global consistency): best class of every node and whether it ties.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>harmonic_function; local_and_global_consistency</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxo_harmonic_function</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.node_classification.harmonic_function(G), labels (v // 4) % 3 on nodes v % 4 == 0 (graph without weights)</code></td><td></td></tr><tr><td><code>nxo_local_global_weighted</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.node_classification.local_and_global_consistency(G, alpha = 0.9, max_iter = 12)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
