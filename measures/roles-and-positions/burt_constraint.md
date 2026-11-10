---
title: "Burt constraint"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Burt constraint {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `burt_constraint`. 1 measure.

## Definition {#concept-definition}

Burt constraint. Entries grouped here: Constraint.

*Definition not yet written.*

## Constraint {#constraint}

Measure id: `constraint`. Original family: Roles and positions.

**Definition.** Constraint.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults, self-loops, ties and weights): NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's total tie volume and lowers every p_ij. <a href="#why-constraint-networkx">details</a></td><td><code>constraint; local_constraint</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>constraint</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>constraint</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-constraint-ucinet">details</a></td><td><code>constraint</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/manynet.html">manynet</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-constraint-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults, self-loops, ties and weights) on inputs tagged loops. constraint: NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's total tie volume and lowers every p\_ij. Burt's measure concerns ties to others; this reference and igraph ignore loops. constraint\_weighted: A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference value and the definition oracle; NetworkX counts the loop as a tie to itself (4 for one loop of weight 2). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 2 comparisons differ and 33 agree.
- <a id="why-constraint-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>constraint</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.constraint(MultiGraph | MultiDiGraph)</code></td><td>NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's total tie volume and lowers every p_ij. Burt's measure concerns ties to others; this reference and igraph ignore loops.</td></tr><tr><td><code>constraint</code></td><td>igraph (R)</td><td>any</td><td>differs</td><td>loops</td><td>defaults, self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>igraph::constraint(g) on a copy without the weight attribute</code></td><td>A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; igraph reports 0.</td></tr><tr><td><code>constraint</code></td><td>igraph (Python)</td><td>any</td><td>differs</td><td>loops</td><td>defaults, self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>python-igraph: gu.constraint()</code></td><td>A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; python-igraph reports 0.</td></tr><tr><td><code>constraint</code></td><td>manynet</td><td>any</td><td>differs</td><td>isolates</td><td>defaults, self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>manynet::node_constraint(g) (node_by_constraint in newer versions)</code></td><td>A node without ties to other nodes (one whose only tie is a self-loop) has undefined constraint for the reference and the definition oracle; manynet reports 0.</td></tr><tr><td><code>constraint_weighted</code></td><td>NetworkX</td><td>any</td><td>differs</td><td>loops</td><td>defaults, self_loops, ties, weights</td><td>abs 1e-12, rel 1e-12</td><td><code>nx.constraint(G, weight = 'weight')</code></td><td>A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; NetworkX counts the loop as a tie to itself (4 for one loop of weight 2).</td></tr><tr><td><code>constraint_weighted</code></td><td>igraph (R)</td><td>any</td><td>differs</td><td>loops</td><td>defaults, self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>igraph::constraint(g, weights = E(g)$weight)</code></td><td>A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; igraph reports 0.</td></tr><tr><td><code>constraint_weighted</code></td><td>igraph (Python)</td><td>any</td><td>differs</td><td>loops</td><td>defaults, self_loops, ties</td><td>abs 1e-12, rel 1e-12</td><td><code>python-igraph: g.constraint(weights=w)</code></td><td>A node whose only tie is a self-loop has no neighbours, so Burt's constraint is undefined for the reference and the definition oracle; python-igraph reports 0.</td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_manynet](../../references.html#tool_manynet)
{% endraw %}
