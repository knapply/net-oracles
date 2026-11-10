---
title: "Forest fire model"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Forest fire model {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Growth and attachment models. Concept id: `forest_fire`. 1 measure.

## Definition {#concept-definition}

Forest fire model. Entries grouped here: Forest fire generator.

## Forest fire generator {#gen_forest_fire}

Measure id: `gen_forest_fire`. Original family: Generators and rewiring.

**Definition.** Forest fire generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_forest_fire-igraph) | `sample_forestfire` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_forest_fire-pyigraph) | `Forest_Fire` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_forest_fire-networkit) | `DynamicForestFireGenerator` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_forest_fire-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: sample\_forestfire.
- <a id="why-gen_forest_fire-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Forest\_Fire.
- <a id="why-gen_forest_fire-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: DynamicForestFireGenerator.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
