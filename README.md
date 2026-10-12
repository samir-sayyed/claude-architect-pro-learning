# Claude Architect Professional — Learning & Practice

Independent visual learning pages and six original, timed CCAR-P mock exams.

**[Open the home page](index.html)** after cloning or downloading the repository. Each section also has its own portable ZIP. After extraction, open `index.html` for the learning pages or `sets.html` for the mock collection in a modern browser.

| Section | Open | Offline download |
|---|---|---|
| Eleven episode learning pages | [Course index](learning/index.html) | [Learning ZIP](learning/claude-architect-pro-learning-pages.zip) |
| Six mock sets, 63 questions / 120 minutes each | [Choose a set](mock-exams/ccar-p/sets.html) | [All-sets ZIP](mock-exams/ccar-p/ccarp-professional-all-sets.zip) |

## Repository layout

```text
index.html                 Home page linking both sections
build.py                   Rebuild both sections and verify local navigation
learning/                  Episode pages, course data, generator, previews and ZIP
mock-exams/
  ccar-p/                  Set 01, shared generator/runtime, research and set catalogue
    sets/set-02/ ... set-06/  Each: question data, timed HTML, coverage, print/key, research
```

The root `index.html` opens the study home. The course index and all eleven episode pages live only in `learning/`. Downloads, data files and previews live in their section folders. Use the new `learning/ep01-...html` through `learning/ep11-...html` paths; the former root episode URLs have been removed.

## Learning pages

Each episode includes a concept map, process flow, decision table, worked example and checklist. The collection has 55 core takeaways and 39 source-linked slide detail cards. Episode 11 includes an editable cost calculator with illustrative rates. See [course details and attribution](learning/README.md).

Source credits: [Peace Of Code's supplied playlist](https://youtube.com/playlist?list=PLPsBalbS2-zs) and [aakash1999's companion decks/code](https://github.com/aakash1999/claude-certified-architect-professional/tree/f710b2975e297b12f839dda071231448523e43a3). The notes synthesize selected material; original decks and full transcripts are not included.

## Mock exam

The six forms contain **378 original questions**, including 315 added across Sets 02–06. [Choose a set](mock-exams/ccar-p/sets.html). Set 01 retains the original question bank. Each mock covers all 38 objectives in the supplied official CCAR-P guide v1.0, effective July 2026. Each allocates 63 scored questions across seven domains, with single-answer and multiple-response items, saved progress, a continuous 120-minute clock, flags, domain diagnostics and explanations for every option. Candidate-reported Yes/No and matching formats are supplemental, unscored drills.

- [Objective coverage](mock-exams/ccar-p/blueprint.html)
- [Research, credits and limitations](mock-exams/ccar-p/research.html)
- [Printable questions](mock-exams/ccar-p/questions.html)
- [Complete answer key — spoilers](mock-exams/ccar-p/answer-key.html)
- [Exam instructions and scoring conventions](mock-exams/ccar-p/README.md)

The [12 October research refresh](mock-exams/ccar-p/research-refresh-2026-10-12.md) rechecks public candidate accounts and newer October feedback, separating promotional and excluded sources. Each new set has its own research addendum and primary-source citations. The original research includes ten public accounts across six platforms and the user's two sample references. Questions and explanations are original; no leaked or reconstructed live exam questions are included. The supplied official PDF and personal knowledge-vault files are not published here.

Difficulty is intentionally demanding but has not been calibrated against the live exam. Exact-match raw scoring is a mock convention; no official pass prediction or raw-to-scaled conversion is provided. Each form has separate saved progress and timer state. Retakes reuse that form.

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
