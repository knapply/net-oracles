---
title: "BiRank"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# BiRank {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `birank`. 1 measure.

## Definition {#concept-definition}

BiRank scores of both node sets of a bipartite graph: the fixed point of damped, normalized propagation between the sets.

## References {#concept-references}

[he2017birank](../../references.html#he2017birank)

## Birank {#birank}

Measure id: `birank`. Original family: Two-mode and bipartite.

**Definition.** BiRank scores of both node sets of a bipartite graph: the fixed point of damped, normalized propagation between the sets.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `birank` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `birank` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.birank(G, top, max_iter = 1000, tol = 1e-10)` |  |

**References:** [he2017birank](../../references.html#he2017birank)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
