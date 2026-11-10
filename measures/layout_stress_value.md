---
title: "Layout stress value"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Layout stress value

Family: Layout. Identifier: `layout_stress_value`.

## Definition

Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `layout_stress_value` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `the stress sum with nx.all_pairs_shortest_path_length on the skeleton` |  |
| `layout_stress_value_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `the stress sum with nx.all_pairs_dijkstra_path_length on the skeleton` |  |

## References

[brandes2007eigensolver](../references.html#brandes2007eigensolver), [brandes2009experimental](../references.html#brandes2009experimental), [gansner2005graph](../references.html#gansner2005graph), [kamada1989algorithm](../references.html#kamada1989algorithm), [mises1929praktische](../references.html#mises1929praktische), [ortmann2017sparse](../references.html#ortmann2017sparse)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
