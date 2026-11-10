---
title: "Lambda sets"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lambda sets {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `lambda_sets`. 1 measure.

## Definition {#concept-definition}

Gusfield's equivalent flow tree: each node's parent and the edge connectivity to it (n - 1 maximum flows).

## References {#concept-references}

[borgatti1990ls](../../references.html#borgatti1990ls), [edmonds1972theoretical](../../references.html#edmonds1972theoretical), [ford1956maximal](../../references.html#ford1956maximal), [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very)

## Lambda sets {#lambda_sets}

Measure id: `lambda_sets`. Original family: Cohesion and subgroups.

**Definition.** Gusfield's equivalent flow tree: each node's parent and the edge connectivity to it (n - 1 maximum flows).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-lambda_sets-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-lambda_sets-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `lambda_sets` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `classes of nx.edge_connectivity >= k with at least two members, for every k >= 1` |  |

**References:** [borgatti1990ls](../../references.html#borgatti1990ls), [edmonds1972theoretical](../../references.html#edmonds1972theoretical), [ford1956maximal](../../references.html#ford1956maximal), [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
