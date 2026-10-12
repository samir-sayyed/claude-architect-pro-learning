# Form 02 research and construction notes

Reviewed 12 October 2026. This form contains original scenarios and fictional measurements; it does not reproduce confidential exam content or provider samples. Difficulty is intentionally demanding, but no access to the live item bank or psychometric calibration establishes equivalent difficulty or predicts passing.

The attached official **CCAR-P Exam Guide v1.0, July 2026** was reread in full. Pages 3–6 establish 63 items, 120 minutes, seven weighted domains and the objectives. Pages 6–7 illustrate constrained architectural choices. Page 8 describes a scaled passing score of 720; it does not authorize converting 72% raw performance into a pass. Its stated scored formats are multiple-choice and multiple-response. The two independent Yes/No exercises and repeatable matching exercise here are supplementary, unscored practice, not additional official format requirements. [Official directory](https://anthropic-partners.skilljar.com/page/partner-certifications).

## Feedback signal, with limits

An [August 28 firsthand CCAR-P account](https://www.reddit.com/r/claudeskills/comments/1w0sbla/passed_claude_architect_professional_ccarp_exam/) emphasizes building an end-to-end system and reading the blueprint, calling Professional harder than the other certificates. An [October 8 firsthand account](https://www.reddit.com/r/ClaudeAI/comments/1x0nhvy/just_passed_the_ccarp_exam/) instead describes it as fairly easy after preparation. Neither identity, reported score nor preparation efficacy is independently verified; discussion includes commercial course recommendations. These conflicting perceptions argue against manufacturing a difficulty guarantee. They support practice that connects technical choices to operational consequences.

A [Yusuf Barman certification post](https://www.linkedin.com/posts/ybarman_claude-certified-architect-professional-activity-7492807038608060418-qFE7) highlights Integration and stakeholder/governance coverage. This is corroborative study advice, not evidence about confidential item wording or frequency. Form 02 preserves all seven domains rather than becoming a technical trivia bank.

## Primary-source principles checked

[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) distinguishes explicit workflows from dynamic agents and discusses decomposition and orchestration. [Agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) supports outcome and trajectory checks, mixed graders, repeated trials and lifecycle ownership. These informed known-branch, parallel-review, workflow-recovery and evaluation decisions.

[MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) explicitly binds access tokens to intended resources, requires audience validation and describes scope challenges. [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) distinguishes deferred model-context loading from the definitions still supplied in the request catalog. Items test these boundaries rather than memorization of incidental flags.

[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) and [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) inform stable-prefix and chunk-context principles. Supplied cache prices are fictional; they are not claims about current Claude pricing. Legal scenarios cite HHS, EUR-Lex and FedRAMP references in the per-item source list and explicitly assume an established scope or decision owner, rather than asking candidates to invent legal determinations.

## Form checks

- 63 items; allocations 11/8/12/10/9/9/4; all 38 guide objectives covered.
- 38 single-response and 25 multiple-response; four select-three and 21 select-two.
- Eight tabular exhibits; four independently checked numerical decisions: Q06 $4,510 first-month contribution; Q19 21.7391304% cache break-even; Q24 2.1-second modeled critical path; Q38 94.3% workload-weighted correctness with a failing independent forged-document gate.
- Unique IDs, deterministic option shuffle and mixed item order. Every option has a rationale and each item states the decision tie-break.
- Question construction targets authority boundaries, stage diagnosis, dependency constraints, trade-offs and controlled lifecycle transitions. Benchmark gates are supplied by the scenario, not asserted as universal production thresholds.

Editorial review replaced 15 initially repetitive decision structures and tightened nine competitor sets. Revised scenarios include cache warm-up after a catalog change, resumption with stale external facts, exact evidence lost by a reranker, backup restoration replay, recovery-role rehearsal and feedback-collection bias. This reduces similarity to the first form while retaining the blueprint.
