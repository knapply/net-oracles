---
title: "Nx eppstein"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nx eppstein

Family: Two-mode and bipartite. Identifier: `nx_eppstein`.

## Definition

Nx eppstein.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_eppstein` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.eppstein_matching(G, top_nodes = top): the dictionary's (key, value) pairs in order; [-1] if top is not a side` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
