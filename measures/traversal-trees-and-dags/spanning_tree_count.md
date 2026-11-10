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

## References {#concept-references}

[kirchhoff1847ueber](../../references.html#kirchhoff1847ueber), [tutte1948dissection](../../references.html#tutte1948dissection)

## Spanning trees {#gb_spanning_trees}

Measure id: `gb_spanning_trees`. Original family: Traversal, trees and DAGs.

**Definition.** Number of spanning trees (arborescences rooted at the root for a directed network) by the matrix-tree theorem.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `number_of_spanning_trees` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_spanning_trees` | NetworkX | undirected | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.number_of_spanning_trees(M)` |  |

**References:** [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber), [tutte1948dissection](../../references.html#tutte1948dissection)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
