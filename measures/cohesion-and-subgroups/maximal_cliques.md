---
title: "Maximal cliques"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximal cliques {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cliques. Concept id: `maximal_cliques`. 2 measures.

## Definition {#concept-definition}

Every maximal clique with at least min\_size members, in lexicographic order.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_clique_detect">Clique Detect</a></td><td><code>cat_clique_detect</code></td><td>1</td></tr><tr><td><a href="#max_cliques">Max cliques</a></td><td><code>max_cliques</code></td><td>9</td></tr></tbody></table></div>

## References {#concept-references}

[bron1973algorithm](../../references.html#bron1973algorithm), [eppstein2010listing](../../references.html#eppstein2010listing), [matula1983smallest](../../references.html#matula1983smallest), [tomita2006worst](../../references.html#tomita2006worst)

## Clique Detect {#cat_clique_detect}

Measure id: `cat_clique_detect`. Original family: Cohesion and subgroups.

**Definition.** Clique Detect.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_clique_detect-networkit">details</a></td><td><code>CliqueDetect</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clique_detect-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: CliqueDetect.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Max cliques {#max_cliques}

Measure id: `max_cliques`. Original family: Cohesion and subgroups.

**Definition.** Every maximal clique with at least min\_size members, in lexicographic order.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>enumerate_all_cliques; find_cliques; find_cliques_recursive</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>clique_size_counts; cliques; largest_cliques; max_cliques</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cliques; largest_cliques; maximal_cliques</code></td><td></td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-max_cliques-graphtool">details</a></td><td><code>max_cliques</code></td><td>API listing</td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>MaximalCliques</code></td><td></td></tr><tr><td><a href="../../tools/sknetwork.html">scikit-network</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-max_cliques-sknetwork">details</a></td><td><code>count_cliques</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>BronKerboschCliqueFinder; DegeneracyBronKerboschCliqueFinder; PivotBronKerboschCliqueFinder</code></td><td></td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-max_cliques-boost">details</a></td><td><code>bron_kerbosch_all_cliques</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-max_cliques-ucinet">details</a></td><td><code>cliqueoverlap; cliques</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-max_cliques-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: max\_cliques.
- <a id="why-max_cliques-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: count\_cliques.
- <a id="why-max_cliques-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: bron\_kerbosch\_all\_cliques.
- <a id="why-max_cliques-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>max_cliques</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.find_cliques(nx.Graph(G)) (undirected simple projection; find_cliques rejects directed graphs and ignores loops)</code></td><td></td></tr><tr><td><code>max_cliques</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::max_cliques(g) (ignores directions, loops, and parallel edges)</code></td><td></td></tr><tr><td><code>max_cliques</code></td><td>igraph (Python)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: [tuple(sorted(c)) for c in g.maximal_cliques(min=0)]</code></td><td></td></tr><tr><td><code>max_cliques</code></td><td>NetworKit</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nk.clique.MaximalCliques(G simple undirected).getCliques()</code></td><td></td></tr><tr><td><code>max_cliques</code></td><td>JGraphT</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) directed, (no value) loops, (no value) multi_edges</td><td>direction, multi_edges, self_loops</td><td>abs 0, rel 0</td><td><code>JGraphT 1.5.2: new BronKerboschCliqueFinder&lt;&gt;(g) on a pseudograph</code></td><td>BronKerboschCliqueFinder throws 'Graph must be simple' on loops or parallel edges; on directed input it does not error but returns a collection that is not the maximal cliques of the underlying graph (pair 0-&gt;1 gives two singletons, cycle7_dir six cliques instead of seven edges), so it is not compared.</td></tr><tr><td><code>max_cliques_min3</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>[c for c in nx.find_cliques(nx.Graph(G)) if len(c) &gt;= 3]</code></td><td></td></tr><tr><td><code>max_cliques_min3</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::max_cliques(g, min = 3)</code></td><td></td></tr><tr><td><code>max_cliques_min3</code></td><td>igraph (Python)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: [tuple(sorted(c)) for c in g.maximal_cliques(min=3)]</code></td><td></td></tr><tr><td><code>max_cliques_min3</code></td><td>NetworKit</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nk.clique.MaximalCliques(G simple undirected).getCliques(), size &gt;= 3</code></td><td></td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f066">F066</a></td><td>NetworKit</td><td>convention</td><td>MaximalCliques omits a node without edges</td></tr></tbody></table></div>

**References:** [bron1973algorithm](../../references.html#bron1973algorithm), [eppstein2010listing](../../references.html#eppstein2010listing), [matula1983smallest](../../references.html#matula1983smallest), [tomita2006worst](../../references.html#tomita2006worst)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
