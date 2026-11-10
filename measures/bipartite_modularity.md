---
title: "Bipartite modularity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bipartite modularity

Family: Two-mode and bipartite. Identifier: `bipartite_modularity`.

## Definition

Bipartite modularity.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `bipartite_modularity` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.modularity(G, blocks, top)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
