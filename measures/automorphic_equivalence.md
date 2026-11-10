---
title: "Automorphic equivalence"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Automorphic equivalence

Family: Roles and positions. Identifier: `automorphic_equivalence`.

## Definition

Orbits of the automorphism group of the binary ties: nodes that map to each other under some automorphism share a label.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../tools/ucinet.html) | · reported in docs | `orbits` | published documentation |
| [nauty](../tools/nauty.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `automorphic_equivalence` | nauty | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `pynauty.autgrp(Graph).orbits (nauty 2.8.8): orbit of the automorphism group` | nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented. |

## References

[mckay2014practical](../references.html#mckay2014practical)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [mckay2014practical](../references.html#mckay2014practical)
{% endraw %}
