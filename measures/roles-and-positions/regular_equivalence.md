---
title: "Regular equivalence (REGE, CATREGE)"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Regular equivalence (REGE, CATREGE) {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Equivalence and clustering. Concept id: `regular_equivalence`. 2 measures.

## Definition {#concept-definition}

Regular equivalence (REGE, CATREGE). Entries grouped here: Regular equivalence; Automorphic (Max Sim) and regular equivalence (REGE, CATREGE).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Regular equivalence](#regular_equivalence) | `regular_equivalence` | 3 |
| [Automorphic (Max Sim) and regular equivalence (REGE, CATREGE)](#cat_automorphic_catrege_equivalence_max_rege_regular_sim) | `cat_automorphic_catrege_equivalence_max_rege_regular_sim` | 1 |

## Regular equivalence {#regular_equivalence}

Measure id: `regular_equivalence`. Original family: Roles and positions.

**Definition.** Regular equivalence.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `redist` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-regular_equivalence-ucinet) |  | published documentation |
| [blockmodeling](../../tools/blockmodeling.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-regular_equivalence-blockmodeling) | `REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-regular_equivalence-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-regular_equivalence-blockmodeling"></a>**[blockmodeling](../../tools/blockmodeling.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. blockmodeling 1.1.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package blockmodeling: exported functions and help titles); API names: REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `regular_equivalence` | sna | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `classes at distance 0 in sna::redist(m, method = 'catrege')` | sna fails on a network with a single node. |
| `regular_equivalence_seed` | sna | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `sna::redist(m, method = 'catrege', seed.partition = v %% 3), distance 0` | sna fails on a network with a single node. |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [ziberna2007generalized](../../references.html#ziberna2007generalized)

## Automorphic (Max Sim) and regular equivalence (REGE, CATREGE) {#cat_automorphic_catrege_equivalence_max_rege_regular_sim}

Measure id: `cat_automorphic_catrege_equivalence_max_rege_regular_sim`. Original family: Roles and positions.

**Definition.** Automorphic (Max Sim) and regular equivalence (REGE, CATREGE).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-cat_automorphic_catrege_equivalence_max_rege_regular_sim-ucinet) | `Automorphic (MaxSim) and regular equivalence (REGE, CATREGE)` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_automorphic_catrege_equivalence_max_rege_regular_sim-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
