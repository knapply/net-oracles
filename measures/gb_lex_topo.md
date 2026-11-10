---
title: "Lex topo"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Lex topo

Family: Traversal, trees and DAGs. Identifier: `gb_lex_topo`.

## Definition

Lex topo.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_lex_topo` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.lexicographical_topological_sort(M)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
