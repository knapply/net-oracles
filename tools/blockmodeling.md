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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 1 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 1 |
| <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | 3 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Roles and positions | Blockmodels | [Block density](../measures/roles-and-positions/block_density.html) | [Block density](../measures/roles-and-positions/block_density.html#block_density) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Roles and positions | Blockmodels | [Blockmodel criterion function](../measures/roles-and-positions/blockmodel_criterion.html) | [Crit Fun C](../measures/roles-and-positions/blockmodel_criterion.html#cat_c_crit_fun) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `critFunC` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/roles-and-positions/blockmodel_criterion.html#why-cat_c_crit_fun-blockmodeling) |
| Roles and positions | Blockmodels | [Direct blockmodel search](../measures/roles-and-positions/blockmodel_search.html) | [Direct blockmodel search (structural, regular, generalised block types)](../measures/roles-and-positions/blockmodel_search.html#blockmodel_search) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `optParC; optRandomParC` | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](../measures/roles-and-positions/blockmodel_search.html#why-blockmodel_search-blockmodeling) |
| Roles and positions | Equivalence and clustering | [Regular equivalence (REGE, CATREGE)](../measures/roles-and-positions/regular_equivalence.html) | [Regular equivalence](../measures/roles-and-positions/regular_equivalence.html#regular_equivalence) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/roles-and-positions/regular_equivalence.html#why-regular_equivalence-blockmodeling) |
| Roles and positions | Equivalence and clustering | [Structural equivalence](../measures/roles-and-positions/structural_equivalence.html) | [Structural equivalence](../measures/roles-and-positions/structural_equivalence.html#structural_equivalence) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | `sedist` | Differs by convention (direction): On a symmetric matrix (every undirected fixture and complete5\_dir) blockmodeling::sedist agrees with the reference. [details](../measures/roles-and-positions/structural_equivalence.html#why-structural_equivalence-blockmodeling) |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F084](../findings.html#f084) | convention | Profiles keep the entries for the two nodes themselves on asymmetric matrices |
{% endraw %}
