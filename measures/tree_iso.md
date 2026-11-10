---
title: "Tree iso"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Tree iso

Family: Graph theory and combinatorics. Identifier: `tree_iso`.

## Definition

Tree iso.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `tree_iso` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `isomorphism.tree_isomorphism(T1, T2), (T1, T3), isomorphism.rooted_tree_isomorphism(T1, 0, T2, k - 1), (T1, 0, T2, k - 2); (non-empty, valid) each` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
