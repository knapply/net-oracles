---
title: "All cliques (not only maximal)"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# All cliques (not only maximal) {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cliques. Concept id: `all_cliques`. 2 measures.

## Definition {#concept-definition}

All cliques (not only maximal). Entries grouped here: All cliques; Nx cliques order.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [All cliques](#all_cliques) | `all_cliques` | 1 |
| [Nx cliques order](#nx_cliques_order) | `nx_cliques_order` | 1 |

## All cliques {#all_cliques}

Measure id: `all_cliques`. Original family: Cohesion and subgroups.

**Definition.** All cliques.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `all_cliques` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `list(nx.enumerate_all_cliques(G))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nx cliques order {#nx_cliques_order}

Measure id: `nx_cliques_order`. Original family: Cohesion and subgroups.

**Definition.** Nx cliques order.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_cliques_order` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `list(nx.find_cliques(G)) then list(nx.find_cliques_recursive(G)), each clique in order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
