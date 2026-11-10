---
title: "Attracting components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Attracting components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `attracting_components`. 4 measures.

## Definition {#concept-definition}

Attracting components. Entries grouped here: Attracting; Attracting flags; Is attracting component; Number attracting components.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#attracting">Attracting</a></td><td><code>attracting</code></td><td>1</td></tr><tr><td><a href="#attracting_flags">Attracting flags</a></td><td><code>attracting_flags</code></td><td>1</td></tr><tr><td><a href="#cat_attracting_component_is">Is attracting component</a></td><td><code>cat_attracting_component_is</code></td><td>1</td></tr><tr><td><a href="#cat_attracting_component">Number attracting components</a></td><td><code>cat_attracting_component</code></td><td>1</td></tr></tbody></table></div>

## Attracting {#attracting}

Measure id: `attracting`. Original family: Components and connectivity.

**Definition.** Attracting.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>attracting_components</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_attracting</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.attracting_components(G), labelled by nx.condensation(G).graph['mapping'], -1 elsewhere</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Attracting flags {#attracting_flags}

Measure id: `attracting_flags`. Original family: Components and connectivity.

**Definition.** Attracting flags.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>conn_attracting_flags</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>1 if v is in a component of nx.attracting_components(G)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is attracting component {#cat_attracting_component_is}

Measure id: `cat_attracting_component_is`. Original family: Components and connectivity.

**Definition.** Is attracting component.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_attracting_component_is-networkx">details</a></td><td><code>is_attracting_component</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attracting_component_is-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_attracting\_component.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Number attracting components {#cat_attracting_component}

Measure id: `cat_attracting_component`. Original family: Components and connectivity.

**Definition.** Number attracting components.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_attracting_component-networkx">details</a></td><td><code>number_attracting_components</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attracting_component-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: number\_attracting\_components.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
