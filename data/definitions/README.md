# Definitions of measures

`data/definitions/<family-slug>.json` holds, for every concept of one family, the precise definition from the original paper, written so that each difference between tools can be read off it. `_vocabulary.json` defines each edge case once. The schema is `data/schema/definitions.schema.json`; `python3 scripts/build.py --check` validates everything below and `python3 scripts/build.py` renders it on the concept pages (Notation, Definition with KaTeX formulas, Variants, Edge cases). `centrality.json` is the finished example: read the entries for `betweenness` (all fields), `closeness` (partial, with a note) and `centrality_table` (name only) before starting.

One worker, one file: never edit another family's file. Do not edit generated pages; run the build.

## File layout

```json
{ "family": "Centrality",
  "concepts": { "<concept id>": { ...concept... } } }
```

The file name is the family slug (lower case, runs of other characters replaced by a hyphen). A concept of the family without a key is shown as "Definition not yet written".

A concept has:

| Field | Content |
|---|---|
| `status` | `complete`, `partial` or `name_only` (below) |
| `note` | required unless complete: what is missing or why the sources do not give it |
| `notation` | list of `{symbol, meaning}`: every symbol used in the formulas, each defined once. `symbol` is LaTeX without delimiters; inline math in text is written between `\(` and `\)` |
| `formulas` | list of `{name, latex, applies_to, where}`: the published definition and each published form (raw, normalized, directed, weighted, algorithmic form). `latex` is one display formula (KaTeX 0.16, braces balanced); `where` explains the terms and the domain (what must hold for the formula to be defined) |
| `variants` | object keyed by **every** measure id of the concept: what changes in the formula for that measure (normalization constant, direction, weights, a parameter, a different object scored, a sampled sum) |
| `edge_cases` | list of `{case, definition_gives, tools}` |
| `references` | BibTeX keys of the papers the formulas come from |

`edge_cases[].case` is an id of `_vocabulary.json`. `definition_gives` says what the published definition yields, with the justification (the term of the formula that decides it), or "not defined" and why. It never says what a tool does. `tools` is keyed by tool id, only for tools that have an entry for some measure of the concept; each value is `{status, behaviour, source}` plus optional `measure` (a measure of the concept whose reasons.json record explains the entry; the cell links to it) and `finding` (a finding id; the cell links to it instead). Status: `agrees`, `differs`, `no_value`, `documented` (a documented-only tool, never run), `not_recorded`. A tool that is not listed is shown as "not recorded"; unknown is never guessed.

## Status

- `complete`: notation, formulas, a `variants` entry for each measure of the concept, and the edge cases that apply are written, and no part of the published definition is missing.
- `partial`: some of it is written; `note` names what is missing (a formula the sources do not give, a measure whose function is only known by name).
- `name_only`: the sources give only a name; write `status` and `note`, no formulas, no edge cases.

Do not fill a gap from memory when a paper or manual cannot be checked: write `partial` or `name_only` and say what is missing.

## Procedure

1. Read `README.md`, `data/README.md`, this file and the finished `centrality.json` entries named above. List your family's concepts and measures from `data/concepts.json` and `data/measures.json`.
2. For each concept, find the original paper (the keys in the concept's `references` are a start; add missing papers to `data/references.bib` with title, journal, year, volume, pages and a verified DOI, or leave the DOI out) and, for tool-specific functions, the tool's manual. Take the formula from the paper, not from a tool. Cite every paper and package; the author of this survey is Brendan Knapp.
3. Write `notation`, `formulas` and `variants`. The test: a reader who only has the formulas must be able to say which of the tools' normalizations, directions or weight readings a given output corresponds to.
4. Choose the edge cases that apply to the concept from `_vocabulary.json` (the vocabulary lists the input kinds: empty graph, single node, two nodes, too few nodes, isolates, loops, parallel edges, disconnected, directed unreachable, direction, weights, zero and negative weights, ties, complete graph, star, bipartite, parameter outside its range, degenerate group). Add a new case to the vocabulary only when none fits. For each, write `definition_gives` from the formula.
5. Draft the tool entries with `python3 scripts/draft_edge_tools.py <concept id> [case ...]`. It uses only `conventions.json`, `reasons.json`, `capabilities.csv`, `fixtures.json` and `tools.json`, picks the sentences of the convention note that speak about the case, and sets `agrees` only when the tool has agreeing records and no recorded difference and fixtures of that kind were compared. Read every draft entry against the reason text, shorten it if needed, and drop `not_recorded` entries without useful text. `--unattached` lists convention records that name no mappable input; mention them under `variants` or in `note` when they matter. Never edit behaviour into an entry that these files do not state. UCINET was never run: its entries are `documented` or absent, never `agrees`.
6. Run `python3 scripts/build.py` and then `python3 scripts/build.py --check`. Open one rendered concept page of the family (build the site locally or render the markdown with the site CSS and KaTeX) and check that every formula renders without an error box.
7. Commit with a plain message. Content rules: no company or employer names, no mention of the software that produced the comparison files, UCINET never described as checked, edge ends called source and target, author Brendan Knapp only.

## Quality bar

- Every formula is from a cited paper and states its domain. The unnormalized form and each normalization are separate formulas.
- Every measure id of the concept has a `variants` entry that says what changes, not a repetition of its name.
- Every edge case has a justification in terms of the formula ("the sum is empty", "the normalizer \((n-1)(n-2)\) is 0"), and distinguishes "not defined" from "defined, equal to a value".
- Behaviour statements carry a source and are copied from the data, not reasoned out.
- No empty or unbalanced LaTeX; every reference key is in `references.bib`; every tool and edge-case id exists.

## Example (shortened)

```json
"harmonic_centrality": {
  "status": "complete",
  "notation": [ {"symbol": "d(s,t)", "meaning": "length of a shortest path from \\(s\\) to \\(t\\); \\(\\infty\\) if unreachable"} ],
  "formulas": [ {"name": "Harmonic centrality (Marchiori and Latora 2000; Boldi and Vigna 2014)",
                 "latex": "H(v)=\\sum_{u\\ne v}\\frac{1}{d(v,u)}\\qquad\\Bigl(\\tfrac1\\infty=0\\Bigr)",
                 "applies_to": ["any", "raw"],
                 "where": "Sum of inverse distances; unreachable nodes contribute 0, so it is defined on disconnected graphs."} ],
  "variants": { "harmonic": "The formulas above, with distances out of v, into v or ignoring direction, raw or normalized." },
  "edge_cases": [ {"case": "small_n",
                   "definition_gives": "Normalization by \\(n-1\\) is 0/0 for \\(n=1\\); the raw value is 0.",
                   "tools": { "sna": {"status": "differs",
                                      "behaviour": "For a single node sna divides 0 by n - 1 = 0 and reports NaN; igraph and this reference report 0, since there are no other nodes.",
                                      "source": "conventions.json harmonic / harmonic_normalized",
                                      "measure": "harmonic"} } } ],
  "references": ["marchiori2000harmony", "boldi2014axioms"]
}
```

Backslashes are doubled in JSON strings. The rendered result is in `measures/centrality/harmonic_centrality.html`.
