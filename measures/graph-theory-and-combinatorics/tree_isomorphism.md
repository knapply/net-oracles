---
title: "Tree isomorphism"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Tree isomorphism {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `tree_isomorphism`. 1 measure.

## Definition {#concept-definition}

Tree isomorphism. Entries grouped here: Tree iso.

*Definition not yet written.*

## Tree iso {#tree_iso}

Measure id: `tree_iso`. Original family: Graph theory and combinatorics.

**Definition.** Tree iso.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>tree_iso</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>isomorphism.tree_isomorphism(T1, T2), (T1, T3), isomorphism.rooted_tree_isomorphism(T1, 0, T2, k - 1), (T1, 0, T2, k - 2); (non-empty, valid) each</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
