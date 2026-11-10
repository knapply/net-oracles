---
title: "Topological sort"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Topological sort {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `topological_sort`. 1 measure.

## Definition {#concept-definition}

Topological sort. Entries grouped here: Topological sort.

## Topological sort {#topological_sort}

Measure id: `topological_sort`. Original family: Traversal, trees and DAGs.

**Definition.** Topological sort.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `lexicographical_topological_sort; topological_generations; topological_sort` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `topo_sort` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `topological_sorting` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `topological_sort` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `lexicographical_topological_sort; topological_generations; topological_sort` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `topological_sort` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_topological_sort` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.topological_sort(D))` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
