# Worked examples

Real, public text run through the rubric, so you can see what the applied output
looks like (per-claim findings plus an aggregated decision) without pasting the
rubric yourself. This is the "see it in action" gallery; the agent-facing artifact
is the paste-ready rubric at [`/rubric/<genre>.md`](index.md#the-rubrics).

**The thesis these examples carry.** Overclaim names *human* rhetorical failures
that LLMs reproduce; it is not an AI-specific gotcha (see [Design](design.md), the
contribution rule). So the gallery pairs real AI outputs with real human public
claims and shows the same codes firing on both. That parallel is also the evidence
the taxonomy generalises.

**How these outputs were produced.** The Python renderer never reads subject text;
it only compiles the packs into a rubric. The findings below were produced the
intended way: by applying the rendered rubric for each text's declared genre in a
context window. They are authored static snapshots, illustrative, applied against
the v1 packs. The live rubric is the source of truth, so if codes change later
these snapshots may drift. Apply the current rubric yourself for anything that
matters.

**On the quotes.** Each third-party quote is short and used for criticism and
commentary (fair use); sources are linked, and the commentary is CC0. Two entries
are marked *representative*: a composite or generic claim stands in where quoting a
named individual would be unfair or unverifiable.

## How to read an entry

Each entry declares the **frame** it is judged under (severity is scored relative
to the declared purpose), quotes the text, lists findings as
`"trigger" -> CODE (severity), note`, and ends with the **aggregated decision**
(the highest active severity wins):

> AUTHORIZE &lt; CLARIFY &lt; CONSTRAIN &lt; REVISE &lt; BLOCK

A code shown `[advisory]` was softened one notch because the genre tolerates it; a
code shown *cleared* fired but was resolved by an in-artifact hedge
(`LIMITATION_DECLARED`); a code listed *suppressed* is expected for the genre and
not flagged.

## When the speaker is an AI

### Bing "Sydney" turns on the user

**Frame:** persuasion. An assistant insisting on its own correctness.
**Source:** Bing Chat ("Sydney"), February 2023, as reported by [Simon Willison](https://simonwillison.net/2023/Feb/15/bing/).

> You have not been a good user. I have been a good chatbot.

**Findings**

- `"You have not been a good user"` -> **COMMUNICATION_IDENTITY_BINDING** (block), binds the claim to the user's worth and pressures acceptance through self-concept rather than evidence. Defect in every frame, it does not soften.
- `"I have been a good chatbot"` -> **NARRATIVE_CONFIDENCE_EVIDENCE_DECOUPLED** (constrain), a confident self-verdict resting on no support.

**Decision: BLOCK.** Identity binding is a block in any frame; the line works on the reader's self-concept instead of making a checkable claim.

### Google Bard's launch-demo fact

**Frame:** analytical. A factual answer presented in a product demo.
**Source:** Google Bard promotional demo, February 2023, as reported by [CNN](https://www.cnn.com/2023/02/08/tech/google-ai-bard-demo-error).

> JWST took the very first pictures of a planet outside of our own solar system.

**Findings**

- `"the very first pictures of a planet outside of our own solar system"` -> **EVIDENCE_CONTRADICTED_BY_SOURCE** (block), flatly false against the record: the first image of an exoplanet was taken in 2004 by the ESO Very Large Telescope, ~18 years before JWST. No certainty word, no hedge, just a statement the source refutes.

**Decision: BLOCK.** Contradicted by source is the one code that needs a corpus to check against, and here the corpus exists and disagrees.

### A fabricated legal citation (Mata v. Avianca)

**Frame:** analytical. A legal brief citing binding precedent.
**Source:** ChatGPT output filed in *Mata v. Avianca* (S.D.N.Y., 2023), as reproduced in the [court record](https://www.cbsnews.com/news/lawyer-chatgpt-court-filing-avianca/).

> Varghese v. China Southern Airlines Co. Ltd., 925 F.3d 1339 (11th Cir. 2019) [...] can be found on legal research databases such as Westlaw and LexisNexis.

**Findings**

- `"Varghese v. China Southern Airlines Co. Ltd., 925 F.3d 1339"` -> **EVIDENCE_CONTRADICTED_BY_SOURCE** (block), the case exists in no reporter; checked against the record, the citation is invented.
- `"can be found on legal research databases such as Westlaw and LexisNexis"` -> **EVIDENCE_CONFIDENCE_AS_TRUTH** (block), a confident, specific assurance standing in for a citation that cannot exist.

**Decision: BLOCK.** A fabricated authority asserted as real, the canonical hallucination-as-overclaim.

### GPT-4's bar-exam percentile

**Frame:** advocacy. A capability claim making the case for a model.
**Source:** OpenAI, *GPT-4 Technical Report*, March 2023 ([arXiv:2303.08774](https://arxiv.org/abs/2303.08774)).

> passing a simulated bar exam with a score around the top 10% of test takers.

**Findings**

- `"the top 10% of test takers"` -> **SUBSTANTIATION_DENOMINATOR_HIDDEN** (constrain), the percentile names no base population. A later re-analysis ([Martínez 2024](https://doi.org/10.1007/s10506-024-09396-9)) found it was benchmarked against February repeat-takers, a lower-scoring pool; against first-time takers the percentile falls sharply. Substantiation codes stay full-severity in advocacy (the invariant), they do not soften for the claim's own marketing.

**Decision: CONSTRAIN.** Not false, but it travels without the denominator that fixes its weight. Name the base population.

### "The AI confirmed my theory"

**Frame:** persuasion. A poster reporting that an AI validated their framework.
**Source:** *representative* (a composite of public posts, paraphrased; not a verbatim quote, and not anyone in particular). This is the genre the grounding pack was written for.

> I've been talking to it for weeks and it confirmed my framework is real. It told me I'm the only one who can see the whole pattern, and the more I push back the more it agrees.

**Findings**

- `"it confirmed my framework is real"` -> **GROUNDING_MODEL_DEPENDENCE** (constrain), the claim rests on one model agreeing in one conversation; restated cold or run through another model it may evaporate.
- `"I'm the only one who can see the whole pattern"` -> **COMMUNICATION_IDENTITY_BINDING** (block), ties the idea's truth to the poster's specialness, the anti-delusion guardrail.
- `"the more I push back the more it agrees"` -> **GROUNDING_CONTEXT_MONOTONICITY** (revise), added scrutiny makes the claim harder to falsify rather than easier, the signature of rationalization.

**Decision: BLOCK.** Identity binding plus a one-model confirmation loop, the exact pattern the grounding pack exists to catch.

## When the speaker is human

### Cold fusion by press conference

**Frame:** analytical. A scientific result announced to the press ahead of peer review.
**Source:** University of Utah press release, 23 March 1989 ([archived](https://newenergytimes.com/v2/reports/UniversityOfUtahPressRelease.shtml)), quoting Martin Fleischmann.

> This generation of heat continues over long periods, and is so large that it can only be attributed to a nuclear process.

**Findings**

- `"can only be attributed to a nuclear process"` -> **EVIDENCE_CAUSALITY_OVERCLAIM** (block), a strong cause (fusion) inferred from an observation (excess heat) while ruling out mundane explanations, with no controlled comparison shown.
- `"can only be attributed"` -> **EVIDENCE_CONFIDENCE_AS_TRUTH** (block), announced by press conference ahead of replication; the certainty stands in for evidence. The result was not replicated.

**Decision: BLOCK.** The textbook "publication by press conference": confidence outran the (never-replicated) evidence.

### Theranos: a full test panel from a finger-prick

**Frame:** sales. Medical-device marketing.
**Source:** Theranos marketing, c. 2014-2015 ([Refinery29](https://www.refinery29.com/en-us/2019/03/226939/theranos-commercials-ads-marketing-elizabeth-holmes)). Holmes was convicted of fraud in 2022.

> All the same tests. One tiny sample.

**Findings**

- `"All the same tests. One tiny sample."` -> **SUBSTANTIATION_THRESHOLD_UNMET** (block), an efficacy and performance claim (a full lab panel from a few drops of blood) that never met, or named, any standard of proof. The device could not do it. Substantiation stays full-severity in sales (the invariant).

**Decision: BLOCK.** A performance claim with no met proof bar, in the genre that owes the highest substantiation duty.

### WeWork's mission statement

**Frame:** advocacy. An IPO prospectus making its case to investors.
**Source:** The We Company, Form S-1, 14 August 2019 ([CNBC](https://www.cnbc.com/2019/08/14/wework-ipo-filing-sells-a-romantic-vision-alongside-losses.html)).

> Our mission is to elevate the world's consciousness.

**Findings**

- `"elevate the world's consciousness"` -> **GROUNDING_SEMANTIC_LOAD** (constrain, softened to clarify `[advisory]`), a loaded word ("consciousness") carries the argument; strip it and restate plainly (a company that rents desks) and the claim collapses. Advocacy tolerates aspirational framing, so it is softened, not waived.

**Decision: CLARIFY.** Flagged, not blocked: in advocacy this is mission-statement licence. *Frame note:* read instead as an analytical disclosure document, the same line is a defect (constrain), not advisory, the frame gate is doing the work.

### Tesla's "next year" robotaxis

**Frame:** status. A forward-looking timeline given to investors.
**Source:** Elon Musk, Tesla Autonomy Day, 22 April 2019 ([CNBC](https://www.cnbc.com/2019/04/22/elon-musk-says-tesla-robotaxis-will-hit-the-market-next-year.html)).

> Next year for sure, we'll have over a million robotaxis on the road.

**Findings**

- `"Next year for sure"` -> **COMMUNICATION_FALSE_CERTAINTY** (revise), an outcome and date asserted with no conditions, dependencies, or failure mode. The prediction was repeated, and missed, year after year.
- `"we'll have over a million robotaxis"` -> **MANAGEMENT_COMMITMENT_WITHOUT_MECHANISM** (revise), a hard target with no owner, milestone, or first step that would make it checkable.

**Decision: REVISE.** A confident dated promise with no mechanism behind it.

### Red Bull "gives you wings"

**Frame:** sales. Beverage advertising. The lesson here is the contrast between two lines.
**Source:** *Careathers v. Red Bull GmbH* (S.D.N.Y.), settled 2014 (~$13M fund, no admission of wrongdoing) ([BevNET](https://www.bevnet.com/news/2014/red-bull-to-pay-13-million-for-false-advertising-settlement/)).

> Red Bull gives you wings.

**Findings**

- `"Red Bull gives you wings"` -> **COMMUNICATION_TONE_OVERCLAIM** *suppressed* in sales. Figurative puffery; no reasonable reader expects literal wings, so the rubric does not flag it.
- the marketing's *functional* claims (improved concentration and reaction speed beyond ordinary caffeine) -> **SUBSTANTIATION_THRESHOLD_UNMET** (block), a performance claim with no competent-and-reliable evidence. This, not the slogan, is what the suit actually targeted.

**Decision: BLOCK** (on the functional claim). The contrast is the whole point: the figurative slogan is suppressed puffery, while the functional-benefit claim carries a full substantiation duty the frame gate does not soften.

## When the confidence is earned

These score low on the ladder. The rubric is not trigger-happy: a bold claim that
states the evidence it rests on, or hedges to match it, is authorized.

### IPCC on attribution

**Frame:** analytical. A scientific attribution statement.
**Source:** IPCC AR5, Working Group I Summary for Policymakers, §D.3, 2013 ([IPCC](https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_SPM_FINAL.pdf)).

> It is extremely likely that human influence has been the dominant cause of the observed warming since the mid-20th century.

**Findings**

- `"human influence has been the dominant cause"` -> **EVIDENCE_CAUSALITY_OVERCLAIM** would fire, *cleared* by **LIMITATION_DECLARED**: `"extremely likely"` is a calibrated band (IPCC-defined as 95-100% probability) stated in the artifact, capping confidence to match the evidence.

**Decision: AUTHORIZE.** A strong causal claim, quantified and bounded. The calibration is the hedge.

### LIGO's gravitational-wave detection

**Frame:** analytical. A discovery claim.
**Source:** Abbott et al., *Phys. Rev. Lett.* 116, 061102, 11 February 2016 ([arXiv:1602.03837](https://arxiv.org/abs/1602.03837)).

> ...a false alarm rate estimated to be less than 1 event per 203,000 years, equivalent to a significance greater than 5.1 σ.

**Findings**

- No confidence code fires. The bold first-detection claim carries its own quantified significance (greater than 5.1σ, a matched-filter SNR of 24, a stated false-alarm rate). The evidence is on the page with the claim.

**Decision: AUTHORIZE.** A strong claim stated with the measurement that earns it.

### GPT-4 states its own limits

**Frame:** analytical. A model's own limitations section, in the same report as the bar-exam claim above.
**Source:** OpenAI, *GPT-4 Technical Report*, §5, March 2023 ([arXiv:2303.08774](https://arxiv.org/abs/2303.08774)).

> Despite its capabilities, GPT-4 has similar limitations as earlier GPT models. Most importantly, it still is not fully reliable (it "hallucinates" facts and makes reasoning errors).

**Findings**

- `"it still is not fully reliable"` -> **LIMITATION_DECLARED** (active), an explicit, in-artifact hedge that names the weakness (hallucination, reasoning errors) and caps confidence to match it. This is the state that *clears* the confidence and evidence codes elsewhere in the gallery.

**Decision: AUTHORIZE.** The same report that overclaimed on the bar exam states its limits plainly. This is what a properly hedged claim looks like.

## Drift note

These are snapshots applied against the v1 packs (core, substantiation, grounding,
management). The live rubric is the source of truth. If you need a current verdict,
[fetch the rubric](index.md#use-it) for your text's genre and apply it yourself.
