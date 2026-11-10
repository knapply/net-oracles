---
title: "Generalized degree"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Generalized degree {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `generalized_degree`. 1 measure.

## Definition {#concept-definition}

Generalized degree. Entries grouped here: Generalized degree.

*Definition not yet written.*

## Generalized degree {#generalized_degree}

Measure id: `generalized_degree`. Original family: Graph theory and combinatorics.

**Definition.** Generalized degree.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>generalized_degree</code></td><td></td></tr><tr><td><a href="../../tools/graphblas.html">GraphBLAS algorithms</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>generalized_degree</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.generalized_degree(G)</code></td><td></td></tr><tr><td><code>generalized_degree</code></td><td>GraphBLAS algorithms</td><td>undirected</td><td>differs</td><td>multi_edges</td><td>direction, multi_edges, weights</td><td>abs 0, rel 0</td><td><code>nx.generalized_degree(G simple, backend = 'graphblas')</code></td><td>graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge.</td></tr></tbody></table></div>

**Tools cited:** [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
