"""Graph suites: seeded generators and checked downloads, written as edge files (see common.py)."""
from __future__ import annotations

import gzip
import hashlib
import os
import re
import shutil
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

DESCRIPTION = {
    "kron": "R-MAT (Graph500 parameters a=0.57, b=0.19, c=0.19; edge factor 16), 2^{scale} nodes, seed {seed}; "
            "self-loops and duplicates dropped, undirected, node ids randomly permuted",
    "urand": "uniform random pairs (edge factor 8), 2^{scale} nodes, seed {seed}; self-loops and duplicates "
             "dropped, undirected, node ids randomly permuted",
    "road": "square lattice {side}x{side} with 10% of edges removed at random, seed {seed}; node ids randomly permuted",
    "lfr": "LFR benchmark (NetworKit LFRGenerator), 2^{scale} nodes, average degree 20, degree exponent 2.5, "
           "community sizes exponent 1.5, mixing 0.3, seed {seed}",
}


def simple_undirected(n, a, b, rng):
    """Drop self-loops and duplicates, orient u < v, permute node ids."""
    import numpy as np
    keep = a != b
    a, b = a[keep], b[keep]
    lo, hi = np.minimum(a, b).astype(np.int64), np.maximum(a, b).astype(np.int64)
    key = np.unique(lo * n + hi)
    perm = rng.permutation(n)
    return perm[key // n], perm[key % n]


def generate(family: str, scale: int, seed: int, path: str) -> dict:
    """Write the generated graph to `path`; returns its description."""
    import numpy as np
    rng = np.random.Generator(np.random.PCG64(seed))
    fmt = {"scale": scale, "seed": seed}
    if family == "kron":
        n, m = 1 << scale, 16 << scale
        a = np.zeros(m, dtype=np.int64)
        b = np.zeros(m, dtype=np.int64)
        for bit in range(scale):
            r1, r2 = rng.random(m), rng.random(m)
            ib = r1 > 0.57 + 0.19  # c+d quadrants: source bit set
            jb = r2 < np.where(ib, 0.05 / 0.24, 0.19 / 0.76)  # b or d quadrant: target bit set
            a |= ib.astype(np.int64) << bit
            b |= jb.astype(np.int64) << bit
        u, v = simple_undirected(n, a, b, rng)
    elif family == "urand":
        n, m = 1 << scale, 8 << scale
        u, v = simple_undirected(n, rng.integers(0, n, m), rng.integers(0, n, m), rng)
    elif family == "road":
        side = 1 << (scale // 2)
        n = side * side
        fmt["side"] = side
        idx = np.arange(n).reshape(side, side)
        a = np.concatenate([idx[:, :-1].ravel(), idx[:-1, :].ravel()])
        b = np.concatenate([idx[:, 1:].ravel(), idx[1:, :].ravel()])
        keep = rng.random(len(a)) >= 0.10
        u, v = simple_undirected(n, a[keep], b[keep], rng)
    elif family == "lfr":
        import networkit as nk
        n = 1 << scale
        maxdeg, maxc = (100, 300) if scale <= 12 else (200, 1000)
        nk.setNumberOfThreads(1)
        try:
            nk.engineering.setSeed(seed, False)
        except AttributeError:
            nk.setSeed(seed, False)
        gen = nk.generators.LFRGenerator(n)
        gen.generatePowerlawDegreeSequence(20, maxdeg, -2.5)
        gen.generatePowerlawCommunitySizeSequence(20, maxc, -1.5)
        gen.setMu(0.3)
        e = np.array(list(gen.generate().iterEdges()), dtype=np.int64).reshape(-1, 2)
        u, v = simple_undirected(n, e[:, 0], e[:, 1], rng)
    else:
        raise ValueError("unknown family " + family)
    common.write_edges(path, n, False, u, v)
    return {"nodes": int(n), "edges": int(len(u)), "directed": False, "source": DESCRIPTION[family].format(**fmt)}


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def download(spec: dict, path: str, allow_unpinned: bool = False) -> dict:
    """Fetch spec['url'], check spec['sha256'], and convert the edge list (text, one 'u v' per
    line, '#' comments, ids renumbered densely; undirected unless spec['directed']) to `path`."""
    import numpy as np
    raw = path + ".download"
    if not os.path.exists(raw):
        with urllib.request.urlopen(spec["url"], timeout=600) as r, open(raw + ".part", "wb") as f:
            shutil.copyfileobj(r, f, 1 << 20)
        os.replace(raw + ".part", raw)
    got = sha256(raw)
    want = spec.get("sha256") or ""
    if want != got:
        if want or not allow_unpinned:
            os.remove(raw)
            raise RuntimeError(f"sha256 of {spec['url']} is {got}, expected {want or '(none pinned)'}")
        print(f"unpinned download {spec['url']}: sha256 {got}", file=sys.stderr)
    op = gzip.open if spec["url"].endswith(".gz") else open
    with op(raw, "rt") as f:
        rows = [tuple(map(int, ln.split()[:2])) for ln in f if ln.strip() and not ln.startswith(("#", "%"))]
    arr = np.array(rows, dtype=np.int64)
    ids, inv = np.unique(arr, return_inverse=True)
    arr = inv.reshape(-1, 2)
    arr = arr[arr[:, 0] != arr[:, 1]]
    directed = bool(spec.get("directed"))
    if not directed:
        arr = np.unique(np.sort(arr, axis=1), axis=0)
    else:
        arr = np.unique(arr, axis=0)
    common.write_edges(path, len(ids), directed, arr[:, 0], arr[:, 1])
    return {"nodes": int(len(ids)), "edges": int(len(arr)), "directed": directed,
            "source": f"{spec['url']} (sha256 {got[:16]}), self-loops and duplicates dropped, ids renumbered"}


def generate_gnm(nodes: int, degree: float, seed: int, path: str) -> dict:
    """Uniform random undirected graph on `nodes` nodes with about nodes*degree/2 edges (for model fits)."""
    import numpy as np
    rng = np.random.Generator(np.random.PCG64(seed))
    m = int(nodes * degree / 2)
    u, v = simple_undirected(nodes, rng.integers(0, nodes, 2 * m), rng.integers(0, nodes, 2 * m), rng)
    u, v = u[:m], v[:m]
    common.write_edges(path, nodes, False, u, v)
    return {"nodes": int(nodes), "edges": int(len(u)), "directed": False,
            "source": f"uniform random graph, {nodes} nodes, about {degree:g} average degree, seed {seed}; duplicates and self-loops dropped"}


def export_rdata(dataset: str, path: str) -> dict:
    """Export a dataset of an R package (data/export_statnet.R) and write wave 1 as an edge file; the
    waves, ties and node attributes stay next to it in PATH.raw/ for adapters that read tables."""
    import subprocess
    import numpy as np
    raw = path + ".raw"
    here = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(["Rscript", os.path.join(here, "data", "export_statnet.R"), dataset, raw], check=True)
    meta = open(os.path.join(raw, "meta.tsv")).read().split("\n")[1].split("\t")
    n, directed = int(meta[0]), bool(int(meta[1]))
    rows = [ln.split("\t") for ln in open(os.path.join(raw, "edges.tsv")).read().splitlines()[1:]]
    w1 = np.array([(int(r[1]) - 1, int(r[2]) - 1) for r in rows if r[0] == "1"], dtype=np.int64).reshape(-1, 2)
    w1 = w1[w1[:, 0] != w1[:, 1]]
    if not directed:
        w1 = np.unique(np.sort(w1, axis=1), axis=0)
    common.write_edges(path, n, directed, w1[:, 0], w1[:, 1])
    return {"nodes": n, "edges": int(len(w1)), "directed": directed, "source": f"R dataset {dataset}, wave 1 as the edge file"}


def materialize(name: str, spec: dict, seed: int, cache: str, allow_unpinned: bool = False) -> str:
    """Path of graph `name` in `cache`, built on first use (with PATH.sources, the search sources)."""
    os.makedirs(cache, exist_ok=True)
    path = os.path.join(cache, name + ".edges")
    if not os.path.exists(path):
        if spec.get("family") == "gnm":
            info = generate_gnm(int(spec["nodes"]), float(spec["degree"]), seed + int(spec["nodes"]), path)
        elif spec.get("family") == "rdata":
            info = export_rdata(spec["dataset"], path)
        elif "family" in spec:
            fam, scale = spec["family"], int(spec["scale"])
            info = generate(fam, scale, seed + scale, path)
        else:
            info = download(spec["download"], path, allow_unpinned)
        with open(path + ".txt", "w") as f:
            f.write(info["source"] + "\n")
    if not os.path.exists(path + ".sources"):
        n, _, edges = common.read_edges(path)
        src = common.pick_sources(edges, n, os.path.basename(path))
        with open(path + ".sources", "w") as f:
            f.write("\n".join(map(str, src)) + "\n")
    return path
