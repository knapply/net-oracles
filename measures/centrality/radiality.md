---
title: "Radiality and integration"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Radiality and integration {#concept-top}

Family: [Centrality](index.html). Subfamily: Distance-based. Concept id: `radiality`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(d(s,t)\)</td><td>length of a shortest path from \(s\) to \(t\): number of edges, or the total of the edge lengths for a weighted graph; \(\infty\) if \(t\) cannot be reached from \(s\)</td></tr><tr><td>\(\Delta\)</td><td>diameter: the largest finite distance \(\max_{s,t}d(s,t)\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Radiality and integration. Entries grouped here: Radiality; Valente-Foreman integration and radiality.

*Note:* The treatment of unreachable nodes in the original paper is not recorded in the sources read.

<div class="formula-block"><p class="formula-name"><strong>Radiality (Valente and Foreman 1998)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{Rad}(v)=\frac{\sum_{w\ne v}\bigl(\Delta+1-d(v,w)\bigr)}{n-1}\]</div><p class="formula-where">Mean of the distances reversed against the diameter: nodes close to everyone score near \(\Delta\). Uses out-distances \(d(v,w)\). Integration is the same formula with in-distances \(d(w,v)\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Integration</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\mathrm{Int}(v)=\frac{\sum_{w\ne v}\bigl(\Delta+1-d(w,v)\bigr)}{n-1}\]</div><p class="formula-where">The in-distance counterpart.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_radiality">Radiality</a></td><td><code>cat_radiality</code></td><td>1</td><td>Radiality, first formula.</td></tr><tr><td><a href="#valente_foreman">Valente-Foreman integration and radiality</a></td><td><code>valente_foreman</code></td><td>1</td><td>Integration and radiality: the two formulas above (documented in the tool; not run).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Not defined: \(n-1=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">The diameter is taken over finite distances; an isolate has no finite distance, so its terms are not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Infinite distances make \(\Delta+1-d=-\infty\); the definition needs a rule for unreachable nodes (usually only reachable nodes are summed).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Radiality uses out-distances, integration in-distances.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights as lengths give real-valued \(\Delta\); the paper defines the measures for unweighted graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details></div>

## Radiality {#cat_radiality}

Measure id: `cat_radiality`. Original family: Centrality.

**Definition.** Radiality.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_radiality-centiserve">details</a></td><td><code>radiality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_radiality-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: radiality.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Valente-Foreman integration and radiality {#valente_foreman}

Measure id: `valente_foreman`. Original family: Centrality.

**Definition.** Valente-Foreman integration and radiality.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-valente_foreman-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-valente_foreman-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
