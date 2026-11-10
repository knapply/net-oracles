---
title: "Regular equivalence"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Regular equivalence

Family: Roles and positions. Identifier: `regular_equivalence`.

## Definition

Regular equivalence.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../tools/sna.html) | ✓ checked, agrees | `redist` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |
| [blockmodeling](../tools/blockmodeling.html) | · reported in docs | `REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `regular_equivalence` | sna | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `classes at distance 0 in sna::redist(m, method = 'catrege')` | sna fails on a network with a single node. |
| `regular_equivalence_seed` | sna | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `sna::redist(m, method = 'catrege', seed.partition = v %% 3), distance 0` | sna fails on a network with a single node. |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [ziberna2007generalized](../references.html#ziberna2007generalized)
{% endraw %}
