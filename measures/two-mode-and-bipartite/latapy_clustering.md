---
title: "Latapy clustering"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Latapy clustering {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `latapy_clustering`. 1 measure.

## Definition {#concept-definition}

Latapy clustering. Entries grouped here: Latapy clustering.

## Latapy clustering {#latapy_clustering}

Measure id: `latapy_clustering`. Original family: Two-mode and bipartite.

**Definition.** Latapy clustering.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `latapy_clustering` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `latapy_clustering_dot` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.latapy_clustering(G, mode = 'dot')` |  |
| `latapy_clustering_max` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.latapy_clustering(G, mode = 'max')` |  |
| `latapy_clustering_min` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.latapy_clustering(G, mode = 'min')` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
