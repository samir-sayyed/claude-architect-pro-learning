# Claude Architect Professional — Learning & Practice

Independent visual learning pages and an original, timed CCAR-P mock exam.

**[Open the home page](index.html)** after cloning or downloading the repository. Each section also has its own portable ZIP; extract it and open its `index.html` in a modern browser.

| Section | Open | Offline download |
|---|---|---|
| Eleven episode learning pages | [Course index](learning/index.html) | [Learning ZIP](learning/claude-architect-pro-learning-pages.zip) |
| 63-question, 120-minute mock exam | [Start the mock](mock-exams/ccar-p/index.html) | [Exam ZIP](mock-exams/ccar-p/ccarp-professional-mock.zip) |

## Repository layout

```text
index.html                 Home page linking both sections
build.py                   Rebuild both sections and verify local navigation
learning/                  Episode pages, course data, generator, previews and ZIP
mock-exams/
  ccar-p/                  Timed exam, question data, code, tests and research
ep01-...html … ep11-...html  Redirects preserving the original episode URLs
```

The root `index.html` now opens the study home. The original course index is in `learning/`. Downloads, data files and previews have moved into their section folders. The original root episode URLs redirect to their corresponding learning pages.

## Learning pages

Each episode includes a concept map, process flow, decision table, worked example and checklist. The collection has 55 core takeaways and 39 source-linked slide detail cards. Episode 11 includes an editable cost calculator with illustrative rates. See [course details and attribution](learning/README.md).

Source credits: [Peace Of Code's supplied playlist](https://youtube.com/playlist?list=PLPsBalbS2-zs) and [aakash1999's companion decks/code](https://github.com/aakash1999/claude-certified-architect-professional/tree/f710b2975e297b12f839dda071231448523e43a3). The notes synthesize selected material; original decks and full transcripts are not included.

## Mock exam

The original mock covers all 38 objectives in the supplied official CCAR-P guide v1.0, effective July 2026. It allocates 63 scored questions across seven domains, with single-answer and multiple-response items, saved progress, a continuous 120-minute clock, flags, domain diagnostics and explanations for every option. Candidate-reported Yes/No and matching formats are supplemental, unscored drills.

- [Objective coverage](mock-exams/ccar-p/blueprint.html)
- [Research, credits and limitations](mock-exams/ccar-p/research.html)
- [Printable questions](mock-exams/ccar-p/questions.html)
- [Complete answer key — spoilers](mock-exams/ccar-p/answer-key.html)
- [Exam instructions and scoring conventions](mock-exams/ccar-p/README.md)

Research includes ten public candidate accounts across six platforms, the user's two sample references and primary technical documentation. Questions and explanations are original; no leaked or reconstructed live exam questions are included. The supplied official PDF and personal knowledge-vault files are not published here.

Difficulty is intentionally demanding but has not been calibrated against the live exam. Exact-match raw scoring is a mock convention; no official pass prediction or raw-to-scaled conversion is provided. Retakes reuse the same form.

## Rebuild and check

Python 3 is sufficient to rebuild both sections; no third-party packages are needed.

```sh
python3 build.py
```

Run the mock's logic checks with Node.js:

```sh
node mock-exams/ccar-p/test.js
```

To serve the full collection locally:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. The learning pages and exam also run from local files. Source links require internet; browser-local saved progress depends on browser storage availability. No login, analytics or provider API calls are required.

Independent educational material, unaffiliated with Anthropic or the credited sources. Attribution establishes provenance and does not imply endorsement or blanket reuse permission. Current product behavior and exam policies should be checked against official sources.
