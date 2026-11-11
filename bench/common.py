"""Shared helpers for Python adapters.

An adapter is one file in bench/adapters/ that defines a class and ends with
`main(Adapter)`. The command line is the same for every adapter:

    python3 bench/adapters/<tool>.py --measure ID --graph PATH --threads T --reps R

and it prints one JSON line (see `report`). Other options: `--list` prints the
measure ids the adapter implements, `--prepare` builds anything the adapter
caches next to the graph (not measured), `--budget S` stops repeating once the
calls so far took more than half of S seconds.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import os
import random
import sys
import time

MAGIC = b"NETEDGE1"
HEADER = 24


# ---- graph files -------------------------------------------------------------

def read_header(path):
    """(n, directed) from the header of an edge file."""
    with open(path, "rb") as f:
        head = f.read(HEADER)
    if head[:8] != MAGIC:
        raise ValueError("not an edge file: " + path)
    return int.from_bytes(head[8:16], "little"), bool(int.from_bytes(head[16:24], "little"))


def read_edges(path):
    """(n, directed, edges): `edges` is an (m, 2) uint32 array. File layout: the
    8 bytes NETEDGE1, node count (u64), directed flag (u64), then m pairs of u32,
    all little-endian."""
    import numpy as np
    with open(path, "rb") as f:
        head = f.read(HEADER)
    if head[:8] != MAGIC:
        raise ValueError("not an edge file: " + path)
    n = int.from_bytes(head[8:16], "little")
    directed = bool(int.from_bytes(head[16:24], "little"))
    return n, directed, np.fromfile(path, dtype="<u4", offset=HEADER).reshape(-1, 2)


def write_edges(path, n, directed, u, v):
    import numpy as np
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".part"
    with open(tmp, "wb") as f:
        f.write(MAGIC + int(n).to_bytes(8, "little") + int(bool(directed)).to_bytes(8, "little"))
        np.stack([u, v], axis=1).astype("<u4").tofile(f)
    os.replace(tmp, path)


def pick_sources(edges, n, seed, k=16, graph_path=None):
    """k search sources among nodes with at least one edge, drawn once per graph (seeded
    by the graph name, so every tool uses the same ones; the runner writes them to
    PATH.sources so that adapters in other languages read the same list)."""
    import numpy as np
    if graph_path and os.path.exists(graph_path + ".sources"):  # written by the runner, read by every language
        return [int(x) for x in open(graph_path + ".sources").read().split()]
    live = np.flatnonzero(np.bincount(edges.ravel(), minlength=n))
    rng = random.Random(seed)
    return sorted(int(live[i]) for i in rng.sample(range(len(live)), min(k, len(live))))


# ---- memory -------------------------------------------------------------------

def status_kb(key):
    try:
        with open("/proc/self/status") as f:
            for line in f:
                if line.startswith(key):
                    return float(line.split()[1])
    except OSError:
        pass
    return float("nan")


def rss_mb():
    return status_kb("VmRSS:") / 1024


def peak_mb():
    return status_kb("VmHWM:") / 1024


def reset_peak():
    try:
        with open("/proc/self/clear_refs", "w") as f:
            f.write("5")
    except OSError:
        pass


# ---- digests ------------------------------------------------------------------

def sig(x, digits=6):
    """x rounded to `digits` significant digits (so tools agree to rounding)."""
    x = float(x)
    if x == 0 or not math.isfinite(x):
        return x if math.isfinite(x) else str(x)
    return float(f"{x:.{digits}g}")


def vec(values):
    """Digest of a per-node vector: its sum and maximum."""
    vals = [float(x) for x in values if math.isfinite(float(x))]  # isolated nodes give nan in some tools
    return {"sum": sig(sum(vals)), "max": sig(max(vals)) if vals else 0.0}


# ---- driver -------------------------------------------------------------------

class Context:
    def __init__(self, n, directed, edges, sources, threads):
        self.n, self.directed, self.edges, self.sources, self.threads = n, directed, edges, sources, threads


class Adapter:
    """Subclass and set `tool`; implement `version`, `load`, and put one callable per
    measure id in `calls`: `calls[id](G, ctx) -> digest dict` (the call is timed)."""
    tool = ""
    calls: dict = {}
    note = ""

    def version(self):
        raise NotImplementedError

    def threads(self, requested):
        """Set the thread count (0 = every CPU offered) and return the count in use."""
        return 1

    def load(self, ctx):
        """Build the tool's graph from ctx.edges (timed as the `load` measure)."""
        raise NotImplementedError

    def prepare(self, graph_path):
        pass


def report(a, args, extra):
    row = {"tool": a.tool, "tool_version": "", "measure": args.measure, "graph": os.path.basename(args.graph),
           "threads": args.threads, "seconds": [], "peak_megabytes": None, "status": "ok", "digest": {}, "note": ""}
    row.update(extra)
    print(json.dumps(row), flush=True)


def parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("--measure")
    ap.add_argument("--graph")
    ap.add_argument("--threads", type=int, default=0)
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--budget", type=float, default=0)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--prepare", action="store_true")
    return ap


def _main(cls):
    args = parser().parse_args()
    a = cls()
    if args.list:
        print(json.dumps(sorted(["load"] + list(a.calls))))
        return 0
    if args.prepare:
        a.prepare(args.graph)
        return 0
    if args.measure != "load" and args.measure not in a.calls:
        report(a, args, {"status": "unsupported"})
        return 0
    try:
        version = a.version()
        used = a.threads(args.threads)
    except Exception as e:  # tool missing or broken
        report(a, args, {"status": "error", "note": f"{type(e).__name__}: {str(e)[:200]}"})
        return 0
    gc.collect()
    base = rss_mb()  # interpreter and the tool's modules, before the graph is read
    extra = {"tool_version": version, "threads": used, "base_megabytes": round(base, 1)}
    try:
        n, directed, edges = read_edges(args.graph)
        ctx = Context(n, directed, edges, pick_sources(edges, n, os.path.basename(args.graph), graph_path=args.graph), used)
        extra.update(nodes=n, edges=int(len(edges)))
        times, digest = [], {}
        if args.measure == "load":
            reset_peak()
            for r in range(args.reps):
                t = time.perf_counter()
                G = a.load(ctx)
                gc.collect()
                times.append(time.perf_counter() - t)
                if r == 0:
                    extra["peak_megabytes"] = round(max(peak_mb() - base, 0), 1)
                    extra["graph_megabytes"] = round(max(rss_mb() - base, 0), 1)
                if r < args.reps - 1:
                    del G
                    gc.collect()
                if args.budget and sum(times) > args.budget / 2:
                    break
        else:
            G = a.load(ctx)
            del ctx.edges
            ctx.edges = None
            del edges
            gc.collect()
            reset_peak()
            call = a.calls[args.measure]
            for _ in range(args.reps):
                t = time.perf_counter()
                digest = call(G, ctx)
                times.append(time.perf_counter() - t)
                if args.budget and sum(times) > args.budget / 2:
                    break
            extra["peak_megabytes"] = round(max(peak_mb() - base, 0), 1)
        report(a, args, extra | {"seconds": [round(x, 6) for x in times], "digest": digest or {}, "note": a.note})
    except NotImplementedError as e:
        report(a, args, extra | {"status": "unsupported", "note": str(e)[:200]})
    except MemoryError:
        report(a, args, extra | {"status": "error", "note": "MemoryError"})
    except Exception as e:  # a tool's own failure is recorded, not hidden
        report(a, args, extra | {"status": "error", "note": f"{type(e).__name__}: {str(e)[:200]}"})
    return 0


def main(cls):
    sys.exit(_main(cls))
