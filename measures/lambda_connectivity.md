---
title: "Lambda connectivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Lambda connectivity

Family: Cohesion and subgroups. Identifier: `lambda_connectivity`.

## Definition

Edge connectivity between every pair of nodes, read off Gusfield's flow tree.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `lambda_connectivity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.edge_connectivity(G, u, v) for every pair of the simple undirected graph` |  |
| `lambda_connectivity` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::edge_connectivity(g, source = u, target = v) on simplify(as_undirected(g))` |  |

## References

[borgatti1990ls](../references.html#borgatti1990ls), [edmonds1972theoretical](../references.html#edmonds1972theoretical), [ford1956maximal](../references.html#ford1956maximal), [gomory1961multi](../references.html#gomory1961multi), [gusfield1990very](../references.html#gusfield1990very)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
