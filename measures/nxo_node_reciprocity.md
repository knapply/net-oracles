---
title: "Node reciprocity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Node reciprocity

Family: Descriptive statistics. Identifier: `nxo_node_reciprocity`.

## Definition

Node reciprocity.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [GraphBLAS algorithms](../tools/graphblas.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Reciprocity (arc vs dyad question has its own FAQ), normalized reciprocity (6.834); indrecip` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_node_reciprocity` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.reciprocity(nx.DiGraph(G), nodes = every node)` |  |
| `nxo_node_reciprocity` | GraphBLAS algorithms | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-14, rel 1e-12 | `nx.reciprocity(DiGraph, nodes, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
