---
title: "Layered and tree layouts"
layout: default
parent: "Layout"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Layered and tree layouts {#concept-top}

Family: [Layout](index.html). Subfamily: Layout algorithms. Concept id: `layered_layout`. 5 measures.

## Definition {#concept-definition}

Layered and tree layouts. Entries grouped here: Barycenter Greedy Two Layered Bipartite Layout2 D; Layout tree unrooted; Median Greedy Two Layered Bipartite Layout2 D; Sugiyama layered layout; Two Layered Bipartite Layout2 D.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Barycenter Greedy Two Layered Bipartite Layout2 D](#cat_barycenter_bipartite_d_greedy_layered_layout2_two) | `cat_barycenter_bipartite_d_greedy_layered_layout2_two` | 1 |
| [Layout tree unrooted](#cat_layout_tree_unrooted) | `cat_layout_tree_unrooted` | 1 |
| [Median Greedy Two Layered Bipartite Layout2 D](#cat_bipartite_d_greedy_layered_layout2_median_two) | `cat_bipartite_d_greedy_layered_layout2_median_two` | 1 |
| [Sugiyama layered layout](#layout_sugiyama) | `layout_sugiyama` | 2 |
| [Two Layered Bipartite Layout2 D](#cat_bipartite_d_layered_layout2_two) | `cat_bipartite_d_layered_layout2_two` | 1 |

## Barycenter Greedy Two Layered Bipartite Layout2 D {#cat_barycenter_bipartite_d_greedy_layered_layout2_two}

Measure id: `cat_barycenter_bipartite_d_greedy_layered_layout2_two`. Original family: Layout.

**Definition.** Barycenter Greedy Two Layered Bipartite Layout2 D.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_barycenter_bipartite_d_greedy_layered_layout2_two-jgrapht) | `BarycenterGreedyTwoLayeredBipartiteLayout2D` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_barycenter_bipartite_d_greedy_layered_layout2_two-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BarycenterGreedyTwoLayeredBipartiteLayout2D.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Layout tree unrooted {#cat_layout_tree_unrooted}

Measure id: `cat_layout_tree_unrooted`. Original family: Layout.

**Definition.** Layout tree unrooted.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graphlayouts](../../tools/graphlayouts.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: graphlayouts is documented-only in this survey; listed in its documentation. [details](#why-cat_layout_tree_unrooted-graphlayouts) | `layout_tree_unrooted` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_layout_tree_unrooted-graphlayouts"></a>**[graphlayouts](../../tools/graphlayouts.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. graphlayouts (1.2.5) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: CRAN reference manual of graphlayouts 1.2.5: help topics.

**Tools cited:** [tool_graphlayouts](../../references.html#tool_graphlayouts)

## Median Greedy Two Layered Bipartite Layout2 D {#cat_bipartite_d_greedy_layered_layout2_median_two}

Measure id: `cat_bipartite_d_greedy_layered_layout2_median_two`. Original family: Layout.

**Definition.** Median Greedy Two Layered Bipartite Layout2 D.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_bipartite_d_greedy_layered_layout2_median_two-jgrapht) | `MedianGreedyTwoLayeredBipartiteLayout2D` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartite_d_greedy_layered_layout2_median_two-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: MedianGreedyTwoLayeredBipartiteLayout2D.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Sugiyama layered layout {#layout_sugiyama}

Measure id: `layout_sugiyama`. Original family: Layout.

**Definition.** Sugiyama layered layout.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-layout_sugiyama-igraph) | `layout_with_sugiyama` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-layout_sugiyama-pyigraph) | `layout_sugiyama` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-layout_sugiyama-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: layout\_with\_sugiyama.
- <a id="why-layout_sugiyama-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: layout\_sugiyama.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Two Layered Bipartite Layout2 D {#cat_bipartite_d_layered_layout2_two}

Measure id: `cat_bipartite_d_layered_layout2_two`. Original family: Layout.

**Definition.** Two Layered Bipartite Layout2 D.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_bipartite_d_layered_layout2_two-jgrapht) | `TwoLayeredBipartiteLayout2D` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bipartite_d_layered_layout2_two-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: TwoLayeredBipartiteLayout2D.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
