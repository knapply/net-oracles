---
title: "Dominating"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Dominating

Family: Graph theory and combinatorics. Identifier: `st_dominating`.

## Definition

Dominating.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_dominating` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[nx.is_dominating_set(G, even nodes), nx.is_dominating_set(G, [0])]` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
