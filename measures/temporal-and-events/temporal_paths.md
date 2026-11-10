---
title: "Temporal paths"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Temporal paths {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Temporal descriptives. Concept id: `temporal_paths`. 1 measure.

## Definition {#concept-definition}

Temporal paths. Entries grouped here: Temporal paths.

*Definition not yet written.*

## Temporal paths {#temporal_paths}

Measure id: `temporal_paths`. Original family: Temporal and events.

**Definition.** Temporal paths.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tsna.html">tsna / networkDynamic</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>tPath</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>temporal_earliest_arrival_instantaneous</code></td><td>tsna / networkDynamic</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>start + tPath(nd, v, 'fwd', 'earliest.arrive', start, end, graph.step.time = 0)$tdist for every v</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [handcock2008statnet](../../references.html#handcock2008statnet)
{% endraw %}
