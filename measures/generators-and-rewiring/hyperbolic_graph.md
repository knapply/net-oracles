---
title: "Hyperbolic random graph"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Hyperbolic random graph {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Small-world, lattice and geometric models. Concept id: `hyperbolic_graph`. 1 measure.

## Definition {#concept-definition}

Hyperbolic random graph. Entries grouped here: Hyperbolic random graph generator.

## Hyperbolic random graph generator {#gen_hyperbolic}

Measure id: `gen_hyperbolic`. Original family: Generators and rewiring.

**Definition.** Hyperbolic random graph generator.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_hyperbolic-networkit) | `DynamicHyperbolicGenerator; HyperbolicGenerator` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gen_hyperbolic-rustworkx) | `hyperbolic_random_graph` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_hyperbolic-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: DynamicHyperbolicGenerator; HyperbolicGenerator.
- <a id="why-gen_hyperbolic-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: hyperbolic\_random\_graph.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
