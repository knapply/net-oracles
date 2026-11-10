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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vertex_orderings-jgrapht) | `DegeneracyOrderingIterator; MaximumCardinalityIterator` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-vertex_orderings-boost) | `maximum_adjacency_search` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-vertex_orderings-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: DegeneracyOrderingIterator; MaximumCardinalityIterator.
- <a id="why-vertex_orderings-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: maximum\_adjacency\_search.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)

## Maximum cardinality search {#cat_cardinality_maximum_search}

Measure id: `cat_cardinality_maximum_search`. Original family: Traversal, trees and DAGs.

**Definition.** Maximum cardinality search.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_cardinality_maximum_search-pyigraph) | `maximum_cardinality_search` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_cardinality_maximum_search-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: maximum\_cardinality\_search.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
