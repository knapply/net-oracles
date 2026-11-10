---
title: "K-path centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-path centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `k_path_centrality`. 2 measures.

## Definition {#concept-definition}

K-path centrality. Entries grouped here: Geokpath; KPath Centrality.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Geokpath](#cat_geokpath) | `cat_geokpath` | 1 |
| [KPath Centrality](#cat_k_path) | `cat_k_path` | 1 |

## Geokpath {#cat_geokpath}

Measure id: `cat_geokpath`. Original family: Paths and distances.

**Definition.** Geokpath.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_geokpath-centiserve) | `geokpath` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_geokpath-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: geokpath.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## KPath Centrality {#cat_k_path}

Measure id: `cat_k_path`. Original family: Centrality.

**Definition.** KPath Centrality.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_k_path-networkit) | `KPathCentrality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_k_path-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: KPathCentrality.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
