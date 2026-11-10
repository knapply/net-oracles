# net-oracles

A neutral, citable survey of network-analysis software: which tool implements which measure, how their conventions differ (normalization, direction, weights, self-loops, ties, defaults, tolerances), which bugs and disagreements were found, and how the tools were benchmarked. It describes other tools only, and every package and paper is cited by a BibTeX key.

Browse it at <https://knapply.github.io/net-oracles/>. Programs can load the data directly; [llms.txt](llms.txt) lists every file, its schema and how the files join.

## How to navigate

- `data/` is the source of truth (JSON and CSV only, with a JSON Schema per file in `data/schema/`):
  - `tools.json`: tools, versions tested, licenses, how each was run.
  - `measures.json`: measures grouped in families, with definitions and citation keys.
  - `capabilities.csv`: measure by tool, with a documented state vocabulary.
  - `conventions.json`: per measure, variant and tool: scope, call, outcome, conventions involved, tolerance.
  - `findings.json`: bugs, disagreements and limitations found in other tools.
  - `benchmarks/`: `method.md` and `results.csv` (other tools' results only).
  - `references.bib`: every cited key.
- `index.md`, `matrix.md`, `findings.md`, `benchmarks.md`, `references.md`, `data.md`, `tools/` and `measures/` are generated pages for the Jekyll site.

## Regenerate

```sh
python3 scripts/build.py          # validate data/ against data/schema/ and write every page
python3 scripts/build.py --check  # fail if the data is invalid or any generated page is stale
```

The generator uses only the Python standard library. Do not edit generated pages; edit `data/` and regenerate.

## Load the data

```python
import csv, json
tools = json.load(open("data/tools.json"))
caps = list(csv.DictReader(open("data/capabilities.csv")))
checked = [c for c in caps if c["state"].startswith("checked")]
```

## Cite

```bibtex
@misc{netoracles,
  title        = {net-oracles: a survey of network-analysis software, its conventions, findings and benchmarks},
  author       = {{net-oracles contributors}},
  year         = {2026},
  howpublished = {\url{https://github.com/knapply/net-oracles}}
}
```

Cite the individual tools and papers with the keys in `data/references.bib`.
