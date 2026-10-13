# Domain 6 research and evidence notes

Verified: 2026-10-13 (Asia/Kolkata). Scope: the five Stakeholder Communication & Lifecycle Management objectives in the user-supplied official CCAR-P Exam Guide, version 1.0, July 2026. The guide's blueprint was reread; its objective wording is preserved in the content metadata. The official PDF and its sample questions are not redistributed.

## Evidence method and limits

Primary guidance and first-party documentation were searched and opened, then relevant passages were read for each retained claim. This chapter combines that evidence with original architectural explanation, synthetic worked examples and a reproducible local lab. The examples are proposed product extensions, not descriptions of the current NutriMind or Krishi Mazdoor repositories. All numerical operating targets are hypothetical and require an actual owner's agreement and production-representative validation.

Source publication dates differ from verification dates. Mature Google SRE, AWS and GOV.UK guidance is retained for stable engineering principles, while the January 2026 Anthropic evaluation article and August 2026 Fin release announcement supply current AI-industry examples. Vendor case studies document what a participant says it deployed; they do not independently prove effectiveness, establish a universal benchmark or certify the reader's architecture. No live exam items, reconstructed recalled questions, commercial passing claims or unsupported difficulty claims were used.

NIST's current Core page identifies the material as AI RMF 1.0 (2023) and states that a revision is in progress. The chapter explicitly treats it as voluntary, iterative guidance, not a mandatory compliance checklist or finalized 2026 framework. Claude model deprecation documentation is dynamic; the lesson retains only the verified lifecycle/platform distinction and instructs the reader to check exact identifiers and dates for their deployment.

## Verified claims used in the chapter

### D6-S01 — GOV.UK: User research in discovery

Source: [GOV.UK: User research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery)

Discovery investigates the whole existing journey, including offline steps and broad user needs. The chapter applies this to conflicting farmer/worker incentives and a nutrition task; those worked cases are original. Published 2016; verified current page.

### D6-S02 — GOV.UK: Measuring the benefits of your service

Source: [GOV.UK: Measuring the benefits of your service](https://www.gov.uk/service-manual/measuring-success/measuring-service-benefits)

Benefits work begins with a baseline, compares options, distinguishes cashable from other benefits and tests uncertain assumptions. The adoption/correction arithmetic in the chapter is independently constructed. Published 2018; no claim that its governmental procurement rules apply universally.

### D6-S03 — NIST AI RMF Core, version 1.0

Source: [NIST AI RMF Core, version 1.0](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

AI RMF Core covers stakeholder context, accountability, continuous feedback and decommissioning. Functions are iterative and the framework is voluntary. Its current page says AI RMF 1.0 is under revision.

### D6-S04 — Anthropic: Building effective agents

Source: [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

Anthropic distinguishes predetermined workflows from dynamic agents and advises increasing complexity when justified by task performance. The support architecture table and feasibility reasoning are original, not Anthropic benchmark results. Originally published December 2024; current page was read.

### D6-S05 — AWS Prescriptive Guidance: Architectural decision record process

Source: [AWS Prescriptive Guidance: Architectural decision record process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

AWS ADR process preserves context, decision and consequences; accepted decisions are superseded through new reviewed records. The marketplace ADR and all templates are original. This is one explicit ADR process, not a claim that all organizations mandate the same workflow.

### D6-S06 — Google SRE: Service level objectives

Source: [Google SRE: Service level objectives](https://sre.google/sre-book/service-level-objectives/)

SLIs measure a service property, SLOs set targets and SLAs include specified consequences and terms. Business/product considerations inform agreements. The chapter does not offer a legal opinion about a proposed contract.

### D6-S07 — Google SRE Workbook: Implementing SLOs

Source: [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)

SLOs can use good-event ratios with explicit measurement implementations and time windows. Stakeholder agreement is necessary for the indicators to drive priorities. The AI-specific correctness/coverage table is original application, not copied Google targets.

### D6-S08 — Google SRE Workbook: Example error budget policy

Source: [Google SRE Workbook: Example error budget policy](https://sre.google/workbook/error-budget-policy/)

A documented error-budget policy can prioritize reliability over ordinary feature work after budget consumption. The chapter explains the purpose without prescribing Google's sample thresholds as universal rules.

### D6-S09 — Intercom/Fin: Reporting metrics and attributes

Source: [Intercom/Fin: Reporting metrics and attributes](https://www.intercom.com/help/en/articles/7022438-reporting-metrics-attributes)

Current Fin metrics distinguish involved conversations, resolutions, automation and procedure handoffs. Resolution can be confirmed or assumed; outcome can include a configured handoff. Definitions have changed over time. The lesson uses this to explain denominator/meaning alignment, not to rank providers or assert their marketing resolution rate.

### D6-S10 — Anthropic: Demystifying evals for AI agents

Source: [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

Anthropic describes code-based, model-based and human graders, human calibration, transcript review and long-term regression evaluation. Published 2026-01-09. The selection-bias case, feedback admission boundary and labels are original practical applications.

### D6-S11 — Google SRE: Evolving the SRE engagement model

Source: [Google SRE: Evolving the SRE engagement model](https://sre.google/sre-book/evolving-sre-engagement-model/)

Google describes production readiness reviews and acceptance of production operating responsibility. The chapter applies the principle to a small team and tests actual receiving-role capability rather than equating document delivery with readiness.

### D6-S12 — Anthropic customer account: Thomson Reuters

Source: [Anthropic customer account: Thomson Reuters](https://claude.com/customers/thomson-reuters)

The Anthropic-published Thomson Reuters account describes expert validation, RAG and integration with its established enterprise deployment stack. It redirects to claude.com. Historical model names and quoted time-saving impressions are not used as current model recommendations or measured general performance.

### D6-S13 — Fin: Announcing Evals and Releases, 13 August 2026

Source: [Fin: Announcing Evals and Releases, 13 August 2026](https://www.intercom.com/blog/announcing-evals-and-releases)

Fin announced Evals and Releases on 2026-08-13, describing simulations, bundled content/procedure/guidance changes, controlled rollout/A-B testing, monitoring and rollback. Retained as a current product capability example; not independent proof of accuracy or superiority.

### D6-S14 — Google SRE Workbook: Canarying releases

Source: [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)

Google canary guidance discusses representative size/duration, traffic mix, time of day and contamination from overlapping changes. The distinction between limiting exposure and estimating comparative effects is the chapter's explicit engineering explanation.

### D6-S15 — Claude Platform Docs: Model deprecations

Source: [Claude Platform Docs: Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)

Current Claude Platform docs define retired models as unavailable and state that partner-operated platforms can use different retirement schedules. The chapter deliberately avoids hardcoding a model recommendation or retirement date.

### D6-S16 — Google SRE: Postmortem culture

Source: [Google SRE: Postmortem culture](https://sre.google/sre-book/postmortem-culture/)

Google's postmortem guidance recommends pre-agreed triggers, contributing-cause analysis and reviewed corrective actions. The nutrition incident and runbook structure are original illustrative scenarios.

### D6-S17 — GOV.UK: Retiring your service

Source: [GOV.UK: Retiring your service](https://www.gov.uk/service-manual/agile-delivery/retiring-your-service)

GOV.UK retirement guidance considers continuing user needs, consumer/API migration and continued information protection. Published 2016, page updated 2025-08-26. The chapter extends the inventory to AI-derived stores and pending work, while leaving actual retention/hold rules to the accountable information owner.

### D6-S18 — GOV.UK: How to set performance metrics for your service

Source: [GOV.UK: How to set performance metrics for your service](https://www.gov.uk/service-manual/measuring-success/how-to-set-performance-metrics-for-your-service)

Performance guidance combines metrics with research, uses hypotheses and considers segments and time context. The changed rating-exposure example is original and does not purport to describe a named vendor's practice.

### D6-S19 — Google SRE Workbook: Alerting on SLOs

Source: [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/)

SRE burn-rate guidance relates observed error rate to permitted budget rate and discusses alert timing/noise trade-offs. All incident figures and the 8× and 2.5× worked calculations are independently authored.

## Objective coverage

- 6.1 discovery and requirements: sections 1–2 plus lab steps 1–2.
- 6.2 decisions and trade-offs: sections 2–4 plus the ADR lab.
- 6.3 feedback, alignment and SLAs: sections 2, 5–6, 8–9 and the measurement lab.
- 6.4 documentation and implementation guidance: sections 4–5, 7–8 and downloadable templates.
- 6.5 lifecycle: sections 6–10, receiving-role readiness, release gates, migration and retirement.

The objective IDs are local ordinal references to the five bullets in the guide; the guide itself does not number them this way.

## Independent arithmetic and fixture checks

- Architecture feasibility: B violates p95, C violates correctness, D violates region; E dominates A on the stated dimensions. Question 3 explicitly states that A/B/C/E use the approved region.
- Capacity value: 8,000 × 60% × (4 − 1) / 60 = 240 staff-hours. At $25/hour less $1,500 operating cost, modeled net capacity value is $4,500, not automatically cash savings. At 30% adoption, net value is $1,500; at 30% adoption and 3-minute corrections it is −$500.
- Quality versus coverage: 570/600 = 95%, 600/1,000 = 60%, 570/1,000 = 57%. Check 5 compares release B: 388/400 = 97%, 400/1,000 = 40%, 388/1,000 = 38.8%.
- Tail example: 95 × 2 seconds + 5 × 20 seconds gives mean 2.9 seconds. Nearest-rank p95 is 2 seconds and p99 is 20 seconds.
- Request budget: 20,000 × 0.5% = 100; 40 failures leave 60. Incident 20/500 = 4%, divided by 0.5% gives 8× burn, and spends 20 events.
- Check 7: 50,000 × 0.2% = 100; 30 + 10 failures leave 60. Incident 10/2,000 = 0.5%; 0.5/0.2 = 2.5× burn.
- Queue illustration: 60 arrivals/hour − 45 completions/hour = 15 additional pending tasks/hour, under the stated simplified steady-rate assumptions; not a p95-wait estimator.
- Synthetic CSV: release A availability 95%, fast-response ratio 90%, answer coverage 80%, conditional correctness 93.75%, timely required review 100%, critical violations 0. Release B: 100%, 95%, 90%, 88.89%, 50%, 1. The code embedded in the chapter was extracted, HTML-unescaped and executed against the CSV; every assertion passed.

## What remains unverified

The synthetic lab and teaching thresholds do not establish a production SLA, causal business result, legal compliance, fairness guarantee or exam pass prediction. No actual project integration, production load, full two-hour exam behavior or independent audit of vendor claims was attempted. The parent task owns shared rendering, accessibility/browser checks and publication.
