#!/usr/bin/env python3
"""Draft the `tools` object of the edge cases of one concept from the recorded evidence.

    python3 scripts/draft_edge_tools.py <concept_id> [case ...]      print JSON {case: {tool_id: entry}}
    python3 scripts/draft_edge_tools.py <concept_id> --unattached    list records that name no mappable input

The draft is built only from data/conventions.json (conditions and notes), data/reasons.json (inputs, findings),
data/capabilities.csv (which tools have an entry), data/fixtures.json (which kinds of input were compared) and
data/tools.json (documented-only tools). It never adds behaviour that these files do not state: a tool with no
statement for a case gets status not_recorded. Read every draft entry, correct it against the reason text and keep
or shorten the wording; the finished entries belong in data/definitions/<family-slug>.json.

Standard library only.
"""
import csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

# structural tags of conventions.json / reasons.json -> edge-case ids of definitions/_vocabulary.json
TAG2CASE = {"multi_edges": "multi_edges", "loops": "self_loops", "disconnected": "disconnected", "not_strongly_connected": "directed_unreachable",
            "edgeless": "edgeless", "null_graph": "empty_graph", "one_node": "single_node", "two_nodes": "two_nodes", "isolates": "isolates",
            "zero_weights": "zero_weights", "negative_weights": "negative_weights", "integer_weights": "ties", "fractional_weights": "ties",
            "symmetric_nodes": "ties", "edge_case": "small_n", "directed": "direction", "undirected": "direction", "weighted": "weights",
            "bipartite": "bipartite", "onemode": "bipartite"}
# fixture names -> edge-case ids
NAMED2CASE = {"empty": ["edgeless"], "single_node": ["single_node"], "pair": ["two_nodes"], "two_triangles_isolate": ["isolates", "disconnected"],
              "complete5_dir": ["complete_graph"], "complete6": ["complete_graph"], "star8": ["star"],
              "cycle7_dir": ["direction"], "gnp_dir_dense": ["direction"], "gnp_dir_sparse": ["direction"], "weighted_dir": ["direction"],
              "real_weights_dir": ["direction"]}
# which fixtures were compared for a case (an "agrees" statement is made only when some exist)
CASE_FIX = {"edgeless": ["empty"], "single_node": ["single_node"], "two_nodes": ["pair"], "small_n": ["pair", "single_node"],
            "isolates": ["empty", "single_node", "two_triangles_isolate", "gnp_und_sparse"], "self_loops": ["multi_loops_und", "multi_loops_dir"],
            "multi_edges": ["multi_loops_und", "multi_loops_dir"], "disconnected": ["two_triangles_isolate", "gnp_und_sparse", "multi_loops_und"],
            "directed_unreachable": ["gnp_dir_sparse", "weighted_dir", "multi_loops_dir"], "direction": ["karate", "gnp_dir_dense"],
            "weights": ["weighted_und", "weighted_dir", "real_weights_und", "real_weights_dir"], "ties": ["karate", "kite", "les_miserables"],
            "complete_graph": ["complete6", "complete5_dir"], "star": ["star8"], "bipartite": ["davis_twomode", "southern_women", "twomode_random"]}
DIM2CASE = {"multi_edges": "multi_edges", "self_loops": "self_loops", "direction": "direction", "weights": "weights"}


def lj(p):
    with open(os.path.join(DATA, p), encoding="utf-8") as f: return json.load(f)


def first_sentences(t, limit=700):
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) <= limit: return t
    cut = t[:limit]
    k = max(cut.rfind(". "), cut.rfind("; "))
    return (cut[:k + 1] if k > 120 else cut.rsplit(" ", 1)[0] + " ...")


CASE_KW = {"multi_edges": r"parallel|multi", "self_loops": r"loop|diagonal", "small_n": r"fewer than|n < 3|three nodes|n <= 2", "single_node": r"single|one node|one-node|n = 1",
           "two_nodes": r"pair|two node|two-node", "isolates": r"isolat|without a tie|no tie|no other node", "direction": r"directed|undirected|direction",
           "ties": r"tie|equal", "weights": r"weight", "edgeless": r"no edges|without edges|edgeless|without ties", "disconnected": r"disconnect|component",
           "directed_unreachable": r"reach|strongly", "negative_weights": r"negative", "zero_weights": r"zero", "bipartite": r"one-mode|two-mode|bipartite|periodic",
           "empty_graph": r"null|empty"}


def pick(note, case, limit=700):
    """The sentences of a note that speak about the case; the start of the note when none does."""
    parts = re.split(r"(?<=[.;]) ", re.sub(r"\s+", " ", note).strip())
    kw = CASE_KW.get(case)
    hit = [x for x in parts if kw and re.search(kw, x, re.I)]
    return first_sentences(" ".join(hit[:2]) if hit else note, limit)


def load():
    d = {"measures": lj("measures.json"), "conventions": lj("conventions.json"), "reasons": lj("reasons.json"), "tools": lj("tools.json")}
    with open(os.path.join(DATA, "capabilities.csv"), newline="", encoding="utf-8") as f: d["caps"] = list(csv.DictReader(f))
    return d


def cases_of(rec, rsn):
    """(differs cases, no_value cases) a convention record names: its own conditions; else the tags of its reason entry;
    and the fixtures its note names literally (the note says which fixture shows the difference)."""
    dif, nov = set(), set()
    for t in rec["differs_when"]:
        if t in TAG2CASE: dif.add(TAG2CASE[t])
    for t in rec["undefined_when"]:
        if t in TAG2CASE: nov.add(TAG2CASE[t])
    r = rsn.get((rec["measure"], rec["tool"]))
    if r:
        inp = r.get("inputs", {})
        for k, tgt in (("differs", dif), ("no_value", nov)):
            if not rec["differs_when"] and not rec["undefined_when"]:
                for t in inp.get(k, {}).get("tags", []):
                    if t in TAG2CASE: tgt.add(TAG2CASE[t])
            for n in inp.get(k, {}).get("named", []):
                if n not in rec["note"]: continue
                for c in NAMED2CASE.get(n, []): tgt.add(c)
                if n.startswith("multi_loops"):
                    note = rec["note"].lower()
                    if "parallel" in note or "multi" in note: tgt.add("multi_edges")
                    if "loop" in note: tgt.add("self_loops")
    return dif, nov


def draft(d, concept, cases=None):
    mids = {m["id"] for m in d["measures"] if m["concept"] == concept}
    role = {t["id"]: t["role"] for t in d["tools"]}
    rsn = {(r["measure"], r["tool"]): r for r in d["reasons"]}
    tools = sorted({c["tool"] for c in d["caps"] if c["measure"] in mids}, key=lambda t: [x["id"] for x in d["tools"]].index(t))
    recs = [c for c in d["conventions"] if c["measure"] in mids]
    out = {}; unattached = []
    ev = {}  # (tool, case) -> {"differs": [...], "no_value": [...], "documented": [...]}
    flat = {}  # tool -> has a record that names no mappable input
    agrees = {}
    for r in recs:
        t = r["tool"]
        if r["outcome"] == "agrees": agrees[t] = True; continue
        dif, nov = cases_of(r, rsn)
        if r["outcome"] == "documented":
            for dm in r["dimensions"]:
                if dm in DIM2CASE: ev.setdefault((t, DIM2CASE[dm]), {}).setdefault("documented", []).append(r)
            continue
        if not dif and not nov and "one-mode fixture" in r["note"]: nov.add("bipartite")
        if not dif and not nov:
            flat.setdefault(t, []).append(r); unattached.append(r); continue
        for c in dif: ev.setdefault((t, c), {}).setdefault("differs", []).append(r)
        for c in nov: ev.setdefault((t, c), {}).setdefault("no_value", []).append(r)
    allcases = set(c for (_, c) in ev) | set(CASE_FIX)
    for case in (cases or sorted(allcases)):
        row = {}
        for t in tools:
            e = ev.get((t, case), {})
            def mk(status, rec, text):
                x = {"status": status, "behaviour": pick(text, case),
                     "source": "conventions.json %s / %s" % (rec["measure"], rec["variant"])}
                if (rec["measure"], t) in rsn:
                    x["measure"] = rec["measure"]
                    fs = rsn[(rec["measure"], t)].get("findings") or []
                    if fs: x["finding"] = fs[0]
                return x
            if e.get("differs"):
                r = e["differs"][0]; row[t] = mk("differs", r, r["note"] or "Differs from the reference value by a documented convention (dimensions: %s)." % ", ".join(r["dimensions"]))
            elif e.get("no_value"):
                r = e["no_value"][0]; row[t] = mk("no_value", r, r["note"] or "Gives no value on this kind of input.")
            elif e.get("documented"):
                r = e["documented"][0]; row[t] = mk("documented", r, r["note"])
            elif role[t] == "documented-only":
                row[t] = {"status": "not_recorded", "behaviour": "Documented-only tool, never run; its documentation does not state this input.", "source": "tools.json"}
            elif t in flat:
                r = flat[t][0]
                x = mk("not_recorded", r, "The tool gives no value or a different value on some compared inputs; the records do not say which kinds of input. " + (r["note"] or ""))
                row[t] = x
            elif agrees.get(t) and CASE_FIX.get(case):
                row[t] = {"status": "agrees", "behaviour": "No difference from the reference value recorded on the compared inputs of this kind (%s)." % ", ".join(CASE_FIX[case]),
                          "source": "capabilities.csv and conventions.json (outcome agrees)"}
            else:
                row[t] = {"status": "not_recorded", "behaviour": "The sources record no comparison of this tool on this kind of input.", "source": "capabilities.csv"}
        out[case] = row
    return out, unattached


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(2)
    d = load()
    if "--unattached" in a:
        _, un = draft(d, a[0], [])
        for r in un: print(r["tool"], r["measure"], r["variant"], r["outcome"], "|", first_sentences(r["note"], 200))
    else:
        o, _ = draft(d, a[0], [x for x in a[1:] if not x.startswith("-")] or None)
        print(json.dumps(o, indent=1, ensure_ascii=False))
