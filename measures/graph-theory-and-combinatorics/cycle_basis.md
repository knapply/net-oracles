---
title: "Cycle basis"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Cycle basis {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `cycle_basis`. 3 measures.

## Definition {#concept-definition}

Cycle basis. Entries grouped here: Cycle basis; Basis; Nxs cycle basis.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cycle_basis">Cycle basis</a></td><td><code>cycle_basis</code></td><td>3</td></tr><tr><td><a href="#basis">Basis</a></td><td><code>basis</code></td><td>1</td></tr><tr><td><a href="#nxs_cycle_basis">Nxs cycle basis</a></td><td><code>nxs_cycle_basis</code></td><td>1</td></tr></tbody></table></div>

## Cycle basis {#cycle_basis}

Measure id: `cycle_basis`. Original family: Graph theory and combinatorics.

**Definition.** Cycle basis.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges and self-loops): NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the... <a href="#why-cycle_basis-networkx">details</a></td><td><code>cycle_basis</code></td><td></td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cycle_basis-rustworkx">details</a></td><td><code>cycle_basis</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cycle_basis-jgrapht">details</a></td><td><code>PatonCycleBase; QueueBFSFundamentalCycleBasis; StackBFSFundamentalCycleBasis</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cycle_basis-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and self-loops) on inputs tagged multi\_edges. NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the multigraph has m - n + c cycles). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 18 agree.
- <a id="why-cycle_basis-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: cycle\_basis.
- <a id="why-cycle_basis-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: PatonCycleBase; QueueBFSFundamentalCycleBasis; StackBFSFundamentalCycleBasis.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cyc_basis</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>multi_edges</td><td>multi_edges, self_loops</td><td>abs 0, rel 0</td><td><code>nx.cycle_basis(G), cycle for cycle, in order</code></td><td>NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the multigraph has m - n + c cycles).</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx)

## Basis {#basis}

Measure id: `basis`. Original family: Graph theory and combinatorics.

**Definition.** Basis.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (multi-edges): as for cyc_basis. <a href="#why-basis-networkx">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-basis-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges) on inputs tagged multi\_edges. as for cyc\_basis. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 18 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cyc_basis_check</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>the count and the cycle/independence tests of nx.cycle_basis(G)</code></td><td>as for cyc_basis</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nxs cycle basis {#nxs_cycle_basis}

Measure id: `nxs_cycle_basis`. Original family: Graph theory and combinatorics.

**Definition.** Nxs cycle basis.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxs_cycle_basis</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.cycle_basis(G) on the simple graph, in its order</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
