---
title: "Nx hk mates"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nx hk mates

Family: Two-mode and bipartite. Identifier: `nx_hk_mates`.

## Definition

Nx hk mates.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_hk_mates` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.hopcroft_karp_matching(G, top_nodes = top): each node's mate, -1 if unmatched; [-1] if top is not a side` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
