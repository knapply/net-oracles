---
title: "Op union"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Op union

Family: Data transforms. Identifier: `op_union`.

## Definition

Op union.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `disjoint_union; disjoint_union_all; union; union_all` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `disjoint_union; union` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `disjoint_union; union` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `graph_union` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_union; graph_union; union` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `construct_union` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.compose(G, H) edges` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
