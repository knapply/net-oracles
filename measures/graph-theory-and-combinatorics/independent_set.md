---
title: "Maximal independent set"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximal independent set {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `independent_set`. 3 measures.

## Definition {#concept-definition}

A random maximal independent set containing the start nodes (or one random node), nodes in increasing order.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_independent_is_set">Is independent vertex set</a></td><td><code>cat_independent_is_set</code></td><td>1</td></tr><tr><td><a href="#cat_is_ivs">Is ivs</a></td><td><code>cat_is_ivs</code></td><td>1</td></tr><tr><td><a href="#mis">Mis</a></td><td><code>mis</code></td><td>4</td></tr></tbody></table></div>

## References {#concept-references}

[brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [matula1983smallest](../../references.html#matula1983smallest), [schank2005approximating](../../references.html#schank2005approximating), [welsh1967upper](../../references.html#welsh1967upper)

## Is independent vertex set {#cat_independent_is_set}

Measure id: `cat_independent_is_set`. Original family: Graph theory and combinatorics.

**Definition.** Is independent vertex set.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_independent_is_set-pyigraph">details</a></td><td><code>is_independent_vertex_set</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_independent_is_set-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: is\_independent\_vertex\_set.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Is ivs {#cat_is_ivs}

Measure id: `cat_is_ivs`. Original family: Graph theory and combinatorics.

**Definition.** Is ivs.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_is_ivs-igraph">details</a></td><td><code>is_ivs</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_is_ivs-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: is\_ivs.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Mis {#mis}

Measure id: `mis`. Original family: Graph theory and combinatorics.

**Definition.** A random maximal independent set containing the start nodes (or one random node), nodes in increasing order.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>maximal_independent_set; maximum_independent_set</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-mis-igraph">details</a></td><td><code>independence_number; ivs; largest_ivs; max_ivs; maximal_ivs</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-mis-pyigraph">details</a></td><td><code>independent_vertex_sets; largest_independent_vertex_sets; maximal_independent_vertex_sets</code></td><td>API listing</td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-mis-graphtool">details</a></td><td><code>max_independent_vertex_set</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-mis-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: independence\_number; ivs; largest\_ivs; max\_ivs; maximal\_ivs.
- <a id="why-mis-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: independent\_vertex\_sets; largest\_independent\_vertex\_sets; maximal\_independent\_vertex\_sets.
- <a id="why-mis-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: max\_independent\_vertex\_set.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>mis_check</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>1, 1, 1 for nx.maximal_independent_set(G, [start], seed = 11), checked the same way</code></td><td></td></tr></tbody></table></div>

**References:** [brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [matula1983smallest](../../references.html#matula1983smallest), [schank2005approximating](../../references.html#schank2005approximating), [welsh1967upper](../../references.html#welsh1967upper)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
