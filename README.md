# net-oracles

[![pages](https://github.com/knapply/net-oracles/actions/workflows/pages.yml/badge.svg)](https://github.com/knapply/net-oracles/actions/workflows/pages.yml) [![website](https://img.shields.io/badge/website-knapply.github.io%2Fnet--oracles-2340c8)](https://knapply.github.io/net-oracles/) [![license: all rights reserved](https://img.shields.io/badge/license-all%20rights%20reserved-lightgrey)](LICENSE) [![ORCID](https://img.shields.io/badge/ORCID-0000--0003--3284--4972-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0003-3284-4972) [![last commit](https://img.shields.io/github/last-commit/knapply/net-oracles)](https://github.com/knapply/net-oracles/commits/main) [![visitors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fnet-oracles.goatcounter.com%2Fcounter%2FTOTAL.json&query=%24.count&label=visitors&color=2340c8)](https://knapply.github.io/net-oracles/) [![data: JSON + CSV](https://img.shields.io/badge/data-JSON%20%2B%20CSV-0b8a82)](llms.txt)

A neutral, citable survey of network-analysis software: which tool implements which measure, how their conventions differ (normalization, direction, weights, self-loops, ties, defaults, tolerances), which bugs and disagreements were found, and how the tools were benchmarked. It describes other tools only, and every package and paper is cited by a BibTeX key.

Browse it at <https://knapply.github.io/net-oracles/>. Programs can load the data directly; [llms.txt](llms.txt) lists every file, its schema and how the files join.

## How to navigate

- `data/` is the source of truth (JSON and CSV only, with a JSON Schema per file in `data/schema/`):
  - `tools.json`: tools, versions tested, licenses, how each was run.
  - `measures.json`: measures (one per tool function or published quantity), each with a concept, a variant label, a definition and citation keys.
  - `concepts.json`: concepts that group measures (the same quantity, alternative algorithms, options, one tool's function for it), arranged in families and subfamilies; grouping rules in `data/README.md`.
  - `aliases.csv`: every measure id mapped to its concept page and anchor (generated).
  - `capabilities.csv`: measure by tool, with a documented state vocabulary.
  - `conventions.json`: per measure, variant and tool: scope, call, outcome, conventions involved, tolerance.
  - `findings.json`: bugs, disagreements and limitations found in other tools.
  - `benchmarks/`: `method.md` and `results.csv` (other tools' results only).
  - `references.bib`: every cited key.
- `index.md`, `matrix.md`, `findings.md`, `benchmarks.md`, `references.md`, `data.md`, `tools/` and `measures/` are generated pages for the Jekyll site. `measures/` has one folder per family (an overview with a section per subfamily) and one page per concept, with a section per measure whose anchor is the measure id.

## Regenerate

```sh
python3 scripts/build.py          # validate data/ against data/schema/ and write every page
python3 scripts/build.py --check  # fail if the data is invalid, a measure is missing from its concept page, an alias does not resolve, or any generated page is stale
```

The generator uses only the Python standard library. Do not edit generated pages; edit `data/` and regenerate.

## Load the data

```python
import csv, json
tools = json.load(open("data/tools.json"))
caps = list(csv.DictReader(open("data/capabilities.csv")))
checked = [c for c in caps if c["state"].startswith("checked")]
concepts = {c["id"]: c for c in json.load(open("data/concepts.json"))}
measures = json.load(open("data/measures.json"))
by_family = [m["id"] for m in measures if concepts[m["concept"]]["family"] == "Centrality"]
```

## Cite

```bibtex
@misc{netoracles,
  title        = {net-oracles: a survey of network-analysis software, its conventions, findings and benchmarks},
  author       = {Knapp, Brendan},
  year         = {2026},
  howpublished = {\url{https://github.com/knapply/net-oracles}}
}
```

Cite the individual tools and papers with the keys in `data/references.bib`.

## Analytics

Page views on the website are counted with GoatCounter, which sets no cookies.

## License

All rights reserved, see [LICENSE](LICENSE). Quotation and citation with attribution are welcome.
