---
title: "Maximal extendability"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximal extendability {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `matching_extendability`. 1 measure.

## Definition {#concept-definition}

Maximal extendability. Entries grouped here: Maximal extendability.

## Maximal extendability {#maximal_extendability}

Measure id: `maximal_extendability`. Original family: Two-mode and bipartite.

**Definition.** Maximal extendability.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `maximal_extendability` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `maximal_extendability` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.maximal_extendability(cover2(G)) (-1 where it raises)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
