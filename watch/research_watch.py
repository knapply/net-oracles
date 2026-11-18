#!/usr/bin/env python3
"""Weekly research watch: new network and graph papers, and new releases of
the surveyed tools.

Sources: the arXiv API (categories and terms in config.json), OpenAlex (the
journals in config.json) and GitHub releases. Each paper is scored against
the topic keywords and the signal phrases in config.json; papers at or above
min_score are written to research/YYYY-MM-DD.md, newest digest first in
research/index.md. Seen identifiers live in watch/state.json so a paper is
listed once.

Usage:
    python3 watch/research_watch.py [--days N] [--out research] [--issue FILE]
    python3 watch/research_watch.py --offline FILE   # score a saved JSON list
Standard library only.
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
UA = "net-oracles-research-watch (https://github.com/knapply/net-oracles)"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def get(url, headers=None, tries=4):
    h = {"User-Agent": UA}
    h.update(headers or {})
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if i == tries - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if i == tries - 1:
                raise
        time.sleep(5 * (i + 1))
    return None


def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


# ---------- sources ----------

def arxiv(cfg, since):
    out, start = [], 0
    while start < cfg["max_results"]:
        q = urllib.parse.urlencode({
            "search_query": cfg["query"], "sortBy": "submittedDate",
            "sortOrder": "descending", "start": start, "max_results": cfg["page_size"]})
        body = get("https://export.arxiv.org/api/query?" + q)
        if not body:
            break
        entries = ET.fromstring(body).findall(ATOM + "entry")
        if not entries:
            break
        older = False
        for e in entries:
            published = e.findtext(ATOM + "published", "")[:10]
            if published < since:
                older = True
                continue
            aid = e.findtext(ATOM + "id", "").rsplit("/abs/", 1)[-1]
            aid = re.sub(r"v\d+$", "", aid)
            prim = e.find(ARXIV_NS + "primary_category")
            out.append({
                "id": "arxiv:" + aid,
                "title": clean(e.findtext(ATOM + "title")),
                "abstract": clean(e.findtext(ATOM + "summary")),
                "comment": clean(e.findtext(ARXIV_NS + "comment")),
                "authors": [clean(a.findtext(ATOM + "name")) for a in e.findall(ATOM + "author")],
                "date": published,
                "venue": "arXiv " + (prim.get("term") if prim is not None else ""),
                "url": "https://arxiv.org/abs/" + aid,
            })
        if older:
            break
        start += cfg["page_size"]
        time.sleep(3)  # arXiv asks for at most one request every 3 seconds
    return out


def openalex_abstract(inv):
    if not inv:
        return ""
    pos = {}
    for word, idx in inv.items():
        for i in idx:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def openalex(sources, since, mailto):
    out = []
    for src in sources:
        cursor = "*"
        while cursor:
            q = urllib.parse.urlencode({
                "filter": "primary_location.source.issn:%s,from_publication_date:%s,type:article"
                          % (src["issn"], since),
                "per-page": 100, "cursor": cursor, "mailto": mailto})
            body = get("https://api.openalex.org/works?" + q)
            if not body:
                break
            data = json.loads(body)
            for w in data.get("results", []):
                doi = (w.get("doi") or "").replace("https://doi.org/", "")
                out.append({
                    "id": "doi:" + doi.lower() if doi else w["id"],
                    "title": clean(w.get("title")),
                    "abstract": clean(openalex_abstract(w.get("abstract_inverted_index"))),
                    "comment": "",
                    "authors": [clean(a["author"].get("display_name")) for a in w.get("authorships", [])],
                    "date": w.get("publication_date") or "",
                    "venue": src["name"],
                    "url": "https://doi.org/" + doi if doi else w["id"],
                })
            cursor = data.get("meta", {}).get("next_cursor")
            time.sleep(0.2)
    return out


def releases(repos, since, token):
    out = []
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    for repo in repos:
        body = get("https://api.github.com/repos/%s/releases?per_page=10" % repo, headers)
        if body:
            for r in json.loads(body):
                day = (r.get("published_at") or "")[:10]
                if day >= since and not r.get("draft"):
                    out.append({"repo": repo, "tag": r.get("tag_name"), "date": day,
                                "prerelease": bool(r.get("prerelease")), "url": r.get("html_url")})
            continue
        # projects that tag without publishing releases
        body = get("https://api.github.com/repos/%s/tags?per_page=5" % repo, headers)
        if body:
            for t in json.loads(body)[:1]:
                out.append({"repo": repo, "tag": t["name"], "date": "", "prerelease": False,
                            "url": "https://github.com/%s/releases/tag/%s" % (repo, t["name"]),
                            "tag_only": True})
    return out


# ---------- scoring ----------

def score(paper, cfg):
    text = " ".join([paper["title"], paper["title"], paper["abstract"], paper["comment"]]).lower()
    topics, total = [], 0
    for topic, words in cfg["topics"].items():
        hits = sorted({w for w in words if w in text})
        if hits:
            topics.append(topic)
            total += 1 + len(hits)
    if not topics:
        return 0, [], []
    flags = []
    for sig, words in cfg["signals"].items():
        if any(w in text for w in words):
            flags.append(sig)
            total += 1
    if re.search(r"github\.com/[\w.-]+/[\w.-]+", text):
        total += 1
    return total, topics, flags


def code_links(paper):
    return sorted(set(re.findall(r"https?://(?:github|gitlab)\.com/[\w.-]+/[\w.-]+",
                                 paper["abstract"] + " " + paper["comment"])))


# ---------- output ----------

def md_escape(s):
    return s.replace("|", "\\|").replace("{", "&#123;").replace("}", "&#125;")


def render(day, since, papers, rels, counts):
    by_topic = {}
    for p in papers:
        by_topic.setdefault(p["topics"][0], []).append(p)
    lines = [
        "---", "title: %s" % day, "layout: default", "parent: Research watch",
        "nav_exclude: true", "---", "", "# Research watch, %s" % day, "",
        "New papers since %s from arXiv and %d journals, scored by topic and by whether they "
        "propose a method, release code, or report a pitfall in existing practice; plus new "
        "releases of the surveyed tools. Scanned: %s. Listed: %d papers, %d releases."
        % (since, counts["journals"], ", ".join("%s %d" % kv for kv in counts["scanned"].items()),
           len(papers), len(rels)), ""]
    if rels:
        lines += ["## Tool releases", "", "| Tool | Release | Date |", "|---|---|---|"]
        for r in sorted(rels, key=lambda r: r["repo"]):
            tag = r["tag"] + (" (pre-release)" if r["prerelease"] else "")
            lines.append("| %s | [%s](%s) | %s |" % (r["repo"], md_escape(tag), r["url"],
                                                    r["date"] or "latest tag"))
        lines.append("")
    lines += ["## Papers", ""]
    for topic in sorted(by_topic, key=lambda t: -max(p["score"] for p in by_topic[t])):
        lines += ["### %s" % topic.capitalize(), ""]
        for p in sorted(by_topic[topic], key=lambda p: (-p["score"], p["title"])):
            authors = ", ".join(p["authors"][:4]) + (" et al." if len(p["authors"]) > 4 else "")
            tags = ", ".join(p["topics"] + ["**%s**" % f for f in p["flags"]])
            lines.append("- [%s](%s). %s. *%s*, %s. Score %d; %s." % (
                md_escape(p["title"]), p["url"], md_escape(authors).rstrip("."), md_escape(p["venue"]),
                p["date"], p["score"], tags))
            for link in p["code"]:
                lines.append("  Code: <%s>" % link)
        lines.append("")
    return "\n".join(lines) + "\n"


def write_index(out_dir):
    days = sorted((f[:-3] for f in os.listdir(out_dir)
                   if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", f)), reverse=True)
    lines = ["---", "title: Research watch", "layout: default", "nav_order: 11",
             "has_children: true", "---", "", "# Research watch", "",
             "A weekly scan of new network and graph research (arXiv and network-science, "
             "statistics and algorithms journals) and of new releases of the tools surveyed "
             "here. Papers are scored by topic and flagged when they propose a method, "
             "release code, or report a pitfall in common practice. The scan is automated "
             "and unreviewed: a listing is a pointer, not an endorsement. Sources, topics and "
             "weights are in [`watch/config.json`](https://github.com/knapply/net-oracles/"
             "blob/main/watch/config.json).", ""]
    lines += ["- [%s](%s.html)" % (d, d) for d in days]
    with open(os.path.join(out_dir, "index.md"), "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=8)
    ap.add_argument("--out", default=os.path.join(ROOT, "research"))
    ap.add_argument("--issue", help="write a short issue body here")
    ap.add_argument("--offline", help="score papers from a JSON list instead of fetching")
    a = ap.parse_args()

    cfg = json.load(open(os.path.join(HERE, "config.json")))
    state_path = os.path.join(HERE, "state.json")
    state = json.load(open(state_path)) if os.path.exists(state_path) else {"seen": {}}
    today = dt.date.today()
    since = (today - dt.timedelta(days=a.days)).isoformat()

    counts = {"journals": len(cfg["openalex_sources"]), "scanned": {}}
    if a.offline:
        papers, rels = json.load(open(a.offline)), []
        counts["scanned"]["offline"] = len(papers)
    else:
        papers = arxiv(cfg["arxiv"], since)
        counts["scanned"]["arXiv"] = len(papers)
        j = openalex(cfg["openalex_sources"], since, os.environ.get("OPENALEX_MAILTO", ""))
        counts["scanned"]["journals"] = len(j)
        papers += j
        rels = [r for r in releases(cfg["releases"], since, os.environ.get("GITHUB_TOKEN"))
                if ("release:%s@%s" % (r["repo"], r["tag"])) not in state["seen"]]

    kept, ids = [], set()
    for p in papers:
        if p["id"] in state["seen"] or p["id"] in ids or not p["title"]:
            continue
        ids.add(p["id"])
        s, topics, flags = score(p, cfg)
        if s >= cfg["min_score"]:
            p.update(score=s, topics=topics, flags=flags, code=code_links(p))
            kept.append(p)

    if not kept and not rels:
        print("nothing new since", since)
        return 0

    os.makedirs(a.out, exist_ok=True)
    day = today.isoformat()
    with open(os.path.join(a.out, day + ".md"), "w") as f:
        f.write(render(day, since, kept, rels, counts))
    write_index(a.out)

    stamp = day
    for p in kept:
        state["seen"][p["id"]] = stamp
    for r in rels:
        state["seen"]["release:%s@%s" % (r["repo"], r["tag"])] = stamp
    cutoff = (today - dt.timedelta(days=400)).isoformat()
    state["seen"] = {k: v for k, v in sorted(state["seen"].items()) if v >= cutoff}
    with open(state_path, "w") as f:
        json.dump(state, f, indent=0, sort_keys=True)
        f.write("\n")

    if a.issue:
        top = sorted(kept, key=lambda p: -p["score"])[:cfg["issue_top"]]
        body = ["Weekly research watch for %s: %d papers, %d tool releases." % (day, len(kept), len(rels)),
                "", "Full digest: https://knapply.github.io/net-oracles/research/%s.html" % day, ""]
        if rels:
            body += ["**Releases:** " + ", ".join("%s %s" % (r["repo"], r["tag"]) for r in rels), ""]
        body += ["**Top papers**", ""]
        body += ["- [ ] [%s](%s) (%s; score %d%s)" % (
            p["title"], p["url"], ", ".join(p["topics"]), p["score"],
            "; " + ", ".join(p["flags"]) if p["flags"] else "") for p in top]
        with open(a.issue, "w") as f:
            f.write("\n".join(body) + "\n")
    print("listed %d papers and %d releases in %s" % (len(kept), len(rels), day))
    return 0


if __name__ == "__main__":
    sys.exit(main())
