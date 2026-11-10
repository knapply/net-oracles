---
title: "Graph intersection"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph intersection {#concept-top}

Family: [Data transforms](index.html). Subfamily: Graph operators. Concept id: `graph_intersection`. 1 measure.

## Definition {#concept-definition}

Graph intersection. Entries grouped here: Op intersection.

## Op intersection {#op_intersection}

Measure id: `op_intersection`. Original family: Data transforms.

**Definition.** Op intersection.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `intersection; intersection_all` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `intersection` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `intersection` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `graph_intersection` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `construct_intersection` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.intersection(G, H) edges` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
