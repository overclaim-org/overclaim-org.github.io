# Prior Art Literature Map

Status: draft, first academic prior-art pass  
Date: 2026-06-08  
Scope: all 53 draft ontology codes across core, substantiation, grounding, engineering, sales, marketing, and management packs.

## Summary Verdict

The individual codes are mostly not academically novel. Nearly every code maps to an established concept, an existing annotation task, a formal taxonomy, a legal substantiation rule, or a software-engineering standard. The strongest existing taxonomy analogs are clinical-trial spin, propaganda technique classification, FTC advertising substantiation, hallucination/attribution evaluation, factuality/hedging annotation, and automation bias.

The defensible contribution is narrower and cleaner: a unified, frame-aware operational rubric for detecting when confident language outruns its evidence across research, LLM output, engineering, sales, marketing, and management prose. The most plausibly novel pieces are the cross-domain synthesis, the frame gate, the delivery model as an LLM-applied paste-in rubric, and a few management/grounding formulations that combine known concepts but are not obviously named as standard taxonomy members.

## Verdict Legend

- `taxonomy-member`: the code is directly covered by an existing formal taxonomy or annotation scheme.
- `established-term`: the concept is named and mature, but not necessarily as the same taxonomy item.
- `operationalization-only`: the code packages known ideas into an applied check, but no exact canonical term was found in this first pass.
- `no-clear-home`: no clear academic or legal home found yet.

## Code Map

| Code | Verdict | Established home | Notes |
|---|---|---|---|
| `EVIDENCE_CAUSALITY_OVERCLAIM` | established-term | causal-language overstatement, false cause, spin | Strongly covered by causal language vs strength of inference work and informal fallacy taxonomy. |
| `EVIDENCE_CONFIDENCE_AS_TRUTH` | established-term | hedging, calibration, substantiation | Confidence replacing proof maps to epistemic modality, calibration, and advertised proof-level substantiation. |
| `EVIDENCE_DASHBOARD_AUTHORITY` | taxonomy-member | appeal to authority, argument from expert opinion, propaganda appeal to authority | Walton's expert-opinion scheme and SemEval propaganda techniques are direct homes. |
| `EVIDENCE_NO_BASELINE` | established-term | substantiation, comparative claims, denominator/base-rate disclosure | Closest to FTC substantiation plus basic research-design baseline discipline. |
| `NARRATIVE_OBSERVATION_INTERPRETATION_MERGED` | operationalization-only | factuality/source commitment, observation vs inference | FactBank covers source-relative factuality; this code is a practical reader-facing split. |
| `NARRATIVE_CONFIDENCE_ESCALATION_UNDECLARED` | operationalization-only | factuality, hedging, linguistic calibration | Known ingredients, but the longitudinal "confidence rises without evidence" check is the ontology's applied packaging. |
| `NARRATIVE_REINTERPRETATION_UNATTRIBUTED` | operationalization-only | factuality revision, source attribution, correction integrity | Related to HARKing and factuality/source tracking; exact taxonomy item not found. |
| `NARRATIVE_CONFIDENCE_EVIDENCE_DECOUPLED` | established-term | calibration, hallucination/faithfulness, sycophancy | Strongly covered by calibration and faithfulness/attribution literature; social reinforcement adds sycophancy overlap. |
| `RETROACTIVE_NARRATIVE_COLLAPSE` | established-term | HARKing, hindsight reconstruction, post hoc rationalization | Kerr's HARKing is the clearest academic home for presenting later reconstruction as prior reasoning. |
| `COMMUNICATION_TONE_OVERCLAIM` | taxonomy-member | loaded language, hedging/epistemic modality | SemEval loaded language and hedging literature cover inflated certainty/tone. |
| `COMMUNICATION_FALSE_CERTAINTY` | established-term | hedging, epistemic modality, FTC guarantees | Mature in linguistics and advertising law. |
| `COMMUNICATION_DOUBT_SEEDING` | taxonomy-member | propaganda "doubt", FUD, epistemic vigilance | Added from propaganda/persuasion taxonomies. Distinct from honest uncertainty because it raises doubt without evidence or resolution criteria. |
| `COMMUNICATION_COMPRESSION_LOSS` | established-term | summarization factuality, attribution, hallucination | Fits NLG faithfulness, AIS, and intrinsic/extrinsic hallucination framing. |
| `COMMUNICATION_IDENTITY_BINDING` | operationalization-only | sycophancy, epistemic vigilance, persuasion pressure | Strong conceptual overlap, but "bind claim to user's identity/worth" is not yet found as a formal taxonomy member. |
| `PREFLIGHT_PURPOSE_MISSING` | established-term | genre analysis, pragma-dialectics, task framing | Swales/genre and pragma-dialectics support purpose-relative evaluation. |
| `PREFLIGHT_BIASED_FRAME` | taxonomy-member | loaded question, presupposition, biased prompt framing | Direct fallacy/pragmatics home. |
| `PREFLIGHT_FORCED_CONCLUSION` | taxonomy-member | begging the question, black-and-white fallacy, loaded language | Covered by fallacy and propaganda taxonomies, though this code's "pre-empts evaluation" phrasing is applied. |
| `INPUT_FRAME_NOT_DECLARED` | established-term | genre, pragmatics, activity type | Same literature as purpose missing; the code is operational discipline for LLM critique. |
| `INPUT_KNOWN_UNKNOWNS_MISSING` | established-term | Toulmin qualifiers/rebuttals, uncertainty disclosure | Known as missing qualifiers, rebuttals, or limitations. |
| `INPUT_IMPOSSIBLE_REQUEST` | operationalization-only | calibration, impossible task refusal, epistemic limits | Known ingredients, no exact standard taxonomy item found in this pass. |
| `RISK_FRAGILE_ASSUMPTION` | established-term | sensitivity analysis, assumption surfacing, implementation planning | Strong home in decision analysis/research design; not a named rhetoric taxonomy item. |
| `SUBSTANTIATION_THRESHOLD_UNMET` | taxonomy-member | FTC prior substantiation, spin | Directly covered by advertising substantiation law and research spin. |
| `SUBSTANTIATION_DENOMINATOR_HIDDEN` | established-term | denominator disclosure, base rate, substantiation | Common statistics and advertising-substantiation issue. |
| `SUBSTANTIATION_CHERRY_PICKED` | taxonomy-member | cherry-picking/card stacking, QRPs, spin | Covered by propaganda "card stacking" lineage, QRPs, and spin. |
| `SUBSTANTIATION_SPIN_NONPRIMARY_OUTCOME` | taxonomy-member | clinical-trial spin, selective outcome reporting | Added from spin taxonomies. Covers emphasis on secondary outcomes, subgroups, within-group change, surrogate endpoints, or exploratory results when the primary result is weak. |
| `SUBSTANTIATION_SAMPLE_OVERGENERALIZED` | taxonomy-member | hasty generalization, external validity | Direct informal fallacy home. |
| `SUBSTANTIATION_COMPARATIVE_NO_REFERENT` | taxonomy-member | comparative advertising claims, missing comparator | Direct FTC/NAD-style comparative-claim issue. |
| `GROUNDING_CONTEXT_MONOTONICITY` | operationalization-only | falsifiability, ad hoc hypothesis, rationalization | Strong Popper/ad hoc hypothesis overlap, but "monotonicity" is not a standard term found here. |
| `GROUNDING_SEMANTIC_LOAD` | established-term | pseudo-profound bullshit, scientific bullshit, jargon misuse | Pennycook et al. and Frankfurt give the home; "semantic load" is a useful local label. |
| `GROUNDING_MODEL_DEPENDENCE` | established-term | robustness checks, model agreement, sycophancy, calibration | Known validation practice; not a named taxonomy item. |
| `GROUNDING_FIRST_CONTACT_INSTABILITY` | operationalization-only | comprehensibility, genre expectations, unfalsifiable scaffolding | Related to clarity and falsifiability; exact home not found. |
| `GROUNDING_CAPACITY_ASYMMETRY` | established-term | automation misuse, automation bias, verification complexity, calibrated trust | Strong human-factors home. |
| `GROUNDING_DECORATIVE_GATE` | operationalization-only | hedging, caveat effectiveness, disclosures that do not cure deception | Known pieces in FTC and hedging literature; exact term not found. |
| `GROUNDING_CORRECTION_ERASES_ORIGINAL` | operationalization-only | correction integrity, provenance, source tracking | Good local operational check; no clear formal taxonomy found yet. |
| `ENGINEERING_SPEC_AMBIGUITY` | taxonomy-member | requirements quality, unambiguous/verifiable requirements | Direct ISO/IEC/IEEE 29148 home. |
| `ENGINEERING_ESTIMATE_ASSUMPTION_UNSTATED` | established-term | project estimation assumptions, implementation intentions | Established practice, thinner as a named academic taxonomy item. |
| `ENGINEERING_COVERAGE_ILLUSION` | established-term | test adequacy limits, coverage vs oracle quality | Strong software-testing home. |
| `ENGINEERING_BENCHMARK_UNREPRODUCIBLE` | established-term | reproducibility, benchmark reporting, substantiation | Established reproducibility and performance-reporting issue. |
| `ENGINEERING_COMPLEXITY_HANDWAVE` | established-term | algorithmic complexity/performance substantiation | Known engineering claim issue, not a formal rhetoric taxonomy member. |
| `ENGINEERING_REPRODUCIBILITY_GAP` | established-term | reproducibility, root-cause verification | Mature software/research practice home. |
| `SALES_ROI_FABRICATED` | taxonomy-member | FTC substantiation, objective savings claims | Direct advertising-substantiation home. |
| `SALES_SOCIAL_PROOF_UNVERIFIABLE` | taxonomy-member | testimonial/social proof substantiation, appeal to popularity/authority | Covered by FTC endorsement/substantiation and propaganda persuasion techniques. |
| `SALES_URGENCY_MANUFACTURED` | taxonomy-member | scarcity/urgency persuasion, appeal to fear, dark patterns | Established persuasion technique; legal treatment depends on claim facts. |
| `SALES_FEATURE_CAPABILITY_CONFLATION` | established-term | feature-benefit overclaim, causal overclaim, substantiation | Known in advertising and product claims, but not a single canonical taxonomy item found. |
| `SALES_OVERCOMMITMENT` | established-term | commissive speech acts, contract/SLA promises | Clear speech-act and commercial-commitment home. |
| `SALES_COMPLIANCE_CLAIM_UNQUALIFIED` | taxonomy-member | regulated/security compliance substantiation | Direct substantiation and regulatory-claim issue. |
| `MARKETING_PUFFERY_AS_FACT` | taxonomy-member | puffery vs objective claim | Direct advertising-law home. |
| `MARKETING_REGULATED_CLAIM_UNQUALIFIED` | taxonomy-member | health, environmental, financial substantiation | Direct FTC regulated-claim home. |
| `MARKETING_BEFORE_AFTER_UNCONTROLLED` | taxonomy-member | testimonial substantiation, spin, uncontrolled before/after claims | Direct advertising-substantiation and spin home. |
| `MANAGEMENT_COMMITMENT_WITHOUT_MECHANISM` | operationalization-only | commissives, implementation intentions | The pieces are known: promises commit speakers, and action follows better from when/where/how plans. Exact management-rhetoric code not found. |
| `MANAGEMENT_ENDORSEMENT_AS_CONTRIBUTION` | operationalization-only | commitment, decision ownership, speech acts | Thin academic home. Likely a useful local management-communication code. |
| `MANAGEMENT_REASSURANCE_ENACTS_RISK` | operationalization-only | performative reassurance, decorative caveat, commitment without mechanism | Thin academic home. Related to "cheap talk" and commissives, but not yet a standard item. |
| `MANAGEMENT_CREDENTIAL_AS_PLAN` | taxonomy-member | appeal to authority, credentialism | Direct fallacy home; the "as plan" operationalization is local. |

## Literature Clusters

### Clinical-Trial Spin and Causal Language

Clinical-trial and systematic-review "spin" is the closest prior-art family for evidence, substantiation, and marketing claims. Boutron-style spin research formalizes reporting strategies that make weak or nonsignificant findings look more beneficial than the evidence supports. Yavchitz et al. developed a ranked classification of spin in systematic reviews and meta-analyses. Haber et al.'s CLAIMS review directly tests whether causal language is too strong for the underlying inference.

Implication: adopt "spin" terminology where it fits. Do not present the evidence/substantiation pack as novel at the code level.

### Propaganda and Persuasion Taxonomies

Da San Martino et al. and SemEval-2020 Task 11 provide a direct formal taxonomy analog for loaded language, appeal to authority, black-and-white fallacy, doubt, repetition, and related persuasion techniques. This covers a large portion of tone, authority, biased frame, forced conclusion, sales urgency, and cherry-picking/card-stacking style failures.

Implication: the sales and communication packs are mostly applied rhetoric/persuasion detection, not new categories.

### Hedging, Factuality, and Calibration

Hyland's hedging work, BioScope, CoNLL-2010 hedge detection, FactBank, and CommitmentBank all formalize uncertainty, source commitment, factuality, and how claims are linguistically qualified. Guo et al. and Lin et al. provide the ML calibration bridge. Rashkin's AIS and hallucination surveys cover source-grounded generation.

Implication: confidence, certainty, compression loss, and confidence/evidence decoupling should cite this literature heavily.

### Automation Bias and Grounding

Parasuraman and Riley define automation use, misuse, disuse, and abuse; Parasuraman and Manzey review automation complacency and bias; Lee and See frame appropriate reliance as calibrated trust. These are strong academic roots for the avionics-origin "grounding" language and especially `GROUNDING_CAPACITY_ASYMMETRY`.

Implication: keep the avionics framing, but anchor it in human factors rather than presenting it as a new metaphor.

### Advertising Law and Substantiation

FTC policy is a direct home for objective claims, implied claims, competent and reliable scientific evidence, comparative claims, testimonials, guarantees, and puffery vs fact. It covers most substantiation, sales, and marketing codes.

Implication: for commercial packs, cite FTC/NAD-style standards as the proof bar. These codes should not soften just because the frame is sales.

### Management Communication

The management pack is the thinnest. Speech-act theory covers commissives and promises; implementation-intention research covers why vague goals fail without when/where/how action plans. That supports `MANAGEMENT_COMMITMENT_WITHOUT_MECHANISM`, but the other management micro-codes are mostly local operational formulations.

Implication: management/commercial language is the best candidate for a narrow original contribution, but only as applied packaging over speech-act and implementation-planning concepts.

## Candidate Watchlist

These surfaced during the literature pass but are deliberately not first-class codes yet.

| Candidate | Current disposition | Why not added yet |
|---|---|---|
| `SUBSTANTIATION_ADVERTISED_PROOF_LEVEL_UNMET` | Track under `SUBSTANTIATION_THRESHOLD_UNMET` | FTC's "advertised level of substantiation" rule is distinct, but the current threshold code already covers proof-bar mismatch. Split later if examples show it needs separate handling. |
| `COMMUNICATION_LOADED_LANGUAGE` | Track under `COMMUNICATION_TONE_OVERCLAIM` and propaganda mappings | SemEval treats loaded language as first-class. Current tone code covers certainty inflation, but not all emotional loading. Split later if propaganda-style emotional wording becomes a core target. |
| `GROUNDING_AD_HOC_RESCUE` | Track under `GROUNDING_CONTEXT_MONOTONICITY` | Popper/ad hoc hypothesis literature supports a distinct rescue move. Current monotonicity code captures the same pattern over a passage. Split if challenge-response evaluation becomes explicit. |
| `MANAGEMENT_CHEAP_TALK_COMMITMENT` | Track under `MANAGEMENT_COMMITMENT_WITHOUT_MECHANISM` | "Cheap talk" is a useful academic bridge, but the mechanism code already catches no-cost, no-owner, no-date commitments. Split if strategic incentive-free signaling becomes a recurring case. |

## Positioning Recommendation

Use this framing in the README:

> A unified, frame-aware operational rubric for detecting epistemic overclaim in prose. It synthesizes established work on hedging, factuality, spin, hallucination, propaganda techniques, advertising substantiation, automation bias, and requirements quality into a practical code vocabulary that an LLM or reviewer can apply to a declared genre and goal.

Avoid:

> A novel taxonomy of epistemic overclaim.

Acceptable narrower claim:

> The individual failure modes mostly have prior homes. The contribution is the cross-domain synthesis, genre-relative frame gate, and operational packaging for LLM-assisted review.

## Citation Keys

- `TOULMIN_1958`: Stephen Toulmin, *The Uses of Argument*. Claim, grounds/data, warrant, qualifier, rebuttal. Overview: <https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html>
- `WALTON_EXPERT_OPINION`: Douglas Walton's argumentation schemes and critical questions for argument from expert opinion. Overview: <https://www.reasoninglab.com/patterns-of-argument/argumentation-schemes/waltons-argumentation-schemes/>
- `HYLAND_HEDGING_1996`: Ken Hyland, "Talking to the Academy: Forms of Hedging in Science Research Articles." <https://journals.sagepub.com/doi/10.1177/0741088396013002004>
- `BIOSCOPE_2008`: Szarvas et al., BioScope corpus for uncertainty, negation, and scope. <https://pmc.ncbi.nlm.nih.gov/articles/PMC2586758/>
- `CONLL_HEDGE_2010`: CoNLL-2010 shared task on hedge detection. <https://aclanthology.org/W10-30.pdf>
- `FACTBANK_2009`: Sauri and Pustejovsky, FactBank event factuality. <https://www.researchgate.net/publication/220147734_FactBank_A_corpus_annotated_with_event_factuality>
- `COMMITMENTBANK_2019`: de Marneffe et al., CommitmentBank. <https://ojs.ub.uni-konstanz.de/sub/index.php/sub/article/view/601>
- `SPIN_RCT_BOUTRON_2010`: Boutron et al., spin in randomized controlled trial abstracts. Summary example: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10733936/>
- `SPIN_SR_YAVCHITZ_2016`: Yavchitz et al., classification of spin in systematic reviews and meta-analyses. <https://pubmed.ncbi.nlm.nih.gov/26845744/>
- `HABER_CLAIMS_2018`: Haber et al., causal language and strength of inference. <https://pmc.ncbi.nlm.nih.gov/articles/PMC5976147/>
- `HARKING_KERR_1998`: Norbert Kerr, HARKing. <https://pubmed.ncbi.nlm.nih.gov/15647155/>
- `QRP_SIMMONS_2011`: Simmons, Nelson, and Simonsohn, false-positive psychology and undisclosed flexibility. <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1850704>
- `IOANNIDIS_2005`: Ioannidis, "Why Most Published Research Findings Are False." <https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124>
- `PROPAGANDA_DASANMARTINO_2019`: Da San Martino et al., fine-grained propaganda analysis. <https://aclanthology.org/D19-1565.pdf>
- `SEMEVAL_PROPAGANDA_2020`: SemEval-2020 Task 11, propaganda technique detection. <https://arxiv.org/abs/2009.02696>
- `FTC_SUBSTANTIATION_1984`: FTC Policy Statement Regarding Advertising Substantiation. <https://www.ftc.gov/legal-library/browse/ftc-policy-statement-regarding-advertising-substantiation>
- `FTC_HEALTH_GUIDANCE`: FTC Health Products Compliance Guidance. <https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance>
- `PARASURAMAN_RILEY_1997`: Parasuraman and Riley, "Humans and Automation: Use, Misuse, Disuse, Abuse." <https://doi.org/10.1518/001872097778543886>
- `PARASURAMAN_MANZEY_2010`: Parasuraman and Manzey, automation complacency and bias. <https://pubmed.ncbi.nlm.nih.gov/21077562/>
- `LEE_SEE_2004`: Lee and See, trust in automation and appropriate reliance. <https://pubmed.ncbi.nlm.nih.gov/15151155/>
- `GODDARD_AUTOMATION_BIAS_2012`: Goddard et al., automation bias systematic review. <https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/>
- `JI_HALLUCINATION_2023`: Ji et al., survey of hallucination in natural language generation. <https://dl.acm.org/doi/10.1145/3571730>
- `GUO_CALIBRATION_2017`: Guo et al., calibration of modern neural networks. <https://proceedings.mlr.press/v70/guo17a>
- `LIN_VERBAL_UNCERTAINTY_2022`: Lin, Hilton, and Evans, verbalized uncertainty. <https://arxiv.org/abs/2205.14334>
- `RASHKIN_AIS_2021`: Rashkin et al., Attributable to Identified Sources. <https://arxiv.org/abs/2112.12870>
- `PEREZ_SYCOPHANCY_2023`: Perez et al., model-written evaluations and sycophancy. <https://aclanthology.org/2023.findings-acl.847/>
- `SHARMA_SYCOPHANCY_2023`: Sharma et al., sycophancy in language models. <https://dblp.org/rec/journals/corr/abs-2310-13548.html>
- `SPERBER_EPISTEMIC_VIGILANCE_2010`: Sperber et al., epistemic vigilance. <https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0017.2010.01394.x>
- `PENNYCOOK_BULLSHIT_2015`: Pennycook et al., pseudo-profound bullshit. <https://gordonpennycook.com/wp-content/uploads/2021/09/pennycook-et-al.-2015-jdm.pdf>
- `FRANKFURT_BULLSHIT_2005`: Harry Frankfurt, *On Bullshit*. <https://philpapers.org/rec/FRAOBZ>
- `POPPER_FALSIFIABILITY`: Popper/falsifiability and ad hoc hypotheses. Overview: <https://plato.stanford.edu/archives/spr2019/entries/popper/>
- `ISO_29148_2018`: ISO/IEC/IEEE 29148:2018 requirements engineering. <https://www.iso.org/standard/72089.html>
- `COVERAGE_ORACLE_2022`: Oracle-based test adequacy and limits of coverage. <https://arxiv.org/abs/2212.06118>
- `SEARLE_SPEECH_ACTS_1969`: Searle speech-act theory and commissives. Overview: <https://pragmatics.indiana.edu/speechacts/promises.html>
- `GOLLWITZER_IMPLEMENTATION_1999`: Gollwitzer, implementation intentions and when/where/how plans. <https://www.prospectivepsych.org/sites/default/files/pictures/Gollwitzer_Implementation-intentions-1999.pdf>
- `SWALES_GENRE`: Swales genre analysis and discourse-community expectations. Example overview: <https://link.springer.com/article/10.1186/s40554-016-0032-2>
- `PRAGMA_DIALECTICS`: Pragma-dialectics and communicative activity types. Overview: <https://link.springer.com/article/10.1007/s10503-015-9377-z>
