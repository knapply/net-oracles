---
title: "Automorphic equivalence"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Automorphic equivalence {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Equivalence and clustering. Concept id: `automorphic_equivalence`. 1 measure.

## Definition {#concept-definition}

Orbits of the automorphism group of the binary ties: nodes that map to each other under some automorphism share a label.

*Definition not yet written.*

## References {#concept-references}

[mckay2014practical](../../references.html#mckay2014practical)

## Automorphic equivalence {#automorphic_equivalence}

Measure id: `automorphic_equivalence`. Original family: Roles and positions.

**Definition.** Orbits of the automorphism group of the binary ties: nodes that map to each other under some automorphism share a label.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-automorphic_equivalence-ucinet">details</a></td><td><code>orbits</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/nauty.html">nauty</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-automorphic_equivalence-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>automorphic_equivalence</code></td><td>nauty</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>pynauty.autgrp(Graph).orbits (nauty 2.8.8): orbit of the automorphism group</code></td><td>nauty graphs are simple: parallel edges (edge multiplicities, which the reference and the definition oracle respect) cannot be represented.</td></tr></tbody></table></div>

**References:** [mckay2014practical](../../references.html#mckay2014practical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [mckay2014practical](../../references.html#mckay2014practical)
{% endraw %}
