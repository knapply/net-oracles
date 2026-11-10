---
title: "Gomory hu"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Gomory hu

Family: Components and connectivity. Identifier: `gomory_hu`.

## Definition

The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `gomory_hu_tree` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `gomory_hu_tree` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `GusfieldGomoryHuCutTree` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_gomory_hu_tree` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.gomory_hu_tree(G, capacity = 'capacity').edges(data = 'weight'), as (u, v, weight) with u < v` |  |

## References

[gomory1961multi](../references.html#gomory1961multi), [gusfield1990very](../references.html#gusfield1990very), [hagberg2008exploring](../references.html#hagberg2008exploring)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht)
{% endraw %}
