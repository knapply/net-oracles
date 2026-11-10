---
title: "Tree broadcast time and center"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Tree broadcast time and center {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `tree_broadcast`. 2 measures.

## Definition {#concept-definition}

Tree broadcast time and center. Entries grouped here: Broadcast time; Tree broadcast center.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Broadcast time](#gb_broadcast_time) | `gb_broadcast_time` | 1 |
| [Tree broadcast center](#cat_broadcast_center_tree) | `cat_broadcast_center_tree` | 1 |

## Broadcast time {#gb_broadcast_time}

Measure id: `gb_broadcast_time`. Original family: Traversal, trees and DAGs.

**Definition.** Broadcast time.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `tree_broadcast_time` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_broadcast_time` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.tree_broadcast_time(nx.Graph(M))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Tree broadcast center {#cat_broadcast_center_tree}

Measure id: `cat_broadcast_center_tree`. Original family: Traversal, trees and DAGs.

**Definition.** Tree broadcast center.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `tree_broadcast_center` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
