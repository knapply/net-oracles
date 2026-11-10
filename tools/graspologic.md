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
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 2 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction, multi-edges, normalization, self-loops and weights): graspologic-native adds an undirected self-loop's weight once to the community's internal weight but twice to the node's degree (exact rational... [details](../measures/communities/modularity.html#why-modularity-graspologic) |
| Matrices and spectra | Graph matrices | [Laplacian matrix](../measures/matrices-and-spectra/laplacian_matrix.html) | [Gm laplacian](../measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (direction): For a directed graph graspologic's 'I-DAD' form is D\_in^-1/2 (D\_in - A) D\_in^-1/2 with in-degrees (graspologic/utils/utils.py, to\_laplacian), and a... [details](../measures/matrices-and-spectra/laplacian_matrix.html#why-gm_laplacian-graspologic) |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F072](../findings.html#f072) | convention | The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs |
{% endraw %}
