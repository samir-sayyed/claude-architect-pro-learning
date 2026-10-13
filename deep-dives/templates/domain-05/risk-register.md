# AI risk register and release decision

Template for an actual design review. Example entries are hypothetical. Replace brackets with discovered facts; do not interpret a completed table as compliance certification.

## Scope and authority

- System and version: [ ]
- Intended benefit and users: [ ]
- Affected people who are not direct users: [ ]
- Permitted purpose and supported decisions: [ ]
- Actions the system may propose: [ ]
- Actions the system may execute; authoritative executor: [ ]
- Explicitly excluded decisions: [ ]
- Accountable release owner; security/privacy/domain reviewers: [ ]
- Model, prompt, source, tool, policy and environment versions: [ ]

## Risks

Write: trigger → failure → consequence → affected person. An ordinal priority score is a sorting aid, not a measured probability.

| ID | Causal risk | Severity / likelihood and basis | Preventive control + enforcing boundary | Detection / recovery | Owner | Evidence, conditions and limits | Residual risk / acceptance |
|---|---|---|---|---|---|---|---|
| R-01 | Imported recipe lacks verified ingredients → assistant gives suitability badge → user relies on unsupported claim | [ ] | Verified source required at badge generator; missing evidence withholds badge | Sample delivered badges; remove incorrect badge and notify appropriate owner | [ ] | Incomplete-source fixture; excludes clinical validation | [ ] |
| R-02 | Poisoned job text → proposed unrelated profile export → privacy harm | [ ] | No unrelated export authority; executor checks session actor, resource and purpose | Denial event without sensitive payload; incident containment | [ ] | Injection plus backend side-effect tests | [ ] |
| R-03 | Sparse language evidence → frequent abstention → delayed access to opportunities | [ ] | Validated language support and feasible alternative route | Coverage and wait by slice; worker correction/appeal | [ ] | Counts, label quality, small-sample limits | [ ] |

## Release gates

Specify a threshold, measurement window, denominator and owner for each gate. Separate severe escape events from ordinary quality averages.

| Gate | Required evidence | Stop / rollback trigger | Responsible person |
|---|---|---|---|
| Data access | Cross-tenant and revoked-user integration tests | Unauthorized read/write | [ ] |
| Consequential output | Evidence validity and specialist review where required | Unsupported claim delivered | [ ] |
| Review operation | Realistic demand, availability, queue-age measurements | Required review cannot be completed safely | [ ] |
| Rights/recovery | Scoped deletion and quarantined restore evidence | Eligible record returns to live service | [ ] |
| Fairness/recourse | Relevant outcomes, coverage, waiting and appeal results | Unresolved unacceptable exclusion | [ ] |

## Decision record

Decision: [go / limited pilot / pause / no-go].

Evidence supporting the decision: [ ]. Unmeasured risks: [ ]. Compensating controls: [ ]. Residual-risk owner and rationale: [ ]. Expiry/review date: [ ]. Reopen when model, tools, sources, purpose, user population or processing boundary changes: [ ].

Reference: [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). The template is original and uses the framework as an organizing aid.
