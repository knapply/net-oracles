---
title: "Hierarchy"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Hierarchy {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `hierarchy_krackhardt`. 1 measure.

## Definition {#concept-definition}

Hierarchy. Entries grouped here: Hierarchy.

## Hierarchy {#hierarchy}

Measure id: `hierarchy`. Original family: Roles and positions.

**Definition.** Hierarchy.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-hierarchy-igraph) | `hierarchy` | API listing |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-hierarchy-sna) | `hierarchy` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-hierarchy-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-hierarchy-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: hierarchy.
- <a id="why-hierarchy-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: hierarchy.
- <a id="why-hierarchy-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F083](../../findings.html#f083) | manynet | defect | hierarchy differs from the definition on all 25 fixtures |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
