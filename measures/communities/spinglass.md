---
title: "Spinglass"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spinglass {#concept-top}

Family: [Communities](index.html). Subfamily: Modularity-based detection. Concept id: `spinglass`. 1 measure.

## Definition {#concept-definition}

Spinglass communities of a connected network by simulated annealing of a Potts Hamiltonian (Reichardt and Bornholdt).

*Definition not yet written.*

## References {#concept-references}

[reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2009community](../../references.html#traag2009community)

## Spinglass {#spinglass}

Measure id: `spinglass`. Original family: Communities.

**Definition.** Spinglass communities of a connected network by simulated annealing of a Potts Hamiltonian (Reichardt and Bornholdt).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cluster_spinglass</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-spinglass-pyigraph">details</a></td><td><code>community_spinglass</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-spinglass-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_spinglass.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>spinglass_quality</code></td><td>igraph (R)</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected, (no value) edge_case</td><td>defaults</td><td>abs 0.02, rel 0</td><td><code>mean over set.seed(1..10) of modularity(g, cluster_spinglass(g, weights = NA))</code></td><td>both tools reject disconnected networks; igraph also rejects the trivial ones</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f038">F038</a></td><td>igraph (R)</td><td>convention</td><td>Spinglass reads the network as simple</td></tr></tbody></table></div>

**References:** [reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2009community](../../references.html#traag2009community)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
