/* Theme toggle and table enhancements. Everything degrades to plain tables without it. */
(function () {
  var root = document.documentElement;

  /* theme */
  var btn = document.getElementById("theme-toggle");
  function cur() { return root.getAttribute("data-theme") === "dark" ? "dark" : "light"; }
  if (btn) {
    btn.setAttribute("aria-pressed", cur() === "dark");
    btn.addEventListener("click", function () {
      var n = cur() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", n);
      btn.setAttribute("aria-pressed", n === "dark");
      try { localStorage.setItem("no-theme", n); } catch (e) {}
    });
  }
  try {
    matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
      var s = null;
      try { s = localStorage.getItem("no-theme"); } catch (x) {}
      if (!s) { root.setAttribute("data-theme", e.matches ? "dark" : "light"); if (btn) btn.setAttribute("aria-pressed", e.matches); }
    });
  } catch (e) {}

  /* state badges */
  var GLYPH = { "✓": ["ok", "checked, agrees"], "≠": ["conv", "checked, differs by convention"], "✗": ["defect", "checked, defect"],
                "∅": ["nov", "checked, no value on some inputs"], "·": ["docs", "reported in docs"] };
  var WORD = { agrees: "ok", differs: "conv", convention: "conv", defect: "defect", limitation: "nov", "no-value-on-some-inputs": "nov",
               documented: "docs", "documented-only": "docs", reported: "docs", observed: "docs", reproduced: "info", checked: "ok" };
  var WORD_COLS = { kind: 1, status: 1, role: 1, outcome: 1 };

  function badge(cls, shape, glyph, text, label) {
    var s = document.createElement("span");
    s.className = "st st-" + cls + " st-" + shape;
    if (shape === "g") { s.textContent = glyph; s.setAttribute("role", "img"); s.setAttribute("aria-label", label); s.title = label; }
    else if (shape === "t") { var g = document.createElement("span"); g.className = "g"; g.setAttribute("aria-hidden", "true"); g.textContent = glyph; s.appendChild(g); s.appendChild(document.createTextNode(text)); }
    else s.textContent = text;
    return s;
  }

  var tables = document.querySelectorAll(".table-wrapper > table");
  Array.prototype.forEach.call(tables, function (tb) {
    var wrap = tb.parentNode, heads = Array.prototype.map.call(tb.querySelectorAll("thead th"), function (h) { return h.textContent.trim(); });
    var rows = tb.querySelectorAll("tbody tr");
    var matrix = heads[0] === "Concept" && heads[1] === "Variant" && heads.length > 4;
    if (matrix) tb.classList.add("matrix");
    if (rows.length > 14) wrap.classList.add("is-long");
    wrap.tabIndex = 0; wrap.setAttribute("role", "region"); wrap.setAttribute("aria-label", "Table: " + (heads.slice(0, 3).join(", ")) + (heads.length > 3 ? ", ..." : ""));

    if (matrix) Array.prototype.forEach.call(tb.querySelectorAll("thead th"), function (th, i) {
      if (i > 1) { var v = document.createElement("span"); v.className = "v"; v.textContent = th.textContent; th.textContent = ""; th.appendChild(v); }
    });

    Array.prototype.forEach.call(rows, function (tr) {
      Array.prototype.forEach.call(tr.cells, function (td, i) {
        if (td.children.length) return;
        var t = td.textContent.trim(), m = t.match(/^([✓≠✗∅·])(?:\s+(.+))?$/);
        if (m) {
          var info = GLYPH[m[1]];
          td.textContent = "";
          td.appendChild(m[2] ? badge(info[0], "t", m[1], m[2], info[1]) : badge(info[0], "g", m[1], "", info[1]));
        } else if (WORD_COLS[(heads[i] || "").toLowerCase()] && WORD[t]) {
          td.textContent = ""; td.appendChild(badge(WORD[t], "w", "", t));
        }
      });
    });

    if (matrix) {
      var last = null;
      tb.addEventListener("mouseover", function (e) {
        var td = e.target.closest ? e.target.closest("td") : null;
        if (!td || td === last) return;
        last = td;
        Array.prototype.forEach.call(tb.querySelectorAll(".hl"), function (n) { n.classList.remove("hl"); });
        var i = td.cellIndex;
        if (i < 2) return;
        tb.querySelector("thead tr").cells[i].classList.add("hl");
        Array.prototype.forEach.call(tb.rows, function (r) { if (r.cells[i] && r.parentNode.tagName === "TBODY") r.cells[i].classList.add("hl"); });
      });
      tb.addEventListener("mouseleave", function () { last = null; Array.prototype.forEach.call(tb.querySelectorAll(".hl"), function (n) { n.classList.remove("hl"); }); });
    }
  });
})();
