---
title: "Nx eppstein size"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nx eppstein size

Family: Two-mode and bipartite. Identifier: `nx_eppstein_size`.

## Definition

Nx eppstein size.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_eppstein_size` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `(len(eppstein_matching) / 2, 1 if every pair is an edge matched both ways); [-1] if top is not a side` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
