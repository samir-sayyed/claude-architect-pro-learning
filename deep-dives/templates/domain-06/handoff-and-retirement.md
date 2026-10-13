# AI service handoff, runbook and retirement record

Service: [name]
Current owner / receiving owner: [roles]
Version and review date: [version, YYYY-MM-DD]
Approved release bundle: [immutable references]
Access process: [approved scoped process; no secrets in this file]

This original template is complete when the receiving team demonstrates the necessary actions, not when the document has been delivered.

## 1. Service contract and architecture

User journey and scope: [link]
Context / request / data / deployment views: [links]
Interfaces, trust boundaries and meaningful success states: [contracts]
Decision log and accepted constraints: [ADRs]
Dependencies, quotas, regions and retirement dates: [inventory]
Prompt, model route, index, tools, permissions and rubric versions: [release bundle]
Data retention, deletion, holds and restore obligations: [information owner-approved policy]

## 2. Detect and triage

| Symptom | User impact | Evidence location | Immediate owner | Escalation |
|---|---|---|---|---|
| Quality or safety gate failure | | | | |
| Retrieval/source failure | | | | |
| Review queue overload | | | | |
| Dependency unavailable | | | | |

Severity and stop conditions: [agreed before rollout]
Incident communication: [confirmed impact, mitigation, unknowns, next update time]
Privacy-preserving evidence capture: [minimum needed, access, expiry]

## 3. Contain, restore and reconcile

Allowed immediate containment: [e.g., feature disabled or draft-only; authority]
Fallback user path and pending-case owner: [role and behavior]
Compatible rollback bundle and how to access it: [reference]
Restore procedure: [steps plus actual environment-specific commands in the owning repo]
Verification: [known-good user journey, authorization checks, source/prompt versions and metrics]
Business reconciliation: [messages, bookings, payments or recommendations already delivered]

## 4. Receiving-role rehearsal

- [ ] Locate and understand SLOs and critical gates.
- [ ] Detect a seeded bad release and identify affected scope.
- [ ] Exercise containment with the receiving role's actual permissions.
- [ ] Retrieve/decrypt and restore the approved bundle using scoped recovery access.
- [ ] Verify the complete user path, including fallback and authorization.
- [ ] Reconcile pending work and avoid duplicate side effects.
- [ ] Reach the domain expert and escalation owner under the intended coverage model.

Result, evidence, gaps and retest date: [record]
Accepted responsibility by receiving owner: [role, date; conditional until critical gaps close]

## 5. Feedback and iteration

Feedback triage owners: [factual/content, safety, preference, policy, operations]
Label/rubric admission rules: [reviewer, scope, version, minimum data]
Regression cases and holdout checks: [references]
Rollout assignment, segmentation, gates and rollback triggers: [release plan]
Incident review trigger and corrective-action owner: [record]

## 6. Retirement

Reason, decision owner and dates: [record]
Underlying user need after retirement: [replacement or explicit supported end]
API clients / scheduled jobs / users to inform: [inventory and actionable notices]
New-work cutoff and drain plan: [pending confirmations, reviews, appeals, bookings]
Data inventory: [primary records, uploads, vectors, traces, evals, reports, workflow memory, backups]
Disposition: [approved retention, deletion and holds by data type; accountable information owner]
Restore controls: [prevent resurrection of removed records and retired workflows]
Access revocation: [tokens, tools, service accounts, unused integrations]
Redirects and replacement path: [tests]
Final verification, remaining obligations and owner: [record]
