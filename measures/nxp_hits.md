---
title: "Nxp hits"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nxp hits

Family: Centrality. Identifier: `nxp_hits`.

## Definition

NetworkX's hubs and authorities iteration, reproduced step for step; reports when it does not converge.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_hits` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.hits(G) (power iteration; graph read without weights)` |  |
| `nxp_hits_raw_weighted` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.hits(G, normalized = False)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
