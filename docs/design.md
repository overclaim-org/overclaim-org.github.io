# Design

What overclaim is, why it is shaped this way, and the rules that govern it.

## The ontology is the asset, not an engine

The project began from a Reddit thread on avoiding AI-induced delusion, which links
a single Python gist framed as "flight envelope protection for AI output". The
gist's value is its vocabulary, not its code: its free-text detection is keyword
matching, and its structured modules read pre-set booleans the caller supplies and
echo a code rather than reading any text. The real detector was always the LLM that
loaded the framework and evaluated against it.

Overclaim makes that explicit. **The YAML packs are the source of truth, the LLM is
the detector, and the renderer compiles packs into a paste-in rubric and never
reads subject text.** There is no keyword engine here, and there should not be one.
The asset is the taxonomy plus thin adapters that emit into tools that already
exist.

## The frame gate

The central design rule: the ontology judges text relative to its declared purpose,
or it produces true-but-misapplied findings (the classic reason critique tools get
ignored).

1. **The frame gate runs first and modulates severity.** The caller declares
   `{genre, audience, goal}`. Each code carries a disposition per genre: `defect`
   (full severity), `advisory` (downgrade one notch, flag only when egregious), or
   `suppressed` (drop as expected for the genre). An overclaim in an analytical memo
   is a defect; the same line in advocacy or sales copy is often legitimate framing.
2. **A declared limitation is a mitigation, not a violation.** An explicit,
   in-artifact hedge that caps confidence to match the evidence clears the matching
   evidence or risk code. It only counts if visible to the reader in the artifact,
   not in the author's later defence of it.

Severity maps to a decision ladder: `AUTHORIZE < CLARIFY < CONSTRAIN < REVISE <
BLOCK`. The aggregated decision is the highest active severity.

**Invariant:** substantiation codes and identity binding do not soften in
sales/advocacy. Persuasive claims carry the highest substantiation duty (the FTC
"competent and reliable evidence" standard), and identity binding is the
anti-sycophancy guardrail. Their disposition stays `defect` in every genre.

## What is novel

The individual codes mostly have established academic or legal homes. The
contribution is the synthesis and the delivery, not the codes in isolation:

1. The cross-domain synthesis of hedging, factuality, spin, hallucination,
   propaganda technique, advertising substantiation, automation bias, and
   requirements-quality work into one named code vocabulary.
2. The genre-relative frame gate (severity scored against the declared purpose).
3. Serving *this* named taxonomy as an agent-facing domain , pull content
   (`llms.txt` + rendered rubric) a model ingests, rather than a human docs site.
   The apply-a-rubric loop itself is not the novel part: self-critique frameworks
   (Self-Refine, CRITIC, Chain-of-Verification) and Constitutional-AI self-critique
   already do "a model applies criteria to its own output and revises."

## Prior art

The surrounding space splits into mature camps this fuses:

- **Governance / eval runtimes** (DeepEval, RAGAS, Guardrails, NeMo-Guardrails,
  TruLens, llm-guard) operationalize the confidence-vs-evidence axis as numeric
  scores, but ship no named taxonomy of rhetorical overclaim modes. Rubric-scoring
  engines (Prometheus, FLASK) and atomic-fact factuality methods (FActScore, SAFE)
  are the natural execution targets, not competing taxonomies.
- **Reasoning-failure taxonomies** (fallacy datasets, clinical-trial "spin"
  detection, hedge-cue detection) name the failures academically but ship as
  datasets and classifiers, not a paste-in rubric.
- **Served-taxonomy precedent**: Llama Guard + the MLCommons hazard taxonomy show a
  named, public taxonomy applied by a model, in the safety domain. overclaim borrows
  that shape; the wedge is the overclaim taxonomy and frame gate, not the mechanism.

The wedge: a named rhetorical-overclaim taxonomy sitting on top of a real
groundedness scorer. The overclaim codes are the qualitative layer on top of a
quantitative groundedness score.

## Scope

v1 ships **core + substantiation + grounding + management** (40 codes). The
discriminator is validation maturity, not domain coverage: core and substantiation
are the validated spine; grounding cleared the contribution rule and carries the
WillowEmberly / Negentropy attribution; management is validated against live exec
messages. The engineering, sales, and marketing packs are deferred to v1.x because
they were added by reasoning rather than by running over diverse real text, so they
have not yet cleared "true + unnamed + generalises" through use. The rubric build
step makes adding a pack later cheap and non-breaking, so v1 needs to be correct,
not complete.

## Contribution rule

A new code earns its place only if it is **true + unnamed + generalises**: a real
example trips a genuine pattern, no existing code names it precisely, and it holds
beyond that one case. The ontology grows by being run over diverse genres (one
document per genre) and watching for the "true pattern, no precise code" signal,
not by bulk-collecting AI text (which re-confirms existing codes and biases toward
LLM stylistic tells). The ontology is not AI-specific: it names human rhetorical
failures that AI reproduces.
