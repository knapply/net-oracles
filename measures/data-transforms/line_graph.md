---
title: "Line graph"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Line graph {#concept-top}

Family: [Data transforms](index.html). Subfamily: Graph operators. Concept id: `line_graph`. 1 measure.

## Definition {#concept-definition}

Line graph. Entries grouped here: Line graph.

## Line graph {#line_graph}

Measure id: `line_graph`. Original family: Data transforms.

**Definition.** Line graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `line_graph` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `line_graph; make_line_graph` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `linegraph` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `line_graph` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `graph_line_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `LineGraphConverter` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `construct_line_graph` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.line_graph(G) with each node (edge) replaced by its rank in the sorted edge list; edges sorted` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
