---
title: "Core subset"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Core subset

Family: Cohesion and subgroups. Identifier: `core_subset`.

## Definition

Core subset.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `core_corona_k1` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_corona(G, k = 1) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_corona_k2` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_corona(G, k = 2) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_crust` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_crust(G) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_crust_k1` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_crust(G, k = 1) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_k2` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_core(G, k = 2) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_shell` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_shell(G) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |
| `core_shell_k1` | NetworkX | any | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.k_shell(G, k = 1) on nx.Graph or nx.DiGraph without self-loops, its nodes sorted` | nx.core\_number rejects self-loops and multigraphs, so the oracle runs on the simple graph without loops; this reference counts each parallel edge and a loop in a node's degree, as igraph does. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
