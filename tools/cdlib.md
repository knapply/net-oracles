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
| checked, differs by convention (≠) | 2 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | ≠ checked, differs by convention |  |
| Communities | Partition comparison and operations | [Compare partitions](../measures/communities/compare_partitions.html) | [Compare partitions](../measures/communities/compare_partitions.html#compare_partitions) | ≠ checked, differs by convention |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F037](../findings.html#f037) | convention | Adjusted Rand index is 1 on degenerate partitions |
{% endraw %}
