---
title: "Max weight clique"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Max weight clique

Family: Cohesion and subgroups. Identifier: `max_weight_clique`.

## Definition

Max weight clique.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `max_weight_clique` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.max_weight_clique(G) with node attribute weight = (7 v mod 5) - 1: (weight, 1 if the nodes form a clique)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
