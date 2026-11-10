---
title: "Modularity nx"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Modularity nx

Family: Communities. Identifier: `cnx_modularity_nx`.

## Definition

Modularity nx.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_modularity_nx` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.community.modularity(G_natural, blocks, weight = 'weight' if weighted)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
