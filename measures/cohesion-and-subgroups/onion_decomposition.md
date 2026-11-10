---
title: "Onion decomposition"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Onion decomposition {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cores, trusses and cohesive blocks. Concept id: `onion_decomposition`. 1 measure.

## Definition {#concept-definition}

Onion layer of every node, from 1: the round of the core peeling in which it is removed.

*Definition not yet written.*

## References {#concept-references}

[batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

## Onion {#onion}

Measure id: `onion`. Original family: Cohesion and subgroups.

**Definition.** Onion layer of every node, from 1: the round of the core peeling in which it is removed.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>onion_layers</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.onion_layers(G), G the simple undirected graph without loops</code></td><td></td></tr></tbody></table></div>

**References:** [batagelj2003algorithm](../../references.html#batagelj2003algorithm), [carmi2007model](../../references.html#carmi2007model), [goltsev2006k](../../references.html#goltsev2006k), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hebertdufresne2016multi](../../references.html#hebertdufresne2016multi), [seidman1983network](../../references.html#seidman1983network), [wang2012truss](../../references.html#wang2012truss)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
