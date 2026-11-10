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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 1 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 2 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Roles and positions | Structural holes and brokerage | [Burt constraint](../measures/roles-and-positions/burt_constraint.html) | [Constraint](../measures/roles-and-positions/burt_constraint.html#constraint) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Roles and positions | Structural holes and brokerage | [Burt efficiency](../measures/roles-and-positions/burt_efficiency.html) | [Efficiency](../measures/roles-and-positions/burt_efficiency.html#efficiency) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... *(reason incomplete)* [details](../measures/roles-and-positions/burt_efficiency.html#why-efficiency-manynet) |
| Roles and positions | Structural holes and brokerage | [Effective size](../measures/roles-and-positions/effective_size.html) | [Effective size](../measures/roles-and-positions/effective_size.html#effective_size) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... *(reason incomplete)* [details](../measures/roles-and-positions/effective_size.html#why-effective_size-manynet) |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F082](../findings.html#f082) | defect | Effective size and efficiency differ on directed networks and multigraphs with loops |
| [F083](../findings.html#f083) | defect | hierarchy differs from the definition on all 25 fixtures |
{% endraw %}
