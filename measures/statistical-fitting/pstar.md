---
title: "p-star models"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# p-star models {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `pstar`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(y\)</td><td>the network as a matrix of tie indicators \(y_{ij}\in\{0,1\}\) (simple graph, no loops); \(y^{ij+}\) and \(y^{ij-}\) have the tie \((i,j)\) set to 1 and 0</td></tr><tr><td>\(g(y)\)</td><td>vector of network statistics</td></tr><tr><td>\(\theta\)</td><td>coefficient vector</td></tr><tr><td>\(\delta_{ij}(y)\)</td><td>change statistic \(g(y^{ij+})-g(y^{ij-})\)</td></tr><tr><td>\(n\)</td><td>number of nodes</td></tr><tr><td>\(x_i\)</td><td>a nodal attribute</td></tr></tbody></table></div>

## Definition {#concept-definition}

p-star models. Entries grouped here: Pstar.

*Definition partly written:* The pseudolikelihood regression is written (Wasserman and Pattison 1996; Strauss and Ikeda 1990). Which statistics the tool function offers and its options were not recorded.

<div class="formula-block"><p class="formula-name"><strong>Conditional log-odds of a tie</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\operatorname{logit}\Pr_\theta\bigl(Y_{ij}=1\mid Y_{-ij}=y_{-ij}\bigr)=\theta^{\top}\delta_{ij}(y)\]</div><p class="formula-where">Follows from the model; it is what pseudolikelihood fits and what a toggle in a Markov chain uses.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Logit (p*) estimate</strong> <span class="applies">applies to: any, simple</span></p><div class="formula">\[\hat\theta=\arg\max_\theta\sum_{i\ne j}\bigl[y_{ij}\theta^{\top}\delta_{ij}-\log(1+e^{\theta^{\top}\delta_{ij}})\bigr]\]</div><p class="formula-where">A logistic regression of ties on change statistics, i.e. the pseudolikelihood estimate; see ergm_mple.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_pstar">Pstar</a></td><td><code>cat_pstar</code></td><td>1</td><td>p* logistic regression on change statistics of the chosen terms; the term list is a tool option not recorded here.</td></tr></tbody></table></div>

## Pstar {#cat_pstar}

Measure id: `cat_pstar`. Original family: Graph theory and combinatorics.

**Definition.** Pstar.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_pstar-sna">details</a></td><td><code>pstar</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_pstar-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: pstar.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
