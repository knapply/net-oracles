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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 1 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 1 |
| <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | 1 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Ego networks | Ego measures | [Ego composition and heterogeneity](../measures/ego-networks/ego_composition.html) | [Ego composition: alter shares, Blau and Shannon heterogeneity, IQV](../measures/ego-networks/ego_composition.html#ego_composition) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> |  | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](../measures/ego-networks/ego_composition.html#why-ego_composition-egor) |
| Ego networks | Ego measures | [Ego network density](../measures/ego-networks/ego_density.html) | [Ego\_summary / density](../measures/ego-networks/ego_density.html#ego_summary-density) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Mixing and assortativity | Segregation and homophily indices | [E-I index](../measures/mixing-and-assortativity/ei_index.html) | [Ei index](../measures/mixing-and-assortativity/ei_index.html#ei_index) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults, direction, multi-edges, self-loops and ties): egor's comp\_ei() counts alters, each neighbour once whatever the number or direction of the ties to it, and no self-loop. [details](../measures/mixing-and-assortativity/ei_index.html#why-ei_index-egor) |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F073](../findings.html#f073) | convention | comp\_ei counts each neighbour once |
{% endraw %}
