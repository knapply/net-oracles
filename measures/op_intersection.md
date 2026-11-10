---
title: "Op intersection"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Op intersection

Family: Data transforms. Identifier: `op_intersection`.

## Definition

Op intersection.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `intersection; intersection_all` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `intersection` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `intersection` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `graph_intersection` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `construct_intersection` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.intersection(G, H) edges` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool)
{% endraw %}
