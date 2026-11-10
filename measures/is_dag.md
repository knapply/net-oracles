---
title: "Is dag"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Is dag

Family: Traversal, trees and DAGs. Identifier: `is_dag`.

## Definition

Is dag.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `is_directed_acyclic_graph` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `is_acyclic; is_dag` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `is_acyclic; is_dag` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `is_DAG` | API listing |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees | `is_directed_acyclic_graph` |  |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `is_acyclic` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_is_dag` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_directed_acyclic_graph(M)` |  |
| `dag_is_dag` | rustworkx | any | no-value-on-some-inputs | (no value) undirected | direction | abs 0, rel 0 | `rx.is_directed_acyclic_graph(G)` | rx.is\_directed\_acyclic\_graph() accepts only a PyDiGraph. |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
