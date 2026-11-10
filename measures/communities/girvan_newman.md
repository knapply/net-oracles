---
title: "Girvan-Newman edge removal"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Girvan-Newman edge removal {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `girvan_newman`. 5 measures.

## Definition {#concept-definition}

Girvan-Newman clustering by removing the edge of highest betweenness one at a time; returns the best level, its modularity, the removal order and the modularity path.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#girvan_newman">Girvan newman</a></td><td><code>girvan_newman</code></td><td>5</td></tr><tr><td><a href="#cnx_current_flow">Cnx current flow</a></td><td><code>cnx_current_flow</code></td><td>1</td></tr><tr><td><a href="#cnx_edge_betweenness">Cnx edge betweenness</a></td><td><code>cnx_edge_betweenness</code></td><td>1</td></tr><tr><td><a href="#cnx_girvan_newman">Cnx girvan newman</a></td><td><code>cnx_girvan_newman</code></td><td>1</td></tr><tr><td><a href="#girvan_newman_cut">Girvan newman cut</a></td><td><code>girvan_newman_cut</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[girvan2002community](../../references.html#girvan2002community), [brandes2005centrality](../../references.html#brandes2005centrality), [brandes2001faster](../../references.html#brandes2001faster), [chen2014extension](../../references.html#chen2014extension), [clauset2004finding](../../references.html#clauset2004finding), [cordasco2010community](../../references.html#cordasco2010community), [fortunato2010community](../../references.html#fortunato2010community), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kernighan1970efficient](../../references.html#kernighan1970efficient)

## Girvan newman {#girvan_newman}

Measure id: `girvan_newman`. Original family: Communities.

**Definition.** Girvan-Newman clustering by removing the edge of highest betweenness one at a time; returns the best level, its modularity, the removal order and the modularity path.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>edge_betweenness_partition; girvan_newman</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cluster_edge_betweenness</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-girvan_newman-pyigraph">details</a></td><td><code>community_edge_betweenness</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-girvan_newman-jgrapht">details</a></td><td><code>GirvanNewmanClustering</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-girvan_newman-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-girvan_newman-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_edge\_betweenness.
- <a id="why-girvan_newman-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GirvanNewmanClustering.
- <a id="why-girvan_newman-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>girvan_newman</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>max of nx.community.modularity over nx.community.girvan_newman(simple graph)</code></td><td></td></tr><tr><td><code>girvan_newman</code></td><td>igraph (R)</td><td>undirected</td><td>differs</td><td>symmetric_nodes</td><td>ties</td><td>abs 1e-14, rel 1e-12</td><td><code>max(modularity(cluster_edge_betweenness(simplify(g), weights = NULL)))</code></td><td>Edges of exactly equal betweenness (symmetric positions) are removed in a different order, igraph by its own rule, the reference by edge index, so the dendrograms and their best levels can differ.</td></tr><tr><td><code>girvan_newman_membership</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>edgeless</td><td>defaults</td><td>abs 0, rel 0</td><td><code>the first partition of highest modularity among the components and the partitions of nx.community.girvan_newman(simple graph)</code></td><td>Without edges: the reference returns no membership level for the null graph and the singletons otherwise, the NetworkX oracle one value for the empty level.</td></tr></tbody></table></div>

**References:** [girvan2002community](../../references.html#girvan2002community)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Cnx current flow {#cnx_current_flow}

Measure id: `cnx_current_flow`. Original family: Communities.

**Definition.** Component labels after removing the edges of largest current-flow betweenness until at least k components exist (NetworkX's edge current-flow partition).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (ties): Edges whose current-flow betweenness ties in exact arithmetic (symmetric positions) differ in the last digits. <a href="#why-cnx_current_flow-networkx">details</a></td><td><code>edge_current_flow_betweenness_partition</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cnx_current_flow-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (ties) on inputs tagged symmetric\_nodes. Edges whose current-flow betweenness ties in exact arithmetic (symmetric positions) differ in the last digits; NetworkX removes the one its rounding and dict order rank first, the reference the first in edge order. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 4 comparisons differ and 24 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_edge_current_flow_partition</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>symmetric_nodes</td><td>ties</td><td>abs 0, rel 0</td><td><code>nx.community.edge_current_flow_betweenness_partition(G, 3) on the simple undirected graph (-1 when n &lt; 3)</code></td><td>Edges whose current-flow betweenness ties in exact arithmetic (symmetric positions) differ in the last digits; NetworkX removes the one its rounding and dict order rank first, the reference the first in edge order.</td></tr></tbody></table></div>

**References:** [brandes2005centrality](../../references.html#brandes2005centrality)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Cnx edge betweenness {#cnx_edge_betweenness}

Measure id: `cnx_edge_betweenness`. Original family: Communities.

**Definition.** Component labels after removing the most central edges one at a time until at least k components exist (NetworkX's edge betweenness partition).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_edge_betweenness_partition</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.community.edge_betweenness_partition(G, 3) on the simple undirected graph (-1 when n &lt; 3)</code></td><td></td></tr></tbody></table></div>

**References:** [brandes2001faster](../../references.html#brandes2001faster), [chen2014extension](../../references.html#chen2014extension), [clauset2004finding](../../references.html#clauset2004finding), [cordasco2010community](../../references.html#cordasco2010community), [fortunato2010community](../../references.html#fortunato2010community), [girvan2002community](../../references.html#girvan2002community), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kernighan1970efficient](../../references.html#kernighan1970efficient)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Cnx girvan newman {#cnx_girvan_newman}

Measure id: `cnx_girvan_newman`. Original family: Communities.

**Definition.** Cnx girvan newman.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_girvan_newman</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>itertools.islice(nx.community.girvan_newman(G), 3)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Girvan newman cut {#girvan_newman_cut}

Measure id: `girvan_newman_cut`. Original family: Communities.

**Definition.** Girvan newman cut.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>girvan_newman_cut3</code></td><td>igraph (R)</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected, (no value) edge_case, (no value) loops, (no value) multi_edges</td><td>defaults, multi_edges, self_loops</td><td>abs 0, rel 0</td><td><code>cut_at(cluster_edge_betweenness(simplify(g), weights = NULL), no = 3)</code></td><td>the R oracle simplifies the network, so multigraphs and networks with loops are not comparable; disconnected and trivial networks give dendrograms that cannot be cut at 3 groups in one tool or the other</td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
