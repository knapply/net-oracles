---
title: "Structural equivalence"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Structural equivalence

Family: Roles and positions. Identifier: `structural_equivalence`.

## Definition

Pairwise structural equivalence of all nodes: Euclidean distance, correlation or Hamming distance between their tie profiles.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../tools/sna.html) | ✓ checked, agrees | `sedist` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `SE` | published documentation |
| [blockmodeling](../tools/blockmodeling.html) | ≠ checked, differs by convention | `sedist` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `structural_equivalence_correlation` | sna | any | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-12 | `sna::sedist(m, method = 'correlation')` | sna::sedist() fails on a network with one node. |
| `structural_equivalence_euclidean` | sna | any | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-12 | `sna::sedist(m, method = 'euclidean')` | sna::sedist() fails on a network with one node. |
| `structural_equivalence_euclidean` | blockmodeling | any | differs | directed | direction | abs 1e-12, rel 1e-12 | `blockmodeling::sedist(m, method = 'euclidean')` | On a symmetric matrix (every undirected fixture and complete5\_dir) blockmodeling::sedist agrees with the reference. On an asymmetric one it compares full row and column profiles including the entries for the two nodes themselves (k = i, j), where the reference, like sna::sedist, leaves them out; node 0 against node 1 on cycle7\_dir is 2 against sqrt(2), and on pair 0 against sqrt(2). The oracle script does not call blockmodeling on a network of one node: sedist compares pairs of nodes, and there is no pair. |
| `structural_equivalence_euclidean_weighted` | sna | any | agrees |  |  | abs 1e-12, rel 1e-12 | `sna::sedist(valued m, method = 'euclidean')` |  |
| `structural_equivalence_euclidean_weighted` | blockmodeling | any | differs | directed | direction | abs 1e-12, rel 1e-12 | `blockmodeling::sedist(W, method = 'euclidean')` | On a symmetric matrix (every undirected fixture and complete5\_dir) blockmodeling::sedist agrees with the reference. On an asymmetric one it compares full row and column profiles including the entries for the two nodes themselves (k = i, j), where the reference, like sna::sedist, leaves them out; node 0 against node 1 on cycle7\_dir is 2 against sqrt(2), and on pair 0 against sqrt(2). |
| `structural_equivalence_hamming` | sna | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `sna::sedist(m, method = 'hamming')` | sna::sedist() fails on a network with one node. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F084](../findings.html#f084) | blockmodeling | convention | Profiles keep the entries for the two nodes themselves on asymmetric matrices |

## References

[breiger1975algorithm](../references.html#breiger1975algorithm), [burt1976positions](../references.html#burt1976positions), [lorrain1971structural](../references.html#lorrain1971structural), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [ziberna2007generalized](../references.html#ziberna2007generalized)
{% endraw %}
