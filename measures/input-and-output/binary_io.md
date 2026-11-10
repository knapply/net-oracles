---
title: "Binary and serialization formats"
layout: default
parent: "Input and output"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Binary and serialization formats {#concept-top}

Family: [Input and output](index.html). Subfamily: Binary and serialization formats. Concept id: `binary_io`. 4 measures.

## Definition {#concept-definition}

Binary and serialization formats. Entries grouped here: GRAPHTOOLBINARY read and write; NETWORKITBINARY read and write; PICKLE read and write; THRILLGRAPHBINARY read and write.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#io_graphtoolbinary">GRAPHTOOLBINARY read and write</a></td><td><code>io_graphtoolbinary</code></td><td>1</td></tr><tr><td><a href="#io_networkitbinary">NETWORKITBINARY read and write</a></td><td><code>io_networkitbinary</code></td><td>1</td></tr><tr><td><a href="#io_pickle">PICKLE read and write</a></td><td><code>io_pickle</code></td><td>1</td></tr><tr><td><a href="#io_thrillgraphbinary">THRILLGRAPHBINARY read and write</a></td><td><code>io_thrillgraphbinary</code></td><td>1</td></tr></tbody></table></div>

## GRAPHTOOLBINARY read and write {#io_graphtoolbinary}

Measure id: `io_graphtoolbinary`. Original family: Input and output.

**Definition.** GRAPHTOOLBINARY read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_graphtoolbinary-networkit">details</a></td><td><code>GraphToolBinaryReader; GraphToolBinaryWriter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_graphtoolbinary-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: GraphToolBinaryReader; GraphToolBinaryWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## NETWORKITBINARY read and write {#io_networkitbinary}

Measure id: `io_networkitbinary`. Original family: Input and output.

**Definition.** NETWORKITBINARY read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_networkitbinary-networkit">details</a></td><td><code>NetworkitBinaryReader; NetworkitBinaryWriter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_networkitbinary-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: NetworkitBinaryReader; NetworkitBinaryWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## PICKLE read and write {#io_pickle}

Measure id: `io_pickle`. Original family: Input and output.

**Definition.** PICKLE read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_pickle-pyigraph">details</a></td><td><code>Read_Pickle; Read_Picklez; write_pickle; write_picklez</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_pickle-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Read\_Pickle; Read\_Picklez; write\_pickle; write\_picklez.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## THRILLGRAPHBINARY read and write {#io_thrillgraphbinary}

Measure id: `io_thrillgraphbinary`. Original family: Input and output.

**Definition.** THRILLGRAPHBINARY read and write.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-io_thrillgraphbinary-networkit">details</a></td><td><code>ThrillGraphBinaryReader; ThrillGraphBinaryWriter</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-io_thrillgraphbinary-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ThrillGraphBinaryReader; ThrillGraphBinaryWriter.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
