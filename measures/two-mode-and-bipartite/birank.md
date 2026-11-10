---
title: "BiRank"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# BiRank {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `birank`. 1 measure.

## Definition {#concept-definition}

BiRank scores of both node sets of a bipartite graph: the fixed point of damped, normalized propagation between the sets.

*Definition not yet written.*

## References {#concept-references}

[he2017birank](../../references.html#he2017birank)

## Birank {#birank}

Measure id: `birank`. Original family: Two-mode and bipartite.

**Definition.** BiRank scores of both node sets of a bipartite graph: the fixed point of damped, normalized propagation between the sets.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>birank</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>birank</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.bipartite.birank(G, top, max_iter = 1000, tol = 1e-10)</code></td><td></td></tr></tbody></table></div>

**References:** [he2017birank](../../references.html#he2017birank)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
