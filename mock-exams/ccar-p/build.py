#!/usr/bin/env python3
"""Build dependency-free mock exam, printable companions and offline archive."""
import html
import json
import re
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'exam-data.json').read_text())
CSS=(ROOT/'exam.css').read_text()
e=html.escape
QUESTIONS=[D['questions'][i] for i in D['order']]

def table(headers,rows):
    return '<div class="table-wrap"><table><thead><tr>'+''.join(f'<th scope="col">{e(str(x))}</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{x}</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'

def frame(title,body):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><style>{CSS}</style></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><a class="brand" href="index.html">The Architect’s Practice</a><nav aria-label="Reference pages"><a href="index.html">Take exam</a><a href="blueprint.html">Coverage</a><a href="research.html">Research</a></nav></header><main id="main" class="page document">{body}<footer class="footer">Independent original practice · CCAR-P · researched 11 October 2026 · no live exam questions used.<br><a href="index.html">Return to the timed exam</a></footer></main></body></html>'

def sources(q):
    return ' · '.join(f'<a href="{e(D["sources"][s]["url"])}" target="_blank" rel="noopener">{e(D["sources"][s]["title"])}</a>' for s in q['sources'])

def exhibit(q):
    x=q.get('exhibit')
    return table(x['headers'],[[e(v) for v in row] for row in x['rows']]) if x else ''

def blueprint():
    counts=Counter(q['domain'] for q in QUESTIONS)
    body='<p class="eyebrow">THE COVERAGE CONTRACT</p><h1>Seven domains.<br>Thirty-eight objectives.</h1><p>The attached official CCAR-P guide v1.0 (July 2026), pages 4–6, defines the scope. The objective labels 1.1–7.3 below are local ordinal identifiers for its bullet points; the guide itself does not number them that way. Wording is shortened for navigation.</p>'
    body+=table(['Domain','Official weight','Mock items','Mock proportion'],[[e(d['name']),str(d['weight'])+'%',str(counts[d['id']]),f'{counts[d["id"]]/63*100:.2f}%'] for d in D['domains']])
    body+='<p class="note">Largest-remainder rounding allocates 63 questions as 11 / 8 / 12 / 10 / 9 / 9 / 4. Every question has one primary scoring domain and may cover multiple objectives within it. Exposure is not proof of mastery or equal psychometric difficulty.</p>'
    for domain in D['domains']:
        body+=f'<h2>Domain {domain["id"]}: {e(domain["name"])}</h2>'
        for obj in domain['objectives']:
            qs=[(i,q) for i,q in enumerate(QUESTIONS,1) if obj['id'] in q['objectives']]
            links=' · '.join(f'<a href="questions.html#question-{i}">Item {i} ({q["id"]})</a>' for i,q in qs)
            body+=f'<div class="objective"><strong>{obj["id"]} · {e(obj["name"])}</strong><p>{links}</p></div>'
    body+='<h2>Item patterns</h2><p>The scored form contains 38 single-answer and 25 multiple-response items, including select-two and select-three. Patterns include best-fit architecture, first intervention, diagnostic evidence, competing release gates, numerical exhibits, controlled experiments, lifecycle timing, approval boundaries and cost arithmetic. This mix is our design choice, not an official quota.</p><p>Two Yes/No matrices and a repeatable-option matching drill are available after submission. They are unscored practice informed by candidate testimony, not additional official format requirements.</p><h2>Scoring</h2><p>One point per exact correct response set; no partial credit or negative marks in this mock. Unanswered/incomplete sets score zero. Domain percentages are diagnostics. The guide publishes a scaled pass score of 720 on a 100–1,000 scale, but no raw-score conversion or multiple-response partial-credit policy. We do not infer either.</p>'
    return frame('CCAR-P mock · objective coverage',body)

def questions_page():
    body='<p class="eyebrow">FORM A · QUESTIONS ONLY</p><h1>Printable mock exam.</h1><p>63 original questions · 120 minutes. Use this page with a separate timer. Mark exactly the required number of responses. Domain and topic labels are withheld here. Answers and rationales are in <a href="answer-key.html">the separate answer key (spoilers)</a>. Use your browser’s Print command to save a PDF or print paper.</p>'
    for i,q in enumerate(QUESTIONS,1):
        body+=f'<article class="doc-question" id="question-{i}"><p class="eyebrow">QUESTION {i:02d} / 63 · SELECT {q["select"]}</p><p class="stem">{e(q["stem"])}</p>{exhibit(q)}<ol type="A">'+''.join(f'<li>{e(o["text"])}</li>' for o in q['options'])+'</ol></article>'
    return frame('CCAR-P mock · printable questions',body)

def answer_key():
    body='<p class="eyebrow">SPOILERS · OPEN AFTER YOUR SITTING</p><h1>The answer is only<br>half the work.</h1><p>Identify the constraint that decides each case. These are original scenario judgments, not official item-bank rationales. Sources support the underlying principles; scenario data are illustrative. Each item maps to the guide’s objectives in <a href="blueprint.html">the coverage map</a>.</p>'
    for i,q in enumerate(QUESTIONS,1):
        key=', '.join(chr(65+j) for j,o in enumerate(q['options']) if o['correct'])
        body+=f'<article class="doc-question" id="answer-{i}"><p class="eyebrow">ITEM {i:02d} · {q["id"]} · DOMAIN {q["domain"]} · OBJECTIVES {", ".join(q["objectives"])}</p><h2>{e(q["title"])}</h2><p class="stem">{e(q["stem"])}</p>{exhibit(q)}<p><strong>Correct: {key}</strong> · select {q["select"]}</p><p class="decision">{e(q["decision"])}</p><ol class="option-rationale">'
        for j,o in enumerate(q['options']):
            body+=f'<li><b>{chr(65+j)} · {"Correct" if o["correct"] else "Distractor"}</b><p>{e(o["text"])}</p><p class="muted">{e(o["why"])}</p></li>'
        body+=f'</ol><p class="source-links">{sources(q)}</p></article>'
    body+='<h2>Supplemental format drills</h2><p>These are outside the 63-question score. Candidate reports support their inclusion; the official guide does not specify these interfaces.</p>'
    for drill in D['drills']:
        body+=f'<h3>{e(drill["title"])}</h3><p>{e(drill["stem"])}</p>'
        body+=table(['Statement','Answer','Reason'],[[e(r['text']),e(r['answer']),e(r['why'])] for r in drill['rows']])
    return frame('CCAR-P mock · complete answer explanations',body)

def research():
    feedback=[
('Reddit · Tecr','Date not independently confirmed','https://www.reddit.com/r/ClaudeAI/comments/1vrl9ng/passed_the_claude_certified_architect/','Production practitioner: trade-offs and lifecycle wording; felt easier than Foundations.'),
('Reddit · cs135dev','Date not independently confirmed','https://www.reddit.com/r/ClaudeCertified/comments/1vo909f/passed_ccarp_exam_harder_than_expected/','Real sitting felt more complex than a mock; more multiple-answer items.'),
('Reddit · security/AI architect','Date not independently confirmed','https://www.reddit.com/r/Anthropic/comments/1ve5liq/passed_the_claude_certified_architect_professional/','Scoping, customer expectations and business architecture alongside technical knowledge.'),
('LinkedIn · Manoj kumar Katakam','2026-09-04','https://www.linkedin.com/pulse/4-claude-certifications-12-days-heres-what-actually-made-katakam-qxoaf','Several reasonable-looking options; first pass about 90 minutes and substantial review.'),
('LinkedIn · Xi Xiao','2026-09-21','https://www.linkedin.com/pulse/three-tech-claude-certs-one-month-xi-xiao-bydvf','Enterprise terminology, long reading, select-two and Yes/No; 12 minutes left after review.'),
('Qiita · Solbear','2026-08-28; sitting 2026-08-26','https://qiita.com/Solbear/items/2ba5ae5c67cbece68142','Reports single, multiple-select and five-statement Yes/No items; explicitly sitting-specific mix.'),
('Zenn · kyohei.DoAI','2026-08-16','https://zenn.dev/acntechjp/articles/1b60be8da3ba3a','High English reading load, multi-select, governance and lifecycle judgments.'),
('DEV · Blue Panda','September 2026; year from index','https://dev.to/bluepanda/i-cleared-all-4-anthropic-claude-certifications-what-you-actually-need-to-know-and-what-to-skip-224m/','Decision emphasis over obscure flag recall; author also promotes prep resources.'),
('LinkedIn · Matthew Hartman','Exact date not verified','https://www.linkedin.com/posts/matthewhartman_ccar-p-study-guide-all-seven-domains-free-activity-7495904616287711232-oNCf','Reports Yes/No matrices and repeatable dropdown matching; publishes own prep material.'),
('GitHub · vkorost','README: sitting 2026-09-01','https://github.com/vkorost/claude-certified-architect-professional-guide','Professional decision focus and 38-objective mapping; own guide promotion is disclosed.')]
    body='<p class="eyebrow">RESEARCHED 11 OCTOBER 2026</p><h1>Evidence before<br>exam folklore.</h1><p>The attached official guide controls blueprint and official mechanics. Public candidate testimony informs scenario design and supplemental practice. Primary documentation checks technical and regulatory principles. These evidence types are kept separate.</p><h2>What is established</h2><p>Attached guide v1.0: 63 items, 120 minutes, multiple-choice and multiple-response items stating the response count, seven weighted domains and 38 objectives. The score is scaled from 100 to 1,000 with a 720 passing standard. The three published illustrative examples are not live exam questions. This mock uses original scenarios and does not reproduce them.</p><p><a href="https://anthropic-partners.skilljar.com/page/partner-certifications">Official guide directory</a> · <a href="https://claude.com/resources/articles/four-role-based-claude-certifications">Anthropic’s role-based certification announcement</a> · <a href="https://anthropic-partners.skilljar.com/page/faq-certifications">Official certification FAQ</a></p><h2>What candidates report</h2><p>Difficulty is mixed: experienced candidates sometimes find Professional easier than Foundations, while others find real questions harder than mocks. Repeated themes include close distractors, enterprise constraints, lifecycle timing and multiple-response items. Reading pressure varies. Yes/No is reported by multiple candidates; matching is a weaker, single-report format signal. These are self-reports, not authenticated scores or a representative survey.</p>'
    body+=table(['Firsthand source','Date evidence','Reported signal'],[[f'<a href="{e(url)}">{e(name)}</a>',e(date),e(signal)] for name,date,url,signal in feedback])
    body+='<p class="note">Ten accounts across six platforms; cross-posts are counted once. Authors’ scores, identities and exam forms were not independently authenticated. Several authors publish or recommend study products. Japanese sources are paraphrased in English. <a href="research-feedback.md">Full evidence notes and exclusions</a>.</p><h2>Search breadth</h2><p>Searched Professional/CCAR-P variants on Reddit, LinkedIn, GitHub, Medium, DEV, Qiita, Zenn, YouTube, X, Hacker News and Stack Overflow. The final firsthand evidence comes from six platforms. Searches on the others did not yield sufficiently specific, reliable Professional accounts in the returned results. Foundations reports, duplicate summaries, anonymous testimonials and dump promotions were excluded.</p><h2>Your two sample references</h2><p><a href="https://flashgenius.net/sample-tests/ccar-p/quick-start">FlashGenius quick-start</a> illustrates constraint-led scenarios and option-by-option explanations. Its free ten-item page is a provider-authored sample, not independent proof of live difficulty. We used its visible format as a reference, without copying its questions.</p><p><a href="https://claudemockexams.com/architect-professional/sample-questions">Claude Mock Exams sample questions</a> demonstrates multiresponse wording and architectural distinctions. It is preparation-provider material. It does not establish our mock’s difficulty or an official item distribution. No sample questions or rationales were reproduced.</p><h2>How the mock follows the evidence</h2><ol><li>Cover every guide objective, using nearest whole-question domain weighting.</li><li>Mix single-response and select-two/select-three decisions; use exhibits and calculation where relevant.</li><li>Make alternatives plausible but distinguishable by an explicit constraint, evidence boundary or lifecycle phase.</li><li>Use a continuous 120-minute clock, review flags and return navigation.</li><li>Explain every option after submission; keep candidate-reported interface drills outside the official-format score.</li></ol><h2>Primary technical references</h2>'
    for id,s in D['sources'].items():
        if id=='guide':continue
        body+=f'<p><a href="{e(s["url"])}">{e(s["title"])}</a></p>'
    body+='<h2>Difficulty and scoring limits</h2><p>No public evidence here establishes equivalent item-bank difficulty, predictive pass rate, a fixed live format mix or a raw-to-scaled conversion. The mock has not been piloted with candidates or psychometrically calibrated. Exact-match scoring is an explicit practice convention. Retakes use the same form and can reflect memory.</p><h2>Originality and attribution</h2><p>Anthropic owns the credential and official guide. The named candidate authors and sample providers are credited for their public evidence. Questions, diagrams/process guides and explanations in this pack are original teaching material. No live exam content, videos, full transcripts, original decks or attached official PDF are included in the offline pack. This is independent and unaffiliated with Anthropic or the reference providers.</p><h2>Maintenance</h2><p>Scope is pinned to the attached July 2026 v1.0 guide. Product documentation was checked on the research date; MCP authorization links use the retrieved 2026-07-28 revision. Changing model catalogs, prices and numeric context limits are intentionally not recall targets. Fictional exercise rates and measured candidates are supplied in the stems. Legal scenarios state their applicability and approvals; they do not certify any actual provider deployment.</p>'
    return frame('CCAR-P mock · research and attribution',body)

class CheckHTML(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.links=[];self.external_assets=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag in ('script','img','link','iframe') and (a.get('src','').startswith('http') or a.get('href','').startswith('http')):self.external_assets.append(a)

def verify_data():
    assert len(QUESTIONS)==63 and sorted(D['order'])==list(range(63))
    assert Counter(q['domain'] for q in QUESTIONS)==dict(enumerate([11,8,12,10,9,9,4],1))
    assert sum(q['select']==1 for q in QUESTIONS)==38
    assert sum(q['select']>1 for q in QUESTIONS)==25
    assert sum(d['weight'] for d in D['domains'])==100
    objectives={o['id'] for d in D['domains'] for o in d['objectives']}
    assert len(objectives)==38 and {o for q in QUESTIONS for o in q['objectives']}==objectives
    assert len({q['id'] for q in QUESTIONS})==63
    for q in QUESTIONS:
        assert q['select']==sum(o['correct'] for o in q['options']) and q['select'] in (1,2,3)
        assert all(o['why'] and o['text'] for o in q['options'])
        assert all(s in D['sources'] for s in q['sources'])
        assert all(int(o.split('.')[0])==q['domain'] for o in q['objectives'])
        assert len({o['text'] for o in q['options']})==len(q['options'])
        if q.get('exhibit'):assert all(len(r)==len(q['exhibit']['headers']) for r in q['exhibit']['rows'])
    assert len(D['drills'])==3

if __name__=='__main__':
    verify_data()
    bars=''.join(f'<div class="blueprint-row"><div><span>{d["id"]}. {e(d["name"])}</span><strong>{d["weight"]}%</strong></div><div class="bar" aria-hidden="true"><span style="width:{d["weight"]*5}%"></span></div></div>' for d in D['domains'])
    page=(ROOT/'template.html').read_text().replace('__CSS__',CSS).replace('__DOMAIN_BARS__',bars).replace('__DATA__',json.dumps(D,ensure_ascii=False).replace('</','<\\/')).replace('__JS__',(ROOT/'exam.js').read_text())
    assert not any(marker in page for marker in ('__CSS__','__DATA__','__JS__','__DOMAIN_BARS__'))
    files={'index.html':page,'blueprint.html':blueprint(),'questions.html':questions_page(),'answer-key.html':answer_key(),'research.html':research()}
    for name,body in files.items():(ROOT/name).write_text(body)
    pack=list(files)+['research-feedback.md','research-notes.md','README.md','exam-data.json']
    with zipfile.ZipFile(ROOT/'ccarp-professional-mock.zip','w',zipfile.ZIP_DEFLATED) as z:
        for name in pack:z.write(ROOT/name,name)
    parsed={}
    for name,body in files.items():
        c=CheckHTML();c.feed(body);parsed[name]=c
        assert len(c.ids)==len(set(c.ids)),(name,'duplicate ID')
        assert not c.external_assets,(name,'external dependency')
    for name,c in parsed.items():
        for href in c.links:
            if href.startswith(('https:','http:','mailto:')):continue
            path,_,fragment=href.partition('#');path=path or name
            assert (ROOT/path).is_file(),(name,href)
            if fragment and path in parsed:assert fragment in parsed[path].ids,(name,href)
    with zipfile.ZipFile(ROOT/'ccarp-professional-mock.zip') as z:
        assert z.namelist()==pack
        for name in pack:assert z.read(name)==(ROOT/name).read_bytes()
    print('PASS: 63 questions, all 38 objectives, exact domain allocation, 5 standalone HTML pages, valid local links and ZIP byte matches.')
