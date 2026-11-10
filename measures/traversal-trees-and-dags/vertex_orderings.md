---
title: "Vertex orderings (max cardinality, degeneracy)"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Vertex orderings (max cardinality, degeneracy) {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Traversal and orderings. Concept id: `vertex_orderings`. 2 measures.

## Definition {#concept-definition}

Vertex orderings (max cardinality, degeneracy). Entries grouped here: Vertex orderings (max cardinality, degeneracy); Maximum cardinality search.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Vertex orderings (max cardinality, degeneracy)](#vertex_orderings) | `vertex_orderings` | 2 |
| [Maximum cardinality search](#cat_cardinality_maximum_search) | `cat_cardinality_maximum_search` | 1 |

## Vertex orderings (max cardinality, degeneracy) {#vertex_orderings}

Measure id: `vertex_orderings`. Original family: Traversal, trees and DAGs.

**Definition.** Vertex orderings (max cardinality, degeneracy).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `DegeneracyOrderingIterator; MaximumCardinalityIterator` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `maximum_adjacency_search` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)

## Maximum cardinality search {#cat_cardinality_maximum_search}

Measure id: `cat_cardinality_maximum_search`. Original family: Traversal, trees and DAGs.

**Definition.** Maximum cardinality search.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `maximum_cardinality_search` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
