---
title: "How entries are labelled"
layout: default
nav_order: 3
permalink: /method.html
---

{% raw %}

# How entries are labelled


Every tool-by-measure entry in this survey has one state. This page says exactly what the states mean, what was compared, how, and on which inputs. The states are stored in `data/capabilities.csv`; the reason for every state other than `checked-agrees` is stored in `data/reasons.json` and shown wherever the entry is shown (measure pages, tool pages, the capability matrix and the findings).

## What was compared {#what-was-compared}

For each entry the tool's output, obtained by the call recorded in `data/conventions.json` (field `call`), is compared with the **reference value** of the measure on every fixture that applies to it.

### The reference value {#reference-value}

The reference value is the value of the published definition of the measure, computed independently of every tool compared:

- on the fixtures that are small enough, by a direct evaluation of the published definition that shares no code with any tool: exact rational arithmetic, enumeration of all cases, or dense linear algebra;
- on every fixture, by this survey's own implementation of the measure, which is itself checked against the direct evaluation on the small fixtures and against every other tool that computes the quantity.

A difference between a tool and the reference value is attributed to the tool, as a convention or a defect, when the tool disagrees with both this survey's implementation and the direct evaluation of the definition (where one exists), which agree with each other. The direct evaluations are slow by design and run only on the small tier, and only up to a size that depends on the cost of the evaluation (from 10 to 80 nodes).

Each tool is run through its public interface (released library, jar, binary or R or Python package, at the version listed on its page); tools under the GPL or LGPL are run strictly as black boxes. The options of the call select which published quantity is computed (for example normalized or raw, directed or undirected, weighted or not); they are never used to correct the tool's value.

### The inputs {#inputs}

The fixtures are listed [below](#fixtures): 28 small graphs that every tool is run on (classic data sets, synthetic graphs of every structural kind, seeded random graphs, graphs with self-loops and parallel edges, edge cases of zero, one and two nodes), and a size tier of mid-size and large graphs that only the fast tools follow.

**All inputs** means every fixture of that list that applies to the measure and that the tool accepts. A fixture applies to a measure when its direction and weights fit the measure's scope (a directed-only measure is not run on undirected fixtures; a weighted variant is not run on unweighted fixtures). A fixture counts as accepted when the tool returns a value for it. A run that the tool rejects with an error, that returns nothing or a marker for "undefined", that does not finish within the time limit, or that the comparison script declines (for example because the tool cannot represent parallel edges) is not a comparison: it is recorded as *no value* on that input, with the reason, and it neither makes the entry agree nor makes it differ. On the size tier, a pair of measure and tool is run only up to the size the tool can follow; the inputs left out are recorded with the reason (for example "no result within 180 s" or the tool's error text).

## How values are compared {#how-values-are-compared}

The comparison depends on the kind of output, and is fixed per measure before the tool is run.

| Output | Rule |
|---|---|
| Integers, counts, booleans | Exact equality. |
| Sets and collections of groups (cliques, components, edge sets, cuts) | Exact equality of the collections; the order of the groups and of the members within a group does not matter. |
| Partitions (community or equivalence labels) | Equal up to relabelling: group names are arbitrary, so labels are renamed by first appearance before comparing. |
| Values that are a set of numbers without a meaningful order | Compared after sorting. |
| Vectors indexed by node or edge | Compared position by position on the same node and edge identity. A vector that the definition fixes only up to sign (eigenvectors, the Fiedler vector) is put in a fixed sign before comparing, by a rule stated for the measure (for example the scores sum to a positive number). |
| Floating-point values | Two values are equal when their absolute difference is at most `abs` plus `rel` times the larger of their two absolute values, with the `abs` and `rel` recorded for the measure. Equal infinities are equal; an undefined value (NaN) equals only an undefined value. |
| Rankings and orderings with ties | A ranking is compared through the scores it is derived from (vectors indexed by node), so nodes with equal scores are equal by value and no order among them is imposed. Where the definition itself leaves a choice open (equally good merges, equally valid ancestors or independent sets), a tool's different valid answer is a `ties` convention: the reference answer is verified against the definition by a separate validity check instead of being matched node by node. |
| Random and approximate algorithms | Compared by seed where the tool exposes its generator and the procedure is the same (the same seed and the same sampling procedure). Otherwise the comparison is statistical: the quality of the result (for example modularity) is averaged over several seeds (20 to 100) and compared with the tool's own average within a tolerance that only asserts that neither is meaningfully better. Heuristic optimizers are compared one-sidedly: the reference value must be at least as good as the tool's within the tolerance. Monte Carlo estimates are compared within several standard errors. |

### Tolerances {#tolerances}

The tolerance of every record is stored in `data/conventions.json` (`tolerance`: `abs` and `rel`, where 0 means exact). It is set per measure when the measure is added to the comparison, fixed before a tool is run, and recorded with the measure:

- exact (0, 0) where the output is integer-valued, a set, a partition or a discrete label;
- for deterministic floating-point outputs, a bound set per measure, in practice between about 1e-15 and 1e-8, the looser bounds for quantities computed by iterative solvers, which stop at their own convergence tolerance (for example PageRank and eigenvector scores), or summed over many terms;
- for statistical comparisons, a bound of several standard errors of the difference, or about twice the largest difference seen between two correct implementations (about 0.005 to 0.15);
- a tool's own looser bound is recorded on that tool's record only when the tool's own convergence limit requires it.

The distribution of the tolerances used is in the [table below](#tolerance-table). A tolerance is never widened to make an entry agree: where a tool differs by more than the tolerance and the difference is a convention, the entry is `checked-convention`.

## What each state means {#states}

### Checked, agrees {#state-checked-agrees}

<a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> `checked-agrees`

The tool was run, and on **every** fixture that applies to the measure and that the tool accepts, its value equals the reference value within the tolerance recorded for the measure: exactly for integers, sets and discrete labels (partitions up to relabelling), within the absolute and relative tolerances for floating-point values, by seed or by distribution for random and approximate algorithms. The tool's default behaviour is compared as it is: **no convention is mapped for this state**, no input is left out because the tool disagrees, and no tolerance is widened to make the entry agree. Inputs the tool does not accept are not comparisons (see [the inputs](#inputs)). `comparisons_agreeing` counts the agreeing comparisons (variant by fixture) and `comparisons_differing` is 0. Agreement is a statement about the listed fixtures and the tool version tested, not a proof for all graphs.

Entries with this state: **538**.

### Checked, differs by convention {#state-checked-convention}

<a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> `checked-convention`

The tool was run and its value differs from the reference value, beyond the tolerance, on at least one fixture it accepts, and the difference is a documented convention: the tool follows a different, defensible reading of the quantity (normalization, direction, weights, self-loops, multi-edges, ties, defaults, scaling, ordering, or the way an undefined value is encoded). Conventions are mapped before comparing **only for this state**: the reference value is recomputed with the tool's convention, and where such a mapping is recorded it is compared with the tool's values on exactly the inputs where the difference occurs, with its own tolerance; a mismatch there would show that the difference is not the named convention alone. The reason states which convention differs, what each side does, the exact relation between the tool's value and the reference value where the sources give it (for example a constant factor), the inputs, and the tolerance before and after mapping. `comparisons_differing` counts the differing comparisons.

Entries with this state: **129**.

### Checked, defect {#state-checked-defect}

<a class="st st-t st-defect" href="method.html#state-checked-defect"><span class="g" aria-hidden="true">✗</span>checked, defect</a> `checked-defect`

The tool was run and on some input its value is wrong under the published definition: it contradicts the definition, as the direct evaluation shows, rather than reading it differently. The reason states what is wrong, on which inputs, the value observed against the value expected, and the tool version, and links the finding that records the observation and, where available, a minimal reproduction. Findings of kind *defect* are listed on the [findings page](findings.html); a finding recorded for an entry of another state is linked from that entry.

Entries with this state: **1**.

### Checked, no value on some inputs {#state-checked-no-value}

<a class="st st-t st-nov" href="method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> `checked-no-value`

The tool was run for the measure but gave no value on the compared inputs, so no comparison could be made: it raised an error, returned an undefined marker, does not support the type of input, did not finish within the time limit, or its run was declined. The reason states on which inputs and why, with the error text where the sources record it. A tool that gives no value on *some* inputs but values on others is not in this state: its entry is `checked-agrees` or `checked-convention` according to the comparisons made, and the inputs without value are listed in the reason of a `checked-convention` entry (as "No value") and in `data/conventions.json` (`no_value_on_inputs`).

Entries with this state: **3**.

### Reported in docs {#state-reported-in-docs}

<a class="st st-t st-docs" href="method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> `reported-in-docs`

The tool lists the capability in its documentation or public API, but it was **not run** for this measure, so nothing is stated about agreement. The reason says why it was not run and gives the documentation source. Three reasons occur: *not yet wired up* (1627 entries: the tool was run in this survey on other measures, but no comparison against the reference value has been set up for this one), *documented-only tool* (64 entries: the tool is documented-only in this survey, so none of its measures was run), and *commercial, closed-source software* (162 entries: UCINET is proprietary Windows software that was never run here; it is never described as checked).

Entries with this state: **1853**.

### Blank

A blank cell in the matrix, or an absent row in `data/capabilities.csv`, means the tool is not known to implement the measure. It says nothing about whether it does.

## Reasons {#reasons}

Every entry whose state is not `checked-agrees` has a record in `data/reasons.json`, with a plain-words `reason` and a one-sentence `short` form used in tooltips and tables. `python3 scripts/build.py --check` fails if such an entry has no reason, or if the reason lacks the content its state requires. Where the sources used for this survey do not say everything the state requires (for example when the cause of a difference was not traced), the record has `reason_incomplete: true` and `missing` says what is not known; those entries are marked on every page that shows them.

## Fixtures {#fixtures}

54 fixtures: 28 in the small tier (run for every tool and every measure that applies), 16 mid-size and 10 large (run only for the pairs of tool and measure that can follow them). The tags are structural conditions computed from the graph; they are the conditions named in `differs_when`, `undefined_when` and the reasons, and are listed in [data.html](data.html). Node and edge counts are given where fixed by the generator; the edge count of the small tier counts rows of the edge list, including repeated edges and loops.

| Fixture | Tier | Nodes | Edges | Direction | Weights | Tags | Description |
|---|---|---|---|---|---|---|---|
| `complete5_dir` | small | 5 | 20 | directed | none | onemode, symmetric\_nodes | Synthetic |
| `complete6` | small | 6 | 15 | undirected | none | onemode, symmetric\_nodes | Synthetic |
| `cycle7_dir` | small | 7 | 7 | directed | none | onemode, symmetric\_nodes | Synthetic |
| `davis_twomode` | small | 32 | 89 | undirected | none | bipartite, symmetric\_nodes, twomode | Southern women attending social events, as a two-mode network (women type 0, events type 1) [davis1941deep](references.html#davis1941deep) |
| `empty` | small | 5 | 0 | directed | none | bipartite, disconnected, edge\_case, edgeless, isolates, no\_two\_paths, not\_strongly\_connected, onemode, symmetric\_nodes | Synthetic |
| `florentine` | small | 15 | 20 | undirected | none | onemode, unsorted\_edges | Florentine families, marriage ties [breiger1986cumulated](references.html#breiger1986cumulated), [padgett1993robust](references.html#padgett1993robust) |
| `gnp_dir_dense` | small | 40 | 784 | directed | none | onemode | G(n=40, p=0.5), seed 12 |
| `gnp_dir_sparse` | small | 60 | 169 | directed | none | not\_strongly\_connected, onemode | G(n=60, p=0.05), seed 11 |
| `gnp_und_dense` | small | 30 | 268 | undirected | none | onemode | G(n=30, p=0.6), seed 14 |
| `gnp_und_sparse` | small | 80 | 115 | undirected | none | disconnected, isolates, onemode, symmetric\_nodes | G(n=80, p=0.04), seed 13 |
| `karate` | small | 34 | 78 | undirected | none | onemode, symmetric\_nodes | Zachary's karate club network [zachary1977information](references.html#zachary1977information) |
| `kite` | small | 10 | 18 | undirected | none | onemode, symmetric\_nodes | Krackhardt's kite network [krackhardt1990assessing](references.html#krackhardt1990assessing) |
| `les_miserables` | small | 77 | 254 | undirected | integer | integer\_weights, onemode, symmetric\_nodes, weighted | Co-appearance network of Les Miserables characters [knuth1993stanford](references.html#knuth1993stanford) |
| `multi_loops_dir` | small | 20 | 72 | directed | none | loops, multi\_edges, not\_strongly\_connected, onemode, unsorted\_edges | random multigraph n=20, m=72, seed 17 |
| `multi_loops_und` | small | 20 | 72 | undirected | none | disconnected, isolates, loops, multi\_edges, onemode, unsorted\_edges | random multigraph n=20, m=72, seed 18 |
| `pair` | small | 2 | 1 | directed | none | bipartite, edge\_case, no\_two\_paths, not\_strongly\_connected, onemode, symmetric\_nodes, two\_nodes | Synthetic |
| `path10` | small | 10 | 9 | undirected | none | bipartite, onemode, symmetric\_nodes | Synthetic |
| `real_weights_dir` | small | 45 | 208 | directed | real | fractional\_weights, onemode, weighted | G(n=45, p=0.1), seed 22, real weights in \[0.1, 3\] |
| `real_weights_und` | small | 45 | 104 | undirected | real | fractional\_weights, onemode, weighted | G(n=45, p=0.1), seed 23, real weights in \[0.1, 3\] |
| `single_node` | small | 1 | 0 | undirected | none | bipartite, edge\_case, edgeless, isolates, no\_two\_paths, one\_node, onemode | Synthetic |
| `southern_women` | small | 32 | 89 | undirected | none | bipartite, onemode, symmetric\_nodes | Southern women attending social events, one-mode reading of the same data [davis1941deep](references.html#davis1941deep) |
| `star8` | small | 8 | 7 | undirected | none | bipartite, onemode, symmetric\_nodes | Synthetic |
| `two_triangles_isolate` | small | 7 | 6 | undirected | none | disconnected, edge\_case, isolates, onemode, symmetric\_nodes, unsorted\_edges | Synthetic |
| `twomode_random` | small | 21 | 39 | undirected | none | bipartite, symmetric\_nodes, twomode, unsorted\_edges | random bipartite graph, 12 + 9 nodes, p=0.3, seed 32 |
| `twomode_weighted` | small | 15 | 27 | undirected | integer | bipartite, integer\_weights, twomode, unsorted\_edges, weighted | random bipartite graph, 9 + 6 nodes, p=0.45, seed 41 |
| `uniform_weights` | small | 40 | 91 | undirected | real | fractional\_weights, onemode, weighted | G(n=40, p=0.12), seed 21, every weight 2.5 |
| `weighted_dir` | small | 50 | 232 | directed | integer | integer\_weights, not\_strongly\_connected, onemode, weighted | G(n=50, p=0.1), seed 15 |
| `weighted_und` | small | 50 | 133 | undirected | integer | integer\_weights, onemode, weighted | G(n=50, p=0.1), seed 16 |
| `mid_gnm_und_2000` | mid | 2000 | 10000 | undirected | none | size\_mid | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 101, undirected. [erdos1959random](references.html#erdos1959random) |
| `mid_gnm_dir_3000` | mid | 3000 | 15000 | directed | none | size\_mid | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 102, directed. [erdos1959random](references.html#erdos1959random) |
| `mid_plc_und_5000` | mid | 5000 |  | undirected | none | size\_mid | Seeded generator: Holme-Kim power-law graph with triadic closure, seed 103, undirected. [holme2002growing](references.html#holme2002growing) |
| `mid_plc_dir_4000` | mid | 4000 |  | directed | none | size\_mid | Seeded generator: Holme-Kim power-law graph with triadic closure, seed 104, directed. [holme2002growing](references.html#holme2002growing) |
| `mid_sbm_und_4000` | mid | 4000 |  | undirected | none | size\_mid | Seeded generator: stochastic block model with fixed block sizes, seed 105, undirected. [holland1983stochastic](references.html#holland1983stochastic) |
| `mid_sbm_dir_3000` | mid | 3000 |  | directed | none | size\_mid | Seeded generator: stochastic block model with fixed block sizes, seed 106, directed. [holland1983stochastic](references.html#holland1983stochastic) |
| `mid_gnm_und_int_2500` | mid | 2500 | 12000 | undirected | integer | size\_mid | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 107, undirected. [erdos1959random](references.html#erdos1959random) |
| `mid_gnm_dir_real_2500` | mid | 2500 | 12000 | directed | real | size\_mid | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 108, directed. [erdos1959random](references.html#erdos1959random) |
| `mid_plc_und_real_3000` | mid | 3000 |  | undirected | real | size\_mid | Seeded generator: Holme-Kim power-law graph with triadic closure, seed 109, undirected. [holme2002growing](references.html#holme2002growing) |
| `mid_messy_und_2000` | mid | 2000 | 9000 | undirected | none | size\_mid | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 110, undirected, with self-loops (fraction 0.01) and repeated edges (fraction 0.05). [erdos1959random](references.html#erdos1959random) |
| `mid_messy_dir_int_2000` | mid | 2000 | 9000 | directed | integer | size\_mid | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 111, directed, with self-loops (fraction 0.01) and repeated edges (fraction 0.05). [erdos1959random](references.html#erdos1959random) |
| `mid_islands_3000` | mid |  |  | undirected | none | size\_mid | Seeded generator: several components of different kinds plus isolated nodes, seed 112, undirected. |
| `mid_twomode_2500` | mid | 2500 | 9000 | undirected | none | size\_mid | Seeded generator: random two-mode graph, seed 113, undirected. |
| `mid_dense_und_1000` | mid | 1000 | 60000 | undirected | none | size\_mid | Seeded generator: dense random graph, seed 114, undirected. |
| `large_gnm_und_300k` | large | 60000 | 300000 | undirected | none | size\_large | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 201, undirected. [erdos1959random](references.html#erdos1959random) |
| `large_gnm_dir_real_250k` | large | 50000 | 250000 | directed | real | size\_large | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 202, directed. [erdos1959random](references.html#erdos1959random) |
| `large_plc_und_300k` | large | 100000 |  | undirected | none | size\_large | Seeded generator: Holme-Kim power-law graph with triadic closure, seed 203, undirected. [holme2002growing](references.html#holme2002growing) |
| `large_plc_dir_400k` | large | 100000 |  | directed | none | size\_large | Seeded generator: Holme-Kim power-law graph with triadic closure, seed 204, directed. [holme2002growing](references.html#holme2002growing) |
| `large_sbm_und_500k` | large | 100000 |  | undirected | none | size\_large | Seeded generator: stochastic block model with fixed block sizes, seed 205, undirected. [holland1983stochastic](references.html#holland1983stochastic) |
| `large_messy_und_int_200k` | large | 40000 | 190000 | undirected | integer | size\_large | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 206, undirected, with self-loops (fraction 0.01) and repeated edges (fraction 0.05). [erdos1959random](references.html#erdos1959random) |
| `large_gnm_dir_int_1m` | large | 200000 | 1000000 | directed | integer | size\_large | Seeded generator: random graph with a fixed number of edges G(n, m) (Erdos and Renyi), seed 207, directed. [erdos1959random](references.html#erdos1959random) |
| `real_mid_us_counties` | mid |  |  | undirected | none | size\_mid | Real network: US county adjacency (counties and county equivalents that share a boundary). Source: US Census Bureau, County Adjacency File, www2.census.gov/geo/docs/reference/county\_adjacency.txt. Licence: public domain (work of the US Government, 17 U.S.C. 105; US Census Bureau). |
| `real_mid_openflights_routes` | mid |  |  | directed | none | size\_mid | Real network: airline routes between airports (one directed edge per route row; parallel edges for airlines on the same pair). Source: OpenFlights.org route database, openflights.org/data.html. Licence: Open Database License 1.0 (database), Database Contents License (contents), as stated on openflights.org/data.html. |
| `real_large_clickstream_ukwiki` | large |  |  | directed | integer | size\_large | Real network: Wikimedia Clickstream, Ukrainian Wikipedia, August 2026; article-to-article link clicks (weights). Source: Wikimedia Foundation, Clickstream dataset, dumps.wikimedia.org/other/clickstream. Licence: CC0 1.0 (Wikimedia Analytics datasets, dumps.wikimedia.org/other/clickstream/readme.html). [wulczyn2015clickstream](references.html#wulczyn2015clickstream) |
| `real_large_clickstream_plwiki` | large |  |  | directed | integer | size\_large | Real network: Wikimedia Clickstream, Polish Wikipedia, August 2026; article-to-article link clicks (weights). Source: Wikimedia Foundation, Clickstream dataset, dumps.wikimedia.org/other/clickstream. Licence: CC0 1.0 (Wikimedia Analytics datasets, dumps.wikimedia.org/other/clickstream/readme.html). [wulczyn2015clickstream](references.html#wulczyn2015clickstream) |
| `real_large_clickstream_svwiki` | large |  |  | directed | integer | size\_large | Real network: Wikimedia Clickstream, Swedish Wikipedia, August 2026; article-to-article link clicks (weights). Source: Wikimedia Foundation, Clickstream dataset, dumps.wikimedia.org/other/clickstream. Licence: CC0 1.0 (Wikimedia Analytics datasets, dumps.wikimedia.org/other/clickstream/readme.html). [wulczyn2015clickstream](references.html#wulczyn2015clickstream) |

## Tolerances used {#tolerance-table}

Tolerances of the 1412 convention records, by size of the larger bound.

| Class | Records | Measures | Range used |
|---|---|---|---|
| exact (abs 0, rel 0) | 561 | 231 | abs 0 to 0, rel 0 to 0 |
| floating point, both bounds at most 1e-12 | 475 | 127 | abs 0 to 1e-12, rel 1e-15 to 1e-12 |
| floating point, larger bound above 1e-12 up to 1e-9 | 304 | 65 | abs 1e-14 to 1e-09, rel 1e-12 to 1e-09 |
| larger bound above 1e-9 up to 1e-6 | 24 | 7 | abs 1e-12 to 5e-10, rel 2e-09 to 1e-07 |
| larger bound above 1e-6 (statistical comparisons) | 48 | 18 | abs 1e-09 to 0.5, rel 0 to 0.1 |

9 of the 1986 reasons are marked `reason_incomplete`.
{% endraw %}
