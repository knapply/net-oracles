---
title: "Layout stress quality"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Layout stress quality

Family: Layout. Identifier: `layout_stress_quality`.

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
| `layout_stress_vs_kamada_kawai` | NetworkX | any | agrees |  |  | abs 1e-09, rel 0.02 | `optimally scaled stress of nx.kamada_kawai_layout of the largest component (0 below 3 nodes)` |  |
| `layout_stress_vs_kamada_kawai_weighted` | NetworkX | any | agrees |  |  | abs 1e-09, rel 0.02 | `optimally scaled weighted stress of nx.kamada_kawai_layout(weight = 'weight') of the largest component` |  |

## References

[brandes2007eigensolver](../references.html#brandes2007eigensolver), [brandes2009experimental](../references.html#brandes2009experimental), [gansner2005graph](../references.html#gansner2005graph), [kamada1989algorithm](../references.html#kamada1989algorithm), [mises1929praktische](../references.html#mises1929praktische), [ortmann2017sparse](../references.html#ortmann2017sparse)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
