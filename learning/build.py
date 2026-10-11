#!/usr/bin/env python3
"""Build portable episode pages from transcript-grounded learning notes."""
import html
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'course-data.json').read_text())
DETAILS = json.loads((ROOT / 'slide-details.json').read_text())
COMMIT = 'f710b2975e297b12f839dda071231448523e43a3'
REPO = 'https://github.com/aakash1999/claude-certified-architect-professional'
SLIDE_COUNTS = {1:15, 2:16, 3:15, 4:17, 5:15, 6:17, 7:18, 8:18, 10:15}
PLAYLIST = 'https://youtube.com/playlist?list=PLPsBalbS2-zs'
e = html.escape


def stamp(t):
    parts = list(map(int, t.split(':')))
    seconds = 0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds


def filename(d):
    return f"ep{d['episode']:02d}-{d['slug']}.html"


def cite(d, t):
    seconds = stamp(t)
    return f'<a class="cite" href="https://youtu.be/{d["video"]}?t={seconds}" target="_blank" rel="noopener">↗ Lesson {seconds // 60}:{seconds % 60:02d}</a>'


def detail_source(card):
    ep = card['source_episode']
    path = card.get('file', f'episode {ep}/ppt.pptx')
    label = f'Ep{ep:02d} · '+(Path(path).name if 'file' in card else 'deck')
    if card.get('slides') and 'file' not in card:
        label += ' · slides '+', '.join(map(str, card['slides']))
    link = f'<a class="detail-cite" href="{REPO}/blob/{COMMIT}/{quote(path)}" target="_blank" rel="noopener">{e(label)} ↗</a>'
    if card.get('slides') and card.get('file'):
        link += '<br>'+detail_source({key:value for key,value in card.items() if key!='file'})
    return link


def detail_section(d):
    n = d['episode']
    title = 'Important details from the slide deck.'
    note = 'Selected additions from the matching deck. Slide numbers refer to the linked PowerPoint; the explanations and visuals are original learning notes.'
    if n == 9:
        title = 'Inside the evaluation walkthrough.'
        note = 'No Episode 09 deck is present in the reviewed snapshot. These additions come from its walkthrough, dataset, and source code.'
    elif n == 11:
        title = 'Related details from earlier episodes.'
        note = 'No Episode 11 folder or deck is present in the reviewed snapshot. These connections use the Episode 05/08 decks and Episode 09 runner.'
    cards = ''
    for i, card in enumerate(DETAILS[str(n)], 1):
        extra = ''
        if card.get('table'):
            heads, *rows = card['table']
            extra += '<div class="table-box"><table><thead><tr>'+''.join(f'<th scope="col">{e(x)}</th>' for x in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{e(x)}</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'
        if card.get('steps'):
            extra += '<ol class="detail-flow">'+''.join(f'<li>{e(x)}</li>' for x in card['steps'])+'</ol>'
        if card.get('code'):
            extra += f'<pre><code>{e(card["code"])}</code></pre>'
        cards += f'<article class="detail-card" id="detail-{i}"><span class="detail-number">DETAIL {i:02d}</span><h3>{e(card["title"])}</h3><p>{e(card["body"])}</p>{extra}{detail_source(card)}</article>'
    return f'<section id="slide-details"><div class="section-head"><span class="kicker">GO DEEPER</span><h2>{title}</h2></div><p class="detail-intro">{note} <a href="{REPO}/tree/{COMMIT}" target="_blank" rel="noopener">Reviewed repository snapshot ↗</a></p><div class="detail-grid">{cards}</div></section>'


CSS = '''
:root{--paper:#f5f2e9;--card:#fffcf5;--ink:#18312e;--muted:#536a64;--line:#d8ddd0;--accent:#b74423;--teal:#176b61;--soft:#e6eee3;--shadow:0 12px 35px #18312e0b;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:100px}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}a{color:inherit;text-underline-offset:4px}button,input,textarea{font:inherit}button,a,input,textarea,summary{touch-action:manipulation}button{cursor:pointer}button:focus-visible,a:focus-visible,input:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:5px}button:disabled{opacity:.55;cursor:default}.skip{position:fixed;top:-100px;left:20px;background:var(--card);padding:12px;z-index:100}.skip:focus{top:12px}
.rail{position:fixed;left:0;top:0;bottom:0;width:252px;padding:32px 25px 20px;background:#18312e;color:#f5f2e9;overflow:auto;display:flex;flex-direction:column;z-index:30}.brand{text-decoration:none;line-height:1.1;display:block}.brand small{display:block;font:10px/1.4 ui-monospace,monospace;letter-spacing:.2em;color:#aec3b6;margin-bottom:10px}.brand strong{font:32px/.99 Georgia,serif;font-weight:normal}.rail .course{font-size:12px;color:#c7d2c9;margin:22px 0}.rail nav{display:grid;gap:4px}.rail nav a{padding:8px 7px;display:flex;gap:12px;text-decoration:none;font-size:12px;line-height:1.35;border-radius:5px;color:#c7d2c9}.rail nav a span{font:11px/1.6 ui-monospace,monospace;color:#97b1a3}.rail nav a[aria-current=page]{background:#f5f2e9;color:#18312e}.rail nav a:hover{background:#ffffff15;color:#fff}.rail nav a[aria-current=page]:hover{background:#fff;color:#18312e}.rail .rail-foot{margin-top:auto;padding-top:28px;font-size:11px;line-height:1.6;color:#abc2b5}.rail-foot a{display:inline-block;margin-top:7px}.shell{margin-left:252px}.topbar{height:76px;position:sticky;top:0;z-index:20;display:flex;align-items:center;justify-content:space-between;gap:15px;border-bottom:1px solid var(--line);padding:12px 4vw;background:#f5f2e9f2;backdrop-filter:blur(12px)}.crumb{font:11px ui-monospace,monospace;letter-spacing:.08em;color:var(--muted)}.actions{display:flex;align-items:center;gap:8px}.btn{border:1px solid var(--line);background:var(--card);color:var(--ink);padding:9px 14px;border-radius:6px;font-size:12px;line-height:1.5;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:8px}.btn:hover{border-color:var(--teal)}.btn.primary{background:var(--ink);color:var(--paper);border-color:var(--ink)}.mobile-menu{display:none}.progress{height:3px;background:var(--accent);position:absolute;bottom:-1px;left:0;width:0}.wrap{max-width:1290px;margin:auto;padding:48px 4vw 30px}.eyebrow{font:11px/1.5 ui-monospace,monospace;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);margin:0 0 20px}.hero{display:grid;grid-template-columns:1fr 1.02fr;gap:36px;align-items:start;padding-bottom:46px}.episode{font:14px ui-monospace,monospace;color:var(--muted);display:flex;align-items:center;gap:15px;margin-bottom:22px}.episode b{font:68px/.9 Georgia,serif;color:var(--accent);font-weight:normal}.hero h1{font:clamp(38px,3.8vw,62px)/1.04 Georgia,serif;letter-spacing:-.045em;font-weight:normal;margin:0 0 25px}.deck{font-size:17px;line-height:1.7;color:var(--muted);max-width:580px;margin:0 0 25px}.watch{display:inline-flex;gap:10px;align-items:center;font-size:12px;color:var(--teal);font-weight:650}.watch i{display:inline-grid;place-items:center;width:28px;height:28px;border:1px solid var(--teal);border-radius:50%;font-style:normal}.readtime{font:11px ui-monospace,monospace;margin-top:24px;color:var(--muted)}.figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);overflow:hidden}.fig-head{padding:20px 22px 0}.fig-head .tag{font:10px ui-monospace,monospace;letter-spacing:.13em;color:var(--teal)}.fig-head h2{font:23px/1.15 Georgia,serif;margin:10px 0}.fig-head p{font-size:12px;color:var(--muted);margin:0}.map{position:relative;height:320px;margin:8px 14px 0;background-image:radial-gradient(#c7d1c6 .7px,transparent .7px);background-size:14px 14px}.map svg{width:100%;height:100%;position:absolute;inset:0;overflow:visible}.edge{stroke:#8ea99c;stroke-width:.4;fill:none}.edge.active{stroke:var(--accent);stroke-width:.65}.node{position:absolute;transform:translate(-50%,-50%);width:28%;min-height:48px;border:1px solid #a7bbae;border-radius:7px;background:var(--card);color:var(--ink);font-size:11px;font-weight:650;line-height:1.3;padding:9px 5px;box-shadow:0 3px 5px #18312e08}.node:hover{border-color:var(--accent);background:#f8ecdf}.node[aria-pressed=true]{background:var(--accent);color:#fff;border-color:var(--accent)}.node-detail{min-height:118px;padding:15px 20px 17px;border-top:1px solid var(--line);background:var(--soft)}.node-detail strong{font-size:12px;color:var(--teal)}.node-detail p{font-size:12px;line-height:1.6;margin:5px 0 0}.fig-source{padding:10px 20px;border-top:1px solid var(--line);font-size:10px;color:var(--muted)}.cite{font:11px/1.6 ui-monospace,monospace;color:var(--teal);white-space:nowrap}.jumpbar{display:flex;gap:9px;flex-wrap:wrap;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:15px 0;margin-bottom:42px}.jumpbar a{font:11px ui-monospace,monospace;text-decoration:none;padding:6px 12px;border:1px solid var(--line);border-radius:30px}.jumpbar a:hover{background:var(--soft)}section{margin-bottom:48px}.section-head{display:flex;align-items:baseline;gap:20px;margin-bottom:23px}.section-head .kicker{font:11px ui-monospace,monospace;color:var(--accent)}h2{font:32px/1.15 Georgia,serif;font-weight:normal;margin:0}h3{line-height:1.3}.learnings{counter-reset:lessons;display:grid;grid-template-columns:1fr 1fr;column-gap:38px}.learning{padding:22px 0;border-top:1px solid var(--line);position:relative}.learning:last-child{grid-column:1/-1;max-width:760px}.learning h3{font-size:17px;margin:0 0 10px;padding-left:35px}.learning h3:before{counter-increment:lessons;content:"0" counter(lessons);position:absolute;left:0;color:var(--accent);font:12px/1.6 ui-monospace,monospace}.learning p{font-size:14px;color:var(--muted);margin:0 0 12px}.learning .cite{margin-left:35px}.method-grid{display:grid;grid-template-columns:1.15fr 1fr;gap:32px}.method-grid>div{min-width:0}.table-box{overflow-x:auto;border:1px solid var(--line);border-radius:9px;background:var(--card)}table{border-collapse:collapse;width:100%;font-size:12px;text-align:left;min-width:320px}th{font:10px/1.6 ui-monospace,monospace;text-transform:uppercase;letter-spacing:.05em;background:var(--soft)}th,td{padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:top}td:first-child{font-weight:650}tr:last-child td{border-bottom:0}.subheading{font-size:15px;margin:0 0 16px}.flow{list-style:none;padding:0;margin:0;counter-reset:flow}.flow li{position:relative;padding:0 0 23px 39px;font-size:13px;line-height:1.4;min-height:47px}.flow li:before{counter-increment:flow;content:counter(flow);display:grid;place-items:center;position:absolute;left:0;top:-2px;width:24px;height:24px;border:1px solid var(--teal);color:var(--teal);font:11px ui-monospace,monospace;border-radius:50%;background:var(--paper);z-index:1}.flow li:not(:last-child):after{content:"↓";position:absolute;top:22px;left:7px;color:#7e9a8c;font-size:15px}.case{background:var(--ink);color:var(--paper);border-radius:12px;padding:32px}.case .eyebrow{color:#efb79d;margin-bottom:14px}.case h2{max-width:800px}.case .problem{color:#c5d2c9;font-size:15px;margin:18px 0 25px;max-width:850px}.case-grid{display:grid;grid-template-columns:1fr 1fr;gap:25px}.case-grid>div{border-top:1px solid #49645b;padding-top:18px}.case-grid h3{font:11px ui-monospace,monospace;letter-spacing:.1em;color:#efb79d;margin:0 0 10px}.case-grid p{font-size:14px;color:#e3e8df;margin:0}.case .why{font-size:13px;color:#bbd4c3;border-left:2px solid #8bbb9d;margin:25px 0 18px;padding-left:15px}.case .cite{color:#c0dbcb}.practice{display:grid;grid-template-columns:1fr 1.6fr;gap:40px;border-top:1px solid var(--line);padding-top:28px}.practice p{font-size:13px;color:var(--muted)}.checks{display:grid;gap:10px}.check{display:flex;gap:12px;align-items:flex-start;font-size:13px;padding:14px 16px;background:var(--card);border:1px solid var(--line);border-radius:7px;cursor:pointer}.check input{width:18px;height:18px;flex-shrink:0;accent-color:var(--teal);margin-top:2px}.check:has(input:checked){background:var(--soft);border-color:#96b8a0}.check:has(input:checked) span{color:var(--teal)}.check-status{font:11px ui-monospace,monospace;color:var(--teal);margin-top:10px}.source-note{font-size:11px;color:var(--muted);border-top:1px solid var(--line);padding-top:20px;line-height:1.7}.source-note strong{color:var(--ink)}.page-nav{display:flex;justify-content:space-between;gap:15px;margin-top:30px}.page-nav a{max-width:45%;text-decoration:none}.page-nav small{font:10px ui-monospace,monospace;color:var(--muted);display:block;margin-bottom:5px}.page-nav span{font-size:14px}.page-nav a:last-child{text-align:right}.footer{font:10px/1.7 ui-monospace,monospace;padding:30px 0 0;color:var(--muted)}dialog{width:min(500px,90vw);padding:28px;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:12px;box-shadow:0 25px 80px #0004}dialog::backdrop{background:#18312e99}dialog h2{font-size:26px}dialog p,dialog label{font-size:13px}dialog textarea{width:100%;min-height:96px;border:1px solid var(--line);padding:12px;background:var(--paper);color:var(--ink);border-radius:5px;font-size:12px}dialog .actions{margin-top:18px;flex-wrap:wrap}.status{position:fixed;bottom:22px;right:22px;max-width:min(400px,90vw);background:var(--ink);color:var(--paper);padding:12px 20px;border-radius:7px;box-shadow:var(--shadow);z-index:80;font-size:12px}.status:empty{display:none}.calc{padding:25px;border:1px solid var(--line);background:var(--card);border-radius:10px}.calc p{font-size:13px;color:var(--muted)}.calc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:15px}.calc label{font-size:11px;display:block;color:var(--muted);margin:10px 0 4px}.calc h3{font:12px ui-monospace,monospace;color:var(--teal)}.calc input{width:100%;padding:9px 10px;border:1px solid var(--line);border-radius:5px;color:var(--ink);background:var(--paper);font-size:13px}.calc input:invalid{border-color:var(--accent)}.calc-result{margin-top:20px;display:flex;align-items:center;justify-content:space-between;gap:20px;padding-top:20px;border-top:1px solid var(--line)}.calc-result output{font:30px Georgia,serif;color:var(--accent)}.calc-result small{display:block;color:var(--muted);font-size:10px}.cost-bar{display:flex;height:12px;overflow:hidden;border-radius:3px;margin-top:18px;background:var(--soft)}.cost-bar span{min-width:0;transition:width .2s}.cost-bar span:nth-child(1){background:var(--teal)}.cost-bar span:nth-child(2){background:var(--accent)}.cost-bar span:nth-child(3){background:#a57f37}.cost-bar span:nth-child(4){background:#709ea1}.calc-legend{font:10px ui-monospace,monospace;margin-top:10px;line-height:1.8;color:var(--muted)}.index-hero{max-width:850px;padding:12px 0 30px}.index-hero h1{font:clamp(45px,6vw,82px)/.98 Georgia,serif;letter-spacing:-.045em;font-weight:normal;margin:0 0 25px}.index-hero .deck{max-width:700px}.stats{display:flex;gap:28px;flex-wrap:wrap;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:22px 0;margin:5px 0 35px;font:11px ui-monospace,monospace;color:var(--muted)}.stats b{color:var(--accent);font-weight:normal;font-size:22px;margin-right:7px}.episode-list{display:grid;grid-template-columns:1fr 1fr;gap:16px}.episode-card{display:block;text-decoration:none;padding:25px;background:var(--card);border:1px solid var(--line);border-radius:9px;transition:transform .15s,border-color .15s}.episode-card:hover{transform:translateY(-3px);border-color:var(--teal)}.episode-card .card-top{display:flex;justify-content:space-between;font:10px ui-monospace,monospace;color:var(--muted);margin-bottom:22px}.episode-card .card-top b{color:var(--accent);font-size:17px;font-weight:normal}.episode-card h2{font-size:26px;margin-bottom:12px}.episode-card p{font-size:13px;color:var(--muted);margin:0 0 20px}.episode-card .open{font:11px ui-monospace,monospace;color:var(--teal)}.index-intro{display:grid;grid-template-columns:1fr 1fr;gap:25px;margin:42px 0}.index-intro p{font-size:14px;color:var(--muted)}
@media(min-width:1550px){.hero h1{font-size:64px}.wrap{padding-top:60px}}
@media(max-width:1150px){.rail{width:220px;padding:25px 20px}.shell{margin-left:220px}.hero{grid-template-columns:1fr;gap:25px}.hero-copy{max-width:750px}.hero h1{font-size:52px}.figure{max-width:700px}.map{height:330px}.node{font-size:12px}.method-grid{grid-template-columns:1fr}.practice{grid-template-columns:1fr;gap:12px}.hero .deck{max-width:700px}}
@media(max-width:760px){html{scroll-padding-top:80px}.rail{display:none;top:65px;bottom:0;width:270px;padding-top:20px}.rail.is-open{display:flex}.shell{margin-left:0}.topbar{height:65px;padding:10px 20px}.mobile-menu{display:inline-flex}.crumb{display:none}.wrap{padding:32px 22px 25px}.hero h1{font-size:49px}.hero{padding-bottom:30px}.episode{margin-bottom:16px}.episode b{font-size:54px}.deck{font-size:16px}.eyebrow{font-size:10px}.learnings{grid-template-columns:1fr}.learning:last-child{grid-column:auto}.case{padding:25px}.case-grid{grid-template-columns:1fr;gap:22px}.section-head{gap:12px}h2{font-size:29px}.episode-list{grid-template-columns:1fr}.index-intro{grid-template-columns:1fr}.calc-grid{grid-template-columns:1fr 1fr}.map{height:310px;margin-left:8px;margin-right:8px}.node{font-size:11px}.fig-head{padding:20px 18px 0}.node-detail{min-height:120px}.btn{padding:8px 11px;font-size:11px}.topbar .download{font-size:10px}.index-hero h1{font-size:57px}.page-nav span{font-size:12px}.stats{gap:20px}}
@media(max-width:360px){.wrap{padding-left:16px;padding-right:16px}.topbar{padding-left:14px;padding-right:14px}.hero h1{font-size:42px}.node{font-size:10px;min-height:44px}.map{height:300px}.fig-head h2{font-size:21px}.index-hero h1{font-size:48px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
@media print{.rail,.topbar,.jumpbar,.page-nav,.actions,.status,.check-status{display:none!important}.shell{margin:0}.wrap{padding:0}.hero{grid-template-columns:1fr 1fr;gap:20px}.hero h1{font-size:36px}.map{height:260px}.figure,.case,.learning,.practice{break-inside:avoid;box-shadow:none}.case{background:#fff;color:#18312e;border:1px solid #aaa}.case p,.case .why,.case-grid p,.case .cite{color:#18312e}.node{font-size:10px}.node-detail{min-height:0}.deck{font-size:13px}body{font-size:12px}.learning p{font-size:12px}.learnings{gap:20px}.episode-list{grid-template-columns:1fr 1fr}.episode-card{break-inside:avoid}.footer{padding:15px 0}}
'''

CSS += '''
.detail-intro{font-size:13px;color:var(--muted);max-width:850px;margin:-8px 0 25px}.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}.detail-card{min-width:0;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:25px}.detail-number{font:10px ui-monospace,monospace;letter-spacing:.1em;color:var(--accent)}.detail-card h3{font:24px/1.2 Georgia,serif;margin:12px 0}.detail-card p{font-size:14px;color:var(--muted);margin:0 0 20px}.detail-cite{display:inline-block;font:11px/1.7 ui-monospace,monospace;color:var(--teal);margin-top:18px;overflow-wrap:anywhere}.detail-card pre{white-space:pre-wrap;overflow-wrap:anywhere;background:var(--soft);border-radius:6px;padding:16px;font:12px/1.7 ui-monospace,monospace;margin:0}.detail-flow{padding:0;list-style:none;counter-reset:detail;display:grid;gap:10px;margin:0}.detail-flow li{counter-increment:detail;position:relative;font-size:13px;background:var(--soft);border-left:2px solid var(--teal);padding:12px 14px 12px 36px}.detail-flow li:before{content:counter(detail);position:absolute;left:12px;font:11px/1.9 ui-monospace,monospace;color:var(--teal)}.detail-card td,.detail-card th{padding:10px 12px}.detail-grid .detail-card:last-child:nth-child(odd){grid-column:1/-1}
@media(max-width:1150px){.detail-grid{grid-template-columns:1fr}}@media(max-width:760px){.detail-card{padding:20px}.detail-card h3{font-size:23px}}@media print{.detail-grid{grid-template-columns:1fr}.detail-card{break-inside:avoid}}
'''

JS = '''
const $=s=>document.querySelector(s);
const tell=message=>{const status=$('#status');status.textContent=message;clearTimeout(window.noticeTimer);window.noticeTimer=setTimeout(()=>status.textContent='',4500)};
const sourceFile=()=>new File(['<!doctype html>\\n'+document.documentElement.outerHTML],document.body.dataset.file,{type:'text/html'});
function download(){const url=URL.createObjectURL(sourceFile());const link=document.createElement('a');link.href=url;link.download=document.body.dataset.file;document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),30000);tell('HTML download started. Keep the course files together for episode navigation.')}
$('#download').addEventListener('click',download);
const host=location.hostname;
const privateHost=/^(localhost|127\\.|0\\.|10\\.|192\\.168\\.|172\\.(1[6-9]|2\\d|3[01])\\.|\\[?::1\\]?)/.test(host)||/\\.(local|internal)$/.test(host);
$('#share').addEventListener('click',async()=>{const caption=document.title+' — visual learning notes from Peace Of Code.';try{if(/^https?:$/.test(location.protocol)&&!privateHost){if(navigator.share){await navigator.share({title:document.title,text:caption,url:location.href});return}await navigator.clipboard.writeText(location.href);tell('Page link copied.');return}const file=sourceFile();if(navigator.canShare&&navigator.canShare({files:[file]})){await navigator.share({title:document.title,text:caption,files:[file]});return}download();$('#caption').value=caption+' Open the attached HTML in a browser.';$('#share-dialog').showModal()}catch(error){if(error.name==='AbortError')return;if(/^https?:$/.test(location.protocol)&&!privateHost){$('#caption').value=location.href}else{download();$('#caption').value=caption+' Open the attached HTML in a browser.'}$('#share-dialog').showModal()}});
$('#copy-caption').addEventListener('click',async()=>{try{await navigator.clipboard.writeText($('#caption').value);tell('Caption copied.')}catch{$('#caption').focus();$('#caption').select();tell('Caption selected. Copy it with your keyboard.')}});
$('#close-share').addEventListener('click',()=>$('#share-dialog').close());
$('#menu').addEventListener('click',()=>{const open=$('.rail').classList.toggle('is-open');$('#menu').setAttribute('aria-expanded',String(open))});
document.querySelectorAll('.map .node').forEach(button=>button.addEventListener('click',()=>{const figure=button.closest('figure');figure.querySelectorAll('.node').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));figure.querySelector('.detail-title').textContent=button.textContent;figure.querySelector('.detail-text').textContent=button.dataset.detail;figure.querySelectorAll('.edge').forEach(edge=>edge.classList.toggle('active',edge.dataset.from===button.dataset.id||edge.dataset.to===button.dataset.id))}));
const checks=[...document.querySelectorAll('.check input')];const key='architect-pro-'+document.body.dataset.episode;
let storageOK=true;try{const saved=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(saved))checks.forEach((c,i)=>c.checked=saved[i]===true)}catch{storageOK=false}
function updateChecks(){const status=$('#check-status');if(status)status.textContent=checks.filter(c=>c.checked).length+' / '+checks.length+' actions checked'+(storageOK?' · saved in this browser':' · for this session');}
checks.forEach(c=>c.addEventListener('change',()=>{try{localStorage.setItem(key,JSON.stringify(checks.map(x=>x.checked)))}catch{storageOK=false}updateChecks()}));updateChecks();
function progress(){const available=document.documentElement.scrollHeight-innerHeight;$('.progress').style.width=(available>0?Math.min(100,scrollY/available*100):0)+'%'}addEventListener('scroll',progress,{passive:true});addEventListener('resize',progress);progress();
const calculator=$('#calculator');if(calculator){const inputs=[...calculator.querySelectorAll('input')];const output=$('#cost-total');function recalc(){if(inputs.some(i=>!i.validity.valid||i.value.trim()==='')){output.textContent='Enter valid values';$('#cost-summary').textContent='All values must be nonnegative numbers.';calculator.querySelectorAll('.cost-bar span').forEach(s=>s.style.width='0%');return}const costs=[0,1,2,3].map(i=>Number($('#tokens-'+i).value)*Number($('#rate-'+i).value)/1e6);const total=costs.reduce((a,b)=>a+b,0);output.textContent='$'+total.toFixed(5);$('#cost-summary').textContent=total>0?'Largest bucket: '+['fresh input','output','cache write','cache read'][costs.indexOf(Math.max(...costs))]+'. Illustrative cost per request.':'All buckets are zero.';calculator.querySelectorAll('.cost-bar span').forEach((s,i)=>s.style.width=(total>0?costs[i]/total*100:0)+'%');$('#cost-legend').textContent=costs.map((c,i)=>['Fresh','Output','Write','Read'][i]+': $'+c.toFixed(5)).join(' · ')}inputs.forEach(i=>i.addEventListener('input',recalc));$('#reset-cost').addEventListener('click',()=>{inputs.forEach(i=>i.value=i.defaultValue);recalc()});recalc()}
'''


def rail(current):
    links = ''.join(f'<a href="{filename(d)}"'+(' aria-current="page"' if d['episode']==current else '')+f'><span>{d["episode"]:02d}</span>{e(d["title"])}</a>' for d in DATA)
    return f'''<aside class="rail" id="course-navigation"><a class="brand" href="index.html"><small>ARCHITECTURE / FIELD NOTES</small><strong>Build with<br>better judgment.</strong></a><p class="course">Claude Architect Professional<br>A visual learning companion</p><nav aria-label="Episodes">{links}</nav><div class="rail-foot">11 episodes · separate HTML pages<br>Based on Peace Of Code’s lessons.<br><a href="{PLAYLIST}" target="_blank" rel="noopener">Open the source playlist ↗</a></div></aside>'''


def frame(title, episode, file, content):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{e(title)} — transcript-grounded visual learning notes, diagrams, and practical takeaways."><title>{e(title)} | Architecture Field Notes</title><style>{CSS}</style></head>
<body data-episode="{episode}" data-file="{file}"><a class="skip" href="#main">Skip to learning notes</a>{rail(episode)}<div class="shell"><header class="topbar"><button class="btn mobile-menu" id="menu" aria-controls="course-navigation" aria-expanded="false">☰ Episodes</button><a class="crumb" href="index.html">FIELD NOTES / {'THE COURSE' if not episode else f'EPISODE {episode:02d}'}</a><div class="actions"><button class="btn download" id="download">Download HTML</button><button class="btn primary" id="share">Share ↗</button></div><div class="progress" aria-hidden="true"></div></header><main class="wrap" id="main">{content}<footer class="footer">ARCHITECTURE FIELD NOTES · Learning synthesis, 11 October 2026<br>Self-contained pages. No network needed for the notes, diagrams, or tools. Source videos and repository links require internet.</footer></main></div><dialog id="share-dialog" aria-labelledby="share-title"><h2 id="share-title">Share the learning page</h2><p>For a local preview, share the downloaded HTML file. To share the whole course, use the course ZIP and keep its files together.</p><label for="caption">Suggested caption</label><textarea id="caption" readonly></textarea><div class="actions"><button class="btn primary" id="copy-caption">Copy caption</button><button class="btn" id="close-share">Close</button></div></dialog><div class="status" id="status" role="status" aria-live="polite"></div><script>{JS}</script></body></html>'''


def diagram(d):
    nodes = d['nodes']
    edges = ''
    for start, end in d['edges']:
        x1,y1=nodes[start][2:];x2,y2=nodes[end][2:]
        # Stop connectors at node edges so the arrowhead remains legible.
        if abs(x2-x1)>abs(y2-y1):
            direction=1 if x2>x1 else -1
            x1+=direction*14;x2-=direction*14
        else:
            direction=1 if y2>y1 else -1
            y1+=direction*8;y2-=direction*8
        edges+=f'<path class="edge" data-from="{start}" data-to="{end}" d="M{x1} {y1} L{x2} {y2}" marker-end="url(#arrow)"/>'
    buttons=''.join(f'<button class="node" style="left:{x}%;top:{y}%" data-id="{i}" data-detail="{e(detail,quote=True)}" aria-pressed="{str(i==0).lower()}">{e(label)}</button>' for i,(label,detail,x,y) in enumerate(nodes))
    return f'''<figure class="figure"><div class="fig-head"><span class="tag">INTERACTIVE CONCEPT MAP</span><h2>{e(d['diagramTitle'])}</h2><p>{e(d['diagramNote'])}</p></div><div class="map" role="group" aria-label="{e(d['diagramTitle'])}"><svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="2.3" markerHeight="2.3" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M 0 1 L 8 5 L 0 9" fill="none" stroke="#8ea99c" stroke-width="1.5"/></marker></defs>{edges}</svg>{buttons}</div><figcaption><div class="node-detail" aria-live="polite"><strong class="detail-title">{e(nodes[0][0])}</strong><p class="detail-text">{e(nodes[0][1])}</p></div><div class="fig-source">Visual synthesis of the lesson · {cite(d,d['diagramTime'])}</div></figcaption></figure>'''


def cost_tool():
    buckets=[('Fresh input',3000,3),('Output',500,15),('Cache write',0,3.75),('Cache read',2800,.3)]
    controls=''.join(f'<div><h3>{name}</h3><label for="tokens-{i}">Tokens per request</label><input id="tokens-{i}" type="number" min="0" max="1000000000" step="1" value="{tokens}"><label for="rate-{i}">$ per million tokens</label><input id="rate-{i}" type="number" min="0" max="1000000" step="any" value="{rate}"></div>' for i,(name,tokens,rate) in enumerate(buckets))
    return f'''<section id="cost-lab"><div class="section-head"><span class="kicker">05 / EXPLORE</span><h2>See which bucket drives cost.</h2></div><div class="calc" id="calculator"><p><strong>Editable illustration, not live provider prices.</strong> Change counts or rates to compare the four buckets. Enter uncached input only in Fresh input; cached tokens belong in their own bucket.</p><div class="calc-grid">{controls}</div><div class="calc-result"><div><output id="cost-total" aria-live="polite"></output><small id="cost-summary"></small></div><button class="btn" id="reset-cost">Reset example</button></div><div class="cost-bar" aria-hidden="true"><span></span><span></span><span></span><span></span></div><div class="calc-legend" id="cost-legend"></div><p>Cost = Σ(tokens in each bucket × its rate ÷ 1,000,000). This excludes tool, storage, infrastructure, and review costs; include those when measuring total cost per successful outcome.</p></div></section>'''


def episode_page(d):
    n=d['episode']
    learnings=''.join(f'<article class="learning"><h3>{e(title)}</h3><p>{e(body)}</p>{cite(d,t)}</article>' for title,body,t in d['learnings'])
    table='<thead><tr>'+''.join(f'<th scope="col">{e(s)}</th>' for s in d['tableHeads'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{e(s)}</td>' for s in row)+'</tr>' for row in d['tableRows'])+'</tbody>'
    flow=''.join(f'<li>{e(s)}</li>' for s in d['flow'])
    checks=''.join(f'<label class="check"><input type="checkbox" aria-label="{e(s)}"><span>{e(s)}</span></label>' for s in d['checklist'])
    prev=DATA[n-2] if n>1 else None
    nxt=DATA[n] if n<len(DATA) else None
    prevlink=f'<a href="{filename(prev)}"><small>← PREVIOUS / {n-1:02d}</small><span>{e(prev["title"])}</span></a>' if prev else '<a href="index.html"><small>← COURSE INDEX</small><span>Explore all eleven lessons</span></a>'
    nextlink=f'<a href="{filename(nxt)}"><small>NEXT / {n+1:02d} →</small><span>{e(nxt["title"])}</span></a>' if nxt else '<a href="index.html"><small>COURSE INDEX →</small><span>Return to the full learning path</span></a>'
    detail_words = sum(len(str(c).split()) for c in DETAILS[str(n)])
    words=detail_words+sum(len(x.split()) for x in [d['deck'],d['caseProblem'],d['caseBefore'],d['caseAfter'],d['caseWhy']]+[x[1] for x in d['learnings']])
    content=f'''<p class="eyebrow">Peace Of Code / Claude Architect Professional</p><section class="hero" aria-labelledby="lesson-title"><div class="hero-copy"><div class="episode"><b>{n:02d}</b><span>{e(d['theme'])}<br>EPISODE {n:02d} OF 11</span></div><h1 id="lesson-title">{e(d['headline'])}</h1><p class="deck">{e(d['deck'])}</p><a class="watch" href="https://youtu.be/{d['video']}" target="_blank" rel="noopener"><i aria-hidden="true">▶</i> Watch: {e(d['title'])} ↗</a><p class="readtime">≈ {max(4,round(words/150))} MIN READ + EXPLORATION · SOURCE-LINKED</p></div>{diagram(d)}</section><nav class="jumpbar" aria-label="On this page"><a href="#takeaways">The takeaways</a><a href="#method">Decision guide</a><a href="#case">Worked example</a><a href="#practice">Apply it</a><a href="#slide-details">Additional details</a>{'<a href="#cost-lab">Cost explorer</a>' if n==11 else ''}</nav><section id="takeaways"><div class="section-head"><span class="kicker">01 / UNDERSTAND</span><h2>Five ideas worth keeping.</h2></div><div class="learnings">{learnings}</div></section><section id="method"><div class="section-head"><span class="kicker">02 / DECIDE</span><h2>Make the tradeoff visible.</h2></div><div class="method-grid"><div><h3 class="subheading">{e(d['tableTitle'])}</h3><div class="table-box"><table>{table}</table></div></div><div><h3 class="subheading">{e(d['flowTitle'])}</h3><ol class="flow" aria-label="{e(d['flowTitle'])}">{flow}</ol></div></div></section><section class="case" id="case"><p class="eyebrow">03 / WORKED EXAMPLE · FROM THE LESSON</p><h2>{e(d['caseTitle'])}</h2><p class="problem">{e(d['caseProblem'])}</p><div class="case-grid"><div><h3>THE TEMPTING MOVE</h3><p>{e(d['caseBefore'])}</p></div><div><h3>THE BETTER-FITTING MOVE</h3><p>{e(d['caseAfter'])}</p></div></div><p class="why">{e(d['caseWhy'])}</p>{cite(d,d['caseTime'])}</section><section class="practice" id="practice"><div><p class="eyebrow">04 / APPLY IT</p><h2>Take this into<br>the next design review.</h2><p>Check an action after you have applied it. Progress is stored locally when the browser allows it.</p></div><div><div class="checks">{checks}</div><div class="check-status" id="check-status" aria-live="polite"></div></div></section>{cost_tool() if n==11 else ''}{detail_section(d)}<aside class="source-note"><strong>Source & scope.</strong> Based on the complete available English auto-generated transcript of Peace Of Code’s Episode {n:02d}. Additional details are grounded in the pinned companion repository: matching decks for Episodes 01–08 and 10, walkthrough/code for Episode 09, and clearly labeled cross-episode connections for Episode 11. These are selected learning notes, not an exhaustive transcript or slide reproduction. The prose, diagrams, and decision guides are original learning syntheses; timestamp links open the supporting lesson moments. This is a companion to a community course, not official exam documentation.<br><strong>Keep in mind:</strong> {e(d['caveat'])}</aside><nav class="page-nav" aria-label="Adjacent episodes">{prevlink}{nextlink}</nav>'''
    return frame(f'Episode {n:02d} — {d["title"]}',n,filename(d),content)


def index_page():
    cards=''.join(f'<a class="episode-card" href="{filename(d)}"><div class="card-top"><b>EP {d["episode"]:02d}</b><span>{e(d["theme"]).upper()}</span></div><h2>{e(d["title"])}</h2><p>{e(d["headline"])}</p><span class="open">Open the learning page →</span></a>' for d in DATA)
    content=f'''<p class="eyebrow">A visual companion to Peace Of Code’s course</p><section class="index-hero"><h1>From model calls<br>to sound architecture.</h1><p class="deck">Eleven episodes. Eleven separate learning pages. Build the judgment to choose a pattern, shape context, retrieve evidence, evaluate quality, and operate within budget.</p><a class="btn primary" href="{filename(DATA[0])}">Start with Episode 01 →</a></section><div class="stats"><span><b>11</b>EPISODE PAGES</span><span><b>11</b>INTERACTIVE MAPS</span><span><b>55</b>CORE TAKEAWAYS</span><span><b>39</b>SOURCED DETAIL CARDS</span><span><b>146</b>SLIDES REVIEWED</span><span><b>0</b>EXTERNAL DEPENDENCIES</span></div><section aria-labelledby="path-title"><div class="section-head"><span class="kicker">YOUR LEARNING PATH</span><h2 id="path-title">Start at 01. Follow the decisions.</h2></div><div class="episode-list">{cards}</div></section><div class="index-intro"><div><h2>Read. Explore. Apply.</h2><p>Each page turns one episode into five concrete lessons, a selectable concept map, a comparison table, a process flow, a worked example, and three actions for your next design review. Episode 11 includes an editable cost explorer. Additional detail sections include worked arithmetic, decision branches, diagnostic tables, and the evaluation demo’s exact field rules.</p></div><div><h2>Keep the source close.</h2><p>Timestamp links take you back to supporting moments. The notes distinguish scenario numbers from measured results and avoid treating changing provider details as current specifications. This is an independent learning companion, not official certification guidance.</p></div></div><aside class="source-note"><strong>Coverage.</strong> Episodes 01–11 from the supplied <a href="{PLAYLIST}" target="_blank" rel="noopener">YouTube playlist</a>. The introductory video is excluded so the course begins at Episode 01 as requested. All eleven pages use available auto-generated transcripts. The update also reviews all 146 slides in the nine available decks and the Episode 06/09 companion code. Episode 09 has walkthrough files but no deck; Episode 11 has no folder in this snapshot, so its added details explicitly connect earlier material. These are selected learning notes, not exhaustive coverage of every video or slide. <a href="{REPO}/tree/{COMMIT}" target="_blank" rel="noopener">Pinned deck and code sources ↗</a>. Model/API claims, prices, exam weights, and scenario performance figures are not presented as verified current specifications.<br><strong>Offline use.</strong> Extract the course ZIP and open index.html. Keep all twelve HTML files together for navigation. Each episode’s notes and diagrams work independently; the source videos require internet. Download HTML saves the current page.</aside>'''
    return frame('Claude Architect Professional — The Learning Path',0,'index.html',content)


def verify():
    assert [d['episode'] for d in DATA]==list(range(1,12))
    assert len({d['video'] for d in DATA})==11
    assert set(DETAILS)=={str(i) for i in range(1,12)}
    assert sum(SLIDE_COUNTS.values())==146
    for episode, cards in DETAILS.items():
        assert len(cards)>=3
        for card in cards:
            ep=card['source_episode']
            assert card['title'] and card['body']
            assert card.get('slides') or card.get('file')
            if card.get('slides'):
                assert ep in SLIDE_COUNTS
                assert all(1<=s<=SLIDE_COUNTS[ep] for s in card['slides'])
            if card.get('file'):
                assert card['file'] in {'episode 6/rag_pipeline.py','episode 9/WALKTHROUGH.md','episode 9/run_eval.py','episode 9/golden.jsonl'}
            if card.get('table'):
                assert all(len(row)==len(card['table'][0]) for row in card['table'])
        if int(episode) in SLIDE_COUNTS:
            assert all(c['source_episode']==int(episode) for c in cards)
    assert all('file' in c for c in DETAILS['9'])
    assert all(c['source_episode']!=11 for c in DETAILS['11'])
    for d in DATA:
        assert re.fullmatch(r'[A-Za-z0-9_-]{11}',d['video'])
        assert len(d['learnings'])==5 and len(d['checklist'])==3
        assert all(0<=a<len(d['nodes']) and 0<=b<len(d['nodes']) for a,b in d['edges'])
        for t in [d['diagramTime'],d['caseTime']]+[x[2] for x in d['learnings']]:
            assert stamp(t)>0
    pages=list(ROOT.glob('*.html'))
    assert len(pages)==12
    for page in pages:
        text=page.read_text()
        assert text.startswith('<!doctype html>') and 'REPLACE' not in text
        ids=re.findall(r'\bid="([^"]+)"',text)
        assert len(ids)==len(set(ids)),f'Duplicate IDs in {page.name}'
        for href in re.findall(r'href="([^"]+)"',text):
            if href.startswith('#'):
                assert href[1:] in ids,(page.name,href)
            elif not href.startswith('https://'):
                assert (ROOT/href).is_file(),(page.name,href)
        assert not re.search(r'<(?:script|link)[^>]+(?:src|href)="https?://',text)
        assert 'id="share"' in text and 'id="download"' in text
        if page.name!='index.html':
            assert 'id="slide-details"' in text and COMMIT in text
    # Four billing categories are disjoint; the default illustrative result is $0.01734.
    assert abs((3000*3+500*15+0*3.75+2800*.3)/1e6-.01734)<1e-10
    assert round((1-(2800*.1+3000)/5800)*100,1)==43.4


if __name__=='__main__':
    for episode in DATA:
        (ROOT/filename(episode)).write_text(episode_page(episode))
    (ROOT/'index.html').write_text(index_page())
    verify()
    with zipfile.ZipFile(ROOT/'claude-architect-pro-learning-pages.zip','w',zipfile.ZIP_DEFLATED) as package:
        for page in sorted(ROOT.glob('*.html')):
            package.write(page,page.name)
    print('Built and checked 11 episode pages + index; packaged all 12 HTML files.')
