---
title: "Ei index"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Ei index

Family: Mixing and assortativity. Identifier: `ei_index`.

## Definition

Ei index.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../tools/ucinet.html) | · reported in docs | `E-I index; EI` | published documentation |
| [egor](../tools/egor.html) | ≠ checked, differs by convention |  |  |
| [netseg](../tools/netseg.html) | · reported in docs | `ei` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ei_index_node` | egor | any | differs | directed, isolates, loops, multi\_edges | defaults, direction, multi\_edges, self\_loops, ties | abs 1e-15, rel 1e-14 | `egor::comp_ei(egor object, alt.attr = 'group', ego.attr = 'group')` | egor's comp\_ei() counts alters, each neighbour once whatever the number or direction of the ties to it, and no self-loop; the reference value's node E-I index counts ties (each edge, in either direction, separately, a self-loop as an internal tie), and an ego without alters has no value in egor where the reference reports undefined (-1). Undirected fixtures without parallel edges or loops agree. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F073](../findings.html#f073) | egor | convention | comp\_ei counts each neighbour once |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [tool_egor](../references.html#tool_egor), [tool_netseg](../references.html#tool_netseg)
{% endraw %}
