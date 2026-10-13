# Review and measure an AI-assisted workflow

## Task contract
User outcome:
Acceptance examples and failure examples:
Permitted files, commands and side effects:
Relevant source paths and actual project commands:
Risk / test environment / rollback:

## Independent review prompt
Read the task contract, final diff and relevant surrounding code. Do not assume the
implementation narrative is true. Try to produce a concrete counterexample involving
authorization, duplicate delivery, partial failure, changed inputs, stale data or an
unexpected caller. Report only actionable findings with path, evidence and impact.
Distinguish untested concerns from reproduced failures. Do not change files.

## Pilot design
Task population and sampling rule:
Assignment to assisted and comparison workflows:
Task-complexity strata and excluded sensitive work:
Task completion definition, including review and follow-up window:
Active engineer minutes / waiting / reviewer minutes / rework:
Escaped defects and severity / successful user outcomes:
Tool cost / operational support / developer experience:
Stop criteria and owner:

## Worked arithmetic
Illustrative means for comparable tasks: baseline 70 build + 15 review + 5 rework
= 90 minutes. Assisted 45 build + 25 review + 15 rework = 85 minutes.
Net time reduction = (90 - 85) / 90 = 5.56%, before additional adoption costs.
Report variation and sample sizes; these invented values are not a study result.

## Decision
Scale, revise, or stop this particular workflow:
Evidence / uncertainty / next measurement:
