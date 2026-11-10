---
title: "Resistance distance and effective resistance"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Resistance distance and effective resistance {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Resistance and spectral distances. Concept id: `resistance_distance`. 3 measures.

## Definition {#concept-definition}

Resistance distance between every pair of nodes, infinite across components (Klein and Randic 1993).

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cx_effective_resistance">Effective resistance</a></td><td><code>cx_effective_resistance</code></td><td>1</td></tr><tr><td><a href="#cx_resistance">Resistance</a></td><td><code>cx_resistance</code></td><td>2</td></tr><tr><td><a href="#resistance_based">Resistance-based and spectral edge/vertex scores</a></td><td><code>resistance_based</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Effective resistance {#cx_effective_resistance}

Measure id: `cx_effective_resistance`. Original family: Descriptive statistics.

**Definition.** Effective graph resistance (Kirchhoff index): the sum of resistance distances over all node pairs (Ellens et al. 2011).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>effective_graph_resistance</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_effective_resistance</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.effective_graph_resistance(G)</code></td><td></td></tr><tr><td><code>cx_effective_resistance_weighted</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.effective_graph_resistance(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Resistance {#cx_resistance}

Measure id: `cx_resistance`. Original family: Centrality.

**Definition.** Resistance distance between every pair of nodes, infinite across components (Klein and Randic 1993).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>resistance_distance</code></td><td></td></tr><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_resistance</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.resistance_distance(G)</code></td><td>NetworkX's resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant.</td></tr><tr><td><code>cx_resistance</code></td><td>netrankr</td><td>undirected</td><td>differs</td><td>loops, multi_edges, (no value) directed, (no value) disconnected</td><td>defaults, direction, multi_edges, self_loops, weights</td><td>abs 1e-14, rel 1e-12</td><td><code>indirect_relations(g, 'dist_resist')</code></td><td>netrankr reads the network as undirected, unweighted and simple, so parallel edges count once and self-loops not at all; networks without them agree. netrankr reads the network as undirected, unweighted and simple and has no value for a single node; its resistance distance (type = "dist_resist", "depend_curflow") is defined only for connected graphs and raises an error otherwise.</td></tr><tr><td><code>cx_resistance_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.resistance_distance(G, weight = 'weight', invert_weight = True)</code></td><td>NetworkX's resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant.</td></tr></tbody></table></div>

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [schoch2018centrality](../../references.html#schoch2018centrality)

## Resistance-based and spectral edge/vertex scores {#resistance_based}

Measure id: `resistance_based`. Original family: Centrality.

**Definition.** Resistance-based and spectral edge/vertex scores.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-resistance_based-networkit">details</a></td><td><code>AlgebraicDistance; ApproxElectricalCloseness; ApproxSpanningEdge; CommuteTimeDistance; ForestCentrality; SpanningEdgeCentrality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-resistance_based-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AlgebraicDistance; ApproxElectricalCloseness; ApproxSpanningEdge; CommuteTimeDistance; ForestCentrality; SpanningEdgeCentrality.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
