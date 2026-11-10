---
title: "Structural equivalence"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Structural equivalence {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Equivalence and clustering. Concept id: `structural_equivalence`. 3 measures.

## Definition {#concept-definition}

Pairwise structural equivalence of all nodes: Euclidean distance, correlation or Hamming distance between their tie profiles.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#structural_equivalence">Structural equivalence</a></td><td><code>structural_equivalence</code></td><td>3</td></tr><tr><td><a href="#equivalence_extra">Equivalence measures: matches, positive matches, overlaps, cross-products, coverage</a></td><td><code>equivalence_extra</code></td><td>1</td></tr><tr><td><a href="#cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural">Structural equivalence: profile (correlation, Euclidean, etc ), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row</a></td><td><code>cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[breiger1975algorithm](../../references.html#breiger1975algorithm), [burt1976positions](../../references.html#burt1976positions), [lorrain1971structural](../../references.html#lorrain1971structural), [wasserman1994social](../../references.html#wasserman1994social)

## Structural equivalence {#structural_equivalence}

Measure id: `structural_equivalence`. Original family: Roles and positions.

**Definition.** Pairwise structural equivalence of all nodes: Euclidean distance, correlation or Hamming distance between their tie profiles.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>sedist</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-structural_equivalence-ucinet">details</a></td><td><code>SE</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/blockmodeling.html">blockmodeling</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (direction): On a symmetric matrix (every undirected fixture and complete5_dir) blockmodeling::sedist agrees with the reference. <a href="#why-structural_equivalence-blockmodeling">details</a></td><td><code>sedist</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-structural_equivalence-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-structural_equivalence-blockmodeling"></a>**[blockmodeling](../../tools/blockmodeling.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> blockmodeling 1.1.8 was run and its value differs from the reference value by convention (direction) on inputs tagged directed. On a symmetric matrix (every undirected fixture and complete5\_dir) blockmodeling::sedist agrees with the reference. On an asymmetric one it compares full row and column profiles including the entries for the two nodes themselves (k = i, j), where the reference, like sna::sedist, leaves them out; node 0 against node 1 on cycle7\_dir is 2 against sqrt(2), and on pair 0 against sqrt(2). Relation to the reference value: Asymmetric matrices: profiles keep the entries for the two nodes themselves (k = i, j) when the matrix is asymmetric; equal to the reference on symmetric matrices. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 9 comparisons differ and 25 agree. Finding F084 (convention): Profiles keep the entries for the two nodes themselves on asymmetric matrices. Findings: [F084](../../findings.html#f084).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>structural_equivalence_correlation</code></td><td>sna</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>sna::sedist(m, method = 'correlation')</code></td><td>sna::sedist() fails on a network with one node.</td></tr><tr><td><code>structural_equivalence_euclidean</code></td><td>sna</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>sna::sedist(m, method = 'euclidean')</code></td><td>sna::sedist() fails on a network with one node.</td></tr><tr><td><code>structural_equivalence_euclidean</code></td><td>blockmodeling</td><td>any</td><td>differs</td><td>directed</td><td>direction</td><td>abs 1e-12, rel 1e-12</td><td><code>blockmodeling::sedist(m, method = 'euclidean')</code></td><td>On a symmetric matrix (every undirected fixture and complete5_dir) blockmodeling::sedist agrees with the reference. On an asymmetric one it compares full row and column profiles including the entries for the two nodes themselves (k = i, j), where the reference, like sna::sedist, leaves them out; node 0 against node 1 on cycle7_dir is 2 against sqrt(2), and on pair 0 against sqrt(2). The oracle script does not call blockmodeling on a network of one node: sedist compares pairs of nodes, and there is no pair.</td></tr><tr><td><code>structural_equivalence_euclidean_weighted</code></td><td>sna</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>sna::sedist(valued m, method = 'euclidean')</code></td><td></td></tr><tr><td><code>structural_equivalence_euclidean_weighted</code></td><td>blockmodeling</td><td>any</td><td>differs</td><td>directed</td><td>direction</td><td>abs 1e-12, rel 1e-12</td><td><code>blockmodeling::sedist(W, method = 'euclidean')</code></td><td>On a symmetric matrix (every undirected fixture and complete5_dir) blockmodeling::sedist agrees with the reference. On an asymmetric one it compares full row and column profiles including the entries for the two nodes themselves (k = i, j), where the reference, like sna::sedist, leaves them out; node 0 against node 1 on cycle7_dir is 2 against sqrt(2), and on pair 0 against sqrt(2).</td></tr><tr><td><code>structural_equivalence_hamming</code></td><td>sna</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sna::sedist(m, method = 'hamming')</code></td><td>sna::sedist() fails on a network with one node.</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f084">F084</a></td><td>blockmodeling</td><td>convention</td><td>Profiles keep the entries for the two nodes themselves on asymmetric matrices</td></tr></tbody></table></div>

**References:** [breiger1975algorithm](../../references.html#breiger1975algorithm), [burt1976positions](../../references.html#burt1976positions), [lorrain1971structural](../../references.html#lorrain1971structural), [wasserman1994social](../../references.html#wasserman1994social)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [ziberna2007generalized](../../references.html#ziberna2007generalized)

## Equivalence measures: matches, positive matches, overlaps, cross-products, coverage {#equivalence_extra}

Measure id: `equivalence_extra`. Original family: Roles and positions.

**Definition.** Equivalence measures: matches, positive matches, overlaps, cross-products, coverage.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-equivalence_extra-ucinet">details</a></td><td></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-equivalence_extra-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Structural equivalence: profile (correlation, Euclidean, etc ), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row {#cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural}

Measure id: `cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural`. Original family: Paths and distances.

**Definition.** Structural equivalence: profile (correlation, Euclidean, etc ), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural-ucinet">details</a></td><td><code>Structural equivalence: profile (correlation, Euclidean, etc.), similarities and distance measures (Jaccard, matches, Hamming, Manhattan), diagonal options (Row</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_correlation_diagonal_distance_equivalence_etc_euclidean_hamming_jaccard_manhattan_matches_measures_options_profile_row_similarities_structural-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
