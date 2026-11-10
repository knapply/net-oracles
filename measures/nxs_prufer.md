---
title: "Prufer"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Prufer

Family: Graph theory and combinatorics. Identifier: `nxs_prufer`.

## Definition

Prufer.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `to_prufer` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_prufer` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.to_prufer_sequence(T) (nothing below three nodes)` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
