---
title: "Growing network models (GN, citation, Callaway, establishment)"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Growing network models (GN, citation, Callaway, establishment) {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Growth and attachment models. Concept id: `growing_network_models`. 7 measures.

## Definition {#concept-definition}

Growing network models (GN, citation, Callaway, establishment). Entries grouped here: Citation-type growth generators; Establishment; Gn graph; Gnc graph; Gnr graph; Growing random graph generator; and 1 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Citation-type growth generators](#gen_citation) | `gen_citation` | 2 |
| [Establishment](#cat_establishment) | `cat_establishment` | 1 |
| [Gn graph](#cat_gn) | `cat_gn` | 1 |
| [Gnc graph](#cat_gnc) | `cat_gnc` | 1 |
| [Gnr graph](#cat_gnr) | `cat_gnr` | 1 |
| [Growing random graph generator](#gen_growing) | `gen_growing` | 2 |
| [Trait-based (Callaway) growth generator](#gen_traits) | `gen_traits` | 1 |

## Citation-type growth generators {#gen_citation}

Measure id: `gen_citation`. Original family: Generators and rewiring.

**Definition.** Citation-type growth generators.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_citation-igraph) | `cit_cit_types; cit_types; full_citation_graph; last_cit; make_full_citation_graph; sample_cit_cit_types; sample_cit_types; sample_last_cit` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_citation-pyigraph) | `Full_Citation` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_citation-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: cit\_cit\_types; cit\_types; full\_citation\_graph; last\_cit; make\_full\_citation\_graph; sample\_cit\_cit\_types; sample\_cit\_types; sample\_last\_cit.
- <a id="why-gen_citation-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Full\_Citation.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Establishment {#cat_establishment}

Measure id: `cat_establishment`. Original family: Graph theory and combinatorics.

**Definition.** Establishment.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_establishment-pyigraph) | `Establishment` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_establishment-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Establishment.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Gn graph {#cat_gn}

Measure id: `cat_gn`. Original family: Generators and rewiring.

**Definition.** Gn graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_gn-networkx) | `gn_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_gn-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: gn\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Gnc graph {#cat_gnc}

Measure id: `cat_gnc`. Original family: Generators and rewiring.

**Definition.** Gnc graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_gnc-networkx) | `gnc_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_gnc-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: gnc\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Gnr graph {#cat_gnr}

Measure id: `cat_gnr`. Original family: Generators and rewiring.

**Definition.** Gnr graph.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_gnr-networkx) | `gnr_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_gnr-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: gnr\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Growing random graph generator {#gen_growing}

Measure id: `gen_growing`. Original family: Generators and rewiring.

**Definition.** Growing random graph generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_growing-igraph) | `growing; sample_growing` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_growing-pyigraph) | `Growing_Random` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_growing-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: growing; sample\_growing.
- <a id="why-gen_growing-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Growing\_Random.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Trait-based (Callaway) growth generator {#gen_traits}

Measure id: `gen_traits`. Original family: Generators and rewiring.

**Definition.** Trait-based (Callaway) growth generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_traits-igraph) | `sample_traits; sample_traits_callaway; traits; traits_callaway` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_traits-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: sample\_traits; sample\_traits\_callaway; traits; traits\_callaway.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
