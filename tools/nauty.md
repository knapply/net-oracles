---
title: "nauty"
layout: default
parent: Tools
---

{% raw %}

# nauty

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>nauty</code></td></tr><tr><td>Language</td><td>C (via pynauty)</td></tr><tr><td>Version tested</td><td>2.8.8 (pynauty 2.8.8.1)</td></tr><tr><td>License</td><td>permissive (see the distribution COPYRIGHT file)</td></tr><tr><td>Homepage</td><td><https://pallini.di.uniroma1.it/></td></tr><tr><td>Role</td><td>checked</td></tr><tr><td>Citation</td><td><a href="../references.html#mckay2014practical">mckay2014practical</a></td></tr></tbody></table></div>

## How it was run

Called through pynauty on graph adjacency dictionaries.

## Coverage

<div class="table-wrapper"><table><thead><tr><th>State</th><th>Measures</th></tr></thead><tbody><tr><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td>2</td></tr></tbody></table></div>

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

<div class="table-wrapper"><table><thead><tr><th>Family</th><th>Subfamily</th><th>Concept</th><th>Measure (variant)</th><th>State</th><th>API names</th><th>Why, if not agrees</th></tr></thead><tbody><tr><td>Graph theory and combinatorics</td><td>Isomorphism and subgraph matching</td><td><a href="../measures/graph-theory-and-combinatorics/graph_isomorphism.html">Graph isomorphism</a></td><td><a href="../measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp">Vf2pp</a></td><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td></tr><tr><td>Roles and positions</td><td>Equivalence and clustering</td><td><a href="../measures/roles-and-positions/automorphic_equivalence.html">Automorphic equivalence</a></td><td><a href="../measures/roles-and-positions/automorphic_equivalence.html#automorphic_equivalence">Automorphic equivalence</a></td><td><a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td></tr></tbody></table></div>

## Findings

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../findings.html#f071">F071</a></td><td>limitation</td><td>Parallel edges are not representable</td></tr></tbody></table></div>
{% endraw %}
