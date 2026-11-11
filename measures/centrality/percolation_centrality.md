---
title: "Percolation centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Percolation centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `percolation_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(\sigma_{st}\)</td><td>number of shortest paths from \(s\) to \(t\) (paths are counted as sequences of edges); \(\sigma_{ss}=1\)</td></tr><tr><td>\(\sigma_{st}(v)\)</td><td>number of those shortest paths that have \(v\) as an inner node (\(v\ne s,t\))</td></tr><tr><td>\(x_i\in[0,1]\)</td><td>percolation state of node \(i\) (fraction of the node that is percolated)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Percolation centrality of every node for given percolation states (Piraveenan, Prokopenko and Hossain 2013).

<div class="formula-block"><p class="formula-name"><strong>Percolation centrality (Piraveenan et al. 2013)</strong> <span class="applies">applies to: undirected, raw</span></p><div class="formula">\[PC(v)=\frac{1}{n-2}\sum_{\substack{s\ne v\ne r}}\frac{\sigma_{sr}(v)}{\sigma_{sr}}\cdot\frac{x_s}{\sum_{i}x_i-x_v}\]</div><p class="formula-where">Betweenness in which a pair's term is weighted by the percolation state of its source relative to the total state outside \(v\). With all states equal it is proportional to betweenness. Needs \(n\ge 3\) and \(\sum_i x_i-x_v&gt;0\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_percolation">Percolation</a></td><td><code>cx_percolation</code></td><td>2</td><td>The formula above for given states \(x\); with equal states it reduces to normalized betweenness.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/graphtool.html">graph-tool</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Not defined: the factor \(1/(n-2)\) is \(-1\) and the sum is empty; the definition requires \(n&gt;2\).</td><td><span class="st st-w st-nov" title="With one node NetworkX multiplies by 1/(n - 2) = -1 and returns -0;">no value</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">Not defined: \(1/(n-2)\) is a division by zero.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">Not defined for \(n\le 2\) (the factor \(1/(n-2)\)).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">\(PC=0\) for an isolate (no path through it).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Pairs without a path are absent from the sum.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">All shortest paths count with weight \(1/\sigma_{sr}\), as in betweenness.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights as lengths decide the shortest paths.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">States must lie in \([0,1]\) and \(\sum_i x_i-x_v\) must be positive; if all percolation is at \(v\) the term is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li><strong>NetworkX</strong>: no value. With one node NetworkX multiplies by 1/(n - 2) = -1 and returns -0; <em>(conventions.json cx_percolation / cx_percolation)</em></li></ul></details><details><summary>Two nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

## Percolation {#cx_percolation}

Measure id: `cx_percolation`. Original family: Centrality.

**Definition.** Percolation centrality of every node for given percolation states (Piraveenan, Prokopenko and Hossain 2013).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>percolation_centrality</code></td><td></td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cx_percolation-graphtool">details</a></td><td><code>vertex_percolation</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cx_percolation-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: vertex\_percolation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_percolation</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) one_node</td><td>defaults, multi_edges</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.percolation_centrality(G, states = {v: ((37 v) mod 11) / 10})</code></td><td>With one node NetworkX multiplies by 1/(n - 2) = -1 and returns -0; the measure is undefined for n &lt;= 2 and the reference returns NaN (NetworkX raises ZeroDivisionError for n = 2, which the oracle records as undefined).</td></tr><tr><td><code>cx_percolation_weighted</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) one_node</td><td>defaults, multi_edges</td><td>abs 1e-12, rel 1e-09</td><td><code>nx.percolation_centrality(G, states = ..., weight = 'weight')</code></td><td>With one node NetworkX multiplies by 1/(n - 2) = -1 and returns -0; the measure is undefined for n &lt;= 2 and the reference returns NaN (NetworkX raises ZeroDivisionError for n = 2, which the oracle records as undefined).</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/centrality_extra.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/centrality_extra.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
