---
title: "Lexicographic"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Lexicographic

Family: Traversal, trees and DAGs. Identifier: `lexicographic`.

## Definition

Lexicographic.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_lexicographic` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.lexicographical_topological_sort(D))` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
