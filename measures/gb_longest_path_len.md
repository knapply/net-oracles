---
title: "Longest path len"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Longest path len

Family: Traversal, trees and DAGs. Identifier: `gb_longest_path_len`.

## Definition

Longest path len.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_longest_path_len` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `len(nx.dag_longest_path(M, weight=None)) - 1` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
