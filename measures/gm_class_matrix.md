---
title: "Class matrix"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Class matrix

Family: Matrices and spectra. Identifier: `gm_class_matrix`.

## Definition

Class matrix.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `attr_matrix` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_class_matrix` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.attr_matrix(G, node_attr = lambda v: v % 3, rc_order = [0, 1, 2])` |  |
| `gm_class_matrix_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.attr_matrix(G, edge_attr = 'weight', node_attr = lambda v: v % 3, rc_order = [0, 1, 2])` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
