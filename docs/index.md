# Overclaim

**An ontology of epistemic-overclaim failure modes:** named codes for the ways
confident language outruns its evidence, in LLM and human prose.

Overclaim is an *agent-facing domain*. Its primary consumer is a model, not a
reader. The site serves a rubric you fetch and apply to a piece of text. It does
not judge whether a claim is true; it judges whether the confidence is earned,
whether claims are framed honestly, and whether stated certainty matches the
evidence shown.

## Use it

Pick the rubric matching your text's genre, paste it into a context window above
the subject text, and apply it:

```text
Fetch https://overclaim-org.github.io/rubric/analytical.md
Paste it above the text you want checked.
The model returns: per-claim findings, cleared hedges, and one aggregated decision
(AUTHORIZE < CLARIFY < CONSTRAIN < REVISE < BLOCK).
```

Or pull the anchor file first and let the agent choose: [**`/llms.txt`**](/llms.txt).

## The rubrics

Severity is scored relative to the declared frame, so the same line is a defect in
an analytical memo and legitimate framing in sales copy.

| Genre | For |
|-------|-----|
| [analytical](/rubric/analytical.md) | memos, reports, design docs, reviews |
| [advocacy](/rubric/advocacy.md) | proposals, opinion pieces, making a case |
| [sales](/rubric/sales.md) | pitches, landing pages, outbound |
| [status](/rubric/status.md) | standups, updates, exec replies |
| [persuasion](/rubric/persuasion.md) | essays, talks, internal selling |

## The source of truth

The YAML packs are the source of truth; the LLM is the detector; the renderer is a
build step that compiles packs into the rubric and never reads subject text. The
raw packs are served verbatim for callers that want to compile their own rubric or
wire the codes into an eval harness:

- [`/packs/core.yaml`](/packs/core.yaml) , epistemic-overclaim core
- [`/packs/substantiation.yaml`](/packs/substantiation.yaml) , the proof-bar axis
- [`/packs/grounding.yaml`](/packs/grounding.yaml) , reasoning-environment warning lights
- [`/packs/management.yaml`](/packs/management.yaml) , commitment-without-mechanism

Browse every code in the [code catalog](codes.md), or read the [design](design.md)
for why the ontology is the asset and how the frame gate works.

## Status

Draft, v1: 39 codes across four packs (core, substantiation, grounding,
management). The engineering, sales, and marketing packs are deferred to v1.x
until they clear the contribution rule through real use. Ontology content is CC0;
code is MIT. The grounding pack is distilled from WillowEmberly / Negentropy
(OCAP, CC0).
