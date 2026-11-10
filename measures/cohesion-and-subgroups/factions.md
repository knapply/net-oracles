---
title: "Factions"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Factions {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `factions`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>simple undirected graph (direction ignored, parallel edges merged, loops dropped) with node set \(V\), \(n=|V|\)</td></tr><tr><td>\(a_{ij}\)</td><td>1 if \(i,j\) are tied, else 0</td></tr><tr><td>\(p:V\to\{1..k\}\)</td><td>a partition into \(k\) groups</td></tr></tbody></table></div>

## Definition {#concept-definition}

Factions: a partition into k groups that best fits the ideal pattern of ties inside groups only, by tabu search from random starts.

*Definition partly written:* Both measures are documented only (UCINET) and were never run; the objective below is from the measure description (a partition into k groups fitting the ideal pattern of ties inside groups only, by tabu search from random starts) and no verified primary source is available, so no citation is given. The correlation form of the fit and UCINET's options are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Factions error count</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[E(p)=\sum_{i&lt;j,\ p_i\ne p_j}a_{ij}+\sum_{i&lt;j,\ p_i=p_j}(1-a_{ij})\]</div><p class="formula-where">Ties between groups plus missing ties within groups: the deviations from the ideal pattern of complete groups with no ties between them. The best partition minimizes \(E\) for the given \(k\); found by a heuristic search, so not guaranteed optimal and not unique.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_factions">Factions</a></td><td><code>cat_factions</code></td><td>1</td><td>The factions partition as documented for UCINET; the options are not recorded.</td></tr><tr><td><a href="#factions_errors">Factions errors</a></td><td><code>factions_errors</code></td><td>1</td><td>The partition into \(k\) groups with the fewest errors \(E(p)\) against the ideal pattern of ties inside groups only, by tabu search from random starts.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With \(k&gt;n\) groups some groups are empty and cannot reduce \(E\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Within-group missing ties are the only errors; the best partition puts each node alone (\(E=0\)) when \(k\ge n\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">One group (\(E=0\)); with \(k\) groups forced non-empty, ties between groups are errors.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Several partitions may reach the minimum; the search returns one.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(k\) must be between 1 and \(n\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [doreian2005generalized](../../references.html#doreian2005generalized), [glover1989tabu](../../references.html#glover1989tabu), [hanneman2005introduction](../../references.html#hanneman2005introduction)

## Factions {#cat_factions}

Measure id: `cat_factions`. Original family: Cohesion and subgroups.

**Definition.** Factions.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_factions-ucinet">details</a></td><td><code>factions</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_factions-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Factions errors {#factions_errors}

Measure id: `factions_errors`. Original family: Cohesion and subgroups.

**Definition.** Factions: a partition into k groups that best fits the ideal pattern of ties inside groups only, by tabu search from random starts.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-factions_errors-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-factions_errors-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [borgatti1999models](../../references.html#borgatti1999models), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [doreian2005generalized](../../references.html#doreian2005generalized), [glover1989tabu](../../references.html#glover1989tabu), [hanneman2005introduction](../../references.html#hanneman2005introduction)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
