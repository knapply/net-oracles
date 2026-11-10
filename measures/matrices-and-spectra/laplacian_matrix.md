---
title: "Laplacian matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Laplacian matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `laplacian_matrix`. 2 measures.

## Definition {#concept-definition}

Laplacian matrix. Entries grouped here: Gm laplacian; Magnetic laplacian matrix.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#gm_laplacian">Gm laplacian</a></td><td><code>gm_laplacian</code></td><td>8</td></tr><tr><td><a href="#cat_laplacian_magnetic_matrix">Magnetic laplacian matrix</a></td><td><code>cat_laplacian_magnetic_matrix</code></td><td>1</td></tr></tbody></table></div>

## Gm laplacian {#gm_laplacian}

Measure id: `gm_laplacian`. Original family: Matrices and spectra.

**Definition.** Gm laplacian.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>directed_combinatorial_laplacian_matrix; directed_laplacian_matrix; laplacian_matrix; normalized_laplacian_matrix</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gm_laplacian-igraph">details</a></td><td><code>laplacian_matrix</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gm_laplacian-pyigraph">details</a></td><td><code>laplacian</code></td><td>API listing</td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gm_laplacian-graphtool">details</a></td><td><code>laplacian</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gm_laplacian-networkit">details</a></td><td><code>laplacianMatrix</code></td><td>API listing</td></tr><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gm_laplacian-sknetwork">details</a></td><td><code>Laplacian</code></td><td>API listing</td></tr><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gm_laplacian-centiserve">details</a></td><td><code>laplacian</code></td><td>API listing</td></tr><tr><td><a href="../../tools/graspologic.html">graspologic</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (direction): For a directed graph graspologic's 'I-DAD' form is D_in^-1/2 (D_in - A) D_in^-1/2 with in-degrees (graspologic/utils/utils.py, to_laplacian), and a... <a href="#why-gm_laplacian-graspologic">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gm_laplacian-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: laplacian\_matrix.
- <a id="why-gm_laplacian-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: laplacian.
- <a id="why-gm_laplacian-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: laplacian.
- <a id="why-gm_laplacian-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: laplacianMatrix.
- <a id="why-gm_laplacian-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Laplacian.
- <a id="why-gm_laplacian-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: laplacian.
- <a id="why-gm_laplacian-graspologic"></a>**[graspologic](../../tools/graspologic.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> graspologic 3.4.4 was run and its value differs from the reference value by convention (direction) on inputs tagged directed. For a directed graph graspologic's 'I-DAD' form is D\_in^-1/2 (D\_in - A) D\_in^-1/2 with in-degrees (graspologic/utils/utils.py, to\_laplacian), and a node without in-links gets 0 on the diagonal; the reference, like NetworkX's normalized\_laplacian\_matrix, normalizes by out-degrees. Undirected fixtures agree. Relation to the reference value: Degree used: the 'I-DAD' form normalizes by in-degrees and gives a node without in-links 0 on the diagonal; the reference value and NetworkX use out-degrees; undirected agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 8 comparisons differ and 27 agree. Finding F072 (convention): The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs. Findings: [F072](../../findings.html#f072).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gm_laplacian</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.laplacian_matrix(G, weight = None).toarray()</code></td><td></td></tr><tr><td><code>gm_laplacian_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.laplacian_matrix(G, weight = 'weight').toarray()</code></td><td></td></tr><tr><td><code>gm_normalized_laplacian</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.normalized_laplacian_matrix(G, weight = None).toarray()</code></td><td></td></tr><tr><td><code>gm_normalized_laplacian</code></td><td>graspologic</td><td>any</td><td>differs</td><td>directed</td><td>direction</td><td>abs 1e-14, rel 1e-12</td><td><code>graspologic.utils.to_laplacian(A, form = 'I-DAD')</code></td><td>Undirected fixtures agree.</td></tr><tr><td><code>gm_normalized_laplacian_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.normalized_laplacian_matrix(G, weight = 'weight').toarray()</code></td><td></td></tr><tr><td><code>gm_normalized_laplacian_weighted</code></td><td>graspologic</td><td>any</td><td>differs</td><td>directed</td><td>direction</td><td>abs 1e-14, rel 1e-12</td><td><code>graspologic.utils.to_laplacian(W, form = 'I-DAD')</code></td><td>Undirected fixtures agree.</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f072">F072</a></td><td>graspologic</td><td>convention</td><td>The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs</td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_graspologic](../../references.html#tool_graspologic), [tool_sknetwork](../../references.html#tool_sknetwork)

## Magnetic laplacian matrix {#cat_laplacian_magnetic_matrix}

Measure id: `cat_laplacian_magnetic_matrix`. Original family: Matrices and spectra.

**Definition.** Magnetic laplacian matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_laplacian_magnetic_matrix-networkx">details</a></td><td><code>magnetic_laplacian_matrix</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_laplacian_magnetic_matrix-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: magnetic\_laplacian\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
