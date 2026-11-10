---
title: "Brokerage"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Brokerage {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `brokerage`. 1 measure.

## Definition {#concept-definition}

Brokerage. Entries grouped here: Brokerage.

## Brokerage {#brokerage}

Measure id: `brokerage`. Original family: Roles and positions.

**Definition.** Brokerage.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../../tools/sna.html) | ✓ checked, agrees | `brokerage` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Brokerage: Gould-Fernandez roles (five or six); brokerageconcentration` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `brokerage` | sna | any | agrees |  |  | abs 0, rel 0 | `sna::brokerage(m, cl = (0:(n - 1)) %% 3)$raw.nli` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
