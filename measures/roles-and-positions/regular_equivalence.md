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

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../../tools/sna.html) | ✓ checked, agrees | `redist` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |
| [blockmodeling](../../tools/blockmodeling.html) | · reported in docs | `REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow` | API listing |

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

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Automorphic (MaxSim) and regular equivalence (REGE, CATREGE)` | API listing |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
