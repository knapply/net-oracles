#!/usr/bin/env python3
"""Shared benchmark runner: every (tool, graph, measure) in a fresh process.

    python3 bench/run.py --suite smoke --tools networkx --out /tmp/results.csv
    python3 bench/run.py --suite ladder-small --adapters-dir ../private/adapters --out rows.csv

For each adapter (bench/adapters/<tool>.py or .R, plus any --adapters-dir) it builds the graphs of the
suite (graphs.yaml), runs `adapter --prepare` once per graph, then one process per measure
(measures.yaml) with a timeout. Wall time and peak resident memory of the child come from wait4's
rusage; the adapter's own measure-only seconds and peak (above its pre-load baseline) are what is
written to the results file, in the schema of data/benchmarks/results.csv. Raw lines (one JSON
object each, with the environment) go to --raw.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import os
import platform
import shutil
import signal
import statistics
import subprocess
import sys
import tempfile
import time

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import graphs as G  # noqa: E402

COLUMNS = ["suite", "graph", "nodes", "edges", "measure", "tool", "tool_version", "seconds", "peak_megabytes", "threads", "status"]


def load_yaml(name):
    with open(os.path.join(HERE, name)) as f:
        return yaml.safe_load(f)


def discover(extra_dirs):
    """{adapter name: path}; a later directory overrides an earlier one."""
    found = {}
    for d in [os.path.join(HERE, "adapters")] + [os.path.abspath(x) for x in extra_dirs]:
        if not os.path.isdir(d):
            sys.exit(f"adapters dir not found: {d}")
        for fn in sorted(os.listdir(d)):
            stem, ext = os.path.splitext(fn)
            if stem.startswith("common") or stem.startswith("_") or ext not in (".py", ".R", ".sh"):
                continue
            found[stem] = os.path.join(d, fn)
    return found


def command(name, path):
    ext = os.path.splitext(path)[1]
    if ext == ".py":
        py = os.environ.get("BENCH_PYTHON_" + name.upper().replace("-", "_"))
        if not py and name == "graphtool":
            py = os.environ.get("GRAPH_TOOL_PY")
        return [py or sys.executable, path]
    if ext == ".R":
        return ["Rscript", path]
    return ["bash", path]


def environment():
    cpu = ""
    try:
        for ln in open("/proc/cpuinfo"):
            if ln.startswith("model name"):
                cpu = ln.split(":", 1)[1].strip()
                break
    except OSError:
        pass
    mem = ""
    try:
        mem = f"{int(open('/proc/meminfo').readline().split()[1]) / 1048576:.1f} GB"
    except (OSError, ValueError):
        pass
    quota = ""
    try:
        q = open("/sys/fs/cgroup/cpu.max").read().split()
        quota = "unlimited" if q[0] == "max" else f"{int(q[0]) / int(q[1]):.2f}"
    except (OSError, ValueError, IndexError):
        pass
    return {"date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "platform": platform.platform(), "python": platform.python_version(), "cpu": cpu,
            "cores_logical": os.cpu_count(), "cores_offered": len(os.sched_getaffinity(0)),
            "cgroup_cpu_quota": quota, "memory": mem, "github_runner": os.environ.get("RUNNER_NAME", ""),
            "runner_image": os.environ.get("ImageOS", "") + " " + os.environ.get("ImageVersion", "")}


def spawn(cmd, timeout, env=None):
    """Run cmd in a fresh process group; returns (stdout, stderr tail, exit code or None on
    timeout, wall seconds, peak resident MB of the child and its descendants)."""
    with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
        t0 = time.perf_counter()
        try:
            p = subprocess.Popen(cmd, stdout=out, stderr=err, start_new_session=True, env=env)
        except OSError as e:  # interpreter not installed
            return "", f"{type(e).__name__}: {e}", 127, 0.0, 0.0
        timed_out = False
        while True:
            pid, status, ru = os.wait4(p.pid, os.WNOHANG)
            if pid:
                break
            if time.perf_counter() - t0 > timeout:
                timed_out = True
                try:
                    os.killpg(p.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                pid, status, ru = os.wait4(p.pid, 0)
                break
            time.sleep(0.02)
        wall = time.perf_counter() - t0
        p.returncode = os.waitstatus_to_exitcode(status)
        out.seek(0)
        err.seek(0)
        return (out.read().decode(errors="replace"), err.read()[-400:].decode(errors="replace"),
                None if timed_out else p.returncode, wall, ru.ru_maxrss / 1024)


def fmt(x):
    return "" if x is None else f"{x:.6g}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--suite", help="suite from graphs.yaml")
    ap.add_argument("--graphs", help="comma-separated graph names (instead of --suite)")
    ap.add_argument("--tools", help="comma-separated adapter names (default: all found)")
    ap.add_argument("--measures", help="comma-separated measure ids (default: all)")
    ap.add_argument("--threads", type=int, default=0, help="threads offered (0 = every CPU offered)")
    ap.add_argument("--reps", type=int, help="repeats (default: per measure in measures.yaml)")
    ap.add_argument("--budget", type=float, help="seconds per run before it is killed (default: the suite's)")
    ap.add_argument("--suite-tag", help="value of the suite column (default: the suite's tag)")
    ap.add_argument("--adapters-dir", action="append", default=[], help="extra adapters directory (repeatable)")
    ap.add_argument("--cache", default=os.environ.get("BENCH_CACHE", os.path.expanduser("~/.cache/net-oracles-bench")))
    ap.add_argument("--out", default=os.path.join(HERE, "out", "results.csv"), help="results CSV (appended)")
    ap.add_argument("--raw", help="raw JSON lines (default: next to --out, .jsonl)")
    ap.add_argument("--env-out", help="write the environment record to this JSON file")
    ap.add_argument("--allow-unpinned", action="store_true", help="accept a download whose sha256 is not pinned yet (prints it)")
    ap.add_argument("--check", action="store_true", help="check adapters against measures.yaml and exit")
    ap.add_argument("--list", action="store_true", help="list adapters, suites and measures and exit")
    a = ap.parse_args()

    meas, gr = load_yaml("measures.yaml"), load_yaml("graphs.yaml")
    adapters = discover(a.adapters_dir)
    if a.list:
        print("adapters:", ", ".join(sorted(adapters)))
        print("suites:", ", ".join(gr["suites"]))
        print("measures:", ", ".join(meas["measures"]))
        return 0
    if a.check:
        return check(adapters, meas)
    if a.tools:
        missing = [t for t in a.tools.split(",") if t not in adapters]
        if missing:
            sys.exit("no adapter for: " + ", ".join(missing))
    tools = a.tools.split(",") if a.tools else sorted(adapters)
    suite = gr["suites"][a.suite] if a.suite else {"tag": "adhoc", "budget": 240, "graphs": (a.graphs or "").split(",")}
    if not a.suite and not a.graphs:
        sys.exit("give --suite or --graphs")
    tag = a.suite_tag or suite["tag"]
    budget = a.budget or suite["budget"]
    ids = a.measures.split(",") if a.measures else list(meas["measures"])
    env = environment()
    if a.env_out:
        os.makedirs(os.path.dirname(os.path.abspath(a.env_out)), exist_ok=True)
        with open(a.env_out, "w") as f:
            json.dump(env, f, indent=1)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    raw_path = a.raw or os.path.splitext(a.out)[0] + ".jsonl"
    new = not os.path.exists(a.out) or os.path.getsize(a.out) == 0
    csv_f = open(a.out, "a", newline="")
    w = csv.writer(csv_f)
    if new:
        w.writerow(COLUMNS)
    raw_f = open(raw_path, "a")
    print(json.dumps({"environment": env}), file=raw_f, flush=True)
    print(f"suite {a.suite or a.graphs} tag {tag}: {len(tools)} tools, {len(suite['graphs'])} graphs, "
          f"{len(ids)} measures, budget {budget:g} s; writing {a.out}", flush=True)
    digests = {}
    counts = {}
    for gname in suite["graphs"]:
        spec = gr["graphs"][gname]
        path = G.materialize(gname, spec, gr["seed"], a.cache, a.allow_unpinned)
        nodes, _ = G.common.read_header(path)
        edges = (os.path.getsize(path) - 24) // 8
        for tool in tools:
            cmd0 = command(tool, adapters[tool])
            prepared = False
            for mid in ids:
                m = meas["measures"][mid]
                lim = meas.get("limits", {})
                if edges > lim.get("max_edges", {}).get(tool, float("inf")):
                    continue
                if mid == "closeness":
                    gate = lim["closeness_max_nodes_times_edges"]
                    if nodes * edges > gate.get(tool, gate["default"]):
                        continue
                if not prepared:
                    prepared = True
                    _, perr, rc, _, _ = spawn(cmd0 + ["--prepare", "--graph", path, "--threads", str(a.threads)], 4 * budget)
                    if rc != 0:
                        print(f"  {tool} {gname}: prepare failed ({perr.strip()[-120:]})", flush=True)
                reps = a.reps or m["reps"]
                out, err, rc, wall, rss = spawn(cmd0 + ["--measure", mid, "--graph", path, "--threads", str(a.threads),
                                                        "--reps", str(reps), "--budget", str(budget)], budget)
                row = None
                for ln in out.splitlines():
                    if ln.startswith("{"):
                        try:
                            row = json.loads(ln)
                        except ValueError:
                            pass
                if rc is None:
                    status, row = "over-budget", (row or {"tool": tool, "tool_version": "", "threads": a.threads})
                elif row is None and any(k in err for k in ("ModuleNotFoundError", "ImportError", "PackageNotFoundError", "there is no package called", "No such file or directory")):
                    status, row = "unsupported", {"tool": tool}  # the tool is not installed: no row
                elif row is None:
                    status, row = "error", {"tool": tool, "tool_version": "", "threads": a.threads, "note": (err or out)[-200:]}
                else:
                    status = {"ok": "ok", "timeout": "over-budget", "unsupported": "unsupported"}.get(row.get("status"), "error")
                secs = row.get("seconds") if isinstance(row.get("seconds"), list) else []
                med = statistics.median(secs) if secs and status == "ok" else None
                peak = row.get("peak_megabytes")
                peak = peak if peak is not None else (round(rss, 1) if status in ("ok", "over-budget") and rc is not None else None)
                counts[status] = counts.get(status, 0) + 1
                raw = row | {"runner": {"suite": tag, "graph": gname, "measure_id": mid, "status": status, "wall_seconds": round(wall, 3),
                                        "process_peak_megabytes": round(rss, 1), "exit": rc, "stderr": err[-200:] if status == "error" else ""}}
                print(json.dumps(raw), file=raw_f, flush=True)
                if status != "unsupported":
                    w.writerow([tag, gname, nodes, edges, m["label"], row.get("tool") or tool, row.get("tool_version", ""),
                                fmt(med), fmt(peak), row.get("threads", a.threads), status])
                    csv_f.flush()
                if status == "ok" and row.get("digest"):
                    digests.setdefault((gname, mid), []).append((row["tool"], row["digest"]))
                print(f"  {gname:9} {mid:12} {tool:12} {status:11} {fmt(med):>10} s  {fmt(peak):>8} MB", flush=True)
    for (gname, mid), items in digests.items():
        for k in {k for _, d in items for k in d}:
            vals = [(t, d[k]) for t, d in items if k in d]
            if len(vals) > 1 and any(not close(vals[0][1], v) for _, v in vals[1:]):
                print(f"DIGEST DIFFERS {gname} {mid} {k}: " + ", ".join(f"{t}={v}" for t, v in vals), file=sys.stderr)
    print("done: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())), flush=True)
    return 0


def close(x, y, rel=1e-4):
    try:
        return abs(x - y) <= rel * max(abs(x), abs(y), 1e-300)
    except TypeError:
        return x == y


def check(adapters, meas):
    """Each adapter's --list must match the measures.yaml calls that name it; ids must exist."""
    bad = 0
    ids = set(meas["measures"])
    for name, path in sorted(adapters.items()):
        out, err, rc, _, _ = spawn(command(name, path) + ["--list"], 120)
        if rc == 127 or "ModuleNotFoundError" in err or "ImportError" in err or "there is no package called" in err:
            print(f"{name}: skipped, tool not installed")
            continue
        try:
            listed = set(json.loads(out.strip().splitlines()[-1]))
        except (ValueError, IndexError):
            print(f"{name}: --list failed ({(err or out).strip()[-100:]})")
            bad += 1
            continue
        documented = {i for i, m in meas["measures"].items() if name.replace("_", "-") in m["calls"] or name in m["calls"]}
        for what, diff in (("not in measures.yaml", listed - ids), ("listed by adapter, no call documented", (listed & ids) - documented - {"load"}),
                           ("documented, not implemented", documented - listed)):
            if diff:
                print(f"{name}: {what}: {sorted(diff)}")
                bad += 1
    print("check:", "ok" if not bad else f"{bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
