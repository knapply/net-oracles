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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `brokerage` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-brokerage-ucinet) | `Brokerage: Gould-Fernandez roles (five or six); brokerageconcentration` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-brokerage-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `brokerage` | sna | any | agrees |  |  | abs 0, rel 0 | `sna::brokerage(m, cl = (0:(n - 1)) %% 3)$raw.nli` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
