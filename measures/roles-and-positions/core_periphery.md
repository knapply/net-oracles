---
title: "Core-periphery (discrete)"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Core-periphery (discrete) {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Core-periphery. Concept id: `core_periphery`. 2 measures.

## Definition {#concept-definition}

Discrete core-periphery fit: the core membership that best matches the ideal pattern, by tabu search from random starts.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Core periphery](#core_periphery) | `core_periphery` | 3 |
| [Estevez-Nordlund variant](#core_periphery_en) | `core_periphery_en` | 1 |

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [glover1989tabu](../../references.html#glover1989tabu)

## Core periphery {#core_periphery}

Measure id: `core_periphery`. Original family: Roles and positions.

**Definition.** Discrete core-periphery fit: the core membership that best matches the ideal pattern, by tabu search from random starts.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-core_periphery-bct) | `core_periphery_dir` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-core_periphery-ucinet) | `Core/periphery: categorical (Borgatti-Everett), continuous coreness, Estevez-Nordlund variant (6.833); catcp` | published documentation |
| [cpnet](../../tools/cpnet.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_periphery-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: core\_periphery\_dir.
- <a id="why-core_periphery-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `core_periphery_ones_vs_cpnet` | cpnet | any | agrees |  |  | abs 1e-09, rel 1e-09 | `correlation, core-periphery pairs expected tied, of the core set of cpnet.BE().detect(G)` |  |
| `core_periphery_vs_cpnet` | cpnet | any | agrees |  |  | abs 1e-09, rel 1e-09 | `correlation, links 'missing', of the core set of cpnet.BE().detect(G) (undirected, unweighted, no loops)` |  |
| `core_periphery_weighted_vs_cpnet` | cpnet | any | agrees |  |  | abs 1e-09, rel 1e-09 | `correlation with weighted values of the core set of cpnet.BE().detect(G) (unweighted)` |  |
| `core_periphery_zeros_vs_cpnet` | cpnet | any | agrees |  |  | abs 1e-09, rel 1e-09 | `correlation, core-periphery pairs expected untied, of the core set of cpnet.BE().detect(G)` |  |

**References:** [borgatti1999models](../../references.html#borgatti1999models), [glover1989tabu](../../references.html#glover1989tabu)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [rubinov2010complex](../../references.html#rubinov2010complex), [tool_cpnet](../../references.html#tool_cpnet)

## Estevez-Nordlund variant {#core_periphery_en}

Measure id: `core_periphery_en`. Original family: Roles and positions.

**Definition.** Estevez-Nordlund variant.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-core_periphery_en-ucinet) | `enordcp` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_periphery_en-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
