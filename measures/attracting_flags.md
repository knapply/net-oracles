---
title: "Attracting flags"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Attracting flags

Family: Components and connectivity. Identifier: `attracting_flags`.

## Definition

Attracting flags.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_attracting_flags` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `1 if v is in a component of nx.attracting_components(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
