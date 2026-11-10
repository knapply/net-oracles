---
title: "Bipartite coloring and test"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bipartite coloring and test {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Coloring. Concept id: `bipartite_coloring`. 3 measures.

## Definition {#concept-definition}

Bipartite coloring and test. Entries grouped here: Bipartite; Bipartite color; Is bipartite node set (bipartite).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Bipartite](#cat_bipartite) | `cat_bipartite` | 2 |
| [Bipartite color](#bipartite_color) | `bipartite_color` | 7 |
| [Is bipartite node set (bipartite)](#cat_bipartite_is_set-bipartite) | `cat_bipartite_is_set@bipartite` | 1 |

## Bipartite {#cat_bipartite}

Measure id: `cat_bipartite`. Original family: Two-mode and bipartite.

**Definition.** Bipartite.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `bipartite` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `bipartite` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [siek2002boost](../../references.html#siek2002boost)

## Bipartite color {#bipartite_color}

Measure id: `bipartite_color`. Original family: Two-mode and bipartite.

**Definition.** Bipartite color.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `is_bipartite` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `bipartite_mapping; is_bipartite` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `is_bipartite` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `is_bipartite` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `digraph_is_bipartite; digraph_two_color; graph_is_bipartite; graph_two_color; is_bipartite; two_color` | API listing |
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `is_bipartite` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `is_bipartite` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `bipartite_color` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.bipartite.color(G) (-1 everywhere where it raises)` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Is bipartite node set (bipartite) {#cat_bipartite_is_set-bipartite}

Measure id: `cat_bipartite_is_set@bipartite`. Original family: Two-mode and bipartite.

**Definition.** Is bipartite node set (bipartite).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `is_bipartite_node_set` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
