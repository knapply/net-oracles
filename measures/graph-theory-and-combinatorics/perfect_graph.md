---
title: "Perfect graphs"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Perfect graphs {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Chordal, perfect and special graph classes. Concept id: `perfect_graph`. 2 measures.

## Definition {#concept-definition}

Perfect graphs. Entries grouped here: Perfect-graph (Berge) tests; Perfect.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Perfect-graph (Berge) tests](#perfect_graph) | `perfect_graph` | 1 |
| [Perfect](#st_perfect) | `st_perfect` | 1 |

## Perfect-graph (Berge) tests {#perfect_graph}

Measure id: `perfect_graph`. Original family: Graph theory and combinatorics.

**Definition.** Perfect-graph (Berge) tests.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-perfect_graph-jgrapht) | `BergeGraphInspector` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-perfect_graph-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BergeGraphInspector.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Perfect {#st_perfect}

Measure id: `st_perfect`. Original family: Graph theory and combinatorics.

**Definition.** Perfect.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `is_perfect_graph` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_perfect` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.is_perfect_graph(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
