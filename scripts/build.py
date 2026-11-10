#!/usr/bin/env python3
"""Generate every page of the site from data/ and validate data/ against data/schema/.

    python3 scripts/build.py          write pages
    python3 scripts/build.py --check  fail if validation fails or any generated file is stale

Standard library only.
"""
import csv, json, os, re, sys, statistics, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
HARNESS = os.path.join(ROOT, "harness")  # optional; links are emitted only when it exists


# ---------------------------------------------------------------- validation
class Invalid(Exception):
    pass


def _type_ok(v, t):
    if t == "string": return isinstance(v, str)
    if t == "integer": return isinstance(v, int) and not isinstance(v, bool)
    if t == "number": return isinstance(v, (int, float)) and not isinstance(v, bool)
    if t == "boolean": return isinstance(v, bool)
    if t == "array": return isinstance(v, list)
    if t == "object": return isinstance(v, dict)
    if t == "null": return v is None
    raise Invalid("unknown type " + t)


def validate(v, s, path="$"):
    errs = []
    if "enum" in s and v not in s["enum"]:
        errs.append("%s: %r not in %s" % (path, v, s["enum"]))
        return errs
    if "type" in s:
        ts = s["type"] if isinstance(s["type"], list) else [s["type"]]
        if not any(_type_ok(v, t) for t in ts):
            errs.append("%s: expected %s, got %s" % (path, ts, type(v).__name__))
            return errs
    if isinstance(v, str):
        if "pattern" in s and not re.search(s["pattern"], v): errs.append("%s: %r does not match %s" % (path, v, s["pattern"]))
        if "minLength" in s and len(v) < s["minLength"]: errs.append("%s: shorter than %d" % (path, s["minLength"]))
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if "minimum" in s and v < s["minimum"]: errs.append("%s: below %s" % (path, s["minimum"]))
    if isinstance(v, list) and "items" in s:
        for i, x in enumerate(v): errs += validate(x, s["items"], "%s[%d]" % (path, i))
    if isinstance(v, dict):
        for k in s.get("required", []):
            if k not in v: errs.append("%s: missing %s" % (path, k))
        props = s.get("properties", {})
        for k, x in v.items():
            if k in props: errs += validate(x, props[k], path + "." + k)
            elif s.get("additionalProperties") is False: errs.append("%s: unexpected field %s" % (path, k))
    return errs


def load_json(p):
    with open(os.path.join(DATA, p), encoding="utf-8") as f: return json.load(f)


def load_csv(p):
    with open(os.path.join(DATA, p), newline="", encoding="utf-8") as f: return list(csv.DictReader(f))


def load_all():
    d = {
        "tools": load_json("tools.json"), "measures": load_json("measures.json"),
        "conventions": load_json("conventions.json"), "findings": load_json("findings.json"),
        "capabilities": load_csv("capabilities.csv"), "results": load_csv("benchmarks/results.csv"),
        "bib": parse_bib(open(os.path.join(DATA, "references.bib"), encoding="utf-8").read()),
    }
    return d


def check_data(d):
    errs = []
    sch = lambda n: load_json("schema/" + n)
    for name, f in [("tools", "tools"), ("measures", "measures"), ("conventions", "conventions"), ("findings", "findings")]:
        errs += validate(d[name], sch(f + ".schema.json"), name)
    for name, f in [("capabilities", "capabilities"), ("results", "benchmarks-results")]:
        s = sch(f + ".schema.json")
        for i, r in enumerate(d[name]):
            r2 = dict(r)
            for k, p in s["properties"].items():
                if p.get("type") == "integer":
                    try: r2[k] = int(r[k])
                    except ValueError: pass
            errs += validate(r2, s, "%s[%d]" % (name, i))
    tools = {t["id"] for t in d["tools"]}; meas = {m["id"] for m in d["measures"]}; bib = set(d["bib"])
    if len(tools) != len(d["tools"]): errs.append("duplicate tool ids")
    if len(meas) != len(d["measures"]): errs.append("duplicate measure ids")
    slugs = [slug(m["id"]) for m in d["measures"]]
    if len(set(slugs)) != len(slugs): errs.append("measure slugs collide")
    seen = set()
    for r in d["capabilities"]:
        if r["measure"] not in meas: errs.append("capabilities: unknown measure " + r["measure"])
        if r["tool"] not in tools: errs.append("capabilities: unknown tool " + r["tool"])
        if (r["measure"], r["tool"]) in seen: errs.append("capabilities: duplicate %s/%s" % (r["measure"], r["tool"]))
        seen.add((r["measure"], r["tool"]))
    role = {t["id"]: t["role"] for t in d["tools"]}
    for r in d["capabilities"]:
        if role.get(r["tool"]) == "documented-only" and r["state"] != "reported-in-docs":
            errs.append("documented-only tool with checked state: %s/%s" % (r["measure"], r["tool"]))
    for m in d["measures"]:
        for k in m["references"]:
            if k not in bib: errs.append("measure %s: missing bib key %s" % (m["id"], k))
    for t in d["tools"]:
        if t["citation_key"] and t["citation_key"] not in bib: errs.append("tool %s: missing bib key" % t["id"])
    for c in d["conventions"]:
        if c["measure"] not in meas: errs.append("conventions: unknown measure " + c["measure"])
        if c["tool"] not in tools: errs.append("conventions: unknown tool " + c["tool"])
        if "reference" in c and c["reference"] not in bib: errs.append("conventions: missing bib key " + c["reference"])
    for f in d["findings"]:
        if f["tool"] not in tools: errs.append("findings: unknown tool " + f["tool"])
        if f["measure"] is not None and f["measure"] not in meas: errs.append("findings: unknown measure " + f["measure"])
        for k in f["references"]:
            if k not in bib: errs.append("findings: missing bib key " + k)
    for r in d["results"]:
        if r["tool"] not in tools: errs.append("benchmarks: unknown tool " + r["tool"])
    return errs


# ---------------------------------------------------------------- bibtex
def parse_bib(text):
    out = {}
    for m in re.finditer(r"^@(\w+)\{([^,]+),(.*?)\n\}\s*$", text, re.M | re.S):
        fields = {}
        for fm in re.finditer(r"^\s*(\w+)\s*=\s*(\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}|\"[^\"]*\"|[0-9]+)\s*,?\s*$", m.group(3), re.M):
            v = fm.group(2)
            if v[0] in "{\"" : v = v[1:-1]
            fields[fm.group(1).lower()] = v
        out[m.group(2)] = {"type": m.group(1).lower(), **fields}
    return out


def tex(s):
    s = re.sub(r"\\url\{([^}]*)\}", r"\1", s)
    for a, b in [("{\\\"o}", "ö"), ("{\\\"a}", "ä"), ("{\\\"u}", "ü"), ("{\\'e}", "é"), ("{\\'a}", "á"), ("{\\'\\i}", "í"), ("{\\'o}", "ó"), ("{\\v z}", "ž"), ("{\\v Z}", "Ž"),
                 ("{\\v{s}}", "š"), ("{\\v{S}}", "Š"), ("{\\c{c}}", "ç"), ("{\\'c}", "ć"), ("\\&", "&"), ("---", "—"), ("--", "–"), ("{\\l}", "ł"), ("{\\'u}", "ú"), ("{\\\"O}", "Ö"), ("{\\ss}", "ß")]:
        s = s.replace(a, b)
    s = re.sub(r"\\[`'^\"~=.]\{?(\w)\}?", r"\1", s)
    return s.replace("{", "").replace("}", "").replace("\\", "").strip()


def cite_text(e):
    au = e.get("author", e.get("editor", ""))
    names = [tex(a).strip() for a in re.split(r"\s+and\s+", au)] if au else []
    def short(n):
        if "," in n:
            last, first = n.split(",", 1)
            return last.strip() + ", " + "".join(w[0] + "." for w in re.split(r"[\s-]+", first.strip()) if w)
        return n
    a = "; ".join(short(n) for n in names[:6]) + (" et al." if len(names) > 6 else "")
    parts = [a, "(%s)" % e.get("year", "n.d."), tex(e.get("title", ""))]
    venue = e.get("journal") or e.get("booktitle") or ""
    s = " ".join(p for p in parts if p) + "."
    if venue:
        s += " *%s*" % tex(venue)
        if e.get("volume"): s += ", %s" % tex(e["volume"])
        if e.get("number"): s += "(%s)" % tex(e["number"])
        if e.get("pages"): s += ", %s" % tex(e["pages"])
        s += "."
    if e.get("doi"): s += " doi:%s" % e["doi"]
    elif e.get("howpublished") or e.get("url"): s += " %s" % tex(e.get("howpublished") or e.get("url"))
    return s


# ---------------------------------------------------------------- helpers
def slug(i): return re.sub(r"[^A-Za-z0-9_.-]", "-", i)


def esc(s):
    s = re.sub(r"\s+", " ", str(s)).strip()
    if s.count("`") % 2: s = s.replace("`", "")
    parts = s.split("`")
    for i in range(0, len(parts), 2):
        parts[i] = (parts[i].replace("\\", "\\\\").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
                    .replace("*", "\\*").replace("[", "\\[").replace("]", "\\]").replace("_", "\\_"))
    for i in range(1, len(parts), 2): parts[i] = parts[i].replace("|", "\\|")
    return "`".join(parts)


def code(s):
    s = re.sub(r"\s+", " ", str(s)).strip().replace("`", "'").replace("|", "\\|")
    return "`%s`" % s if s else ""


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    for r in rows: out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def page(front, body):
    fm = "---\n" + "\n".join("%s: %s" % (k, v) for k, v in front.items()) + "\n---\n\n"
    return fm + "{% raw %}\n" + body.strip() + "\n{% endraw %}\n"


def yq(s): return json.dumps(s, ensure_ascii=False)


STATE_SYM = {"checked-agrees": "✓", "checked-convention": "≠", "checked-defect": "✗", "checked-no-value": "∅", "reported-in-docs": "·"}
STATE_TXT = {"checked-agrees": "checked, agrees", "checked-convention": "checked, differs by convention", "checked-defect": "checked, defect",
             "checked-no-value": "checked, no value on some inputs", "reported-in-docs": "reported in docs"}
LEGEND = "✓ checked, agrees; ≠ checked, differs by a documented convention; ✗ checked, defect found; ∅ checked, no value on the compared inputs; · reported in the tool's documentation (not run); blank: not known to implement it."


def harness_links(conv_rows, tool_ids):
    """Links into harness/ (added by a later export); empty while the directory is absent."""
    if not os.path.isdir(HARNESS): return []
    out = []
    for f in sorted({c["manifest"] for c in conv_rows if c.get("manifest")}):
        out.append("[harness/%s](../harness/%s)" % (f, f))
    for t in sorted(tool_ids): out.append("[harness/golden/%s/](../harness/golden/%s/)" % (t, t))
    return out


# ---------------------------------------------------------------- pages
def build(d):
    files = {}
    tools = d["tools"]; tid = {t["id"]: t for t in tools}
    meas = sorted(d["measures"], key=lambda m: (m["family"], m["name"].lower(), m["id"])); mid = {m["id"]: m for m in meas}
    caps_by_m = collections.defaultdict(list); caps_by_t = collections.defaultdict(list)
    for r in d["capabilities"]: caps_by_m[r["measure"]].append(r); caps_by_t[r["tool"]].append(r)
    conv_by_m = collections.defaultdict(list)
    for c in d["conventions"]: conv_by_m[c["measure"]].append(c)
    fnd_by_m = collections.defaultdict(list); fnd_by_t = collections.defaultdict(list)
    for f in d["findings"]:
        fnd_by_t[f["tool"]].append(f)
        if f["measure"]: fnd_by_m[f["measure"]].append(f)
    families = sorted({m["family"] for m in meas})
    tool_order = [t["id"] for t in tools]
    n_checked = sum(1 for r in d["capabilities"] if r["state"].startswith("checked"))
    cite = lambda k, rel: "[%s](%sreferences.html#%s)" % (k, rel, k)

    # index
    ncheck_t = sum(1 for t in tools if t["role"] == "checked")
    body = f"""# net-oracles

A neutral, citable survey of network-analysis software: which tool implements which measure, how their conventions differ, which bugs and disagreements were found, and how the tools were benchmarked. Every claim carries a citation key; every table on these pages is generated from the machine-readable files in [`data/`](https://github.com/knapply/net-oracles/tree/main/data).

**{len(tools) - 1} tools** ({ncheck_t} run and compared), **{len(meas)} measures** in {len(families)} families, **{len(d['capabilities'])} tool-by-measure entries** ({n_checked} checked by running the tool), **{len(d['findings'])} findings** about other tools' behaviour, and {len(d['results'])} benchmark rows.

## Where to go

{table(['Page', 'What it holds'], [
 ['[Capability matrix](matrix.html)', 'Measure by tool, one section per family, with the state of each entry.'],
 ['[Measures](measures/)', 'One page per measure: who implements it, convention differences, tolerances, findings, citations.'],
 ['[Tools](tools/)', 'One page per tool: version tested, license, how it was run, coverage, findings.'],
 ['[Findings](findings.html)', 'Bugs, disagreements and limitations found in other tools, with reproductions where recorded.'],
 ['[Benchmarks](benchmarks.html)', 'Method and timing summaries for the other tools; raw rows are in `data/benchmarks/`.'],
 ['[References](references.html)', 'Every cited package and paper.'],
 ['[Data and schemas](data.html)', 'File formats, joins and the state vocabulary.']])}

## How entries are labelled

Each tool-by-measure entry has one state:

{table(['State', 'Meaning'], [[code(k), STATE_TXT[k] + ' (' + STATE_SYM[k] + ')'] for k in STATE_SYM])}

The definitions are in `data/schema/capabilities.schema.json`. A tool marked *documented-only* was never run: its entries come from its documentation and are always `reported-in-docs`.

A *reference value* in these pages means the value of the published definition, evaluated independently (brute force on small graphs, in exact arithmetic where the quantity allows), and confirmed against other tools before a difference is attributed to a convention.
"""
    files["index.md"] = page({"title": "Home", "layout": "default", "nav_order": 1, "permalink": "/"}, body)

    # data page
    schema_rows = [[code("data/" + n), s] for n, s in [
        ("tools.json", "Tools: id, name, language, version tested, license, homepage, citation key, role, how it was run."),
        ("measures.json", "Measures: id, name, family, definition, citation keys."),
        ("capabilities.csv", "Measure by tool: state, API names, comparison counts. Join keys: `measure`, `tool`."),
        ("conventions.json", "Per measure, variant and tool: scope, call, outcome, differing conditions, normalization/direction/weights/self-loops/ties/defaults dimensions, note, tolerance."),
        ("findings.json", "Bugs, disagreements and limitations in other tools."),
        ("benchmarks/results.csv", "Timing and memory of other tools; method in `data/benchmarks/method.md`."),
        ("references.bib", "BibTeX for every cited key.")]]
    body = "# Data and schemas\n\n" + table(["File", "Content"], schema_rows) + """

Each JSON or CSV file has a JSON Schema in `data/schema/` (draft 2020-12). `python3 scripts/build.py --check` validates all of them with a stdlib-only validator and checks the joins below.

## Joins

- `capabilities.csv.measure` is `measures.json[].id`; `capabilities.csv.tool` is `tools.json[].id`.
- `conventions.json[].measure`, `.tool` use the same ids. `.variant` names one parameterization of the measure (for example normalized or weighted).
- `findings.json[].tool`, `.measure` (nullable) use the same ids.
- `benchmarks/results.csv.tool` is `tools.json[].id`.
- Citation keys in `tools.json[].citation_key`, `measures.json[].references`, `findings.json[].references` and `conventions.json[].reference` are keys of `references.bib`.

## Conventions record fields

`outcome` is `agrees` (values agreed on every compared input), `differs` (they differ under `differs_when`), `no-value-on-some-inputs` (the tool returns no value or an error under `undefined_when`), or `documented` (taken from documentation). `dimensions` lists which conventions are involved. `tolerance` is the absolute and relative tolerance used when comparing: integer outputs are compared exactly, floating-point outputs within the stated bound. The structural conditions are: `loops`, `multi_edges`, `directed`, `undirected`, `disconnected`, `not_strongly_connected`, `null_graph`, `one_node`, `two_nodes`, `edgeless`, `isolates`, `symmetric_nodes`, `negative_weights`, `zero_weights`, `integer_weights`, `fractional_weights`, `weighted`, `bipartite`, `onemode`, `unsorted_edges`, `no_two_paths`, `edge_case`.
"""
    files["data.md"] = page({"title": "Data and schemas", "layout": "default", "nav_order": 7}, body)

    # tools index + pages
    rows = []
    for t in tools:
        if t["role"] == "reference": continue
        cs = caps_by_t.get(t["id"], [])
        rows.append(["[%s](%s.html)" % (esc(t["name"]), t["id"]), esc(t["language"] or ""), esc(t["version_tested"]), esc(t["license"] or ""), t["role"], len(cs), sum(1 for c in cs if c["state"].startswith("checked")), len(fnd_by_t.get(t["id"], []))])
    body = "# Tools\n\n" + table(["Tool", "Language", "Version tested", "License", "Role", "Measures", "Checked", "Findings"], rows)
    files["tools/index.md"] = page({"title": "Tools", "layout": "default", "nav_order": 3, "has_children": "true", "permalink": "/tools/"}, body)
    for t in tools:
        if t["role"] == "reference": continue
        cs = sorted(caps_by_t.get(t["id"], []), key=lambda r: (mid[r["measure"]]["family"], mid[r["measure"]]["name"].lower()))
        cnt = collections.Counter(c["state"] for c in cs)
        info = [["Identifier", code(t["id"])], ["Language", esc(t["language"] or "")], ["Version tested", esc(t["version_tested"] or "not recorded")],
                ["License", esc(t["license"] or "not recorded")], ["Homepage", ("<%s>" % t["homepage"]) if t["homepage"] else "none recorded"],
                ["Role", t["role"]], ["Citation", cite(t["citation_key"], "../") if t["citation_key"] else ""]]
        body = "# %s\n\n" % esc(t["name"]) + table(["Field", "Value"], info) + "\n\n## How it was run\n\n" + esc(t["how_run"]) + "\n"
        if t["api_listing"] and t["api_listing"]["method"]:
            body += "\nCapabilities listed by %s of %s.\n" % (esc(t["api_listing"]["method"]), esc(t["api_listing"]["source"] or "its documentation"))
        if cs:
            body += "\n## Coverage\n\n" + table(["State", "Measures"], [[STATE_TXT[k] + " (" + STATE_SYM[k] + ")", cnt[k]] for k in STATE_SYM if cnt[k]]) + "\n"
            body += "\n## Measures\n\n" + table(["Family", "Measure", "State", "API names"], [
                [esc(mid[c["measure"]]["family"]), "[%s](../measures/%s.html)" % (esc(mid[c["measure"]]["name"]), slug(c["measure"])), STATE_SYM[c["state"]] + " " + STATE_TXT[c["state"]], code(c["api_names"]) if c["api_names"] else ""] for c in cs]) + "\n"
        fs = fnd_by_t.get(t["id"], [])
        if fs:
            body += "\n## Findings\n\n" + table(["Id", "Kind", "Title"], [["[%s](../findings.html#%s)" % (f["id"], f["id"].lower()), f["kind"], esc(f["title"])] for f in fs]) + "\n"
        files["tools/%s.md" % t["id"]] = page({"title": yq(t["name"]), "layout": "default", "parent": "Tools"}, body)

    # measures index + pages
    body = "# Measures\n\nOne page per measure, grouped by family. The [capability matrix](../matrix.html) shows the same measures against all tools.\n"
    for fam in families:
        body += "\n## %s\n\n" % esc(fam)
        body += " · ".join("[%s](%s.html)" % (esc(m["name"]), slug(m["id"])) for m in meas if m["family"] == fam) + "\n"
    files["measures/index.md"] = page({"title": "Measures", "layout": "default", "nav_order": 4, "has_children": "true", "permalink": "/measures/"}, body)
    for m in meas:
        cs = sorted(caps_by_m[m["id"]], key=lambda r: tool_order.index(r["tool"]))
        body = "# %s\n\nFamily: %s. Identifier: %s.\n\n## Definition\n\n%s\n" % (esc(m["name"]), esc(m["family"]), code(m["id"]), esc(m["definition"]))
        body += "\n## Implementations\n\n" + table(["Tool", "State", "API names", "Source"], [
            ["[%s](../tools/%s.html)" % (esc(tid[c["tool"]]["name"]), c["tool"]), STATE_SYM[c["state"]] + " " + STATE_TXT[c["state"]], code(c["api_names"]) if c["api_names"] else "", esc(c["source"])] for c in cs]) + "\n"
        cv = [c for c in conv_by_m.get(m["id"], []) if c["tool"] in tid]
        if cv:
            body += "\n## Conventions and tolerances\n\nTolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).\n\n"
            cv = sorted(cv, key=lambda c: (c["variant"], tool_order.index(c["tool"])))
            body += table(["Variant", "Tool", "Scope", "Outcome", "Differs when", "Conventions", "Tolerance", "Call", "Note"], [[
                code(c["variant"]), esc(tid[c["tool"]]["name"]), c["scope"], c["outcome"], esc(", ".join(c["differs_when"] + ["(no value) " + u for u in c["undefined_when"]])),
                esc(", ".join(c["dimensions"])), "abs %g, rel %g" % (c["tolerance"]["abs"], c["tolerance"]["rel"]), code(c["call"]) if c["call"] else "", esc(c["note"])] for c in cv]) + "\n"
            hl = harness_links(cv, {c["tool"] for c in cv})
            if hl: body += "\n## Harness files\n\n" + "; ".join(hl) + "\n"
        fs = fnd_by_m.get(m["id"], [])
        if fs:
            body += "\n## Findings\n\n" + table(["Id", "Tool", "Kind", "Title"], [["[%s](../findings.html#%s)" % (f["id"], f["id"].lower()), esc(tid[f["tool"]]["name"]), f["kind"], esc(f["title"])] for f in fs]) + "\n"
        if m["references"]:
            body += "\n## References\n\n" + ", ".join(cite(k, "../") for k in m["references"]) + "\n"
        tk = sorted({tid[c["tool"]]["citation_key"] for c in cs if tid[c["tool"]]["citation_key"]})
        if tk: body += "\nTools cited: " + ", ".join(cite(k, "../") for k in tk) + "\n"
        files["measures/%s.md" % slug(m["id"])] = page({"title": yq(m["name"]), "layout": "default", "parent": "Measures", "nav_exclude": "true"}, body)

    # matrix
    body = "# Capability matrix\n\n" + LEGEND + "\n\nColumns are tool identifiers (see [Tools](tools/)). Rows link to the measure pages.\n"
    cap = {(r["measure"], r["tool"]): r["state"] for r in d["capabilities"]}
    for fam in families:
        ms = [m for m in meas if m["family"] == fam]
        ts = [t for t in tool_order if any((m["id"], t) in cap for m in ms)]
        body += "\n## %s\n\n%d measures.\n\n" % (esc(fam), len(ms))
        body += table(["Measure"] + [t for t in ts], [["[%s](measures/%s.html)" % (esc(m["name"]), slug(m["id"]))] + [STATE_SYM.get(cap.get((m["id"], t), ""), "") for t in ts] for m in ms]) + "\n"
    files["matrix.md"] = page({"title": "Capability matrix", "layout": "default", "nav_order": 2}, body)

    # findings
    body = "# Findings\n\nBugs, disagreements and limitations observed in other tools. `kind` is *defect* (wrong under the published definition), *convention* (differs by a convention) or *limitation* (refuses or cannot represent the input). `status` is *reproduced* (minimal reproduction recorded), *observed* (seen on a shared corpus of test graphs) or *reported* (public discussion, not re-measured). Versions are those tested; a finding may not hold in later versions.\n\n"
    body += table(["Id", "Tool", "Version", "Measure", "Kind", "Status", "Title"], [[
        "[%s](#%s)" % (f["id"], f["id"].lower()), esc(tid[f["tool"]]["name"]), esc(f["version"]), ("[%s](measures/%s.html)" % (esc(mid[f["measure"]]["name"]), slug(f["measure"]))) if f["measure"] else "", f["kind"], f["status"], esc(f["title"])] for f in d["findings"]]) + "\n"
    for f in d["findings"]:
        body += "\n## %s %s {#%s}\n\nTool: [%s](tools/%s.html) %s. Kind: %s. Status: %s.\n" % (f["id"], esc(f["title"]), f["id"].lower(), esc(tid[f["tool"]]["name"]), f["tool"], esc(f["version"]), f["kind"], f["status"])
        if f["observed"]: body += "\n**Observed:** %s\n" % esc(f["observed"])
        if f["expected"]: body += "\n**Expected:** %s\n" % esc(f["expected"])
        if f["reproduction"]:
            body += "\n**Reproduction:**\n\n```\n%s\n```\n" % f["reproduction"].replace("```", "'''")
        if f["evidence"]: body += "\n**Notes:** %s\n" % esc(f["evidence"])
        if f["references"]: body += "\nReferences: " + ", ".join(cite(k, "") for k in f["references"]) + "\n"
    files["findings.md"] = page({"title": "Findings", "layout": "default", "nav_order": 5}, body)

    # benchmarks
    method = open(os.path.join(DATA, "benchmarks", "method.md"), encoding="utf-8").read().strip()
    method = re.sub(r"^# .*\n", "", method)
    body = "# Benchmarks\n\nTimings and memory of other tools only. Raw rows: `data/benchmarks/results.csv`. Method:\n\n" + method.replace("\n#", "\n##") + "\n"
    R = d["results"]
    grp = collections.defaultdict(list)
    for r in R: grp[(r["suite"], r["tool"], r["measure"])].append(r)
    suites = sorted({r["suite"] for r in R})
    body += "\n## Summary by suite\n\n" + table(["Suite", "Tool", "Rows", "Graphs", "Measures", "Over budget"], [[
        s, esc(tid[t]["name"]), len(rs), len({r["graph"] for r in rs}), len({r["measure"] for r in rs}), sum(1 for r in rs if r["status"] == "over-budget")]
        for s in suites for t in sorted({r["tool"] for r in R if r["suite"] == s}) for rs in [[r for r in R if r["suite"] == s and r["tool"] == t]]]) + "\n"
    for s in suites:
        body += "\n## Median time per measure: %s\n\nMedian over the graphs on which the tool finished within the budget; threads as in the data file.\n\n" % s
        rows = []
        for (ss, t, me), rs in sorted(grp.items(), key=lambda kv: (kv[0][2].lower(), kv[0][1])):
            if ss != s: continue
            sec = [float(r["seconds"]) for r in rs if r["seconds"]]
            mb = [float(r["peak_megabytes"]) for r in rs if r["peak_megabytes"]]
            rows.append([esc(me), esc(tid[t]["name"]), len(rs), len(sec), "%.4g" % statistics.median(sec) if sec else "", "%.4g" % statistics.median(mb) if mb else ""])
        body += table(["Measure", "Tool", "Graphs", "Finished", "Median seconds", "Median peak MB"], rows) + "\n"
    files["benchmarks.md"] = page({"title": "Benchmarks", "layout": "default", "nav_order": 6}, body)

    # references
    cited = collections.defaultdict(list)
    for t in tools:
        if t["citation_key"]: cited[t["citation_key"]].append("tool " + t["id"])
    for m in d["measures"]:
        for k in m["references"]: cited[k].append("measure " + m["id"])
    body = "# References\n\nEvery cited package and paper. Keys match `data/references.bib`.\n\n"
    for k in sorted(d["bib"]):
        body += '- <a id="%s"></a>`%s` %s\n' % (k, k, esc(cite_text(d["bib"][k])))
    files["references.md"] = page({"title": "References", "layout": "default", "nav_order": 8}, body)

    # llms.txt
    files["llms.txt"] = llms(d, families)
    return files


def llms(d, families):
    n_checked = sum(1 for r in d["capabilities"] if r["state"].startswith("checked"))
    return f"""# net-oracles

A neutral survey of network-analysis software. It records which tool implements which measure, how conventions differ between tools (normalization, direction, weights, self-loops, ties, defaults, tolerances), bugs and disagreements found in other tools, how tools were benchmarked, and citations. It describes other tools only.

Counts: {len(d['tools'])} tool records, {len(d['measures'])} measures in {len(families)} families, {len(d['capabilities'])} measure-by-tool entries ({n_checked} checked by running the tool), {len(d['conventions'])} convention records, {len(d['findings'])} findings, {len(d['results'])} benchmark rows.

Source of truth is data/. Pages are generated from it by scripts/build.py (python3, standard library only). Raw base: https://raw.githubusercontent.com/knapply/net-oracles/main/ ; site: https://knapply.github.io/net-oracles/

## Data files and schemas

- data/tools.json (schema data/schema/tools.schema.json): array of tools. Fields: id, name, language, version_tested, license, homepage, citation_key, role (checked | documented-only | benchmarked-only | reference), how_run, api_listing.
- data/measures.json (data/schema/measures.schema.json): array of measures. Fields: id, name, family, definition, references (BibTeX keys).
- data/capabilities.csv (data/schema/capabilities.schema.json): one row per measure and tool. Columns: measure, tool, state, api_names (semicolon separated), comparisons_agreeing, comparisons_differing, source.
  State vocabulary: reported-in-docs (listed in the tool's documentation or public API, not run); checked-agrees (run, agrees with an independent evaluation within tolerance); checked-convention (run, differs on some inputs by a documented convention); checked-defect (run, wrong under the published definition); checked-no-value (run, returns no value or an error on the compared inputs). Tools with role documented-only only have reported-in-docs. A blank (absent row) means not known to implement it.
- data/conventions.json (data/schema/conventions.schema.json): array of records per measure, variant and tool. Fields: measure, variant, manifest, tool, scope (any | directed | undirected), weights_required, call (how the tool was invoked), outcome (agrees | differs | no-value-on-some-inputs | documented), differs_when and undefined_when (structural conditions such as loops, multi_edges, directed, disconnected, ties), only_on, dimensions (normalization, direction, weights, self_loops, multi_edges, ties, defaults), note, tolerance {{abs, rel}} (0 means exact), optional differs_on_inputs, no_value_on_inputs, reference.
- data/findings.json (data/schema/findings.schema.json): array of findings. Fields: id, tool, version, measure (nullable), kind (defect | convention | limitation), status (reproduced | observed | reported), title, reproduction, observed, expected, evidence, references.
- data/benchmarks/results.csv (data/schema/benchmarks-results.schema.json): timing rows of other tools. Columns: suite, graph, nodes, edges, measure, tool, tool_version, seconds (empty when over budget), peak_megabytes, threads, status. Method: data/benchmarks/method.md.
- data/references.bib: BibTeX for every key used above.

## Joins

capabilities.measure -> measures.id; capabilities.tool -> tools.id; conventions.measure/tool -> measures.id/tools.id; findings.tool -> tools.id; findings.measure -> measures.id (nullable); benchmarks.tool -> tools.id; every citation key -> references.bib. Page for a measure: measures/<id>.html (characters other than letters, digits, underscore, dot and hyphen in the id become hyphens). Page for a tool: tools/<id>.html.

## Conventions of the data

Edge ends are called source and target. A reference value is the published definition evaluated independently. UCINET is documented-only: it was never run. Tool versions are those tested; findings may not hold in later versions.

## Regenerate and validate

python3 scripts/build.py          # write pages
python3 scripts/build.py --check  # validate data against schemas and fail if pages are stale
"""


# ---------------------------------------------------------------- main
GENERATED_DIRS = ["tools", "measures"]
GENERATED_TOP = ["index.md", "data.md", "matrix.md", "findings.md", "benchmarks.md", "references.md", "llms.txt"]


def existing_generated():
    out = set(p for p in GENERATED_TOP if os.path.exists(os.path.join(ROOT, p)))
    for dname in GENERATED_DIRS:
        base = os.path.join(ROOT, dname)
        if os.path.isdir(base):
            for fn in os.listdir(base): out.add(dname + "/" + fn)
    return out


def main(argv):
    check = "--check" in argv
    d = load_all()
    errs = check_data(d)
    if errs:
        print("data validation failed:")
        for e in errs[:50]: print("  " + e)
        if len(errs) > 50: print("  ... %d more" % (len(errs) - 50))
        return 1
    files = build(d)
    if check:
        stale = []
        for p, content in files.items():
            fp = os.path.join(ROOT, p)
            if not os.path.exists(fp) or open(fp, encoding="utf-8").read() != content: stale.append(p)
        extra = sorted(existing_generated() - set(files))
        if stale or extra:
            print("stale generated files: %d, unexpected files: %d" % (len(stale), len(extra)))
            for p in stale[:20]: print("  stale: " + p)
            for p in extra[:20]: print("  unexpected: " + p)
            print("run: python3 scripts/build.py")
            return 1
        print("ok: data valid, %d generated files current" % len(files))
        return 0
    for p in sorted(existing_generated() - set(files)): os.remove(os.path.join(ROOT, p))
    for p, content in files.items():
        fp = os.path.join(ROOT, p)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "w", encoding="utf-8") as f: f.write(content)
    print("wrote %d files" % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
