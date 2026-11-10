---
title: "Minimum-weight matching"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum-weight matching {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `minimum_weight_matching`. 2 measures.

## Definition {#concept-definition}

A matching of least total weight among the matchings of largest size, as input edge positions.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#min_weight_full_matching">Min weight full matching</a></td><td><code>min_weight_full_matching</code></td><td>1</td></tr><tr><td><a href="#min_weight_matching">Min weight matching</a></td><td><code>min_weight_matching</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[jonker1987shortest](../../references.html#jonker1987shortest), [kuhn1955hungarian](../../references.html#kuhn1955hungarian), [edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min weight full matching {#min_weight_full_matching}

Measure id: `min_weight_full_matching`. Original family: Two-mode and bipartite.

**Definition.** A full matching of least total cost of a bipartite graph, as each node's mate (-1 if unmatched).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>minimum_weight_full_matching</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>min_weight_full_matching</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-12</td><td><code>nx.bipartite.minimum_weight_full_matching(G, top, weight = c): (total cost, 1 if it covers the smaller side); -1 where it raises</code></td><td></td></tr></tbody></table></div>

**References:** [jonker1987shortest](../../references.html#jonker1987shortest), [kuhn1955hungarian](../../references.html#kuhn1955hungarian)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min weight matching {#min_weight_matching}

Measure id: `min_weight_matching`. Original family: Graph theory and combinatorics.

**Definition.** A matching of least total weight among the matchings of largest size, as input edge positions.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>min_weight_matching</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>matching_min_weight</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.min_weight_matching(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**References:** [edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
