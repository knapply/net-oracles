---
title: "Dispersion"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Dispersion

Family: Centrality. Identifier: `cx_dispersion`.

## Definition

Dispersion of the tie between each given pair of nodes (Backstrom and Kleinberg), one value per pair.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `dispersion` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_dispersion` | NetworkX | any | differs | directed, loops | direction, self\_loops, ties | abs 1e-12, rel 1e-09 | `nx.dispersion(G)[u][v] for every ordered pair of adjacent nodes` | On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. |
| `cx_dispersion_params` | NetworkX | any | differs | directed, loops | direction, self\_loops, ties | abs 1e-12, rel 1e-09 | `nx.dispersion(G, alpha = 2, b = 1, c = 0.5)` | On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. |
| `cx_dispersion_raw` | NetworkX | any | differs | directed, loops | direction, self\_loops, ties | abs 1e-12, rel 1e-09 | `nx.dispersion(G, normalized = False)` | On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. |

## References

[qi2012laplacian](../references.html#qi2012laplacian), [zhang2016identifying](../references.html#zhang2016identifying)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
