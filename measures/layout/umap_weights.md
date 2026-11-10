---
title: "UMAP weights and layout"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# UMAP weights and layout {#concept-top}

Family: [Layout](index.html). Subfamily: Embeddings. Concept id: `umap_weights`. 2 measures.

## Definition {#concept-definition}

UMAP weights and layout. Entries grouped here: Layout umap; Umap compute weights.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Layout umap](#cat_layout_umap) | `cat_layout_umap` | 1 |
| [Umap compute weights](#cat_umap_weights) | `cat_umap_weights` | 1 |

## Layout umap {#cat_layout_umap}

Measure id: `cat_layout_umap`. Original family: Layout.

**Definition.** Layout umap.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-cat_layout_umap-graphlayouts) | `layout_umap` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_layout_umap-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Umap compute weights {#cat_umap_weights}

Measure id: `cat_umap_weights`. Original family: Graph theory and combinatorics.

**Definition.** Umap compute weights.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_umap_weights-pyigraph) | `umap_compute_weights` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_umap_weights-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: umap\_compute\_weights.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
