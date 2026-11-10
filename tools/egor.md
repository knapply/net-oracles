---
title: "egor"
layout: default
parent: Tools
---

{% raw %}

# egor

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>egor</code></td></tr><tr><td>Language</td><td>R</td></tr><tr><td>Version tested</td><td>1.25.10</td></tr><tr><td>License</td><td>AGPL-3.0</td></tr><tr><td>Homepage</td><td><https://cran.r-project.org/package=egor></td></tr><tr><td>Role</td><td>checked</td></tr><tr><td>Citation</td><td><a href="../references.html#tool_egor">tool_egor</a></td></tr></tbody></table></div>

## How it was run

Called from R on ego-centred data objects.

## Coverage

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Measures</th></tr></thead><tbody><tr><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td>1</td></tr><tr><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>1</td></tr><tr><td><a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>1</td></tr></tbody></table></div>

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

<div class="table-wrapper"><table><thead><tr><th>Family</th><th>Subfamily</th><th>Concept</th><th>Measure (variant)</th><th>State</th><th>API names</th><th>Why, if not agrees</th></tr></thead><tbody><tr><td>Ego networks</td><td>Ego measures</td><td><a href="../measures/ego-networks/ego_composition.html">Ego composition and heterogeneity</a></td><td><a href="../measures/ego-networks/ego_composition.html#ego_composition">Ego composition: alter shares, Blau and Shannon heterogeneity, IQV</a></td><td><a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="../measures/ego-networks/ego_composition.html#why-ego_composition-egor">details</a></td></tr><tr><td>Ego networks</td><td>Ego measures</td><td><a href="../measures/ego-networks/ego_density.html">Ego network density</a></td><td><a href="../measures/ego-networks/ego_density.html#ego_summary-density">Ego_summary / density</a></td><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td></tr><tr><td>Mixing and assortativity</td><td>Segregation and homophily indices</td><td><a href="../measures/mixing-and-assortativity/ei_index.html">E-I index</a></td><td><a href="../measures/mixing-and-assortativity/ei_index.html#ei_index">Ei index</a></td><td><a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td></td><td>Differs by convention (defaults, direction, multi-edges, self-loops and ties): egor's comp_ei() counts alters, each neighbour once whatever the number or direction of the ties to it, and no self-loop. <a href="../measures/mixing-and-assortativity/ei_index.html#why-ei_index-egor">details</a></td></tr></tbody></table></div>

## Findings

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../findings.html#f073">F073</a></td><td>convention</td><td>comp_ei counts each neighbour once</td></tr></tbody></table></div>
{% endraw %}
