# AI service-level measurement and operating contract

Service and supported user journey: [name, actor, start/end]
Owner: [accountable role]
Operating owner and staffed hours: [role, timezone and coverage]
Status: Proposed / Accepted
Version and review date: [version, YYYY-MM-DD]

This original template helps define SLIs, SLOs and proposed SLA terms. Example targets in the learning chapter are teaching fixtures; negotiate and validate your own. An internal target alone is not a contractual SLA.

## Scope and measurement boundary

Eligible population: [authenticated actors, tasks, channels, languages]
Exclusions and rationale agreed in advance: [explicit and inspectable]
Observation point: [client, gateway, application, workflow state]
Time start/end: [request accepted to usable response, review accepted, etc.]
Dependency failures: [how they count from the user's perspective]
Timeout, cancellation, retry and deduplication rules: [define once per logical task where appropriate]
Window: [rolling/calendar, exact length, timezone]
Telemetry gaps: [measurement uncertainty and owner]

## Indicators and targets

| Indicator | Good-event numerator | Full denominator | Target | Window and segments | Evidence owner |
|---|---|---|---|---|---|
| Availability | | | | | |
| Latency within threshold | | | | | |
| Answer correctness | | reviewed answered sample | | sampling/rubric versions | |
| Answer coverage | eligible tasks receiving an answer | all eligible tasks | | | |
| Required escalation timeliness | | all required escalations | | service hours | |
| Critical safety condition | [define independent gate] | [count / applicable population] | | | |

Quality sampling: [representative method, language/task slices, sample size and uncertainty]
Abstention meaning and fallback outcome: [safe handoff versus abandoned/unresolved work]
Quantile convention and timeouts: [do not average p95 values]

## Error budget and response policy

Budget for a completed request-based window = eligible attempts × (1 − availability target).
Burn rate = observed bad-event fraction / allowed bad-event fraction.

Illustrative self-check: 20,000 attempts at 99.5% permits 100 bad attempts. Forty failures leave 60. An incident with 20 failures / 500 attempts has 8× burn relative to 0.5% allowed, and spends 20 events. This does not mean the budget is exhausted.

Release halt / containment trigger: [condition, accountable role]
Reliability-priority trigger: [condition and agreed action]
Exception authority, expiry and evidence: [role, deadline, record]
Alert policy: [observation windows, volume, severity and response time]

## Review queue and dependency commitments

Arrival rate, service capacity and peak assumptions: [measured, not only averages]
Admission limits and overflow path: [who handles excess work]
Fallback and recovery: [scope, owner and expected user experience]
Dependency agreements and documented limitations: [provider terms do not automatically cover the full journey]

## Proposed SLA terms, if required

Customer promise and scope: [business/legal owner review]
Measurement and dispute process: [agreed evidence]
Consequences of a specified miss: [credits, escalation or other agreed terms]
Exclusions and maintenance terms: [agreed and transparent]
Notification/update policy: [audience and timing]
Accepted by product, operations and authorized contractual owner: [roles and dates]
