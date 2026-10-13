# Human review and approval policy

Original template. All example routes are hypothetical product policies, not clinical or legal conclusions.

## Decision and consequence

- Decision supported: [ ]
- Consequence the reviewer can prevent: [ ]
- Affected person and alternative route: [ ]
- Automatic handling explicitly permitted: [ ]
- Mandatory review triggers and why: [ ]
- Unsupported/out-of-scope cases: [withhold, redirect or stop; specify]
- Review owner and qualified backup: [ ]

## Routes

| Route | Entry condition | Reviewer authority and expertise | Evidence required | Deadline / overflow |
|---|---|---|---|---|
| Routine formatting | No consequential content change | Automated checks under approved scope | Schema, rendering, source integrity | [ ] |
| Consequential claim | Required by product policy | Qualified domain reviewer may edit/reject | Original evidence, conflicts, missing fields, proposed claim | Withhold until safely resolved |
| User-authorized disclosure | Precise recipient and fields ready | Authenticated user controls this disclosure | Recipient, data fields, purpose, consequences | Pending; never approve on timeout |
| Appeal or disputed exclusion | User challenges outcome | Operational reviewer empowered to correct | Actual reason, relevant records and prior decisions | [accessible route, queue-age target]

## Review interface

Show exact consequential changes first. Separate evidence from model suggestions. Display missing evidence, source date/version and conflict. Provide approve, edit, reject and escalate controls. Explain the consequences of approval. Do not make a generated rationale the authoritative record.

## Approval binding and execution

Store the canonical proposal or its securely computed hash, action type, resource identifier and version, recipient, allowed fields/amount, reviewer identity and authority, approval time and expiry. Protect the record from model edits.

Immediately before applying, verify:

1. The authenticated actor still has the required permission.
2. The resource is still inside the actor's allowed scope.
3. The proposed consequence matches the approved content.
4. The resource state and policy version remain applicable.
5. Approval is from an authorized person and has not expired.
6. The operation has not already completed; reconcile ambiguous retries.

Changed recipient, added data fields, increased amount or material resource change: require a new decision. A valid approval does not override denied access.

## Staffing and failure behavior

- Incoming cases/hour and peak pattern: [ ]
- Review fraction by route: [ ]
- Review arrival rate = incoming × fraction: [ ]
- Qualified reviewers available, duties and absence coverage: [ ]
- Mean and tail review duration: [ ]
- Ideal capacity = reviewers × 60 / mean minutes: [ ]
- Measured queue age by risk class and language/access needs: [ ]
- Approved admission/pause/fallback response: [ ]

A workload ratio below one does not establish a p95 SLA. Use realistic variability, peak demand and reviewer availability. Timeout, missing reviewer, tool outage or changed evidence must not silently become approval.

## Quality feedback

Sample approved, rejected and abstained cases. Adjudicate disagreement with appropriate expertise. Record error causes, not just button counts. Review automation bias and review-access barriers. Add validated findings to a versioned evaluation set before changing routing.
