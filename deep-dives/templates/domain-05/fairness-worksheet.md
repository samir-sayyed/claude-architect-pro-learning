# Fairness, transparency and recourse worksheet

Original worksheet for a specific decision. Synthetic numbers below are teaching examples, not population findings.

## Decision and harm

- Decision (for example, recommendation for a job with stated requirements): [ ]
- Affected person and harm of false positive / false negative / abstention / delay: [ ]
- Legitimate factors and factors that must not drive this decision: [ ]
- Label source, independent assessment and known selection bias: [ ]
- Who helped define the policy, including affected users: [ ]
- Audit-data purpose, lawful handling, safeguards and access limits: [ ]

## Measure the complete service

| Stage | Comparison/slice | Metric + denominator | Sample size / uncertainty | Investigation or mitigation owner |
|---|---|---|---|---|
| Input/source availability | [ ] | [ ] | [ ] | [ ] |
| Retrieval/ranking | [ ] | Recall or relevant recommendation outcome | [ ] | [ ] |
| Answer/abstention | [ ] | Accepted accuracy AND coverage | [ ] | [ ] |
| Human review | [ ] | Queue age, disagreement, adjudicated error | [ ] | [ ] |
| Final outcome | [ ] | Suitable opportunities delivered / completed | [ ] | [ ] |
| Appeal/accessibility | [ ] | Reachability, correction, time to resolution | [ ] | [ ] |

## Arithmetic fixture

| Quantity | Group A | Group B |
|---|---|---|
| Total | 1,000 | 1,000 |
| Independently meets requirements | 200 | 100 |
| Does not meet requirements | 800 | 900 |
| True-positive rate | 80% | 80% |
| False-positive rate | 10% | 10% |
| True positives | 160 | 80 |
| False positives | 80 | 90 |
| False negatives | 40 | 20 |
| Precision = TP / (TP + FP) | 66.7% | 47.1% |
| Selection rate = (TP + FP) / total | 24% | 17% |

Explain why equal error rates do not yield equal precision in this fixture: [ ].

Chosen fairness objective(s), context and rationale: [ ]. Competing objective or unresolved trade-off: [ ]. Label assumptions that could invalidate the conclusion: [ ]. A metric that improved while service got worse: [ ].

## Paired test

Hold legitimate skills, requirements and availability fixed. Change one irrelevant synthetic field. Compare recommendation, explanation, review route and timing. Expected invariant: [ ]. Observed difference: [ ]. Investigation: [ ]. This test does not prove fairness for every real case.

## User-facing explanation and appeal

Explain AI involvement, actual decision reason, evidence/limitations and how to correct relevant data. Do not use a generated rationale as proof of causation. Example: “This job requires a licence absent from the verified profile; update the record or request review.”

- User explanation and accessible language: [ ]
- Correction/appeal route and empowered owner: [ ]
- Response expectation and overflow handling: [ ]
- How appeals affect evaluation labels after adjudication: [ ]

Reference: [NIST SP 1270](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf). Formal fairness goals may conflict under particular assumptions; do not turn that fact into a claim that fairer design is impossible.
