---
title: "ERGM change statistics"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# ERGM change statistics {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_change_sums`. 1 measure.

## Definition {#concept-definition}

ERGM change statistics. Entries grouped here: Ergm change sums.

*Definition not yet written.*

## Ergm change sums {#ergm_change_sums}

Measure id: `ergm_change_sums`. Original family: Statistical fitting.

**Definition.** Ergm change sums.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_change_sums_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>mple &lt;- ergmMPLE(nw ~ &lt;the terms of ergm_stats_directed&gt;, output = "matrix"); colSums(mple$predictor * mple$weights)</code></td><td>nodefactor() gives one statistic on two nodes (see ergm_stats_directed).</td></tr><tr><td><code>ergm_change_sums_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>direction, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>mple &lt;- ergmMPLE(nw ~ &lt;the terms of ergm_stats_undirected&gt;, output = "matrix"); colSums(mple$predictor * mple$weights)</code></td><td>A network of one node has no dyads, and nodefactor() has no level left (see ergm_stats_undirected).</td></tr></tbody></table></div>

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
