---
title: "Lukes tree partitioning"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lukes tree partitioning {#concept-top}

Family: [Communities](index.html). Subfamily: Graph bisection and partitioning. Concept id: `lukes_partitioning`. 1 measure.

## Definition {#concept-definition}

Lukes tree partitioning. Entries grouped here: Lukes.

*Definition not yet written.*

## Lukes {#cnx_lukes}

Measure id: `cnx_lukes`. Original family: Communities.

**Definition.** Lukes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>lukes_partitioning</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_lukes_partitioning</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.community.lukes_partitioning(G, 3): (edges inside clusters, 1 if every cluster has at most 3 nodes); -1 if not a tree</code></td><td>NetworkX 3.7 fails with a KeyError on a tree of one node</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
