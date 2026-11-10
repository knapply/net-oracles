---
title: "Wiener index"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Wiener index {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `wiener_index`. 1 measure.

## Definition {#concept-definition}

Sum of the distances over unordered pairs (ordered pairs in a directed network); infinite unless connected.

*Definition not yet written.*

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Index {#dm_index}

Measure id: `dm_index`. Original family: Paths and distances.

**Definition.** Sum of the distances over unordered pairs (ordered pairs in a directed network); infinite unless connected.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>gutman_index; hyper_wiener_index; schultz_index; wiener_index</code></td><td></td></tr><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults): The efficiency of a one-node network is 0/0: BCT returns NaN, the reference 0. <a href="#why-dm_index-bct">details</a></td><td></td><td></td></tr><tr><td><a href="../../tools/bctpy.html">bctpy</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dm_index-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> BCT (Octave) 2019-03-03 was run and its value differs from the reference value by convention (defaults) on the fixtures single\_node. The efficiency of a one-node network is 0/0: BCT returns NaN, the reference 0. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 1 comparisons differ and 27 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>dm_global_efficiency</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) directed</td><td>direction</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.global_efficiency(G)</code></td><td>NetworkX's global_efficiency is not implemented for directed graphs.</td></tr><tr><td><code>dm_global_efficiency</code></td><td>BCT (Octave)</td><td>any</td><td>differs</td><td></td><td>defaults</td><td>abs 1e-12, rel 1e-12</td><td><code>Brain Connectivity Toolbox 2019-03-03 in Octave: efficiency_bin, on the binary adjacency matrix without loops or parallel edges</code></td><td>The efficiency of a one-node network is 0/0: BCT returns NaN, the reference 0.</td></tr><tr><td><code>dm_global_efficiency</code></td><td>bctpy</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td>defaults, normalization</td><td>abs 1e-12, rel 1e-12</td><td><code>bct.efficiency_bin(A binary, local = False)</code></td><td>With one node efficiency_bin() divides by n (n - 1) = 0 and returns NaN; the reference (like NetworkX) returns 0.</td></tr><tr><td><code>dm_global_efficiency_weighted</code></td><td>bctpy</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>bct.efficiency_wei(W summed, local = False)</code></td><td></td></tr><tr><td><code>dm_gutman</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.gutman_index(G)</code></td><td>NetworkX's schultz_index, gutman_index, and hyper_wiener_index are not implemented for multigraphs.</td></tr><tr><td><code>dm_gutman_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.gutman_index(G, weight = 'weight')</code></td><td>NetworkX's schultz_index, gutman_index, and hyper_wiener_index are not implemented for multigraphs.</td></tr><tr><td><code>dm_harmonic_diameter</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.harmonic_diameter(G)</code></td><td></td></tr><tr><td><code>dm_harmonic_diameter_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.harmonic_diameter(G, weight = 'weight')</code></td><td></td></tr><tr><td><code>dm_hyper_wiener</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>0.5 * nx.hyper_wiener_index(G)</code></td><td>NetworkX's hyper_wiener_index is not implemented for multigraphs.</td></tr><tr><td><code>dm_hyper_wiener_networkx</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.hyper_wiener_index(G)</code></td><td>NetworkX's schultz_index, gutman_index, and hyper_wiener_index are not implemented for multigraphs.</td></tr><tr><td><code>dm_schultz</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.schultz_index(G)</code></td><td>NetworkX's schultz_index, gutman_index, and hyper_wiener_index are not implemented for multigraphs.</td></tr><tr><td><code>dm_schultz_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.schultz_index(G, weight = 'weight')</code></td><td>NetworkX's schultz_index, gutman_index, and hyper_wiener_index are not implemented for multigraphs.</td></tr><tr><td><code>dm_wiener</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.wiener_index(G)</code></td><td></td></tr><tr><td><code>dm_wiener_strength</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.wiener_index(G, weight = 'length') with length = 1 / weight</code></td><td></td></tr><tr><td><code>dm_wiener_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.wiener_index(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f023">F023</a></td><td>NetworkX</td><td>defect</td><td>hyper_wiener_index is twice the published value</td></tr></tbody></table></div>

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
