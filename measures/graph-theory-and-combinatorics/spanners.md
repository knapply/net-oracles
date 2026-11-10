---
title: "Spanners"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spanners {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `spanners`. 2 measures.

## Definition {#concept-definition}

Spanners. Entries grouped here: Greedy Multiplicative Spanner; Spanner ok.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Greedy Multiplicative Spanner](#cat_greedy_multiplicative_spanner) | `cat_greedy_multiplicative_spanner` | 1 |
| [Spanner ok](#gb_spanner_ok) | `gb_spanner_ok` | 1 |

## Greedy Multiplicative Spanner {#cat_greedy_multiplicative_spanner}

Measure id: `cat_greedy_multiplicative_spanner`. Original family: Graph theory and combinatorics.

**Definition.** Greedy Multiplicative Spanner.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_greedy_multiplicative_spanner-jgrapht) | `GreedyMultiplicativeSpanner` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_greedy_multiplicative_spanner-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GreedyMultiplicativeSpanner.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Spanner ok {#gb_spanner_ok}

Measure id: `gb_spanner_ok`. Original family: Traversal, trees and DAGs.

**Definition.** Spanner ok.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `spanner` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_spanner_ok` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `stretch check of nx.spanner(nx.Graph(M), 3, seed=1)` | NetworkX's spanner rejects multigraphs. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
