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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 2 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Graph theory and combinatorics | Isomorphism and subgraph matching | [Graph isomorphism](../measures/graph-theory-and-combinatorics/graph_isomorphism.html) | [Vf2pp](../measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Roles and positions | Equivalence and clustering | [Automorphic equivalence](../measures/roles-and-positions/automorphic_equivalence.html) | [Automorphic equivalence](../measures/roles-and-positions/automorphic_equivalence.html#automorphic_equivalence) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F071](../findings.html#f071) | limitation | Parallel edges are not representable |
{% endraw %}
