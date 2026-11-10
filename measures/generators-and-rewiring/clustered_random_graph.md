---
title: "Random clustered graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random clustered graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Classic random graphs. Concept id: `clustered_random_graph`. 2 measures.

## Definition {#concept-definition}

Random clustered graph. Entries grouped here: Clustering Generator; Random clustered graph.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Clustering Generator](#cat_clustering_generator) | `cat_clustering_generator` | 1 |
| [Random clustered graph](#cat_clustered_random) | `cat_clustered_random` | 1 |

## Clustering Generator {#cat_clustering_generator}

Measure id: `cat_clustering_generator`. Original family: Generators and rewiring.

**Definition.** Clustering Generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clustering_generator-networkit) | `ClusteringGenerator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clustering_generator-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ClusteringGenerator.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Random clustered graph {#cat_clustered_random}

Measure id: `cat_clustered_random`. Original family: Generators and rewiring.

**Definition.** Random clustered graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clustered_random-networkx) | `random_clustered_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clustered_random-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: random\_clustered\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
