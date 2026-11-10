---
title: "Twomode / density"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Twomode / density

Family: Two-mode and bipartite. Identifier: `twomode:density`.

## Definition

Twomode / density.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `2-mode eigenvector, SVD, matching 2-mode, bipartite/density` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_density` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nx.bipartite.density(G, first_mode_nodes)` | one-mode fixture (no node types) |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
