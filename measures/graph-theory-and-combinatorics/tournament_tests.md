---
title: "Tournament tests"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Tournament tests {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `tournament_tests`. 1 measure.

## Definition {#concept-definition}

Tournament tests. Entries grouped here: Tournament.

## Tournament {#st_tournament}

Measure id: `st_tournament`. Original family: Graph theory and combinatorics.

**Definition.** Tournament.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `is_tournament` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_tournament` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[nx.tournament.is_tournament(G), nx.tournament.is_strongly_connected(G)] on the simple DiGraph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
