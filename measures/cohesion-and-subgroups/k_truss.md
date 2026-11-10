---
title: "K-truss"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-truss {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cores, trusses and cohesive blocks. Concept id: `k_truss`. 2 measures.

## Definition {#concept-definition}

The k-truss: the edges in at least k - 2 triangles of the subgraph, and the nodes they touch.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#k_truss">K truss</a></td><td><code>k_truss</code></td><td>1</td></tr><tr><td><a href="#truss">Truss</a></td><td><code>truss</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

## K truss {#k_truss}

Measure id: `k_truss`. Original family: Cohesion and subgroups.

**Definition.** The k-truss: the edges in at least k - 2 triangles of the subgraph, and the nodes they touch.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>k_truss</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>k_truss_3_edges</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 3), G the simple undirected graph without loops: the fixture edges whose pair it keeps</code></td><td></td></tr><tr><td><code>k_truss_3_nodes</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 3), G the simple undirected graph without loops: its nodes</code></td><td></td></tr><tr><td><code>k_truss_4_edges</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 4), G the simple undirected graph without loops: the fixture edges whose pair it keeps</code></td><td></td></tr><tr><td><code>k_truss_4_nodes</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.k_truss(G, 4), G the simple undirected graph without loops: its nodes</code></td><td></td></tr></tbody></table></div>

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Truss {#truss}

Measure id: `truss`. Original family: Cohesion and subgroups.

**Definition.** Truss number of every edge: the largest k whose k-truss contains it.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>truss_numbers</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>the largest k with the edge in nx.k_truss(G, k), G the simple undirected graph without loops (0 for loops)</code></td><td></td></tr></tbody></table></div>

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
