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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-cat_constrained_layout_stress-graphlayouts) | `layout_constrained_stress` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_constrained_layout_stress-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Layout constrained stress3 D {#cat_constrained_d_layout_stress3}

Measure id: `cat_constrained_d_layout_stress3`. Original family: Layout.

**Definition.** Layout constrained stress3 D.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-cat_constrained_d_layout_stress3-graphlayouts) | `layout_constrained_stress3D` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_constrained_d_layout_stress3-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Layout stress quality {#layout_stress_quality}

Measure id: `layout_stress_quality`. Original family: Layout.

**Definition.** Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> | Checked, no comparison counts recorded for this entry. *(reason incomplete)* [details](#why-layout_stress_quality-networkx) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_stress_quality-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> NetworkX 3.7 was run for this measure, but the survey's comparison report records no comparison counts (neither agreeing nor differing) for the entry, so the inputs on which the tool gives no value, and why, cannot be stated from the sources. **Reason incomplete:** The sources record no comparison counts (agreeing or differing) for this entry, so the inputs on which the tool gives no value, and why, cannot be stated.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> | Checked, no comparison counts recorded for this entry. *(reason incomplete)* [details](#why-layout_stress_value-networkx) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_stress_value-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> NetworkX 3.7 was run for this measure, but the survey's comparison report records no comparison counts (neither agreeing nor differing) for the entry, so the inputs on which the tool gives no value, and why, cannot be stated from the sources. **Reason incomplete:** The sources record no comparison counts (agreeing or differing) for this entry, so the inputs on which the tool gives no value, and why, cannot be stated.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-cat_d_layout_stress3-graphlayouts) | `layout_stress3D` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_d_layout_stress3-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Maxent Stress {#cat_maxent_stress}

Measure id: `cat_maxent_stress`. Original family: Layout.

**Definition.** Maxent Stress.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_maxent_stress-networkit) | `MaxentStress` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_maxent_stress-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: MaxentStress.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Sparse stress / pivot MDS layout {#layout_sparse_stress}

Measure id: `layout_sparse_stress`. Original family: Layout.

**Definition.** Sparse stress / pivot MDS layout.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-layout_sparse_stress-graphlayouts) | `layout_sparse_stress` | documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_sparse_stress-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Stress-majorization layout (Kamada-Kawai energy) {#layout_stress}

Measure id: `layout_stress`. Original family: Layout.

**Definition.** Stress-majorization layout (Kamada-Kawai energy).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  | documentation |
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-layout_stress-graphlayouts) | `layout_stress` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_stress-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_graphlayouts](../../references.html#tool_graphlayouts)
{% endraw %}
