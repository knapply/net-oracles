---
title: "MR-QAP regression"
layout: default
parent: "Inference (QAP, null models)"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# MR-QAP regression {#concept-top}

Family: [Inference (QAP, null models)](index.html). Subfamily: QAP and permutation tests. Concept id: `qap_regression`. 1 measure.

## Definition {#concept-definition}

MR-QAP regression. Entries grouped here: MR-QAP regression (Y-permutation, double semi-partialling).

## MR-QAP regression (Y-permutation, double semi-partialling) {#qap_regression}

Measure id: `qap_regression`. Original family: Inference (QAP, null models).

**Definition.** MR-QAP regression (Y-permutation, double semi-partialling).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-qap_regression-sna) | `netlm` | documentation |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-qap_regression-ucinet) | `Logistic regression with 2-tailed tests (6.751), OLS regression, univariate statistics, correlation, ANOVA/density-by-group (blocks), contingency tables with od; logistic; regress` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-qap_regression-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (R package sna: exported functions and help titles); API names: netlm.
- <a id="why-qap_regression-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
