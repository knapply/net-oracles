---
title: "Label propagation"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Label propagation {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `label_propagation`. 3 measures.

## Definition {#concept-definition}

Label propagation communities: every node repeatedly takes the dominant label among the nodes it reads.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#label_propagation">Label propagation</a></td><td><code>label_propagation</code></td><td>7</td></tr><tr><td><a href="#cnx_label_propagation">Cnx label propagation</a></td><td><code>cnx_label_propagation</code></td><td>1</td></tr><tr><td><a href="#cnx_seeded_labels">Seeded labels</a></td><td><code>cnx_seeded_labels</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[cordasco2010community](../../references.html#cordasco2010community), [raghavan2007near](../../references.html#raghavan2007near), [traag2023large](../../references.html#traag2023large)

## Label propagation {#label_propagation}

Measure id: `label_propagation`. Original family: Communities.

**Definition.** Label propagation communities: every node repeatedly takes the dominant label among the nodes it reads.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults, multi-edges and self-loops): NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity. <a href="#why-label_propagation-networkx">details</a></td><td><code>asyn_lpa_communities; fast_label_propagation_communities; label_propagation_communities</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges and self-loops): the reference ignores self-loops (a node never reads its own label). <a href="#why-label_propagation-igraph">details</a></td><td><code>cluster_label_prop</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-label_propagation-pyigraph">details</a></td><td><code>community_label_propagation</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-label_propagation-networkit">details</a></td><td><code>LPDegreeOrdered; PLP</code></td><td>API listing</td></tr><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-label_propagation-sknetwork">details</a></td><td><code>PropagationClustering</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-label_propagation-jgrapht">details</a></td><td><code>LabelPropagationClustering</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-label_propagation-ucinet">details</a></td><td><code>labelprop</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-label_propagation-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults, multi-edges and self-loops) on inputs tagged edge\_case, loops and multi\_edges. label\_prop\_quality\_fast and label\_prop\_quality\_retention: NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0). label\_prop\_semisync: NetworkX runs on the simple graph here (parallel edges once, no loops); the reference counts parallel edges with their multiplicity. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0.05, rel 0 on all 2 comparisons where the difference occurs. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0, rel 0 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 0.05, rel 0; abs 0, rel 0 (0 means exact equality). 3 comparisons differ and 84 agree. Finding F029 (convention): Ties are broken by Python set or insertion order. Findings: [F029](../../findings.html#f029).
- <a id="why-label_propagation-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (multi-edges and self-loops) on inputs tagged loops. the reference ignores self-loops (a node never reads its own label); igraph documents no rule for loops, but its mean on multi\_loops\_und (0.258) is what a node that reads its own label once per loop gives (0.265 over 300 simulated runs, against 0.206 with loops ignored), as NetworkX does. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0.05, rel 0 (0 means exact equality). 1 comparisons differ and 29 agree.
- <a id="why-label_propagation-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_label\_propagation.
- <a id="why-label_propagation-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LPDegreeOrdered; PLP.
- <a id="why-label_propagation-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: PropagationClustering.
- <a id="why-label_propagation-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: LabelPropagationClustering.
- <a id="why-label_propagation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>label_prop_quality</code></td><td>igraph (R)</td><td>undirected</td><td>differs</td><td>loops</td><td>multi_edges, self_loops</td><td>abs 0.05, rel 0</td><td><code>mean over set.seed(1..100) of modularity(g, cluster_label_prop(g, weights = NA))</code></td><td>the reference ignores self-loops (a node never reads its own label); igraph documents no rule for loops, but its mean on multi_loops_und (0.258) is what a node that reads its own label once per loop gives (0.265 over 300 simulated runs, against 0.206 with loops ignored), as NetworkX does</td></tr><tr><td><code>label_prop_quality_fast</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>edge_case, loops, multi_edges</td><td>defaults, multi_edges, self_loops</td><td>abs 0.05, rel 0</td><td><code>mean over seeds of modularity(G, fast_label_propagation_communities(simple graph, seed = s))</code></td><td>NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0)</td></tr><tr><td><code>label_prop_quality_retention</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>edge_case, loops, multi_edges</td><td>defaults, multi_edges, self_loops</td><td>abs 0.05, rel 0</td><td><code>mean over seeds of modularity(G, asyn_lpa_communities(simple graph, seed = s))</code></td><td>NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0)</td></tr><tr><td><code>label_prop_semisync</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>loops, multi_edges</td><td>multi_edges, self_loops</td><td>abs 0, rel 0</td><td><code>nx.community.label_propagation_communities(simple graph)</code></td><td>NetworkX runs on the simple graph here (parallel edges once, no loops); the reference counts parallel edges with their multiplicity</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f029">F029</a></td><td>NetworkX</td><td>convention</td><td>Ties are broken by Python set or insertion order</td></tr></tbody></table></div>

**References:** [cordasco2010community](../../references.html#cordasco2010community), [raghavan2007near](../../references.html#raghavan2007near), [traag2023large](../../references.html#traag2023large)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)

## Cnx label propagation {#cnx_label_propagation}

Measure id: `cnx_label_propagation`. Original family: Communities.

**Definition.** Cnx label propagation.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_label_propagation</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.community.label_propagation_communities(G) on the simple undirected graph</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Seeded labels {#cnx_seeded_labels}

Measure id: `cnx_seeded_labels`. Original family: Communities.

**Definition.** Seeded labels.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_seeded_labels</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>per node: community index under asyn_lpa_communities and fast_label_propagation_communities (simple graph), and asyn_fluidc(k = min(3, n)) on the simple undirected graph (-1 if not connected), each with seed=random.Random(7)</code></td><td></td></tr><tr><td><code>nx_seeded_labels_valid</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>the same checks on NetworkX's communities</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
