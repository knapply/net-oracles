---
title: "K-plexes"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-plexes {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `k_plexes`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>simple undirected graph (direction ignored, parallel edges merged, loops dropped) with node set \(V\), \(n=|V|\)</td></tr><tr><td>\(S\)</td><td>a set of \(s=|S|\) nodes</td></tr><tr><td>\(\deg_S(v)\)</td><td>number of neighbours of \(v\) inside \(S\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Maximal k-plexes: node sets in which each member has at most k - 1 non-neighbours among the others.

*Note:* Documented only (UCINET), never run; the formula is the definition of Seidman and Foster 1978.

<div class="formula-block"><p class="formula-name"><strong>k-plex (Seidman and Foster 1978)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[S\text{ is a }k\text{-plex}\iff\deg_S(v)\ge |S|-k\ \ \forall v\in S\]</div><p class="formula-where">Each member is adjacent to all but at most \(k-1\) of the other members; a 1-plex is a clique. Maximal \(k\)-plexes cannot be extended. Defined for \(k\ge1\); sets of fewer than \(k\) nodes satisfy it trivially, so a minimum size is imposed in practice.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#k_plexes">K plexes</a></td><td><code>k_plexes</code></td><td>1</td><td>All maximal \(k\)-plexes of at least a given size.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No node set.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Any set of at most \(k\) nodes is a \(k\)-plex.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">Sets smaller than the minimum size are not reported.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">The whole node set is a 1-plex.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(k&lt;1\) is meaningless (a node would need more than all other members as neighbours).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[bron1973algorithm](../../references.html#bron1973algorithm), [seidman1978graph](../../references.html#seidman1978graph), [seidman1983network](../../references.html#seidman1983network)

## K plexes {#k_plexes}

Measure id: `k_plexes`. Original family: Cohesion and subgroups.

**Definition.** Maximal k-plexes: node sets in which each member has at most k - 1 non-neighbours among the others.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-k_plexes-ucinet">details</a></td><td><code>kplex</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-k_plexes-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [bron1973algorithm](../../references.html#bron1973algorithm), [seidman1978graph](../../references.html#seidman1978graph), [seidman1983network](../../references.html#seidman1983network)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
