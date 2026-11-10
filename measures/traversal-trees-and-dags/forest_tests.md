---
title: "Tree, forest and arborescence tests"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Tree, forest and arborescence tests {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `forest_tests`. 1 measure.

## Definition {#concept-definition}

Tree, forest and arborescence tests. Entries grouped here: Forest flags.

## Forest flags {#nxs_forest_flags}

Measure id: `nxs_forest_flags`. Original family: Graph theory and combinatorics.

**Definition.** Forest flags.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `is_arborescence; is_branching; is_forest; is_tree` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `is_forest; is_tree` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `is_tree` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_forest_flags` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_tree, nx.is_forest, nx.is_arborescence, nx.is_branching on the multigraph` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
