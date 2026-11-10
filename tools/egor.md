---
title: "egor"
layout: default
parent: Tools
---

{% raw %}
# egor

| Field | Value |
|---|---|
| Identifier | `egor` |
| Language | R |
| Version tested | 1.25.10 |
| License | AGPL-3.0 |
| Homepage | <https://cran.r-project.org/package=egor> |
| Role | checked |
| Citation | [tool_egor](../references.html#tool_egor) |

## How it was run

Called from R on ego-centred data objects.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 1 |
| checked, differs by convention (≠) | 1 |
| reported in docs (·) | 1 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Ego networks | [Ego composition: alter shares, Blau and Shannon heterogeneity, IQV](../measures/ego_composition.html) | · reported in docs |  |
| Mixing and assortativity | [Ei index](../measures/ei_index.html) | ≠ checked, differs by convention |  |
| Two-mode and bipartite | [Ego\_summary / density](../measures/ego_summary-density.html) | ✓ checked, agrees |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F073](../findings.html#f073) | convention | comp\_ei counts each neighbour once |
{% endraw %}
