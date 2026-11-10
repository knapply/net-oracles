---
title: "Spectral bipartivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Spectral bipartivity

Family: Two-mode and bipartite. Identifier: `spectral_bipartivity`.

## Definition

Spectral bipartivity.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `spectral_bipartivity` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `spectral_bipartivity` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.bipartite.spectral_bipartivity(G, nodes = list(G)) and nx.bipartite.spectral_bipartivity(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
