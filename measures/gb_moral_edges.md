---
title: "Moral edges"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Moral edges

Family: Traversal, trees and DAGs. Identifier: `gb_moral_edges`.

## Definition

Moral edges.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `moral_graph` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_moral_edges` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `distinct pairs of nx.moral_graph(M)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
