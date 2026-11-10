---
title: "Optimal modularity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Optimal modularity

Family: Communities. Identifier: `optimal_modularity`.

## Definition

A partition of maximum modularity found exactly by Russian doll search.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `cluster_optimal` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_optimal_modularity` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `optimal_modularity` | igraph (R) | any | no-value-on-some-inputs |  | direction | abs 1e-14, rel 1e-12 | `modularity(cluster_optimal(g, weights = NULL))` | the exact search is not run on these larger fixtures (see the note above), and GLPK would take too long on several of them |
| `optimal_modularity_weighted` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `modularity(cluster_optimal(g, weights = E(g)$weight))` | as for optimal\_modularity |

## References

[brandes2008modularity](../references.html#brandes2008modularity)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
