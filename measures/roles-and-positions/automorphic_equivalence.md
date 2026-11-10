---
title: "Automorphic equivalence"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Automorphic equivalence {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Equivalence and clustering. Concept id: `automorphic_equivalence`. 1 measure.

## Definition {#concept-definition}

Orbits of the automorphism group of the binary ties: nodes that map to each other under some automorphism share a label.

## References {#concept-references}

[mckay2014practical](../../references.html#mckay2014practical)

## Automorphic equivalence {#automorphic_equivalence}

Measure id: `automorphic_equivalence`. Original family: Roles and positions.

**Definition.** Orbits of the automorphism group of the binary ties: nodes that map to each other under some automorphism share a label.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs | `orbits` | published documentation |
| [nauty](../../tools/nauty.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `automorphic_equivalence` | nauty | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `pynauty.autgrp(Graph).orbits (nauty 2.8.8): orbit of the automorphism group` | nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented. |

**References:** [mckay2014practical](../../references.html#mckay2014practical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [mckay2014practical](../../references.html#mckay2014practical)
{% endraw %}
