---
title: "Birank"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Birank

Family: Two-mode and bipartite. Identifier: `birank`.

## Definition

BiRank scores of both node sets of a bipartite graph: the fixed point of damped, normalized propagation between the sets.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `birank` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `birank` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.birank(G, top, max_iter = 1000, tol = 1e-10)` |  |

## References

[he2017birank](../references.html#he2017birank)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
