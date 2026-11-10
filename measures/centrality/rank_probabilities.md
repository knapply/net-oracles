---
title: "Rank probabilities and expected ranks"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Rank probabilities and expected ranks {#concept-top}

Family: [Centrality](index.html). Subfamily: Partial rankings (netrankr). Concept id: `rank_probabilities`. 4 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(P=(V,\preceq)\)</td><td>partial order of the nodes</td></tr><tr><td>\(\mathcal L(P)\)</td><td>set of linear extensions (total rankings that respect the order)</td></tr><tr><td>\(r_\ell(v)\)</td><td>rank of \(v\) in linear extension \(\ell\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Rank probabilities and expected ranks. Entries grouped here: Approx rank expected; Approx rank relative; Exact rank prob; Mcmc rank prob.

<div class="formula-block"><p class="formula-name"><strong>Rank probability</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\Pr[r(v)=k]=\frac{|\{\ell\in\mathcal L(P):\ r_\ell(v)=k\}|}{|\mathcal L(P)|}\]</div><p class="formula-where">Probability that \(v\) has rank \(k\) when a linear extension is drawn uniformly (Schoch 2018).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Expected rank and relative rank</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathbb E[r(v)]=\sum_kk\Pr[r(v)=k],\qquad \Pr[u\prec v]=\frac{|\{\ell:\ r_\ell(u)&lt;r_\ell(v)\}|}{|\mathcal L(P)|}\]</div><p class="formula-where">Mean rank and the probability that \(u\) ranks below \(v\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_approx_expected_rank">Approx rank expected</a></td><td><code>cat_approx_expected_rank</code></td><td>1</td><td>Approximation of the expected ranks (bounds) without enumeration.</td></tr><tr><td><a href="#cat_approx_rank_relative">Approx rank relative</a></td><td><code>cat_approx_rank_relative</code></td><td>1</td><td>Approximation of the relative rank probabilities.</td></tr><tr><td><a href="#cat_exact_prob_rank">Exact rank prob</a></td><td><code>cat_exact_prob_rank</code></td><td>1</td><td>Exact probabilities by enumeration of the linear extensions (feasible for small orders).</td></tr><tr><td><a href="#cat_mcmc_prob_rank">Mcmc rank prob</a></td><td><code>cat_mcmc_prob_rank</code></td><td>1</td><td>Estimates by a Markov chain over linear extensions; random, compared as estimates.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One extension; rank 1 with probability 1.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equivalent nodes have the same distribution of ranks only if ties are broken uniformly.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">If all nodes are mutually dominating the order is trivial: all \(n!\) extensions are possible and each rank has probability \(1/n\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">The number of linear extensions grows factorially: exact computation is infeasible for large orders.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details></div>

## Approx rank expected {#cat_approx_expected_rank}

Measure id: `cat_approx_expected_rank`. Original family: Graph theory and combinatorics.

**Definition.** Approx rank expected.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_approx_expected_rank-netrankr">details</a></td><td><code>approx_rank_expected</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_approx_expected_rank-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: approx\_rank\_expected.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Approx rank relative {#cat_approx_rank_relative}

Measure id: `cat_approx_rank_relative`. Original family: Graph theory and combinatorics.

**Definition.** Approx rank relative.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_approx_rank_relative-netrankr">details</a></td><td><code>approx_rank_relative</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_approx_rank_relative-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: approx\_rank\_relative.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Exact rank prob {#cat_exact_prob_rank}

Measure id: `cat_exact_prob_rank`. Original family: Graph theory and combinatorics.

**Definition.** Exact rank prob.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_exact_prob_rank-netrankr">details</a></td><td><code>exact_rank_prob</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_exact_prob_rank-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: exact\_rank\_prob.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Mcmc rank prob {#cat_mcmc_prob_rank}

Measure id: `cat_mcmc_prob_rank`. Original family: Inference (QAP, null models).

**Definition.** Mcmc rank prob.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_mcmc_prob_rank-netrankr">details</a></td><td><code>mcmc_rank_prob</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mcmc_prob_rank-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: mcmc\_rank\_prob.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
