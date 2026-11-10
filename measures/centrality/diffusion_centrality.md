---
title: "Diffusion centrality and diffusion degree"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Diffusion centrality and diffusion degree {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `diffusion_centrality`. 3 measures.

## Definition {#concept-definition}

Diffusion centrality and diffusion degree. Entries grouped here: Diffusion; Diffusion degree; Diffusion efficiency.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Diffusion](#cat_diffusion) | `cat_diffusion` | 2 |
| [Diffusion degree](#cat_degree_diffusion) | `cat_degree_diffusion` | 1 |
| [Diffusion efficiency](#cat_diffusion_efficiency) | `cat_diffusion_efficiency` | 1 |

## Diffusion {#cat_diffusion}

Measure id: `cat_diffusion`. Original family: Centrality.

**Definition.** Diffusion.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_diffusion-sknetwork) | `Diffusion; diffusion` | API listing |
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_diffusion-keyplayer) | `diffusion` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_diffusion-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Diffusion; diffusion.
- <a id="why-cat_diffusion-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. keyplayer 1.0.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package keyplayer: exported functions and help titles); API names: diffusion.

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer), [tool_sknetwork](../../references.html#tool_sknetwork)

## Diffusion degree {#cat_degree_diffusion}

Measure id: `cat_degree_diffusion`. Original family: Centrality.

**Definition.** Diffusion degree.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degree_diffusion-centiserve) | `diffusion.degree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_diffusion-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: diffusion.degree.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)

## Diffusion efficiency {#cat_diffusion_efficiency}

Measure id: `cat_diffusion_efficiency`. Original family: Centrality.

**Definition.** Diffusion efficiency.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_diffusion_efficiency-bct) | `diffusion_efficiency` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_diffusion_efficiency-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: diffusion\_efficiency.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
