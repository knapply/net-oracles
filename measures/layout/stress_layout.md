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

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_constrained_layout_stress">Layout constrained stress</a></td><td><code>cat_constrained_layout_stress</code></td><td>1</td></tr><tr><td><a href="#cat_constrained_d_layout_stress3">Layout constrained stress3 D</a></td><td><code>cat_constrained_d_layout_stress3</code></td><td>1</td></tr><tr><td><a href="#layout_stress_quality">Layout stress quality</a></td><td><code>layout_stress_quality</code></td><td>1</td></tr><tr><td><a href="#layout_stress_value">Layout stress value</a></td><td><code>layout_stress_value</code></td><td>1</td></tr><tr><td><a href="#cat_d_layout_stress3">Layout stress3 D</a></td><td><code>cat_d_layout_stress3</code></td><td>1</td></tr><tr><td><a href="#cat_maxent_stress">Maxent Stress</a></td><td><code>cat_maxent_stress</code></td><td>1</td></tr><tr><td><a href="#layout_sparse_stress">Sparse stress / pivot MDS layout</a></td><td><code>layout_sparse_stress</code></td><td>1</td></tr><tr><td><a href="#layout_stress">Stress-majorization layout (Kamada-Kawai energy)</a></td><td><code>layout_stress</code></td><td>2</td></tr></tbody></table></div>

## References {#concept-references}

[brandes2007eigensolver](../../references.html#brandes2007eigensolver), [brandes2009experimental](../../references.html#brandes2009experimental), [gansner2005graph](../../references.html#gansner2005graph), [kamada1989algorithm](../../references.html#kamada1989algorithm), [mises1929praktische](../../references.html#mises1929praktische), [ortmann2017sparse](../../references.html#ortmann2017sparse)

## Layout constrained stress {#cat_constrained_layout_stress}

Measure id: `cat_constrained_layout_stress`. Original family: Layout.

**Definition.** Layout constrained stress.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-cat_constrained_layout_stress-graphlayouts">details</a></td><td><code>layout_constrained_stress</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_constrained_layout_stress-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Layout constrained stress3 D {#cat_constrained_d_layout_stress3}

Measure id: `cat_constrained_d_layout_stress3`. Original family: Layout.

**Definition.** Layout constrained stress3 D.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-cat_constrained_d_layout_stress3-graphlayouts">details</a></td><td><code>layout_constrained_stress3D</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_constrained_d_layout_stress3-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Layout stress quality {#layout_stress_quality}

Measure id: `layout_stress_quality`. Original family: Layout.

**Definition.** Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a></td><td>Checked, no comparison counts recorded for this entry. <em>(reason incomplete)</em> <a href="#why-layout_stress_quality-networkx">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_stress_quality-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> NetworkX 3.7 was run for this measure, but the survey's comparison report records no comparison counts (neither agreeing nor differing) for the entry, so the inputs on which the tool gives no value, and why, cannot be stated from the sources. **Reason incomplete:** The sources record no comparison counts (agreeing or differing) for this entry, so the inputs on which the tool gives no value, and why, cannot be stated.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>layout_stress_vs_kamada_kawai</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 0.02</td><td><code>optimally scaled stress of nx.kamada_kawai_layout of the largest component (0 below 3 nodes)</code></td><td></td></tr><tr><td><code>layout_stress_vs_kamada_kawai_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 0.02</td><td><code>optimally scaled weighted stress of nx.kamada_kawai_layout(weight = 'weight') of the largest component</code></td><td></td></tr></tbody></table></div>

**References:** [brandes2007eigensolver](../../references.html#brandes2007eigensolver), [brandes2009experimental](../../references.html#brandes2009experimental), [gansner2005graph](../../references.html#gansner2005graph), [kamada1989algorithm](../../references.html#kamada1989algorithm), [mises1929praktische](../../references.html#mises1929praktische), [ortmann2017sparse](../../references.html#ortmann2017sparse)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Layout stress value {#layout_stress_value}

Measure id: `layout_stress_value`. Original family: Layout.

**Definition.** Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a></td><td>Checked, no comparison counts recorded for this entry. <em>(reason incomplete)</em> <a href="#why-layout_stress_value-networkx">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_stress_value-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> NetworkX 3.7 was run for this measure, but the survey's comparison report records no comparison counts (neither agreeing nor differing) for the entry, so the inputs on which the tool gives no value, and why, cannot be stated from the sources. **Reason incomplete:** The sources record no comparison counts (agreeing or differing) for this entry, so the inputs on which the tool gives no value, and why, cannot be stated.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>layout_stress_value</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>the stress sum with nx.all_pairs_shortest_path_length on the skeleton</code></td><td></td></tr><tr><td><code>layout_stress_value_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>the stress sum with nx.all_pairs_dijkstra_path_length on the skeleton</code></td><td></td></tr></tbody></table></div>

**References:** [brandes2007eigensolver](../../references.html#brandes2007eigensolver), [brandes2009experimental](../../references.html#brandes2009experimental), [gansner2005graph](../../references.html#gansner2005graph), [kamada1989algorithm](../../references.html#kamada1989algorithm), [mises1929praktische](../../references.html#mises1929praktische), [ortmann2017sparse](../../references.html#ortmann2017sparse)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Layout stress3 D {#cat_d_layout_stress3}

Measure id: `cat_d_layout_stress3`. Original family: Layout.

**Definition.** Layout stress3 D.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-cat_d_layout_stress3-graphlayouts">details</a></td><td><code>layout_stress3D</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_d_layout_stress3-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Maxent Stress {#cat_maxent_stress}

Measure id: `cat_maxent_stress`. Original family: Layout.

**Definition.** Maxent Stress.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_maxent_stress-networkit">details</a></td><td><code>MaxentStress</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_maxent_stress-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: MaxentStress.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Sparse stress / pivot MDS layout {#layout_sparse_stress}

Measure id: `layout_sparse_stress`. Original family: Layout.

**Definition.** Sparse stress / pivot MDS layout.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-layout_sparse_stress-graphlayouts">details</a></td><td><code>layout_sparse_stress</code></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_sparse_stress-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Stress-majorization layout (Kamada-Kawai energy) {#layout_stress}

Measure id: `layout_stress`. Original family: Layout.

**Definition.** Stress-majorization layout (Kamada-Kawai energy).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td>documentation</td></tr><tr><td><a href="../../tools/graphlayouts.html">graphlayouts</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: graphlayouts is documented-only in this survey; listed in its documentation. <a href="#why-layout_stress-graphlayouts">details</a></td><td><code>layout_stress</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_stress-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_graphlayouts](../../references.html#tool_graphlayouts)
{% endraw %}
