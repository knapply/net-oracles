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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `cycle; sum` |  |

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_census_kcycle-sna) | `kcycle.census` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_census_kcycle-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: kcycle.census.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
