---
title: "Stoer wagner"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Stoer wagner

Family: Traversal, trees and DAGs. Identifier: `gb_stoer_wagner`.

## Definition

Stoer wagner.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_stoer_wagner` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.stoer_wagner(nx.Graph(M))` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
