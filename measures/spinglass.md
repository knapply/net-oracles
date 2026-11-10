---
title: "Spinglass"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Spinglass

Family: Communities. Identifier: `spinglass`.

## Definition

Spinglass communities of a connected network by simulated annealing of a Potts Hamiltonian (Reichardt and Bornholdt).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `cluster_spinglass` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_spinglass` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `spinglass_quality` | igraph (R) | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) edge\_case | defaults | abs 0.02, rel 0 | `mean over set.seed(1..10) of modularity(g, cluster_spinglass(g, weights = NA))` | both tools reject disconnected networks; igraph also rejects the trivial ones |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F038](../findings.html#f038) | igraph (R) | convention | Spinglass reads the network as simple |

## References

[reichardt2006statistical](../references.html#reichardt2006statistical), [traag2009community](../references.html#traag2009community)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
