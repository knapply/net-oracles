---
title: "Bethe Hessian"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bethe Hessian {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `bethe_hessian`. 1 measure.

## Definition {#concept-definition}

Bethe Hessian. Entries grouped here: Bethe hessian.

*Definition not yet written.*

## Bethe hessian {#gm_bethe_hessian}

Measure id: `gm_bethe_hessian`. Original family: Matrices and spectra.

**Definition.** Bethe hessian.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>bethe_hessian_matrix</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gm_bethe_hessian</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.bethe_hessian_matrix(G).toarray() (graph built without weights)</code></td><td>NetworkX does not implement the Bethe Hessian for multigraphs.</td></tr><tr><td><code>gm_bethe_hessian_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.bethe_hessian_matrix(G).toarray() (it reads the attribute 'weight')</code></td><td>NetworkX does not implement the Bethe Hessian for multigraphs.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
