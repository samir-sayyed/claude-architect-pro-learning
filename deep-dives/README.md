# Domains 5–7: practical architecture learning

Open **[index.html](index.html)** for the learning path and connected capstone. Each domain page is self-contained and runs offline, with source links requiring internet.

- [Domain 5 — Governance, Safety & Risk Management](domain-05.html)
- [Domain 6 — Stakeholder Communication & Lifecycle Management](domain-06.html)
- [Domain 7 — Developer Productivity & Operational Enablement](domain-07.html)

The modules teach all 13 objective bullets in these domains of the user-supplied CCAR-P guide v1.0, effective July 2026. Weights are 14%, 14% and 7%. Numbers such as 5.1 are local ordinal study labels, not official objective numbering. This material is separate from the Foundations exam and the episode collection.

Each module includes substantial explanations, original project cases, diagrams, tricky distinctions, ten original decision checks with explanations for all four options, a glossary, a synthetic hands-on lab and downloadable templates. The index connects them in one capstone. The capacity and event-budget calculators explain their assumptions and reject invalid input.

## Use it actively

1. Choose a hypothetical project extension and write its outcome, users and consequence of error.
2. Read a mechanism and redraw its diagram without looking.
3. Change one assumption in the example and explain which decision must change.
4. Complete the synthetic lab and templates; verify actual outcomes rather than document completion.
5. Answer a decision check before revealing all four rationales.
6. Have a second person reproduce your evidence and operating procedure.

Section-completion marks use browser-local storage, independently per domain. They are a reading aid, not a competence score. Storage can be unavailable or behave differently with local files. Checks remain usable without saving. No learner content is sent to a service. The pages have no account, telemetry, provider API calls or external runtime dependencies. Printing expands explanations temporarily and restores folded sections afterwards.

## Evidence and limits

Research edition: **13 October 2026**. Each section links supporting primary sources; `research/` records what was verified and its limitations. Product configuration and legal/regulatory material must be rechecked when used in a real deployment. Legal applicability, roles and approved controls depend on the organization and use case. Illustrative configurations and policies are teaching examples, not a compliance certification or a ready-to-deploy security boundary.

NutriMind-, marketplace- and Android-inspired examples are proposed teaching scenarios. They do not claim current project implementation, deployed incidents or validated production thresholds. Vendor case studies and research findings are described within their reported context, not universal benchmarks. No live exam questions are reproduced, and the material has no verified live-exam difficulty calibration or score guarantee.

Original educational content, independent of and unaffiliated with Anthropic or other cited organizations. The supplied official PDF is not distributed. Existing Peace Of Code / aakash1999 course attribution remains in the separate episode section; these domain tutorials use their own cited primary-source research.

## Rebuild and verify

Python 3 and Node.js suffice; no packages need installing.

```sh
python3 deep-dives/build.py
node deep-dives/test.js
```

The generator validates objective coverage, substantive module lengths, cited sections, source usage, diagrams, check structure, unique HTML IDs and local targets, and checks ZIP entries against final file bytes. It produces four portable HTML pages, `templates.zip`, and `domain-05-07-learning.zip`. The offline bundle includes the rendered pages, linked templates and research notes; clone the public repository for generator source and rebuild commands. Source documentation requires internet. Python labs in templates are educational fixtures and are not executed by opening a page.
