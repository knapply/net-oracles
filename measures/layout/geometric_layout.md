---
title: "Grid, random, circle and sphere layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Grid, random, circle and sphere layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `geometric_layout`. 4 measures.

## Definition {#concept-definition}

Grid, random, circle and sphere layouts. Entries grouped here: Circle, tree and two-mode (barycenter) layouts; Grid layout; Random layout; Sphere layout.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Circle, tree and two-mode (barycenter) layouts](#layout_simple) | `layout_simple` | 5 |
| [Grid layout](#layout_grid) | `layout_grid` | 1 |
| [Random layout](#layout_random) | `layout_random` | 3 |
| [Sphere layout](#layout_sphere) | `layout_sphere` | 1 |

## Circle, tree and two-mode (barycenter) layouts {#layout_simple}

Measure id: `layout_simple`. Original family: Layout.

**Definition.** Circle, tree and two-mode (barycenter) layouts.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs |  | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_as_bipartite; layout_as_star; layout_as_tree; layout_in_circle` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_reingold_tilford; layout_reingold_tilford_circular` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `bipartite_layout; circular_layout; digraph_bipartite_layout; digraph_circular_layout; digraph_shell_layout; digraph_spiral_layout; graph_bipartite_layout; graph_circular_layout; graph_shell_layout; graph_spiral_layout; shell_layout; spiral_layout` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `circle_layout` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Grid layout {#layout_grid}

Measure id: `layout_grid`. Original family: Layout.

**Definition.** Grid layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_on_grid` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Random layout {#layout_random}

Measure id: `layout_random`. Original family: Layout.

**Definition.** Random layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_randomly` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `digraph_random_layout; graph_random_layout; random_layout` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `random_graph_layout` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Sphere layout {#layout_sphere}

Measure id: `layout_sphere`. Original family: Layout.

**Definition.** Sphere layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_on_sphere` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
