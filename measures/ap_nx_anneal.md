---
title: "Nx anneal"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nx anneal

Family: Graph theory and combinatorics. Identifier: `ap_nx_anneal`.

## Definition

Nx anneal.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_nx_anneal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `simulated_annealing_tsp and threshold_accepting_tsp(K, 'greedy', move='1-1' and '1-0', seed=7), each tour with its length first; [-1] if disconnected or under three nodes` |  |
| `ap_nx_anneal_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's tours` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
