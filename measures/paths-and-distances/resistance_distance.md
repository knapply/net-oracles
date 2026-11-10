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

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Effective resistance](#cx_effective_resistance) | `cx_effective_resistance` | 1 |
| [Resistance](#cx_resistance) | `cx_resistance` | 2 |
| [Resistance-based and spectral edge/vertex scores](#resistance_based) | `resistance_based` | 1 |

## References {#concept-references}

[brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Effective resistance {#cx_effective_resistance}

Measure id: `cx_effective_resistance`. Original family: Descriptive statistics.

**Definition.** Effective graph resistance (Kirchhoff index): the sum of resistance distances over all node pairs (Ellens et al. 2011).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `effective_graph_resistance` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_effective_resistance` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.effective_graph_resistance(G)` |  |
| `cx_effective_resistance_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.effective_graph_resistance(G, weight = 'weight')` |  |

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Resistance {#cx_resistance}

Measure id: `cx_resistance`. Original family: Centrality.

**Definition.** Resistance distance between every pair of nodes, infinite across components (Klein and Randic 1993).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `resistance_distance` |  |
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_resistance` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected | defaults, normalization | abs 1e-14, rel 1e-12 | `nx.resistance_distance(G)` | NetworkX's resistance\_distance and kemeny\_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant. |
| `cx_resistance` | netrankr | undirected | differs | loops, multi\_edges, (no value) directed, (no value) disconnected | defaults, direction, multi\_edges, self\_loops, weights | abs 1e-14, rel 1e-12 | `indirect_relations(g, 'dist_resist')` | netrankr reads the network as undirected, unweighted and simple, so parallel edges count once and self-loops not at all; networks without them agree. netrankr reads the network as undirected, unweighted and simple and has no value for a single node; its resistance distance (type = "dist\_resist", "depend\_curflow") is defined only for connected graphs and raises an error otherwise. |
| `cx_resistance_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected | defaults, normalization | abs 1e-14, rel 1e-12 | `nx.resistance_distance(G, weight = 'weight', invert_weight = True)` | NetworkX's resistance\_distance and kemeny\_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant. |

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [schoch2018centrality](../../references.html#schoch2018centrality)

## Resistance-based and spectral edge/vertex scores {#resistance_based}

Measure id: `resistance_based`. Original family: Centrality.

**Definition.** Resistance-based and spectral edge/vertex scores.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-resistance_based-networkit) | `AlgebraicDistance; ApproxElectricalCloseness; ApproxSpanningEdge; CommuteTimeDistance; ForestCentrality; SpanningEdgeCentrality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-resistance_based-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AlgebraicDistance; ApproxElectricalCloseness; ApproxSpanningEdge; CommuteTimeDistance; ForestCentrality; SpanningEdgeCentrality.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
