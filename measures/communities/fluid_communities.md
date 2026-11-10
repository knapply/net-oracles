---
title: "Fluid communities"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Fluid communities {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `fluid_communities`. 1 measure.

## Definition {#concept-definition}

Fluid communities of a connected undirected network: k groups found by density-propagating sweeps.

*Definition not yet written.*

## References {#concept-references}

[pares2018fluid](../../references.html#pares2018fluid)

## Fluid communities {#fluid_communities}

Measure id: `fluid_communities`. Original family: Communities.

**Definition.** Fluid communities of a connected undirected network: k groups found by density-propagating sweeps.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>asyn_fluidc</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cluster_fluid_communities</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-fluid_communities-pyigraph">details</a></td><td><code>community_fluid_communities</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-fluid_communities-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_fluid\_communities.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>fluid_quality</code></td><td>NetworkX</td><td>undirected</td><td>differs</td><td>directed, undirected</td><td>direction, ties</td><td>abs 0.05, rel 0</td><td><code>mean over seeds of modularity(G, asyn_fluidc(simple graph, 3, seed = s))</code></td><td>Fluid communities are randomized and the two procedures draw from different generators; the mean modularity over 20 seeds agrees on the corpus but not on every graph (0.505 against 0.560 on a 60-node tree). The comparison is statistical, not per run.</td></tr><tr><td><code>fluid_quality</code></td><td>igraph (R)</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected, (no value) edge_case</td><td>defaults</td><td>abs 0.05, rel 0</td><td><code>mean over set.seed(1..20) of modularity(g, cluster_fluid_communities(simplify(g), 3))</code></td><td>both tools reject disconnected networks (the reference reports -1); igraph also rejects the trivial ones</td></tr></tbody></table></div>

**References:** [pares2018fluid](../../references.html#pares2018fluid)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
