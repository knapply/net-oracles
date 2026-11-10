---
title: "Network autocorrelation"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Network autocorrelation {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `network_autocorrelation`. 1 measure.

## Definition {#concept-definition}

Network autocorrelation. Entries grouped here: Network autocorrelation: lag/error model, Moran, Geary.

## Network autocorrelation: lag/error model, Moran, Geary {#network_autocorrelation}

Measure id: `network_autocorrelation`. Original family: Inference (QAP, null models).

**Definition.** Network autocorrelation: lag/error model, Moran, Geary.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-network_autocorrelation-sna) | `lnam; nacf` | documentation |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-network_autocorrelation-ucinet) | `Geary; Network autocorrelation (continuous, 6.753): Moran, Geary; lautocorr` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-network_autocorrelation-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: lnam; nacf.
- <a id="why-network_autocorrelation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
