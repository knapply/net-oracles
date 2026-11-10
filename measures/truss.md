---
title: "Truss"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Truss

Family: Cohesion and subgroups. Identifier: `truss`.

## Definition

Truss number of every edge: the largest k whose k-truss contains it.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `truss_numbers` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the largest k with the edge in nx.k_truss(G, k), G the simple undirected graph without loops (0 for loops)` |  |

## References

[batagelj2003algorithm](../references.html#batagelj2003algorithm), [carmi2007model](../references.html#carmi2007model), [goltsev2006k](../references.html#goltsev2006k), [hagberg2008exploring](../references.html#hagberg2008exploring), [hebertdufresne2016multi](../references.html#hebertdufresne2016multi), [seidman1983network](../references.html#seidman1983network), [wang2012truss](../references.html#wang2012truss)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
