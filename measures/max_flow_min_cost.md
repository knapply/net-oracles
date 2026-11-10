---
title: "Max flow min cost"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Max flow min cost

Family: Components and connectivity. Identifier: `max_flow_min_cost`.

## Definition

A maximum flow of least cost between two nodes, with its value.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `cost_of_flow; max_flow_min_cost; min_cost_flow; min_cost_flow_cost; network_simplex` |  |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `cycle_canceling; successive_shortest_path_nonnegative_weights` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_max_flow_min_cost` | NetworkX | directed | no-value-on-some-inputs |  | weights | abs 1e-09, rel 1e-09 | `F = nx.maximum_flow_value(G, 0, n - 1); nx.min_cost_flow_cost(M) on the multigraph M with demand -F at 0 and F at n - 1` | NetworkX's network simplex reports this real-valued problem infeasible (NetworkXUnfeasible): its documentation warns that it may fail on floating-point capacities and suggests integers. The linear program of the definition oracle confirms the reference value's value and cost. |

## References

[ahuja1993network](../references.html#ahuja1993network), [cunningham1976network](../references.html#cunningham1976network), [dantzig1951application](../references.html#dantzig1951application), [grigoriadis1986efficient](../references.html#grigoriadis1986efficient), [hagberg2008exploring](../references.html#hagberg2008exploring)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [siek2002boost](../references.html#siek2002boost)
{% endraw %}
