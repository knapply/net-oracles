---
title: "Load centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Load centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `load_centrality`. 2 measures.

## Definition {#concept-definition}

Load centrality of every node: flow split equally among predecessors (Goh, Kahng and Kim 2001).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Load](#cx_load) | `cx_load` | 2 |
| [Loadcent](#cat_loadcent) | `cat_loadcent` | 1 |

## References {#concept-references}

[brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

## Load {#cx_load}

Measure id: `cx_load`. Original family: Centrality.

**Definition.** Load centrality of every node: flow split equally among predecessors (Goh, Kahng and Kim 2001).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `newman_betweenness_centrality` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cx_load-pyigraph) | `Load` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cx_load-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Load.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_load` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G, normalized = False)` |  |
| `cx_load_cutoff` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G, normalized = False, cutoff = 2)` |  |
| `cx_load_normalized` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G)` |  |
| `cx_load_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G, normalized = False, weight = 'weight')` |  |

**References:** [brandes2001faster](../../references.html#brandes2001faster), [brandes2007centrality](../../references.html#brandes2007centrality), [brandes2008variants](../../references.html#brandes2008variants), [goh2001universal](../../references.html#goh2001universal), [piraveenan2013percolation](../../references.html#piraveenan2013percolation)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Loadcent {#cat_loadcent}

Measure id: `cat_loadcent`. Original family: Centrality.

**Definition.** Loadcent.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_loadcent-sna) | `loadcent` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_loadcent-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: loadcent.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)
{% endraw %}
