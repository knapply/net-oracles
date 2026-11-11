"""Shared helpers for fixtures, golden files, and the manifest.

Every Python oracle and engine binding imports from here, so the layout of
the corpus is defined once:

    fixtures/<name>/edges.csv, meta.json   the corpus (fixtures.py)
    manifest/<area>.yaml                 what is compared, and how
    golden/<oracle>/<fixture>/<variant>.csv  one oracle's answers
    golden/<oracle>/VERSION                the oracle version that wrote them
"""

from __future__ import annotations

import csv
import json
import os
from dataclasses import dataclass
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
# The differential fuzzer (fuzz/) points the oracles at generated
# graphs and a scratch golden directory with these variables; unset, the
# committed corpus and golden files are used.
FIXTURES = Path(os.environ.get("NETORACLES_FIXTURES_DIR") or HERE / "fixtures")
GOLDEN = Path(os.environ.get("NETORACLES_GOLDEN_DIR") or HERE / "golden")
# Comma-separated manifest keys: when set, load_area / load_manifest /
# load_manifest_by_area return only these entries, so an oracle script
# computes only what the fuzzer is shrinking.
_ONLY = {k for k in os.environ.get("NETORACLES_MANIFEST_ONLY", "").split(",") if k}


def _only(entries: dict) -> dict:
    return {k: v for k, v in entries.items() if k in _ONLY} if _ONLY else entries
MANIFEST_DIR = HERE / "manifest"

# Fixture tags that manifest entries may name in `differs_when` and
# `undefined_when`. `directed` and `undirected` are added from meta.json;
# the rest are written by fixtures.py (and computed the same way
# for generated graphs by fuzz/generators.py), all but
# `edge_case` by `structure_tags`.
TAGS = {"directed", "undirected", "weighted", "integer_weights", "loops",
        "multi_edges", "disconnected", "edge_case", "twomode",
        "null_graph", "one_node", "two_nodes", "edgeless", "isolates",
        "negative_weights", "zero_weights", "not_strongly_connected", "bipartite",
        "symmetric_nodes", "unsorted_edges", "onemode", "no_two_paths",
        "fractional_weights"}


def structure_tags(n: int, edges: list[tuple[int, int]], directed: bool,
                   weights: list[float] | None, types: list[int] | None) -> set[str]:
    """The tags a graph's structure implies (every tag of TAGS except
    `directed`, `undirected` and `edge_case`), so that a convention declared
    with `differs_when` / `undefined_when` applies alike to the corpus and to
    generated graphs:

    weighted, integer_weights, fractional_weights, negative_weights,
    zero_weights       weights given; all whole numbers; some not a whole
                       number; some < 0; some == 0
    loops, multi_edges self-loops; parallel edges (same direction if directed)
    disconnected       more than one weak component (n > 0)
    not_strongly_connected  directed, n > 0, not strongly connected
    null_graph, one_node, two_nodes   n = 0, 1, 2
    edgeless           no edges (the null graph included)
    isolates           a node without edges to other nodes (n > 0)
    no_two_paths       no node has two distinct neighbours (ignoring
                       direction and loops): no connected triple
    bipartite          no self-loop and no odd cycle ignoring direction
                       (n > 0)
    symmetric_nodes    colour refinement (1-dimensional Weisfeiler-Leman on
                       the multigraph: loops, out- and in-neighbour colours
                       with multiplicity; weights ignored), on the graph or,
                       for a directed one, on its undirected reading, leaves
                       two nodes with the same colour. Every nontrivial automorphism
                       does (regular graphs, twins, mirror images), so
                       spectra with repeated eigenvalues and exact ties
                       between symmetric positions are covered, together
                       with some graphs that only look alike to refinement
    unsorted_edges     the edge list is not in increasing order of (source,
                       target), (min, max) when undirected: NetworkX then
                       lists some node's neighbours out of node order
    twomode, onemode   node types given or not
    """
    tags: set[str] = set()
    if weights is not None:
        tags.add("weighted")
        if all(float(w).is_integer() for w in weights):
            tags.add("integer_weights")
        else:
            tags.add("fractional_weights")
        if any(float(w) < 0 for w in weights):
            tags.add("negative_weights")
        if any(float(w) == 0 for w in weights):
            tags.add("zero_weights")
    tags.add("twomode" if types is not None else "onemode")
    if n == 0:
        tags.add("null_graph")
    elif n == 1:
        tags.add("one_node")
    elif n == 2:
        tags.add("two_nodes")
    if not edges:
        tags.add("edgeless")
    keys = [(a, b) if directed else (min(a, b), max(a, b)) for a, b in edges]
    if any(a == b for a, b in edges):
        tags.add("loops")
    if len(set(keys)) < len(keys):
        tags.add("multi_edges")
    if keys != sorted(keys):
        tags.add("unsorted_edges")
    nbrs: list[set[int]] = [set() for _ in range(n)]
    for a, b in edges:
        if a != b:
            nbrs[a].add(b)
            nbrs[b].add(a)
    if n > 0:
        if any(not s for s in nbrs):
            tags.add("isolates")
        if _components(n, nbrs) > 1:
            tags.add("disconnected")
        if directed:
            succ: list[set[int]] = [set() for _ in range(n)]
            pred: list[set[int]] = [set() for _ in range(n)]
            for a, b in edges:
                succ[a].add(b)
                pred[b].add(a)
            if not (_reaches_all(n, succ) and _reaches_all(n, pred)):
                tags.add("not_strongly_connected")
        if "loops" not in tags and _two_colourable(n, nbrs):
            tags.add("bipartite")
    if all(len(s) <= 1 for s in nbrs):
        tags.add("no_two_paths")
    if _refinement_ties(n, edges, directed) or (directed and _refinement_ties(n, edges, False)):
        tags.add("symmetric_nodes")
    return tags


def _components(n: int, nbrs) -> int:
    seen, count = [False] * n, 0
    for start in range(n):
        if seen[start]:
            continue
        count += 1
        seen[start] = True
        stack = [start]
        while stack:
            v = stack.pop()
            for u in nbrs[v]:
                if not seen[u]:
                    seen[u] = True
                    stack.append(u)
    return count


def _reaches_all(n: int, adj) -> bool:
    seen = [False] * n
    seen[0] = True
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if not seen[u]:
                seen[u] = True
                stack.append(u)
    return all(seen)


def _two_colourable(n: int, nbrs) -> bool:
    side = [-1] * n
    for start in range(n):
        if side[start] >= 0:
            continue
        side[start] = 0
        stack = [start]
        while stack:
            v = stack.pop()
            for u in nbrs[v]:
                if side[u] < 0:
                    side[u] = 1 - side[v]
                    stack.append(u)
                elif side[u] == side[v]:
                    return False
    return True


def _refinement_ties(n: int, edges, directed: bool) -> bool:
    """Whether colour refinement leaves two nodes with the same colour."""
    if n < 2:
        return False
    out: list[list[int]] = [[] for _ in range(n)]
    inc: list[list[int]] = [[] for _ in range(n)]
    loops = [0] * n
    for a, b in edges:
        if a == b:
            loops[a] += 1
        elif directed:
            out[a].append(b)
            inc[b].append(a)
        else:
            out[a].append(b)
            out[b].append(a)
    colour = [0] * n
    signature = [(loops[v], len(out[v]), len(inc[v])) for v in range(n)]
    classes = 0
    while True:
        ids: dict = {}
        colour = [ids.setdefault(sig, len(ids)) for sig in signature]
        if len(ids) == classes:
            break
        classes = len(ids)
        signature = [(colour[v], tuple(sorted(colour[u] for u in out[v])),
                      tuple(sorted(colour[u] for u in inc[v]))) for v in range(n)]
    return classes < n

# Comparison modes a manifest entry may ask for (see compare.py).
COMPARE_MODES = {"values", "sorted", "partition", "sets", "ge", "le"}


@dataclass
class Fixture:
    name: str
    n: int
    directed: bool
    weighted: bool
    tags: list[str]
    src: list[int]
    tgt: list[int]
    weights: list[float] | None


def load_fixture(name: str) -> Fixture:
    d = FIXTURES / name
    meta = json.loads((d / "meta.json").read_text())
    src, tgt, w = [], [], []
    with open(d / "edges.csv", newline="") as fh:
        for row in csv.DictReader(fh):
            src.append(int(row["from"]))
            tgt.append(int(row["to"]))
            if meta["weighted"]:
                w.append(float(row["weight"]))
    return Fixture(name, meta["n"], meta["directed"], meta["weighted"], meta["tags"],
                   src, tgt, w if meta["weighted"] else None)


def fixture_names() -> list[str]:
    return sorted(p.name for p in FIXTURES.iterdir() if (p / "meta.json").exists())


# Convention checks (README "Convention presets"): engine runs with a
# reference tool's convention, compared with the golden files of another
# entry. Their oracle keys name `<oracle>/<variant>`, so no oracle script
# computes them; only compare.py and check_manifest.py read this file.
PRESETS = "presets"


def manifest_files(include_presets: bool = False) -> list[Path]:
    """Every manifest file, in name order (presets.yaml only on request)."""
    return sorted(p for p in MANIFEST_DIR.glob("*.yaml")
                  if include_presets or p.stem != PRESETS)


def golden_source(oracle: str, variant: str) -> tuple[str, str]:
    """The (oracle, variant) whose golden files an oracle key reads: a key
    `<oracle>/<variant>` reads another entry's files."""
    if "/" in oracle:
        base, other = oracle.split("/", 1)
        return base, other
    return oracle, variant


def _read_manifest_file(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}



def load_area(area: str) -> dict:
    """The manifest entries of one area (manifest/<area>.yaml)."""
    return _only(_read_manifest_file(MANIFEST_DIR / f"{area}.yaml"))


def load_manifest(include_presets: bool = False) -> dict:
    """Every manifest entry, in file order; a key may appear only once."""
    manifest: dict = {}
    for path in manifest_files(include_presets):
        for key, spec in _read_manifest_file(path).items():
            if key in manifest:
                raise ValueError(f"measure {key!r} is defined twice (in {path.name})")
            manifest[key] = spec
    return _only(manifest)


def load_manifest_by_area(include_presets: bool = False) -> dict[str, dict]:
    """Area (manifest file stem) -> its entries, in file order."""
    areas: dict[str, dict] = {}
    seen: set[str] = set()
    for path in manifest_files(include_presets):
        entries = _read_manifest_file(path)
        for key in entries:
            if key in seen:
                raise ValueError(f"measure {key!r} is defined twice (in {path.name})")
            seen.add(key)
        areas[path.stem] = _only(entries)
    return areas


def applies(variant: dict, fx: Fixture) -> bool:
    kind = variant.get("applies_to", "any")
    if kind == "directed" and not fx.directed:
        return False
    if kind == "undirected" and fx.directed:
        return False
    if variant.get("requires_weights") and not fx.weighted:
        return False
    return True


def write_values(oracle: str, fixture: str, variant: str, values) -> None:
    """Writes one value per line. A value may be a number or a sequence of
    numbers (written space-separated, e.g. one clique per line)."""
    d = GOLDEN / oracle / fixture
    d.mkdir(parents=True, exist_ok=True)
    with open(d / f"{variant}.csv", "w", newline="") as fh:
        fh.write("value\n")
        for v in values:
            if isinstance(v, (list, tuple)):
                fh.write(" ".join(f"{float(x):.17g}" for x in v) + "\n")
            else:
                fh.write(f"{float(v):.17g}\n")


def write_version(oracle: str, version: str) -> None:
    """Records which oracle version produced golden/<oracle>/ (shown in
    REPORT.md). Every oracle script calls this once, after writing."""
    (GOLDEN / oracle).mkdir(parents=True, exist_ok=True)
    (GOLDEN / oracle / "VERSION").write_text(version.rstrip("\n") + "\n", newline="")


DEFINITION_VERSION = "definition (direct evaluation, exact arithmetic)"


def read_values(oracle: str, fixture: str, variant: str):
    """Numbers, or tuples of numbers for lines holding several values."""
    p = GOLDEN / oracle / fixture / f"{variant}.csv"
    if not p.exists():
        return None
    out = []
    with open(p) as fh:
        next(fh)
        for line in fh:
            # R writes missing values as NA; they are undefined, like NaN.
            parts = ["nan" if x == "NA" else x for x in line.split()]
            if not parts:
                # An empty line is an empty group (e.g. no members).
                out.append(())
            elif len(parts) == 1:
                out.append(float(parts[0]))
            else:
                out.append(tuple(float(x) for x in parts))
    return out
