---
title: "Implicit family"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Implicit family

Family: Graph theory and combinatorics. Identifier: `implicit_family`.

## Definition

Implicit family.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `implicit_circulant` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.circulant_graph(n, offsets)` |  |
| `implicit_complete_bipartite` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_bipartite_graph(a, b)` |  |
| `implicit_complete_bipartite_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_bipartite_graph(a, b), oriented from the first part` |  |
| `implicit_complete_multipartite` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.complete_multipartite_graph(*sizes)` |  |
| `implicit_de_bruijn` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `iterated nx.line_graph of the complete digraph with loops` |  |
| `implicit_hypercube` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.hypercube_graph(d), tuple read as an integer` |  |
| `implicit_kautz` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `iterated nx.line_graph of the complete digraph` |  |
| `implicit_path` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.path_graph(n)` |  |
| `implicit_path_dir` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.path_graph(n, create_using=nx.DiGraph)` |  |
| `implicit_star` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.star_graph(n)` |  |
| `implicit_wheel` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.wheel_graph(n)` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F034](../findings.html#f034) | NetworkX | convention | hypercube\_graph nodes are bit tuples; dimension 0 is the null graph |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
