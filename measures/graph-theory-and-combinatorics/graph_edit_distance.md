---
title: "Graph edit distance"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph edit distance {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `graph_edit_distance`. 2 measures.

## Definition {#concept-definition}

Graph edit distance. Entries grouped here: Ged Walk; Graph edit distance.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Ged Walk](#cat_ged_walk) | `cat_ged_walk` | 1 |
| [Graph edit distance](#ged) | `ged` | 2 |

## Ged Walk {#cat_ged_walk}

Measure id: `cat_ged_walk`. Original family: Paths and distances.

**Definition.** Ged Walk.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_ged_walk-networkit) | `GedWalk` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_ged_walk-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: GedWalk.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Graph edit distance {#ged}

Measure id: `ged`. Original family: Graph theory and combinatorics.

**Definition.** Graph edit distance.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `graph_edit_distance; optimal_edit_paths; optimize_edit_paths; optimize_graph_edit_distance` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-ged-jgrapht) | `ZhangShashaTreeEditDistance` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ged-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ZhangShashaTreeEditDistance.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ged` | NetworkX | any | differs | loops | self\_loops | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2) with G2 = ged_pair(fixture)` | NetworkX's graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes |
| `ged_labels` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2, node_match = equal labels, edge_match = equal labels) with G2 = ged_pair(fixture)` | exact edit distance is exponential; networks of at most 10 nodes |
| `ged_node_labels` | NetworkX | any | differs | loops | self\_loops | abs 0, rel 0 | `nx.graph_edit_distance(G1, G2, node_match = equal labels) with G2 = ged_pair(fixture)` | NetworkX's graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost when the loop's node is mapped onto one endpoint ((1, 1) against (0, 1), edit distance 0); the reference and the definition count deleting the loop and inserting the edge (2). exact edit distance is exponential; networks of at most 10 nodes |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F003](../../findings.html#f003) | NetworkX | defect | graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
