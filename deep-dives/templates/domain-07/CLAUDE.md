# Learning sandbox instructions

This is an offline Python retry lab, not a production payment service.
Use Python 3.9 or newer. No package install, API account, network, secrets or real money.

## Repository map
- `lab.py`: toy provider, checkout retry loop, business-invariant checks.
- `incident-runbook.md`: incident evidence and containment worksheet.
- `review-and-measure.md`: independent review and pilot measurement worksheet.

## Work sequence
Read the relevant caller and the invariant before proposing a change.
Run `python3 lab.py buggy` to reproduce the intentional failure.
Run `python3 lab.py fixed` to verify the reference behavior.
Expected red: duplicate charges for one intent; expected green: all four named checks pass.
Do not weaken the invariant, delete the failing assertion, or invent successful output.
Report exact command, exit status, behavior, changed files, and unresolved limits.

## Boundaries
Do not paste credentials, patient information, or production logs into this exercise.
Do not publish, deploy, send messages, or alter an external service for this task.
These instructions guide the model; they do not enforce filesystem or network isolation.
The example settings file is inert until deliberately installed and reviewed.
