---
title: "Graph complement"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Graph complement {#concept-top}

Family: [Data transforms](index.html). Subfamily: Graph operators. Concept id: `graph_complement`. 2 measures.

## Definition {#concept-definition}

Graph complement. Entries grouped here: Graph complement (graph\_complement); Graph complement (op\_complement).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Graph complement (graph\_complement)](#graph_complement) | `graph_complement` | 1 |
| [Graph complement (op\_complement)](#op_complement) | `op_complement` | 4 |

## Graph complement (graph\_complement) {#graph_complement}

Measure id: `graph_complement`. Original family: Data transforms.

Name: Graph complement.

**Definition.** Graph complement.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `ComplementGraphGenerator` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Graph complement (op\_complement) {#op_complement}

Measure id: `op_complement`. Original family: Data transforms.

Name: Graph complement.

**Definition.** Graph complement.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `complement` | API listing |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `complementer` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `complementer` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `complement; digraph_complement; graph_complement` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
