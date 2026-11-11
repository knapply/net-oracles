---
title: "Kemeny constant"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Kemeny constant {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Resistance and spectral distances. Concept id: `kemeny_constant`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target</td></tr><tr><td>\(P=D^{-1}A\)</td><td>transition matrix of the random walk (\(A\) adjacency or weight matrix, \(D\) its row sums)</td></tr><tr><td>\(\pi_j\)</td><td>stationary distribution, \(\pi_j=k_j/\sum k\) for an undirected graph</td></tr><tr><td>\(m_{ij}\)</td><td>mean first passage time from \(i\) to \(j\) (\(m_{ii}=0\))</td></tr><tr><td>\(\lambda_2,\dots,\lambda_n\)</td><td>the eigenvalues of \(P\) other than the eigenvalue 1</td></tr></tbody></table></div>

## Definition {#concept-definition}

Kemeny's constant of the random walk: the expected steps to reach a stationary-distributed node, the same from every start.

<div class="formula-block"><p class="formula-name"><strong>Kemeny constant (Kemeny and Snell 1960; Levene and Loizou 2002)</strong> <span class="applies">applies to: connected</span></p><div class="formula">\[K=\sum_{j}\pi_jm_{ij}=\sum_{i=2}^{n}\frac{1}{1-\lambda_i}\]</div><p class="formula-where">Expected number of steps to reach a node drawn from the stationary distribution; the same from every start \(i\). Defined for an irreducible chain: a connected undirected graph (periodicity, as in a bipartite graph, is allowed). With several components there is no unique stationary distribution and the passage times are infinite.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_kemeny">Kemeny</a></td><td><code>cx_kemeny</code></td><td>1</td><td>\(K\) of the random walk on the graph, from the eigenvalues of \(P\) or from the Laplacian pseudoinverse.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No chain.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">A single node with no edge: the walk is not defined (row sum 0); with a loop \(K=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">One edge: \(P\) is a swap, \(\lambda_2=-1\), \(K=1/2\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A node without edges has a row sum of 0 and the walk is not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Not irreducible: passage times between components are infinite; not defined.</td><td><span class="st st-w st-nov" title="NetworkX&#x27;s resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny&#x27;s constant.">no value</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">Not strongly connected: not irreducible; not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights enter \(P\); weights must be positive on the edges.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is a step that stays at the node and enters \(P\) (it adds to the degree).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges add to the weight.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The node set splits into two classes with edges only between classes (periodic structure; two-mode data)."><strong>Bipartite or two-mode graph</strong></td><td class="def">Periodic but irreducible: \(\lambda=-1\) is allowed and gives the term 1/2.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(\lambda_i=-1/(n-1)\) for \(i\ge2\): \(K=(n-1)^2/n\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Two nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>NetworkX</strong>: no value. NetworkX's resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant. <em>(conventions.json cx_kemeny / cx_kemeny)</em></li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Bipartite or two-mode graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Kemeny {#cx_kemeny}

Measure id: `cx_kemeny`. Original family: Descriptive statistics.

**Definition.** Kemeny's constant of the random walk: the expected steps to reach a stationary-distributed node, the same from every start.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>kemeny_constant</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_kemeny</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.kemeny_constant(G)</code></td><td>NetworkX's resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant.</td></tr><tr><td><code>cx_kemeny_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.kemeny_constant(G, weight = 'weight')</code></td><td>NetworkX's resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/centrality_extra.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/centrality_extra.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
