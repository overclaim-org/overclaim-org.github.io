# overclaim

An ontology of epistemic-overclaim failure modes: named codes for the ways
confident language outruns its evidence, in LLM and human prose. Published at
**[overclaim.org](https://overclaim.org)**.

This is an *agent-facing domain*. The primary consumer is a model: the site serves
a rubric an LLM fetches and applies to a piece of text, judging whether confidence
is earned rather than whether a claim is true.

## How it works

- **The YAML packs are the source of truth.** `ontology/*.yaml` defines the codes.
- **The LLM is the detector.** There is no keyword engine. `ontology/render/rubric.py`
  compiles the packs into a paste-ready markdown rubric and never reads subject text.
- **The site is the delivery.** `build.py` renders the rubric per genre and serves
  it, plus the raw packs and an `llms.txt` anchor, as static files.

```bash
# Render a rubric locally for one frame
python ontology/render/rubric.py --genre analytical \
  --pack core --pack substantiation --pack grounding --pack management

# Build the whole site (codes catalog + mkdocs + raw rubric/pack artifacts)
pip install -r requirements.txt
python build.py          # output in site/
```

## Published surface

| URL | What |
|-----|------|
| `/llms.txt` | agent anchor file: summary + links to the rubric and packs |
| `/rubric/<genre>.md` | paste-ready rubric per frame (analytical, advocacy, sales, status, persuasion) |
| `/packs/<pack>.yaml` | raw packs, served verbatim |
| `/`, `/codes`, `/design` | human docs |

`/rubric/*.md` and `/packs/*.yaml` are served as raw markdown/YAML (not rendered to
HTML), because the consumer is a model. The build regenerates them from the packs on
every deploy, so the served rubric never drifts from source.

## Scope (v1)

40 codes across four packs: `core`, `substantiation`, `grounding`, `management`. The
`engineering`, `sales`, and `marketing` packs live in `ontology/packs/` as source but
are not yet shipped; they are deferred to v1.x until they clear the contribution rule
through real use. See [`docs/design.md`](docs/design.md).

## Licensing

Dual-licensed:

- **Ontology content** (`ontology/*.yaml`, the rendered rubric, the docs) is under
  **CC0 1.0** (`LICENSE-DATA`). Public-domain dedication, frictionless ingestion,
  matching the agent-facing goal.
- **Code** (`render/rubric.py`, `build.py`, adapters) is under **MIT** (`LICENSE`).

The `grounding` pack is distilled from WillowEmberly's "AI Grounding Principles" and
the Negentropic Reasoning Protocol (OCAP, itself CC0). See `NOTICE`.
