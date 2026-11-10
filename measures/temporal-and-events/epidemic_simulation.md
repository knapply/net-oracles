---
title: "Epidemic simulation (SIR, SEIR)"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Epidemic simulation (SIR, SEIR) {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Diffusion simulation. Concept id: `epidemic_simulation`. 2 measures.

## Definition {#concept-definition}

Epidemic simulation (SIR, SEIR). Entries grouped here: Epidemic Simulation SEIR; Sir.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_epidemic_seir_simulation">Epidemic Simulation SEIR</a></td><td><code>cat_epidemic_seir_simulation</code></td><td>1</td></tr><tr><td><a href="#cat_sir">Sir</a></td><td><code>cat_sir</code></td><td>1</td></tr></tbody></table></div>

## Epidemic Simulation SEIR {#cat_epidemic_seir_simulation}

Measure id: `cat_epidemic_seir_simulation`. Original family: Graph theory and combinatorics.

**Definition.** Epidemic Simulation SEIR.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_epidemic_seir_simulation-networkit">details</a></td><td><code>EpidemicSimulationSEIR</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_epidemic_seir_simulation-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: EpidemicSimulationSEIR.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Sir {#cat_sir}

Measure id: `cat_sir`. Original family: Graph theory and combinatorics.

**Definition.** Sir.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_sir-igraph">details</a></td><td><code>sir</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sir-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: sir.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
