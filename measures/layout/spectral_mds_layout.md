---
title: "Spectral and MDS layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Spectral and MDS layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `spectral_mds_layout`. 2 measures.

## Definition {#concept-definition}

Spectral and MDS layouts. Entries grouped here: Layout spectral; Multidimensional scaling layout.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Layout spectral](#cat_layout_spectral) | `cat_layout_spectral` | 1 |
| [Multidimensional scaling layout](#layout_mds) | `layout_mds` | 2 |

## Layout spectral {#cat_layout_spectral}

Measure id: `cat_layout_spectral`. Original family: Layout.

**Definition.** Layout spectral.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | · reported in docs | `layout_spectral` | API listing |

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Multidimensional scaling layout {#layout_mds}

Measure id: `layout_mds`. Original family: Layout.

**Definition.** Multidimensional scaling layout.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `layout_with_mds` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `layout_mds` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
