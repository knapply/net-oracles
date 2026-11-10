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

{{STATE_SECTIONS}}

## Reasons {#reasons}

Every entry whose state is not `checked-agrees` has a record in `data/reasons.json`, with a plain-words `reason` and a one-sentence `short` form used in tooltips and tables. `python3 scripts/build.py --check` fails if such an entry has no reason, or if the reason lacks the content its state requires. Where the sources used for this survey do not say everything the state requires (for example when the cause of a difference was not traced), the record has `reason_incomplete: true` and `missing` says what is not known; those entries are marked on every page that shows them.

## Fixtures {#fixtures}

{{FIXTURES}}

## Tolerances used {#tolerance-table}

{{TOLERANCES}}
