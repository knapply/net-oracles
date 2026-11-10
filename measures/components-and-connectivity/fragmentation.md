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

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `fragcent` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `fragmentation` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-09 | `1 - sum(s (s - 1)) / (n (n - 1)) over the sizes s of igraph::components(g, mode = 'weak')$csize` |  |
| `fragmentation_strong` | igraph (R) | directed | agrees |  |  | abs 1e-12, rel 1e-09 | `1 - sum(s (s - 1)) / (n (n - 1)) over the sizes s of igraph::components(g, mode = 'strong')$csize` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
