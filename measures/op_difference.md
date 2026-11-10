---
title: "Op difference"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Op difference

Family: Data transforms. Identifier: `op_difference`.

## Definition

Op difference.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `difference; symmetric_difference` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `difference` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `difference` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `graph_difference` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `GraphDifference` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `construct_difference` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.difference(G, H) edges` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
