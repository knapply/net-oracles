---
title: "Idom"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Idom

Family: Traversal, trees and DAGs. Identifier: `idom`.

## Definition

Immediate dominator of every node reachable from the start node (the start's is itself); unreachable nodes get the none mark u32::MAX.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `dominance_frontiers; immediate_dominators` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `dominator_tree` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `dominator_tree` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `dominance_frontiers; immediate_dominators` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `lengauer_tarjan_dominator_tree` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_immediate_dominators` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.immediate_dominators(G, 0), with 0 for the start and -1 for unreachable nodes` |  |

## References

[cooper2001simple](../references.html#cooper2001simple)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
