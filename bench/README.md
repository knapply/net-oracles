# Shared benchmark runner

One command line for every tool, one runner, one results format (`data/benchmarks/results.csv`).

    pip install numpy pyyaml
    python3 bench/run.py --suite smoke --tools networkx --out /tmp/results.csv
    python3 bench/run.py --list          # adapters, suites, measures
    python3 bench/run.py --check         # adapters against measures.yaml

- `adapters/<tool>.py` (or `.R`): one adapter per tool. Run alone: `python3 bench/adapters/networkx.py --measure bfs --graph PATH --threads 1 --reps 3` prints one JSON line (tool, tool_version, measure, graph, threads, seconds list, peak_megabytes, status `ok|timeout|error|unsupported`, digest of the result).
- `measures.yaml`: measure ids, the label written to the CSV, repeats, and the call each adapter makes. `graphs.yaml`: suites of graphs (seeded generators; downloads pinned by sha256).
- `run.py`: builds the graphs, then runs every (tool, graph, measure) in a fresh process with a timeout; takes wall time and peak resident memory of the child from the operating system (rusage), the adapter's own measure-only times and memory above its pre-load baseline, the median of the repeats, the environment (CPU, cores offered, memory), and appends rows to `--out` (raw JSON lines next to it, or `--raw`).
- `--adapters-dir DIR` (repeatable): load more adapters from outside this repository; a same-named file overrides the one here.
- Graph files (`*.edges`): `NETEDGE1`, node count and directed flag (u64 each), then u32 pairs, little-endian. `PATH.sources` lists the 16 seeded search sources, so every language uses the same ones.
- `merge_hosted.py` and `.github/workflows/bench.yml`: hosted runs; see `data/benchmarks/method.md`.

## Add a tool in one file

Checklist, for people and for language models:

1. Copy `adapters/_template.py` to `adapters/<tool>.py` (the file name is the adapter name; `tool` inside is the id in `data/tools.json`). For R, copy `adapters/igraph.R`.
2. Implement `version()`, `load(ctx)` (build the tool's graph from `ctx.edges`, an `(m, 2)` uint32 array; `ctx.n`, `ctx.directed`) and `threads(requested)` (0 means every CPU offered; return the number used).
3. Put one callable per measure in `calls`, `calls[id](G, ctx) -> digest dict` (the call is what is timed). Measure ids are the keys of `measures.yaml`. Leave out what the tool cannot do, or `raise NotImplementedError("why")`: that is recorded as `unsupported`, not as a failure.
4. Use the tool only through its public interface, and apply the conventions in `measures.yaml` (damping 0.85, tolerance 1e-6, at most 100 iterations; BFS from `ctx.sources[0]`; betweenness from `ctx.sources`).
5. Digest: small, deterministic numbers (counts, sums rounded to 6 digits with `sig`, `vec`) so tools can be compared; the runner warns when two tools differ on a shared key.
6. Add the call text per measure under the tool's name in `measures.yaml`, then `python3 bench/run.py --check` and `python3 bench/run.py --suite tiny --tools <tool> --out /tmp/t.csv`.
7. Name the tool in `data/tools.json` if it is not there, and run `python3 scripts/build.py --check`.

An adapter named like its tool (`networkx.py`) is fine: the template removes its own directory from `sys.path` so the real package is imported.
Adapters that need an extra interpreter read `BENCH_PYTHON_<NAME>` (for example `GRAPH_TOOL_PY` for graph-tool). Anything an adapter builds is cached next to the graph in `--prepare`, which is not measured.
