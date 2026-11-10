---
title: "Cnx label propagation"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cnx label propagation

Family: Communities. Identifier: `cnx_label_propagation`.

## Definition

Cnx label propagation.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_label_propagation` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.label_propagation_communities(G) on the simple undirected graph` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
