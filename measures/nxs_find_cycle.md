---
title: "Nxs find cycle"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nxs find cycle

Family: Graph theory and combinatorics. Identifier: `nxs_find_cycle`.

## Definition

Nxs find cycle.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_find_cycle_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, orientation = 'ignore'), with 1 for an edge reported 'reverse'` |  |
| `nxs_find_cycle_ignore_source` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, source = n // 2, orientation = 'ignore')` |  |
| `nxs_find_cycle_none` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(G) on the simple graph with loops (the cycle's edges; (-1, -1) if none)` |  |
| `nxs_find_cycle_none_source` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(G, source = n // 2)` |  |
| `nxs_find_cycle_original` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, orientation = 'original')` |  |
| `nxs_find_cycle_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, orientation = 'reverse'), with 1 for an edge reported 'reverse'` |  |
| `nxs_find_cycle_reverse_source` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(D, source = n // 2, orientation = 'reverse')` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
