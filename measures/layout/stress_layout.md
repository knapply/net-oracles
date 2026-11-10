---
title: "Stress-based layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Stress-based layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `stress_layout`. 8 measures.

## Definition {#concept-definition}

Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Layout constrained stress](#cat_constrained_layout_stress) | `cat_constrained_layout_stress` | 1 |
| [Layout constrained stress3 D](#cat_constrained_d_layout_stress3) | `cat_constrained_d_layout_stress3` | 1 |
| [Layout stress quality](#layout_stress_quality) | `layout_stress_quality` | 1 |
| [Layout stress value](#layout_stress_value) | `layout_stress_value` | 1 |
| [Layout stress3 D](#cat_d_layout_stress3) | `cat_d_layout_stress3` | 1 |
| [Maxent Stress](#cat_maxent_stress) | `cat_maxent_stress` | 1 |
| [Sparse stress / pivot MDS layout](#layout_sparse_stress) | `layout_sparse_stress` | 1 |
| [Stress-majorization layout (Kamada-Kawai energy)](#layout_stress) | `layout_stress` | 2 |

## References {#concept-references}

[brandes2007eigensolver](../../references.html#brandes2007eigensolver), [brandes2009experimental](../../references.html#brandes2009experimental), [gansner2005graph](../../references.html#gansner2005graph), [kamada1989algorithm](../../references.html#kamada1989algorithm), [mises1929praktische](../../references.html#mises1929praktische), [ortmann2017sparse](../../references.html#ortmann2017sparse)

## Layout constrained stress {#cat_constrained_layout_stress}

Measure id: `cat_constrained_layout_stress`. Original family: Layout.

**Definition.** Layout constrained stress.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | · reported in docs | `layout_constrained_stress` | API listing |

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Layout constrained stress3 D {#cat_constrained_d_layout_stress3}

Measure id: `cat_constrained_d_layout_stress3`. Original family: Layout.

**Definition.** Layout constrained stress3 D.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | · reported in docs | `layout_constrained_stress3D` | API listing |

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Layout stress quality {#layout_stress_quality}

Measure id: `layout_stress_quality`. Original family: Layout.

**Definition.** Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `layout_stress_vs_kamada_kawai` | NetworkX | any | agrees |  |  | abs 1e-09, rel 0.02 | `optimally scaled stress of nx.kamada_kawai_layout of the largest component (0 below 3 nodes)` |  |
| `layout_stress_vs_kamada_kawai_weighted` | NetworkX | any | agrees |  |  | abs 1e-09, rel 0.02 | `optimally scaled weighted stress of nx.kamada_kawai_layout(weight = 'weight') of the largest component` |  |

**References:** [brandes2007eigensolver](../../references.html#brandes2007eigensolver), [brandes2009experimental](../../references.html#brandes2009experimental), [gansner2005graph](../../references.html#gansner2005graph), [kamada1989algorithm](../../references.html#kamada1989algorithm), [mises1929praktische](../../references.html#mises1929praktische), [ortmann2017sparse](../../references.html#ortmann2017sparse)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Layout stress value {#layout_stress_value}

Measure id: `layout_stress_value`. Original family: Layout.

**Definition.** Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `layout_stress_value` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `the stress sum with nx.all_pairs_shortest_path_length on the skeleton` |  |
| `layout_stress_value_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `the stress sum with nx.all_pairs_dijkstra_path_length on the skeleton` |  |

**References:** [brandes2007eigensolver](../../references.html#brandes2007eigensolver), [brandes2009experimental](../../references.html#brandes2009experimental), [gansner2005graph](../../references.html#gansner2005graph), [kamada1989algorithm](../../references.html#kamada1989algorithm), [mises1929praktische](../../references.html#mises1929praktische), [ortmann2017sparse](../../references.html#ortmann2017sparse)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Layout stress3 D {#cat_d_layout_stress3}

Measure id: `cat_d_layout_stress3`. Original family: Layout.

**Definition.** Layout stress3 D.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | · reported in docs | `layout_stress3D` | API listing |

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Maxent Stress {#cat_maxent_stress}

Measure id: `cat_maxent_stress`. Original family: Layout.

**Definition.** Maxent Stress.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `MaxentStress` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Sparse stress / pivot MDS layout {#layout_sparse_stress}

Measure id: `layout_sparse_stress`. Original family: Layout.

**Definition.** Sparse stress / pivot MDS layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | · reported in docs | `layout_sparse_stress` | documentation |

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Stress-majorization layout (Kamada-Kawai energy) {#layout_stress}

Measure id: `layout_stress`. Original family: Layout.

**Definition.** Stress-majorization layout (Kamada-Kawai energy).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  | documentation |
| [graphlayouts](../../tools/graphlayouts.html) | · reported in docs | `layout_stress` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_graphlayouts](../../references.html#tool_graphlayouts)
{% endraw %}
