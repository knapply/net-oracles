---
title: "ERGM statistics"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# ERGM statistics {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `ergm_statistics`. 1 measure.

## Definition {#concept-definition}

ERGM statistics. Entries grouped here: Ergm statistics.

*Definition not yet written.*

## Ergm statistics {#ergm_statistics}

Measure id: `ergm_statistics`. Original family: Statistical fitting.

**Definition.** Ergm statistics.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>gwidegree; gwodegree; istar; nodecov; nodefactor; ostar</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ergm_stats_directed</code></td><td>ergm (statnet)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>normalization</td><td>abs 1e-09, rel 1e-12</td><td><code>summary(nw ~ edges + mutual + isolates + istar(2) + ostar(2) + ttriple + ctriple + triangle + gwidegree(0.5, fixed = TRUE, cutoff = 100) + gwodegree(0.5, fixed = TRUE, cutoff = 100) + gwesp(0.5, fixed = TRUE, cutoff = 100) + gwdsp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3") + nodefactor("mod3") + nodecov("num7"))</code></td><td>With two nodes mod3 takes only levels 0 and 1, so nodefactor() gives one statistic instead of two.</td></tr><tr><td><code>ergm_stats_undirected</code></td><td>ergm (statnet)</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>normalization</td><td>abs 1e-09, rel 1e-12</td><td><code>summary(nw ~ edges + isolates + kstar(2:3) + triangle + gwdegree(0.5, fixed = TRUE, cutoff = 100) + gwesp(0.5, fixed = TRUE, cutoff = 100) + gwdsp(0.5, fixed = TRUE, cutoff = 100) + nodematch("mod3") + nodefactor("mod3") + nodecov("num7"))</code></td><td>With one node only level 0 of mod3 occurs, so nodefactor() has no statistics left after dropping the first level.</td></tr></tbody></table></div>

**Tools cited:** [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
