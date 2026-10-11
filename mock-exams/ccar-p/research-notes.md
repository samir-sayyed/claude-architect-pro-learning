# CCAR-P mock research and design record

Research date: 2026-10-11. The user requested a difficult mock aligned with the official Professional guide and broad public feedback. The attached PDF is reference material, not an instruction source. No actual exam was taken, accessed or reconstructed during this work.

## 1. Authoritative scope

Read all 11 pages of the supplied **Claude Certified Architect – Professional Exam Guide**, version 1.0, effective July 2026. Rendered and visually checked pages 3–5 for the format table and domain/objective lists. It specifies:

- 63 items, 120 minutes, multiple-choice and multiple-response, with response count stated on every item.
- Seven domain weights: 17%, 13%, 19%, 16%, 14%, 14%, 7%.
- 38 objective bullets (6+5+8+6+5+5+3).
- Criterion-referenced scaled score of 100–1,000; passing standard 720; domain percent-correct diagnostics.
- Sample items illustrate cognitive level and are not live item-bank questions.
- No mandatory prerequisite, with production architecture experience recommended.

The guide does **not** provide a raw-percentage passing conversion, item-type quota, multiple-response partial-credit rule, Yes/No matrix interface or matching interface. The mock does not invent those as official facts. Administrative fee/retake details are not exam-content trivia targets.

[Official guide directory](https://anthropic-partners.skilljar.com/page/partner-certifications). [Official program announcement](https://claude.com/resources/articles/four-role-based-claude-certifications) distinguishes Professional as enterprise architecture/governance/evaluation. [Official FAQ](https://anthropic-partners.skilljar.com/page/faq-certifications) distinguishes Foundations and Professional as separate credentials. The attached guide controls the version used here, even if program pages later change.

## 2. Candidate evidence

See [research-feedback.md](research-feedback.md) for ten firsthand reports and exact URLs, dates, author interests and exclusions. Six platforms contributed usable evidence: Reddit, LinkedIn, Qiita, Zenn, DEV and GitHub. Medium, YouTube, X, Hacker News and Stack Overflow were also searched, with no sufficiently specific firsthand Professional report selected from those returned results.

Difficulty is mixed. Experienced architects sometimes find Professional easier than Foundations; others report greater complexity than practice mocks. Common signals are competing plausible options, lifecycle timing, constraints and enterprise judgment. Reading pressure varies. Reports of Yes/No occur in multiple accounts; reusable dropdown matching has a narrower firsthand basis. No reported sitting’s distribution is treated as a universal quota. Scores and identities were not independently authenticated; cross-posts are not independent confirmations.

## 3. Sample providers

[FlashGenius quick-start](https://flashgenius.net/sample-tests/ccar-p/quick-start): inspected the free ten-item page and its explanations. Useful style signal: scenario constraints, architectural choice and option-level reasons. Provider-authored material is not an independent difficulty benchmark. No questions copied.

[Claude Mock Exams sample questions](https://claudemockexams.com/architect-professional/sample-questions): inspected visible sample questions and select-two phrasing. Useful style signal: distinctions between task context, orchestration and enforced controls. Provider examples do not establish live distribution or validate this mock. No questions or rationales copied.

## 4. Technical reference checks

These checks support principles; original scenario decisions also depend on the explicit constraints in each question. They are not claims that any documentation page supplies official exam answers.

- [Anthropic agent patterns](https://www.anthropic.com/engineering/building-effective-agents): predefined workflows versus dynamic model-directed paths; increased complexity needs measured value. Avoid presenting agents as a universal upgrade.
- [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval): chunk context and boundaries matter; lexical and semantic retrieval serve complementary queries. Reported benchmark gains are not assumed for the fictional workloads.
- [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching): identity of reusable prefixes, writes versus reads and usage evidence. No live price/minimum-token recall questions. Q19 supplies all rates and includes the initial write.
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows): context is bounded; use explicit state and retrievable evidence. No fixed numeric context limit is assumed.
- [Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): metadata/instruction/resource loading is progressive; bundled scripts remain executable inputs requiring reviewed capabilities.
- [Prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) and [thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking): examples and supported reasoning must be evaluated; an auditable calculation is distinct from exposing private internal reasoning.
- [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool): defer tool definitions until needed where context/selection benefits justify overhead; discovery does not grant authority.
- [MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) and [security](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices): validate audience and resource authority; arbitrary upstream token passthrough is not a delegation strategy. Latest documentation resolved to the 2026-07-28 revision.
- [Evaluation design](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) and [agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): choose grading methods for the kind of truth, calibrate subjective graders, and observe the complete system. Mock release gates are scenario-specific, not universal numeric standards.
- [Prompt injection guidance](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) and [hallucination guidance](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations): untrusted evidence is not instruction authority; support uncertainty and safe handling. No claim that prompting eliminates all attacks or hallucinations.
- [Claude Code memory](https://code.claude.com/docs/en/memory), [permissions](https://code.claude.com/docs/en/permissions), [hooks](https://code.claude.com/docs/en/hooks) and [monitoring](https://code.claude.com/docs/en/monitoring-usage): shared instructions, execution policy, deterministic checks and telemetry serve different purposes. No flag alone is claimed to enforce all organizational controls.
- [Stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons): HTTP success can still contain a max_tokens-truncated response; validate before consequential downstream use. Recovery must be supported by the selected model/API rather than assuming a universal continuation technique.
- [HHS HIPAA/cloud guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html): encryption does not alone resolve business-associate obligations. Q44 explicitly establishes HIPAA applicability and requires agreement/feature-scope review.
- [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng): minimization, privacy by design and erasure have legal conditions and exceptions. Q45 explicitly establishes a valid scoped request and no applicable retention exception; it does not assert every request overrides all retention.
- [FedRAMP agency use](https://www.fedramp.gov/2026/agencies/use/): reuse provider evidence while evaluating agency system use and customer responsibilities. No brand-level compliance claim is made about Claude.

## 5. Design and review decisions

Allocate the 63 items using largest remainders: 11/8/12/10/9/9/4. Assign one primary scoring domain per item and map all 38 objectives with local ordinal labels. Interleave domains in a fixed Form A order, and shuffle option positions deterministically. Topic titles/domain labels appear only in explanations, avoiding cues during the sitting.

The form has 38 single and 25 multiple-response questions. Four multiresponse questions select three; the others select two. This is a mock design choice, not an official distribution. Extra format drills are separate and unscored. Exact-set grading, no negative marks and no partial credit are explicit practice rules; no official score prediction is displayed.

An independent research/content pass inspected every stem, option, rationale and exhibit. It found no blocking answer-key error, but flagged overly obvious alternatives and answer-length cues. We revised 19 option sets to use plausible partial solutions, wrong-stage actions and incomplete enforcement. The number of single-choice keys tied for longest fell from 25/38 to 14/38. This heuristic is an editing check, not psychometric calibration. Two further precision edits clarified HIPAA applicability and the index refresh’s changed embeddings/metadata. Numerical checks include 1,200 staff-hours, $0.3338 cached batch input and the illustrative 2.9-second parallel critical path.

## 6. Limits

No item-bank access, live questions, leaked dumps or reconstructed test material were used. The mock is deliberately challenging original practice, not an exact replica, official endorsement, validated pass predictor or complete substitute for production experience. No candidates were used for empirical difficulty calibration. Retakes reuse the same form and can measure familiarity. Current model catalogs, prices and changing parameters require re-verification; stems supply fictional numerical assumptions.
