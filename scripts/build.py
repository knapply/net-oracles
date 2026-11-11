#!/usr/bin/env python3
"""Generate every page of the site from data/ and validate data/ against data/schema/.

    python3 scripts/build.py          write pages
    python3 scripts/build.py --check  fail if validation fails or any generated file is stale

Standard library only.
"""
import csv, io, json, os, re, sys, statistics, collections, glob, html

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
        "hosted": load_csv("benchmarks/hosted.csv") if os.path.exists(os.path.join(DATA, "benchmarks", "hosted.csv")) else [],
        "hosted_env": load_json("benchmarks/hosted-environments.json") if os.path.exists(os.path.join(DATA, "benchmarks", "hosted-environments.json")) else [],
        "reasons": load_json("reasons.json"), "fixtures": load_json("fixtures.json"),
        "bib": parse_bib(open(os.path.join(DATA, "references.bib"), encoding="utf-8").read()),
    }
    d["vocabulary"] = load_json("definitions/_vocabulary.json")["cases"]
    d["definitions"] = {}
    for fp in sorted(glob.glob(os.path.join(DATA, "definitions", "*.json"))):
        fn = os.path.basename(fp)
        if fn.startswith("_"): continue
        d["definitions"][fn] = load_json("definitions/" + fn)
    return d


def check_data(d):
    errs = []
    sch = lambda n: load_json("schema/" + n)
    for name, f in [("tools", "tools"), ("measures", "measures"), ("concepts", "concepts"), ("conventions", "conventions"), ("findings", "findings"), ("reasons", "reasons"), ("fixtures", "fixtures")]:
        errs += validate(d[name], sch(f + ".schema.json"), name)
    for name, f in [("capabilities", "capabilities"), ("results", "benchmarks-results"), ("hosted", "benchmarks-hosted")]:
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
    for r in d["hosted"]:
        if r["tool"] not in tools: errs.append("hosted benchmarks: unknown tool " + r["tool"])
    errs += validate(d["hosted_env"], load_json("schema/benchmarks-hosted-environments.schema.json"), "hosted_env")
    for fx in d["fixtures"]:
        for k in fx["references"]:
            if k not in bib: errs.append("fixtures: missing bib key " + k)
    if len({fx["name"] for fx in d["fixtures"]}) != len(d["fixtures"]): errs.append("duplicate fixture names")
    errs += check_reasons(d)
    errs += check_definitions(d)
    return errs


def balanced(latex):
    """Braces of a LaTeX string balance (escaped braces are skipped) and no brace closes before it opens."""
    depth = 0; i = 0
    while i < len(latex):
        c = latex[i]
        if c == "\\": i += 2; continue
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0: return False
        i += 1
    return depth == 0


def check_definitions(d):
    """definitions/<family-slug>.json: structure, vocabulary, tool ids, measure ids, bibliography keys, LaTeX braces."""
    errs = []
    fam_slug = lambda f: re.sub(r"[^a-z0-9]+", "-", f.lower()).strip("-")
    schema = load_json("schema/definitions.schema.json")
    vocab = d["vocabulary"]
    for k, v in vocab.items():
        if not re.fullmatch(r"[a-z][a-z0-9_]*", k): errs.append("vocabulary: bad id " + k)
        if not v.get("label") or len(v.get("description", "")) < 20: errs.append("vocabulary: %s needs a label and a description" % k)
    tools = {t["id"] for t in d["tools"]}; bib = set(d["bib"]); findings = {f["id"] for f in d["findings"]}
    meas_of = collections.defaultdict(set); fam_of = {}
    for m in d["measures"]: meas_of[m["concept"]].add(m["id"])
    for c in d["concepts"]: fam_of[c["id"]] = c["family"]
    rsn = {(r["measure"], r["tool"]) for r in d["reasons"]}
    tools_of = collections.defaultdict(set)
    mconcept = {m["id"]: m["concept"] for m in d["measures"]}
    for r in d["capabilities"]: tools_of[mconcept[r["measure"]]].add(r["tool"])
    for fn, df in d["definitions"].items():
        w = "definitions/" + fn
        errs += validate(df, schema, w)
        if not isinstance(df, dict) or "family" not in df: continue
        if fn != fam_slug(df["family"]) + ".json": errs.append("%s: file name must be %s.json for family %r" % (w, fam_slug(df["family"]), df["family"]))
        if df["family"] not in set(fam_of.values()): errs.append("%s: unknown family %r" % (w, df["family"]))
        for cid, c in df["concepts"].items():
            w2 = "%s %s" % (w, cid)
            if cid not in fam_of: errs.append(w2 + ": unknown concept"); continue
            if fam_of[cid] != df["family"]: errs.append(w2 + ": concept belongs to family %r" % fam_of[cid])
            st = c["status"]
            if st != "complete" and not c.get("note", "").strip(): errs.append(w2 + ": a note is required for status " + st)
            if st == "name_only" and (c.get("formulas") or c.get("edge_cases")): errs.append(w2 + ": name_only concepts carry no formulas or edge cases")
            if st == "complete":
                if not c.get("notation"): errs.append(w2 + ": complete needs a notation")
                if not c.get("formulas"): errs.append(w2 + ": complete needs formulas")
                if not c.get("edge_cases"): errs.append(w2 + ": complete needs edge cases")
                missing = meas_of[cid] - set(c.get("variants", {}))
                if missing: errs.append("%s: no variants entry for %s" % (w2, ", ".join(sorted(missing))))
            for k in c.get("variants", {}):
                if k not in meas_of[cid]: errs.append("%s: variants key %s is not a measure of the concept" % (w2, k))
            for i, f in enumerate(c.get("formulas", [])):
                if not f["latex"].strip(): errs.append("%s formulas[%d]: empty latex" % (w2, i))
                elif not balanced(f["latex"]): errs.append("%s formulas[%d] (%s): unbalanced braces" % (w2, i, f["name"]))
            for i, n in enumerate(c.get("notation", [])):
                if not n["symbol"].strip() or not balanced(n["symbol"]): errs.append("%s notation[%d]: empty or unbalanced symbol" % (w2, i))
            texts = [n["meaning"] for n in c.get("notation", [])] + [f["where"] for f in c.get("formulas", [])] + list(c.get("variants", {}).values()) + [e["definition_gives"] for e in c.get("edge_cases", [])]
            for t in texts:
                if t.count("\\(") != t.count("\\)"): errs.append("%s: unbalanced inline math in %r" % (w2, t[:50]))
            seen = set()
            for e in c.get("edge_cases", []):
                if e["case"] not in vocab: errs.append("%s: unknown edge case %r" % (w2, e["case"]))
                if e["case"] in seen: errs.append("%s: edge case %s listed twice" % (w2, e["case"]))
                seen.add(e["case"])
                for t, x in e.get("tools", {}).items():
                    w3 = "%s %s/%s" % (w2, e["case"], t)
                    if t not in tools: errs.append(w3 + ": unknown tool"); continue
                    if t not in tools_of[cid]: errs.append(w3 + ": tool has no entry for this concept")
                    for f in ("status", "behaviour", "source"):
                        if f not in x or not str(x[f]).strip(): errs.append("%s: missing %s" % (w3, f))
                    if x.get("status") not in ("agrees", "differs", "no_value", "documented", "not_recorded"): errs.append(w3 + ": bad status")
                    if "measure" in x and (x["measure"], t) not in rsn: errs.append("%s: no reason entry for %s/%s" % (w3, x["measure"], t))
                    if "measure" in x and mconcept.get(x["measure"]) != cid: errs.append("%s: measure %s is not in the concept" % (w3, x["measure"]))
                    if "finding" in x and x["finding"] not in findings: errs.append("%s: unknown finding %s" % (w3, x["finding"]))
            for k in c.get("references", []):
                if k not in bib: errs.append("%s: missing bib key %s" % (w2, k))
    return errs


NEEDS_REASON = ("reported-in-docs", "checked-convention", "checked-defect", "checked-no-value")


def check_reasons(d):
    """Every capabilities row whose state is not checked-agrees has exactly one record in reasons.json, with the content its state requires."""
    errs = []
    caps = {(r["measure"], r["tool"]): r["state"] for r in d["capabilities"]}
    fids = {f["id"] for f in d["findings"]}
    seen = collections.Counter((r["measure"], r["tool"]) for r in d["reasons"])
    for k, n in seen.items():
        if n > 1: errs.append("reasons: %s/%s appears %d times" % (k[0], k[1], n))
        if k not in caps: errs.append("reasons: %s/%s is not a capabilities row" % k)
        elif caps[k] == "checked-agrees": errs.append("reasons: %s/%s is checked-agrees and needs no reason" % k)
    for k, st in caps.items():
        if st in NEEDS_REASON and k not in seen: errs.append("capabilities: %s/%s is %s and has no reason in reasons.json" % (k[0], k[1], st))
    for r in d["reasons"]:
        k = (r["measure"], r["tool"]); w = "reasons %s/%s" % k
        if k in caps and caps[k] != r["state"]: errs.append("%s: state %s differs from capabilities.csv (%s)" % (w, r["state"], caps[k]))
        if not r["reason"].strip(): errs.append(w + ": empty reason")
        if r["reason_incomplete"] and not r.get("missing", "").strip(): errs.append(w + ": reason_incomplete without a statement of what is missing")
        if not r["reason_incomplete"] and r.get("missing"): errs.append(w + ": 'missing' given but reason_incomplete is false")
        for f in r.get("findings", []):
            if f not in fids: errs.append("%s: unknown finding %s" % (w, f))
        need = {"checked-convention": ["tool_version", "convention", "variants", "inputs", "comparisons"],
                "checked-defect": ["tool_version", "observed", "expected", "findings", "inputs", "comparisons"],
                "checked-no-value": ["tool_version", "inputs", "comparisons"],
                "reported-in-docs": ["why_not_run", "documentation"]}.get(r["state"], [])
        for f in need:
            if f in r and r[f] not in ("", [], None): continue
            if f == "convention" and r["reason_incomplete"]: continue
            if f == "variants" and r["state"] == "checked-no-value": continue
            errs.append("%s: %s required for %s" % (w, f, r["state"]))
        if r["state"] == "checked-convention":
            if not any(v["outcome"] == "differs" for v in r.get("variants", [])): errs.append(w + ": no variant with outcome differs")
            if not r.get("inputs", {}).get("differs", {}).get("tags") and not r.get("inputs", {}).get("differs", {}).get("named"):
                errs.append(w + ": no inputs on which the values differ")
        if r["state"] == "checked-defect" and not (r.get("inputs", {}).get("differs", {}).get("named") or r.get("inputs", {}).get("differs", {}).get("tags")):
            errs.append(w + ": no inputs on which the value is wrong")
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


def md_inline(s):
    """Cell text written as inline markdown (links, code spans, emphasis, backslash escapes from esc()) to HTML; HTML already in the text passes through."""
    codes = []
    def keep(m):
        codes.append("<code>%s</code>" % re.sub(r"&(?!(?:lt|gt|amp|quot|#\d+);)", "&amp;", m.group(1).replace("\\|", "|")).replace("<", "&lt;").replace(">", "&gt;"))
        return "\x00%d\x00" % (len(codes) - 1)
    s = re.sub(r"`([^`]*)`", keep, str(s))
    s = re.sub(r"&(?!(?:lt|gt|amp|quot|#\d+);)", "&amp;", s)
    s = re.sub(r"(?<!\\)\[((?:[^\]\\]|\\.)*)\]\(([^)\s]*)\)", lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\\*])\*([^*\s][^*]*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\\([\\*\[\]_|`])", r"\1", s)
    return re.sub("\x00(\\d+)\x00", lambda m: codes[int(m.group(1))], s)


def pipe_tables_to_html(text):
    """Markdown pipe tables inside hand-written text (data/method.md, benchmarks/method.md) to the HTML tables of table()."""
    lines = text.split("\n"); out = []; i = 0
    cells = lambda l: [c.strip() for c in re.split(r"(?<!\\)\|", l.strip().strip("|"))]
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            head = cells(lines[i]); i += 2; rows = []
            while i < len(lines) and lines[i].startswith("|"): rows.append(cells(lines[i])); i += 1
            out.append(table(head, rows))
        else: out.append(lines[i]); i += 1
    return "\n".join(out)


def table(head, rows):
    """An HTML table in the theme's table wrapper (cells are inline markdown), so that the site search shows text and not pipe syntax."""
    out = ["<tr>" + "".join("<th>%s</th>" % md_inline(h) for h in head) + "</tr>"]
    body = ["<tr>" + "".join("<td>%s</td>" % md_inline(c) for c in r) + "</tr>" for r in rows]
    return '<div class="table-wrapper"><table><thead>%s</thead><tbody>%s</tbody></table></div>' % (out[0], "".join(body))


def page(front, body):
    fm = "---\n" + "\n".join("%s: %s" % (k, v) for k, v in front.items()) + "\n---\n\n"
    return fm + "{% raw %}\n\n" + body.strip() + "\n{% endraw %}\n"


def yq(s): return json.dumps(s, ensure_ascii=False)


STATE_SYM = {"checked-agrees": "✓", "checked-convention": "≠", "checked-defect": "✗", "checked-no-value": "∅", "reported-in-docs": "·"}
STATE_TXT = {"checked-agrees": "checked, agrees", "checked-convention": "checked, differs by convention", "checked-defect": "checked, defect",
             "checked-no-value": "checked, no value on some inputs", "reported-in-docs": "reported in docs"}
LEGEND = "✓ checked, agrees; ≠ checked, differs by a documented convention; ✗ checked, defect found; ∅ checked, no value on the compared inputs; · reported in the tool's documentation (not run); blank: not known to implement it."


STATE_CLS = {"checked-agrees": "ok", "checked-convention": "conv", "checked-defect": "defect", "checked-no-value": "nov", "reported-in-docs": "docs"}


METHOD = "method.html"
STATE_DEF = {
    "checked-agrees": "The tool was run and its value equals the reference value of the published definition, within the stated tolerance, on every fixture the tool accepts. No convention is mapped.",
    "checked-convention": "The tool was run and on some fixtures its value differs from the reference value because it follows a different, documented convention. The entry states the convention, what each side does, the relation between the two values and the tolerances.",
    "checked-defect": "The tool was run and on some inputs its value is wrong under the published definition. The entry states what is wrong, on which inputs, observed against expected, the tool version and the finding.",
    "checked-no-value": "The tool was run but gave no value on the compared inputs, so no comparison could be made. The entry states on which inputs and why.",
    "reported-in-docs": "The tool lists the capability in its documentation or public API, but it was not run for this measure. The entry states why and the documentation source.",
}


def state_badge(k, rel="", title=None):
    """A glyph badge that links to the definition of the state on the method page."""
    t = title if title is not None else STATE_TXT[k]
    return '<a class="st st-g st-%s" href="%s%s#state-%s" title="%s" aria-label="%s">%s</a>' % (STATE_CLS[k], rel, METHOD, k, esc_attr(t), esc_attr(STATE_TXT[k]), STATE_SYM[k])


def state_tag(k, rel=""):
    """A badge with the state in words, linking to its definition."""
    return '<a class="st st-t st-%s" href="%s%s#state-%s"><span class="g" aria-hidden="true">%s</span>%s</a>' % (STATE_CLS[k], rel, METHOD, k, STATE_SYM[k], STATE_TXT[k])


def esc_attr(s): return re.sub(r"\s+", " ", str(s)).strip().replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;").replace("|", "&#124;")


def legend_html(rel=""):
    items = "".join("<span>%s %s</span>" % (state_badge(k, rel), STATE_TXT[k]) for k in STATE_SYM)
    return ('<div class="legend" role="group" aria-label="State legend">' + items + '<span class="blank">blank: not known to implement it</span>'
            + '<span><a href="%s%s">How entries are labelled</a></span></div>' % (rel, METHOD))


def harness_links(conv_rows, tool_ids, rel="../"):
    """Links into harness/ (added by a later export); empty while the directory is absent."""
    if not os.path.isdir(HARNESS): return []
    # harness/ is not part of the website (it is excluded from the site
    # build), so link to the files in the repository instead.
    base = "https://github.com/knapply/net-oracles/tree/main/harness/"
    out = []
    for f in sorted({c["manifest"].replace("manifest.d/", "manifest/")
                     for c in conv_rows if c.get("manifest")}):
        if os.path.exists(os.path.join(HARNESS, f)):
            out.append("[harness/%s](%s%s)" % (f, base, f))
    for t in sorted(tool_ids):
        if os.path.isdir(os.path.join(HARNESS, "golden", t)):
            out.append("[harness/golden/%s/](%sgolden/%s/)" % (t, base, t))
    return out


# ---------------------------------------------------------------- definitions (rendering)
def hx(s): return html.escape(str(s), quote=False)
def hq(s): return html.escape(re.sub(r"\s+", " ", str(s)).strip(), quote=True)


EDGE_STATUS = {"agrees": ("ok", "agrees"), "differs": ("conv", "differs"), "no_value": ("nov", "no value"), "documented": ("docs", "documented")}


def render_definition(c, entry, ms_, tid, tool_order, caps_by_m, vocab, fam_findings=None):
    """HTML/markdown sections of one concept page from its definitions entry (None: not written)."""
    out = {"notation": "", "formulas": "", "variants": None, "edge": ""}
    if entry is None or entry["status"] == "name_only":
        out["formulas"] = "\n*Definition not yet written.*" + (" " + esc(entry["note"]) if entry else "") + "\n"
        return out
    if entry["status"] == "partial":
        out["formulas"] += "\n*Definition partly written:* " + esc(entry["note"]) + "\n"
    elif entry.get("note"):
        out["formulas"] += "\n*Note:* " + esc(entry["note"]) + "\n"
    if entry.get("notation"):
        rows = "".join("<tr><td>\\(%s\\)</td><td>%s</td></tr>" % (hx(n["symbol"]), hx(n["meaning"])) for n in entry["notation"])
        out["notation"] = '\n<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody>%s</tbody></table></div>\n' % rows
    for f in entry.get("formulas", []):
        out["formulas"] += ('\n<div class="formula-block"><p class="formula-name"><strong>%s</strong> <span class="applies">applies to: %s</span></p>'
                            '<div class="formula">\\[%s\\]</div><p class="formula-where">%s</p></div>\n') % (hx(f["name"]), hx(", ".join(f["applies_to"])), hx(f["latex"]), hx(f["where"]))
    if entry.get("variants") is not None and entry["variants"]:
        rows = ""
        for m in ms_:
            if m["id"] not in entry["variants"]: continue
            ntools = len({r["tool"] for r in caps_by_m[m["id"]]})
            rows += '<tr><td><a href="#%s">%s</a></td><td><code>%s</code></td><td>%d</td><td>%s</td></tr>' % (slug(m["id"]), hx(m["variant"]), hx(m["id"]), ntools, hx(entry["variants"][m["id"]]))
        out["variants"] = '\n<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody>%s</tbody></table></div>\n' % rows
    cases = entry.get("edge_cases", [])
    if cases:
        ctools = [t for t in tool_order if any(r["tool"] == t for m in ms_ for r in caps_by_m[m["id"]])]
        head = "<tr><th>Case</th><th>The published definition gives</th>" + "".join('<th><a href="../../tools/%s.html">%s</a></th>' % (t, hx(tid[t]["name"])) for t in ctools) + "</tr>"
        body = ""; det = ""
        for e in cases:
            v = vocab[e["case"]]
            row = '<tr><td title="%s"><strong>%s</strong></td><td class="def">%s</td>' % (hq(v["description"]), hx(v["label"]), hx(e["definition_gives"]))
            lis = ""
            for t in ctools:
                x = e.get("tools", {}).get(t)
                if not x or x["status"] == "not_recorded":
                    row += '<td><span class="nr" title="%s">not recorded</span></td>' % hq(x["behaviour"] if x else "The sources do not record this tool's behaviour on this input.")
                    if x: lis += "<li><strong>%s</strong>: not recorded. %s <em>(%s)</em></li>" % (hx(tid[t]["name"]), hx(x["behaviour"]), hx(x["source"]))
                    continue
                cls, word = EDGE_STATUS[x["status"]]
                href = ""
                if x.get("finding"): href = "../../findings.html#" + x["finding"].lower()
                elif x.get("measure"): href = "#why-%s-%s" % (slug(x["measure"]), t)
                badge = '<span class="st st-w st-%s">%s</span>' % (cls, word)
                if href: badge = '<a class="st st-w st-%s" href="%s" title="%s">%s</a>' % (cls, href, hq(x["behaviour"]), word)
                else: badge = '<span class="st st-w st-%s" title="%s">%s</span>' % (cls, hq(x["behaviour"]), word)
                row += "<td>%s</td>" % badge
                lis += "<li><strong>%s</strong>: %s. %s <em>(%s)</em></li>" % (hx(tid[t]["name"]), word, hx(x["behaviour"]), hx(x["source"]))
            body += row + "</tr>"
            det += "<details><summary>%s</summary><ul>%s</ul></details>" % (hx(v["label"]), lis or "<li>No tool entries.</li>")
        out["edge"] = ('\n<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead>%s</thead><tbody>%s</tbody></table></div>\n'
                       '\n**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.\n\n<div class="edge-details">%s</div>\n') % (head, body, det)
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
    rsn = {(r["measure"], r["tool"]): r for r in d["reasons"]}
    why_id = lambda m_, t_: "why-%s-%s" % (slug(m_), t_)

    def why_cell(m_, t_, rel):
        r = rsn.get((m_, t_))
        if not r: return ""
        href = ("" if rel is None else curl(cid_[mid[m_]["concept"]], rel)) + "#" + why_id(m_, t_)
        return "%s%s [details](%s)" % (esc(r["short"]), " *(reason incomplete)*" if r["reason_incomplete"] else "", href)
    families = sorted({c["family"] for c in concepts})
    defs_of = {}
    for df in d["definitions"].values(): defs_of.update(df["concepts"])
    tool_order = [t["id"] for t in tools]
    n_checked = sum(1 for r in d["capabilities"] if r["state"].startswith("checked"))
    cite = lambda k, rel: "[%s](%sreferences.html#%s)" % (k, rel, k)

    # index
    ncheck_t = sum(1 for t in tools if t["role"] == "checked")
    ntools = len(tools) - 1
    counts = [(ntools, "tools"), (len(meas), "measures"), (len(concepts), "concepts"), (len(d["findings"]), "findings"), (len(d["results"]), "benchmark rows")]
    hero = ('<section class="hero" aria-labelledby="hero-title">'
            '<canvas id="hero-graph" class="hero-graph" aria-hidden="true"></canvas>'
            '<div class="hero-body"><h1 id="hero-title">net-oracles</h1>'
            '<p class="hero-lead">Which network-analysis tool implements which measure, and where their answers differ.</p>'
            '<ul class="hero-counts">' + "".join("<li><b>%d</b>%s</li>" % c for c in counts) + '</ul></div></section>')
    cards = [("measures/", "Families", "%d families, %d concepts and %d measures." % (len(families), len(concepts), len(meas))),
             ("tools/", "Tools", "%d tools, %d run and compared." % (ntools, ncheck_t)),
             ("matrix.html", "Capability matrix", "Measure by tool, with the state of each entry and the reason for it."),
             ("method.html", "How entries are labelled", "What was compared, how, on which inputs, and what each state means."),
             ("findings.html", "Findings", "%d bugs, disagreements and limitations." % len(d["findings"])),
             ("benchmarks.html", "Benchmarks", "Method and %d timing rows." % len(d["results"])),
             ("references.html", "References", "Every cited package and paper."),
             ("data.html", "Data and schemas", "File formats, joins and the state vocabulary."),
             ("llms.txt", "llms.txt", "Every data file, its schema and how the files join, as plain text.")]
    cards_html = '<nav class="cards" aria-label="Sections">' + "".join('<a class="card" href="%s"><strong>%s</strong><span>%s</span></a>' % c for c in cards) + "</nav>"
    body = f"""{hero}

A neutral, citable survey of network-analysis software: which tool implements which measure, how their conventions differ, which bugs and disagreements were found, and how the tools were benchmarked. Every claim carries a citation key; every table on these pages is generated from the machine-readable files in [`data/`](https://github.com/knapply/net-oracles/tree/main/data).

**{len(tools) - 1} tools** ({ncheck_t} run and compared), **{len(meas)} measures** grouped into {len(concepts)} concepts in {len(families)} families, **{len(d['capabilities'])} tool-by-measure entries** ({n_checked} checked by running the tool), **{len(d['findings'])} findings** about other tools' behaviour, and {len(d['results'])} benchmark rows.

## Where to go

{cards_html}

## How entries are labelled

Each tool-by-measure entry has one state. Every state other than `checked-agrees` carries a reason, shown wherever the entry is shown. The full definitions, the comparison rules and the fixture list are on [How entries are labelled](method.html).

{table(['State', 'Meaning'], [[state_tag(k) + ' ' + code(k), STATE_DEF[k]] for k in STATE_SYM])}

A tool marked *documented-only* was never run: its entries come from its documentation and are always `reported-in-docs`. A *reference value* is the value of the published definition, evaluated independently of every tool compared (see [How entries are labelled](method.html#reference-value)).
"""
    files["index.md"] = page({"title": "Home", "layout": "default", "nav_order": 1, "permalink": "/"}, body)

    # data page
    schema_rows = [[code("data/" + n), s] for n, s in [
        ("tools.json", "Tools: id, name, language, version tested, license, homepage, citation key, role, how it was run."),
        ("measures.json", "Measures: id, name, original family, concept, variant label, definition, citation keys."),
        ("concepts.json", "Concepts: id, name, family, subfamily, definition, citation keys. A concept groups measures that are the same quantity, alternative algorithms, options or one tool's function for it."),
        ("aliases.csv", "Old measure id to concept page and anchor (generated). Join key: `measure`."),
        ("capabilities.csv", "Measure by tool: state, API names, comparison counts. Join keys: `measure`, `tool`."),
        ("reasons.json", "Per measure and tool, for every entry whose state is not `checked-agrees`: plain-words reason, short form, structured fields (convention, relation, inputs, tolerance, finding, source) and `reason_incomplete`."),
        ("fixtures.json", "The input graphs used for the comparisons: id, tier, kind, size, direction, weights, source and citation key."),
        ("conventions.json", "Per measure, variant and tool: scope, call, outcome, differing conditions, normalization/direction/weights/self-loops/ties/defaults dimensions, note, tolerance."),
        ("findings.json", "Bugs, disagreements and limitations in other tools."),
        ("benchmarks/results.csv", "Timing and memory of other tools (headline runs); method in `data/benchmarks/method.md`."),
        ("benchmarks/hosted.csv", "The same measures run on GitHub-hosted runners (suite `hosted`); hardware in `benchmarks/hosted-environments.json`."),
        ("definitions/<family-slug>.json", "Precise definitions per concept of a family: notation, LaTeX formulas, variants per measure, edge cases (what the published definition gives and what each tool does). Cases are defined in `definitions/_vocabulary.json`; procedure in `data/definitions/README.md`."),
        ("references.bib", "BibTeX for every cited key.")]]
    body = "# Data and schemas\n\n" + table(["File", "Content"], schema_rows) + """

Each JSON or CSV file has a JSON Schema in `data/schema/` (draft 2020-12). `python3 scripts/build.py --check` validates all of them with a stdlib-only validator and checks the joins below, that every measure appears in exactly one concept page, and that every alias resolves to an anchor on its page. How measures were grouped into concepts and concepts into subfamilies is written down in [`data/README.md`](https://github.com/knapply/net-oracles/blob/main/data/README.md).

## Joins

- `measures.json[].concept` is `concepts.json[].id`; `aliases.csv.measure` is `measures.json[].id` and `aliases.csv.concept` is `concepts.json[].id`. The page of a measure is `aliases.csv.page` plus `#` plus `aliases.csv.anchor`.
- `capabilities.csv.measure` is `measures.json[].id`; `capabilities.csv.tool` is `tools.json[].id`.
- `reasons.json[].measure`, `.tool` use the same ids; every row of `capabilities.csv` whose state is not `checked-agrees` has exactly one record there, and no other row has one.
- `fixtures.json[].id` are the fixture names used in `conventions.json` (`differs_on_inputs`, `no_value_on_inputs`) and in `reasons.json[].inputs`.
- `conventions.json[].measure`, `.tool` use the same ids. `.variant` names one parameterization of the measure (for example normalized or weighted).
- `findings.json[].tool`, `.measure` (nullable) use the same ids.
- `benchmarks/results.csv.tool` is `tools.json[].id`.
- Citation keys in `tools.json[].citation_key`, `measures.json[].references`, `concepts.json[].references`, `findings.json[].references` and `conventions.json[].reference` are keys of `references.bib`.

## Reasons

Every entry that is not `checked-agrees` has a reason in `reasons.json`. `build.py --check` fails if one is missing or lacks what its state requires. `reason_incomplete: true` marks the entries for which the sources do not state everything; `missing` says what is not known. The states, the comparison rules and the fixtures are defined on [How entries are labelled](method.html).

## Conventions record fields

`outcome` is `agrees` (values agreed on every compared input), `differs` (they differ under `differs_when`), `no-value-on-some-inputs` (the tool returns no value or an error under `undefined_when`), or `documented` (taken from documentation). `dimensions` lists which conventions are involved. `tolerance` is the absolute and relative tolerance used when comparing: integer outputs are compared exactly, floating-point outputs within the stated bound. The structural conditions are: `loops`, `multi_edges`, `directed`, `undirected`, `disconnected`, `not_strongly_connected`, `null_graph`, `one_node`, `two_nodes`, `edgeless`, `isolates`, `symmetric_nodes`, `negative_weights`, `zero_weights`, `integer_weights`, `fractional_weights`, `weighted`, `bipartite`, `onemode`, `unsorted_edges`, `no_two_paths`, `edge_case`.
"""
    files["data.md"] = page({"title": "Data and schemas", "layout": "default", "nav_order": 8}, body)

    # tools index + pages
    rows = []
    for t in tools:
        if t["role"] == "reference": continue
        cs = caps_by_t.get(t["id"], [])
        rows.append(["[%s](%s.html)" % (esc(t["name"]), t["id"]), esc(t["language"] or ""), esc(t["version_tested"]), esc(t["license"] or ""), t["role"], len(cs), sum(1 for c in cs if c["state"].startswith("checked")), len(fnd_by_t.get(t["id"], []))])
    body = "# Tools\n\n" + table(["Tool", "Language", "Version tested", "License", "Role", "Measures", "Checked", "Findings"], rows)
    files["tools/index.md"] = page({"title": "Tools", "layout": "default", "nav_order": 4, "has_children": "true", "permalink": "/tools/"}, body)
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
            body += "\n## Coverage\n\n" + table(["State", "Measures"], [[state_tag(k, "../"), cnt[k]] for k in STATE_SYM if cnt[k]]) + "\n"
            body += "\nEvery state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).\n"
            body += "\n## Measures\n\n" + table(["Family", "Subfamily", "Concept", "Measure (variant)", "State", "API names", "Why, if not agrees"], [
                [esc(cid_[mid[c["measure"]]["concept"]]["family"]), esc(cid_[mid[c["measure"]]["concept"]]["subfamily"]), "[%s](%s)" % (esc(cid_[mid[c["measure"]]["concept"]]["name"]), curl(cid_[mid[c["measure"]]["concept"]], "../")), mlink(c["measure"], "../", esc(mid[c["measure"]]["variant"])), state_tag(c["state"], "../"), code(c["api_names"]) if c["api_names"] else "",
                 why_cell(c["measure"], t["id"], "../") ] for c in cs]) + "\n"
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
    files["measures/index.md"] = page({"title": "Measures", "layout": "default", "nav_order": 5, "has_children": "true", "permalink": "/measures/"}, body)
    for fi, (f, cs) in enumerate(fam_concepts.items()):
        subs = collections.OrderedDict()
        for c in cs: subs.setdefault(c["subfamily"], []).append(c)
        nm = sum(len(mem[c["id"]]) for c in cs)
        body = "# %s\n\n%d measures in %d concepts and %d subfamilies. Each concept page has a section per measure (variant); the anchor of a section is the measure id (characters other than letters, digits, underscore, dot and hyphen become hyphens).\n" % (esc(f), nm, len(cs), len(subs))
        for sf, sc in subs.items():
            body += "\n## %s\n\n" % esc(sf)
            body += table(["Concept", "Measures", "Tools", "Formulas", "Definition"], [[
                "[%s](%s.html)" % (esc(c["name"]), c["id"]), len(mem[c["id"]]), len({r["tool"] for m in mem[c["id"]] for r in caps_by_m[m["id"]]}), {"complete": "written", "partial": "partly written", "name_only": "not yet written"}[defs_of[c["id"]]["status"]] if c["id"] in defs_of else "not yet written", esc(c["definition"] if len(c["definition"]) <= 160 else c["definition"][:157].rsplit(" ", 1)[0] + "...")] for c in sc]) + "\n"
        files["measures/%s/index.md" % fam_slug(f)] = page({"title": yq(f), "layout": "default", "parent": "Measures", "has_children": "true", "nav_order": fi + 1, "permalink": "/measures/%s/" % fam_slug(f)}, body)
    for c in concepts:
        ms_ = mem[c["id"]]
        dent = defs_of.get(c["id"])
        dr = render_definition(c, dent, ms_, tid, tool_order, caps_by_m, d["vocabulary"])
        body = "# %s {#concept-top}\n\nFamily: [%s](index.html). Subfamily: %s. Concept id: %s. %d measure%s.\n" % (
            esc(c["name"]), esc(c["family"]), esc(c["subfamily"]), code(c["id"]), len(ms_), "" if len(ms_) == 1 else "s")
        if dr["notation"]: body += "\n## Notation {#concept-notation}\n" + dr["notation"]
        body += "\n## Definition {#concept-definition}\n\n%s\n" % esc(c["definition"]) + dr["formulas"]
        if dr["variants"]: body += "\n## Variants {#concept-variants}\n" + dr["variants"]
        elif len(ms_) > 1:
            body += "\n## Variants {#concept-variants}\n\n" + table(["Variant", "Measure id", "Tools"], [
                ["[%s](#%s)" % (esc(m["variant"]), slug(m["id"])), code(m["id"]), len({r["tool"] for r in caps_by_m[m["id"]]})] for m in ms_]) + "\n"
        if dr["edge"]: body += "\n## Edge cases {#concept-edge-cases}\n" + dr["edge"]
        if c["references"]:
            body += "\n## References {#concept-references}\n\n" + ", ".join(cite(k, "../../") for k in c["references"]) + "\n"
        for m in ms_:
            cs_ = sorted(caps_by_m[m["id"]], key=lambda r: tool_order.index(r["tool"]))
            body += "\n## %s {#%s}\n\nMeasure id: %s. Original family: %s.\n" % (esc(m["variant"]), slug(m["id"]), code(m["id"]), esc(m["family"]))
            if m["name"] != m["variant"]: body += "\nName: %s.\n" % esc(m["name"])
            body += "\n**Definition.** %s\n" % esc(m["definition"])
            body += "\n**Implementations**\n\n" + table(["Tool", "State", "Why, if not agrees", "API names", "Source"], [
                ["[%s](../../tools/%s.html)" % (esc(tid[r["tool"]]["name"]), r["tool"]), state_tag(r["state"], "../../"), why_cell(m["id"], r["tool"], None) if (m["id"], r["tool"]) in rsn else "", code(r["api_names"]) if r["api_names"] else "", esc(r["source"])] for r in cs_]) + "\n"
            ws = [r for r in cs_ if (m["id"], r["tool"]) in rsn]
            if ws:
                body += "\n**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).\n\n"
                for r in ws:
                    z = rsn[(m["id"], r["tool"])]
                    body += '- <a id="%s"></a>**[%s](../../tools/%s.html)** %s %s' % (why_id(m["id"], r["tool"]), esc(tid[r["tool"]]["name"]), r["tool"], state_tag(r["state"], "../../"), esc(z["reason"]))
                    if z.get("findings"): body += " Findings: " + ", ".join("[%s](../../findings.html#%s)" % (f, f.lower()) for f in z["findings"]) + "."
                    if z["reason_incomplete"]: body += " **Reason incomplete:** " + esc(z["missing"])
                    body += "\n"
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
    body = "# Capability matrix\n\n" + legend_html() + "\n\nColumns are tool identifiers (see [Tools](tools/)). Rows are measures, grouped by family, subfamily and concept; the concept name links to its page and each variant links to its section. Every symbol is a link: hover for the reason, or follow it to the full reason on the measure's page (for a state other than checked, agrees) or to the definition of the state on [How entries are labelled](method.html) (for checked, agrees). Entries marked with a reason the sources only partly give say so in the detail.\n"
    cap = {(r["measure"], r["tool"]): r["state"] for r in d["capabilities"]}

    def cell_html(m_, t_, cap_):
        k = cap_.get((m_, t_))
        if not k: return ""
        z = rsn.get((m_, t_))
        if z is None: return state_badge(k, "", STATE_TXT[k] + ": agrees with the reference value on every compared input")
        tip = z["short"] + (" (reason incomplete)" if z["reason_incomplete"] else "")
        return '<a class="st st-g st-%s" href="%s#%s" title="%s" aria-label="%s: %s">%s</a>' % (STATE_CLS[k], curl(cid_[mid[m_]["concept"]], ""), why_id(m_, t_), esc_attr(tip), esc_attr(STATE_TXT[k]), esc_attr(z["short"]), STATE_SYM[k])
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
                    rows.append(["[%s](%s)" % (esc(c["name"]), curl(c, "")) if i == 0 else "", mlink(m["id"], "", esc(m["variant"]))] + [cell_html(m["id"], t, cap) for t in ts])
            body += "\n### %s\n\n%d measures in %d concepts.\n\n" % (esc(sf), len(ms_), len(sc))
            body += table(["Concept", "Variant"] + [t for t in ts], rows) + "\n"
    files["matrix.md"] = page({"title": "Capability matrix", "layout": "default", "nav_order": 2}, body)


    # method: how entries are labelled
    mtxt = pipe_tables_to_html(open(os.path.join(DATA, "method.md"), encoding="utf-8").read().strip())
    mtxt = re.sub(r"^# .*\n", "", mtxt)
    ncap = collections.Counter(r["state"] for r in d["capabilities"])
    nwhy = collections.Counter(r["why_not_run"] for r in d["reasons"] if r["state"] == "reported-in-docs")
    ninc = sum(1 for r in d["reasons"] if r["reason_incomplete"])
    sec = []
    def state_sec(k, text):
        sec.append("### %s {#state-%s}\n\n%s %s\n\n%s\n\nEntries with this state: **%d**.\n" % (STATE_TXT[k][0].upper() + STATE_TXT[k][1:], k, state_tag(k), code(k), text, ncap[k]))
    state_sec("checked-agrees", "The tool was run, and on **every** fixture that applies to the measure and that the tool accepts, its value equals the reference value within the tolerance recorded for the measure: exactly for integers, sets and discrete labels (partitions up to relabelling), within the absolute and relative tolerances for floating-point values, by seed or by distribution for random and approximate algorithms. The tool's default behaviour is compared as it is: **no convention is mapped for this state**, no input is left out because the tool disagrees, and no tolerance is widened to make the entry agree. Inputs the tool does not accept are not comparisons (see [the inputs](#inputs)). `comparisons_agreeing` counts the agreeing comparisons (variant by fixture) and `comparisons_differing` is 0. Agreement is a statement about the listed fixtures and the tool version tested, not a proof for all graphs.")
    state_sec("checked-convention", "The tool was run and its value differs from the reference value, beyond the tolerance, on at least one fixture it accepts, and the difference is a documented convention: the tool follows a different, defensible reading of the quantity (normalization, direction, weights, self-loops, multi-edges, ties, defaults, scaling, ordering, or the way an undefined value is encoded). Conventions are mapped before comparing **only for this state**: the reference value is recomputed with the tool's convention, and where such a mapping is recorded it is compared with the tool's values on exactly the inputs where the difference occurs, with its own tolerance; a mismatch there would show that the difference is not the named convention alone. The reason states which convention differs, what each side does, the exact relation between the tool's value and the reference value where the sources give it (for example a constant factor), the inputs, and the tolerance before and after mapping. `comparisons_differing` counts the differing comparisons.")
    state_sec("checked-defect", "The tool was run and on some input its value is wrong under the published definition: it contradicts the definition, as the direct evaluation shows, rather than reading it differently. The reason states what is wrong, on which inputs, the value observed against the value expected, and the tool version, and links the finding that records the observation and, where available, a minimal reproduction. Findings of kind *defect* are listed on the [findings page](findings.html); a finding recorded for an entry of another state is linked from that entry.")
    state_sec("checked-no-value", "The tool was run for the measure but gave no value on the compared inputs, so no comparison could be made: it raised an error, returned an undefined marker, does not support the type of input, did not finish within the time limit, or its run was declined. The reason states on which inputs and why, with the error text where the sources record it. A tool that gives no value on *some* inputs but values on others is not in this state: its entry is `checked-agrees` or `checked-convention` according to the comparisons made, and the inputs without value are listed in the reason of a `checked-convention` entry (as \"No value\") and in `data/conventions.json` (`no_value_on_inputs`).")
    state_sec("reported-in-docs", "The tool lists the capability in its documentation or public API, but it was **not run** for this measure, so nothing is stated about agreement. The reason says why it was not run and gives the documentation source. Three reasons occur: *not yet wired up* (%d entries: the tool was run in this survey on other measures, but no comparison against the reference value has been set up for this one), *documented-only tool* (%d entries: the tool is documented-only in this survey, so none of its measures was run), and *commercial, closed-source software* (%d entries: UCINET is proprietary Windows software that was never run here; it is never described as checked)." % (nwhy["not-yet-wired"], nwhy["documented-only-tool"], nwhy["commercial-closed-source"]))
    sec.append("### Blank\n\nA blank cell in the matrix, or an absent row in `data/capabilities.csv`, means the tool is not known to implement the measure. It says nothing about whether it does.\n")
    mtxt = mtxt.replace("{{STATE_SECTIONS}}", "\n".join(sec).strip())
    mtxt = mtxt.replace("only when the sources used for this survey do not say", "only when the sources used for this survey do not say")
    mtxt += "\n\n%d of the %d reasons are marked `reason_incomplete`.\n" % (ninc, len(d["reasons"]))
    fr = [[code(fx["name"]), fx["tier"], fx["nodes"] if fx["nodes"] is not None else "", fx["edges"] if fx["edges"] is not None else "", "directed" if fx["directed"] else "undirected", fx["weights"],
           esc(", ".join(fx["tags"])), esc(fx["description"]) + (" " + ", ".join(cite(k, "") for k in fx["references"]) if fx["references"] else "")] for fx in d["fixtures"]]
    ftxt = ("%d fixtures: %d in the small tier (run for every tool and every measure that applies), %d mid-size and %d large (run only for the pairs of tool and measure that can follow them). The tags are structural conditions computed from the graph; they are the conditions named in `differs_when`, `undefined_when` and the reasons, and are listed in [data.html](data.html). Node and edge counts are given where fixed by the generator; the edge count of the small tier counts rows of the edge list, including repeated edges and loops.\n\n"
            % (len(d["fixtures"]), sum(1 for x in d["fixtures"] if x["tier"] == "small"), sum(1 for x in d["fixtures"] if x["tier"] == "mid"), sum(1 for x in d["fixtures"] if x["tier"] == "large"))
            + table(["Fixture", "Tier", "Nodes", "Edges", "Direction", "Weights", "Tags", "Description"], fr))
    mtxt = mtxt.replace("{{FIXTURES}}", ftxt)
    def tclass(t):
        m_ = max(t["abs"], t["rel"])
        if m_ == 0: return 0
        return 1 if m_ <= 1e-12 else 2 if m_ <= 1e-9 else 3 if m_ <= 1e-6 else 4
    tnames = ["exact (abs 0, rel 0)", "floating point, both bounds at most 1e-12", "floating point, larger bound above 1e-12 up to 1e-9", "larger bound above 1e-9 up to 1e-6", "larger bound above 1e-6 (statistical comparisons)"]
    tc = collections.defaultdict(list)
    for c in d["conventions"]: tc[tclass(c["tolerance"])].append(c)
    trows = [[tnames[k], len(tc[k]), len({c["measure"] for c in tc[k]}), ("abs %g to %g, rel %g to %g" % (min(c["tolerance"]["abs"] for c in tc[k]), max(c["tolerance"]["abs"] for c in tc[k]), min(c["tolerance"]["rel"] for c in tc[k]), max(c["tolerance"]["rel"] for c in tc[k]))) if tc[k] else ""] for k in range(5)]
    mtxt = mtxt.replace("{{TOLERANCES}}", "Tolerances of the %d convention records, by size of the larger bound.\n\n" % len(d["conventions"]) + table(["Class", "Records", "Measures", "Range used"], trows))
    files["method.md"] = page({"title": yq("How entries are labelled"), "layout": "default", "nav_order": 3, "permalink": "/method.html"}, "# How entries are labelled\n\n" + mtxt)

    # findings
    body = "# Findings\n\nBugs, disagreements and limitations observed in other tools. `kind` is *defect* (wrong under the published definition), *convention* (differs by a convention) or *limitation* (refuses or cannot represent the input). `status` is *reproduced* (minimal reproduction recorded), *observed* (seen on a shared corpus of test graphs) or *reported* (public discussion, not re-measured). Versions are those tested; a finding may not hold in later versions.\n\n"
    body += table(["Id", "Tool", "Version", "Measure", "Kind", "Status", "Title"], [[
        "[%s](#%s)" % (f["id"], f["id"].lower()), esc(tid[f["tool"]]["name"]), esc(f["version"]), mlink(f["measure"], "", esc(mid[f["measure"]]["name"])) if f["measure"] else "", f["kind"], f["status"], esc(f["title"])] for f in d["findings"]]) + "\n"
    for f in d["findings"]:
        body += "\n## %s %s {#%s}\n\nTool: [%s](tools/%s.html) %s. Kind: %s. Status: %s.\n" % (f["id"], esc(f["title"]), f["id"].lower(), esc(tid[f["tool"]]["name"]), f["tool"], esc(f["version"]), f["kind"], f["status"])
        z = rsn.get((f["measure"], f["tool"])) if f["measure"] else None
        if f["measure"] and (f["measure"], f["tool"]) in cap:
            k = cap[(f["measure"], f["tool"])]
            why = (esc(z["short"]) + " [Full reason](%s#%s)." % (curl(cid_[mid[f["measure"]]["concept"]], ""), why_id(f["measure"], f["tool"]))) if z else "Agrees with the reference value on every compared input."
            body += "\n**Entry:** %s %s %s\n" % (mlink(f["measure"], "", esc(mid[f["measure"]]["name"])), state_tag(k), why)
        if f["observed"]: body += "\n**Observed:** %s\n" % esc(f["observed"])
        if f["expected"]: body += "\n**Expected:** %s\n" % esc(f["expected"])
        if f["reproduction"]:
            body += "\n**Reproduction:**\n\n```\n%s\n```\n" % f["reproduction"].replace("```", "'''")
        if f["evidence"]: body += "\n**Notes:** %s\n" % esc(f["evidence"])
        if f["references"]: body += "\nReferences: " + ", ".join(cite(k, "") for k in f["references"]) + "\n"
    files["findings.md"] = page({"title": "Findings", "layout": "default", "nav_order": 6}, body)

    # benchmarks
    method = pipe_tables_to_html(open(os.path.join(DATA, "benchmarks", "method.md"), encoding="utf-8").read().strip())
    method = re.sub(r"^# .*\n", "", method)
    body = "# Benchmarks\n\nTimings and memory of other tools only. The first tables are the headline runs (dedicated hardware, rows in `data/benchmarks/results.csv`); results from GitHub-hosted runners are in a separate section at the end and are never combined with them. Method:\n\n" + method.replace("\n#", "\n##") + "\n"
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
    # Rows measured on GitHub-hosted runners are a different dataset (shared, variable hardware): their own section and tables,
    # never combined with the headline rows above.
    H = d["hosted"]
    if H:
        body += "\n## Hosted-runner results\n\nMeasured by the `bench` workflow on GitHub-hosted runners with the shared runner in `bench/`. Hardware is shared and varies between runs, so compare tools within one run, not with the headline tables above. Raw rows: `data/benchmarks/hosted.csv`; hardware per run: `data/benchmarks/hosted-environments.json`.\n\n"
        body += table(["Tool", "Suite", "Date", "Runner CPU", "Cores offered", "Memory", "Tool version"], [[
            esc(tid[e["tool"]]["name"] if e["tool"] in tid else e["tool"]), esc(e["suite"]), esc(e["date"][:10]), esc(e["cpu"]), e["cores_offered"], esc(e["memory"]), esc(e.get("tool_version", ""))]
            for e in sorted(d["hosted_env"], key=lambda e: (e["tool"], e["suite"]))]) + "\n"
        hg = collections.defaultdict(list)
        for r in H: hg[(r["tool"], r["measure"])].append(r)
        rows = []
        for (t, me), rs in sorted(hg.items(), key=lambda kv: (kv[0][1].lower(), kv[0][0])):
            sec = [float(r["seconds"]) for r in rs if r["seconds"]]
            mb = [float(r["peak_megabytes"]) for r in rs if r["peak_megabytes"]]
            rows.append([mlink(me, "", esc(me)) if me in mid else esc(me), esc(tid[t]["name"]), len(rs), len(sec), "%.4g" % statistics.median(sec) if sec else "", "%.4g" % statistics.median(mb) if mb else ""])
        body += "\n### Median time per measure (hosted)\n\nMedian over the graphs on which the tool finished within the budget.\n\n" + table(["Measure", "Tool", "Graphs", "Finished", "Median seconds", "Median peak MB"], rows) + "\n"
    files["benchmarks.md"] = page({"title": "Benchmarks", "layout": "default", "nav_order": 7}, body)

    # references
    cited = collections.defaultdict(list)
    for t in tools:
        if t["citation_key"]: cited[t["citation_key"]].append("tool " + t["id"])
    for m in d["measures"]:
        for k in m["references"]: cited[k].append("measure " + m["id"])
    body = "# References\n\nEvery cited package and paper. Keys match `data/references.bib`.\n\n"
    for k in sorted(d["bib"]):
        body += '- <a id="%s"></a>`%s` %s\n' % (k, k, esc(cite_text(d["bib"][k])))
    files["references.md"] = page({"title": "References", "layout": "default", "nav_order": 9}, body)

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
  State vocabulary: reported-in-docs (listed in the tool's documentation or public API, not run); checked-agrees (run, agrees with an independent evaluation within tolerance); checked-convention (run, differs on some inputs by a documented convention); checked-defect (run, wrong under the published definition); checked-no-value (run, returns no value or an error on the compared inputs). Tools with role documented-only only have reported-in-docs. Precise definitions, the comparison rules (tolerances, exact for integers and sets, partitions up to relabelling, ties, sign of eigenvectors, seeds or distributions for random algorithms) and the fixture list are at method.html (How entries are labelled). checked-agrees means the tool equals the reference value on every fixture that applies and that the tool accepts, with no convention mapped; conventions are mapped only for checked-convention. A blank (absent row) means not known to implement it.
- data/reasons.json (data/schema/reasons.schema.json): one record per capabilities.csv row whose state is not checked-agrees (join: measure, tool). Fields: measure, tool, state, reason (plain words), short (one sentence), convention, relation, inputs, tolerance, finding, source, why_not_run (reported-in-docs only), reason_incomplete, missing.
- data/fixtures.json (data/schema/fixtures.schema.json): the input graphs of the comparisons (id, tier, kind, size, direction, weights, source, citation key).
- data/conventions.json (data/schema/conventions.schema.json): array of records per measure, variant and tool. Fields: measure, variant, manifest, tool, scope (any | directed | undirected), weights_required, call (how the tool was invoked), outcome (agrees | differs | no-value-on-some-inputs | documented), differs_when and undefined_when (structural conditions such as loops, multi_edges, directed, disconnected, ties), only_on, dimensions (normalization, direction, weights, self_loops, multi_edges, ties, defaults), note, tolerance {{abs, rel}} (0 means exact), optional differs_on_inputs, no_value_on_inputs, reference.
- data/findings.json (data/schema/findings.schema.json): array of findings. Fields: id, tool, version, measure (nullable), kind (defect | convention | limitation), status (reproduced | observed | reported), title, reproduction, observed, expected, evidence, references.
- data/benchmarks/results.csv (data/schema/benchmarks-results.schema.json): timing rows of other tools (headline runs). Columns: suite, graph, nodes, edges, measure, tool, tool_version, seconds (empty when over budget), peak_megabytes, threads, status. Method: data/benchmarks/method.md.
- data/benchmarks/hosted.csv (data/schema/benchmarks-hosted.schema.json): the same columns, suite always `hosted`, measured on GitHub-hosted runners; never combined with results.csv. data/benchmarks/hosted-environments.json (data/schema/benchmarks-hosted-environments.schema.json): one record per tool and suite with the runner hardware, date and run id.
- data/definitions/<family-slug>.json (data/schema/definitions.schema.json): one file per family with the precise definitions of its concepts, keyed by concept id. Per concept: status (complete | partial | name_only), note, notation (symbol, meaning), formulas (name, latex, applies_to, where), variants (measure id -> what changes in the formula), edge_cases (case, definition_gives, tools: tool id -> status agrees | differs | no_value | documented | not_recorded, behaviour, source, optional measure and finding), references (BibTeX keys). The edge-case ids and their meaning are in data/definitions/_vocabulary.json. Procedure: data/definitions/README.md.
- data/references.bib: BibTeX for every key used above.

## Joins

reasons.measure/tool -> capabilities.measure/tool; measures.concept -> concepts.id; aliases.measure -> measures.id; aliases.concept -> concepts.id; capabilities.measure -> measures.id; capabilities.tool -> tools.id; conventions.measure/tool -> measures.id/tools.id; findings.tool -> tools.id; findings.measure -> measures.id (nullable); benchmarks.tool -> tools.id; every citation key -> references.bib; definitions concept key -> concepts.id, variants key -> measures.id, edge_cases[].case -> definitions/_vocabulary.json, edge_cases[].tools key -> tools.id. Page for a concept: measures/<family-slug>/<concept id>.html, where family-slug is the family name in lower case with runs of other characters replaced by a hyphen (see aliases.csv, column page). Each measure is a section of its concept page with anchor = the measure id (characters other than letters, digits, underscore, dot and hyphen become hyphens), so the page of a measure is aliases.page + "#" + aliases.anchor. Family overview: measures/<family-slug>/. Page for a tool: tools/<id>.html. To join a measure-level table to concepts: join on measure id with measures.json (concept, variant) and then with concepts.json (family, subfamily).

## Conventions of the data

Edge ends are called source and target. A reference value is the published definition evaluated independently. Every state other than checked-agrees has a reason in data/reasons.json. UCINET is documented-only: it was never run. Tool versions are those tested; findings may not hold in later versions.

## Oracle harness (harness/)

Reproduces every reference value. harness/manifest/<area>.yaml: one entry per measure variant, keyed by variant id, with params (the parameters every oracle computes with), applies_to, requires_weights and oracles (tool id -> oracle options, tolerance, documented differences). harness/fixtures/, fixtures-extra/ and derived/: the test graphs (edge lists with source and target columns). harness/golden/<tool>/: the values each tool returned per fixture and variant, with a VERSION file recording the tool version; golden-sized/ holds the larger graphs. harness/oracles/: one script per tool and area (Python *_oracle.py, R *.R), each tool used as a black box; harness/run_oracles.py reruns a script only when its inputs change (hashes in harness/golden/.hashes/). The manifest variant id is the measure id used in data/ where the measure was checked.

## Regenerate and validate

python3 scripts/build.py          # write pages
python3 scripts/build.py --check  # validate data against schemas, check that every measure appears in exactly one concept page and every alias resolves, and fail if pages are stale
"""


# ---------------------------------------------------------------- main
GENERATED_DIRS = ["tools", "measures"]
GENERATED_TOP = ["index.md", "method.md", "data.md", "matrix.md", "findings.md", "benchmarks.md", "references.md", "llms.txt", "data/aliases.csv"]


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
