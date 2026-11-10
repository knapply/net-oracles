---
title: "Second-order centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Second-order centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `second_order_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(T_v\)</td><td>return time of a random walk that starts at \(v\): the number of steps until it first returns to \(v\)</td></tr><tr><td>\(\pi_v\)</td><td>stationary probability of the walk at \(v\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Second-order centrality of every node: the standard deviation of its return times in a random walk (Kermarrec et al. 2011).

<div class="formula-block"><p class="formula-name"><strong>Second-order centrality (Kermarrec et al. 2011)</strong> <span class="applies">applies to: undirected, connected</span></p><div class="formula">\[C_{\mathrm{SO}}(v)=\sqrt{\mathrm{Var}(T_v)}=\sqrt{\mathbb E[T_v^2]-\mathbb E[T_v]^2}\]</div><p class="formula-where">Standard deviation of the return times of a random walk on the graph (mean return time is \(1/\pi_v\)); low values mean the walk visits \(v\) regularly. Computed from the matrix of mean first-passage times.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_second_order">Second order</a></td><td><code>cx_second_order</code></td><td>1</td><td>The formula above, with unweighted or weighted transition probabilities.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Not defined: the walk has no move.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Return times and first-passage times between components are infinite: defined for connected graphs only.</td><td><span class="st st-w st-nov" title="NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks);">no value</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Transition probabilities proportional to edge counts; the definition is stated for simple graphs.</td><td><span class="st st-w st-nov" title="NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps.">no value</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Transition probabilities proportional to weights.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">The walk cannot leave: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); <em>(conventions.json cx_second_order / cx_second_order)</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. <em>(conventions.json cx_second_order / cx_second_order)</em></li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Second order {#cx_second_order}

Measure id: `cx_second_order`. Original family: Centrality.

**Definition.** Second-order centrality of every node: the standard deviation of its return times in a random walk (Kermarrec et al. 2011).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>second_order_centrality</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_second_order</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected, (no value) multi_edges</td><td>defaults, multi_edges, normalization, ties</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.second_order_centrality(G)</code></td><td>NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps.</td></tr><tr><td><code>cx_second_order_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected, (no value) multi_edges</td><td>defaults, multi_edges, normalization, ties</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.second_order_centrality(G, weight = 'weight')</code></td><td>NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps.</td></tr></tbody></table></div>

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
