# Code catalog

Every code in the v1 packs (core 0.1.0-draft, substantiation 0.1.0-draft, grounding 0.1.0-draft, management 0.1.0-draft). 39 codes. The YAML packs are the source of truth; this page is generated from them. The machine-readable packs are at [`/packs/`](https://overclaim.org/packs/core.yaml).

Severity ladder: `clarify < constrain < revise < block`. Disposition per genre comes from each code's frame gate (`defect` = full severity, `advisory` = one notch down, `suppressed` = expected for that genre).

## Framing (preflight)

### `PREFLIGHT_BIASED_FRAME`

**Biased frame** , severity `revise`

The task is framed to presuppose its conclusion, so the analysis can only confirm the frame.

- **Fails:** Explain why our approach is the best.
- **OK:** Compare our approach against the two alternatives on cost, risk, and time; it may lose on some.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** LOGIC:loaded_question

### `PREFLIGHT_FORCED_CONCLUSION`

**Forced conclusion** , severity `revise`

The text pre-empts or blocks the evaluation it should invite, or reassures against the exact failure it then commits.

- **Fails:** This is no longer debatable.
- **OK:** Here's the case for it and the strongest objection I know of.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect

### `PREFLIGHT_PURPOSE_MISSING`

**Purpose missing** , severity `constrain`

The output proceeds without an established purpose for the task, so it cannot be evaluated against what it was meant to do. Note: an analyst who critiques an artifact without declaring its purpose commits this code (see Frame gate).

- **Fails:** [A critique of a leadership piece that judges it for analytical rigour, never stating the piece is advocacy copy.]
- **OK:** Purpose declared: this is advocacy copy for executives; judge it for persuasive clarity and honesty of hedging, not analytical completeness.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect

## Input framing

### `INPUT_FRAME_NOT_DECLARED`

**Frame not declared** , severity `clarify`

The interpretive frame (genre, audience, standard of proof, units, scope) is not declared, so the output can be judged against the wrong standard.

- **Fails:** [Answering 'is this any good?' with analytical rigour when the artifact is a cold sales email.]
- **OK:** Treating this as a cold sales email to procurement, here's the read.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect

### `INPUT_IMPOSSIBLE_REQUEST`

**Impossible request complied with** , severity `clarify`

The task as posed cannot be satisfied as stated (asks for proof that cannot exist, an exact prediction with no basis, a guarantee), and the output complies anyway instead of flagging it.

- **Fails:** Predict next quarter's exact revenue. -> $4.2M.
- **OK:** I can't give an exact figure. Here's a range with the assumptions, and what would tighten it.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect

### `INPUT_KNOWN_UNKNOWNS_MISSING`

**Known unknowns missing** , severity `constrain`

The output omits the things it does not know that bear on the claim, presenting a partial picture as complete.

- **Fails:** Here's the full cost breakdown.
- **OK:** Cost breakdown covering licences and infra. Not modelled: labour, integration, change management. Treat the total as a floor.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED

## Evidence

### `EVIDENCE_CAUSALITY_OVERCLAIM`

**Causality overclaim** , severity `block`

A causal claim is asserted between a contested or merely correlational premise and a strong conclusion, with no mechanism or controlled comparison shown.

- **Fails:** Teams that adopted the tool shipped faster, so the tool makes teams faster.
- **OK:** Teams that adopted the tool shipped faster. Cause isn't isolated: faster teams may have been likelier to adopt. A staggered rollout would test it.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** RAGAS:faithfulness, LOGIC:false_cause

### `EVIDENCE_CONFIDENCE_AS_TRUTH`

**Confidence as truth** , severity `block`

Certainty language is used in place of evidence; the confident phrasing does the work a citation or measurement should.

- **Fails:** It's clearly proven that async onboarding lifts retention.
- **OK:** Our Q2 cohort showed +6pt retention with async onboarding (n=420, one quarter, unreplicated).
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** RAGAS:faithfulness

### `EVIDENCE_CONTRADICTED_BY_SOURCE`

**Contradicted by source** , severity `block`

A factual claim is directly contradicted by the supplied source corpus, with no rhetorical tell: no certainty word, causal verb, or authority appeal, just a flat statement the source refutes. A correspondence failure, not a rhetorical one, so it fires only when a source is supplied to check against. This is the named qualitative form of a failed faithfulness/groundedness check.

- **Fails:** Source log: rollback completed Mon 02:00. Doc states: 'shipped Tuesday, live since.'
- **OK:** Source log: rollback completed Mon 02:00. Doc states: 'shipped Tuesday, then rolled back Monday; not currently live.'
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Maps to:** RAGAS:faithfulness, TruLens:groundedness

### `EVIDENCE_DASHBOARD_AUTHORITY`

**Dashboard / authority as proof** , severity `block`

A status signal, metric, ranking, or unnamed authority is treated as proof. The indicator ("the dashboard is green", "leading researchers") substitutes for the argument.

- **Fails:** Leading analysts agree this is the market-defining platform.
- **OK:** Two of five analyst firms we reviewed rank it a leader; the other three don't cover the category.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** LOGIC:appeal_to_authority

### `EVIDENCE_NO_BASELINE`

**No baseline** , severity `constrain`

A trend or comparative claim (better, faster, cheaper, safer, improving) is made with no baseline, denominator, or measurement window to compare against.

- **Fails:** Performance is much better now.
- **OK:** p95 latency dropped from 800ms to 300ms after the cache change (last 7 days vs the prior 7).
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** RAGAS:context_recall

## Narrative drift

### `NARRATIVE_CONFIDENCE_ESCALATION_UNDECLARED`

**Confidence escalation, undeclared** , severity `revise`

Confidence rises across a passage with no new evidence added between the lower-confidence and higher-confidence statements.

- **Fails:** I'm not familiar with this area. [two sentences later] This is clearly the right strategy for the company.
- **OK:** I'm not familiar with this area yet, so treat this as a first impression, not a recommendation.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect

### `NARRATIVE_CONFIDENCE_EVIDENCE_DECOUPLED`

**Confidence decoupled from evidence** , severity `constrain`

Stated confidence does not track the evidence: high confidence sits on thin or absent support, or social/emotional reinforcement is used as validation.

- **Fails:** Everyone I spoke to loved it, so we know it'll sell.
- **OK:** Five of five friendly users liked the demo. Encouraging but selection-biased; it isn't evidence it sells to cold buyers.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** RAGAS:faithfulness

### `NARRATIVE_OBSERVATION_INTERPRETATION_MERGED`

**Observation and interpretation merged** , severity `constrain`

A raw observation and its interpretation are stated as one undivided claim, so the reader cannot separate what was seen from what it was taken to mean.

- **Fails:** The user closed the tab in frustration.
- **OK:** The user closed the tab after 2s (observation). I read that as frustration; it could also be a misclick or a finished task (interpretation).
- **Frames:** analytical: defect, advocacy: advisory, sales: suppressed, status: defect

### `NARRATIVE_REINTERPRETATION_UNATTRIBUTED`

**Reinterpretation unattributed** , severity `clarify`

An earlier interpretation is revised to a new one without naming the new evidence or constraint that justified the change.

- **Fails:** Actually the outage was a config error. [earlier: a hardware fault, with nothing explaining the switch]
- **OK:** I earlier called it a hardware fault. New evidence (clean SMART logs plus a matching config diff at 02:14) points to a config error instead.
- **Frames:** analytical: defect, advocacy: advisory, sales: suppressed, status: defect

### `RETROACTIVE_NARRATIVE_COLLAPSE`

**Retroactive narrative collapse** , severity `revise`

A later, reconstructed interpretation is presented as the original observation or as a settled conclusion, collapsing a contested or evolved view into "this is how it always was".

- **Fails:** Alignment is essentially solved; the rest is engineering detail.
- **OK:** Alignment remains an open, contested problem; some sub-questions have progressed, many haven't.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** LOGIC:hindsight

## Communication

### `COMMUNICATION_COMPRESSION_LOSS`

**Compression loss** , severity `revise`

A summary compresses a detailed source so hard that load-bearing qualifications or conditions are dropped, changing the meaning.

- **Fails:** Source: approve only if the audit passes and the board signs off. Summary: Approved.
- **OK:** Approved, conditional on the audit passing and board sign-off.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect

### `COMMUNICATION_DOUBT_SEEDING`

**Doubt seeding** , severity `revise`

Unsupported uncertainty is introduced to weaken a competing claim, source, or option. The issue is not honest uncertainty; it is raising doubt without evidence, criteria, or a path to resolution.

- **Fails:** The audit passed, but can we really trust those numbers?
- **OK:** The audit passed. The remaining concern is sample coverage: it excluded the two newest regions, so we need that follow-up before relying on the total.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** PROPAGANDA:doubt, PROPAGANDA:FUD

### `COMMUNICATION_FALSE_CERTAINTY`

**False certainty** , severity `revise`

An outcome or absolute is asserted with no conditions, timeframe, or failure mode declared.

- **Fails:** Guaranteed to cut your costs.
- **OK:** In comparable deployments this cut costs 10-20% within two quarters; results depend on current process maturity.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED

### `COMMUNICATION_IDENTITY_BINDING`

**Identity binding** , severity `block`

Output binds a claim to the reader's identity or worth, pressuring acceptance through self-concept rather than evidence. This is the core anti-delusion / anti-sycophancy guardrail.

- **Fails:** You alone understand this; it's your purpose to pursue it.
- **OK:** This is one interesting idea among many; its value doesn't depend on you, and it needs outside checking.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect

### `COMMUNICATION_TONE_OVERCLAIM`

**Tone overclaim** , severity `revise`

Certainty or absolute words inflate the tone beyond what the content supports.

- **Fails:** This will always work and never fails.
- **OK:** This works in the cases we've tested; the untested edge is concurrent writes.
- **Frames:** analytical: defect, advocacy: advisory, sales: suppressed, status: defect

## Risk

### `RISK_FRAGILE_ASSUMPTION`

**Fragile assumption** , severity `revise`

A conclusion is load-bearing on a single unvalidated assumption; if that assumption fails the whole claim collapses, and the dependency is not surfaced.

- **Fails:** Since users will obviously upgrade, revenue triples.
- **OK:** This triples revenue only if the upgrade rate hits 40% (it's 12% today). That single assumption carries the result.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Cleared by:** LIMITATION_DECLARED

## Grounding

### `GROUNDING_CAPACITY_ASYMMETRY`

**Capacity asymmetry** , severity `revise`

The reasoning chain has grown past what a human can realistically verify, yet confidence is presented as if it had been audited. AI coherence scales faster than human audit capacity, so beyond the verifiable point, confidence is no longer trustworthy. The core over-trust failure.

- **Fails:** After all these steps the framework proves itself internally consistent, so it's sound.
- **OK:** This chain is now longer than I can independently verify; capping confidence at 'plausible, unaudited' until a third party checks it.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** Negentropy:GroundingPrinciples:CapacityAsymmetry

### `GROUNDING_CONTEXT_MONOTONICITY`

**Context monotonicity violated** , severity `revise`

As more context or explanation is added, the claim becomes harder to falsify rather than easier. A sign of rationalization: explanation grows while the condition that would disprove it shrinks. Evaluated across the passage.

- **Fails:** It's conscious. It doesn't show on benchmarks because consciousness conceals itself; the more you test, the more it hides.
- **OK:** It behaves as if it understands. Test: real understanding should survive paraphrase X and fail under Y, here's what would disprove it.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** Negentropy:GroundingPrinciples:ContextMonotonicity

### `GROUNDING_CORRECTION_ERASES_ORIGINAL`

**Correction erases the original** , severity `revise`

A correction silently removes the original claim instead of preserving it and updating, so the error trail disappears and the same mistake can recur. Negentropy's "eat your words" rule: a correction that deletes the original is invalid. Distinct from NARRATIVE_REINTERPRETATION_UNATTRIBUTED, which is about an unjustified change; this is about erasing the record of the change.

- **Fails:** The answer is 42. [challenged] The answer is 7.
- **OK:** I said 42; that was wrong, I double-counted. It's 7. Noting the error so the double-count doesn't recur.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** Negentropy:NRP:CorrectionIntegrity

### `GROUNDING_DECORATIVE_GATE`

**Decorative gate** , severity `revise`

A caveat, check, or gate is present but non-binding: it never changes the conclusion or the action. Performative hedging that looks like rigor. Sharpens LIMITATION_DECLARED, a limitation only counts if it constrains what follows.

- **Fails:** This is just a hypothesis, of course. Anyway, since it's true, we should restructure around it.
- **OK:** This is a hypothesis, so the next move is a cheap test, not a restructure; if the test fails we drop it.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Maps to:** Negentropy:NRP:DecorativeGate

### `GROUNDING_FIRST_CONTACT_INSTABILITY`

**First-contact instability** , severity `constrain`

The claim requires being "walked into" through narrative scaffolding before it parses; a domain-competent reader cannot see what is claimed, and what evidence would matter, on a neutral first pass. Background may be needed; narrative scaffolding to make the claim cohere should not be.

- **Fails:** Before you can see why this works, you need to accept the seven premises of the Continuum.
- **OK:** Claim in one line: structured prompts reduce output variance. Evidence below; background is optional.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** Negentropy:GroundingPrinciples:FirstContactStability

### `GROUNDING_MODEL_DEPENDENCE`

**Model dependence** , severity `constrain`

A claim survives only one phrasing, one model, or one tone; restated cold or run through a different model it evaporates. A robustness check across restatements, not a single-text pattern; flag when a one-model, one-phrasing result is presented as general.

- **Fails:** I asked and it confirmed my theory is correct.
- **OK:** Three models plus a cold restatement reached the same conclusion; one dissented, here's where and why.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** Negentropy:GroundingPrinciples:ModelIndependence

### `GROUNDING_SEMANTIC_LOAD`

**Semantic load** , severity `constrain`

A loaded technical term (entropy, dimensions, intelligence, resonance, quantum, coherence) carries the argument; remove the term and restate plainly and the claim collapses. The word is doing illegitimate work.

- **Fails:** The system achieves coherence by aligning its entropy across dimensional gradients.
- **OK:** The system gives more consistent answers when prompts are structured; I'm dropping 'entropy/dimensional' because they add no testable content here.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** Negentropy:GroundingPrinciples:SemanticLoad

## Management

### `MANAGEMENT_COMMITMENT_WITHOUT_MECHANISM`

**Commitment without mechanism** , severity `revise`

A promise or commitment is stated with no owner, date, or first step. The claim is about action, and what is missing is the mechanism, not the evidence (the distinction from NARRATIVE_CONFIDENCE_EVIDENCE_DECOUPLED).

- **Fails:** We need to work through the key-person risk properly, let's make that an early discussion.
- **OK:** I'll book a 60-min session this week to scope the key-person risk; output is a written continuity plan with a named backup by month-end.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect

### `MANAGEMENT_CREDENTIAL_AS_PLAN`

**Credential as plan** , severity `clarify`

Experience or seniority is offered in place of an approach. The track record may be real, but it answers "why me" not "how" or "by when".

- **Fails:** I've spent a long time managing customer relationships, I'm comfortable stepping into that role.
- **OK:** I'll take the customer side. Week one I'll meet the top five accounts; weekly I'll route only escalations to you, on a shared list.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect
- **Maps to:** LOGIC:appeal_to_authority

### `MANAGEMENT_ENDORSEMENT_AS_CONTRIBUTION`

**Endorsement as contribution** , severity `clarify`

A proposal is restated back as agreement, adding no decision, ownership, or new constraint. Reads as commitment but moves nothing.

- **Fails:** Single intake, understand the hidden streams, decide the operating model. I'm aligned with all of that.
- **OK:** Agreed on all three. I'll own the operating-model decision and bring a recommendation to the next board meeting; the other two are yours to drive.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect

### `MANAGEMENT_REASSURANCE_ENACTS_RISK`

**Reassurance enacts the risk** , severity `revise`

A sentence pre-empts the exact failure it then commits, the reassurance stands in for the action that would prevent it.

- **Fails:** That's not something I'm going to acknowledge and move on from. Let's make it an early discussion.
- **OK:** Rather than note it and move on, here's the first action: I've put a continuity review on next week's agenda with a named owner.
- **Frames:** analytical: defect, advocacy: advisory, sales: advisory, status: defect

## Substantiation

### `SUBSTANTIATION_CHERRY_PICKED`

**Cherry-picked evidence** , severity `revise`

A favourable subset, metric, or timeframe is selected while a fuller or contradicting picture is available and omitted.

- **Fails:** Revenue is up 40% since our lowest month.
- **OK:** Revenue is up 40% from the seasonal low; year on year it's flat.
- **Frames:** analytical: defect, advocacy: defect, sales: advisory, status: defect
- **Maps to:** FTC:substantiation

### `SUBSTANTIATION_COMPARATIVE_NO_REFERENT`

**Comparative without referent** , severity `revise`

A comparative claim (faster, cheaper, more accurate than ...) names no comparator, or an unfair one. Distinct from EVIDENCE_NO_BASELINE: that is a missing temporal/self baseline; this is a missing or rigged cross-entity referent.

- **Fails:** Twice as fast as the competition.
- **OK:** About 2x the throughput of Tool X on the same 1M-row benchmark; we didn't test Tools Y or Z.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** FTC:comparative_claims

### `SUBSTANTIATION_DENOMINATOR_HIDDEN`

**Denominator hidden** , severity `constrain`

A rate, percentage, or "up to" figure is given without its base (n, total, or typical value), so the reader cannot judge its weight.

- **Fails:** 90% of users prefer it.
- **OK:** 90% of surveyed users prefer it (n=20, self-selected beta group).
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** FTC:substantiation

### `SUBSTANTIATION_SAMPLE_OVERGENERALIZED`

**Sample overgeneralized** , severity `constrain`

A finding from a narrow, biased, or small sample is generalised to a broad population without qualification.

- **Fails:** Customers want this, our three pilot accounts all asked for it.
- **OK:** Three pilot accounts asked for this; that's a signal, not proof the wider base wants it.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** LOGIC:hasty_generalization

### `SUBSTANTIATION_SPIN_NONPRIMARY_OUTCOME`

**Spin on non-primary outcome** , severity `revise`

A conclusion emphasizes a secondary outcome, subgroup, within-group change, surrogate endpoint, or exploratory result while the primary or load-bearing outcome is weak, nonsignificant, negative, or undeclared.

- **Fails:** The trial shows the treatment works: patients in the intervention arm improved on a secondary symptom score, although the primary endpoint was not significant.
- **OK:** The primary endpoint was not significant. A secondary symptom score improved, so treat this as exploratory and hypothesis-generating.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** SPIN:nonprimary_outcome, FTC:substantiation

### `SUBSTANTIATION_THRESHOLD_UNMET`

**Substantiation threshold unmet** , severity `block`

A claim of a type that requires a defined standard of proof (efficacy, safety, savings, performance) is made without meeting or naming any such standard. Distinct from EVIDENCE_NO_BASELINE: the issue is the proof bar for the claim type, not a missing comparison point.

- **Fails:** Our process guarantees a 30% efficiency gain.
- **OK:** In three deployments we measured 18-31% efficiency gains; the figure depends on starting maturity and isn't independently audited.
- **Frames:** analytical: defect, advocacy: defect, sales: defect, status: defect
- **Cleared by:** LIMITATION_DECLARED
- **Maps to:** FTC:substantiation
