---
title: "Triads"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Triads

Family: Graph theory and combinatorics. Identifier: `st_triads`.

## Definition

Triads.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_triads` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.triadic_census(G), (G, even nodes), (G, [0]) on the MultiDiGraph` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
