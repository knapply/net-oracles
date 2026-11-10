---
title: "Min basis weights"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Min basis weights

Family: Graph theory and combinatorics. Identifier: `min_basis_weights`.

## Definition

A minimum cycle basis of an undirected network and the weight of each cycle (de Pina).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_min_basis_weights` | NetworkX | undirected | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `weights of the cycles of nx.minimum_cycle_basis(G)` | as for cyc\_basis |
| `cyc_min_basis_weights_weighted` | NetworkX | undirected | differs | multi\_edges | multi\_edges, self\_loops, weights | abs 1e-12, rel 1e-12 | `weights of the cycles of nx.minimum_cycle_basis(G, weight = 'weight')` | Two parallel edges form a cycle of their total weight for the reference and the definition (two parallel loops, two cycles); NetworkX's simple graph keeps one edge per pair and has no such cycle. |

## References

[depina1995applications](../references.html#depina1995applications), [dias2013efficient](../references.html#dias2013efficient), [gupta2021finding](../references.html#gupta2021finding), [hagberg2008exploring](../references.html#hagberg2008exploring), [itai1978finding](../references.html#itai1978finding), [johnson1975finding](../references.html#johnson1975finding), [kavitha2009cycle](../references.html#kavitha2009cycle), [kirchhoff1847ueber](../references.html#kirchhoff1847ueber)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
