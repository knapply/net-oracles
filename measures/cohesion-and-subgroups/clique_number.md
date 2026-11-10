---
title: "Clique number"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Clique number {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cliques. Concept id: `clique_number`. 2 measures.

## Definition {#concept-definition}

Size of the largest clique.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#clique_number">Clique number</a></td><td><code>clique_number</code></td><td>5</td></tr><tr><td><a href="#node_clique_number">Node clique number</a></td><td><code>node_clique_number</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[bron1973algorithm](../../references.html#bron1973algorithm), [eppstein2010listing](../../references.html#eppstein2010listing), [matula1983smallest](../../references.html#matula1983smallest), [tomita2006worst](../../references.html#tomita2006worst)

## Clique number {#clique_number}

Measure id: `clique_number`. Original family: Cohesion and subgroups.

**Definition.** Size of the largest clique.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>max_clique; max_weight_clique; node_clique_number; number_of_cliques</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>clique_num; weighted_clique_num</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>clique_number</code></td><td></td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>clique_number</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>max(len(c) for c in nx.find_cliques(nx.Graph(G)))</code></td><td></td></tr><tr><td><code>clique_number</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::clique_num(g)</code></td><td></td></tr><tr><td><code>clique_number</code></td><td>igraph (Python)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>python-igraph: [g.clique_number()]</code></td><td></td></tr><tr><td><code>clique_number</code></td><td>NetworKit</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>max size in nk.clique.MaximalCliques(G simple undirected).getCliques()</code></td><td></td></tr><tr><td><code>clique_number</code></td><td>JGraphT</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) directed, (no value) loops, (no value) multi_edges</td><td>direction, multi_edges, self_loops</td><td>abs 0, rel 0</td><td><code>JGraphT 1.5.2: size of the largest BronKerboschCliqueFinder clique on a pseudograph</code></td><td>BronKerboschCliqueFinder throws 'Graph must be simple' on loops or parallel edges; on directed input it does not error but returns a collection that is not the maximal cliques of the underlying graph (pair 0-&gt;1 gives two singletons, cycle7_dir six cliques instead of seven edges), so it is not compared.</td></tr></tbody></table></div>

**References:** [bron1973algorithm](../../references.html#bron1973algorithm), [eppstein2010listing](../../references.html#eppstein2010listing), [matula1983smallest](../../references.html#matula1983smallest), [tomita2006worst](../../references.html#tomita2006worst)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit)

## Node clique number {#node_clique_number}

Measure id: `node_clique_number`. Original family: Cohesion and subgroups.

**Definition.** Node clique number.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>node_clique_number</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.node_clique_number(G)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
