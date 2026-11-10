---
title: "Robins-Alexander clustering"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Robins-Alexander clustering {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `robins_alexander`. 1 measure.

## Definition {#concept-definition}

Robins-Alexander clustering. Entries grouped here: Robins alexander.

## Robins alexander {#robins_alexander}

Measure id: `robins_alexander`. Original family: Two-mode and bipartite.

**Definition.** Robins alexander.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `robins_alexander_clustering` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `robins_alexander` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.robins_alexander_clustering(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
