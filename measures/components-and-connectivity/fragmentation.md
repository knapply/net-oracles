---
title: "Fragmentation"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Fragmentation {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `fragmentation`. 1 measure.

## Definition {#concept-definition}

Fragmentation. Entries grouped here: Fragmentation.

## Fragmentation {#fragmentation}

Measure id: `fragmentation`. Original family: Components and connectivity.

**Definition.** Fragmentation.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-fragmentation-ucinet) | `fragcent` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-fragmentation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `fragmentation` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-09 | `1 - sum(s (s - 1)) / (n (n - 1)) over the sizes s of igraph::components(g, mode = 'weak')$csize` |  |
| `fragmentation_strong` | igraph (R) | directed | agrees |  |  | abs 1e-12, rel 1e-09 | `1 - sum(s (s - 1)) / (n (n - 1)) over the sizes s of igraph::components(g, mode = 'strong')$csize` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
