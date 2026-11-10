---
title: Data and schemas
layout: default
nav_order: 7
---

{% raw %}

# Data and schemas

| File | Content |
|---|---|
| `data/tools.json` | Tools: id, name, language, version tested, license, homepage, citation key, role, how it was run. |
| `data/measures.json` | Measures: id, name, original family, concept, variant label, definition, citation keys. |
| `data/concepts.json` | Concepts: id, name, family, subfamily, definition, citation keys. A concept groups measures that are the same quantity, alternative algorithms, options or one tool's function for it. |
| `data/aliases.csv` | Old measure id to concept page and anchor (generated). Join key: `measure`. |
| `data/capabilities.csv` | Measure by tool: state, API names, comparison counts. Join keys: `measure`, `tool`. |
| `data/conventions.json` | Per measure, variant and tool: scope, call, outcome, differing conditions, normalization/direction/weights/self-loops/ties/defaults dimensions, note, tolerance. |
| `data/findings.json` | Bugs, disagreements and limitations in other tools. |
| `data/benchmarks/results.csv` | Timing and memory of other tools; method in `data/benchmarks/method.md`. |
| `data/references.bib` | BibTeX for every cited key. |

Each JSON or CSV file has a JSON Schema in `data/schema/` (draft 2020-12). `python3 scripts/build.py --check` validates all of them with a stdlib-only validator and checks the joins below, that every measure appears in exactly one concept page, and that every alias resolves to an anchor on its page. How measures were grouped into concepts and concepts into subfamilies is written down in [`data/README.md`](https://github.com/knapply/net-oracles/blob/main/data/README.md).

## Joins

- `measures.json[].concept` is `concepts.json[].id`; `aliases.csv.measure` is `measures.json[].id` and `aliases.csv.concept` is `concepts.json[].id`. The page of a measure is `aliases.csv.page` plus `#` plus `aliases.csv.anchor`.
- `capabilities.csv.measure` is `measures.json[].id`; `capabilities.csv.tool` is `tools.json[].id`.
- `conventions.json[].measure`, `.tool` use the same ids. `.variant` names one parameterization of the measure (for example normalized or weighted).
- `findings.json[].tool`, `.measure` (nullable) use the same ids.
- `benchmarks/results.csv.tool` is `tools.json[].id`.
- Citation keys in `tools.json[].citation_key`, `measures.json[].references`, `concepts.json[].references`, `findings.json[].references` and `conventions.json[].reference` are keys of `references.bib`.

## Conventions record fields

`outcome` is `agrees` (values agreed on every compared input), `differs` (they differ under `differs_when`), `no-value-on-some-inputs` (the tool returns no value or an error under `undefined_when`), or `documented` (taken from documentation). `dimensions` lists which conventions are involved. `tolerance` is the absolute and relative tolerance used when comparing: integer outputs are compared exactly, floating-point outputs within the stated bound. The structural conditions are: `loops`, `multi_edges`, `directed`, `undirected`, `disconnected`, `not_strongly_connected`, `null_graph`, `one_node`, `two_nodes`, `edgeless`, `isolates`, `symmetric_nodes`, `negative_weights`, `zero_weights`, `integer_weights`, `fractional_weights`, `weighted`, `bipartite`, `onemode`, `unsorted_edges`, `no_two_paths`, `edge_case`.
{% endraw %}
