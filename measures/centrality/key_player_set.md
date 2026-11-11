---
title: "Key player set (KPP)"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Key player set (KPP) {#concept-top}

Family: [Centrality](index.html). Subfamily: Key players. Concept id: `key_player_set`. 5 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(k\)</td><td>size of the set</td></tr><tr><td>\(f(S)\)</td><td>one of the criteria of the single-set concept (fragmentation, distance-weighted fragmentation, m-reach, distance-weighted reach)</td></tr></tbody></table></div>

## Definition {#concept-definition}

The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

<div class="formula-block"><p class="formula-name"><strong>Optimal key player set (Borgatti 2006)</strong> <span class="applies">applies to: group</span></p><div class="formula">\[S^*=\arg\min_{|S|=k}F(S)\ \ \text{or}\ \ \arg\max_{|S|=k}R(S)\]</div><p class="formula-where">The set of \(k\) nodes that best satisfies the criterion: minimum remaining connectedness for the fragmentation criteria (KPP-1), maximum reach for the reach criteria (KPP-2). Exact enumeration or a greedy swap search; the search is random-start, so different runs can return different local optima.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#kpp_optimum-distance_fragmentation">Kpp_optimum / distance_fragmentation</a></td><td><code>kpp_optimum:distance_fragmentation</code></td><td>1</td><td>Distance-weighted fragmentation criterion.</td></tr><tr><td><a href="#kpp_optimum-distance_reach">Kpp_optimum / distance_reach</a></td><td><code>kpp_optimum:distance_reach</code></td><td>1</td><td>Distance-weighted reach criterion.</td></tr><tr><td><a href="#kpp_optimum-fragmentation">Kpp_optimum / fragmentation</a></td><td><code>kpp_optimum:fragmentation</code></td><td>1</td><td>Fragmentation criterion (documented in the tool; not run).</td></tr><tr><td><a href="#kpp_optimum-m_reach">Kpp_optimum / m_reach</a></td><td><code>kpp_optimum:m_reach</code></td><td>1</td><td>m-reach criterion.</td></tr><tr><td><a href="#cat_kpset">Kpset</a></td><td><code>cat_kpset</code></td><td>1</td><td>The search procedure of one tool with a choice of criteria (degree, closeness, betweenness, eigenvector, m-reach, fragmentation, diffusion).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/keyplayer.html">keyplayer</a></th></tr></thead><tbody><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">\(k\) larger than \(n\): no set to score; \(k=n\): the whole network.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Several sets can share the optimum; the greedy search returns one of them.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Fewer nodes than the set size: no set.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Pairs without a path are disconnected in fragmentation; reach is within the group's components.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Kpp\_optimum / distance\_fragmentation {#kpp_optimum-distance_fragmentation}

Measure id: `kpp_optimum:distance_fragmentation`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>kpp_distance_fragmentation_optimum_k2</code></td><td>keyplayer</td><td>any</td><td>no-value-on-some-inputs</td><td>(no value) directed</td><td>direction</td><td>abs 1e-14, rel 1e-12</td><td><code>maximum over every pair S of keyplayer::fragment(adjacency, S, binary = TRUE)</code></td><td>single_node has fewer nodes than the set size, so there is no set to score; keyplayer's fragmentation is not directional, so it is compared on undirected networks only.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/resilience.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/resilience.yaml); [harness/golden/keyplayer/](https://github.com/knapply/net-oracles/tree/main/harness/golden/keyplayer/)

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_optimum / distance\_reach {#kpp_optimum-distance_reach}

Measure id: `kpp_optimum:distance_reach`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>kpp_distance_reach_optimum_k2</code></td><td>keyplayer</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-14, rel 1e-12</td><td><code>maximum over every pair S of (|S| + (n - |S|) kpcent(adjacency, S, 'mreach.closeness', M = Inf, method = 'min', binary = TRUE, cmode = 'outdegree')) / n</code></td><td>no set of two nodes leaves anything to reach (single node), and keyplayer::kpcent fails on a two-node network.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/resilience.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/resilience.yaml); [harness/golden/keyplayer/](https://github.com/knapply/net-oracles/tree/main/harness/golden/keyplayer/)

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_optimum / fragmentation {#kpp_optimum-fragmentation}

Measure id: `kpp_optimum:fragmentation`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-kpp_optimum-fragmentation-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_optimum-fragmentation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Kpp\_optimum / m\_reach {#kpp_optimum-m_reach}

Measure id: `kpp_optimum:m_reach`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>kpcent</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>kpp_m_reach_optimum_k3</code></td><td>keyplayer</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>maximum over every set S of three nodes of keyplayer::kpcent(adjacency, S, 'mreach.degree', M = 1, method = 'min', binary = TRUE, cmode = 'outdegree')</code></td><td>fewer nodes than the set size, so there is no set to score.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/resilience.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/resilience.yaml); [harness/golden/keyplayer/](https://github.com/knapply/net-oracles/tree/main/harness/golden/keyplayer/)

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpset {#cat_kpset}

Measure id: `cat_kpset`. Original family: Graph theory and combinatorics.

**Definition.** Kpset.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/keyplayer.html">keyplayer</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_kpset-keyplayer">details</a></td><td><code>kpset</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_kpset-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. keyplayer 1.0.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package keyplayer: exported functions and help titles); API names: kpset.

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)
{% endraw %}
