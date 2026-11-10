---
title: "Approximate node connectivity"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Approximate node connectivity {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connectivity numbers. Concept id: `node_connectivity`. 1 measure.

## Definition {#concept-definition}

Approximate node connectivity of the whole network by greedy node-disjoint shortest paths.

*Definition not yet written.*

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Node connectivity {#ap_node_connectivity}

Measure id: `ap_node_connectivity`. Original family: Graph theory and combinatorics.

**Definition.** Approximate node connectivity of the whole network by greedy node-disjoint shortest paths.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>ap_node_connectivity</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.approximation.node_connectivity(G_sorted)</code></td><td></td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f031">F031</a></td><td>NetworkX</td><td>defect</td><td>approximation.node_connectivity starts from a bound that can exceed the connectivity</td></tr></tbody></table></div>

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
