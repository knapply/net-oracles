---
title: "Kuratowski subgraph and counterexample"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Kuratowski subgraph and counterexample {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Planarity. Concept id: `kuratowski_subgraph`. 2 measures.

## Definition {#concept-definition}

Kuratowski subgraph and counterexample. Entries grouped here: Counterexample; Kuratowski.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Counterexample](#st_counterexample) | `st_counterexample` | 1 |
| [Kuratowski](#st_kuratowski) | `st_kuratowski` | 1 |

## Counterexample {#st_counterexample}

Measure id: `st_counterexample`. Original family: Graph theory and combinatorics.

**Definition.** Counterexample.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_counterexample` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted edges of nx.get_counterexample(G), or [-1] if planar` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Kuratowski {#st_kuratowski}

Measure id: `st_kuratowski`. Original family: Graph theory and combinatorics.

**Definition.** Kuratowski.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_kuratowski` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `1 if nx.get_counterexample(G) smooths to K5 or K3,3, -1 if planar` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
