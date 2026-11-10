---
title: "Graph matrix operators"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph matrix operators {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `matrix_operators`. 1 measure.

## Definition {#concept-definition}

Graph matrix operators. Entries grouped here: Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence).

## Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence) {#matrix_operators}

Measure id: `matrix_operators`. Original family: Matrices and spectra.

**Definition.** Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-matrix_operators-graphtool) | `AdjacencyOperator; CompactHashimotoOperator; HashimotoOperator; IncidenceOperator; LaplacianOperator; TransitionOperator; hashimoto; transition` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-matrix_operators-ucinet) | `transition` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-matrix_operators-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: AdjacencyOperator; CompactHashimotoOperator; HashimotoOperator; IncidenceOperator; LaplacianOperator; TransitionOperator; hashimoto; transition.
- <a id="why-matrix_operators-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
