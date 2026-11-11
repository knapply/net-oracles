---
title: "Key player single-node scores (KPP)"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Key player single-node scores (KPP) {#concept-top}

Family: [Centrality](index.html). Subfamily: Key players. Concept id: `key_player_single`. 4 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(S\)</td><td>set of nodes whose criterion value is computed</td></tr><tr><td>\(d_{ij}\)</td><td>distance between \(i\) and \(j\)</td></tr><tr><td>\(s_k\)</td><td>size of the \(k\)-th connected component of \(G-S\)</td></tr><tr><td>\(d_{Sj}\)</td><td>\(\min_{i\in S}d_{ij}\), taken as 1 for \(j\in S\)</td></tr><tr><td>\(m\)</td><td>distance limit</td></tr></tbody></table></div>

## Definition {#concept-definition}

Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

<div class="formula-block"><p class="formula-name"><strong>Fragmentation (Borgatti 2006)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[F(S)=1-\frac{\sum_k s_k(s_k-1)}{n(n-1)}\]</div><p class="formula-where">Share of ordered pairs of nodes that are disconnected after \(S\) is removed.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Distance-weighted fragmentation</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[D_F(S)=1-\frac{2\sum_{i&lt;j}d_{ij}^{-1}}{n(n-1)}\quad\text{(distances in }G-S\text{)}\]</div><p class="formula-where">Disconnected pairs count 0 and nearby pairs count more.</p></div>

<div class="formula-block"><p class="formula-name"><strong>m-reach</strong> <span class="applies">applies to: any</span></p><div class="formula">\[R_m(S)=\frac{|\{j:\ d_{Sj}\le m\}|}{n}\]</div><p class="formula-where">Share of the nodes within \(m\) steps of \(S\) (members included).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Distance-weighted reach</strong> <span class="applies">applies to: any</span></p><div class="formula">\[D_R(S)=\frac{\sum_j d_{Sj}^{-1}}{n}\]</div><p class="formula-where">Average inverse distance from the group to all nodes.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#kpp_single-distance_fragmentation">Kpp_single / distance_fragmentation</a></td><td><code>kpp_single:distance_fragmentation</code></td><td>1</td><td>Distance-weighted fragmentation of a given set.</td></tr><tr><td><a href="#kpp_single-distance_reach">Kpp_single / distance_reach</a></td><td><code>kpp_single:distance_reach</code></td><td>1</td><td>Distance-weighted reach of a given set.</td></tr><tr><td><a href="#kpp_single-fragmentation">Kpp_single / fragmentation</a></td><td><code>kpp_single:fragmentation</code></td><td>1</td><td>Fragmentation of a given set (documented in the tool; not run).</td></tr><tr><td><a href="#kpp_single-m_reach">Kpp_single / m_reach</a></td><td><code>kpp_single:m_reach</code></td><td>1</td><td>m-reach of a given set.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/keyplayer.html">keyplayer</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Fragmentation: \(n(n-1)=0\) makes the quotient 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (single_node).">agrees</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Fragmentation 1 (all pairs disconnected); reach values reduce to the group itself.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><a class="st st-w st-nov" href="#why-kpp_single-distance_fragmentation-keyplayer" title="keyplayer&#x27;s fragmentation is not directional, so it is compared on undirected networks only. Its formula divides by the largest inverse distance in the residual network (1 on a binary network with any tie left, which makes it Borgatti&#x27;s DF), so it is undefined when removing a node leaves no ties (the centre of star8) or no pairs (one node).">no value</a></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Pairs without a path count as disconnected in fragmentation and have \(d^{-1}=0\) in the weighted forms.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">The paper treats undirected networks; fragmentation is not directional in the tool.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><a class="st st-w st-nov" href="#why-kpp_single-distance_fragmentation-keyplayer" title="keyplayer&#x27;s fragmentation is not directional, so it is compared on undirected networks only.">no value</a></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Distances as lengths for the weighted criteria.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir).">agrees</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">\(S\) equal to all nodes leaves no network to fragment.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li><strong>keyplayer</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>keyplayer</strong>: no value. keyplayer's fragmentation is not directional, so it is compared on undirected networks only. Its formula divides by the largest inverse distance in the residual network (1 on a binary network with any tie left, which makes it Borgatti's DF), so it is undefined when removing a node leaves no ties (the centre of star8) or no pairs (one node). <em>(conventions.json kpp_single:distance_fragmentation / kpp_distance_fragmentation_single)</em></li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>keyplayer</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (two_triangles_isolate, gnp_und_sparse, multi_loops_und). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>keyplayer</strong>: no value. keyplayer's fragmentation is not directional, so it is compared on undirected networks only. <em>(conventions.json kpp_single:distance_fragmentation / kpp_distance_fragmentation_single)</em></li></ul></details><details><summary>Edge weights</summary><ul><li><strong>keyplayer</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (weighted_und, weighted_dir, real_weights_und, real_weights_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Kpp\_single / distance\_fragmentation {#kpp_single-distance_fragmentation}

Measure id: `kpp_single:distance_fragmentation`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults, direction and weights): keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the... <em>(reason incomplete)</em> <a href="#why-kpp_single-distance_fragmentation-keyplayer">details</a></td><td><code>fragment</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_single-distance_fragmentation-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> keyplayer 1.0.4 was run and its value differs from the reference value by convention (defaults, direction and weights) on the fixtures real\_weights\_und, uniform\_weights. keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. The reference equals the definition oracle (exact shortest paths). Unresolved without reading the tool. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (kpp\_distance\_fragmentation\_single) on inputs tagged directed and edgeless and the fixtures single\_node, star8: keyplayer's fragmentation is not directional, so it is compared on undirected networks only. Its formula divides by the largest inverse distance in the residual network (1 on a binary network with any tie left, which makes it Borgatti's DF), so it is undefined when removing a node leaves no ties (the centre of star8) or no pairs (one node). 2 comparisons differ and 20 agree. **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>kpp_distance_fragmentation_single</code></td><td>keyplayer</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) directed, (no value) edgeless</td><td>defaults, direction, normalization, ties</td><td>abs 1e-14, rel 1e-12</td><td><code>keyplayer::fragment(adjacency, v, binary = TRUE) for each node v: 1 - sum_{j,k != v} 1/d_jk / (d (n - 1)(n - 2)), d the largest 1/d_jk (An and Liu 2016, eq. 7)</code></td><td>keyplayer's fragmentation is not directional, so it is compared on undirected networks only. Its formula divides by the largest inverse distance in the residual network (1 on a binary network with any tie left, which makes it Borgatti's DF), so it is undefined when removing a node leaves no ties (the centre of star8) or no pairs (one node).</td></tr><tr><td><code>kpp_distance_fragmentation_single_weighted</code></td><td>keyplayer</td><td>any</td><td>differs</td><td>(no value) directed, (no value) edgeless</td><td>defaults, direction, weights</td><td>abs 1e-14, rel 1e-12</td><td><code>keyplayer::fragment(weighted adjacency, v, binary = FALSE) for each node v (edge values read as distances)</code></td><td>keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. the reference equals the definition oracle (exact shortest paths).</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/resilience.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/resilience.yaml); [harness/golden/keyplayer/](https://github.com/knapply/net-oracles/tree/main/harness/golden/keyplayer/)

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_single / distance\_reach {#kpp_single-distance_reach}

Measure id: `kpp_single:distance_reach`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults and weights): keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the... <em>(reason incomplete)</em> <a href="#why-kpp_single-distance_reach-keyplayer">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_single-distance_reach-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> keyplayer 1.0.4 was run and its value differs from the reference value by convention (defaults and weights) on the fixtures real\_weights\_dir, real\_weights\_und, uniform\_weights. keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. The reference equals the definition oracle (exact shortest paths). Unresolved without reading the tool. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (kpp\_distance\_reach\_single) on inputs tagged edgeless: keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. No value (kpp\_distance\_reach\_single\_in) on inputs tagged edgeless: keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. 3 comparisons differ and 38 agree. Finding F012 (defect): Weighted distances (binary = FALSE) are not shortest-path lengths. Findings: [F012](../../findings.html#f012). **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>kpp_distance_reach_single</code></td><td>keyplayer</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) edgeless</td><td>defaults</td><td>abs 1e-14, rel 1e-12</td><td><code>(1 + (n - 1) * keyplayer::mreach.closeness(adjacency, v, M = Inf, binary = TRUE, cmode = 'outdegree')) / n; keyplayer divides the sum of 1/d by n - 1, Borgatti's DR by n</code></td><td>keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined.</td></tr><tr><td><code>kpp_distance_reach_single_in</code></td><td>keyplayer</td><td>directed</td><td>no-value-on-some-inputs</td><td>(no value) edgeless</td><td>defaults</td><td>abs 1e-14, rel 1e-12</td><td><code>as kpp_distance_reach_single with cmode = 'indegree'</code></td><td>keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined.</td></tr><tr><td><code>kpp_distance_reach_single_weighted</code></td><td>keyplayer</td><td>any</td><td>differs</td><td>(no value) edgeless</td><td>defaults, weights</td><td>abs 1e-14, rel 1e-12</td><td><code>as kpp_distance_reach_single on the weighted adjacency matrix with binary = FALSE (edge values read as distances)</code></td><td>keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. the reference equals the definition oracle (exact shortest paths).</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/resilience.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/resilience.yaml); [harness/golden/keyplayer/](https://github.com/knapply/net-oracles/tree/main/harness/golden/keyplayer/)

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f012">F012</a></td><td>keyplayer</td><td>defect</td><td>Weighted distances (binary = FALSE) are not shortest-path lengths</td></tr></tbody></table></div>

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_single / fragmentation {#kpp_single-fragmentation}

Measure id: `kpp_single:fragmentation`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-kpp_single-fragmentation-ucinet">details</a></td><td><code>Key player / group centrality; exhaustivekp</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_single-fragmentation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Kpp\_single / m\_reach {#kpp_single-m_reach}

Measure id: `kpp_single:m_reach`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>kpp_m_reach_single</code></td><td>keyplayer</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>keyplayer::mreach.degree(adjacency, v, M = 2, binary = TRUE, cmode = 'outdegree')</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/resilience.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/resilience.yaml); [harness/golden/keyplayer/](https://github.com/knapply/net-oracles/tree/main/harness/golden/keyplayer/)

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)
{% endraw %}
