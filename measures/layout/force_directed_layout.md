---
title: "Force-directed layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Force-directed layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `force_directed_layout`. 10 measures.

## Definition {#concept-definition}

Force-directed layouts. Entries grouped here: Davidson-Harel layout; DrL (OpenOrd) layout; Fruchterman-Reingold layout; GEM layout; Graphopt layout; Gursoy atun layout; and 4 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Davidson-Harel layout](#layout_dh) | `layout_dh` | 2 |
| [DrL (OpenOrd) layout](#layout_drl) | `layout_drl` | 2 |
| [Fruchterman-Reingold layout](#layout_fruchterman_reingold) | `layout_fruchterman_reingold` | 6 |
| [GEM layout](#layout_gem) | `layout_gem` | 1 |
| [Graphopt layout](#layout_graphopt) | `layout_graphopt` | 2 |
| [Gursoy atun layout](#cat_atun_gursoy_layout) | `cat_atun_gursoy_layout` | 1 |
| [Kamada-Kawai layout](#layout_kamada_kawai) | `layout_kamada_kawai` | 4 |
| [Large graph layout (LGL)](#layout_lgl) | `layout_lgl` | 2 |
| [Layout multilevel](#cat_layout_multilevel) | `cat_layout_multilevel` | 1 |
| [Spring](#cat_spring) | `cat_spring` | 1 |

## Davidson-Harel layout {#layout_dh}

Measure id: `layout_dh`. Original family: Layout.

**Definition.** Davidson-Harel layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_with_dh` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_davidson_harel` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## DrL (OpenOrd) layout {#layout_drl}

Measure id: `layout_drl`. Original family: Layout.

**Definition.** DrL (OpenOrd) layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_with_drl` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_drl` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Fruchterman-Reingold layout {#layout_fruchterman_reingold}

Measure id: `layout_fruchterman_reingold`. Original family: Layout.

**Definition.** Fruchterman-Reingold layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs |  | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_nicely; layout_with_fr` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_fruchterman_reingold; layout_fruchterman_reingold_3d` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `digraph_spring_layout; graph_spring_layout; spring_layout` | API listing |
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `ForceAtlas` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `fruchterman_reingold_force_directed_layout` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## GEM layout {#layout_gem}

Measure id: `layout_gem`. Original family: Layout.

**Definition.** GEM layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_with_gem` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Graphopt layout {#layout_graphopt}

Measure id: `layout_graphopt`. Original family: Layout.

**Definition.** Graphopt layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_with_graphopt` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_graphopt` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Gursoy atun layout {#cat_atun_gursoy_layout}

Measure id: `cat_atun_gursoy_layout`. Original family: Layout.

**Definition.** Gursoy atun layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `gursoy_atun_layout` | API listing |

**Tools cited:** [siek2002boost](../../references.html#siek2002boost)

## Kamada-Kawai layout {#layout_kamada_kawai}

Measure id: `layout_kamada_kawai`. Original family: Layout.

**Definition.** Kamada-Kawai layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_with_kk` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_kamada_kawai; layout_kamada_kawai_3d` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `digraph_kamada_kawai_layout; graph_kamada_kawai_layout; kamada_kawai_layout` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `kamada_kawai_spring_layout` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Large graph layout (LGL) {#layout_lgl}

Measure id: `layout_lgl`. Original family: Layout.

**Definition.** Large graph layout (LGL).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_with_lgl` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_lgl` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Layout multilevel {#cat_layout_multilevel}

Measure id: `cat_layout_multilevel`. Original family: Layout.

**Definition.** Layout multilevel.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | · reported in docs | `layout_multilevel` | API listing |

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Spring {#cat_spring}

Measure id: `cat_spring`. Original family: Layout.

**Definition.** Spring.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `Spring` | API listing |

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
