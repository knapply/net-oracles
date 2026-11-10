---
title: "Number of spanning trees"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Number of spanning trees {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Spanning trees and branchings. Concept id: `spanning_tree_count`. 1 measure.

## Definition {#concept-definition}

Number of spanning trees (arborescences rooted at the root for a directed network) by the matrix-tree theorem.

*Definition not yet written.*

## References {#concept-references}

[kirchhoff1847ueber](../../references.html#kirchhoff1847ueber), [tutte1948dissection](../../references.html#tutte1948dissection)

## Spanning trees {#gb_spanning_trees}

Measure id: `gb_spanning_trees`. Original family: Traversal, trees and DAGs.

**Definition.** Number of spanning trees (arborescences rooted at the root for a directed network) by the matrix-tree theorem.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>number_of_spanning_trees</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_spanning_trees</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>nx.number_of_spanning_trees(M)</code></td><td></td></tr></tbody></table></div>

**References:** [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber), [tutte1948dissection](../../references.html#tutte1948dissection)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
