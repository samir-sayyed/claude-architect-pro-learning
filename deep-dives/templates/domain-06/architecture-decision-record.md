# ADR-[number]: [specific architecture decision]

Status: Proposed / Accepted / Rejected / Superseded
Author and accountable owner: [roles]
Reviewers: [domain, product, engineering, operations, risk roles as relevant]
Date and version: [YYYY-MM-DD, version]
Supersedes / superseded by: [record links]

This is an original working template. Keep accepted reasoning as history; propose a reviewed superseding record when the decision changes.

## Context and decision required

[User outcome, task, present problem and why a decision is needed now.]

Binding constraints: [scope, access, region, safety, review, capacity]
Evidence: [dataset/rubric versions, period, population, uncertainty]
Unknowns: [which assumption could invalidate the choice]

## Feasible alternatives

| Alternative | Outcome / quality | Latency | Full operating cost | Constraint fit | Important consequence |
|---|---|---|---|---|---|
| Current or non-AI approach | | | | | |
| Proposed option | | | | | |
| Credible alternative | | | | | |

Eliminate prohibited options before ranking. State whether differences are measured, estimated or unknown. Include human correction/review effort and operating ownership.

## Decision

[Choose one specific behavior/architecture and its authorized boundary.]

Why this meets the constraints: [evidence]
Why the other feasible option was not chosen: [actual trade-off]
Sensitivity: [what happens if adoption, correction effort, demand or dependency reliability changes]
What would change this decision: [explicit trigger]

## Consequences and implementation guidance

Benefits: [expected outcome, not a benchmark guarantee]
Accepted costs and remaining risks: [owner and authority]
Required interface/state changes: [contract references]
Fallback, rollback and business compensation: [distinguish configuration from already-completed actions]
Acceptance and negative tests: [links or concrete cases]

## Review and lifecycle

Owner acceptance and date: [record]
Release bundle and validation evidence: [references]
Operational readiness / receiving owner: [reference]
Review trigger or date: [e.g., SLO miss, new scope, dependency retirement]

## Audience-specific communication

Sponsor: [outcome, cost range, decision and uncertainty]
Builder: [contract, boundaries, versions and checks]
Operator: [detection, containment, recovery and escalation]
