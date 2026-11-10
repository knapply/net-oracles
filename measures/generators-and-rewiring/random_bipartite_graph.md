---
title: "Random bipartite graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random bipartite graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Classic random graphs. Concept id: `random_bipartite_graph`. 2 measures.

## Definition {#concept-definition}

Random bipartite graph. Entries grouped here: Correlated and bipartite random graph generators; Random bipartite graph generator.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Correlated and bipartite random graph generators](#gen_correlated_bipartite) | `gen_correlated_bipartite` | 1 |
| [Random bipartite graph generator](#gen_random_bipartite) | `gen_random_bipartite` | 4 |

## Correlated and bipartite random graph generators {#gen_correlated_bipartite}

Measure id: `gen_correlated_bipartite`. Original family: Generators and rewiring.

**Definition.** Correlated and bipartite random graph generators.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_correlated_bipartite-igraph) | `sample_bipartite_gnm; sample_bipartite_gnp; sample_correlated_gnp; sample_correlated_gnp_pair` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_correlated_bipartite-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: sample\_bipartite\_gnm; sample\_bipartite\_gnp; sample\_correlated\_gnp; sample\_correlated\_gnp\_pair.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Random bipartite graph generator {#gen_random_bipartite}

Measure id: `gen_random_bipartite`. Original family: Generators and rewiring.

**Definition.** Random bipartite graph generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_random_bipartite-igraph) | `bipartite_gnm; bipartite_gnp; sample_bipartite` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_random_bipartite-pyigraph) | `Random_Bipartite` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_random_bipartite-rustworkx) | `directed_random_bipartite_graph; undirected_random_bipartite_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_random_bipartite-jgrapht) | `GnmRandomBipartiteGraphGenerator; GnpRandomBipartiteGraphGenerator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_random_bipartite-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: bipartite\_gnm; bipartite\_gnp; sample\_bipartite.
- <a id="why-gen_random_bipartite-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Random\_Bipartite.
- <a id="why-gen_random_bipartite-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: directed\_random\_bipartite\_graph; undirected\_random\_bipartite\_graph.
- <a id="why-gen_random_bipartite-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GnmRandomBipartiteGraphGenerator; GnpRandomBipartiteGraphGenerator.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
