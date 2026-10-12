'use strict';
const ExamCore = {
  remaining: (deadline, now = Date.now()) => Math.max(0, Math.ceil((deadline - now) / 1000)),
  complete: (q, a) => Array.isArray(a) && a.length === q.select,
  correct: (q, a) => Array.isArray(a) && a.length === q.select && new Set(a).size === a.length && a.every(i => Number.isInteger(i) && q.options[i]?.correct === true),
  grade(questions, answers) { return questions.map(q => ({id:q.id, domain:q.domain, correct:this.correct(q,answers[q.id]||[]), complete:this.complete(q,answers[q.id]||[])})); },
  validate(s, data) {
    if (!s || s.version !== data.version || !Number.isFinite(s.started) || s.started <= 0 || s.deadline !== s.started + data.minutes*60000 || !Number.isInteger(s.index) || s.index < 0 || s.index >= data.questions.length || !s.answers || typeof s.answers !== 'object' || Array.isArray(s.answers) || !Array.isArray(s.flagged) || new Set(s.flagged).size !== s.flagged.length || !(s.submitted === null || Number.isFinite(s.submitted) && s.submitted >= s.started)) return false;
    const ids = new Set(data.questions.map(q => q.id));
    if (s.flagged.some(id => !ids.has(id)) || Object.keys(s.answers).some(id => !ids.has(id))) return false;
    return data.questions.every(q => {
      const a = s.answers[q.id];
      return a === undefined || Array.isArray(a) && a.length <= q.select && new Set(a).size === a.length && a.every(i => Number.isInteger(i) && i >= 0 && i < q.options.length);
    });
  },
  choose(q, a, i, checked) {
    if (!Number.isInteger(i) || i < 0 || i >= q.options.length) return a;
    if (q.select === 1) return checked ? [i] : [];
    if (!checked) return a.filter(x => x !== i);
    return a.includes(i) || a.length >= q.select ? a : [...a,i].sort((x,y)=>x-y);
  }
};
if (typeof module !== 'undefined') module.exports = ExamCore;
if (typeof document !== 'undefined') {
  const data = JSON.parse(document.getElementById('exam-data').textContent);
  const questions = data.order.map(i => data.questions[i]);
  const key = 'ccarp-mock-' + data.version;
  const $ = id => document.getElementById(id);
  const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const letter = i => String.fromCharCode(65+i);
  let state = null, storageOK = true;
  try {
    const raw = localStorage.getItem(key);
    if (raw) { const parsed = JSON.parse(raw); if (ExamCore.validate(parsed,data)) state = parsed; else $('storage-note').textContent = 'Saved progress was incompatible and was not loaded.'; }
  } catch (_) { storageOK = false; }
  function save() {
    try { localStorage.setItem(key,JSON.stringify(state)); } catch (_) { storageOK=false; }
    $('save-state').textContent = storageOK ? 'Saved in this browser · timer continues while this page is closed.' : 'Storage unavailable. Keep this tab open; reload may lose progress.';
  }
  function show(id) {
    for (const section of document.querySelectorAll('[data-screen]')) section.hidden=section.id!==id;
    $('top-exam').hidden=id==='welcome'; window.scrollTo({top:0,behavior:'instant'});
  }
  const counts = () => questions.filter(q=>ExamCore.complete(q,state.answers[q.id])).length;
  function updateClock() {
    if (!state || state.submitted!==null) return;
    const seconds=ExamCore.remaining(state.deadline);
    $('clock').textContent=`${String(Math.floor(seconds/60)).padStart(2,'0')}:${String(seconds%60).padStart(2,'0')}`;
    $('clock').classList.toggle('urgent',seconds<=600);
    if (seconds===0) finish();
  }
  function nav() {
    $('answered-count').textContent=`${counts()} / 63 complete`;
    $('question-grid').innerHTML=questions.map((q,i)=>{
      const complete=ExamCore.complete(q,state.answers[q.id]), partial=!complete && (state.answers[q.id]||[]).length>0, flag=state.flagged.includes(q.id);
      return `<button type="button" data-go="${i}" class="nav-q ${complete?'done':''} ${partial?'partial':''} ${flag?'flagged':''}" ${i===state.index?'aria-current="step"':''} aria-label="Question ${i+1}, ${complete?'complete':partial?'partial':'unanswered'}${flag?', flagged':''}">${i+1}${flag?'<span aria-hidden="true">•</span>':''}</button>`;
    }).join('');
  }
  function exhibit(q) {
    if (!q.exhibit) return '';
    return `<div class="table-wrap"><table><caption>Scenario measurements · illustrative</caption><thead><tr>${q.exhibit.headers.map(x=>`<th scope="col">${esc(x)}</th>`).join('')}</tr></thead><tbody>${q.exhibit.rows.map(row=>`<tr>${row.map(v=>`<td>${esc(v)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  }
  function renderQuestion(focus=false) {
    if (state.submitted!==null) return results();
    show('sitting'); const q=questions[state.index], a=state.answers[q.id]||[];
    $('question-number').textContent=`QUESTION ${String(state.index+1).padStart(2,'0')} / 63`;
    $('select-count').textContent=`Select ${q.select===1?'ONE':q.select===2?'TWO':'THREE'} response${q.select>1?'s':''}`;
    // Titles and domain labels are review metadata; hiding them avoids answer cues during the sitting.
    $('question-stem').textContent=q.stem; $('exhibit').innerHTML=exhibit(q);
    $('options').innerHTML=q.options.map((o,i)=>`<label class="option ${a.includes(i)?'chosen':''}"><input type="${q.select===1?'radio':'checkbox'}" name="answer" value="${i}" ${a.includes(i)?'checked':''}><span class="option-letter" aria-hidden="true">${letter(i)}</span><span>${esc(o.text)}</span></label>`).join('');
    $('selection-status').textContent=`${a.length} of ${q.select} selected${a.length===q.select?' · complete':''}`;
    const flag=state.flagged.includes(q.id); $('flag').setAttribute('aria-pressed',String(flag)); $('flag').textContent=flag?'Flagged for review':'Flag for review';
    $('previous').disabled=state.index===0; $('next').textContent=state.index===62?'Review sitting →':'Next question →'; nav();updateClock();
    if (focus && state.submitted===null) $('question-heading').focus();
  }
  function go(i) { updateClock();if(state.submitted!==null)return;state.index=i;save();renderQuestion(true); }
  function reviewSitting() {
    updateClock();if(state.submitted!==null)return;show('overview');
    $('overview-summary').textContent=`${counts()} complete · ${63-counts()} unanswered or incomplete · ${state.flagged.length} flagged. Partial selections receive no credit under this mock’s exact-match scoring.`;
    $('review-list').innerHTML=questions.map((q,i)=>{const a=state.answers[q.id]||[];return `<button class="review-row" data-go="${i}"><strong>Question ${i+1}</strong><span>${ExamCore.complete(q,a)?'Complete':a.length?'Incomplete':'Unanswered'} · ${a.length}/${q.select} selected${state.flagged.includes(q.id)?' · flagged':''}</span></button>`;}).join('');
    $('overview-heading').focus();
  }
  function finish() {
    if (!state || state.submitted!==null)return;
    state.submitted=Date.now();save();if($('submit-dialog').open)$('submit-dialog').close();results();
  }
  const citations = q => q.sources.map(id=>`<a href="${esc(data.sources[id].url)}" target="_blank" rel="noopener">${esc(data.sources[id].title)} ↗</a>`).join(' · ');
  function renderSolutions(filter='all') {
    $('expand-solutions').textContent='Expand explanations';
    const grades=ExamCore.grade(questions,state.answers);
    $('solutions').innerHTML=questions.map((q,i)=>{
      const g=grades[i], a=state.answers[q.id]||[];
      if(filter==='missed'&&g.correct || filter==='flagged'&&!state.flagged.includes(q.id))return '';
      const correct=q.options.flatMap((o,j)=>o.correct?[letter(j)]:[]).join(', ');
      return `<details class="solution"><summary><span class="verdict ${g.correct?'pass':'fail'}">${g.correct?'Correct':'Review'}</span><span>Question ${i+1} · ${esc(q.title)}<small>Domain ${q.domain} · objectives ${q.objectives.join(', ')} · ${q.id}</small></span></summary><div class="solution-body"><p class="stem">${esc(q.stem)}</p>${exhibit(q)}<p><strong>Your response:</strong> ${a.length?a.map(letter).join(', '):'Unanswered'} · <strong>Correct:</strong> ${correct}</p><p class="decision">${esc(q.decision)}</p><ol class="option-rationale">${q.options.map((o,j)=>`<li><b>${letter(j)} · ${o.correct?'Correct':'Distractor'}</b><p>${esc(o.text)}</p><p class="muted">${esc(o.why)}</p></li>`).join('')}</ol><p class="source-links">${citations(q)}</p></div></details>`;
    }).join('')||'<p>No questions match this filter.</p>';
  }
  function results() {
    show('results');const grades=ExamCore.grade(questions,state.answers), score=grades.filter(g=>g.correct).length;
    $('clock').textContent='Submitted';$('clock').classList.remove('urgent');
    $('review').hidden=true;$('top-submit').hidden=true;
    $('raw-score').textContent=`${score} / 63`;$('raw-percent').textContent=`${(score/63*100).toFixed(1)}% raw exact-match score`;
    const elapsed=Math.min(7200,Math.max(0,Math.floor((state.submitted-state.started)/1000)));
    $('result-note').textContent=`${state.submitted>=state.deadline?'Time expired; responses were submitted automatically. ':''}Time used: ${Math.floor(elapsed/60)}m ${elapsed%60}s. ${grades.filter(g=>!g.complete).length} unanswered or incomplete.`;
    $('domain-results').innerHTML=data.domains.map(d=>{const list=grades.filter(g=>g.domain===d.id),n=list.filter(g=>g.correct).length;return `<div class="domain-result"><div><strong>${esc(d.name)}</strong><span>${n}/${list.length} · ${Math.round(n/list.length*100)}%</span></div><progress value="${n}" max="${list.length}" aria-label="${esc(d.name)}: ${n} correct out of ${list.length}"></progress></div>`;}).join('');
    $('solution-filter').value='all';renderSolutions();renderDrills();$('results-heading').focus();
  }
  function renderDrills() {
    $('format-drills').innerHTML=data.drills.map(d=>`<article class="drill" data-drill="${d.id}"><span class="eyebrow">SUPPLEMENTAL · UNSCORED</span><h3>${esc(d.title)}</h3><p>${esc(d.stem)}</p>${d.rows.map((r,i)=>d.type==='matrix'?`<fieldset><legend>${i+1}. ${esc(r.text)}</legend><label><input type="radio" name="${d.id}-${i}" value="Yes"> Yes</label> <label><input type="radio" name="${d.id}-${i}" value="No"> No</label></fieldset>`:`<label class="match-row">${i+1}. ${esc(r.text)}<select data-row="${i}"><option value="">Choose a match</option>${d.choices.map(c=>`<option>${esc(c)}</option>`).join('')}</select></label>`).join('')}<button class="btn" data-check="${d.id}">Check this drill</button><div class="drill-feedback" role="status"></div></article>`).join('');
  }
  $('start').addEventListener('click',()=>{
    if(!state){const now=Date.now();state={version:data.version,started:now,deadline:now+data.minutes*60000,index:0,answers:{},flagged:[],submitted:null};}
    save();
    $('review').hidden=false;$('top-submit').hidden=false;
    if(state.submitted!==null)results();else renderQuestion(true);
  });
  $('options').addEventListener('change',e=>{
    if(!e.target.matches('input')||state.submitted!==null)return;
    updateClock();if(state.submitted!==null)return;
    const q=questions[state.index],i=Number(e.target.value),selected=ExamCore.choose(q,state.answers[q.id]||[],i,e.target.checked);
    if(e.target.checked&&!selected.includes(i)){e.target.checked=false;$('selection-status').textContent=`Select exactly ${q.select}; deselect a response before choosing another.`;return;}
    state.answers[q.id]=selected;save();for(const label of $('options').children)label.classList.toggle('chosen',label.querySelector('input').checked);
    $('selection-status').textContent=`${selected.length} of ${q.select} selected${selected.length===q.select?' · complete':''}`;nav();
  });
  $('flag').addEventListener('click',()=>{updateClock();if(state.submitted!==null)return;const id=questions[state.index].id;state.flagged=state.flagged.includes(id)?state.flagged.filter(x=>x!==id):[...state.flagged,id];save();renderQuestion();});
  $('clear').addEventListener('click',()=>{updateClock();if(state.submitted!==null)return;delete state.answers[questions[state.index].id];save();renderQuestion();});
  $('previous').addEventListener('click',()=>go(state.index-1));$('next').addEventListener('click',()=>state.index===62?reviewSitting():go(state.index+1));
  for(const id of ['question-grid','review-list'])$(id).addEventListener('click',e=>{const b=e.target.closest('[data-go]');if(b)go(Number(b.dataset.go));});
  $('review').addEventListener('click',reviewSitting);$('return-question').addEventListener('click',()=>renderQuestion(true));
  for(const b of document.querySelectorAll('[data-submit]'))b.addEventListener('click',()=>{updateClock();if(state.submitted!==null)return;$('submit-message').textContent=`${counts()} complete; ${63-counts()} unanswered or incomplete. Submit and reveal explanations? This sitting cannot be edited afterward.`;$('submit-dialog').showModal();});
  $('confirm-submit').addEventListener('click',finish);$('cancel-submit').addEventListener('click',()=>$('submit-dialog').close());
  $('solution-filter').addEventListener('change',e=>renderSolutions(e.target.value));
  $('expand-solutions').addEventListener('click',()=>{const list=[...document.querySelectorAll('.solution')],open=list.some(d=>!d.open);list.forEach(d=>d.open=open);$('expand-solutions').textContent=open?'Collapse explanations':'Expand explanations';});
  $('format-drills').addEventListener('click',e=>{
    const b=e.target.closest('[data-check]');if(!b)return;const d=data.drills.find(x=>x.id===b.dataset.check),el=b.closest('.drill');let score=0;
    const lines=d.rows.map((r,i)=>{const selected=d.type==='matrix'?el.querySelector(`input[name="${d.id}-${i}"]:checked`)?.value:el.querySelector(`select[data-row="${i}"]`).value;const ok=selected===r.answer;score+=Number(ok);return `<li><strong>${i+1}. ${ok?'Correct':'Review'} · ${esc(r.answer)}</strong> — ${esc(r.why)}</li>`;}).join('');
    el.querySelector('.drill-feedback').innerHTML=`<p><strong>${score}/${d.rows.length} rows correct</strong> · not part of your 63-question score.</p><ul>${lines}</ul>`;
  });
  $('export').addEventListener('click',()=>{
    const payload={mockVersion:data.version,submittedAt:new Date(state.submitted).toISOString(),answers:state.answers,flagged:state.flagged,results:ExamCore.grade(questions,state.answers)};
    const url=URL.createObjectURL(new Blob([JSON.stringify(payload,null,2)],{type:'application/json'})),a=document.createElement('a');a.href=url;a.download='ccarp-mock-results.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  });
  $('retake').addEventListener('click',()=>$('reset-dialog').showModal());$('cancel-reset').addEventListener('click',()=>$('reset-dialog').close());
  $('confirm-reset').addEventListener('click',()=>{try{localStorage.removeItem(key);}catch(_){}state=null;$('reset-dialog').close();$('start').textContent='Start 120-minute exam';$('storage-note').textContent='';show('welcome');$('welcome-heading').focus();});
  if(state){$('start').textContent=state.submitted!==null?'Open saved results':'Resume timed sitting';$('storage-note').textContent=state.submitted!==null?'A submitted sitting is saved here.':'An in-progress sitting is saved here. Its clock continues while this page is closed.';if(state.submitted===null&&ExamCore.remaining(state.deadline)===0)finish();}
  if(!storageOK)$('storage-note').textContent='Storage unavailable. The exam works in this tab; reload may lose progress.';
  setInterval(updateClock,1000);
}
