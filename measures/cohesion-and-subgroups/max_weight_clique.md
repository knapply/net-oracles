---
title: "Maximum-weight clique"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximum-weight clique {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cliques. Concept id: `max_weight_clique`. 3 measures.

## Definition {#concept-definition}

Maximum-weight clique. Entries grouped here: Max weight clique; Largest weighted cliques; Max weight clique nodes.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#max_weight_clique">Max weight clique</a></td><td><code>max_weight_clique</code></td><td>1</td></tr><tr><td><a href="#cat_clique_largest_weighted">Largest weighted cliques</a></td><td><code>cat_clique_largest_weighted</code></td><td>1</td></tr><tr><td><a href="#max_weight_clique_nodes">Max weight clique nodes</a></td><td><code>max_weight_clique_nodes</code></td><td>1</td></tr></tbody></table></div>

## Max weight clique {#max_weight_clique}

Measure id: `max_weight_clique`. Original family: Cohesion and subgroups.

**Definition.** Max weight clique.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>max_weight_clique</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.max_weight_clique(G) with node attribute weight = (7 v mod 5) - 1: (weight, 1 if the nodes form a clique)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Largest weighted cliques {#cat_clique_largest_weighted}

Measure id: `cat_clique_largest_weighted`. Original family: Cohesion and subgroups.

**Definition.** Largest weighted cliques.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_clique_largest_weighted-igraph">details</a></td><td><code>largest_weighted_cliques</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clique_largest_weighted-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: largest\_weighted\_cliques.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Max weight clique nodes {#max_weight_clique_nodes}

Measure id: `max_weight_clique_nodes`. Original family: Cohesion and subgroups.

**Definition.** Max weight clique nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>max_weight_clique_nodes</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.max_weight_clique(G)[0] (members in the order NetworkX's branch and bound adds them)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
