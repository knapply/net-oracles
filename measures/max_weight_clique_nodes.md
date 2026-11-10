---
title: "Max weight clique nodes"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Max weight clique nodes

Family: Cohesion and subgroups. Identifier: `max_weight_clique_nodes`.

## Definition

Max weight clique nodes.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `max_weight_clique_nodes` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.max_weight_clique(G)[0] (members in the order NetworkX's branch and bound adds them)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
