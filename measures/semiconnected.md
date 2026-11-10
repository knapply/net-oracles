---
title: "Semiconnected"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Semiconnected

Family: Components and connectivity. Identifier: `semiconnected`.

## Definition

Semiconnected.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `is_semiconnected` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_semiconnected` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_semiconnected(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
