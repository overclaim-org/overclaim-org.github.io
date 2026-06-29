# Groundedness Bridge: The Claims Ledger

How the ontology's evidence and substantiation codes connect to a quantitative
groundedness signal. The bridge is represented not as a scalar but as a **claims
ledger**: the list of atomic assertions a document makes, each with a support
verdict. The scalar groundedness score (RAGAS faithfulness / TruLens groundedness)
is a derived rollup over that ledger, not the primitive.

Read `DESIGN.md` first for the architecture (packs are the source of truth, the LLM
is the detector, `rubric.py` never reads subject text). This document defines the
ledger that the detector emits alongside its findings, and the rule that promotes a
failed claim into an overclaim code.

## Two grounding dimensions, kept separate

A claim can fail to be grounded in two unrelated ways, and conflating them is the
main error to avoid:

1. **Inline self-substantiation** (text-only, always computable): does the claim
   carry its own support in the artifact, a baseline, a denominator, a mechanism, a
   named comparator, a declared limitation? Judging this needs only the document.
   Most evidence and all substantiation codes test this axis.
2. **Corpus support** (needs a source): when an external source corpus is supplied,
   is the claim entailed by it? This is the RAGAS-faithfulness axis. It is `n/a`
   when no corpus is provided, which is the common case for status reports, exec
   replies, and advocacy memos with no attached evidence.

The two are orthogonal. A figure can be inline-unsupported (no denominator) yet
corpus-supported (the source confirms it), or inline-supported yet corpus-
contradicted. They feed different codes and never substitute for each other. Corpus
support does **not** clear an inline presentation defect: a hidden denominator is a
hidden denominator even if the number is true.

## Claim schema

One entry per atomic assertion. Lives under a top-level `claims:` array in the
finding sidecar.

```yaml
- id: c3                      # local handle; findings[].claim references it
  text: "latency dropped 40% after the cache change"
  block: 8f24                 # BlockRefs id of the source block (v2); loc string (v1)
  type: quantitative          # factual | quantitative | comparative | causal | predictive | normative
  inline_support: absent      # present | partial | absent
  corpus_support: n/a         # supported | contradicted | not-found | n/a
  evidence:                   # spans bearing on the claim, inline and/or corpus
    - where: inline           # inline | corpus
      source: null            # corpus filename when where=corpus
      span: null              # the supporting/contradicting text, null if none found
      relation: none          # supports | contradicts | partial | none
  promotes_to: [EVIDENCE_NO_BASELINE]   # overclaim codes this claim triggers; may be empty
```

`type` matters because it selects which codes a claim can promote to and whether the
claim is a groundedness target at all (`normative` never is). `inline_support` and
`corpus_support` are the two axes above. `promotes_to` is computed by the promotion
rule below, not authored by hand.

## What counts as one claim (atomicity rule)

Extraction decomposes prose into atomic, independently checkable assertions, the
FActScore / SAFE atomic-fact method (decompose, then verify each fact against a
source). The rule here is tighter than RAGAS's loose "statement" split because each
claim gets its own address and may be read out of context by a downstream agent:

- One predicate per claim. Split conjunctions ("X and Y" becomes two claims).
- Split an embedded justification: "X because Y" yields the factual claim X and the
  causal claim "X because Y".
- Resolve pronouns and ellipsis so each claim stands alone without the surrounding
  paragraph.
- Extract `normative` claims (value/should statements) and tag them, but never check
  them for groundedness; they exist in the ledger for completeness, not scoring.
- Do not extract questions, instructions, or pure hedges. A hedge is a `state`
  (`LIMITATION_DECLARED`), not a claim.

Extraction always runs; it needs no corpus. Corpus checking is the optional second
pass that fills `corpus_support` when a source is supplied. With no corpus, every
claim is `corpus_support: n/a` and only the inline axis is live, so a sourceless
status report does not light up every sentence.

## The promotion rule (claim status to overclaim code)

The bridge is mechanical: a claim that fails grounding promotes into the evidence or
substantiation code that names its failure shape. Keep the mapping in the packs, not
in a parallel table that drifts. Add a `claim_trigger` block to each promotable code:

```yaml
# on EVIDENCE_NO_BASELINE
claim_trigger:
  types: [quantitative, comparative]
  fires_when: { inline_support: [absent, partial] }
  corpus: not_required
  escalate_if: { corpus_support: contradicted }   # bump one severity notch
```

Promotion is then a lookup: for each claim, find the codes whose `claim_trigger`
matches its `type` and support state. The frame gate still runs afterward on the
resulting findings, so genre disposition and `LIMITATION_DECLARED` clearing apply
exactly as they do for any other finding.

Representative mappings against the current packs:

| Claim type | Failure shape | Promotes to |
|---|---|---|
| quantitative | no temporal/self baseline | `EVIDENCE_NO_BASELINE` |
| quantitative | rate/% with no base | `SUBSTANTIATION_DENOMINATOR_HIDDEN` |
| quantitative | efficacy/safety/savings claim, no proof standard | `SUBSTANTIATION_THRESHOLD_UNMET` |
| comparative | no cross-entity referent | `SUBSTANTIATION_COMPARATIVE_NO_REFERENT` |
| causal | no mechanism or controlled comparison | `EVIDENCE_CAUSALITY_OVERCLAIM` |
| factual | certainty language replacing evidence | `EVIDENCE_CONFIDENCE_AS_TRUTH` |
| factual | metric/authority treated as proof | `EVIDENCE_DASHBOARD_AUTHORITY` |
| factual | favourable subset/timeframe | `SUBSTANTIATION_CHERRY_PICKED` |
| factual | narrow sample generalised | `SUBSTANTIATION_SAMPLE_OVERGENERALIZED` |
| predictive | absolute outcome, no conditions | `COMMUNICATION_FALSE_CERTAINTY` |
| normative | n/a | never promotes |

Corpus-gating, the rule that stops a sourceless document being flagged to death:

- `corpus_support: contradicted` requires a corpus by definition (you can only
  contradict against a source). It always promotes, and escalates severity.
- `inline_support` gaps promote regardless of corpus; they are text-only defects.
- `corpus_support: n/a` (no corpus supplied) promotes nothing on its own. Absence of
  an external check is not a failure of the document.

## What this exercise surfaced: a missing code

The promotion table has no target for a plain factual claim that a supplied corpus
**contradicts** with no rhetorical tell, e.g. the document says "deployed Tuesday",
the source says "rolled back Monday", stated flatly with no certainty word, causal
verb, or authority appeal. The existing faithfulness mappings hang off rhetorical
codes (`EVIDENCE_CONFIDENCE_AS_TRUTH`, `EVIDENCE_CAUSALITY_OVERCLAIM`,
`NARRATIVE_CONFIDENCE_EVIDENCE_DECOUPLED`), so a bare contradiction matches none of
them. This is a candidate code (`EVIDENCE_CONTRADICTED_BY_SOURCE`, the named form of
a faithfulness failure) but it must clear the contribution rule (true + unnamed +
generalises) before being added. Logged as an open question, not added unilaterally.

## Where it sits in the sidecar

```yaml
claims: [ ... ]                  # the ledger above
findings: [ ... ]                # overclaim judgments; evidence-axis findings cite claim ids
decision: REVISE                 # gate = max severity over ACTIVE findings
severity_counts: {block: 0, revise: 1, constrain: 0, clarify: 2}
groundedness: null               # rollup over CHECKABLE claims only; null if none had a corpus
```

Relationships:

- `claims` is the universe of factual assertions; `findings` is the set of overclaim
  judgments. They overlap but are not the same list. A rhetorical finding
  (`COMMUNICATION_TONE_OVERCLAIM`, `MANAGEMENT_COMMITMENT_WITHOUT_MECHANISM`) is not
  a factual claim and never appears in `claims`. A supported claim appears in
  `claims` with no finding. The intersection is a failed claim that promotes.
- `groundedness` (the scalar) is the fraction of corpus-checkable claims that are
  `corpus_support: supported`. It is `null` when no claim had a corpus to check, and
  it speaks only to the corpus axis, never to inline substantiation. It is not a
  whole-document trust score; presenting it as one would be the tool's own
  `EVIDENCE_DASHBOARD_AUTHORITY`.
- Each claim's `block` is a BlockRefs id in v2, so the ledger is a third consumer of
  the identity layer alongside findings and annotations. v1 uses a plain loc string.

## What this touches in the packs

- Adds an optional `claim_trigger` block to evidence and substantiation codes (the
  promotable ones). Codes without it never receive promoted claims; they fire only
  from direct rhetorical detection as today.
- No change to existing fields, frame gate, or severities. Promotion produces
  ordinary findings that flow through the gate unchanged.
- The corpus-checking pass is an external engine (RAGAS / TruLens) or the LLM with
  the corpus in context. `rubric.py` still never reads subject text.

## Open questions

1. `EVIDENCE_CONTRADICTED_BY_SOURCE` , resolved: **added** to `core.yaml` as a
   `block`, never-softening code. It clears the contribution rule, it is the only
   corpus-axis (correspondence) code in the pack, and the distribute-plus-escalate
   alternative can't catch a bare contradiction because there is no rhetorical finding
   to escalate. Its `claim_trigger` (gated `corpus: required`) is deferred to when the
   claim-ledger machinery lands (see #2).
2. `claim_trigger` grammar: the `fires_when` / `escalate_if` predicate shape needs
   pinning before more than one code carries it, same drift risk as hash
   normalization in any spec with a tunable condition.
3. Multi-code promotion: a single quantitative claim can be both `NO_BASELINE` and
   `DENOMINATOR_HIDDEN`. Allow multiple promotions per claim (current assumption) or
   pick the most specific? Current call: allow multiple, let the frame gate and
   `decision` rollup dedupe by severity.
