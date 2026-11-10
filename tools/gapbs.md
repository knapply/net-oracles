---
title: "GAP Benchmark Suite"
layout: default
parent: Tools
---

{% raw %}

# GAP Benchmark Suite

<div class="table-wrapper"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody><tr><td>Identifier</td><td><code>gapbs</code></td></tr><tr><td>Language</td><td>C++</td></tr><tr><td>Version tested</td><td>941462c7c42e</td></tr><tr><td>License</td><td>BSD-3-Clause</td></tr><tr><td>Homepage</td><td><https://github.com/sbeamer/gapbs></td></tr><tr><td>Role</td><td>benchmarked-only</td></tr><tr><td>Citation</td><td><a href="../references.html#beamer2015gap">beamer2015gap</a></td></tr></tbody></table></div>

## How it was run

Compiled reference kernels run with the thread counts listed in the benchmark data.

## Findings

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../findings.html#f088">F088</a></td><td>convention</td><td>Rank held by dangling vertices is not passed on</td></tr><tr><td><a href="../findings.html#f089">F089</a></td><td>convention</td><td>The BC verifier uses a float-epsilon tolerance against its own float accumulation</td></tr></tbody></table></div>
{% endraw %}
