---
title: "Eulerian circuits and paths"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Eulerian circuits and paths {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Eulerian paths, Hamiltonian paths and tours. Concept id: `eulerian`. 4 measures.

## Definition {#concept-definition}

Eulerian circuits and paths. Entries grouped here: Eulerian circuits and paths; Euler; Euler circuit; Is eulerian.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#eulerian">Eulerian circuits and paths</a></td><td><code>eulerian</code></td><td>1</td></tr><tr><td><a href="#nxs_euler">Euler</a></td><td><code>nxs_euler</code></td><td>2</td></tr><tr><td><a href="#nxs_euler_circuit">Euler circuit</a></td><td><code>nxs_euler_circuit</code></td><td>1</td></tr><tr><td><a href="#gb_is_eulerian">Is eulerian</a></td><td><code>gb_is_eulerian</code></td><td>1</td></tr></tbody></table></div>

## Eulerian circuits and paths {#eulerian}

Measure id: `eulerian`. Original family: Traversal, trees and DAGs.

**Definition.** Eulerian circuits and paths.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-eulerian-jgrapht">details</a></td><td><code>HierholzerEulerianCycle</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-eulerian-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: HierholzerEulerianCycle.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Euler {#nxs_euler}

Measure id: `nxs_euler`. Original family: Graph theory and combinatorics.

**Definition.** Euler.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-nxs_euler-networkx">details</a></td><td><code>eulerian_circuit; eulerian_path; eulerize; has_eulerian_path; is_eulerian; is_semieulerian</code></td><td>API listing</td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-nxs_euler-igraph">details</a></td><td><code>eulerian_cycle; eulerian_path; has_eulerian_cycle; has_eulerian_path</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxs_euler-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: eulerian\_circuit; eulerian\_path; eulerize; has\_eulerian\_path; is\_eulerian; is\_semieulerian.
- <a id="why-nxs_euler-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: eulerian\_cycle; eulerian\_path; has\_eulerian\_cycle; has\_eulerian\_path.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Euler circuit {#nxs_euler_circuit}

Measure id: `nxs_euler_circuit`. Original family: Graph theory and combinatorics.

**Definition.** Euler circuit.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxs_euler_circuit</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>list(nx.eulerian_circuit(G, source = 0, keys = True))</code></td><td>NetworkX refuses a graph that is not connected (or has no node)</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is eulerian {#gb_is_eulerian}

Measure id: `gb_is_eulerian`. Original family: Traversal, trees and DAGs.

**Definition.** Is eulerian.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_is_eulerian</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.is_eulerian(M)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
