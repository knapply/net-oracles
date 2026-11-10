---
title: "Minimum-cost flow"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum-cost flow {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Flows and flow trees. Concept id: `min_cost_flow`. 4 measures.

## Definition {#concept-definition}

A maximum flow of least cost between two nodes, with its value.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma">Ahuja Orlin Sharma Cyclic Exchange Local Augmentation</a></td><td><code>cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma</code></td><td>1</td></tr><tr><td><a href="#cat_capacity_cost_flow_minimum_scaling">Capacity Scaling Minimum Cost Flow</a></td><td><code>cat_capacity_cost_flow_minimum_scaling</code></td><td>1</td></tr><tr><td><a href="#max_flow_min_cost">Max flow min cost</a></td><td><code>max_flow_min_cost</code></td><td>2</td></tr><tr><td><a href="#gb_mincost">Mincost</a></td><td><code>gb_mincost</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[ahuja1993network](../../references.html#ahuja1993network), [cunningham1976network](../../references.html#cunningham1976network), [dantzig1951application](../../references.html#dantzig1951application), [grigoriadis1986efficient](../../references.html#grigoriadis1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Ahuja Orlin Sharma Cyclic Exchange Local Augmentation {#cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma}

Measure id: `cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma`. Original family: Graph theory and combinatorics.

**Definition.** Ahuja Orlin Sharma Cyclic Exchange Local Augmentation.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma-jgrapht">details</a></td><td><code>AhujaOrlinSharmaCyclicExchangeLocalAugmentation</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: AhujaOrlinSharmaCyclicExchangeLocalAugmentation.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Capacity Scaling Minimum Cost Flow {#cat_capacity_cost_flow_minimum_scaling}

Measure id: `cat_capacity_cost_flow_minimum_scaling`. Original family: Components and connectivity.

**Definition.** Capacity Scaling Minimum Cost Flow.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_capacity_cost_flow_minimum_scaling-jgrapht">details</a></td><td><code>CapacityScalingMinimumCostFlow</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_capacity_cost_flow_minimum_scaling-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: CapacityScalingMinimumCostFlow.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Max flow min cost {#max_flow_min_cost}

Measure id: `max_flow_min_cost`. Original family: Components and connectivity.

**Definition.** A maximum flow of least cost between two nodes, with its value.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cost_of_flow; max_flow_min_cost; min_cost_flow; min_cost_flow_cost; network_simplex</code></td><td></td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-max_flow_min_cost-boost">details</a></td><td><code>cycle_canceling; successive_shortest_path_nonnegative_weights</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-max_flow_min_cost-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: cycle\_canceling; successive\_shortest\_path\_nonnegative\_weights.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>flow_max_flow_min_cost</code></td><td>NetworkX</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td>weights</td><td>abs 1e-09, rel 1e-09</td><td><code>F = nx.maximum_flow_value(G, 0, n - 1); nx.min_cost_flow_cost(M) on the multigraph M with demand -F at 0 and F at n - 1</code></td><td>NetworkX's network simplex reports this real-valued problem infeasible (NetworkXUnfeasible): its documentation warns that it may fail on floating-point capacities and suggests integers. The linear program of the definition oracle confirms the reference value's value and cost.</td></tr></tbody></table></div>

**References:** [ahuja1993network](../../references.html#ahuja1993network), [cunningham1976network](../../references.html#cunningham1976network), [dantzig1951application](../../references.html#dantzig1951application), [grigoriadis1986efficient](../../references.html#grigoriadis1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost)

## Mincost {#gb_mincost}

Measure id: `gb_mincost`. Original family: Traversal, trees and DAGs.

**Definition.** Mincost.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_mincost</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.network_simplex(M) with demand -1 at 0 and 1 at n - 1</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
