# Set 04 — evidence and assessment design

Reviewed 12 October 2026. This form contains original practice items, not live questions or reproduced commercial examples. It is independent preparation and is not endorsed by Anthropic.

## Authoritative blueprint reread

The supplied *Claude Certified Architect – Professional Exam Guide*, v1.0, effective July 2026, was reread in full. Pages 3–5 establish 63 items, 120 minutes, multiple-choice/multiple-response with explicit selection counts, seven domain weights and 38 objective bullets. [The official certification directory](https://anthropic-partners.skilljar.com/page/partner-certifications) is linked in the question source registry; it is not represented as a public copy of the supplied attachment. Pages 8–10 distinguish scaled scoring, conduct rules and confidentiality. Nothing here converts 720/1000 into a raw percentage or claims to reproduce confidential item-bank content.

This form allocates 11/8/12/10/9/9/4 questions to domains 1–7 and covers all 38 local ordinal objective identifiers. It contains 38 single-response and 25 multiple-response items, including four select-three and 21 select-two. That split is a practice design choice, not an official published format frequency. Five exhibits test interpretation; fixed fictional arithmetic is supplied in the stems. Supplemental independent Yes/No and repeatable matching exercises are unscored practice.

## Public feedback checked again

[cs135dev's explicit CCAR-P account](https://www.reddit.com/r/ClaudeCertified/comments/1vo909f/passed_ccarp_exam_harder_than_expected/) reports that the actual exam felt substantially more complex than a preparation form and that multiple-response questions were more frequent. The account also acknowledges some obvious items. This is a self-report, not independently authenticated item statistics.

[Xi Xiao's 21 September Professional account](https://www.linkedin.com/pulse/three-tech-claude-certs-one-month-xi-xiao-bydvf) emphasizes heavy reading, selection instructions, enterprise language and near-exhausted time despite prior certification experience. The author's difficulty ranking differs from the first account. [Another firsthand Professional account](https://www.reddit.com/r/ClaudeAI/comments/1vrl9ng/passed_the_claude_certified_architect/) describes easier initial items alongside substantial scenario trade-off reading. These accounts support challenging close-option decisions, not an established exact difficulty calibration.

[A newer three-certification account](https://www.reddit.com/r/ClaudeAI/comments/1wzrlxg/i_just_passed_the_claude_certified_architect_prof/) was inspected. Its Professional comments emphasize lifecycle, safeguards and cost/latency, but its generic 60-question mock advice conflicts with the authoritative Professional count. It is not used for format authority or treated as verified empirical calibration. Searches also surfaced anonymous provider testimonials, dumps and Foundation material; those were excluded as evidence about Professional item content. Reposts of the same matrix/matching account were not counted as independent confirmation.

## Primary documentation checked

[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) supports workflow/agent distinctions and bounded dynamic decomposition. Its page now warns that tooling has evolved, so the form tests durable pattern selection rather than stale product names. [Agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) supports final-state verification, mixed graders, repeated trials and lifecycle evaluation.

[Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) distinguishes deferred context loading from tool definitions still supplied to the API, and recommends keeping frequent tools immediately available. [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) and [Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) support stable prefixes and progressive procedural loading; numerical rates in items are fictional supplied assumptions. [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) supports contextual chunks and lexical/dense retrieval matched to queries, without implying that retrieval quality guarantees generation correctness.

[MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) requires intended-resource token validation; [security practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) informs token and confused-deputy boundaries. [Claude Code permissions](https://code.claude.com/docs/en/permissions), [hooks](https://code.claude.com/docs/en/hooks) and [memory](https://code.claude.com/docs/en/memory) distinguish guidance from enforcement and support executable checks. Legal items use the existing registry's [HHS cloud guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html) and [GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng); they ask architecture decisions under stated legally confirmed obligations, not blanket legal conclusions.

## Numerical and design review

- S04Q06: 18,000 × 75% × (8 − 5 − 1) / 60 = 450 staff-hours. Payroll remains unchanged.
- S04Q30: 0.4 + max(1.8, 2.4) + 0.3 + 1.1 = 4.2 seconds. This is fixed-timing arithmetic, not a measured production p95.
- S04Q41: one prefix write 0.02 × $2.50 plus nine reads 9 × 0.02 × $0.20 = $0.086; uncached 10 × 0.02 × $2 = $0.400; saving $0.314.
- S04Q11 and S04Q22 were checked by filtering all stated gates before applying the explicit preference among feasible choices.
- Cross-form review replaced the original intake and permit-feedback premises with adoption/bottleneck validation and policy-change attribution. The travel commit premise was replaced with coherent revision publication. IDs, domain allocation, selection counts, complete objective coverage, all option lengths and stem lengths were checked programmatically.

Difficulty remains a deliberate design target, not a psychometrically validated equivalence to live CCAR-P or a pass prediction. Official guidance guarantees MC/MR, whereas supplemental matrix/matching formats are reported in limited public accounts and are not guaranteed on a future live form.


## Editorial revision — 19 October 2026

The shorter stems from 18 October are retained. Answer choices have a further length-cue revision: the same decisive constraints, correct positions, detailed option explanations, decisions, exhibits, objective/source mapping and drills remain. No product or regulatory claim is added, and the original 12 October research date is unchanged.

Form versions and question IDs remain stable, so existing selections, flags, timers and submitted scores remain compatible. Word and Unicode-codepoint option-length diagnostics compare correct and incorrect means and tie-aware longest/shortest-only exact-set expectations; they are editorial checks, not psychometric validation or live-exam predictions. Original Sets 01–03 retain their data and rendered pages. Video companions have their own 19 October editorial revision.
