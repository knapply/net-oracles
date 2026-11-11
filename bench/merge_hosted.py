#!/usr/bin/env python3
"""Merge the artifacts of a hosted `bench` workflow run into data/benchmarks/hosted.csv and
data/benchmarks/hosted-environments.json.

    python3 bench/merge_hosted.py ARTIFACT_DIR --run-id ID --event schedule

ARTIFACT_DIR holds, per matrix entry, rows-<tool>-<suite>.csv and env-<tool>-<suite>.json (from
run.py --out and --env-out). Rows are keyed by (tool, graph, measure): a new row replaces the old
one with the same key, other rows stay. Rows are written with suite `hosted`.
"""
import argparse
import csv
import glob
import json
import os
import sys

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "benchmarks")
COLUMNS = ["suite", "graph", "nodes", "edges", "measure", "tool", "tool_version", "seconds", "peak_megabytes", "threads", "status"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("artifacts")
    ap.add_argument("--run-id", default="")
    ap.add_argument("--event", default="")
    ap.add_argument("--data", default=DATA)
    a = ap.parse_args()
    csv_path = os.path.join(a.data, "hosted.csv")
    env_path = os.path.join(a.data, "hosted-environments.json")
    rows = {}
    if os.path.exists(csv_path):
        for r in csv.DictReader(open(csv_path, newline="")):
            rows[(r["tool"], r["graph"], r["measure"])] = r
    envs = {}
    if os.path.exists(env_path):
        for e in json.load(open(env_path)):
            envs[(e["tool"], e["suite"])] = e
    n = 0
    for f in sorted(glob.glob(os.path.join(a.artifacts, "**", "rows-*.csv"), recursive=True)):
        suite = os.path.basename(f)[5:-4].split("__", 1)[1] if "__" in os.path.basename(f) else ""
        tools = set()
        versions = {}
        for r in csv.DictReader(open(f, newline="")):
            r["suite"] = "hosted"
            rows[(r["tool"], r["graph"], r["measure"])] = {k: r[k] for k in COLUMNS}
            tools.add(r["tool"])
            versions[r["tool"]] = r["tool_version"] or versions.get(r["tool"], "")
            n += 1
        envf = f.replace("rows-", "env-").replace(".csv", ".json")
        env = json.load(open(envf)) if os.path.exists(envf) else {}
        for t in tools:
            envs[(t, suite)] = {"tool": t, "suite": suite, "date": env.get("date", ""), "run_id": str(a.run_id), "event": a.event,
                                "cpu": env.get("cpu", ""), "cores_offered": int(env.get("cores_offered") or 0),
                                "cores_logical": int(env.get("cores_logical") or 0), "memory": env.get("memory", ""),
                                "platform": env.get("platform", ""), "runner_image": env.get("runner_image", "").strip(),
                                "github_runner": env.get("github_runner", ""), "cgroup_cpu_quota": env.get("cgroup_cpu_quota", ""),
                                "python": env.get("python", ""), "tool_version": versions.get(t, "")}
    if not n:
        sys.exit("no rows found in " + a.artifacts)
    order = sorted(rows.values(), key=lambda r: (r["tool"], r["graph"], r["measure"]))
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(order)
    with open(env_path, "w") as f:
        json.dump([envs[k] for k in sorted(envs)], f, indent=1)
        f.write("\n")
    print(f"merged {n} rows; {len(order)} in total")


if __name__ == "__main__":
    main()
