---
title: "Leading eigen"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Leading eigen

Family: Communities. Identifier: `leading_eigen`.

## Definition

Leading eigenvector communities by repeated modularity-matrix splits (Newman); returns the membership, its modularity and the number of splits.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `cluster_leading_eigen` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_leading_eigenvector` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs | `NCD` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `leading_eigen` | igraph (R) | undirected | differs | disconnected, (no value) edge\_case, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_leading_eigen(g) with the weight attribute removed` | On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero components for isolated nodes), and the definition oracle declines; igraph's ARPACK vector and the reference value's then split differently. On the two sized power-law networks the modularities differ by 5e-7 (0.356872 against 0.356871): the division is decided by the signs of eigenvector entries, and the entries below the solvers' stopping tolerances are assigned differently (about one low-degree node). kite and two\_triangles\_isolate have a degenerate leading eigenvalue (see the definition oracle), so the division is not unique; igraph's ARPACK-based routine is not run on multigraphs, networks with self-loops, or trivial networks, where its conventions for loops and its convergence are not those documented here |
| `leading_eigen_membership` | igraph (R) | undirected | differs | disconnected, symmetric\_nodes, (no value) edge\_case, (no value) loops, (no value) multi\_edges | defaults, multi\_edges, self\_loops, ties | abs 0, rel 0 | `igraph::membership(cluster_leading_eigen(g)) with the weight attribute removed` | igraph puts each isolated node in a group of its own; the reference leaves isolated nodes, whose eigenvector components are zero, on the non-positive side of each division. Isolated nodes add nothing to modularity, so the modularity of the two partitions is the same (checked by leading\_eigen). With symmetric positions the leading eigenvector of a division can be repeated or have zero components, which the two place differently. as for leading\_eigen (the oracle script skips these fixtures; on other graphs the tag declarations apply) |
| `leading_eigen_weighted` | igraph (R) | undirected | differs | disconnected | defaults | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_leading_eigen(g, weights = E(g)$weight)` | On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero components for isolated nodes), and the definition oracle declines; igraph's ARPACK vector and the reference value's then split differently. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F011](../findings.html#f011) | igraph (R) | convention | Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance |

## References

[newman2006modularity](../references.html#newman2006modularity), [wu2000thick](../references.html#wu2000thick)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
