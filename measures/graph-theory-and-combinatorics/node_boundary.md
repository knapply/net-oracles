---
title: "Node boundary"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Node boundary {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `node_boundary`. 1 measure.

## Definition {#concept-definition}

Node boundary. Entries grouped here: Node boundary.

## Node boundary {#gb_node_boundary}

Measure id: `gb_node_boundary`. Original family: Traversal, trees and DAGs.

**Definition.** Node boundary.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_node_boundary` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.node_boundary(M, {0, 1, 2}))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
