---
title: "Maximal independent set"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximal independent set {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `independent_set`. 3 measures.

## Definition {#concept-definition}

A random maximal independent set containing the start nodes (or one random node), nodes in increasing order.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Is independent vertex set](#cat_independent_is_set) | `cat_independent_is_set` | 1 |
| [Is ivs](#cat_is_ivs) | `cat_is_ivs` | 1 |
| [Mis](#mis) | `mis` | 4 |

## References {#concept-references}

[brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [matula1983smallest](../../references.html#matula1983smallest), [schank2005approximating](../../references.html#schank2005approximating), [welsh1967upper](../../references.html#welsh1967upper)

## Is independent vertex set {#cat_independent_is_set}

Measure id: `cat_independent_is_set`. Original family: Graph theory and combinatorics.

**Definition.** Is independent vertex set.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `is_independent_vertex_set` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Is ivs {#cat_is_ivs}

Measure id: `cat_is_ivs`. Original family: Graph theory and combinatorics.

**Definition.** Is ivs.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `is_ivs` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Mis {#mis}

Measure id: `mis`. Original family: Graph theory and combinatorics.

**Definition.** A random maximal independent set containing the start nodes (or one random node), nodes in increasing order.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `maximal_independent_set; maximum_independent_set` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `independence_number; ivs; largest_ivs; max_ivs; maximal_ivs` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `independent_vertex_sets; largest_independent_vertex_sets; maximal_independent_vertex_sets` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `max_independent_vertex_set` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `mis_check` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `1, 1, 1 for nx.maximal_independent_set(G, [start], seed = 11), checked the same way` |  |

**References:** [brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [matula1983smallest](../../references.html#matula1983smallest), [schank2005approximating](../../references.html#schank2005approximating), [welsh1967upper](../../references.html#welsh1967upper)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
