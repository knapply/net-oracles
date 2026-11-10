---
title: "Kemeny constant"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Kemeny constant {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Resistance and spectral distances. Concept id: `kemeny_constant`. 1 measure.

## Definition {#concept-definition}

Kemeny's constant of the random walk: the expected steps to reach a stationary-distributed node, the same from every start.

## References {#concept-references}

[brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Kemeny {#cx_kemeny}

Measure id: `cx_kemeny`. Original family: Descriptive statistics.

**Definition.** Kemeny's constant of the random walk: the expected steps to reach a stationary-distributed node, the same from every start.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `kemeny_constant` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_kemeny` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected | defaults, normalization | abs 1e-14, rel 1e-12 | `nx.kemeny_constant(G)` | NetworkX's resistance\_distance and kemeny\_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant. |
| `cx_kemeny_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected | defaults, normalization | abs 1e-14, rel 1e-12 | `nx.kemeny_constant(G, weight = 'weight')` | NetworkX's resistance\_distance and kemeny\_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant. |

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
