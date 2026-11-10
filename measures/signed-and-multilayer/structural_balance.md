---
title: "Structural balance and frustration"
layout: default
parent: "Signed and multilayer"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Structural balance and frustration {#concept-top}

Family: [Signed and multilayer](index.html). Subfamily: Signed networks. Concept id: `structural_balance`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\sigma:E\to\{+1,-1\}\)</td><td>sign of each edge</td></tr><tr><td>\((X,V\setminus X)\)</td><td>a split of the nodes into two sets</td></tr><tr><td>\(\ell(G)\)</td><td>frustration index</td></tr><tr><td>\(C=\{C_1,\dots,C_k\}\)</td><td>partition of the nodes into \(k\) clusters</td></tr><tr><td>\(\alpha\)</td><td>weight in \([0,1]\) between the two kinds of inconsistent edge</td></tr></tbody></table></div>

## Definition {#concept-definition}

Structural balance and frustration. Entries grouped here: Structural balance, frustration index, signed blockmodels.

<div class="formula-block"><p class="formula-name"><strong>Balance (Harary 1953; Cartwright and Harary 1956)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\prod_{e\in\text{cycle}}\sigma(e)=+1\ \text{for every cycle}\iff\exists X\subseteq V:\ \sigma(uv)=+1\text{ exactly when }u,v\text{ lie on the same side}\]</div><p class="formula-where">A signed graph is balanced when every cycle has an even number of negative edges; equivalently, the nodes split into two sets with positive edges inside and negative edges between.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Frustration index</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\ell(G)=\min_{X\subseteq V}\Bigl(\bigl|\{uv\in E^-:\ u,v\in X\text{ or }u,v\notin X\}\bigr|+\bigl|\{uv\in E^+:\ |\{u,v\}\cap X|=1\}\bigr|\Bigr)\]</div><p class="formula-where">Least number of edges whose sign must change (or that must be deleted) to reach balance; 0 exactly when the graph is balanced. The minimum is over all \(2^n\) splits. This is the two-group form of the partitioning criterion below.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Partitioning criterion (Doreian and Mrvar 1996)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[P_\alpha(C)=\alpha\,\bigl|\{uv\in E^-:\ u,v\text{ in the same cluster}\}\bigr|+(1-\alpha)\,\bigl|\{uv\in E^+:\ u,v\text{ in different clusters}\}\bigr|\]</div><p class="formula-where">Weighted count of negative ties inside clusters and positive ties between clusters, minimized over partitions into \(k\) clusters; \(k=2\) and \(\alpha=\tfrac12\) gives half the frustration objective.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#signed_balance">Structural balance, frustration index, signed blockmodels</a></td><td><code>signed_balance</code></td><td>1</td><td>Three objects scored: the balance test (yes or no), the frustration index (a count of inconsistent edges, minimum over two-group splits) and the \(k\)-cluster partitioning criterion with weight \(\alpha\); a signed blockmodel is the partition that minimizes the criterion.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/signnet.html">signnet</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No cycle exists and no edge is inconsistent: balanced, frustration 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A positive loop is a balanced cycle of length 1; a negative loop is an unbalanced cycle that no split can repair, so the cycle form of the definition gives unbalanced while the split form ignores loops.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">An edge of sign 0 has no sign in \(\{+1,-1\}\): the definition covers only signed edges, so such edges must be removed or assigned a sign first.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\alpha\) outside \([0,1]\) or \(k&lt;1\) is outside the definition of the criterion.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Structural balance, frustration index, signed blockmodels {#signed_balance}

Measure id: `signed_balance`. Original family: Signed and multilayer.

**Definition.** Structural balance, frustration index, signed blockmodels.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/signnet.html">signnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: signnet is documented-only in this survey; listed in its documentation. <a href="#why-signed_balance-signnet">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-signed_balance-signnet"></a>**[signnet](../../tools/signnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. signnet (version not recorded) is a documented-only tool in this survey: no comparison has been set up for it (not yet wired up), so its values are not compared with the reference value. Documentation source: its documentation.

**Tools cited:** [tool_signnet](../../references.html#tool_signnet)
{% endraw %}
