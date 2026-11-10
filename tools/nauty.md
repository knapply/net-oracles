---
title: "nauty"
layout: default
parent: Tools
---

{% raw %}
# nauty

| Field | Value |
|---|---|
| Identifier | `nauty` |
| Language | C (via pynauty) |
| Version tested | 2.8.8 (pynauty 2.8.8.1) |
| License | permissive (see the distribution COPYRIGHT file) |
| Homepage | <https://pallini.di.uniroma1.it/> |
| Role | checked |
| Citation | [mckay2014practical](../references.html#mckay2014practical) |

## How it was run

Called through pynauty on graph adjacency dictionaries.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 2 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Graph theory and combinatorics | Isomorphism and subgraph matching | [Graph isomorphism](../measures/graph-theory-and-combinatorics/graph_isomorphism.html) | [Vf2pp](../measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp) | ✓ checked, agrees |  |
| Roles and positions | Equivalence and clustering | [Automorphic equivalence](../measures/roles-and-positions/automorphic_equivalence.html) | [Automorphic equivalence](../measures/roles-and-positions/automorphic_equivalence.html#automorphic_equivalence) | ✓ checked, agrees |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F071](../findings.html#f071) | limitation | Parallel edges are not representable |
{% endraw %}
