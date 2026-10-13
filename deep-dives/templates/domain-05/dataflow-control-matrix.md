# AI dataflow and shared-control matrix

Original engineering template. Scope and retention decisions must be supplied by the responsible organization; this worksheet does not establish legal applicability.

## Deployment assumptions

- Purpose, actors, affected people and jurisdictions: [ ]
- Privacy/legal applicability assessment owner and decision reference: [ ]
- Controller/processor and, where applicable, covered entity/BA relationships: [ ]
- Exact provider offering, endpoint, region and contractual scope: [ ]
- Additional services, subprocessors and connectors: [ ]
- Permitted sensitive fields and prohibited fields: [ ]

## Every data copy

| Stage or copy | Minimum fields and purpose | Identity / permitted reader | Storage, region, vendor | Retention + basis owner | Rights/erasure path | Test evidence |
|---|---|---|---|---|---|---|
| Original record | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Model request | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Retrieved chunks | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Summary / embedding | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Prompt/result cache | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Trace / support export | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Backup / restored system | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Keep lineage so derived copies can be located. Pseudonymous identifiers and encrypted text are not automatically anonymous or outside scope.

## Who operates each control?

| Control | Provider / application / customer / shared | Exact boundary and dependency | Evidence supplied | Test we own | Failure / escalation owner |
|---|---|---|---|---|---|
| Session authentication | [ ] | [ ] | [ ] | [ ] | [ ] |
| Resource-level authorization | [ ] | [ ] | [ ] | [ ] | [ ] |
| Model/tool service identity | [ ] | [ ] | [ ] | [ ] | [ ] |
| Encryption + key recovery | [ ] | [ ] | [ ] | [ ] | [ ] |
| Audit without excess payload | [ ] | [ ] | [ ] | [ ] | [ ] |
| Rights request + vendor completion | [ ] | [ ] | [ ] | [ ] | [ ] |
| Restore and erasure replay | [ ] | [ ] | [ ] | [ ] | [ ] |
| Incident response / notification | [ ] | [ ] | [ ] | [ ] | [ ] |
| Availability and safe degradation | [ ] | [ ] | [ ] | [ ] | [ ] |

## Scoped erasure exercise

Record an authorized determination: eligible records [ ], justified retained records and purposes [ ], responsible decision maker [ ]. Verify live stores, derived indexes, caches and processors. For backups, document the approved retention and restore procedure; test a quarantined restore before it returns to use. Keep any erasure-tracking record minimal, protected and subject to its own justified retention.

## Boundary-change review

Before adding a tracing service, external model, connector, support export or new purpose, ask: what new data leaves which boundary, which party receives it, which controls still apply, and which approval must be revisited?

Primary references: [EDPB controller/processor guidance](https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en), [HHS cloud guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html), [FedRAMP 2026 agency use](https://www.fedramp.gov/2026/agencies/use/).
