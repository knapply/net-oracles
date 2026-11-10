---
title: "Find cycle"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Find cycle

Family: Graph theory and combinatorics. Identifier: `find_cycle`.

## Definition

Find cycle.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `find_cycle` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `find_cycle` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_find_cycle` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `get_cycles` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `CycleDetector` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_find_cycle` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(M) as (key, 0) pairs, nothing on NetworkXNoCycle` |  |
| `cyc_find_cycle_ignore` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(M, orientation = 'ignore') as (key, reversed) pairs` |  |
| `cyc_find_cycle_reverse` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.find_cycle(M, orientation = 'reverse') as (key, reversed) pairs` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
