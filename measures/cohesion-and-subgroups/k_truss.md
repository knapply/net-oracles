---
title: "K-truss"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-truss {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cores, trusses and cohesive blocks. Concept id: `k_truss`. 2 measures.

## Definition {#concept-definition}

The k-truss: the edges in at least k - 2 triangles of the subgraph, and the nodes they touch.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [K truss](#k_truss) | `k_truss` | 1 |
| [Truss](#truss) | `truss` | 1 |

## References {#concept-references}

[batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

## K truss {#k_truss}

Measure id: `k_truss`. Original family: Cohesion and subgroups.

**Definition.** The k-truss: the edges in at least k - 2 triangles of the subgraph, and the nodes they touch.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `k_truss` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `k_truss_3_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.k_truss(G, 3), G the simple undirected graph without loops: the fixture edges whose pair it keeps` |  |
| `k_truss_3_nodes` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.k_truss(G, 3), G the simple undirected graph without loops: its nodes` |  |
| `k_truss_4_edges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.k_truss(G, 4), G the simple undirected graph without loops: the fixture edges whose pair it keeps` |  |
| `k_truss_4_nodes` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.k_truss(G, 4), G the simple undirected graph without loops: its nodes` |  |

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Truss {#truss}

Measure id: `truss`. Original family: Cohesion and subgroups.

**Definition.** Truss number of every edge: the largest k whose k-truss contains it.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `truss_numbers` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the largest k with the edge in nx.k_truss(G, k), G the simple undirected graph without loops (0 for loops)` |  |

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
