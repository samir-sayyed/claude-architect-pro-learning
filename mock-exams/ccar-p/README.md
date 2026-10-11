# Claude Architect Professional — Original Mock Exam

Open **index.html** in a modern browser. The full exam runs offline with no API, sign-in, analytics or external assets. Keep the companion files together for navigation. The ZIP is a portable study pack.

- 63 scored questions, 120 uninterrupted minutes.
- 38 single-answer and 25 multiple-response questions, including select-two and select-three.
- All 38 objectives in the attached official CCAR-P guide v1.0, effective July 2026.
- Nearest whole-question domain allocation: 11 / 8 / 12 / 10 / 9 / 9 / 4.
- Flags, return navigation, browser-local saved progress, expiry submission and result export.
- Explained correct answers **and every distractor**, with source links and objective mappings.
- Two independent Yes/No matrices and one repeatable-option matching drill after submission; supplemental and unscored.

## Companion pages

- `blueprint.html`: complete objective-to-question mapping.
- `questions.html`: print-friendly questions only, same order as the exam.
- `answer-key.html`: full explanations (spoilers).
- `research.html`: readable evidence, sources, attribution and limitations.
- `research-feedback.md`: ten firsthand accounts, dates, credibility and exclusions.
- `research-notes.md`: official mechanics, source hierarchy and design decisions.
- `exam-data.json`: editable original question bank, option rationales and mapping.

## Scoring and timing

Exact correct response sets earn one point. No partial credit or negative marking in this mock. Unanswered/incomplete items earn zero. This is a practice convention: the guide does not disclose the live exam’s partial-credit policy or raw-to-scaled conversion. **720/1,000 is a scaled passing standard, not a raw 72% cutoff.** No official pass/fail prediction is provided.

The timer uses an absolute browser deadline and continues while the tab is closed. If the browser suspends the page, expiry is enforced on the next timer tick or when reopened. Saved progress is validated before loading. Local-file storage behavior varies by browser; if unavailable, keep the tab open. Use one tab for a sitting. Reset is available after submission and requires an explicit UI confirmation. Retakes use the same form, so familiarity may raise scores.

## Sources and independence

The attached **Claude Certified Architect – Professional Exam Guide, version 1.0 (July 2026)** controls scope. [Anthropic guide directory](https://anthropic-partners.skilljar.com/page/partner-certifications), [official certification announcement](https://claude.com/resources/articles/four-role-based-claude-certifications).

User-supplied sample references: [FlashGenius quick-start](https://flashgenius.net/sample-tests/ccar-p/quick-start), [Claude Mock Exams samples](https://claudemockexams.com/architect-professional/sample-questions). They informed visible item style; none of their questions or explanations were copied.

Public feedback spans Reddit, LinkedIn, Qiita, Zenn, DEV and GitHub; full attribution is in the research pages. Technical principles were checked against Anthropic, Claude Code, MCP, HHS, EUR-Lex and FedRAMP primary sources. The prior Peace Of Code learning course is a separate companion; this exam extends to governance, lifecycle and enablement beyond its eleven episodes.

Questions and explanations are original practice material. Independent and unaffiliated with Anthropic or the source providers. No leaked/reconstructed live questions, original decks, videos, full transcripts or official PDF are distributed in the pack. Scenario numbers, model labels and exercise rates are fictional and supplied in the stems.

**Difficulty is deliberately demanding but not calibrated against live items.** Public candidate reports conflict and do not establish exact equivalence, a pass prediction or a universal item-format mix. Research date: 2026-10-11. Scope is pinned to guide v1.0; changing product specs need re-verification.

## Rebuild and checks

Python 3 standard library only:

```sh
python3 build.py
node test.js
```

Edit `exam-data.json` for content; `template.html`, `exam.css` and `exam.js` for the experience. Build checks cover counts, allocation, objective coverage, required selections, citations, IDs, local links, standalone dependencies and ZIP byte matches. Node assertions cover exact scoring, invalid saved state, selection limits and expiry arithmetic. Browser verification covers the interactive flow and responsive layout.
