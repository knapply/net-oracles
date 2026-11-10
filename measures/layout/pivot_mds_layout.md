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

*Definition not yet written.* Documented by name only; the sources record the tool functions (pivot MDS) but the pivot-based formulas were not checked against the original paper.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_layout_pmds">Layout pmds</a></td><td><code>cat_layout_pmds</code></td><td>1</td></tr><tr><td><a href="#cat_mds_pivot">Pivot MDS</a></td><td><code>cat_mds_pivot</code></td><td>1</td></tr></tbody></table></div>

## Layout pmds {#cat_layout_pmds}

Measure id: `cat_layout_pmds`. Original family: Layout.

**Definition.** Layout pmds.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-cat_layout_pmds-graphlayouts">details</a></td><td><code>layout_pmds</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_layout_pmds-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Pivot MDS {#cat_mds_pivot}

Measure id: `cat_mds_pivot`. Original family: Graph theory and combinatorics.

**Definition.** Pivot MDS.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_mds_pivot-networkit">details</a></td><td><code>PivotMDS</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mds_pivot-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: PivotMDS.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
