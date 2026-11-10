---
title: "Lambda connectivity matrix"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lambda connectivity matrix {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `lambda_connectivity`. 1 measure.

## Definition {#concept-definition}

Edge connectivity between every pair of nodes, read off Gusfield's flow tree.

*Definition not yet written.*

## References {#concept-references}

[borgatti1990ls](../../references.html#borgatti1990ls), [edmonds1972theoretical](../../references.html#edmonds1972theoretical), [ford1956maximal](../../references.html#ford1956maximal), [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very)

## Lambda connectivity {#lambda_connectivity}

Measure id: `lambda_connectivity`. Original family: Cohesion and subgroups.

**Definition.** Edge connectivity between every pair of nodes, read off Gusfield's flow tree.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>lambda_connectivity</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.edge_connectivity(G, u, v) for every pair of the simple undirected graph</code></td><td></td></tr><tr><td><code>lambda_connectivity</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>igraph::edge_connectivity(g, source = u, target = v) on simplify(as_undirected(g))</code></td><td></td></tr></tbody></table></div>

**References:** [borgatti1990ls](../../references.html#borgatti1990ls), [edmonds1972theoretical](../../references.html#edmonds1972theoretical), [ford1956maximal](../../references.html#ford1956maximal), [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
