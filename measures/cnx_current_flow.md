---
title: "Cnx current flow"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cnx current flow

Family: Communities. Identifier: `cnx_current_flow`.

## Definition

Component labels after removing the edges of largest current-flow betweenness until at least k components exist (NetworkX's edge current-flow partition).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `edge_current_flow_betweenness_partition` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_edge_current_flow_partition` | NetworkX | any | differs | symmetric\_nodes | ties | abs 0, rel 0 | `nx.community.edge_current_flow_betweenness_partition(G, 3) on the simple undirected graph (-1 when n < 3)` | Edges whose current-flow betweenness ties in exact arithmetic (symmetric positions) differ in the last digits; NetworkX removes the one its rounding and dict order rank first, the reference the first in edge order. |

## References

[brandes2005centrality](../references.html#brandes2005centrality)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
