---
title: "cdlib"
layout: default
parent: Tools
---

{% raw %}

# cdlib

| Field | Value |
|---|---|
| Identifier | `cdlib` |
| Language | Python |
| Version tested | 0.4.1 |
| License | BSD-2-Clause |
| Homepage | <https://cdlib.readthedocs.io> |
| Role | checked |
| Citation | [tool_cdlib](../references.html#tool_cdlib) |

## How it was run

Imported in CPython; evaluation functions called on communities.

## Coverage

| State | Measures |
|---|---|
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 2 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction, multi-edges and self-loops): cdlib's newman\_girvan\_modularity counts the parallel edges inside a community once while the edge total and the degrees count every copy (a triangle... [details](../measures/communities/modularity.html#why-modularity-cdlib) |
| Communities | Partition comparison and operations | [Compare partitions](../measures/communities/compare_partitions.html) | [Compare partitions](../measures/communities/compare_partitions.html#compare_partitions) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults): For partitions of one element cdlib (through scikit-learn) returns 1.0. [details](../measures/communities/compare_partitions.html#why-compare_partitions-cdlib) |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F037](../findings.html#f037) | convention | Adjusted Rand index is 1 on degenerate partitions |
{% endraw %}
