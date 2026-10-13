# Domain 5 research and teaching decisions

Verified: 2026-10-13 (Asia/Kolkata). This chapter teaches practical architecture first and exam decision-making second.

## Scope and provenance

The supplied official CCAR-P Professional Exam Guide (July 2026 v1.0) was reread for the five Domain 5 objectives and 14% weighting. The guide is not republished. Objective identifiers 5.1–5.5 are local ordinal mappings, not official numbered identifiers. No actual exam items, recollections or dumps were used.

All sources below were opened during this research. For long documents, relevant portions were inspected rather than claiming a full independent regulatory or security assessment. Regulator pages support narrow educational statements; exact applicability and lawful processing in a real product require the responsible organization’s assessment.

## Verified findings and design implications

- **Risk management is continuous.** NIST AI RMF 1.0 functions are interrelated and Govern is cross-cutting. The official resource says a revision is in progress; the chapter does not invent a completed replacement. The GenAI Profile is a July 2024 companion, useful for confabulation and human-interaction risks rather than a current model benchmark.

- **Model behavior and authority are different controls.** OWASP’s 2025 pages distinguish prompt injection and excessive functionality, permissions and autonomy. The chapter uses those named 2025 references without claiming an unverified later Top 10 taxonomy. Actual enforcement examples are original application designs.

- **Current industry evidence is qualified.** Anthropic’s 24 November 2025 browser report describes multiple defenses and explicitly leaves residual injection risk. Its internal attack-success results are not production failure probabilities. The 9 April 2026 trustworthy-agents article describes model, harness, tools and environment and oversight friction. The 9 October 2026 unintended-actions report covers investigated evaluation/internal-use cases, reports limited impact in those cases, and describes containment/remediation. These are vendor reports, not independently measured prevalence across customer systems. No exploit instructions or private systems were reconstructed.

- **Protocol controls stay outside model interpretation.** The 2026-07-28 MCP security page forbids token passthrough and explains audience/security-boundary problems. Claude Code permissions were checked on the live documentation; the chapter avoids asserting that repository instructions themselves enforce tool or OS permissions. Product behavior is version/configuration dependent.

- **Confidence and fairness definitions need assumptions.** Guo et al. is an ICML 2017 classification-calibration paper, not evidence that an LLM self-confidence sentence is calibrated. Kleinberg et al. proves incompatibilities for particular formal risk-score conditions under specified assumptions, not that all fairness is impossible. NIST SP 1270 includes systemic and human bias factors. The synthetic arithmetic is original and explicitly distinguishes denominators.

- **GDPR implementation follows a scoped legal decision.** EDPB guidance supports purposes/means and processor relationships, purpose-specific lawful bases, minimisation, sensitive-data conditions and conditional rights. Its rights page describes erasure exceptions, access protecting others and significant solely automated decisions. The February 2026 erasure report pages 20–22 discusses backup integrity, tracking requests and restored-system handling. The chapter does not grant a universal backup exemption or assert that hashing equals anonymisation. EUR-Lex fetches did not return usable substantive text in this tool session, so the chapter relies on the directly read EDPB regulator guidance rather than claiming independent full-law verification.

- **HIPAA is relational and risk-based.** HHS covered-entity and BA pages, including current AI-chatbot/app examples, support the actor/relationship distinction. Cloud guidance states that no-view encrypted ePHI storage can still make a provider a BA and that encryption alone does not satisfy integrity, availability and administrative needs. Specific control responsibilities can be allocated as described by HHS; the chapter avoids both “BAA is enough” and “every control must be duplicated.”

- **FedRAMP boundary and agency decision matter.** Current 2026 agency-use rules call provider certifications reusable evidence and require agency authorization of the actual federal information system. The chapter names this current terminology and avoids equating a cloud offering badge with authorization for external endpoints or a whole application. It does not assert federal applicability to the user’s private projects.

## Original teaching artifacts

Hypothetical NutriMind and Krishi Mazdoor extensions are used to make mechanisms concrete. No assertion is made about current project implementation, patient use, agency customers or legal status. All records, counts, policies and figures are invented for teaching. No personal or clinical data is included.

The six diagrams cover continuous risk work, layered guardrails, injection authority transfer, approval binding, data-copy lifecycle and shared cloud responsibility. Ten checks test architectural decisions rather than vocabulary recall. Four copyable Markdown templates and one deterministic Python lab connect the concepts to project work without credentials or real side effects.

## Arithmetic independently checked

- Confidence bin: 166/200 = 83%; selective answering: 152/160 = 95% accepted accuracy and 160/200 = 80% coverage.
- Detector fixture: 90 true alerts + 198 false alerts gives 90/288 = 31.25% precision despite 90% recall.
- Zero observed failures: approximately 3/300 = 1% upper 95% bound under the stated independent, representative, stable-probability assumptions; not a production guarantee.
- Queue: 40 × 0.6 = 24 review cases/hour; 2 × 60/6 = 20 ideal capacity; five hours adds 20 cases; with arrivals stopped, that backlog requires one idealized hour to clear. No p95 inference.
- Fairness: A TP160/FP80/FN40/TN720, B TP80/FP90/FN20/TN810. Both TPR80% and FPR10%; precision A66.7%, B47.1%; selection A24%, B17%.

## Rejected shortcuts and limits

Rejected: provider badge implies application compliance; BAA alone configures controls; encrypted/no-view means no BA relationship; internal document provenance grants action authority; RAG removes injection; schema-valid means correct; model confidence is a measured probability; abstention is harmless; average capacity establishes a tail SLA; nominal approval establishes meaningful oversight; one parity metric proves fairness; deletion of one database row completes a rights request.

The lab is deliberately not a production authentication, authorization or compliance library. It assumes trusted synthetic actors, approvals and a pre-decided legal scope. It does not test a live model, clinical appropriateness, actual project integrations, real reviewers, users, regulatory applicability or production queue distributions. Guide alignment does not establish psychometric equality to the live exam.

## Sources actually used

### D5-S01 — NIST AI RMF 1.0 Core (2023; revision in progress when checked)
[NIST AI RMF 1.0 Core (2023; revision in progress when checked)](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

Continuous Govern, Map, Measure, Manage functions; owners and risk decisions.

### D5-S02 — NIST AI 600-1: Generative AI Profile (July 2024)
[NIST AI 600-1: Generative AI Profile (July 2024)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

Confabulation, information integrity, human interaction and generative-AI risk framing.

### D5-S03 — OWASP LLM06:2025 Excessive Agency
[OWASP LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)

Functionality, permissions and autonomy as separate sources of dangerous authority.

### D5-S04 — OWASP LLM01:2025 Prompt Injection
[OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

Direct and indirect injection; RAG is not an injection immunity mechanism.

### D5-S05 — Anthropic: Mitigating the risk of prompt injections in browser use (24 Nov 2025)
[Anthropic: Mitigating the risk of prompt injections in browser use (24 Nov 2025)](https://www.anthropic.com/research/prompt-injection-defenses)

Layered browser defenses and limits of vendor attack-success measurements.

### D5-S06 — Anthropic: Trustworthy agents in practice (9 Apr 2026)
[Anthropic: Trustworthy agents in practice (9 Apr 2026)](https://www.anthropic.com/research/trustworthy-agents)

Model, harness, tools and environment; meaningful human control and permission fatigue.

### D5-S07 — Anthropic: Investigating unintended model actions (9 Oct 2026)
[Anthropic: Investigating unintended model actions (9 Oct 2026)](https://www.anthropic.com/research/investigating-unintended-model-actions)

Recently reported evaluation/internal-use restriction workarounds and containment response.

### D5-S08 — MCP Security Best Practices (2026-07-28 documentation)
[MCP Security Best Practices (2026-07-28 documentation)](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)

Token audience, no token passthrough, and explicit security boundaries.

### D5-S09 — Claude Code: Configure permissions (checked 13 Oct 2026)
[Claude Code: Configure permissions (checked 13 Oct 2026)](https://code.claude.com/docs/en/permissions)

Tool permissions are an implementation control distinct from repository instructions.

### D5-S10 — Guo et al.: On Calibration of Modern Neural Networks (ICML 2017)
[Guo et al.: On Calibration of Modern Neural Networks (ICML 2017)](https://arxiv.org/abs/1706.04599)

Definition of empirical calibration; classification findings are not an LLM confidence guarantee.

### D5-S11 — EDPB: Respect individuals’ rights (checked 13 Oct 2026)
[EDPB: Respect individuals’ rights (checked 13 Oct 2026)](https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en)

Conditional erasure, access protecting other people, and significant solely automated decisions.

### D5-S12 — EDPB: 2025 CEF right-to-erasure report (adopted February 2026)
[EDPB: 2025 CEF right-to-erasure report (adopted February 2026)](https://www.edpb.europa.eu/system/files/2026-02/edpb_cef-report_2025_right-to-erasure_en.pdf)

Data location, retention and backup erasure/restore handling, especially pages 20–22.

### D5-S13 — HHS: Covered Entities and Business Associates (checked 13 Oct 2026)
[HHS: Covered Entities and Business Associates (checked 13 Oct 2026)](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html)

HIPAA actor/relationship applicability rather than health-data keywords alone.

### D5-S14 — HHS: Business Associates (checked 13 Oct 2026)
[HHS: Business Associates (checked 13 Oct 2026)](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html)

Health-app/cloud/AI-chatbot business-associate examples and relationships.

### D5-S15 — HHS: Guidance on HIPAA & Cloud Computing (checked 13 Oct 2026)
[HHS: Guidance on HIPAA & Cloud Computing (checked 13 Oct 2026)](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html)

No-view cloud remains a BA; encryption, BAA, availability and assigned controls.

### D5-S16 — FedRAMP Consolidated Rules for 2026: Using a Certified Cloud Service
[FedRAMP Consolidated Rules for 2026: Using a Certified Cloud Service](https://www.fedramp.gov/2026/agencies/use/)

Cloud-service evidence versus agency information-system authorization and customer controls.

### D5-S17 — NIST SP 1270: Identifying and Managing Bias in AI (March 2022)
[NIST SP 1270: Identifying and Managing Bias in AI (March 2022)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf)

Bias as a sociotechnical issue, including systemic and human factors.

### D5-S18 — Kleinberg, Mullainathan & Raghavan: Inherent Trade-Offs in Fair Risk Scores (2016)
[Kleinberg, Mullainathan & Raghavan: Inherent Trade-Offs in Fair Risk Scores (2016)](https://arxiv.org/abs/1609.05807)

Scoped mathematical incompatibility of particular fairness conditions; no universal fairness score.

### D5-S19 — Google DeepMind: Model cards (checked 13 Oct 2026)
[Google DeepMind: Model cards (checked 13 Oct 2026)](https://deepmind.google/models/model-cards/)

Current industry example of published model documentation; not application assurance.

### D5-S20 — Anthropic: Demystifying evals for AI agents (9 Jan 2026)
[Anthropic: Demystifying evals for AI agents (9 Jan 2026)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

Outcome/state evaluation, transcripts and complementary production/human evidence.

### D5-S21 — EDPB: Data protection basics (checked 13 Oct 2026)
[EDPB: Data protection basics (checked 13 Oct 2026)](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en)

Purpose, minimisation, retention and identifiable or sensitive data.

### D5-S22 — EDPB: Data controller or data processor (checked 13 Oct 2026)
[EDPB: Data controller or data processor (checked 13 Oct 2026)](https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en)

Purposes/means, processing on instructions, contracts and subprocessors.

### D5-S23 — EDPB: Process personal data lawfully (checked 13 Oct 2026)
[EDPB: Process personal data lawfully (checked 13 Oct 2026)](https://www.edpb.europa.eu/sme/be-compliant/process-personal-data-lawfully_en)

Purpose-specific lawful bases and additional conditions for sensitive data.
