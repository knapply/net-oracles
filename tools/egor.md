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

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Ego networks | Ego measures | [Ego composition and heterogeneity](../measures/ego-networks/ego_composition.html) | [Ego composition: alter shares, Blau and Shannon heterogeneity, IQV](../measures/ego-networks/ego_composition.html#ego_composition) | · reported in docs |  |
| Ego networks | Ego measures | [Ego network density](../measures/ego-networks/ego_density.html) | [Ego\_summary / density](../measures/ego-networks/ego_density.html#ego_summary-density) | ✓ checked, agrees |  |
| Mixing and assortativity | Segregation and homophily indices | [E-I index](../measures/mixing-and-assortativity/ei_index.html) | [Ei index](../measures/mixing-and-assortativity/ei_index.html#ei_index) | ≠ checked, differs by convention |  |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F073](../findings.html#f073) | convention | comp\_ei counts each neighbour once |
{% endraw %}
