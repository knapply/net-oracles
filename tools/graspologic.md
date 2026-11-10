---
title: "graspologic"
layout: default
parent: Tools
---

{% raw %}
# graspologic

| Field | Value |
|---|---|
| Identifier | `graspologic` |
| Language | Python |
| Version tested | 3.4.4 |
| License | MIT |
| Homepage | <https://graspologic-org.github.io/graspologic/> |
| Role | checked |
| Citation | [tool_graspologic](../references.html#tool_graspologic) |

## How it was run

Imported in CPython; functions called on NumPy matrices.

## Coverage

| State | Measures |
|---|---|
| checked, differs by convention (≠) | 2 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | ≠ checked, differs by convention |  |
| Matrices and spectra | Graph matrices | [Laplacian matrix](../measures/matrices-and-spectra/laplacian_matrix.html) | [Gm laplacian](../measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian) | ≠ checked, differs by convention |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F072](../findings.html#f072) | convention | The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs |
{% endraw %}
