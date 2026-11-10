---
title: "Block density"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Block density {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Blockmodels. Concept id: `block_density`. 1 measure.

## Definition {#concept-definition}

Block density. Entries grouped here: Block density.

## Block density {#block_density}

Measure id: `block_density`. Original family: Roles and positions.

**Definition.** Block density.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `blockmodel` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-block_density-ucinet) |  | published documentation |
| [blockmodeling](../../tools/blockmodeling.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-block_density-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `block_density` | sna | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `sna::blockmodel(m, v %% 3, block.content = 'density')$block.model` | sna::blockmodel() needs at least three nodes to form the mod-3 blocks it is given here (the partition has fewer than three blocks and sna indexes them by number). |
| `block_density` | blockmodeling | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `blockmodeling::funByBlocks(m, clu = v %% 3 + 1, ignore.diag = TRUE, FUN = 'mean')` | The oracle script does not call blockmodeling on a network of one node: its block tools are built on pairwise node profiles, and there is no pair. |
| `block_density_loops` | blockmodeling | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `blockmodeling::funByBlocks(m with diagonal, clu = v %% 3 + 1, ignore.diag = FALSE, FUN = 'mean')` | The oracle script does not call blockmodeling on a network of one node: its block tools are built on pairwise node profiles, and there is no pair. |
| `block_density_mod2` | sna | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `sna::blockmodel(m, v %% 2, block.content = 'density')$block.model` | A single node forms one block, and sna::blockmodel() cannot index two. |
| `block_density_mod2` | blockmodeling | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `blockmodeling::funByBlocks(m, clu = v %% 2 + 1, ignore.diag = TRUE, FUN = 'mean')` | The oracle script does not call blockmodeling on a network of one node: its block tools are built on pairwise node profiles, and there is no pair. |
| `block_density_weighted` | sna | any | agrees |  |  | abs 0, rel 1e-12 | `sna::blockmodel(valued matrix, v %% 3, block.content = 'density')$block.model` |  |
| `block_density_weighted` | blockmodeling | any | agrees |  |  | abs 0, rel 1e-12 | `blockmodeling::funByBlocks(W, clu = v %% 3 + 1, ignore.diag = TRUE, FUN = 'mean')` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [ziberna2007generalized](../../references.html#ziberna2007generalized)
{% endraw %}
