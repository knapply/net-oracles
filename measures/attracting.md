---
title: "Attracting"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Attracting

Family: Components and connectivity. Identifier: `attracting`.

## Definition

Attracting.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `attracting_components` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_attracting` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.attracting_components(G), labelled by nx.condensation(G).graph['mapping'], -1 elsewhere` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
