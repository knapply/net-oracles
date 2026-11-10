---
title: "Pivot MDS layout"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Pivot MDS layout {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `pivot_mds_layout`. 2 measures.

## Definition {#concept-definition}

Pivot MDS layout. Entries grouped here: Layout pmds; Pivot MDS.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Layout pmds](#cat_layout_pmds) | `cat_layout_pmds` | 1 |
| [Pivot MDS](#cat_mds_pivot) | `cat_mds_pivot` | 1 |

## Layout pmds {#cat_layout_pmds}

Measure id: `cat_layout_pmds`. Original family: Layout.

**Definition.** Layout pmds.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-cat_layout_pmds-graphlayouts) | `layout_pmds` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_layout_pmds-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Pivot MDS {#cat_mds_pivot}

Measure id: `cat_mds_pivot`. Original family: Graph theory and combinatorics.

**Definition.** Pivot MDS.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_mds_pivot-networkit) | `PivotMDS` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mds_pivot-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: PivotMDS.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
