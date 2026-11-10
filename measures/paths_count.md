---
title: "Paths count"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths count

Family: Paths and distances. Identifier: `paths_count`.

## Definition

Paths count.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `count_shortest_paths` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_count_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.all_shortest_paths(G, 0, t))) for every t (0 without a path)` |  |
| `paths_count_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.all_shortest_paths(G, 0, t, weight = 'weight'))) for every t` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool)
{% endraw %}
