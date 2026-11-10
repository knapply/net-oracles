/* Home page header: a slowly drifting network of three communities. No libraries.
   Static under prefers-reduced-motion, paused when scrolled away or the tab is hidden. */
(function () {
  var c = document.getElementById("hero-graph");
  if (!c || !c.getContext) return;
  var x = c.getContext("2d"), mq = matchMedia("(prefers-reduced-motion: reduce)");
  var COL = ["#8da2ff", "#5ee0d0", "#ffb454"], W = 0, H = 0, nodes = [], edges = [], sig = [];
  var raf = 0, onscreen = true, t0 = 0, nextSig = 0;

  function rng(s) { return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }

  function build() {
    var r = c.getBoundingClientRect(), dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = r.width; H = r.height;
    if (!W || !H) return;
    c.width = Math.round(W * dpr); c.height = Math.round(H * dpr);
    x.setTransform(dpr, 0, 0, dpr, 0, 0);
    var R = rng(11), n = Math.max(18, Math.min(60, Math.round(W * H / 6500))), k = 3, cs = [], i, j;
    for (i = 0; i < k; i++) cs.push({ x: W * (0.5 + 0.5 * (i + 0.5) / k), y: H * (0.28 + 0.46 * R()), s: Math.min(W, H) * 0.3 });
    nodes = []; edges = []; sig = [];
    for (i = 0; i < n; i++) {
      var g = i % k, a = cs[g];
      nodes.push({ g: g, hx: a.x + (R() + R() - 1) * a.s * 1.3, hy: a.y + (R() + R() - 1) * a.s, ax: 4 + R() * 9, ay: 4 + R() * 9,
        w1: 0.25 + R() * 0.35, w2: 0.2 + R() * 0.35, p1: R() * 6.28, p2: R() * 6.28, d: 0, x: 0, y: 0 });
    }
    var L = Math.max(90, Math.min(150, Math.sqrt(W * H / n) * 1.5));
    for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) {
      var dx = nodes[i].hx - nodes[j].hx, dy = nodes[i].hy - nodes[j].hy, d = Math.sqrt(dx * dx + dy * dy);
      if (d < L && R() < (nodes[i].g === nodes[j].g ? 0.6 : 0.1)) { edges.push([i, j]); nodes[i].d++; nodes[j].d++; }
    }
    pos(0);
  }

  function pos(t) {
    for (var i = 0; i < nodes.length; i++) {
      var o = nodes[i];
      o.x = o.hx + Math.sin(t * o.w1 + o.p1) * o.ax;
      o.y = o.hy + Math.cos(t * o.w2 + o.p2) * o.ay;
    }
  }

  function draw(t) {
    x.clearRect(0, 0, W, H);
    var i, o, e, a, b;
    x.lineWidth = 1;
    for (i = 0; i < edges.length; i++) {
      e = edges[i]; a = nodes[e[0]]; b = nodes[e[1]];
      x.strokeStyle = a.g === b.g ? "rgba(150,170,255,.32)" : "rgba(255,255,255,.14)";
      x.beginPath(); x.moveTo(a.x, a.y); x.lineTo(b.x, b.y); x.stroke();
    }
    for (i = sig.length - 1; i >= 0; i--) {
      var s = sig[i], f = (t - s.t) / 1.6;
      if (f >= 1) { sig.splice(i, 1); continue; }
      a = nodes[s.e[0]]; b = nodes[s.e[1]];
      if (s.r) { o = a; a = b; b = o; }
      x.fillStyle = "rgba(255,255,255," + (0.9 * Math.sin(f * Math.PI)).toFixed(2) + ")";
      x.beginPath(); x.arc(a.x + (b.x - a.x) * f, a.y + (b.y - a.y) * f, 2.2, 0, 6.283); x.fill();
    }
    for (i = 0; i < nodes.length; i++) {
      o = nodes[i];
      var r = 2 + Math.sqrt(o.d) * 1.1;
      x.fillStyle = COL[o.g];
      if (o.d > 3) { x.globalAlpha = 0.18; x.beginPath(); x.arc(o.x, o.y, r + 5, 0, 6.283); x.fill(); x.globalAlpha = 1; }
      x.beginPath(); x.arc(o.x, o.y, r, 0, 6.283); x.fill();
    }
  }

  function frame(ms) {
    var t = ms / 1000;
    if (!t0) t0 = t;
    t -= t0;
    pos(t);
    if (t > nextSig && edges.length) { sig.push({ e: edges[Math.floor(Math.random() * edges.length)], t: t, r: Math.random() < 0.5 }); nextSig = t + 0.5 + Math.random(); }
    draw(t);
    raf = requestAnimationFrame(frame);
  }

  function update() {
    var go = onscreen && !document.hidden && !mq.matches;
    if (go && !raf) { t0 = 0; raf = requestAnimationFrame(frame); }
    else if (!go) { if (raf) { cancelAnimationFrame(raf); raf = 0; } if (mq.matches) { pos(0); draw(0); } }
  }

  var tm;
  function resize() { clearTimeout(tm); tm = setTimeout(function () { build(); if (!raf) draw(0); }, 120); }

  build(); draw(0);
  if (window.ResizeObserver) new ResizeObserver(resize).observe(c); else addEventListener("resize", resize);
  if (window.IntersectionObserver) new IntersectionObserver(function (en) { onscreen = en[0].isIntersecting; update(); }).observe(c);
  document.addEventListener("visibilitychange", update);
  (mq.addEventListener ? mq.addEventListener("change", update) : mq.addListener(update));
  update();
})();
