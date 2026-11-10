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

*Definition not yet written.*

## Block density {#block_density}

Measure id: `block_density`. Original family: Roles and positions.

**Definition.** Block density.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>blockmodel</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-block_density-ucinet">details</a></td><td></td><td>published documentation</td></tr><tr><td><a href="../../tools/blockmodeling.html">blockmodeling</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-block_density-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>block_density</code></td><td>sna</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>sna::blockmodel(m, v %% 3, block.content = 'density')$block.model</code></td><td>sna::blockmodel() needs at least three nodes to form the mod-3 blocks it is given here (the partition has fewer than three blocks and sna indexes them by number).</td></tr><tr><td><code>block_density</code></td><td>blockmodeling</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>blockmodeling::funByBlocks(m, clu = v %% 3 + 1, ignore.diag = TRUE, FUN = 'mean')</code></td><td>The oracle script does not call blockmodeling on a network of one node: its block tools are built on pairwise node profiles, and there is no pair.</td></tr><tr><td><code>block_density_loops</code></td><td>blockmodeling</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>blockmodeling::funByBlocks(m with diagonal, clu = v %% 3 + 1, ignore.diag = FALSE, FUN = 'mean')</code></td><td>The oracle script does not call blockmodeling on a network of one node: its block tools are built on pairwise node profiles, and there is no pair.</td></tr><tr><td><code>block_density_mod2</code></td><td>sna</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>sna::blockmodel(m, v %% 2, block.content = 'density')$block.model</code></td><td>A single node forms one block, and sna::blockmodel() cannot index two.</td></tr><tr><td><code>block_density_mod2</code></td><td>blockmodeling</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>blockmodeling::funByBlocks(m, clu = v %% 2 + 1, ignore.diag = TRUE, FUN = 'mean')</code></td><td>The oracle script does not call blockmodeling on a network of one node: its block tools are built on pairwise node profiles, and there is no pair.</td></tr><tr><td><code>block_density_weighted</code></td><td>sna</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>sna::blockmodel(valued matrix, v %% 3, block.content = 'density')$block.model</code></td><td></td></tr><tr><td><code>block_density_weighted</code></td><td>blockmodeling</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-12</td><td><code>blockmodeling::funByBlocks(W, clu = v %% 3 + 1, ignore.diag = TRUE, FUN = 'mean')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [ziberna2007generalized](../../references.html#ziberna2007generalized)
{% endraw %}
