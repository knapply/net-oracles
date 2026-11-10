---
title: "Class matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Class matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `class_matrix`. 1 measure.

## Definition {#concept-definition}

Class matrix. Entries grouped here: Class matrix.

*Definition not yet written.*

## Class matrix {#gm_class_matrix}

Measure id: `gm_class_matrix`. Original family: Matrices and spectra.

**Definition.** Class matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>attr_matrix</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gm_class_matrix</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.attr_matrix(G, node_attr = lambda v: v % 3, rc_order = [0, 1, 2])</code></td><td></td></tr><tr><td><code>gm_class_matrix_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.attr_matrix(G, edge_attr = 'weight', node_attr = lambda v: v % 3, rc_order = [0, 1, 2])</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
