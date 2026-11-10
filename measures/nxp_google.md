---
title: "Google"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Google

Family: Centrality. Identifier: `nxp_google`.

## Definition

Google.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `google_matrix` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_google` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.google_matrix(G, weight = None)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
