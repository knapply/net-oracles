---
title: "Reciprocity"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Reciprocity {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Reciprocity, dyad and triad census. Concept id: `reciprocity`. 2 measures.

## Definition {#concept-definition}

Reciprocity. Entries grouped here: Reciprocity; Node reciprocity.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#reciprocity">Reciprocity</a></td><td><code>reciprocity</code></td><td>8</td></tr><tr><td><a href="#nxo_node_reciprocity">Node reciprocity</a></td><td><code>nxo_node_reciprocity</code></td><td>3</td></tr></tbody></table></div>

## Reciprocity {#reciprocity}

Measure id: `reciprocity`. Original family: Descriptive statistics.

**Definition.** Reciprocity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>overall_reciprocity; reciprocity</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>reciprocity</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>reciprocity</code></td><td></td></tr><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults, direction and ties): On a two-node network with one arc the two ordered pairs give the perfectly anticorrelated values (1, 0) and (0, 1), so the correlation is -1, as... <a href="#why-reciprocity-sna">details</a></td><td><code>grecip; mutuality</code></td><td></td></tr><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>mutual</code></td><td></td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-reciprocity-graphtool">details</a></td><td><code>edge_reciprocity</code></td><td>API listing</td></tr><tr><td><a href="../../tools/graphblas.html">GraphBLAS algorithms</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-reciprocity-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-reciprocity-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (defaults, direction and ties) on inputs tagged edge\_case. On a two-node network with one arc the two ordered pairs give the perfectly anticorrelated values (1, 0) and (0, 1), so the correlation is -1, as the definition oracle confirms; sna reports 0. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (reciprocity) on the fixtures empty: The ratio is 0 / 0 without arcs; not compared. No value (reciprocity\_ratio) on the fixtures empty: The ratio is 0 / 0 without arcs; not compared. 1 comparisons differ and 55 agree. Finding F044 (convention): Reciprocity correlation is 0 on a single arc. Findings: [F044](../../findings.html#f044).
- <a id="why-reciprocity-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: edge\_reciprocity.
- <a id="why-reciprocity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>reciprocity</code></td><td>NetworkX</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nx.overall_reciprocity(DiGraph without self-loops)</code></td><td>NetworkX raises for a graph without edges, where the ratio is 0 / 0.</td></tr><tr><td><code>reciprocity</code></td><td>igraph (R)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction</td><td>abs 0, rel 1e-14</td><td><code>igraph::reciprocity(igraph::simplify(g), mode = 'default')</code></td><td>The ratio is 0 / 0 without arcs; not compared.</td></tr><tr><td><code>reciprocity</code></td><td>igraph (Python)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction</td><td>abs 0, rel 1e-14</td><td><code>python-igraph: [simple.reciprocity(mode="default")] if simple.ecount() else None</code></td><td>The ratio is 0 / 0 without arcs; not compared.</td></tr><tr><td><code>reciprocity</code></td><td>sna</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction</td><td>abs 0, rel 1e-14</td><td><code>sna::grecip(m with its diagonal set to 0, measure = 'edgewise')</code></td><td>The ratio is 0 / 0 without arcs; not compared.</td></tr><tr><td><code>reciprocity</code></td><td>ergm (statnet)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>ties</td><td>abs 0, rel 1e-14</td><td><code>2 * summary(nw ~ mutual) / summary(nw ~ edges)</code></td><td>A network without ties has no reciprocity.</td></tr><tr><td><code>reciprocity</code></td><td>GraphBLAS algorithms</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>defaults</td><td>abs 0, rel 1e-14</td><td><code>nx.overall_reciprocity(DiGraph without loops, backend = 'graphblas')</code></td><td>As in NetworkX, overall_reciprocity raises 'Not defined for empty graphs'.</td></tr><tr><td><code>reciprocity_correlation</code></td><td>sna</td><td>directed</td><td>differs</td><td>edge_case</td><td>defaults, direction, ties</td><td>abs 1e-14, rel 1e-12</td><td><code>sna::grecip(m with its diagonal set to 0, measure = 'correlation')</code></td><td>On a two-node network with one arc the two ordered pairs give the perfectly anticorrelated values (1, 0) and (0, 1), so the correlation is -1, as the definition oracle confirms; sna reports 0. Every tie between distinct nodes is absent (or present), so the correlation is 0 / 0. This reference reports NaN; sna defines it as 1. Not compared.</td></tr><tr><td><code>reciprocity_dyadic</code></td><td>sna</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>sna::grecip(m with its diagonal set to 0, measure = 'dyadic')</code></td><td></td></tr><tr><td><code>reciprocity_ratio</code></td><td>igraph (R)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction</td><td>abs 0, rel 1e-14</td><td><code>igraph::reciprocity(igraph::simplify(g), mode = 'ratio')</code></td><td>The ratio is 0 / 0 without arcs; not compared.</td></tr><tr><td><code>reciprocity_ratio</code></td><td>igraph (Python)</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction</td><td>abs 0, rel 1e-14</td><td><code>python-igraph: [simple.reciprocity(mode="ratio")] if simple.ecount() else None</code></td><td>The ratio is 0 / 0 without arcs; not compared.</td></tr><tr><td><code>reciprocity_ratio</code></td><td>sna</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>direction</td><td>abs 0, rel 1e-14</td><td><code>sna::grecip(m with its diagonal set to 0, measure = 'dyadic.nonnull')</code></td><td>The ratio is 0 / 0 without arcs; not compared.</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f044">F044</a></td><td>sna</td><td>convention</td><td>Reciprocity correlation is 0 on a single arc</td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Node reciprocity {#nxo_node_reciprocity}

Measure id: `nxo_node_reciprocity`. Original family: Descriptive statistics.

**Definition.** Node reciprocity.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/graphblas.html">GraphBLAS algorithms</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-nxo_node_reciprocity-ucinet">details</a></td><td><code>Reciprocity (arc vs dyad question has its own FAQ), normalized reciprocity (6.834); indrecip</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxo_node_reciprocity-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxo_node_reciprocity</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.reciprocity(nx.DiGraph(G), nodes = every node)</code></td><td></td></tr><tr><td><code>nxo_node_reciprocity</code></td><td>GraphBLAS algorithms</td><td>directed</td><td>differs</td><td>multi_edges</td><td>direction, multi_edges, weights</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.reciprocity(DiGraph, nodes, backend = 'graphblas')</code></td><td>graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge.</td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
