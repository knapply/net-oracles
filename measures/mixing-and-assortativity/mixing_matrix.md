---
title: "Mixing matrices"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Mixing matrices {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Mixing matrices. Concept id: `mixing_matrix`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(c(u)\)</td><td>class of node \(u\) (an attribute value, or a degree value for the degree mixing matrix)</td></tr><tr><td>\(M_{ij}\)</td><td>number of edges from a node of class \(i\) to a node of class \(j\)</td></tr><tr><td>\(e_{ij}=M_{ij}/\sum_{kl}M_{kl}\)</td><td>normalized mixing matrix (Newman 2003)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Mixing matrices. Entries grouped here: Attribute mixing matrix; Degree mixing matrix; Mixing.

<div class="formula-block"><p class="formula-name"><strong>Mixing matrix (Newman 2003)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[M_{ij}=\bigl|\{(u,v)\in E: c(u)=i,\;c(v)=j\}\bigr|\]</div><p class="formula-where">Counts of edges between classes. For an undirected graph each edge (u,v) is counted in both orders (so \(M\) is symmetric and a within-class edge adds 2 to \(M_{ii}\)); for a directed graph each arc once, from source class to target class. Defined for any graph; \(e=M/\sum M\) is defined only with at least one edge.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Degree mixing matrix</strong> <span class="applies">applies to: any</span></p><div class="formula">\[c(u)=k_u\]</div><p class="formula-where">The classes are degree values (out at the source, in at the target for directed graphs); the matrix is indexed by degree.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_attribute_matrix_mixing">Attribute mixing matrix</a></td><td><code>cat_attribute_matrix_mixing</code></td><td>1</td><td>The mixing matrix \(M\) with classes given by a node attribute, as documented for NetworkX (not run).</td></tr><tr><td><a href="#cat_degree_matrix_mixing">Degree mixing matrix</a></td><td><code>cat_degree_matrix_mixing</code></td><td>1</td><td>The mixing matrix \(M\) with classes given by node degree, as documented for NetworkX (not run).</td></tr><tr><td><a href="#mixing">Mixing</a></td><td><code>mixing</code></td><td>2</td><td>The attribute or degree mixing matrix \(M\) as produced by a generic mixing function; the counting of edges in both orders for undirected graphs follows the formula above.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No edges: \(M=0\); the normalized \(e_{ij}\) is 0/0.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is an edge from a node to itself: it adds to \(M_{c,c}\) on the diagonal.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Each parallel edge counts: \(M\) counts edges, not distinct pairs.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Directed graphs give an asymmetric \(M\) by source and target class; undirected graphs a symmetric one with each edge in both orders.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">With weights, each edge adds its weight instead of 1.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## Attribute mixing matrix {#cat_attribute_matrix_mixing}

Measure id: `cat_attribute_matrix_mixing`. Original family: Mixing and assortativity.

**Definition.** Attribute mixing matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_attribute_matrix_mixing-networkx">details</a></td><td><code>attribute_mixing_matrix</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attribute_matrix_mixing-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: attribute\_mixing\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Degree mixing matrix {#cat_degree_matrix_mixing}

Measure id: `cat_degree_matrix_mixing`. Original family: Mixing and assortativity.

**Definition.** Degree mixing matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_degree_matrix_mixing-networkx">details</a></td><td><code>degree_mixing_matrix</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_matrix_mixing-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: degree\_mixing\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Mixing {#mixing}

Measure id: `mixing`. Original family: Mixing and assortativity.

**Definition.** Mixing.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>attribute_mixing_dict; degree_mixing_dict</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-mixing-ucinet">details</a></td><td><code>Homophily: categorical (categonethomophily), continuous attributes (own FAQ), PropSame (6.793), mixing matrices / tables (6.813, 6.837)</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-mixing-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>mixing_attribute</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.attribute_mixing_dict(G, 'label')</code></td><td></td></tr><tr><td><code>mixing_attribute_subset</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.attribute_mixing_dict(G, 'label', nodes = even nodes)</code></td><td></td></tr><tr><td><code>mixing_degree</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.degree_mixing_dict(G)</code></td><td></td></tr><tr><td><code>mixing_degree_in_out</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.degree_mixing_dict(G, x = 'in', y = 'out')</code></td><td></td></tr><tr><td><code>mixing_degree_subset</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.degree_mixing_dict(G, nodes = even nodes)</code></td><td></td></tr><tr><td><code>mixing_degree_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.degree_mixing_dict(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
