---
title: "Twomode / degree"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Twomode / degree

Family: Two-mode and bipartite. Identifier: `twomode:degree`.

## Definition

Twomode / degree.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `2-mode centrality` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_degree` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nx.bipartite.degree_centrality(G, first_mode_nodes)` | one-mode fixture (no node types) |
| `twomode_degree_raw` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `igraph::degree(simplify(g))` | one-mode fixture (no node types) |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
