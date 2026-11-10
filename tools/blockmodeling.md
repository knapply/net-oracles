---
title: "blockmodeling"
layout: default
parent: Tools
---

{% raw %}
# blockmodeling

| Field | Value |
|---|---|
| Identifier | `blockmodeling` |
| Language | R |
| Version tested | 1.1.8 |
| License | see package DESCRIPTION |
| Homepage | <https://cran.r-project.org/package=blockmodeling> |
| Role | checked |
| Citation | [ziberna2007generalized](../references.html#ziberna2007generalized) |

## How it was run

Called from R on matrices.

Capabilities listed by introspection of R package blockmodeling: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 1 |
| checked, differs by convention (≠) | 1 |
| reported in docs (·) | 3 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Graph theory and combinatorics | [Crit Fun C](../measures/cat_c_crit_fun.html) | · reported in docs | `critFunC` |
| Roles and positions | [Block density](../measures/block_density.html) | ✓ checked, agrees |  |
| Roles and positions | [Direct blockmodel search (structural, regular, generalised block types)](../measures/blockmodel_search.html) | · reported in docs | `optParC; optRandomParC` |
| Roles and positions | [Regular equivalence](../measures/regular_equivalence.html) | · reported in docs | `REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow` |
| Roles and positions | [Structural equivalence](../measures/structural_equivalence.html) | ≠ checked, differs by convention | `sedist` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F084](../findings.html#f084) | convention | Profiles keep the entries for the two nodes themselves on asymmetric matrices |
{% endraw %}
