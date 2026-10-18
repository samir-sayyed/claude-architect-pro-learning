#!/usr/bin/env python3
"""Render original video companion exams with the existing shared exam runtime."""
import json
import re
from collections import Counter
from html import escape as esc
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

ROOT = Path(__file__).resolve().parent
SHARED = ROOT.parent / 'ccar-p'
VIDEOS = json.loads((ROOT / 'videos.json').read_text())
CSS = (SHARED / 'exam.css').read_text()
JS = (SHARED / 'exam.js').read_text()

def table(headers, rows):
    return '<div class="table-wrap"><table><thead><tr>' + ''.join('<th scope="col">'+esc(str(h))+'</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+str(c)+'</td>' for c in row)+'</tr>' for row in rows) + '</tbody></table></div>'

def frame(title, body, home='../../sets.html'):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+'</title><style>'+CSS+'</style></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><a class="brand" href="'+home+'">Video companion exams</a></header><main id="main" class="page">'+body+'<footer class="footer">Original independent practice · 18 October 2026 · Concepts credited to <a href="https://www.youtube.com/@coreconceptlearning">Core Concept Learning</a>. No endorsement by the channel or Anthropic. Source links require internet.</footer></main></body></html>'

def sources(data, q):
    return '<ul>'+''.join('<li><a href="'+esc(data['sources'][s]['url'],quote=True)+'">'+esc(data['sources'][s]['title'])+'</a></li>' for s in q['sources'])+'</ul>'

def exhibit(q):
    x=q.get('exhibit')
    if not x: return ''
    return '<p><strong>'+esc(x.get('caption','Exhibit'))+'</strong></p>'+table(x['headers'],[[esc(str(c)) for c in row] for row in x['rows']])

def validate(data, n):
    qs=data['questions']
    assert len(qs)==63 and data['minutes']==120
    assert Counter(q['domain'] for q in qs)=={1:11,2:8,3:12,4:10,5:9,6:9,7:4}
    assert Counter(q['select'] for q in qs)=={1:38,2:21,3:4}
    assert sorted(data['order'])==list(range(63))
    assert len({q['id'] for q in qs})==63
    all_obj={o['id'] for d in data['domains'] for o in d['objectives']}
    assert {o for q in qs for o in q['objectives']}==all_obj
    expected={1:{1:21,2:21,3:21},2:{4:21,5:21,6:21},3:{7:16,8:16,9:16,10:15}}[n]
    assert Counter(q['video_evidence']['video'] for q in qs)==expected
    assert sum(bool(q.get('exhibit')) for q in qs)>=6
    assert len(data['drills'])==3
    assert Counter(d['type'] for d in data['drills'])=={'matrix':2,'matching':1}
    assert all(len(d['rows'])==5 for d in data['drills'])
    for q in qs:
        assert len(q['options'])==(4 if q['select']==1 else 5)
        assert all(isinstance(o['correct'],bool) for o in q['options'])
        assert sum(o['correct'] for o in q['options'])==q['select']
        assert q['stem'] and q['decision'] and all(o['why'] for o in q['options'])
        assert all(o.startswith(str(q['domain'])+'.') for o in q['objectives'])
        ev=q['video_evidence']; v=VIDEOS['videos'][ev['video']-1]
        chapters=[c for c in v['chapters'] if int(c['start'])==ev['start'] and re.match(r'Q\d+\s*[·:—–-]',c['title'])]
        assert len(chapters)==1,(q['id'],ev)
        assert any(o in chapters[0]['title'] for o in q['objectives']),(q['id'],chapters[0])
        assert all(s in data['sources'] for s in q['sources'])
        assert any(v['id'] in data['sources'][s]['url'] and 't='+str(ev['start']) in data['sources'][s]['url'] for s in q['sources'])

def render(data, n):
    label=f'Video companion {n:02d}'
    dest=ROOT/'sets'/f'set-{n:02d}'; dest.mkdir(parents=True,exist_ok=True)
    (dest/'exam-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    bars=''.join('<div class="blueprint-row"><div><span>'+str(d['id'])+'. '+esc(d['name'])+'</span><strong>'+str(d['weight'])+'%</strong></div><div class="bar" aria-hidden="true"><span style="width:'+str(d['weight']*5)+'%"></span></div></div>' for d in data['domains'])
    html=(SHARED/'template.html').read_text().replace('__CSS__',CSS).replace('__DOMAIN_BARS__',bars).replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')).replace('__JS__',JS)
    html=html.replace('Professional Mock Exam',label).replace('FORM A',label.upper()).replace('Form A',label)
    html=html.replace('<a class="btn" href="ccarp-professional-mock.zip" download>Download offline pack</a>','<a class="btn" href="../../sets.html">Choose a video set</a>')
    html=html.replace('Original questions informed by the attached official guide, current primary documentation and ten public candidate reports across six platforms.','Original scenarios based on concepts across the Core Concept Learning playlist, checked against primary documentation. Each explanation credits the relevant video chapter. These questions do not reproduce the source practice bank.')
    html=html.replace('researched 11 October 2026','researched 18 October 2026')
    html=html.replace('Independent original practice · researched', 'Concept credits: <a href="https://www.youtube.com/@coreconceptlearning">Core Concept Learning</a> · Independent original practice · researched')
    html=html.replace('<nav aria-label="Reference pages">','<nav aria-label="Reference pages"><a href="../../sets.html">All video sets</a>')
    html=html.replace('These formats are reported by candidates; they are supplemental and excluded from the 63-question score.', 'These optional learning exercises are excluded from the 63-question score.')
    html=html.replace('Practice reported formats.', 'Practice additional formats.').replace('Yes/No and repeatable-option matching come from public candidate reports;', 'Yes/No and repeatable-option matching are optional learning exercises;')
    (dest/'index.html').write_text(html)
    intro='<p class="eyebrow">'+label+'</p><h2>Inspect the evidence.</h2><div class="actions"><a class="btn primary" href="index.html">Start timed exam</a><a class="btn" href="questions.html">Print questions</a><a class="btn" href="answer-key.html">Answer key · spoilers</a><a class="btn" href="research.html">Research & credits</a></div>'
    rows=[]
    for d in data['domains']:
        for o in d['objectives']:
            links=', '.join('<a href="questions.html#question-'+str(i+1)+'">Q'+str(i+1)+'</a>' for i,q in enumerate(data['questions']) if o['id'] in q['objectives'])
            rows.append([esc(d['name']),esc(o['id']+' · '+o['name']),links])
    (dest/'blueprint.html').write_text(frame(label+' · Coverage',intro+'<p>All 38 guide objectives are covered. Objective IDs are local ordinal labels. Domain question counts: 11 / 8 / 12 / 10 / 9 / 9 / 4. The chosen item mix is a practice design, not a published live-exam distribution.</p>'+table(['Domain','Objective','Questions'],rows)))
    questions=[]; answers=[]; evidence=[]
    for i,q in enumerate(data['questions'],1):
        head='<article id="question-'+str(i)+'"><h2>Q'+str(i)+' · '+esc(q['title'])+'</h2><p><strong>Select '+str(q['select'])+'.</strong></p><p>'+esc(q['stem'])+'</p>'+exhibit(q)
        opts='<ol type="A">'+''.join('<li>'+esc(o['text'])+'</li>' for o in q['options'])+'</ol>'
        questions.append(head+opts+'</article>')
        optswhy='<ol type="A">'+''.join('<li><strong>'+('Correct. ' if o['correct'] else 'Incorrect. ')+esc(o['text'])+'</strong><p>'+esc(o['why'])+'</p></li>' for o in q['options'])+'</ol>'
        answers.append(head+optswhy+'<p class="note">'+esc(q['decision'])+'</p>'+sources(data,q)+'</article>')
        ev=q['video_evidence']; v=VIDEOS['videos'][ev['video']-1]
        evidence.append([f'Q{i}',esc(', '.join(q['objectives'])),'<a href="'+esc(v['url']+'&t='+str(ev['start']))+'">Exam '+str(ev['video'])+' · '+str(ev['start']//60)+':'+str(ev['start']%60).zfill(2)+'</a>',esc(ev['concept'])])
    (dest/'questions.html').write_text(frame(label+' · Questions',intro+'<h1>Printable questions.</h1><p>63 questions · 120 minutes · Use a separate timer. Printable order differs from the mixed timed sitting; the question text is identical.</p>'+''.join(questions)))
    (dest/'answer-key.html').write_text(frame(label+' · Answers',intro+'<h1>Understand every choice.</h1><p>Spoilers: all correct choices and explanations follow. Supplemental drills appear in the interactive exam after submission.</p>'+''.join(answers)))
    research='<h1>Concepts, evidence, credit.</h1><p>We reviewed complete English captions and chapter metadata for all ten videos. These are materially original scenarios with new constraints and distractors, not transcripts or reproductions of the channel’s questions. Every scored question maps a general concept to an actual source chapter and to supporting documentation. The guide source opens the official certification directory; the supplied July 2026 PDF is not hosted or redistributed here.</p><p>The source videos are unofficial practice walkthroughs. Their suggested raw targets do not establish an official passing conversion. Live-exam equivalence is unverified. Product-specific claims were checked against primary sources on 18 October 2026; example rates and configurations are fictional unless explicitly attributed.</p><p><a href="../../research/set-'+f'{n:02d}'+'.md">Read the research notes and corrections</a></p>'+table(['Question','Objectives','Video chapter','Concept'],evidence)+'<h2>Supporting sources.</h2><ul>'+''.join('<li><a href="'+esc(s['url'],quote=True)+'">'+esc(s['title'])+'</a></li>' for s in data['sources'].values())+'</ul>'
    (dest/'research.html').write_text(frame(label+' · Research',intro+research))

if __name__=='__main__':
    forms=[json.loads((ROOT/'content'/f'set-{n:02d}.json').read_text()) for n in (1,2,3)]
    assert len({d['version'] for d in forms})==3
    assert len({q['stem'] for d in forms for q in d['questions']})==189
    for n,data in enumerate(forms,1): validate(data,n); render(data,n)
    cards=''
    for n,span in [(1,'01–03'),(2,'04–06'),(3,'07–10')]:
        cards+='<article class="note"><p class="eyebrow">Video companion '+f'{n:02d}'+'</p><h2>Decide under competing constraints.</h2><p>Concepts from source exams '+span+' · 63 original questions · 120 minutes · all 38 objectives · independent saved progress.</p><div class="actions"><a class="btn primary" href="sets/set-'+f'{n:02d}'+'/index.html">Start set '+str(n)+'</a><a class="btn" href="sets/set-'+f'{n:02d}'+'/blueprint.html">Coverage</a><a class="btn" href="sets/set-'+f'{n:02d}'+'/research.html">Sources & chapter map</a></div></article>'
    body='<p class="eyebrow">Core Concept Learning · video companion collection</p><h1>Watch the reasoning.<br>Test the transfer.</h1><p class="lead">Three original full-length practice exams, grounded in concepts across all ten playlist videos. Close alternatives, numerical trade-offs and an explanation for every option.</p><div class="facts"><span><strong>189</strong> questions</span><span><strong>10</strong> source videos</span><span><strong>38</strong> objectives per set</span></div>'+cards+'<h2>Credit to the original teacher.</h2><p>Conceptual source: <a href="'+VIDEOS['channel_url']+'">'+esc(VIDEOS['channel'])+'</a> · <a href="'+VIDEOS['playlist']+'">'+esc(VIDEOS['title'])+'</a>. Please support the original videos. No affiliation or endorsement is implied. Full source transcripts, original questions and slides are not distributed.</p>'+table(['Video','Source','Duration'],[[str(v['number']),'<a href="'+v['url']+'">'+esc(v['title'])+'</a>',str(v['duration']//60)+' minutes'] for v in VIDEOS['videos']])+'<p class="note">Independent practice. Difficulty is demanding but has not been calibrated against the live exam. Raw scores do not predict the official scaled result. Each sitting includes 38 single-answer, 21 select-two and four select-three items; three supplemental drills are unscored. All exam pages work offline; external sources require internet.</p>'
    (ROOT/'sets.html').write_text(frame('Core Concept Learning · Three video companion exams',body,'sets.html'))
    paths=[ROOT/'sets.html',ROOT/'README.md',ROOT/'videos.json']+list((ROOT/'sets').rglob('*'))+list((ROOT/'research').glob('*.md'))
    with ZipFile(ROOT/'core-concept-companions.zip','w',ZIP_DEFLATED) as z:
        for p in sorted(p for p in paths if p.is_file()):
            info=ZipInfo(p.relative_to(ROOT).as_posix(),(2026,10,18,0,0,0)); info.compress_type=ZIP_DEFLATED; z.writestr(info,p.read_bytes())
    with ZipFile(ROOT/'core-concept-companions.zip') as z:
        assert all(z.read(name)==(ROOT/name).read_bytes() for name in z.namelist())
    print('PASS: three original forms, 189 questions, all objectives, exact timestamp mappings, 16 rendered pages and byte-verified offline pack.')
