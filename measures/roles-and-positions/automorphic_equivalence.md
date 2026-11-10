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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-automorphic_equivalence-ucinet) | `orbits` | published documentation |
| [nauty](../../tools/nauty.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-automorphic_equivalence-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `automorphic_equivalence` | nauty | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `pynauty.autgrp(Graph).orbits (nauty 2.8.8): orbit of the automorphism group` | nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented. |

**References:** [mckay2014practical](../../references.html#mckay2014practical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [mckay2014practical](../../references.html#mckay2014practical)
{% endraw %}
