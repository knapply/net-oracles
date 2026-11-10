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

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Roles and positions | Blockmodels | [Block density](../measures/roles-and-positions/block_density.html) | [Block density](../measures/roles-and-positions/block_density.html#block_density) | ✓ checked, agrees |  |
| Roles and positions | Blockmodels | [Blockmodel criterion function](../measures/roles-and-positions/blockmodel_criterion.html) | [Crit Fun C](../measures/roles-and-positions/blockmodel_criterion.html#cat_c_crit_fun) | · reported in docs | `critFunC` |
| Roles and positions | Blockmodels | [Direct blockmodel search](../measures/roles-and-positions/blockmodel_search.html) | [Direct blockmodel search (structural, regular, generalised block types)](../measures/roles-and-positions/blockmodel_search.html#blockmodel_search) | · reported in docs | `optParC; optRandomParC` |
| Roles and positions | Equivalence and clustering | [Regular equivalence (REGE, CATREGE)](../measures/roles-and-positions/regular_equivalence.html) | [Regular equivalence](../measures/roles-and-positions/regular_equivalence.html#regular_equivalence) | · reported in docs | `REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow` |
| Roles and positions | Equivalence and clustering | [Structural equivalence](../measures/roles-and-positions/structural_equivalence.html) | [Structural equivalence](../measures/roles-and-positions/structural_equivalence.html#structural_equivalence) | ≠ checked, differs by convention | `sedist` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F084](../findings.html#f084) | convention | Profiles keep the entries for the two nodes themselves on asymmetric matrices |
{% endraw %}
