---
title: "manynet"
layout: default
parent: Tools
---

{% raw %}

# manynet

| Field | Value |
|---|---|
| Identifier | `manynet` |
| Language | R |
| Version tested | 2.4.0 |
| License | MIT |
| Homepage | <https://cran.r-project.org/package=manynet> |
| Role | checked |
| Citation | [tool_manynet](../references.html#tool_manynet) |

## How it was run

Called from R on igraph objects.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 1 |
| checked, differs by convention (≠) | 2 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Roles and positions | Structural holes and brokerage | [Burt constraint](../measures/roles-and-positions/burt_constraint.html) | [Constraint](../measures/roles-and-positions/burt_constraint.html#constraint) | ✓ checked, agrees |  |
| Roles and positions | Structural holes and brokerage | [Burt efficiency](../measures/roles-and-positions/burt_efficiency.html) | [Efficiency](../measures/roles-and-positions/burt_efficiency.html#efficiency) | ≠ checked, differs by convention |  |
| Roles and positions | Structural holes and brokerage | [Effective size](../measures/roles-and-positions/effective_size.html) | [Effective size](../measures/roles-and-positions/effective_size.html#effective_size) | ≠ checked, differs by convention |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F082](../findings.html#f082) | defect | Effective size and efficiency differ on directed networks and multigraphs with loops |
| [F083](../findings.html#f083) | defect | hierarchy differs from the definition on all 25 fixtures |
{% endraw %}
