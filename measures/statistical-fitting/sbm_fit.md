---
title: "Stochastic block model fit"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Stochastic block model fit {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `sbm_fit`. 1 measure.

## Definition {#concept-definition}

Stochastic block model fit by minimum description length: agglomerative start, annealed and Markov chain refinement, best of several restarts; returns the blocks, their number and the description length with its parts.

*Definition not yet written.*

## Sbm fit {#sbm_fit}

Measure id: `sbm_fit`. Original family: Statistical fitting.

**Definition.** Stochastic block model fit by minimum description length: agglomerative start, annealed and Markov chain refinement, best of several restarts; returns the blocks, their number and the description length with its parts.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>minimize_blockmodel_dl</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>sbm_fit_dc_vs_graphtool</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network with fewer than two nodes or without edges.</td></tr><tr><td><code>sbm_fit_vs_graphtool</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network with fewer than two nodes or without edges.</td></tr></tbody></table></div>

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
