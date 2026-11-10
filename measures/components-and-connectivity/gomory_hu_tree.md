---
title: "Gomory-Hu and equivalent-flow trees"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Gomory-Hu and equivalent-flow trees {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Flows and flow trees. Concept id: `gomory_hu_tree`. 3 measures.

## Definition {#concept-definition}

The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#gomory_hu">Gomory hu</a></td><td><code>gomory_hu</code></td><td>3</td></tr><tr><td><a href="#gomory_hu_values">Gomory hu values</a></td><td><code>gomory_hu_values</code></td><td>1</td></tr><tr><td><a href="#cat_equivalent_flow_gusfield_tree">Gusfield Equivalent Flow Tree</a></td><td><code>cat_equivalent_flow_gusfield_tree</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Gomory hu {#gomory_hu}

Measure id: `gomory_hu`. Original family: Components and connectivity.

**Definition.** The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>gomory_hu_tree</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gomory_hu-pyigraph">details</a></td><td><code>gomory_hu_tree</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gomory_hu-jgrapht">details</a></td><td><code>GusfieldGomoryHuCutTree</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gomory_hu-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: gomory\_hu\_tree.
- <a id="why-gomory_hu-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GusfieldGomoryHuCutTree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>flow_gomory_hu_tree</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.gomory_hu_tree(G, capacity = 'capacity').edges(data = 'weight'), as (u, v, weight) with u &lt; v</code></td><td></td></tr></tbody></table></div>

**References:** [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Gomory hu values {#gomory_hu_values}

Measure id: `gomory_hu_values`. Original family: Components and connectivity.

**Definition.** The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>flow_gomory_hu_values</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.minimum_cut_value(G, u, v) for every pair u &lt; v</code></td><td></td></tr></tbody></table></div>

**References:** [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Gusfield Equivalent Flow Tree {#cat_equivalent_flow_gusfield_tree}

Measure id: `cat_equivalent_flow_gusfield_tree`. Original family: Components and connectivity.

**Definition.** Gusfield Equivalent Flow Tree.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_equivalent_flow_gusfield_tree-jgrapht">details</a></td><td><code>GusfieldEquivalentFlowTree</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_equivalent_flow_gusfield_tree-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GusfieldEquivalentFlowTree.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
