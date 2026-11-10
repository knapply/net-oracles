---
title: "Maximal independent set"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximal independent set {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `independent_set`. 3 measures.

## Definition {#concept-definition}

A random maximal independent set containing the start nodes (or one random node), nodes in increasing order.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Is independent vertex set](#cat_independent_is_set) | `cat_independent_is_set` | 1 |
| [Is ivs](#cat_is_ivs) | `cat_is_ivs` | 1 |
| [Mis](#mis) | `mis` | 4 |

## References {#concept-references}

[brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [matula1983smallest](../../references.html#matula1983smallest), [schank2005approximating](../../references.html#schank2005approximating), [welsh1967upper](../../references.html#welsh1967upper)

## Is independent vertex set {#cat_independent_is_set}

Measure id: `cat_independent_is_set`. Original family: Graph theory and combinatorics.

**Definition.** Is independent vertex set.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_independent_is_set-pyigraph) | `is_independent_vertex_set` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_independent_is_set-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: is\_independent\_vertex\_set.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Is ivs {#cat_is_ivs}

Measure id: `cat_is_ivs`. Original family: Graph theory and combinatorics.

**Definition.** Is ivs.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_is_ivs-igraph) | `is_ivs` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_is_ivs-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: is\_ivs.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Mis {#mis}

Measure id: `mis`. Original family: Graph theory and combinatorics.

**Definition.** A random maximal independent set containing the start nodes (or one random node), nodes in increasing order.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `maximal_independent_set; maximum_independent_set` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-mis-igraph) | `independence_number; ivs; largest_ivs; max_ivs; maximal_ivs` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-mis-pyigraph) | `independent_vertex_sets; largest_independent_vertex_sets; maximal_independent_vertex_sets` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-mis-graphtool) | `max_independent_vertex_set` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-mis-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: independence\_number; ivs; largest\_ivs; max\_ivs; maximal\_ivs.
- <a id="why-mis-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: independent\_vertex\_sets; largest\_independent\_vertex\_sets; maximal\_independent\_vertex\_sets.
- <a id="why-mis-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: max\_independent\_vertex\_set.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `mis_check` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `1, 1, 1 for nx.maximal_independent_set(G, [start], seed = 11), checked the same way` |  |

**References:** [brelaz1979new](../../references.html#brelaz1979new), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kosowski2004classical](../../references.html#kosowski2004classical), [luby1986simple](../../references.html#luby1986simple), [magnien2009fast](../../references.html#magnien2009fast), [matula1983smallest](../../references.html#matula1983smallest), [schank2005approximating](../../references.html#schank2005approximating), [welsh1967upper](../../references.html#welsh1967upper)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
