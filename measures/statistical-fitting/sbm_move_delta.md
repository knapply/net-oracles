---
title: "SBM move delta"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SBM move delta {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `sbm_move_delta`. 1 measure.

## Definition {#concept-definition}

SBM move delta. Entries grouped here: Sbm move delta.

*Definition not yet written.*

## Sbm move delta {#sbm_move_delta}

Measure id: `sbm_move_delta`. Original family: Statistical fitting.

**Definition.** Sbm move delta.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>sbm_move_delta_b1</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_move_delta_b3</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_move_delta_dc_b1</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_move_delta_dc_b3</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr></tbody></table></div>

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
