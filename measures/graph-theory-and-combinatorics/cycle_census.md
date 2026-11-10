---
title: "Cycle census and count"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Cycle census and count {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `cycle_census`. 2 measures.

## Definition {#concept-definition}

Cycle census and count. Entries grouped here: Cycle count; Kcycle census.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Cycle count](#gb_cycle_count) | `gb_cycle_count` | 2 |
| [Kcycle census](#cat_census_kcycle) | `cat_census_kcycle` | 1 |

## Cycle count {#gb_cycle_count}

Measure id: `gb_cycle_count`. Original family: Traversal, trees and DAGs.

**Definition.** Cycle count.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [ergm (statnet)](../../tools/ergm.html) | ✓ checked, agrees | `cycle; sum` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_cycle_count` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(list(nx.simple_cycles(M)))` |  |
| `gb_cycle_count` | ergm (statnet) | any | agrees |  |  | abs 0, rel 0 | `sum(summary(nw ~ cycle(2:n))) directed, cycle(3:n) undirected` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm)

## Kcycle census {#cat_census_kcycle}

Measure id: `cat_census_kcycle`. Original family: Graph theory and combinatorics.

**Definition.** Kcycle census.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../../tools/sna.html) | · reported in docs | `kcycle.census` | API listing |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
