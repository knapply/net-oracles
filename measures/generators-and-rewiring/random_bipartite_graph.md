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

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `sample_bipartite_gnm; sample_bipartite_gnp; sample_correlated_gnp; sample_correlated_gnp_pair` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Random bipartite graph generator {#gen_random_bipartite}

Measure id: `gen_random_bipartite`. Original family: Generators and rewiring.

**Definition.** Random bipartite graph generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `bipartite_gnm; bipartite_gnp; sample_bipartite` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Random_Bipartite` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_random_bipartite_graph; undirected_random_bipartite_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GnmRandomBipartiteGraphGenerator; GnpRandomBipartiteGraphGenerator` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
