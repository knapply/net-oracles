---
title: "Overlapping communities"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Overlapping communities {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `overlapping_communities`. 1 measure.

## Definition {#concept-definition}

Overlapping communities. Entries grouped here: Overlapping.

*Definition not yet written.* Checked against NetworkX (overlapping\_modularity of a cover on the simple undirected graph), but the sources record no formula for it; the modularity-density extension of Chen, Kuzmin and Szymanski 2014 is a related but different quantity, so no definition is written.

## Overlapping {#cnx_overlapping}

Measure id: `cnx_overlapping`. Original family: Communities.

**Definition.** Overlapping.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>overlapping_modularity</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_overlapping_modularity</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>nx.community.overlapping_modularity(G_simple_undirected, cover)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/community_nx.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/community_nx.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
