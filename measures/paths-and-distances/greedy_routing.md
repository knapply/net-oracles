---
title: "Greedy routing and navigation"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Greedy routing and navigation {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `greedy_routing`. 3 measures.

## Definition {#concept-definition}

Greedy routing and navigation. Entries grouped here: Hyperbolic greedy routing; Hyperbolic greedy success rate; Navigation.

*Definition not yet written.* Documented only (rustworkx hyperbolic greedy routing and BCT navigation), never run; the sources give the name and the tool's function, not a formula, and no verified bibliography entry for the original definition is available.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_greedy_hyperbolic_routing">Hyperbolic greedy routing</a></td><td><code>cat_greedy_hyperbolic_routing</code></td><td>1</td></tr><tr><td><a href="#cat_greedy_hyperbolic_rate_success">Hyperbolic greedy success rate</a></td><td><code>cat_greedy_hyperbolic_rate_success</code></td><td>1</td></tr><tr><td><a href="#cat_navigation">Navigation</a></td><td><code>cat_navigation</code></td><td>1</td></tr></tbody></table></div>

## Hyperbolic greedy routing {#cat_greedy_hyperbolic_routing}

Measure id: `cat_greedy_hyperbolic_routing`. Original family: Generators and rewiring.

**Definition.** Hyperbolic greedy routing.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_greedy_hyperbolic_routing-rustworkx">details</a></td><td><code>hyperbolic_greedy_routing</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_greedy_hyperbolic_routing-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: hyperbolic\_greedy\_routing.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Hyperbolic greedy success rate {#cat_greedy_hyperbolic_rate_success}

Measure id: `cat_greedy_hyperbolic_rate_success`. Original family: Generators and rewiring.

**Definition.** Hyperbolic greedy success rate.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_greedy_hyperbolic_rate_success-rustworkx">details</a></td><td><code>hyperbolic_greedy_success_rate</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_greedy_hyperbolic_rate_success-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: hyperbolic\_greedy\_success\_rate.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Navigation {#cat_navigation}

Measure id: `cat_navigation`. Original family: Graph theory and combinatorics.

**Definition.** Navigation.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_navigation-bct">details</a></td><td><code>navigation_wu</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_navigation-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: navigation\_wu.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
