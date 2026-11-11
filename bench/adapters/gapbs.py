#!/usr/bin/env python3
"""GAP Benchmark Suite reference implementation (https://github.com/sbeamer/gapbs), C++ with OpenMP.

The adapter converts the graph to the suite's serialized format once (--prepare, not measured), then
runs the suite's own kernel binary and reads the per-trial times it prints (the suite times only the
kernel). The binaries are built from the commit in bench/gapbs.pin into $GAPBS_DIR (default
~/.cache/net-oracles-bench/gapbs). Memory is the peak of the whole process tree, taken by the runner.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != HERE]
sys.path.insert(0, os.path.join(HERE, ".."))
import common  # noqa: E402

KERNELS = {"bfs": "bfs", "components": "cc", "pagerank": "pr", "betweenness": "bc", "triangles": "tc"}
REPO = "https://github.com/sbeamer/gapbs.git"
DIR = os.environ.get("GAPBS_DIR", os.path.expanduser("~/.cache/net-oracles-bench/gapbs"))


def pin():
    with open(os.path.join(HERE, "..", "gapbs.pin")) as f:
        return f.read().split()[0]


def build():
    if os.path.exists(os.path.join(DIR, "converter")) and os.path.exists(os.path.join(DIR, ".pin-" + pin())):
        return
    if not os.path.exists(os.path.join(DIR, "Makefile")):
        os.makedirs(os.path.dirname(DIR), exist_ok=True)
        subprocess.run(["git", "clone", "-q", REPO, DIR], check=True)
    subprocess.run(["git", "-C", DIR, "checkout", "-q", pin()], check=True)
    subprocess.run(["make", "-C", DIR, "-j", str(os.cpu_count() or 2), "converter", *KERNELS.values()],
                   check=True, stdout=subprocess.DEVNULL)
    open(os.path.join(DIR, ".pin-" + pin()), "w").close()


def prepare(path):
    import numpy as np
    build()
    n, directed, edges = common.read_edges(path)
    el = path + ".el"
    with open(el, "w") as f:
        for i in range(0, len(edges), 1 << 20):
            np.savetxt(f, edges[i:i + (1 << 20)], fmt="%d")
    del edges
    outs = [(path + ".sg", [] if directed else ["-s"])]
    if directed:
        outs.append((path + ".sym.sg", ["-s"]))
    for out, flags in outs:
        subprocess.run([os.path.join(DIR, "converter"), "-f", el, *flags, "-b", out], check=True, stdout=subprocess.DEVNULL)
    os.remove(el)


def main():
    args = common.parser().parse_args()
    if args.list:
        print(json.dumps(sorted(KERNELS)))
        return
    if args.prepare:
        return prepare(args.graph)
    row = {"tool": "gapbs", "tool_version": pin()[:12], "measure": args.measure, "graph": os.path.basename(args.graph),
           "threads": args.threads, "seconds": [], "peak_megabytes": None, "status": "ok", "digest": {}, "note": ""}
    if args.measure not in KERNELS:
        row["status"] = "unsupported"
        return print(json.dumps(row))
    threads = args.threads or len(os.sched_getaffinity(0))
    row["threads"] = threads
    n, directed = common.read_header(args.graph)
    src = common.pick_sources(None, n, os.path.basename(args.graph), graph_path=args.graph)  # needs PATH.sources
    k = KERNELS[args.measure]
    sg = args.graph + (".sym.sg" if (k in ("cc", "tc") and directed) else ".sg")
    cmd = [os.path.join(DIR, k), "-f", sg, "-n", str(args.reps)]
    if k == "bfs":
        cmd += ["-r", str(src[0])]
    elif k == "bc":
        cmd += ["-i", str(len(src))]
    row["note"] = "kernel time as printed by the suite; its default parameters (its default PageRank parameters)"
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=dict(os.environ, OMP_NUM_THREADS=str(threads)))
        times = [float(x) for x in re.findall(r"Trial Time:\s+([0-9.eE+-]+)", p.stdout)]
        row["seconds"] = times
        if p.returncode or not times:
            row["status"], row["note"] = "error", (p.stderr or p.stdout)[-200:]
    except OSError as e:
        row["status"], row["note"] = "error", str(e)[:200]
    print(json.dumps(row))


if __name__ == "__main__":
    main()
