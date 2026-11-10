---
title: "Assortativity degree"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Assortativity degree

Family: Mixing and assortativity. Identifier: `assortativity_degree`.

## Definition

Assortativity degree.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees |  |  |
| [BCT (Octave)](../tools/bct.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assortativity_degree` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-08 | `igraph::assortativity_degree(g, directed = TRUE)` |  |
| `assortativity_degree` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-08 | `python-igraph: [g.assortativity_degree(directed=True)]` |  |
| `assortativity_degree` | BCT (Octave) | any | differs |  | defaults, direction, multi\_edges, self\_loops, ties, weights | abs 1e-12, rel 1e-10 | `Brain Connectivity Toolbox 2019-03-03 in Octave: assortativity_bin(A, 0 \| 1), on the binary adjacency matrix without loops or parallel edges` | BCT returns NaN where the degree variance is zero (regular networks, a single node); the reference returns no value there, so both are undefined. On directed networks BCT's assortativity\_bin(A, 1) is close to but not equal to the Pearson correlation of out-degree at the source and in-degree at the target over the arcs (differences of 0.1% to 14% on the four directed random/weighted fixtures; cause not identified), and it cannot count loops or parallel edges. |
| `assortativity_degree_networkx` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(MultiGraph/MultiDiGraph)` |  |
| `assortativity_degree_undirected` | igraph (R) | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `igraph::assortativity_degree(g, directed = FALSE)` |  |
| `assortativity_degree_undirected` | igraph (Python) | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `python-igraph: [g.assortativity_degree(directed=False)]` |  |
| `assortativity_degree_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, weight = 'weight')` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F058](../findings.html#f058) | BCT (Octave) | convention | Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [rubinov2010complex](../references.html#rubinov2010complex)
{% endraw %}
