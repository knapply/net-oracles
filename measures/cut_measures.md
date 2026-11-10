---
title: "Cut measures"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cut measures

Family: Components and connectivity. Identifier: `cut_measures`.

## Definition

Cut measures.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cut_measures` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.cut_size, volume, normalized_cut_size, conductance, edge_expansion, mixing_expansion, node_expansion, boundary_expansion with S = even nodes, T = the rest` |  |
| `cut_measures_overlap` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `the same functions with T = nodes v % 3 == 1` |  |
| `cut_measures_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `the same functions with weight = 'weight'` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
