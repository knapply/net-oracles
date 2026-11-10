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

*Definition not yet written.*

## Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence) {#matrix_operators}

Measure id: `matrix_operators`. Original family: Matrices and spectra.

**Definition.** Graph matrix operators (adjacency, Laplacian, Hashimoto, incidence).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-matrix_operators-graphtool">details</a></td><td><code>AdjacencyOperator; CompactHashimotoOperator; HashimotoOperator; IncidenceOperator; LaplacianOperator; TransitionOperator; hashimoto; transition</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-matrix_operators-ucinet">details</a></td><td><code>transition</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-matrix_operators-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: AdjacencyOperator; CompactHashimotoOperator; HashimotoOperator; IncidenceOperator; LaplacianOperator; TransitionOperator; hashimoto; transition.
- <a id="why-matrix_operators-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
