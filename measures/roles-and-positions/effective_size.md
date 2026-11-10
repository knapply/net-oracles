---
title: "Effective size"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Effective size {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `effective_size`. 1 measure.

## Definition {#concept-definition}

Effective size. Entries grouped here: Effective size.

*Definition not yet written.*

## Effective size {#effective_size}

Measure id: `effective_size`. Original family: Roles and positions.

**Definition.** Effective size.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (self-loops, ties and weights): NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. <a href="#why-effective_size-networkx">details</a></td><td><code>effective_size</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-effective_size-ucinet">details</a></td><td><code>structuralholes</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/manynet.html">manynet</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... <em>(reason incomplete)</em> <a href="#why-effective_size-manynet">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-effective_size-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (self-loops, ties and weights) on inputs tagged loops. effective\_size: NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. This reference ignores loops. effective\_size\_weighted: Burt's effective size counts a node's neighbours; NetworkX's weighted formula also counts a neighbour's self-loop as redundancy (0.5 for node 0 of 1-0 plus a loop at 1, against 1). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 2 comparisons differ and 33 agree. Finding F025 (defect): effective\_size is wrong for weighted or directed graphs on its vectorized path. Findings: [F025](../../findings.html#f025).
- <a id="why-effective_size-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-effective_size-manynet"></a>**[manynet](../../tools/manynet.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> manynet 2.4.0 was run and its value differs from the reference value by convention (defaults, direction, multi-edges, normalization, self-loops and ties) on inputs tagged directed, edge\_case, loops and multi\_edges. manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree. Relation to the reference value: Directed input, multigraphs: the values differ from the reference value's on directed networks and on multigraphs with loops (half the reference value's on a directed cycle), cause not traced; simple undirected networks agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 8 comparisons differ and 20 agree. Finding F082 (defect): Effective size and efficiency differ on directed networks and multigraphs with loops. Findings: [F082](../../findings.html#f082). **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>effective_size</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.effective_size(MultiGraph | MultiDiGraph)</code></td><td>NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. This reference ignores loops.</td></tr><tr><td><code>effective_size</code></td><td>manynet</td><td>any</td><td>differs</td><td>directed, edge_case, loops, multi_edges</td><td>defaults, direction, multi_edges, normalization, self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>manynet::node_effsize(g) (node_by_effsize in newer versions)</code></td><td>manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree.</td></tr><tr><td><code>effective_size_weighted</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>self_loops, weights</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.effective_size(G, weight = 'weight')</code></td><td>Burt's effective size counts a node's neighbours; NetworkX's weighted formula also counts a neighbour's self-loop as redundancy (0.5 for node 0 of 1-0 plus a loop at 1, against 1).</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f025">F025</a></td><td>NetworkX</td><td>defect</td><td>effective_size is wrong for weighted or directed graphs on its vectorized path</td></tr><tr><td><a href="../../findings.html#f082">F082</a></td><td>manynet</td><td>defect</td><td>Effective size and efficiency differ on directed networks and multigraphs with loops</td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_manynet](../../references.html#tool_manynet)
{% endraw %}
