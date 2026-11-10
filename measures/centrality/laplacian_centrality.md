---
title: "Laplacian centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Laplacian centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `laplacian_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(s_i\)</td><td>strength of node \(i\) (degree if unweighted)</td></tr><tr><td>\(w_{ij}\)</td><td>edge weight (1 if unweighted)</td></tr><tr><td>\(E_L(G)\)</td><td>Laplacian energy \(\sum_i\lambda_i^2=\sum_i s_i^2+2\sum_{i&lt;j}w_{ij}^2\), with \(\lambda_i\) the eigenvalues of the Laplacian</td></tr></tbody></table></div>

## Definition {#concept-definition}

Laplacian centrality. Entries grouped here: Cx laplacian.

<div class="formula-block"><p class="formula-name"><strong>Laplacian centrality (Qi et al. 2012)</strong> <span class="applies">applies to: undirected, weighted</span></p><div class="formula">\[C_L(v)=\frac{E_L(G)-E_L(G-v)}{E_L(G)}\]</div><p class="formula-where">Relative drop of the Laplacian energy when \(v\) is removed. The implementation notes of one tool say it simplifies the original algorithm; the raw (unnormalized) form is the numerator.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cx_laplacian">Cx laplacian</a></td><td><code>cx_laplacian</code></td><td>2</td><td>The formula above, raw or normalized by the energy of the whole graph.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/networkit.html">NetworKit</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(E_L(G)=0\): the quotient is 0/0.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop adds to the strength (an undirected loop counts twice); the energy formula is stated for graphs without loops.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges add to weights and strengths.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">\(w^2\) still positive; the interpretation changes.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Cx laplacian {#cx_laplacian}

Measure id: `cx_laplacian`. Original family: Centrality.

**Definition.** Cx laplacian.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>laplacian_centrality</code></td><td></td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>LaplacianCentrality</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_laplacian</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.laplacian_centrality(G, weight = None)</code></td><td></td></tr><tr><td><code>cx_laplacian</code></td><td>NetworKit</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nk.centrality.LaplacianCentrality(G, normalized = True)</code></td><td></td></tr><tr><td><code>cx_laplacian_raw</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.laplacian_centrality(G, normalized = False, weight = None)</code></td><td></td></tr><tr><td><code>cx_laplacian_raw</code></td><td>NetworKit</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nk.centrality.LaplacianCentrality(G, normalized = False)</code></td><td></td></tr><tr><td><code>cx_laplacian_weighted</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.laplacian_centrality(G, weight = 'weight')</code></td><td></td></tr><tr><td><code>cx_laplacian_weighted</code></td><td>NetworKit</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nk.centrality.LaplacianCentrality(G_weighted, normalized = True)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
