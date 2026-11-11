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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(X=(x_1,\dots,x_n)\)</td><td>node coordinates in \(\mathbb R^2\) (or \(\mathbb R^3\) for the three-dimensional layouts)</td></tr><tr><td>\(d_{ij}\)</td><td>graph distance between \(i\) and \(j\): hops, or the sum of edge lengths for weighted layouts; \(\infty\) between components</td></tr><tr><td>\(w_{ij}\)</td><td>pair weight, \(d_{ij}^{-2}\) in the stress and Kamada-Kawai models</td></tr><tr><td>\(\|\cdot\|\)</td><td>Euclidean norm</td></tr><tr><td>\(\alpha\)</td><td>a uniform scale factor applied to the layout</td></tr></tbody></table></div>

## Definition {#concept-definition}

Stress-majorization layout: two coordinates per node whose distances approximate the graph distances, on all pairs or on pivots.

*Definition partly written:* The stress and Kamada-Kawai objectives and the optimal scaling are written. The constrained, three-dimensional and maximum-entropy variants and the sparse stress model are named in the sources only: their objectives and constraints are not written here, so their variants have no entry. The comparison builds the distances on the undirected skeleton of the input (loops dropped, parallel edges keep the smallest weight).

<div class="formula-block"><p class="formula-name"><strong>Stress (Kamada and Kawai 1989; Gansner, Koren and North 2005)</strong> <span class="applies">applies to: any, connected</span></p><div class="formula">\[\sigma(X)=\sum_{i&lt;j}w_{ij}\bigl(\|x_i-x_j\|-d_{ij}\bigr)^2,\qquad w_{ij}=d_{ij}^{-2}\]</div><p class="formula-where">The weighted squared mismatch between layout distance and graph distance. The Kamada-Kawai energy is the same sum with spring constant \(k_{ij}=K/d_{ij}^2\) and natural length \(L\,d_{ij}\) (\(K,L\) constants), so the two minimizers coincide up to scale. The sum runs over pairs with finite \(d_{ij}\); layouts are determined up to rotation, reflection and translation.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Optimally scaled stress</strong> <span class="applies">applies to: any, connected</span></p><div class="formula">\[\sigma^\ast(X)=\min_{\alpha&gt;0}\sigma(\alpha X)=\sum_{i&lt;j}w_{ij}d_{ij}^2-\frac{\bigl(\sum_{i&lt;j}w_{ij}d_{ij}\|x_i-x_j\|\bigr)^2}{\sum_{i&lt;j}w_{ij}\|x_i-x_j\|^2}\]</div><p class="formula-where">Stress after the best uniform rescaling, which removes the arbitrary unit of the layout, so values of layouts produced with different scales are comparable. Needs at least one pair with \(\|x_i-x_j\|&gt;0\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Stress majorization step (Gansner, Koren and North 2005)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[x_i^{(t+1)}=\frac{\sum_{j\ne i}w_{ij}\Bigl(x_j^{(t)}+d_{ij}\dfrac{x_i^{(t)}-x_j^{(t)}}{\|x_i^{(t)}-x_j^{(t)}\|}\Bigr)}{\sum_{j\ne i}w_{ij}}\]</div><p class="formula-where">Localized update of one node with the others fixed; it never increases \(\sigma\). The result depends on the starting coordinates, so a layout is reproducible only for a fixed start or seed.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#layout_stress_quality">Layout stress quality</a></td><td><code>layout_stress_quality</code></td><td>1</td><td>The optimally scaled stress \(\sigma^\ast(X)\) of a layout, hop or weighted distances; set to 0 when the layout has fewer than three nodes.</td></tr><tr><td><a href="#layout_stress_value">Layout stress value</a></td><td><code>layout_stress_value</code></td><td>1</td><td>The number \(\sigma(X)\) of a given layout, with \(w_{ij}=d_{ij}^{-2}\) and distances in hops or by edge weights, over pairs inside one component.</td></tr><tr><td><a href="#layout_stress">Stress-majorization layout (Kamada-Kawai energy)</a></td><td><code>layout_stress</code></td><td>2</td><td>Minimizes the stress \(\sigma\) (Kamada-Kawai energy) over all pairs by majorization or by direct minimization; the starting layout decides which local minimum is returned.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/networkit.html">NetworKit</a></th><th><a href="../../tools/graphlayouts.html">graphlayouts</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With fewer than three nodes the scaled stress is 0: one or two nodes can always be placed at the exact distance.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Pairs in different components have \(d_{ij}=\infty\) and \(w_{ij}=0\): they carry no term, so the stress is a sum over pairs inside components and does not constrain how components are placed relative to each other.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Edge weights are read as lengths, \(d_{ij}\) is the weighted shortest-path length and the weighted stress uses \(w_{ij}=d_{ij}^{-2}\) of those lengths.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

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

**Harness files:** [harness/manifest/layout.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/layout.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

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

**Harness files:** [harness/manifest/layout.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/layout.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

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
