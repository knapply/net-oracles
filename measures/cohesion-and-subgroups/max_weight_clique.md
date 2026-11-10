---
title: "Maximum-weight clique"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Maximum-weight clique {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cliques. Concept id: `max_weight_clique`. 3 measures.

## Definition {#concept-definition}

Maximum-weight clique. Entries grouped here: Max weight clique; Largest weighted cliques; Max weight clique nodes.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Max weight clique](#max_weight_clique) | `max_weight_clique` | 1 |
| [Largest weighted cliques](#cat_clique_largest_weighted) | `cat_clique_largest_weighted` | 1 |
| [Max weight clique nodes](#max_weight_clique_nodes) | `max_weight_clique_nodes` | 1 |

## Max weight clique {#max_weight_clique}

Measure id: `max_weight_clique`. Original family: Cohesion and subgroups.

**Definition.** Max weight clique.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `max_weight_clique` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.max_weight_clique(G) with node attribute weight = (7 v mod 5) - 1: (weight, 1 if the nodes form a clique)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Largest weighted cliques {#cat_clique_largest_weighted}

Measure id: `cat_clique_largest_weighted`. Original family: Cohesion and subgroups.

**Definition.** Largest weighted cliques.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `largest_weighted_cliques` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Max weight clique nodes {#max_weight_clique_nodes}

Measure id: `max_weight_clique_nodes`. Original family: Cohesion and subgroups.

**Definition.** Max weight clique nodes.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `max_weight_clique_nodes` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.max_weight_clique(G)[0] (members in the order NetworkX's branch and bound adds them)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
