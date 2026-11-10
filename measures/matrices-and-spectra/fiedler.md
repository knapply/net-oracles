---
title: "Fiedler value and vector"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Fiedler value and vector {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Spectra. Concept id: `fiedler`. 1 measure.

## Definition {#concept-definition}

Fiedler value and vector. Entries grouped here: Fiedler.

*Definition not yet written.*

## Fiedler {#gm_fiedler}

Measure id: `gm_fiedler`. Original family: Matrices and spectra.

**Definition.** Fiedler.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults, normalization and ties): For two nodes NetworkX returns [1, -1] without solving. <a href="#why-gm_fiedler-networkx">details</a></td><td><code>algebraic_connectivity; fiedler_vector; spectral_bisection</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gm_fiedler-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults, normalization and ties) on inputs tagged two\_nodes. For two nodes NetworkX returns \[1, -1\] without solving; the reference returns the unit vector with its first entry negative. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-06, rel 1e-05 (0 means exact equality). 2 comparisons differ and 85 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gm_fiedler_value</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-09</td><td><code>nx.algebraic_connectivity(G, tol = 1e-10, method = 'tracemin_lu') (directed graphs through NetworkX's _preprocess_graph, then weight = 'weight', as spectral_ordering reads them)</code></td><td></td></tr><tr><td><code>gm_fiedler_value_normalized_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-10, rel 1e-09</td><td><code>nx.algebraic_connectivity(G, weight = 'weight', normalized = True, tol = 1e-10, method = 'tracemin_lu')</code></td><td></td></tr><tr><td><code>gm_fiedler_vector</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>two_nodes</td><td>defaults</td><td>abs 1e-06, rel 1e-05</td><td><code>nx.fiedler_vector(G) (default method tracemin_pcg, tol 1e-8)</code></td><td>For two nodes NetworkX returns [1, -1] without solving; the reference returns the unit vector with its first entry negative (the backend returns NetworkX's [1, -1]).</td></tr><tr><td><code>gm_fiedler_vector_normalized</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>two_nodes</td><td>defaults, normalization, ties</td><td>abs 1e-06, rel 1e-05</td><td><code>nx.fiedler_vector(G, normalized = True)</code></td><td>For two nodes NetworkX returns [1, -1] without solving; the reference returns the unit vector with its first entry negative. NetworkX's tracemin_pcg iteration for the normalized Laplacian does not converge on these graphs and, having no iteration cap, never returns.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
