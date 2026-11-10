---
title: "Onion"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Onion

Family: Cohesion and subgroups. Identifier: `onion`.

## Definition

Onion layer of every node, from 1: the round of the core peeling in which it is removed.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `onion_layers` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.onion_layers(G), G the simple undirected graph without loops` |  |

## References

[batagelj2003algorithm](../references.html#batagelj2003algorithm), [carmi2007model](../references.html#carmi2007model), [goltsev2006k](../references.html#goltsev2006k), [hagberg2008exploring](../references.html#hagberg2008exploring), [hebertdufresne2016multi](../references.html#hebertdufresne2016multi), [seidman1983network](../references.html#seidman1983network), [wang2012truss](../references.html#wang2012truss)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
