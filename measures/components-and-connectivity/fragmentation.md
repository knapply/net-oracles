---
title: "Fragmentation"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Fragmentation {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `fragmentation`. 1 measure.

## Definition {#concept-definition}

Fragmentation. Entries grouped here: Fragmentation.

*Definition not yet written.*

## Fragmentation {#fragmentation}

Measure id: `fragmentation`. Original family: Components and connectivity.

**Definition.** Fragmentation.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-fragmentation-ucinet">details</a></td><td><code>fragcent</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-fragmentation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>fragmentation</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>1 - sum(s (s - 1)) / (n (n - 1)) over the sizes s of igraph::components(g, mode = 'weak')$csize</code></td><td></td></tr><tr><td><code>fragmentation_strong</code></td><td>igraph (R)</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>1 - sum(s (s - 1)) / (n (n - 1)) over the sizes s of igraph::components(g, mode = 'strong')$csize</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
