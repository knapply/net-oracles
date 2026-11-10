---
title: "N-clans"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# N-clans {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `n_clans`. 1 measure.

## Definition {#concept-definition}

n-clans: the n-cliques whose induced subgraph also has diameter at most n.

## References {#concept-references}

[alba1973graph](../../references.html#alba1973graph), [luce1950connectivity](../../references.html#luce1950connectivity), [mokken1979cliques](../../references.html#mokken1979cliques)

## N clans {#n_clans}

Measure id: `n_clans`. Original family: Cohesion and subgroups.

**Definition.** n-clans: the n-cliques whose induced subgraph also has diameter at most n.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-n_clans-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-n_clans-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `n_clans_2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `2-cliques whose induced subgraph is connected with nx.diameter <= 2` |  |

**References:** [alba1973graph](../../references.html#alba1973graph), [luce1950connectivity](../../references.html#luce1950connectivity), [mokken1979cliques](../../references.html#mokken1979cliques)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
