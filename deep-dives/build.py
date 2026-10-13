#!/usr/bin/env python3
"""Render three portable, primary-source learning modules using only Python."""
import html
import json
import re
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
DATE = '2026-10-13'
e = html.escape


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.words, self.tags = [], [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        assert tag not in ('iframe', 'object', 'embed'), ('Unexpected embedded content', tag)
        assert not any(k.startswith('on') for k in attrs), 'Inline event handler'
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('img', 'script', 'link') and ('src' in attrs or 'href' in attrs):
            self.links.append(attrs.get('src', attrs.get('href')))

    def handle_data(self, data):
        self.words.extend(re.findall(r"\b[\w’-]+\b", data))


def analyze(fragment):
    p = Page()
    p.feed(fragment)
    return p


def load():
    modules = []
    for domain, count, weight in ((5, 5, 14), (6, 5, 14), (7, 3, 7)):
        d = json.loads((ROOT / 'content' / f'domain-{domain:02d}.json').read_text())
        assert d['domain'] == domain and d['weight'] == weight
        assert len(d['objectives']) == count
        valid = {f'{domain}.{i}' for i in range(1, count + 1)}
        assert {x for section in d['sections'] for x in section['objective_ids']} == valid
        assert 8 <= len(d['sections']) <= 12
        assert len({s['id'] for s in d['sections']}) == len(d['sections'])
        assert len(d['checks']) == 10
        assert len({c['id'] for c in d['checks']}) == 10
        assert all(len(c['options']) == len(c['explanations']) == 4 and len(set(c['options'])) == 4 and type(c['correct']) is int and 0 <= c['correct'] < 4 for c in d['checks'])
        assert all(len(c['question'].split()) >= 20 and all(len(r.split()) >= 10 for r in c['explanations']) for c in d['checks'])
        assert len(d['glossary']) >= 8
        sources = d['sources']
        assert len(sources) >= 8 and len({x['id'] for x in sources}) == len(sources)
        assert all(urlsplit(s['url']).scheme == 'https' and s['used_for'] for s in sources)
        body = '\n'.join(s['body'] for s in d['sections'])
        p = analyze(body)
        assert 'h1' not in p.tags and 'h2' not in p.tags and 'script' not in p.tags and 'style' not in p.tags
        assert p.tags.count('figure') >= 5 and p.tags.count('figcaption') >= 5
        assert len(p.words) >= 4000, ('Module needs substantive teaching', domain, len(p.words))
        assert all(s['id'].startswith(f'd{domain}-') and s['title'] and 1 <= s['minutes'] <= 90 and set(s['objective_ids']) <= valid for s in d['sections'])
        assert all(set(analyze(s['body']).links) & {x['url'] for x in sources} for s in d['sections']), ('Uncited section', domain)
        assert all(s['url'] in p.links for s in sources), ('Unused listed source', domain)
        assert (ROOT / 'research' / f'domain-{domain:02d}.md').is_file()
        assert len(list((ROOT / 'templates' / f'domain-{domain:02d}').glob('*'))) >= 3
        d['word_count'] = len(p.words)
        modules.append(d)
    return modules


def top():
    return '<a class="skip" href="#main">Skip to content</a><header class="topbar"><a class="brand" href="index.html">The Architect’s Practice / Deep learning</a><nav aria-label="Learning modules"><a href="domain-05.html">Governance</a><a href="domain-06.html">Lifecycle</a><a href="domain-07.html">Developer enablement</a></nav></header>'


def document(title, description, body, domain='index'):
    css = (ROOT / 'study.css').read_text()
    js = (ROOT / 'study.js').read_text()
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{e(description, quote=True)}"><meta name="theme-color" content="#f4f1e9"><title>{e(title)}</title><style>{css}</style></head>
<body data-domain="{domain}">{top()}{body}<footer><p>Original independent teaching, researched 13 October 2026. Mapped to the user-supplied official CCAR-P guide v1.0 (July 2026); objective numbers here are local ordinal labels. Source documentation can change. Illustrative figures, project extensions and release thresholds are teaching assumptions.</p><p>Unaffiliated with Anthropic. No live exam questions, official guide PDF, private project data or source decks are redistributed. Practical readiness and exam results require further evidence in your own environment.</p></footer><script>{js}</script></body></html>'''


def calculator(kind):
    if kind == 'queue':
        title = 'Explore the human-review capacity limit'
        intro = 'Change the assumptions. This is a steady hourly load calculation, not a queue-wait forecast. The review fraction includes all cases your approved policy routes to people; capacity assumes uninterrupted reviewers and the stated mean handling time.'
        fields = [('Requests per hour', 100, '0', '', 'any'), ('Routed to review (%)', 30, '0', '100', 'any'), ('Available reviewers (whole people)', 2, '1', '', '1'), ('Mean minutes per review', 5, '0', '', 'any')]
        limits = 'Utilization below 100% is necessary for headroom under these assumptions, but does not prove an SLA. Account for bursts, breaks, case complexity and reviewer accuracy. Equality leaves no spare capacity.'
    else:
        title = 'Explore an event-based error budget'
        intro = 'Choose one clearly defined good-event SLI and a fixed window. A bad event is an eligible request that fails that definition. This arithmetic does not combine safety, availability and answer quality into a single gate.'
        fields = [('Eligible requests in the window', 100000, '1', '', '1'), ('Good-event target (%)', 99.5, '0', '100', 'any'), ('Observed bad events', 600, '0', '', '1')]
        limits = 'This is a window-total event budget, not a time-based availability calculation or rolling burn-rate alert. Fractional allowance is a mathematical threshold; whole bad-event counts must stay at or below it. A 100% target has zero allowance and no finite budget-consumption ratio, so this calculator excludes it.'
    inputs = ''.join(f'<label>{e(label)}<input type="number" value="{value}" min="{minimum}" {f"max={maximum}" if maximum else ""} step="{step}" required></label>' for label,value,minimum,maximum,step in fields)
    return f'<form class="calc" data-calc="{kind}"><h3>{title}</h3><p>{intro}</p><div class="calc-grid">{inputs}</div><output aria-live="polite"></output><p class="small">{limits}</p><noscript><p>Interactive calculation needs JavaScript. Queue demand = arrivals × review fraction; capacity = reviewers × 60 / mean review minutes. Event allowance = eligible requests × (1 − target / 100).</p></noscript></form>'


def quiz(check):
    options = ''.join(f'<label class="option"><input type="radio" name="{check["id"]}" value="{i}"><span><b>{chr(65+i)}.</b> {e(option)}</span></label>' for i,option in enumerate(check['options']))
    explanations = ''.join(f'<li><p><b>{chr(65+i)} · {"Best response" if i == check["correct"] else "Alternative"}</b></p><p>{e(reason)}</p></li>' for i,reason in enumerate(check['explanations']))
    return f'<form class="check-card" id="{check["id"]}" data-check data-correct="{check["correct"]}"><fieldset><legend>{e(check["question"])}</legend>{options}</fieldset><button type="submit">Check this decision</button><p class="check-status" role="status"></p><details class="explanation"><summary>Reveal reasoning for every option</summary><p class="correct-label">Best response: {chr(65+check["correct"])}</p><ol type="A">{explanations}</ol></details></form>'


def module_page(d):
    n = d['domain']
    nav = ''.join(f'<a href="#{s["id"]}">{i:02d}. {e(s["title"])}</a>' for i,s in enumerate(d['sections'],1))
    sidebar = f'<aside class="sidebar"><details open><summary>On this page</summary><nav aria-label="Module contents"><a href="#objectives">Objective map</a>{nav}<a href="#decision-checks">10 decision checks</a><a href="#glossary">Glossary</a><a href="#sources">Primary sources</a></nav></details><div class="side-foot"><p id="study-progress"></p><p id="save-note"></p><p><a href="templates.zip" download>Download all templates</a></p><button id="print-page" type="button">Print / save as PDF</button></div></aside>'
    objectives = ''.join(f'<li><strong>{n}.{i}</strong> {e(o)}</li>' for i,o in enumerate(d['objectives'],1))
    total_minutes = sum(s['minutes'] for s in d['sections'])
    hero = f'<div class="hero"><p class="eyebrow">Domain {n} / {d["weight"]}% of the supplied blueprint</p><h1>{e(d["title"])}</h1><p class="lead">{e(d["summary"])}</p><div class="facts"><span><strong>{len(d["sections"])}</strong> lessons</span><span><strong>{d["word_count"]:,}</strong> teaching words</span><span><strong>{total_minutes}</strong> suggested study + practice minutes</span><span><strong>10</strong> decisions to test</span></div><div class="scope"><p><strong>Build practical judgment.</strong> Read the mechanism, redraw the diagram, change a worked example, then complete the lab using synthetic data. Mark a section only after you can explain its trade-off without looking.</p><p>Project scenarios are proposed teaching extensions, not an assessment of your deployed apps. Compliance examples explain architectural questions; applicability and legal decisions need the responsible organization’s review. Vendor findings are evidence in their stated setting, not a guarantee for your product.</p></div></div>'
    sections = f'<section class="chapter" id="objectives"><h2>The objective map</h2><ol class="objective-list">{objectives}</ol><p class="small">The numbers above are local study labels. Each lesson shows its corresponding objectives. This module follows the supplied Professional guide, distinct from the five-domain Foundations blueprint.</p></section>'
    inserted = False
    for i,s in enumerate(d['sections'],1):
        extra = ''
        if not inserted and ((n == 5 and s['id'] == 'd5-hitl') or (n == 6 and s['id'] == 'd6-service-levels')):
            extra = calculator('queue' if n == 5 else 'budget')
            inserted = True
        sections += f'<section class="chapter" id="{s["id"]}"><p class="section-meta">LESSON {i:02d} / OBJECTIVES {", ".join(s["objective_ids"])} / ~{s["minutes"]} MIN</p><h2>{e(s["title"])}</h2><div class="body-copy">{s["body"]}</div>{extra}<label class="mark"><input type="checkbox" data-complete="{s["id"]}"><span>Studied: {e(s["title"])}. I can explain and apply its key decision.</span></label></section>'
    sections += '<section class="chapter" id="decision-checks"><h2>Make the decision before reading the answer</h2><p>These are original learning scenarios. Identify the binding constraint and the authority boundary, then compare all four explanations. They do not reproduce live exam items or estimate an official pass result.</p>'+''.join(quiz(c) for c in d['checks'])+'</section>'
    sections += '<section class="chapter" id="glossary"><h2>Terms you should be able to explain</h2><dl class="glossary">'+''.join(f'<dt>{e(x["term"])}</dt><dd>{e(x["definition"])}</dd>' for x in d['glossary'])+'</dl></section>'
    sections += '<section class="chapter" id="sources"><h2>Inspect the primary evidence</h2><p>Sources were checked for this learning edition on 13 October 2026. The research note records what was used and the limits of the evidence. Laws, product behavior and organizational policies can change independently of this material.</p><ol class="sources">'+''.join(f'<li id="{s["id"]}"><a href="{e(s["url"], quote=True)}">{e(s["id"])} · {e(s["title"])}</a><small>{e(s["used_for"])}</small></li>' for s in d['sources'])+f'</ol><p><a href="research/domain-{n:02d}.md">Read the research record</a> · <a href="templates.zip" download>Download the implementation templates</a></p></section>'
    prev = f'<a href="domain-{n-1:02d}.html">← Domain {n-1}</a>' if n > 5 else '<a href="index.html">← Learning path</a>'
    nxt = f'<a href="domain-{n+1:02d}.html">Domain {n+1} →</a>' if n < 7 else '<a href="index.html#capstone">Connect the three domains →</a>'
    body = f'<div class="layout">{sidebar}<main id="main">{hero}{sections}<nav class="page-nav" aria-label="Continue learning">{prev}{nxt}</nav></main></div>'
    return document(f'Domain {n}: {d["title"]}', d['summary'], body, str(n))


def index_page(modules):
    cards = ''.join(f'<article class="module-card"><p class="eyebrow">DOMAIN {d["domain"]} / {d["weight"]}%</p><h2>{e(d["title"])}</h2><p>{e(d["summary"])}</p><p class="small">{len(d["sections"])} lessons · {d["word_count"]:,} teaching words · 10 decision checks</p><a class="button" href="domain-{d["domain"]:02d}.html">Study Domain {d["domain"]} →</a></article>' for d in modules)
    words = sum(d['word_count'] for d in modules)
    content = f'''<main id="main" class="index-main"><div class="hero"><p class="eyebrow">Professional architecture / Domains 5–7 / Practical learning</p><h1>Build systems people can trust, operate and improve.</h1><p class="lead">Go from knowing the terms to making defensible project decisions. Three substantial modules connect governance, delivery and developer operations, with the exam as a useful coverage check.</p><div class="facts"><span><strong>13</strong> guide objectives</span><span><strong>{words:,}</strong> teaching words</span><span><strong>30</strong> decision checks</span><span><strong>3</strong> hands-on labs</span></div><div class="actions"><a class="button" href="domain-05.html">Start with Domain 5 →</a><a class="button secondary" href="templates.zip" download>Download reusable templates</a></div><p class="small">Researched 13 October 2026. Original explanations and synthetic project exercises; primary sources are linked beside claims. Runs offline after download, except source links.</p></div><div class="module-grid">{cards}</div>
<section class="chapter" id="path"><h2>A path that turns reading into skill</h2><p>Choose one consequential feature to work through all three modules. A nutrition-information draft assistant, multilingual job-post helper or internal support copilot works well. Keep your first exercise synthetic and draft-only so you can test failure cases without affecting users. These are proposed extensions inspired by familiar project types, not claims about the current state of any repository.</p><ol class="reading-plan"><li><strong>Define the work before choosing autonomy.</strong> Write one user journey, its current baseline, who is affected by failure and who may authorize a consequential action. Domain 6 supplies the discovery brief; it is useful to skim that template before reading Domain 5.</li><li><strong>Draw the trust and data boundaries.</strong> Follow input, retrieval, prompts, tools, logs and human decisions. Name where each control actually runs. Complete Domain 5’s risk and reviewer exercises.</li><li><strong>Turn expectations into acceptance evidence.</strong> Choose constraints that must all pass, then optimization goals. Record an ADR and a measurable service contract in Domain 6. Make the denominator, window, exclusions and owner explicit.</li><li><strong>Build a repeatable team workflow.</strong> Apply Domain 7’s configuration distinctions and offline debugging lab. Keep policy enforcement, runtime isolation and human instructions separate. Collect evidence that another developer can reproduce.</li><li><strong>Review the assembled system.</strong> Explain each trade-off to a technical peer and a product stakeholder. Use the capstone below to find missing ownership, stale approval, hidden review load or an untested rollback.</li><li><strong>Use checks as diagnosis.</strong> Answer the ten scenarios per module before expanding rationales. A correct choice is useful only if you can explain why the other choices fail under that scenario’s conditions.</li></ol><p>Read in several sessions rather than a single skim. For every worked example, change one assumption—traffic, user population, action impact, data rights or recovery requirement—and identify which decision must change. Suggested lesson times include explanation and short reflection; running a real pilot takes additional project time.</p></section>
<section class="chapter" id="capstone"><h2>One feature, three connected responsibilities</h2><p><strong>Capstone scenario:</strong> a marketplace team proposes a multilingual assistant that drafts job descriptions and suggests matches. The first pilot may prepare suggestions for an authorized person; it cannot rank workers automatically for exclusion, alter wages, send offers or move money. These are exercise boundaries, not a statement that such a feature exists in your app.</p><figure class="diagram"><figcaption>The same request crosses product, authority and operating boundaries</figcaption><ol class="flow"><li><strong>Person and purpose</strong><br>Authenticated user, declared task and language; only the data needed for that task.</li><li><strong>Evidence and draft</strong><br>Authorized current records enter the model. Retrieved text cannot grant new tool authority.</li><li><strong>Decision boundary</strong><br>Policy checks and a qualified reviewer handle consequential proposals. Approval binds to exact current action data.</li><li><strong>Execution and receipt</strong><br>A separate executor rechecks permissions and state, then records the actual outcome or a failure.</li><li><strong>Feedback and release</strong><br>Versioned traces, slice-level outcomes, incident ownership and a reversible change process.</li></ol></figure><p>This diagram is an original synthesis. Its separation of model behavior from actual outcomes follows <a href="https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents">Anthropic’s agent-evaluation guidance</a>; the choice to begin with a constrained workflow follows <a href="https://www.anthropic.com/engineering/building-effective-agents">its agent-architecture guidance</a>. Neither source supplies the illustrative thresholds or project policy below.</p><div class="cross-map"><article><h3>Domain 5: decide what must be protected</h3><p>Create a data inventory and risk register. Test indirect injection in job text, unauthorized records, misleading wage statements, stale approvals and disparate burden across languages. Define review authority and an explicit stop path. Successful parsing is not evidence that a suggestion is appropriate or authorized.</p></article><article><h3>Domain 6: decide what success and ownership mean</h3><p>Record an approved scope, accountable release owner and measurable pilot criteria. Separate usefulness, latency, appeal access and reviewer load. Agree who may change scope, who handles complaints and what evidence is needed to expand beyond drafts.</p></article><article><h3>Domain 7: make the implementation reproducible</h3><p>Pin the evaluation bundle, document development commands, scope tool permissions and test runtime access separately. Reproduce a failure with synthetic fixtures, ship a reviewed repair and prove rollback and handoff using the receiving team’s actual access.</p></article></div>
<h3>A pilot scorecard that resists misleading averages</h3><p>Suppose 1,000 synthetic or consented pilot tasks include 800 in language A and 200 in language B. The assistant completes 760 A tasks and 140 B tasks. Overall completion is 900/1,000 = 90%, but the slices are 95% and 70%. If the team agreed an 85% minimum completion gate for each language, the release fails that independent gate. A higher overall target does not repair the disparity. Diagnose task mix, data quality, language support and review routing before changing a threshold.</p><p>Now suppose 25% of 100 hourly requests need a reviewer, each review takes six minutes, and two reviewers are available. Demand is 25 reviews/hour; nominal capacity is 2 × 60/6 = 20. The queue grows by five cases per hour before accounting for breaks or bursts. Do not fix the promised response time by silently reducing mandatory review. Reduce accepted demand, add trained capacity or negotiate a narrower approved pilot.</p><p>For a separate event-based draft-availability objective of 99% over 10,000 eligible tasks, allowance is 100 bad events. Recording 75 bad events leaves 25. That availability result cannot offset a missed language gate, unsafe action, privacy breach or overloaded reviewer. Every figure here is an invented teaching assumption; each project must justify its own definitions and thresholds.</p><h3>The practical proof package</h3><ol class="reading-plan"><li><strong>Discovery evidence:</strong> one observed workflow, a baseline, affected users, assumptions, exclusions and a person who can decide scope.</li><li><strong>Control evidence:</strong> a data-flow map, risk owners, executor checks, denial behavior, review policy and representative adversarial cases.</li><li><strong>Decision evidence:</strong> a short ADR comparing feasible alternatives and naming the assumption that would trigger reconsideration.</li><li><strong>Quality evidence:</strong> a versioned evaluation set with slice denominators, failure severities, expected outcomes and acknowledged blind spots.</li><li><strong>Operating evidence:</strong> sanitized trace examples, on-call ownership, a tested fallback, explicit rollback conditions and a release record tying configuration to results.</li><li><strong>Handoff evidence:</strong> a second person can set up the environment, run the checks, identify an incident and execute the approved recovery path without borrowing the author’s credentials.</li></ol><p>The templates give you a starting point for these artifacts. Completing a document is not the acceptance test: try the denied action, let approval become stale, remove a dependency, introduce a repeat request, change the population mix and ask the receiving team to recover the system.</p></section>
<section class="chapter" id="exam"><h2>Translate practical skill into exam judgment</h2><p>The supplied Professional guide assigns 14%, 14% and 7% to these domains, together 35% of its blueprint. Its 13 objective bullets define this collection’s scope. Local labels such as 5.1 identify study mappings; the guide itself does not number each bullet.</p><p>In a scenario, first locate the lifecycle phase and the unresolved obligation. A technically strong implementation can still be premature if the task’s success criteria, data rights or decision authority are unknown. A later monitoring improvement cannot substitute for an executor permission check. A larger model cannot supply a missing approval, and a human checkbox cannot repair a review process without evidence, time and authority.</p><p>Look for independent constraints, not merely the highest metric. Distinguish preventive control from detection, a provider’s capabilities from the customer system’s obligations, a proposal from the observed outcome, an SLO from a contractual SLA, and a source-code worktree from an isolation boundary. The decision checks require that same reasoning without reproducing the live item bank.</p><p>The collection supports preparation; it does not establish live-exam calibration or guarantee a score. The six original mock forms remain a separate practice collection in the repository, with their own source and scoring disclosures.</p></section></main>'''
    return document('Domains 5–7: Practical architecture learning', 'Deep learning for governance, stakeholder delivery and Claude developer operations, with practical cases, diagrams, labs and decision checks.', content)


def archive(path, files):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for item in sorted(files):
            name = str(item.relative_to(ROOT))
            info = zipfile.ZipInfo(name, (2026, 10, 13, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, item.read_bytes())
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(files)
        assert all(z.read(str(f.relative_to(ROOT))) == f.read_bytes() for f in files)


def verify(modules):
    parsed = {p.resolve(): analyze(p.read_text()) for p in ROOT.glob('*.html')}
    assert len(parsed) == 4
    for path, page in parsed.items():
        assert len(page.ids) == len(set(page.ids)), ('Duplicate IDs', path)
        assert page.tags.count('h1') == 1
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                assert url.scheme == 'https' and url.netloc, ('Unexpected external URL', href)
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(ROOT) and target.is_file(), ('Invalid local target', path, href)
            if url.fragment and target in parsed:
                assert unquote(url.fragment) in parsed[target].ids, ('Missing fragment', path, href)
    for d in modules:
        page = parsed[(ROOT / f'domain-{d["domain"]:02d}.html').resolve()]
        assert all(s['id'] in page.ids for s in d['sections'])
        assert all(c['id'] in page.ids for c in d['checks'])
    assert not list(ROOT.rglob('*.pdf'))
    print(f'PASS: 3 domain modules / 13 objectives / 30 checks / {sum(d["word_count"] for d in modules):,} teaching words; 4 portable pages, unique IDs, local links, cited sections and ZIP byte checks.')


if __name__ == '__main__':
    modules = load()
    archive(ROOT / 'templates.zip', list((ROOT / 'templates').rglob('*.*')))
    for d in modules:
        (ROOT / f'domain-{d["domain"]:02d}.html').write_text(module_page(d))
    (ROOT / 'index.html').write_text(index_page(modules))
    verify(modules)
    files = list(ROOT.glob('*.html')) + list((ROOT / 'templates').rglob('*.*')) + list((ROOT / 'research').glob('*.md')) + [ROOT / 'README.md', ROOT / 'templates.zip']
    archive(ROOT / 'domain-05-07-learning.zip', files)
