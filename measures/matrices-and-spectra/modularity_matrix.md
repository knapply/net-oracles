---
title: "Modularity matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Modularity matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `modularity_matrix`. 1 measure.

## Definition {#concept-definition}

Modularity matrix. Entries grouped here: Gm modularity.

## Gm modularity {#gm_modularity}

Measure id: `gm_modularity`. Original family: Matrices and spectra.

**Definition.** Gm modularity.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `directed_modularity_matrix; modularity_matrix` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_modularity-igraph) | `modularity_matrix` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_modularity-pyigraph) | `modularity_matrix` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_modularity-graphtool) | `modularity_matrix` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gm_modularity-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: modularity\_matrix.
- <a id="why-gm_modularity-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: modularity\_matrix.
- <a id="why-gm_modularity-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: modularity\_matrix.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_modularity` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.modularity_matrix(G) or nx.directed_modularity_matrix(G)` | NetworkX does not implement the modularity matrices for multigraphs. |
| `gm_modularity_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.modularity_matrix(G, weight = 'weight') or the directed version` | NetworkX does not implement the modularity matrices for multigraphs. |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
