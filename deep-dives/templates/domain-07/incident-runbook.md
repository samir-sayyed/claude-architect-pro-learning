# AI-assisted incident worksheet

Example, reviewed 2026-10-13. Adapt the owners, access and contracts to your system.

## Declare and contain
- Incident owner / start time / severity / affected user journey:
- Impact numerator and denominator / measurement window:
- Approved read-only observations:
- Write actions requiring authorization / approving person / rollback:
- Reversible containment and resulting service trade-off:

## Reconstruct one failed operation
- Trace ID / business operation ID / deployment version:
- Authentication and authorization verdict, without token values:
- Retrieval source IDs and versions, without sensitive content:
- Model request ID / model configuration / timeout budget:
- Tool input schema verdict / transport outcome / business outcome:
- Retry count / stable idempotency reference / reconciliation status:
- User-visible result and verified external state:

## Test competing hypotheses
| Hypothesis | Evidence that would support it | Safe discriminating observation | Result |
| --- | --- | --- | --- |
| Local runtime/configuration | Failure isolated to one machine or version | Compare approved version and loaded settings | |
| Authentication/authorization | Credential or scope error | Check sanitized status and audience verdict | |
| Provider/rate limit | Provider error or broad shared failure | Check request IDs, error category and official status | |
| Retrieval/data version | Evidence missing, stale or wrong tenant | Check source IDs, versions and access decision | |
| Tool/application semantics | HTTP succeeded but business action failed | Compare response schema, status and external state | |

## Support bundle
Share only a minimal synthetic reproducer, relevant versions, sanitized timestamps,
error categories and request IDs through the approved private support channel.
Review all contents manually. Exclude credentials, raw prompts, patient/customer
data, complete transcripts, environment dumps and heap snapshots.

## Recover and learn
- Fix / targeted regression / independent review / rollback criteria:
- Evidence that safe user behavior is restored:
- Backlog reconciliation / duplicate side effects / notification owner:
- Preventive control and runbook change / owner / due date:
