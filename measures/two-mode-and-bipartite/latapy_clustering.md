---
title: "Latapy clustering"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Latapy clustering {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `latapy_clustering`. 1 measure.

## Definition {#concept-definition}

Latapy clustering. Entries grouped here: Latapy clustering.

*Definition not yet written.*

## Latapy clustering {#latapy_clustering}

Measure id: `latapy_clustering`. Original family: Two-mode and bipartite.

**Definition.** Latapy clustering.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>latapy_clustering</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>latapy_clustering_dot</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.latapy_clustering(G, mode = 'dot')</code></td><td></td></tr><tr><td><code>latapy_clustering_max</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.latapy_clustering(G, mode = 'max')</code></td><td></td></tr><tr><td><code>latapy_clustering_min</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.latapy_clustering(G, mode = 'min')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
