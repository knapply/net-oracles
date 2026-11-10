---
title: "Hamiltonian paths and cycles"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Hamiltonian paths and cycles {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Eulerian paths, Hamiltonian paths and tours. Concept id: `hamiltonian`. 2 measures.

## Definition {#concept-definition}

Hamiltonian paths and cycles. Entries grouped here: Hampath; Palmer Hamiltonian Cycle.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#st_hampath">Hampath</a></td><td><code>st_hampath</code></td><td>1</td></tr><tr><td><a href="#cat_cycle_hamiltonian_palmer">Palmer Hamiltonian Cycle</a></td><td><code>cat_cycle_hamiltonian_palmer</code></td><td>1</td></tr></tbody></table></div>

## Hampath {#st_hampath}

Measure id: `st_hampath`. Original family: Graph theory and combinatorics.

**Definition.** Hampath.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>hamiltonian_path</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>st_hampath</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.tournament.hamiltonian_path(G) on the simple digraph</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Palmer Hamiltonian Cycle {#cat_cycle_hamiltonian_palmer}

Measure id: `cat_cycle_hamiltonian_palmer`. Original family: Traversal, trees and DAGs.

**Definition.** Palmer Hamiltonian Cycle.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_cycle_hamiltonian_palmer-jgrapht">details</a></td><td><code>PalmerHamiltonianCycle</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_cycle_hamiltonian_palmer-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: PalmerHamiltonianCycle.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
