---
title: "Random walks"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random walks {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Traversal and orderings. Concept id: `random_walks`. 2 measures.

## Definition {#concept-definition}

Random walks. Entries grouped here: Random walk generation and sampling; Random walks.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Random walk generation and sampling](#random_walk_sampling) | `random_walk_sampling` | 2 |
| [Random walks](#random_walk) | `random_walk` | 4 |

## Random walk generation and sampling {#random_walk_sampling}

Measure id: `random_walk_sampling`. Original family: Traversal, trees and DAGs.

**Definition.** Random walk generation and sampling.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `RandomWalkVertexIterator` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `loop_erased_random_walk` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)

## Random walks {#random_walk}

Measure id: `random_walk`. Original family: Traversal, trees and DAGs.

**Definition.** Random walks.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `generate_random_paths; random_walk` | API listing |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `random_edge_walk; random_walk` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `random_walk` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `digraph_generate_random_path; generate_random_path; graph_generate_random_path` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
