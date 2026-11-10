---
title: "N-cliques"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# N-cliques {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `n_cliques`. 1 measure.

## Definition {#concept-definition}

n-cliques: maximal sets whose members are all within distance n of each other in the whole network.

*Definition not yet written.*

## References {#concept-references}

[alba1973graph](../../references.html#alba1973graph), [luce1950connectivity](../../references.html#luce1950connectivity), [mokken1979cliques](../../references.html#mokken1979cliques)

## N cliques {#n_cliques}

Measure id: `n_cliques`. Original family: Cohesion and subgroups.

**Definition.** n-cliques: maximal sets whose members are all within distance n of each other in the whole network.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-n_cliques-ucinet">details</a></td><td><code>ncliques</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-n_cliques-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>n_cliques_2</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.find_cliques on the graph joining nodes at distance &lt;= 2 (single_source_shortest_path_length, cutoff 2)</code></td><td></td></tr><tr><td><code>n_cliques_3_min4</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.find_cliques on the distance-3 power graph, keeping cliques of at least 4</code></td><td></td></tr></tbody></table></div>

**References:** [alba1973graph](../../references.html#alba1973graph), [luce1950connectivity](../../references.html#luce1950connectivity), [mokken1979cliques](../../references.html#mokken1979cliques)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
