---
title: "Compactness"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Compactness {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Efficiency, compactness and hierarchy. Concept id: `compactness`. 1 measure.

## Definition {#concept-definition}

Compactness. Entries grouped here: Compactness.

*Definition not yet written.*

## Compactness {#compactness}

Measure id: `compactness`. Original family: Descriptive statistics.

**Definition.** Compactness.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-compactness-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-compactness-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>compactness</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>nx.global_efficiency (undirected), or mean of 1/d from nx.shortest_path_length (directed)</code></td><td></td></tr><tr><td><code>compactness</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>mean of 1 / igraph::distances(g, mode = 'out', weights = NA) off the diagonal</code></td><td></td></tr><tr><td><code>compactness_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-12</td><td><code>mean of 1/d from nx.shortest_path_length(G, weight = 'weight')</code></td><td></td></tr><tr><td><code>compactness_weighted</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-12</td><td><code>mean of 1 / igraph::distances(g, mode = 'out', weights = E(g)$weight) off the diagonal</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
