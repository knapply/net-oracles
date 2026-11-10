---
title: "Triad census"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Triad census {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Reciprocity, dyad and triad census. Concept id: `triad_census`. 2 measures.

## Definition {#concept-definition}

The 16 triad counts in MAN order (Holland and Leinhardt), one value per triad type.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#triad_census">Triad census</a></td><td><code>triad_census</code></td><td>7</td></tr><tr><td><a href="#st_triads">Triads</a></td><td><code>st_triads</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[batagelj2001subquadratic](../../references.html#batagelj2001subquadratic), [holland1976local](../../references.html#holland1976local)

## Triad census {#triad_census}

Measure id: `triad_census`. Original family: Descriptive statistics.

**Definition.** The 16 triad counts in MAN order (Holland and Leinhardt), one value per triad type.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>triadic_census</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges and ties): igraph's triad census does not support multigraphs: parallel edges change its counts. <a href="#why-triad_census-igraph">details</a></td><td><code>triad_census</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges and ties): igraph's triad census does not support multigraphs: parallel edges change its counts. <a href="#why-triad_census-pyigraph">details</a></td><td><code>triad_census</code></td><td></td></tr><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults and direction): sna returns NaN for networks with fewer than three nodes, which have no triads. <a href="#why-triad_census-sna">details</a></td><td><code>triad.census; triad.classify</code></td><td></td></tr><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>triadcensus</code></td><td></td></tr><tr><td><a href="../../tools/rsiena.html">RSiena</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-triad_census-rsiena">details</a></td><td><code>TriadCensus</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-triad_census-ucinet">details</a></td><td><code>Triad census, dyad census, hierarchy; nodetriadcensus</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-triad_census-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (multi-edges and ties) on inputs tagged multi\_edges. igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 5 comparisons differ and 39 agree. Finding F039 (defect): Triad census on multigraphs differs from the definition. Findings: [F039](../../findings.html#f039).
- <a id="why-triad_census-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (Python) 1.0.0 was run and its value differs from the reference value by convention (multi-edges and ties) on inputs tagged multi\_edges. igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 6 comparisons differ and 47 agree.
- <a id="why-triad_census-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (defaults and direction) on inputs tagged edge\_case and undirected. sna returns NaN for networks with fewer than three nodes, which have no triads; this reference returns zero counts. For undirected graphs sna reports only the four undirected triad classes, while igraph and this reference report all 16 types with every edge treated as mutual. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 14 agree.
- <a id="why-triad_census-rsiena"></a>**[RSiena](../../tools/rsiena.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. RSiena 1.6.6 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (RSiena exported functions and help titles; effects from getEffects()); API names: TriadCensus.
- <a id="why-triad_census-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>triad_census</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>undirected, (no value) undirected</td><td>direction</td><td>abs 0, rel 0</td><td><code>nx.triadic_census(DiGraph(G))</code></td><td>NetworkX defines the triad census only for directed graphs. NetworkX's triadic_census accepts only directed graphs.</td></tr><tr><td><code>triad_census</code></td><td>igraph (R)</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, ties</td><td>abs 0, rel 0</td><td><code>igraph::triad_census(g)</code></td><td>igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once.</td></tr><tr><td><code>triad_census</code></td><td>igraph (Python)</td><td>any</td><td>differs</td><td>multi_edges</td><td>multi_edges, ties</td><td>abs 0, rel 0</td><td><code>python-igraph: list(g.triad_census()),</code></td><td>igraph's triad census does not support multigraphs: parallel edges change its counts. This reference, sna, and the definition oracle classify each dyad as tied or not, so parallel edges count once.</td></tr><tr><td><code>triad_census</code></td><td>sna</td><td>any</td><td>differs</td><td>edge_case, undirected, (no value) undirected</td><td>defaults, direction</td><td>abs 0, rel 0</td><td><code>sna::triad.census(m, mode = 'digraph')</code></td><td>sna returns NaN for networks with fewer than three nodes, which have no triads; this reference returns zero counts.</td></tr><tr><td><code>triad_census</code></td><td>ergm (statnet)</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td>direction</td><td>abs 0, rel 0</td><td><code>summary(nw ~ triadcensus(0:15))</code></td><td>The census is computed for directed networks with at least three nodes only.</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f039">F039</a></td><td>igraph (R)</td><td>defect</td><td>Triad census on multigraphs differs from the definition</td></tr></tbody></table></div>

**References:** [batagelj2001subquadratic](../../references.html#batagelj2001subquadratic), [holland1976local](../../references.html#holland1976local)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [ripley2026manual](../../references.html#ripley2026manual)

## Triads {#st_triads}

Measure id: `st_triads`. Original family: Graph theory and combinatorics.

**Definition.** Triads.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>st_triads</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.triadic_census(G), (G, even nodes), (G, [0]) on the MultiDiGraph</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
