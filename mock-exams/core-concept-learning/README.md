# Core Concept Learning · Original video companion exams

Five separate 63-question, 120-minute exams (315 original scored questions), based on concepts across [all ten CCAR-P walkthroughs](https://www.youtube.com/playlist?list=PLNyAiuHx7c5c) by [Core Concept Learning](https://www.youtube.com/@coreconceptlearning).

Open `sets.html` to choose a sitting. Each covers all 38 objectives in the supplied July 2026 Professional guide with domain counts 11/8/12/10/9/9/4. Each has 38 single-answer, 21 select-two and four select-three questions. Two Yes/No matrices and a repeatable matching drill appear after submission and are unscored. This format mix is our practice design, not an official live-exam specification.

- Set 01: concepts from source exams 01–03, 21 questions per video.
- Set 02: source exams 04–06, 21 questions per video.
- Set 03: source exams 07–10, 16/16/16/15 questions respectively.
- Set 04: Video 04 only, one original question grounded in each of its 63 question chapters.
- Set 05: Video 05 only, one original question grounded in each of its 63 question chapters.

Sets 01–03 are mixed companions. Sets 04–05 begin single-video coverage without changing those earlier forms. No further sets are created until requested. Source chapters are conceptual references; the original questions and options are not reproduced.

The timer continues across reloads and closure. Storage is local to the browser and each form has a distinct version key. Use the printable questions if browser storage or scripting is unavailable. Option explanations, decisive constraints, primary sources and timestamped conceptual credits are available after submission; reference pages contain spoilers.

## Attribution and limits

The source playlist and chapter metadata were inspected and complete English captions reviewed. The source material is an unofficial practice series. These scenarios and options are original, not reproductions of its question bank. No full transcripts, original slides or official PDF are distributed. Attribution does not grant permission to copy source material. There is no affiliation or endorsement by the channel, Anthropic or other cited providers.

Technical claims were checked against primary documentation on 18 October 2026. Read each research note for corrections, evidence and limits. Scenario metrics and exercise configurations are fictional. Raw scores have no validated conversion to the official scaled passing score. We cannot establish equivalence to live-exam difficulty.

The ZIP contains self-contained HTML pages, question data, source metadata and research notes. The exams work offline; external references require internet. No analytics, login or API calls.

## Rebuild from the repository

Run `python3 mock-exams/core-concept-learning/build.py` from the site root, then `node mock-exams/core-concept-learning/test.js`. The builder uses the existing `mock-exams/ccar-p/` runtime, stylesheet and template. Authoritative content is in `content/`; rendered copies are in `sets/`.
