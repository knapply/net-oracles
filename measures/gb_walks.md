---
title: "Walks"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Walks

Family: Traversal, trees and DAGs. Identifier: `gb_walks`.

## Definition

Walks.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `number_of_walks` |  |
| [NetworKit](../tools/networkit.html) | · reported in docs | `walk` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_walks` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.number_of_walks(M, 2)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
