---
title: "Latent-space graphs"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Latent-space graphs {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Small-world, lattice and geometric models. Concept id: `latent_space_graph`. 1 measure.

## Definition {#concept-definition}

Latent-space graphs. Entries grouped here: Latent-space generators (dot product, sphere, islands).

## Latent-space generators (dot product, sphere, islands) {#gen_latent_space}

Measure id: `gen_latent_space`. Original family: Generators and rewiring.

**Definition.** Latent-space generators (dot product, sphere, islands).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_latent_space-igraph) | `dot_product; sample_dirichlet; sample_dot_product; sample_islands; sample_sphere_surface; sample_sphere_volume` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_latent_space-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: dot\_product; sample\_dirichlet; sample\_dot\_product; sample\_islands; sample\_sphere\_surface; sample\_sphere\_volume.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
