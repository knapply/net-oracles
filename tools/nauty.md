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

| Family | Measure | State | API names |
|---|---|---|---|
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | ✓ checked, agrees |  |
| Roles and positions | [Automorphic equivalence](../measures/automorphic_equivalence.html) | ✓ checked, agrees |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F071](../findings.html#f071) | limitation | Parallel edges are not representable |
{% endraw %}
