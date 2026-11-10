#!/usr/bin/env python3
"""Generate every page of the site from data/ and validate data/ against data/schema/.

    python3 scripts/build.py          write pages
    python3 scripts/build.py --check  fail if validation fails or any generated file is stale

Standard library only.
"""
import csv, io, json, os, re, sys, statistics, collections

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
        "tools": load_json("tools.json"), "measures": load_json("measures.json"), "concepts": load_json("concepts.json"),
        "conventions": load_json("conventions.json"), "findings": load_json("findings.json"),
        "capabilities": load_csv("capabilities.csv"), "results": load_csv("benchmarks/results.csv"),
        "bib": parse_bib(open(os.path.join(DATA, "references.bib"), encoding="utf-8").read()),
    }
    return d


def check_data(d):
    errs = []
    sch = lambda n: load_json("schema/" + n)
    for name, f in [("tools", "tools"), ("measures", "measures"), ("concepts", "concepts"), ("conventions", "conventions"), ("findings", "findings")]:
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
    if len(set(slugs)) != len(slugs): errs.append("measure anchors collide")
    cids = [c["id"] for c in d["concepts"]]
    if len(set(cids)) != len(cids): errs.append("duplicate concept ids")
    cset = set(cids)
    members = collections.Counter()
    labels = collections.Counter()
    for m in d["measures"]:
        if m["concept"] not in cset: errs.append("measure %s: unknown concept %s" % (m["id"], m["concept"]))
        members[m["concept"]] += 1
        labels[(m["concept"], m["variant"])] += 1
    for c in d["concepts"]:
        if not members[c["id"]]: errs.append("concept %s has no measures" % c["id"])
        for k in c["references"]:
            if k not in d["bib"]: errs.append("concept %s: missing bib key %s" % (c["id"], k))
    for (c, v), n in labels.items():
        if n > 1: errs.append("concept %s: variant label %r used %d times" % (c, v, n))
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


def harness_links(conv_rows, tool_ids, rel="../"):
    """Links into harness/ (added by a later export); empty while the directory is absent."""
    if not os.path.isdir(HARNESS): return []
    out = []
    for f in sorted({c["manifest"] for c in conv_rows if c.get("manifest")}):
        out.append("[harness/%s](%sharness/%s)" % (f, rel, f))
    for t in sorted(tool_ids): out.append("[harness/golden/%s/](%sharness/golden/%s/)" % (t, rel, t))
    return out


# ---------------------------------------------------------------- pages
def build(d):
    files = {}
    tools = d["tools"]; tid = {t["id"]: t for t in tools}
    concepts = sorted(d["concepts"], key=lambda c: (c["family"], c["subfamily"].lower(), c["name"].lower(), c["id"])); cid_ = {c["id"]: c for c in concepts}
    mem = collections.defaultdict(list)
    for m in d["measures"]: mem[m["concept"]].append(m)
    for k in mem: mem[k].sort(key=lambda m: (m["id"] != k, m["variant"].lower(), m["id"]))
    meas = [m for c in concepts for m in mem[c["id"]]]; mid = {m["id"]: m for m in meas}
    fam_slug = lambda f: re.sub(r"[^a-z0-9]+", "-", f.lower()).strip("-")
    def curl(c, rel): return "%smeasures/%s/%s.html" % (rel, fam_slug(c["family"]), c["id"])
    def mlink(mid_, rel, text=None):
        m = mid[mid_]; c = cid_[m["concept"]]
        return "[%s](%s#%s)" % (text if text is not None else esc(m["name"]), curl(c, rel), slug(mid_))
    def mpath(mid_):
        m = mid[mid_]; c = cid_[m["concept"]]
        return ("measures/%s/%s.html" % (fam_slug(c["family"]), c["id"]), slug(mid_))
    mkey = lambda mid_: (cid_[mid[mid_]["concept"]]["family"], cid_[mid[mid_]["concept"]]["subfamily"].lower(), cid_[mid[mid_]["concept"]]["name"].lower(), mid[mid_]["concept"], mid[mid_]["variant"].lower())
    caps_by_m = collections.defaultdict(list); caps_by_t = collections.defaultdict(list)
    for r in d["capabilities"]: caps_by_m[r["measure"]].append(r); caps_by_t[r["tool"]].append(r)
    conv_by_m = collections.defaultdict(list)
    for c in d["conventions"]: conv_by_m[c["measure"]].append(c)
    fnd_by_m = collections.defaultdict(list); fnd_by_t = collections.defaultdict(list)
    for f in d["findings"]:
        fnd_by_t[f["tool"]].append(f)
        if f["measure"]: fnd_by_m[f["measure"]].append(f)
    families = sorted({c["family"] for c in concepts})
    tool_order = [t["id"] for t in tools]
    n_checked = sum(1 for r in d["capabilities"] if r["state"].startswith("checked"))
    cite = lambda k, rel: "[%s](%sreferences.html#%s)" % (k, rel, k)

    # index
    ncheck_t = sum(1 for t in tools if t["role"] == "checked")
    body = f"""# net-oracles

A neutral, citable survey of network-analysis software: which tool implements which measure, how their conventions differ, which bugs and disagreements were found, and how the tools were benchmarked. Every claim carries a citation key; every table on these pages is generated from the machine-readable files in [`data/`](https://github.com/knapply/net-oracles/tree/main/data).

**{len(tools) - 1} tools** ({ncheck_t} run and compared), **{len(meas)} measures** grouped into {len(concepts)} concepts in {len(families)} families, **{len(d['capabilities'])} tool-by-measure entries** ({n_checked} checked by running the tool), **{len(d['findings'])} findings** about other tools' behaviour, and {len(d['results'])} benchmark rows.

## Where to go

{table(['Page', 'What it holds'], [
 ['[Capability matrix](matrix.html)', 'Measure by tool, grouped by family, subfamily and concept, with the state of each entry.'],
 ['[Measures](measures/)', 'Families, subfamilies and one page per concept; each concept page has a section per measure (variant) with implementations, convention differences, tolerances, findings, citations.'],
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
        ("measures.json", "Measures: id, name, original family, concept, variant label, definition, citation keys."),
        ("concepts.json", "Concepts: id, name, family, subfamily, definition, citation keys. A concept groups measures that are the same quantity, alternative algorithms, options or one tool's function for it."),
        ("aliases.csv", "Old measure id to concept page and anchor (generated). Join key: `measure`."),
        ("capabilities.csv", "Measure by tool: state, API names, comparison counts. Join keys: `measure`, `tool`."),
        ("conventions.json", "Per measure, variant and tool: scope, call, outcome, differing conditions, normalization/direction/weights/self-loops/ties/defaults dimensions, note, tolerance."),
        ("findings.json", "Bugs, disagreements and limitations in other tools."),
        ("benchmarks/results.csv", "Timing and memory of other tools; method in `data/benchmarks/method.md`."),
        ("references.bib", "BibTeX for every cited key.")]]
    body = "# Data and schemas\n\n" + table(["File", "Content"], schema_rows) + """

Each JSON or CSV file has a JSON Schema in `data/schema/` (draft 2020-12). `python3 scripts/build.py --check` validates all of them with a stdlib-only validator and checks the joins below, that every measure appears in exactly one concept page, and that every alias resolves to an anchor on its page. How measures were grouped into concepts and concepts into subfamilies is written down in [`data/README.md`](https://github.com/knapply/net-oracles/blob/main/data/README.md).

## Joins

- `measures.json[].concept` is `concepts.json[].id`; `aliases.csv.measure` is `measures.json[].id` and `aliases.csv.concept` is `concepts.json[].id`. The page of a measure is `aliases.csv.page` plus `#` plus `aliases.csv.anchor`.
- `capabilities.csv.measure` is `measures.json[].id`; `capabilities.csv.tool` is `tools.json[].id`.
- `conventions.json[].measure`, `.tool` use the same ids. `.variant` names one parameterization of the measure (for example normalized or weighted).
- `findings.json[].tool`, `.measure` (nullable) use the same ids.
- `benchmarks/results.csv.tool` is `tools.json[].id`.
- Citation keys in `tools.json[].citation_key`, `measures.json[].references`, `concepts.json[].references`, `findings.json[].references` and `conventions.json[].reference` are keys of `references.bib`.

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
        cs = sorted(caps_by_t.get(t["id"], []), key=lambda r: mkey(r["measure"]))
        cnt = collections.Counter(c["state"] for c in cs)
        info = [["Identifier", code(t["id"])], ["Language", esc(t["language"] or "")], ["Version tested", esc(t["version_tested"] or "not recorded")],
                ["License", esc(t["license"] or "not recorded")], ["Homepage", ("<%s>" % t["homepage"]) if t["homepage"] else "none recorded"],
                ["Role", t["role"]], ["Citation", cite(t["citation_key"], "../") if t["citation_key"] else ""]]
        body = "# %s\n\n" % esc(t["name"]) + table(["Field", "Value"], info) + "\n\n## How it was run\n\n" + esc(t["how_run"]) + "\n"
        if t["api_listing"] and t["api_listing"]["method"]:
            body += "\nCapabilities listed by %s of %s.\n" % (esc(t["api_listing"]["method"]), esc(t["api_listing"]["source"] or "its documentation"))
        if cs:
            body += "\n## Coverage\n\n" + table(["State", "Measures"], [[STATE_TXT[k] + " (" + STATE_SYM[k] + ")", cnt[k]] for k in STATE_SYM if cnt[k]]) + "\n"
            body += "\n## Measures\n\n" + table(["Family", "Subfamily", "Concept", "Measure (variant)", "State", "API names"], [
                [esc(cid_[mid[c["measure"]]["concept"]]["family"]), esc(cid_[mid[c["measure"]]["concept"]]["subfamily"]), "[%s](%s)" % (esc(cid_[mid[c["measure"]]["concept"]]["name"]), curl(cid_[mid[c["measure"]]["concept"]], "../")), mlink(c["measure"], "../", esc(mid[c["measure"]]["variant"])), STATE_SYM[c["state"]] + " " + STATE_TXT[c["state"]], code(c["api_names"]) if c["api_names"] else ""] for c in cs]) + "\n"
        fs = fnd_by_t.get(t["id"], [])
        if fs:
            body += "\n## Findings\n\n" + table(["Id", "Kind", "Title"], [["[%s](../findings.html#%s)" % (f["id"], f["id"].lower()), f["kind"], esc(f["title"])] for f in fs]) + "\n"
        files["tools/%s.md" % t["id"]] = page({"title": yq(t["name"]), "layout": "default", "parent": "Tools"}, body)

    # measures index, family pages, concept pages
    fam_concepts = collections.OrderedDict((f, [c for c in concepts if c["family"] == f]) for f in families)
    body = "# Measures\n\nMeasures are grouped into concepts (the same quantity, an alternative algorithm, a normalization, direction or weighting option, or one tool's function for it), concepts into subfamilies, and subfamilies into families. Each concept has one page with a section per measure (variant). The [capability matrix](../matrix.html) shows the same measures against all tools; `data/aliases.csv` maps every measure id to its concept page and anchor.\n\n"
    body += table(["Family", "Subfamilies", "Concepts", "Measures"], [[
        "[%s](%s/)" % (esc(f), fam_slug(f)), len({c["subfamily"] for c in cs}), len(cs), sum(len(mem[c["id"]]) for c in cs)] for f, cs in fam_concepts.items()]) + "\n"
    for f, cs in fam_concepts.items():
        body += "\n## %s\n\n" % esc(f)
        subs = collections.OrderedDict()
        for c in cs: subs.setdefault(c["subfamily"], []).append(c)
        body += " · ".join("%s (%d)" % (esc(sf), len(sc)) for sf, sc in subs.items()) + "\n"
    files["measures/index.md"] = page({"title": "Measures", "layout": "default", "nav_order": 4, "has_children": "true", "permalink": "/measures/"}, body)
    for fi, (f, cs) in enumerate(fam_concepts.items()):
        subs = collections.OrderedDict()
        for c in cs: subs.setdefault(c["subfamily"], []).append(c)
        nm = sum(len(mem[c["id"]]) for c in cs)
        body = "# %s\n\n%d measures in %d concepts and %d subfamilies. Each concept page has a section per measure (variant); the anchor of a section is the measure id (characters other than letters, digits, underscore, dot and hyphen become hyphens).\n" % (esc(f), nm, len(cs), len(subs))
        for sf, sc in subs.items():
            body += "\n## %s\n\n" % esc(sf)
            body += table(["Concept", "Measures", "Tools", "Definition"], [[
                "[%s](%s.html)" % (esc(c["name"]), c["id"]), len(mem[c["id"]]), len({r["tool"] for m in mem[c["id"]] for r in caps_by_m[m["id"]]}), esc(c["definition"] if len(c["definition"]) <= 160 else c["definition"][:157].rsplit(" ", 1)[0] + "...")] for c in sc]) + "\n"
        files["measures/%s/index.md" % fam_slug(f)] = page({"title": yq(f), "layout": "default", "parent": "Measures", "has_children": "true", "nav_order": fi + 1, "permalink": "/measures/%s/" % fam_slug(f)}, body)
    for c in concepts:
        ms_ = mem[c["id"]]
        body = "# %s {#concept-top}\n\nFamily: [%s](index.html). Subfamily: %s. Concept id: %s. %d measure%s.\n\n## Definition {#concept-definition}\n\n%s\n" % (
            esc(c["name"]), esc(c["family"]), esc(c["subfamily"]), code(c["id"]), len(ms_), "" if len(ms_) == 1 else "s", esc(c["definition"]))
        if len(ms_) > 1:
            body += "\n## Variants {#concept-variants}\n\n" + table(["Variant", "Measure id", "Tools"], [
                ["[%s](#%s)" % (esc(m["variant"]), slug(m["id"])), code(m["id"]), len({r["tool"] for r in caps_by_m[m["id"]]})] for m in ms_]) + "\n"
        if c["references"]:
            body += "\n## References {#concept-references}\n\n" + ", ".join(cite(k, "../../") for k in c["references"]) + "\n"
        for m in ms_:
            cs_ = sorted(caps_by_m[m["id"]], key=lambda r: tool_order.index(r["tool"]))
            body += "\n## %s {#%s}\n\nMeasure id: %s. Original family: %s.\n" % (esc(m["variant"]), slug(m["id"]), code(m["id"]), esc(m["family"]))
            if m["name"] != m["variant"]: body += "\nName: %s.\n" % esc(m["name"])
            body += "\n**Definition.** %s\n" % esc(m["definition"])
            body += "\n**Implementations**\n\n" + table(["Tool", "State", "API names", "Source"], [
                ["[%s](../../tools/%s.html)" % (esc(tid[r["tool"]]["name"]), r["tool"]), STATE_SYM[r["state"]] + " " + STATE_TXT[r["state"]], code(r["api_names"]) if r["api_names"] else "", esc(r["source"])] for r in cs_]) + "\n"
            cv = [x for x in conv_by_m.get(m["id"], []) if x["tool"] in tid]
            if cv:
                body += "\n**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).\n\n"
                cv = sorted(cv, key=lambda x: (x["variant"], tool_order.index(x["tool"])))
                body += table(["Variant", "Tool", "Scope", "Outcome", "Differs when", "Conventions", "Tolerance", "Call", "Note"], [[
                    code(x["variant"]), esc(tid[x["tool"]]["name"]), x["scope"], x["outcome"], esc(", ".join(x["differs_when"] + ["(no value) " + u for u in x["undefined_when"]])),
                    esc(", ".join(x["dimensions"])), "abs %g, rel %g" % (x["tolerance"]["abs"], x["tolerance"]["rel"]), code(x["call"]) if x["call"] else "", esc(x["note"])] for x in cv]) + "\n"
                hl = harness_links(cv, {x["tool"] for x in cv}, "../../")
                if hl: body += "\n**Harness files:** " + "; ".join(hl) + "\n"
            fs = fnd_by_m.get(m["id"], [])
            if fs:
                body += "\n**Findings**\n\n" + table(["Id", "Tool", "Kind", "Title"], [["[%s](../../findings.html#%s)" % (x["id"], x["id"].lower()), esc(tid[x["tool"]]["name"]), x["kind"], esc(x["title"])] for x in fs]) + "\n"
            if m["references"]:
                body += "\n**References:** " + ", ".join(cite(k, "../../") for k in m["references"]) + "\n"
            tk = sorted({tid[r["tool"]]["citation_key"] for r in cs_ if tid[r["tool"]]["citation_key"]})
            if tk: body += "\n**Tools cited:** " + ", ".join(cite(k, "../../") for k in tk) + "\n"
        files["measures/%s/%s.md" % (fam_slug(c["family"]), c["id"])] = page({"title": yq(c["name"]), "layout": "default", "parent": yq(c["family"]), "grand_parent": "Measures", "nav_exclude": "true"}, body)

    # matrix
    body = "# Capability matrix\n\n" + LEGEND + "\n\nColumns are tool identifiers (see [Tools](tools/)). Rows are measures, grouped by family, subfamily and concept; the concept name links to its page and each variant links to its section.\n"
    cap = {(r["measure"], r["tool"]): r["state"] for r in d["capabilities"]}
    for f, cs in fam_concepts.items():
        body += "\n## %s\n\n%d measures in %d concepts.\n" % (esc(f), sum(len(mem[c["id"]]) for c in cs), len(cs))
        subs = collections.OrderedDict()
        for c in cs: subs.setdefault(c["subfamily"], []).append(c)
        for sf, sc in subs.items():
            ms_ = [m for c in sc for m in mem[c["id"]]]
            ts = [t for t in tool_order if any((m["id"], t) in cap for m in ms_)]
            rows = []
            for c in sc:
                for i, m in enumerate(mem[c["id"]]):
                    rows.append(["[%s](%s)" % (esc(c["name"]), curl(c, "")) if i == 0 else "", mlink(m["id"], "", esc(m["variant"]))] + [STATE_SYM.get(cap.get((m["id"], t), ""), "") for t in ts])
            body += "\n### %s\n\n%d measures in %d concepts.\n\n" % (esc(sf), len(ms_), len(sc))
            body += table(["Concept", "Variant"] + [t for t in ts], rows) + "\n"
    files["matrix.md"] = page({"title": "Capability matrix", "layout": "default", "nav_order": 2}, body)

    # findings
    body = "# Findings\n\nBugs, disagreements and limitations observed in other tools. `kind` is *defect* (wrong under the published definition), *convention* (differs by a convention) or *limitation* (refuses or cannot represent the input). `status` is *reproduced* (minimal reproduction recorded), *observed* (seen on a shared corpus of test graphs) or *reported* (public discussion, not re-measured). Versions are those tested; a finding may not hold in later versions.\n\n"
    body += table(["Id", "Tool", "Version", "Measure", "Kind", "Status", "Title"], [[
        "[%s](#%s)" % (f["id"], f["id"].lower()), esc(tid[f["tool"]]["name"]), esc(f["version"]), mlink(f["measure"], "", esc(mid[f["measure"]]["name"])) if f["measure"] else "", f["kind"], f["status"], esc(f["title"])] for f in d["findings"]]) + "\n"
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
            rows.append([mlink(me, "", esc(me)) if me in mid else esc(me), esc(tid[t]["name"]), len(rs), len(sec), "%.4g" % statistics.median(sec) if sec else "", "%.4g" % statistics.median(mb) if mb else ""])
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

    # aliases: old measure id -> concept page and anchor
    arows = [[m["id"], m["concept"], cid_[m["concept"]]["family"], cid_[m["concept"]]["subfamily"], mpath(m["id"])[0], mpath(m["id"])[1]] for m in sorted(d["measures"], key=lambda m: m["id"])]
    buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(["measure", "concept", "family", "subfamily", "page", "anchor"]); w.writerows(arows)
    files["data/aliases.csv"] = buf.getvalue()

    # llms.txt
    files["llms.txt"] = llms(d, families)
    return files


def llms(d, families):
    n_checked = sum(1 for r in d["capabilities"] if r["state"].startswith("checked"))
    return f"""# net-oracles

A neutral survey of network-analysis software. It records which tool implements which measure, how conventions differ between tools (normalization, direction, weights, self-loops, ties, defaults, tolerances), bugs and disagreements found in other tools, how tools were benchmarked, and citations. It describes other tools only.

Counts: {len(d['tools'])} tool records, {len(d['measures'])} measures grouped into {len(d['concepts'])} concepts in {len(families)} families, {len(d['capabilities'])} measure-by-tool entries ({n_checked} checked by running the tool), {len(d['conventions'])} convention records, {len(d['findings'])} findings, {len(d['results'])} benchmark rows.

Source of truth is data/. Pages are generated from it by scripts/build.py (python3, standard library only). Raw base: https://raw.githubusercontent.com/knapply/net-oracles/main/ ; site: https://knapply.github.io/net-oracles/

## Data files and schemas

- data/tools.json (schema data/schema/tools.schema.json): array of tools. Fields: id, name, language, version_tested, license, homepage, citation_key, role (checked | documented-only | benchmarked-only | reference), how_run, api_listing.
- data/measures.json (data/schema/measures.schema.json): array of measures (one per tool function or published quantity; the unit all other files refer to). Fields: id, name, family (the original catalogue family; browsing families come from concepts.json), concept (id in concepts.json), variant (short label of this measure within its concept), definition, references (BibTeX keys).
- data/concepts.json (data/schema/concepts.schema.json): array of concepts. A concept groups measures that are the same quantity, an alternative algorithm for it, a normalization, direction or weighting option of it, or one tool's function for it; measures that compute different quantities are never merged. Fields: id (snake_case), name, family, subfamily, definition, references (BibTeX keys, union of its measures' keys). The grouping rules are in data/README.md.
- data/aliases.csv (data/schema/aliases.schema.json, generated by scripts/build.py): one row per measure id. Columns: measure, concept, family, subfamily, page (site-relative path of the concept page), anchor (section of that page for this measure). Use it to map an old measure id, or any measure id found in capabilities.csv, conventions.json, findings.json or benchmarks, to its concept page.
- data/capabilities.csv (data/schema/capabilities.schema.json): one row per measure and tool. Columns: measure, tool, state, api_names (semicolon separated), comparisons_agreeing, comparisons_differing, source.
  State vocabulary: reported-in-docs (listed in the tool's documentation or public API, not run); checked-agrees (run, agrees with an independent evaluation within tolerance); checked-convention (run, differs on some inputs by a documented convention); checked-defect (run, wrong under the published definition); checked-no-value (run, returns no value or an error on the compared inputs). Tools with role documented-only only have reported-in-docs. A blank (absent row) means not known to implement it.
- data/conventions.json (data/schema/conventions.schema.json): array of records per measure, variant and tool. Fields: measure, variant, manifest, tool, scope (any | directed | undirected), weights_required, call (how the tool was invoked), outcome (agrees | differs | no-value-on-some-inputs | documented), differs_when and undefined_when (structural conditions such as loops, multi_edges, directed, disconnected, ties), only_on, dimensions (normalization, direction, weights, self_loops, multi_edges, ties, defaults), note, tolerance {{abs, rel}} (0 means exact), optional differs_on_inputs, no_value_on_inputs, reference.
- data/findings.json (data/schema/findings.schema.json): array of findings. Fields: id, tool, version, measure (nullable), kind (defect | convention | limitation), status (reproduced | observed | reported), title, reproduction, observed, expected, evidence, references.
- data/benchmarks/results.csv (data/schema/benchmarks-results.schema.json): timing rows of other tools. Columns: suite, graph, nodes, edges, measure, tool, tool_version, seconds (empty when over budget), peak_megabytes, threads, status. Method: data/benchmarks/method.md.
- data/references.bib: BibTeX for every key used above.

## Joins

measures.concept -> concepts.id; aliases.measure -> measures.id; aliases.concept -> concepts.id; capabilities.measure -> measures.id; capabilities.tool -> tools.id; conventions.measure/tool -> measures.id/tools.id; findings.tool -> tools.id; findings.measure -> measures.id (nullable); benchmarks.tool -> tools.id; every citation key -> references.bib. Page for a concept: measures/<family-slug>/<concept id>.html, where family-slug is the family name in lower case with runs of other characters replaced by a hyphen (see aliases.csv, column page). Each measure is a section of its concept page with anchor = the measure id (characters other than letters, digits, underscore, dot and hyphen become hyphens), so the page of a measure is aliases.page + "#" + aliases.anchor. Family overview: measures/<family-slug>/. Page for a tool: tools/<id>.html. To join a measure-level table to concepts: join on measure id with measures.json (concept, variant) and then with concepts.json (family, subfamily).

## Conventions of the data

Edge ends are called source and target. A reference value is the published definition evaluated independently. UCINET is documented-only: it was never run. Tool versions are those tested; findings may not hold in later versions.

## Regenerate and validate

python3 scripts/build.py          # write pages
python3 scripts/build.py --check  # validate data against schemas, check that every measure appears in exactly one concept page and every alias resolves, and fail if pages are stale
"""


# ---------------------------------------------------------------- main
GENERATED_DIRS = ["tools", "measures"]
GENERATED_TOP = ["index.md", "data.md", "matrix.md", "findings.md", "benchmarks.md", "references.md", "llms.txt", "data/aliases.csv"]


def existing_generated():
    out = set(p for p in GENERATED_TOP if os.path.exists(os.path.join(ROOT, p)))
    for dname in GENERATED_DIRS:
        base = os.path.join(ROOT, dname)
        for dp, _, fns in os.walk(base):
            for fn in fns: out.add(os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/"))
    return out


def check_pages(d, files):
    """Every measure is in exactly one concept page, and every alias resolves to an anchor on its page."""
    errs = []
    rows = list(csv.DictReader(io.StringIO(files["data/aliases.csv"])))
    for r in rows:
        if r["anchor"].startswith("concept-"): errs.append("anchor %s clashes with the reserved concept- prefix" % r["anchor"])
    asch = load_json("schema/aliases.schema.json")
    for i, r in enumerate(rows): errs += validate(dict(r), asch, "aliases[%d]" % i)
    seen = collections.Counter(r["measure"] for r in rows)
    for m in d["measures"]:
        if seen[m["id"]] != 1: errs.append("measure %s has %d aliases" % (m["id"], seen[m["id"]]))
    cmem = {c["id"]: {m["id"] for m in d["measures"] if m["concept"] == c["id"]} for c in d["concepts"]}
    anchors = collections.defaultdict(list)
    for r in rows:
        p = r["page"][:-5] + ".md"
        if p not in files: errs.append("alias %s: no page %s" % (r["measure"], r["page"])); continue
        if ("{#%s}" % r["anchor"]) not in files[p]: errs.append("alias %s: no anchor %s in %s" % (r["measure"], r["anchor"], r["page"]))
        anchors[(r["page"], r["anchor"])].append(r["measure"])
    for k, v in anchors.items():
        if len(v) > 1: errs.append("anchor %s used by %s" % (k, v))
    pages = {p for p in files if p.startswith("measures/") and p.count("/") == 2 and not p.endswith("/index.md")}
    if len(pages) != len(d["concepts"]): errs.append("concept pages %d != concepts %d" % (len(pages), len(d["concepts"])))
    for p in pages:
        body = files[p]
        found = {a for a in re.findall(r"^## .*\{#([^}]+)\}\s*$", body, re.M) if not a.startswith("concept-")}
        want = {slug(i) for c in d["concepts"] if p.endswith("/%s.md" % c["id"]) for i in cmem[c["id"]]}
        if found != want: errs.append("page %s: sections do not match its measures" % p)
    return errs


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
    perrs = check_pages(d, files)
    if perrs:
        print("page validation failed:")
        for e in perrs[:50]: print("  " + e)
        return 1
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
